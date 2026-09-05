"""Forge V1 structural verification helper.

Checks the filesystem convention from SPEC section 2 + FORGE_SPEC.md IDs
(TASK-008 Agent1), plus git state and KICKOFF freshness (TASK-009 Agent2).
Stdlib only — no dependencies per project rules.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REQUIRED_FILES = [
    "FORGE_SPEC.md",
    "AGENTS.md",
    ".forge/INIT.md",
    ".forge/KICKOFF.md",
    ".forge/rules.md",
    ".forge/state.md",
    ".forge/tasks.md",
    ".forge/taste/preferences.md",
]

REQUIRED_DIRS = [
    ".forge/decisions",
    ".forge/skills",
    ".forge/checkpoints",
]

ID_PATTERN = re.compile(r"^### (FR|NFR|AC)-\d+", re.MULTILINE)

EXPECTED_COUNTS = {"FR": 17, "NFR": 5, "AC": 6}


def repo_root(start: Path | None = None) -> Path:
    """Return repo root (dir containing FORGE_SPEC.md), searching upward."""
    here = (start or Path(__file__)).resolve()
    for candidate in [here, *here.parents]:
        if (candidate / "FORGE_SPEC.md").exists():
            return candidate
        if (candidate / ".forge").is_dir() and (candidate / "SPEC.md").exists():
            return candidate
    # Fallback: parent of tools/
    return Path(__file__).resolve().parent.parent


def check_layout(root: Path) -> dict:
    """Check required files/dirs exist; count ADRs, skills, checkpoints."""
    root = Path(root)
    missing_files = [f for f in REQUIRED_FILES if not (root / f).is_file()]
    missing_dirs = [d for d in REQUIRED_DIRS if not (root / d).is_dir()]
    adrs = sorted((root / ".forge/decisions").glob("ADR-*.md")) if (root / ".forge/decisions").is_dir() else []
    skills = sorted((root / ".forge/skills").glob("*/SKILL.md")) if (root / ".forge/skills").is_dir() else []
    checkpoints = (
        sorted((root / ".forge/checkpoints").glob("checkpoint-*.md"))
        if (root / ".forge/checkpoints").is_dir()
        else []
    )
    return {
        "missing_files": missing_files,
        "missing_dirs": missing_dirs,
        "adr_count": len(adrs),
        "skill_count": len(skills),
        "checkpoint_count": len(checkpoints),
        "ok": not missing_files and not missing_dirs,
    }


def count_ids(spec_path: Path) -> dict:
    """Count FR/NFR/AC requirement IDs in FORGE_SPEC.md."""
    text = Path(spec_path).read_text(encoding="utf-8")
    kinds = ID_PATTERN.findall(text)
    counts = {"FR": kinds.count("FR"), "NFR": kinds.count("NFR"), "AC": kinds.count("AC")}
    counts["total"] = sum(counts.values())
    return counts


def verify(root: Path | None = None) -> dict:
    """Full verification: layout + ID counts + git state + KICKOFF freshness."""
    root = Path(root) if root else repo_root()
    layout = check_layout(root)
    counts = count_ids(root / "FORGE_SPEC.md")
    ids_ok = all(counts[k] == v for k, v in EXPECTED_COUNTS.items())
    content_ok = layout["adr_count"] >= 3 and layout["skill_count"] >= 3
    git = check_git_state(root)
    kickoff = check_kickoff_freshness(root)
    ok = layout["ok"] and ids_ok and content_ok and _check_ok(git) and _check_ok(kickoff)
    return {
        "root": str(root),
        "layout": layout,
        "counts": counts,
        "ids_ok": ids_ok,
        "git": git,
        "kickoff": kickoff,
        "ok": ok,
    }


def check_git_state(root: Path | None = None) -> dict:
    """Report git state at repo root: rev-parse HEAD + status --short.

    Returns {"present": bool, "rev": str|"", "clean": bool, "status_lines": [...]}.
    If git is unavailable or the repo has no commits, ``present`` is False
    and the other fields are empty defaults (checked, not assumed).
    """
    root = Path(root) if root else repo_root()

    def _run(*args: str) -> tuple[str, int]:
        proc = subprocess.run(  # noqa: S603
            ["git", *args],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.stdout.strip(), proc.returncode

    rev, rc = _run("rev-parse", "HEAD")
    if rc != 0:
        return {"present": False, "rev": "", "clean": False, "status_lines": []}
    status, _ = _run("status", "--short")
    status_lines = [line for line in status.splitlines() if line]
    return {
        "present": True,
        "rev": rev,
        "clean": not status_lines,
        "status_lines": status_lines,
    }


def check_kickoff_freshness(root: Path | None = None) -> dict:
    """Verify KICKOFF.md reflects the current project state.

    Checks that: (1) an in-progress task from tasks.md is mentioned,
    (2) every checkpoint referenced in KICKOFF exists on disk,
    (3) KICKOFF contains no stale "no git repo" claim.
    Returns {"ok": bool, "issues": [str, ...], "referenced_checkpoints": [...]}.
    """
    root = Path(root) if root else repo_root()
    issues: list[str] = []

    kickoff_path = root / ".forge/KICKOFF.md"
    tasks_path = root / ".forge/tasks.md"
    checkpoints_dir = root / ".forge/checkpoints"

    kickoff_text = (
        kickoff_path.read_text(encoding="utf-8")
        if kickoff_path.is_file()
        else ""
    )

    # 1. KICKOFF mentions the active task (single IN_PROGRESS in V1).
    if tasks_path.is_file():
        active = [
            line for line in tasks_path.read_text(encoding="utf-8").splitlines()
            if re.match(r"^## TASK-\d+", line)
            and "IN_PROGRESS" in line
        ]
        for task_line in active:
            task_id = re.match(r"^## (TASK-\d+) ", task_line).group(1)
            if task_id not in kickoff_text:
                issues.append(f"KICKOFF does not mention active task {task_id}")
    elif "TASK-" not in kickoff_text:
        issues.append("tasks.md missing and KICKOFF mentions no task")

    # 2. Checkpoint references in KICKOFF exist on disk.
    referenced = sorted(
        set(re.findall(r"checkpoint-\d+\.md", kickoff_text))
    )
    for name in referenced:
        if not (checkpoints_dir / name).is_file():
            issues.append(f"KICKOFF references missing checkpoint {name}")

    # 3. No stale "no git repo" claim after git init.
    if re.search(r"no git repo", kickoff_text, re.IGNORECASE):
        issues.append("KICKOFF contains stale 'no git repo' claim")

    return {"ok": not issues, "issues": issues, "referenced_checkpoints": referenced}


def _check_ok(result: dict) -> bool:
    """Aggregate ok for git/kickoff checks with sane defaults."""
    if "present" in result:  # git state
        return result["present"] and result["clean"]
    return result["ok"]  # kickoff freshness


def main() -> int:
    result = verify()
    print(f"root: {result['root']}")
    print(f"counts: {result['counts']} ids_ok={result['ids_ok']}")
    print(
        "layout: missing_files={} missing_dirs={} adrs={} skills={} checkpoints={}".format(
            result["layout"]["missing_files"],
            result["layout"]["missing_dirs"],
            result["layout"]["adr_count"],
            result["layout"]["skill_count"],
            result["layout"]["checkpoint_count"],
        )
    )
    git = result["git"]
    print(
        "git: present={} clean={} rev={} changes={}".format(
            git["present"],
            git["clean"],
            git["rev"][:7] if git["rev"] else "-",
            len(git["status_lines"]),
        )
    )
    kickoff = result["kickoff"]
    print(
        "kickoff: ok={} checkpoints_ref={} issues={}".format(
            kickoff["ok"],
            kickoff["referenced_checkpoints"],
            kickoff["issues"],
        )
    )
    print("OK" if result["ok"] else "FAIL")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

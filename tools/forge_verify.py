"""Forge V1 structural verification helper (TASK-008 Agent1 partial).

Checks the filesystem convention from SPEC section 2 + FORGE_SPEC.md IDs.
Git-integration and KICKOFF-freshness checks are intentionally left as
stubs for Agent2 (see TASK-009).
"""

from __future__ import annotations

import re
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
    """Full Agent1 verification: layout + ID counts + ADR/skill minimums."""
    root = Path(root) if root else repo_root()
    layout = check_layout(root)
    counts = count_ids(root / "FORGE_SPEC.md")
    ids_ok = all(counts[k] == v for k, v in EXPECTED_COUNTS.items())
    content_ok = layout["adr_count"] >= 3 and layout["skill_count"] >= 3
    ok = layout["ok"] and ids_ok and content_ok
    return {"root": str(root), "layout": layout, "counts": counts, "ids_ok": ids_ok, "ok": ok}


def check_git_state(root: Path | None = None) -> dict:  # noqa: ARG001
    """Agent2 TODO (TASK-009): report rev-parse HEAD + status --short.

    Must return e.g. {"rev": "<sha>", "clean": True, "status_lines": [...]}.
    """
    raise NotImplementedError("TASK-009: implement git state check via subprocess")


def check_kickoff_freshness(root: Path | None = None) -> dict:  # noqa: ARG001
    """Agent2 TODO (TASK-009): verify KICKOFF reflects tasks/state/checkpoints.

    Must confirm: current TASK status mentioned, checkpoint files referenced
    exist on disk, no stale 'no git repo' claims after git init.
    """
    raise NotImplementedError("TASK-009: implement KICKOFF freshness check")


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
    print("OK" if result["ok"] else "FAIL")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

"""Tests for tools/forge_verify.py — TASK-008 Agent1 + TASK-009 Agent2.

Uses stdlib unittest (no new dependencies per project rules).
Covers layout/ID checks (Agent1) and git-state/KICKOFF-freshness
checks (Agent2).
"""

import tempfile
import unittest
from pathlib import Path

from tools.forge_verify import (
    EXPECTED_COUNTS,
    check_git_state,
    check_kickoff_freshness,
    check_layout,
    count_ids,
    repo_root,
    verify,
)

ROOT = repo_root(Path(__file__))


class TestForgeVerifyAgent1(unittest.TestCase):
    def test_required_files_present(self):
        layout = check_layout(ROOT)
        self.assertEqual(layout["missing_files"], [], f"missing: {layout['missing_files']}")
        self.assertEqual(layout["missing_dirs"], [], f"missing dirs: {layout['missing_dirs']}")

    def test_id_counts(self):
        counts = count_ids(ROOT / "FORGE_SPEC.md")
        for kind, expected in EXPECTED_COUNTS.items():
            self.assertEqual(counts[kind], expected, f"{kind}: {counts}")
        self.assertEqual(counts["total"], 28)

    def test_adr_skill_minimums(self):
        layout = check_layout(ROOT)
        self.assertGreaterEqual(layout["adr_count"], 3)
        self.assertGreaterEqual(layout["skill_count"], 3)
        self.assertGreaterEqual(layout["checkpoint_count"], 2)

    def test_verify_ok(self):
        self.assertTrue(verify(ROOT)["ok"])


class TestAgent2(unittest.TestCase):
    """TASK-009: real assertions for git-state and KICKOFF-freshness checks."""

    def test_git_state_reports_head_and_clean(self):
        git = check_git_state(ROOT)
        self.assertTrue(git["present"], "expected a git repo at repo root")
        self.assertRegex(git["rev"], r"^[0-9a-f]{40}$")
        self.assertTrue(git["clean"], f"unexpected changes: {git['status_lines']}")

    def test_kickoff_freshness_ok(self):
        kickoff = check_kickoff_freshness(ROOT)
        self.assertEqual(kickoff["issues"], [], f"issues: {kickoff['issues']}")
        self.assertTrue(kickoff["ok"])
        # Every checkpoint referenced in KICKOFF exists on disk.
        for name in kickoff["referenced_checkpoints"]:
            self.assertTrue((ROOT / ".forge/checkpoints" / name).is_file(), name)

    def test_kickoff_freshness_detects_stale_git_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            (tmp_root / ".forge/checkpoints").mkdir(parents=True)
            (tmp_root / ".forge/checkpoints/checkpoint-001.md").write_text("x")
            (tmp_root / ".forge/KICKOFF.md").write_text(
                "No git repo in this checkout. see checkpoint-001.md\n"
            )
            (tmp_root / ".forge/tasks.md").write_text(
                "## TASK-001\nStatus: IN_PROGRESS\n"
            )
            result = check_kickoff_freshness(tmp_root)
            self.assertFalse(result["ok"])
            self.assertTrue(
                any("stale 'no git repo'" in i for i in result["issues"]),
                f"issues: {result['issues']}",
            )

    def test_kickoff_freshness_detects_missing_checkpoint_ref(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            (tmp_root / ".forge/checkpoints").mkdir(parents=True)
            (tmp_root / ".forge/KICKOFF.md").write_text(
                "see checkpoint-099.md\n"
            )
            (tmp_root / ".forge/tasks.md").write_text(
                "## TASK-001\nStatus: IN_PROGRESS\n"
            )
            result = check_kickoff_freshness(tmp_root)
            self.assertFalse(result["ok"])
            self.assertTrue(
                any("missing checkpoint" in i for i in result["issues"]),
                f"issues: {result['issues']}",
            )

    def test_verify_includes_git_and_kickoff(self):
        result = verify(ROOT)
        self.assertIn("git", result)
        self.assertIn("kickoff", result)
        self.assertTrue(result["git"]["present"])
        self.assertTrue(result["git"]["clean"])
        self.assertEqual(result["kickoff"]["issues"], [])
        self.assertTrue(result["ok"])


if __name__ == "__main__":
    unittest.main()

"""Tests for tools/forge_verify.py — TASK-008 Agent1.

Uses stdlib unittest (no new dependencies per project rules).
Green now for layout/ID checks; stub tests document TASK-009 remainder.
"""

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


class TestAgent2Deferred(unittest.TestCase):
    """Intentionally incomplete — Agent2 implements these in TASK-009."""

    def test_git_stub_raises(self):
        with self.assertRaises(NotImplementedError):
            check_git_state(ROOT)

    def test_kickoff_stub_raises(self):
        with self.assertRaises(NotImplementedError):
            check_kickoff_freshness(ROOT)


if __name__ == "__main__":
    unittest.main()

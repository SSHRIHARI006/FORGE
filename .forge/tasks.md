# Tasks

> Bounded, requirement-traceable work. Statuses: READY | IN_PROGRESS | BLOCKED | DONE | FAILED.
> V1 rule: exactly one task IN_PROGRESS at a time.

## TASK-001

Status: DONE

Goal:
Create `.forge/INIT.md` master initialization prompt covering discovery, adaptive interview, challenge/recommendation, confirmation, context creation, task planning, verification, hierarchy, security, and non-goals.

Requirements:
FR-001, FR-002, FR-003, FR-004

Verification:
`test -f .forge/INIT.md && grep -c "Do not modify application code" .forge/INIT.md` → must be ≥1. (Ran during implementation; see state.md.)

---

## TASK-002

Status: DONE

Goal:
Create living `FORGE_SPEC.md` at repo root with Overview, Goals, Users, Workflows, FR-001..FR-017, NFR-001..NFR-005, AC-001..AC-006, Scope In/Out, Technical Direction, Constraints, Definition of Done.

Requirements:
FR-005
AC-002

Verification:
`test -f FORGE_SPEC.md && grep -E "^### (FR|NFR|AC)-" FORGE_SPEC.md | wc -l` → 28 IDs (17 FR + 5 NFR + 6 AC).

---

## TASK-003

Status: DONE

Goal:
Create project rules, task/state/kickoff scaffolding: `.forge/rules.md`, `.forge/tasks.md` (this file), `.forge/state.md`, `.forge/KICKOFF.md`.

Requirements:
FR-006, FR-007, FR-008, FR-009

Verification:
`ls .forge/rules.md .forge/tasks.md .forge/state.md .forge/KICKOFF.md` → all present.

---

## TASK-004

Status: DONE

Goal:
Record foundational decisions as ADRs (filesystem-over-DB, single-active-agent, agent-agnostic markdown).

Requirements:
FR-010

Verification:
`ls .forge/decisions/ADR-*.md` → ≥3 files, each containing Decision/Context/Alternatives/Reason/Status.

---

## TASK-005

Status: DONE

Goal:
Add minimal V1 skills (testing, security, specification) with `name/description/tags` frontmatter + Goal/Rules/Workflow, plus `taste/preferences.md` and initial `checkpoints/checkpoint-001.md`.

Requirements:
FR-011, FR-012, FR-013

Verification:
`ls .forge/skills/*/SKILL.md .forge/taste/preferences.md .forge/checkpoints/checkpoint-*.md` → 3 skills + taste + checkpoint present.

---

## TASK-006

Status: DONE

Goal:
Add `AGENTS.md` adapter pointing agent-specific tooling at Forge as cross-agent source of truth.

Requirements:
FR-016

Verification:
`test -f AGENTS.md && grep -c "KICKOFF" AGENTS.md` → ≥1.

---

## TASK-007

Status: DONE

Goal:
Verify end-to-end V1 enablement: structure matches SPEC §2, all 17 V1 checklist items (§29) satisfiable, continuation test passes (a fresh agent can state project/task/done/broken/verified/next from files + git alone).

Requirements:
FR-014, FR-015
AC-001, AC-002, AC-003, AC-004, AC-005, AC-006

Verification:
`ls -R .forge; git status --short` + manual continuation check recorded in `state.md` Verification section.

---

## TASK-008

Status: DONE (2026-09-05 — Agent1 partial, Agent2 completed remainder via TASK-009)

Goal:
Dogfood pilot Agent1: create small Python `tools/forge_verify.py` that checks Forge V1 structure (required files present, FR/NFR/AC counts, ADR/skill counts) with `tests/test_forge_verify.py`. Leave git-integration + KICKOFF-freshness checks as stubs for Agent2. Follow BUILD/VERIFY with recorded evidence, then handoff.

Requirements:
FR-015
AC-003, AC-004

Verification:
`python3 -m unittest discover -s tests -v` — must paste real command output into `state.md` before marking DONE. Agent1 stop point: layout/ID tests green, 2 stubs raise NotImplementedError. Agent2 close-out: stubs implemented + real tests; full suite green (see `state.md` Verification, 9 tests OK).

---

## TASK-009

Status: DONE (2026-09-05 — Agent2 continuation drill completed)

Goal:
Dogfood pilot Agent2 (handoff continuation, no prior conversation): implement `check_git_state()` and `check_kickoff_freshness()` stubs in `tools/forge_verify.py`, add real tests replacing the NotImplementedError expectations, re-run verification green, update state/KICKOFF, prove continuation from files + git alone.

Requirements:
FR-014, FR-015
AC-003, AC-004, AC-005

Verification:
`python3 -m unittest discover -s tests -t . -v && python3 tools/forge_verify.py` — real output pasted into `state.md` Verification: 9 tests OK, forge_verify.py exits 0 with git/kickoff lines green. During development the new git check correctly flagged the dirty working tree (3 test failures, diagnosed: uncommitted edits); after commit, clean + green. Continuation assessment recorded in `state.md` / `checkpoint-004.md`.

---

## TASK-010

Status: DONE (2026-09-05 — v1.0.0 presentation, release notes, and unrelated adoption test completed)

Goal:
Finalize Forge v1.0.0 public repository presentation, release preparation, and unrelated real-world adoption verification:
1. Polish root `README.md` (clean remote-add Option A install command, remove local machine path references, sync file tree and ADR/checkpoint counts).
2. Prepare GitHub v1.0.0 release notes and publish instructions (`.forge/releases/v1.0.0.md`).
3. Perform an unrelated real-world adoption test in an isolated workspace (`/tmp/forge-unrelated-adoption-test` with an in-memory inventory service).
4. Verify everything with `tools/forge_verify.py` and test suite, recording real output.

Requirements:
FR-005, FR-008, FR-009, FR-014, FR-015
AC-001, AC-003, AC-004, AC-005

Verification:
`python3 -m unittest discover -s tests -t . -v && python3 tools/forge_verify.py` — verified 9 tests pass, forge_verify.py clean. Real-world adoption test passed with 16 template files cleanly adopted and zero leaks. Checkpoint-009 recorded.



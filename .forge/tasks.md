# Tasks

> Bounded, requirement-traceable work. Statuses: READY | IN_PROGRESS | BLOCKED | DONE | FAILED.
> V1 rule: exactly one task IN_PROGRESS at a time.

## TASK-001

Status: READY

Goal:
Initialize this project into Forge per `.forge/INIT.md`: read-only discovery, adaptive user interview, challenge/conformation, user confirmation, then create `FORGE_SPEC.md` (with FR/NFR/AC stable IDs), project-specific `.forge/rules.md`, `tasks.md`, `state.md`, record decisions in `decisions/ADR-*.md`, populate `taste/preferences.md`, create a checkpoint, and update `KICKOFF.md`.

Requirements:
FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, FR-013
AC-001, AC-002

Verification:
`test -f FORGE_SPEC.md && grep -cE "^### (FR|NFR|AC)-" FORGE_SPEC.md` (≥1 of each, stable IDs) + `ls .forge/` + real output recorded in `state.md` Verification.

---

*(Replace this file's content with your project's real task plan after initialization. Keep one task IN_PROGRESS at a time.)*
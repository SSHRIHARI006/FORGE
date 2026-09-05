# Tasks

> Bounded, requirement-traceable work. Statuses: READY | IN_PROGRESS | BLOCKED | DONE | FAILED.
> V1 rule: exactly one task IN_PROGRESS at a time.

## TASK-001

Status: READY

Goal:
Initialize this project into Forge per `.forge/INIT.md`: read-only discovery, adaptive user interview, challenge/confirmation, user confirmation, then create `FORGE_SPEC.md` (with FR/NFR/AC stable IDs), project-specific `.forge/rules.md`, `tasks.md`, `state.md`, record decisions in `decisions/ADR-*.md`, populate `taste/preferences.md`, create a checkpoint, and update `KICKOFF.md`.

Requirements:
None yet — this task *is* the initialization. The project's requirement IDs (FR-xxx / NFR-xxx / AC-xxx) are defined in `FORGE_SPEC.md` during this task and referenced by subsequent tasks.

Verification:
`test -f FORGE_SPEC.md && grep -cE "^### (FR|NFR|AC)-" FORGE_SPEC.md` (≥1 of each kind, stable IDs) + `ls .forge/` + real output recorded in `state.md` Verification.

---

*(Replace this file's content with your project's real task plan after initialization. Keep one task IN_PROGRESS at a time.)*
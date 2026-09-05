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

Status: READY

Goal:
Dogfood: use Forge context to implement the next real change in this repo (or a pilot repo), following BUILD/VERIFY/ENGINEER with recorded evidence, then perform a cross-agent handoff drill.

Requirements:
FR-015
AC-003, AC-004

Verification:
`tbd per pilot task, e.g. pytest tests/ / npm test` — must paste real command output into `state.md` before marking DONE.

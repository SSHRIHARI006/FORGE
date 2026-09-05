# Current KICKOFF

> New agent? Read in this order: this file → `../FORGE_SPEC.md` (repo root) → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status / git diff / git log --oneline -10`.

## Project

Forge — portable, agent-agnostic project context layer (`.forge/` + `FORGE_SPEC.md`). Agents are temporary; project context is persistent. V1 is filesystem + instructions only: no daemon, DB, service, runtime, or dashboard.

## Current Task

TASK-007 DONE 2026-09-05 (structural verification passed, evidence in `state.md`). Next: TASK-008 READY — dogfood pilot, awaiting user authorization.

## Goal

Prove a fresh repo was converted into a Forge-enabled project where a different agent can continue without the original conversation, with real verification evidence.

## Completed

- `FORGE_SPEC.md` (17 FR / 5 NFR / 6 AC), `.forge/INIT.md`, `rules.md`, `tasks.md`, `state.md`
- Decisions: ADR-001 (filesystem over DB), ADR-002 (single active agent), ADR-003 (agent-agnostic markdown)
- Skills: testing, security, specification; `taste/preferences.md`; `checkpoints/checkpoint-001.md`; `AGENTS.md` adapter
- Repo was empty except `SPEC.md`; no app code touched during init.

## Current Work

TASK-007 closed with evidence. No active IN_PROGRESS task — next agent picks up TASK-008 when user authorizes, or awaits user direction on spec confirmation.

## Verification

Structural verification passed 2026-09-05 (see `state.md` Verification for pasted output): `.forge/` layout matches SPEC §2, 28 requirement IDs, 3 ADRs, 3 skills, taste + checkpoints present. No app test suite exists yet. Checkpoint-002 records the milestone.

## Current Failure

None. Open confirmation: user to verify `FORGE_SPEC.md` accuracy and `SPEC.md`-vs-`FORGE_SPEC.md` retention (currently: keep both).

## Important Decisions

- ADR-001: filesystem/markdown convention, no DB/runtime in V1.
- ADR-002: one active agent at a time; file-based handoff via KICKOFF/state/tasks.
- ADR-003: agent-agnostic markdown; `AGENTS.md` is a thin adapter, Forge is source of truth.

## Next Action

User: confirm `FORGE_SPEC.md` accuracy → authorize TASK-008 pilot (real change with evidence + handoff drill). Suggested first step: `git init && git add -A && git commit` (no git history exists yet).

## Constraints

- Never commit secrets; human confirmation for destructive/prod/credential/security-policy actions.
- One task IN_PROGRESS; tasks traceable to FR/AC with executable Verification.
- Taste never overrides instructions/requirements/safety. Assumptions labeled, never treated as requirements.

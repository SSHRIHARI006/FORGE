# Current KICKOFF

> New agent? Read in this order: this file → `../FORGE_SPEC.md` (repo root, if present) → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status / git diff / git log --oneline -10`.

## Project

This project is being adopted into **Forge** — a portable, agent-agnostic project context layer (`.forge/` + `FORGE_SPEC.md`). Agents are temporary; project context is persistent. V1 is filesystem + instructions only: no daemon, DB, service, runtime, or dashboard.

## Current Task

Initialization pending. This is a fresh template install: read `.forge/INIT.md` and follow it exactly (read-only discovery → adaptive interview → challenge → confirmation → context creation). The concrete deliverable is a project-specific `FORGE_SPEC.md` + populated rules/tasks/state + checkpoint + KICKOFF.

## Goal

Turn this repository into a Forge-enabled project where any compatible agent can continue work without the original conversation, with real verification evidence.

## Completed

- Template installed: `.forge/` convention + `AGENTS.md` adapter present.
- No project context created yet — the template's state/tasks/KICKOFF are placeholders by design.

## Current Work

Nothing beyond installation. All Forge files except `INIT.md`, `rules.md`, `AGENTS.md`, skills, ADRs, and taste are placeholders awaiting initialization.

## Verification

Installation check (run in the adopting project):
```text
$ ls .forge/
INIT.md KICKOFF.md checkpoints/ decisions/ rules.md skills/ state.md tasks.md taste/
$ test -f .forge/INIT.md && echo "init ok"
```

## Current Failure

None. This is a pre-initialization state, not a failure.

## Important Decisions

- ADR-001: Forge is a filesystem/markdown convention; no DB/runtime in V1.
- ADR-002: one active agent at a time; file-based handoff via KICKOFF/state/tasks.
- ADR-003: agent-agnostic markdown; `AGENTS.md` is a thin adapter, Forge is source of truth.

## Next Action

Run initialization per `.forge/INIT.md`, then record the project-specific context (spec, rules, tasks, state, decisions, checkpoint, KICKOFF) with user confirmation.

## Constraints

- Never commit secrets; human confirmation for destructive/prod/credential/security-policy actions.
- One task IN_PROGRESS; tasks traceable to FR/AC with executable Verification.
- Taste never overrides instructions/requirements/safety. Assumptions labeled, never treated as requirements.
- Do not modify application code during initialization.
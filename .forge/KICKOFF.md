# Current KICKOFF

> New agent? Read in this order: this file → `../FORGE_SPEC.md` (repo root) → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status / git diff / git log --oneline -10`.

## Project

Forge — portable, agent-agnostic project context layer (`.forge/` + `FORGE_SPEC.md`). Agents are temporary; project context is persistent. V1 is filesystem + instructions only: no daemon, DB, service, runtime, or dashboard.

## Current Task

TASK-008 IN_PROGRESS (Agent1 partial 2026-09-05). Pilot: `tools/forge_verify.py` + tests, layout/ID checks green, git/KICKOFF checks stubbed. TASK-009 READY for Agent2 continuation. See `state.md` Verification for pasted output.

## Goal

Prove a fresh repo was converted into a Forge-enabled project where a different agent can continue without the original conversation, with real verification evidence.

## Completed

- `FORGE_SPEC.md` (17 FR / 5 NFR / 6 AC), `.forge/INIT.md`, `rules.md`, `tasks.md`, `state.md`
- Decisions: ADR-001 (filesystem over DB), ADR-002 (single active agent), ADR-003 (agent-agnostic markdown)
- Skills: testing, security, specification; `taste/preferences.md`; `checkpoints/checkpoint-001.md` + `checkpoint-002.md` (TASK-007 close-out) + `checkpoint-003.md` (TASK-008 Agent1 stop); `AGENTS.md` adapter
- Repo was empty except `SPEC.md`; no app code touched during init.
- Git initialized 2026-09-05: first commit `14fb107` "feat: initialize Forge V1 context layer".
- FORGE_SPEC vs SPEC reviewed 2026-09-05: faithful, no edits proposed (awaiting user sign-off).
- TASK-008 Agent1: `tools/forge_verify.py`, `tests/test_forge_verify.py`, 6 tests green.

## Current Work

Agent1 stopped after partial TASK-008. `tools/forge_verify.py` implements `check_layout` / `count_ids` / `verify`; `check_git_state()` and `check_kickoff_freshness()` raise NotImplementedError by design. Tests: 4 functional green + 2 stub-expectation green. Next agent implements TASK-009.

## Verification

Structural verification passed 2026-09-05 (see `state.md` Verification): 28 IDs, 3 ADRs, 3 skills, checkpoints 001+002 present. Pilot verification 2026-09-05: `python3 -m unittest discover -s tests -t . -v` → 6 tests OK; `python3 tools/forge_verify.py` → OK (counts 17/5/6, layout clean). Git rev at Agent1 test time: `14fb107`.

## Current Failure

None blocking. Intentional remainder: 2 stubs NotImplemented (TASK-009). Open confirmations: user to sign off `FORGE_SPEC.md` accuracy (Agent1 found no issues) and `SPEC.md`-vs-`FORGE_SPEC.md` retention (currently: keep both).

## Important Decisions

- ADR-001: filesystem/markdown convention, no DB/runtime in V1.
- ADR-002: one active agent at a time; file-based handoff via KICKOFF/state/tasks.
- ADR-003: agent-agnostic markdown; `AGENTS.md` is a thin adapter, Forge is source of truth.

## Next Action

Agent2 (different agent, fresh session): read Forge context + git state, then do TASK-009 — implement the 2 stubs, replace stub tests with real assertions, re-run `python3 -m unittest discover -s tests -t . -v && python3 tools/forge_verify.py` green, mark TASK-008 DONE, update state/KICKOFF. Must answer from files alone: what built, done, why, remains, failed, next.

## Constraints

- Never commit secrets; human confirmation for destructive/prod/credential/security-policy actions.
- One task IN_PROGRESS; tasks traceable to FR/AC with executable Verification.
- Taste never overrides instructions/requirements/safety. Assumptions labeled, never treated as requirements.
- Pilot uses stdlib unittest, no new dependencies.

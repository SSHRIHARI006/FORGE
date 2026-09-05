# Current KICKOFF

> New agent? Read in this order: this file → `../FORGE_SPEC.md` (repo root) → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status / git diff / git log --oneline -10`.

## Project

Forge — portable, agent-agnostic project context layer (`.forge/` + `FORGE_SPEC.md`). Agents are temporary; project context is persistent. V1 is filesystem + instructions only: no daemon, DB, service, runtime, or dashboard.

## Current Task

None IN_PROGRESS. TASK-008/009 DONE (2026-09-05); ADR-004 executed — the `forge-template` branch exists (`a944298`, 16 clean files). Latest checkpoint: `checkpoint-005.md`.

## Goal

Prove a fresh repo was converted into a Forge-enabled project where a different agent can continue without the original conversation, with real verification evidence. **Achieved**: Agent2 reconstructed state from files + git alone, implemented the two remaining stubs, replaced stub tests, verified green, and updated all context.

## Completed

- `FORGE_SPEC.md` (17 FR / 5 NFR / 6 AC), `.forge/INIT.md`, `rules.md`, `tasks.md`, `state.md`
- Decisions: ADR-001 (filesystem over DB), ADR-002 (single active agent), ADR-003 (agent-agnostic markdown), ADR-004 (dev repo vs template split — executed 2026-09-05)
- Skills: testing, security, specification; `taste/preferences.md`; checkpoints 001..005; `AGENTS.md` adapter
- Git: master HEAD `502e8c5` + `forge-template` branch `a944298` (16 files) — see `git log --oneline -10`, `git branch -v`
- TASK-008: `tools/forge_verify.py` (layout + ID counts + git state + KICKOFF freshness), `tests/test_forge_verify.py` (9 tests)
- TASK-009 (Agent2): `check_git_state()` + `check_kickoff_freshness()` implemented, wired into `verify()`/`main()`; 2 stub tests replaced with 5 real tests; continuation assessment recorded in `state.md` + `checkpoint-004.md`

## Current Work

TASK-008/009 drill complete (Agent2) and ADR-004 executed: `forge-template` branch created (`a944298`) with 16 sanitized files, adoption procedure verified in a fresh repo (`/tmp/forge-adoption-test`). Details: `checkpoint-005.md`.

## Verification

Structural + pilot verification passed 2026-09-05 (full output in `state.md` Verification):
```text
$ python3 -m unittest discover -s tests -t . -v
Ran 9 tests ... OK
$ python3 tools/forge_verify.py
counts: {'FR': 17, 'NFR': 5, 'AC': 6, 'total': 28} ids_ok=True
layout: missing_files=[] missing_dirs=[] adrs=4 skills=3 checkpoints=5
git: present=True clean=True rev=502e8c5 changes=0
kickoff: ok=True checkpoints_ref=['checkpoint-004.md', 'checkpoint-005.md'] issues=[]
OK
```
Template integrity (ADR-004): 16 files, zero dev references (`grep` clean), branch blobs byte-identical to `../forge-template/`, fresh-repo adoption passed.

## Current Failure

None. Open user confirmations: sign-off on `FORGE_SPEC.md` accuracy (no issues found) and `SPEC.md` retention (currently: keep both).

## Important Decisions

- ADR-001: filesystem/markdown convention, no DB/runtime in V1.
- ADR-002: one active agent at a time; file-based handoff via KICKOFF/state/tasks.
- ADR-003: agent-agnostic markdown; `AGENTS.md` is a thin adapter, Forge is source of truth.
- ADR-004: executed 2026-09-05 — clean template on the `forge-template` branch (16 files: README + AGENTS + `.gitignore` + sanitized `.forge/`); adoption procedure verified in a fresh repo; branch pushed to origin (`a944298`).
- Pilot stays dependency-free (stdlib unittest; no pytest).

## Next Action

1. ~~Push forge-template~~ — done (remote = `a944298`). Note: local master is ahead of remote master (`239ecc3`); pushing master is a separate user decision.
2. Get sign-off on spec accuracy + `SPEC.md` retention.
3. Dogfood the template in a real project (per template README Option A); feed issues back to dev.

## Constraints

- Never commit secrets; human confirmation for destructive/prod/credential/security-policy actions.
- One task IN_PROGRESS; tasks traceable to FR/AC with executable Verification.
- Taste never overrides instructions/requirements/safety. Assumptions labeled, never treated as requirements.
- No new dependencies without a stated reason; stdlib only for the pilot.
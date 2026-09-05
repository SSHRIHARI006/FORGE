# Current KICKOFF

> New agent? Read in this order: this file → `../FORGE_SPEC.md` (repo root) → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status / git diff / git log --oneline -10`.

## Project

Forge — portable, agent-agnostic project context layer (`.forge/` + `FORGE_SPEC.md`). Agents are temporary; project context is persistent. V1 is filesystem + instructions only: no daemon, DB, service, runtime, or dashboard.

## Current Task

None IN_PROGRESS. TASK-008 DONE + TASK-009 DONE (2026-09-05) — the cross-agent continuation drill passed. See `state.md` Verification for real output; latest checkpoint: `checkpoint-004.md`.

## Goal

Prove a fresh repo was converted into a Forge-enabled project where a different agent can continue without the original conversation, with real verification evidence. **Achieved**: Agent2 reconstructed state from files + git alone, implemented the two remaining stubs, replaced stub tests, verified green, and updated all context.

## Completed

- `FORGE_SPEC.md` (17 FR / 5 NFR / 6 AC), `.forge/INIT.md`, `rules.md`, `tasks.md`, `state.md`
- Decisions: ADR-001 (filesystem over DB), ADR-002 (single active agent), ADR-003 (agent-agnostic markdown), ADR-004 (dev repo vs template split, execution deferred)
- Skills: testing, security, specification; `taste/preferences.md`; checkpoints 001..004; `AGENTS.md` adapter
- Git: 7 commits, HEAD `bbcf83d` (close-out commits `ab7e70e` TASK-008/009 + `bbcf83d` docs) — see `git log --oneline -10`
- TASK-008: `tools/forge_verify.py` (layout + ID counts + git state + KICKOFF freshness), `tests/test_forge_verify.py` (9 tests)
- TASK-009 (Agent2): `check_git_state()` + `check_kickoff_freshness()` implemented, wired into `verify()`/`main()`; 2 stub tests replaced with 5 real tests; continuation assessment recorded in `state.md` + `checkpoint-004.md`

## Current Work

Agent2's cold-start continuation drill for TASK-009 is complete. During development the new git check correctly failed on the dirty working tree (diagnosed: uncommitted edits; fixed via user-approved commit). Final state: working tree clean, 9 tests OK, `forge_verify.py` exits 0.

## Verification

Structural + pilot verification passed 2026-09-05 (full output in `state.md` Verification):
```text
$ python3 -m unittest discover -s tests -t . -v
Ran 9 tests ... OK
$ python3 tools/forge_verify.py
counts: {'FR': 17, 'NFR': 5, 'AC': 6, 'total': 28} ids_ok=True
layout: missing_files=[] missing_dirs=[] adrs=4 skills=3 checkpoints=4
git: present=True clean=True rev=bbcf83d changes=0
kickoff: ok=True checkpoints_ref=['checkpoint-004.md'] issues=[]
OK
```

## Current Failure

None. Open user confirmations: sign-off on `FORGE_SPEC.md` accuracy (no issues found) and `SPEC.md` retention (currently: keep both).

## Important Decisions

- ADR-001: filesystem/markdown convention, no DB/runtime in V1.
- ADR-002: one active agent at a time; file-based handoff via KICKOFF/state/tasks.
- ADR-003: agent-agnostic markdown; `AGENTS.md` is a thin adapter, Forge is source of truth.
- ADR-004: split a clean `forge-template` repo later, after the contract stabilizes (deferred until now — drill passed, so execution can begin when authorized).
- Pilot stays dependency-free (stdlib unittest; no pytest).

## Next Action

1. Report drill outcome to user; get sign-off on spec accuracy + retention.
2. If authorized: execute ADR-004 (extract `.forge/` + README into `forge-template`).
3. Otherwise: await direction — V1 scenario (§29 of SPEC.md) is now fully proven.

## Constraints

- Never commit secrets; human confirmation for destructive/prod/credential/security-policy actions.
- One task IN_PROGRESS; tasks traceable to FR/AC with executable Verification.
- Taste never overrides instructions/requirements/safety. Assumptions labeled, never treated as requirements.
- No new dependencies without a stated reason; stdlib only for the pilot.
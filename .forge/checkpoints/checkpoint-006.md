# Checkpoint 006 — Dogfood Drill Results (forge-template in a Real Project)

Date: 2026-09-05
Type: milestone — template validated end-to-end in `../forge-dogfood/`; findings fed back to dev

## Project State

The `forge-template` branch was installed into a fresh project (`../forge-dogfood/`), initialized per `INIT.md`, and a real feature (`dscan`, stdlib-only Python CLI) was implemented and verified with recorded output. The dogfood loop from ADR-004 is now closed: template → adopt → init → implement → verify → handoff all worked. Findings below.

## Specification

Dev `FORGE_SPEC.md` unchanged (17 FR / 5 NFR / 6 AC). The dogfood project has its own spec (5 FR / 3 NFR / 4 AC).

## Current Task

None IN_PROGRESS in the dev repo. Dogfood drill completed; follow-up = apply template fixes (next steps).

## Completed Work

- Installed template into `../forge-dogfood/` (git init → `git fetch <forge-repo> forge-template:forge-template` → checkout → commit `2ac7727`).
- Ran `INIT.md` flow: discovery (fresh repo), adaptive interview (user chose minimal stdlib-only Python CLI, tested), confirmation, context creation (`FORGE_SPEC.md` 12 IDs, tasks/state/KICKOFF, `ADR-004`, `checkpoint-002.md`).
- Implemented TASK-002: `dscan.py` + `tests/test_dscan.py` — 5 tests green, manual CLI runs recorded (`state.md` Verification).
- TASK-003 handoff close-out: cold-start reading order confirmed answers what/done/verified/next; committed `2d5d22d`.
- This checkpoint + KICKOFF/state updates in the dev repo.

## Git State

```text
Dev repo master HEAD: f40ccc1 (before this checkpoint)
Dogfood repo: 2d5d22d "feat: dscan v1 (TASK-002) + handoff context (TASK-003)" (main)
Template branch: forge-template (a944298) — fixes proposed, not yet applied
```

## Verification Results

```text
$ python3 -m unittest discover -s tests -t . -v   # in ../forge-dogfood
Ran 5 tests in 0.002s
OK
$ python3 dscan.py /tmp/dscan-demo
EXTENSION         FILES         SIZE
--------------------------------------
py                    2          5 B
txt                   1          4 B
--------------------------------------
TOTAL                 3          9 B
```
(Full transcripts in `../forge-dogfood/.forge/state.md`.)

## Important Decisions

- ADR-001..004 in dev repo unchanged.
- Template content is validated as workable; fixes below are refinements, not redesigns.

## Known Problems — Template Rough Edges (found during dogfood)

1. **README install command broken for fresh projects (medium).** Option A says `git fetch origin forge-template:forge-template`, but a new project's `origin` is itself — the fetch fails unless the adopter knows to use the Forge repo URL. Fix: show `git fetch <forge-repo-url> forge-template:forge-template` (or `git remote add forge <url> && git fetch forge forge-template`) with the actual URL.
2. **Placeholder `tasks.md` cites dev-spec IDs (medium).** Template TASK-001 lists `FR-001..FR-013 / AC-001..AC-002` — those IDs belong to the Forge dev spec and don't exist in an adopting project until it writes its own `FORGE_SPEC.md`. Fix: reference `.forge/INIT.md` itself (no FR IDs), or say "requirement IDs defined by the project's new FORGE_SPEC.md".
3. **`AGENTS.md` reading order assumes `FORGE_SPEC.md` exists (low).** "Every Session" step 1 lists it, but at install time it doesn't exist yet. Harmless (agents skip missing files) but should say "(if present)" like KICKOFF does.
4. **`INIT.md` length (low/informational).** ~250 lines, comprehensive; a 5-line "what to do now" summary at the top would speed cold starts. Not a defect.
5. **No automated structure check ships in the template (informational).** The dev repo's `tools/forge_verify.py` is deliberately excluded (ADR-004: template = `.forge/` + README only). Adopters verify via `ls .forge/`/grep per INIT.md. A future "add `tools/forge_verify.py` to the template" decision is possible but out of current scope.

## Next Steps

1. Apply fixes 1–3 to `../forge-template/` + `forge-template` branch; re-run sanitization + adoption test; push branch (with user approval).
2. Optionally add a "quick summary" header to `INIT.md` (fix 4).
3. Record the decision about shipping a verify tool in the template (fix 5) if the user wants it.
4. Report findings to the user.
# Checkpoint 005 — ADR-004 Executed: forge-template Branch Created

Date: 2026-09-05
Type: milestone — template extraction (ADR-004)

## Project State

Forge V1 context complete (TASK-001..009 DONE) and the installable artifact now exists: the `forge-template` branch of this repo (commit `a944298`), mirrored at `../forge-template/` on disk. The dev repo remains the source of truth for Forge development; adopters pull the clean template.

## Specification

`FORGE_SPEC.md`: 17 FR, 5 NFR, 6 AC (28 IDs) — unchanged. `SPEC.md` retained as frozen input.

## Current Task

None IN_PROGRESS. TASK-008/009 DONE; ADR-004 executed as follow-up work.

## Completed Work

- Created clean template content (16 files): `README.md` (install + working procedure), `AGENTS.md`, `.gitignore`, and `.forge/` with generic `INIT.md`, `rules.md`, skills (testing/security/specification), `decisions/ADR-001..003.md`, `taste/preferences.md`, plus **neutral placeholders** for `state.md`, `tasks.md` (single TASK-001 initialization task), `KICKOFF.md`, and `checkpoints/checkpoint-001.md`.
- Sanitization verified: no `TASK-008/009`, `checkpoint-002..004`, `Agent1/Agent2`, or repo-name references in the template.
- Created branch `forge-template` (commit `a944298`, `git commit-tree` — independent root, master history untouched); blob-integrity checked (all 16 files byte-identical to `../forge-template/`).
- Adoption procedure verified end-to-end: fresh repo at `/tmp/forge-adoption-test` → `git fetch origin forge-template:forge-template` → `git checkout forge-template -- .` → 16 files adopted → commit clean.
- Updated `state.md` / `KICKOFF.md` / `README.md` (dev) and this checkpoint.

## Git State

```text
master HEAD: 536f114 (unchanged; working tree clean at execution start)
forge-template branch: a944298c548b31529ba55b1948ad2a61dd9d4901 (root commit, 16 files)
Adoption test repo: /tmp/forge-adoption-test (clean, template committed)
Template mirror on disk: ../forge-template/
```

## Verification Results

```text
$ find ../forge-template -type f | wc -l
16
$ grep -rl "TASK-008\|TASK-009\|checkpoint-00[234]\|Agent1\|Agent2\|SSHRIHARI006" ../forge-template/
(no output — no dev references)
$ git ls-tree -r --name-only forge-template | wc -l
16
(blob SHA1 comparison: all 16 files identical to ../forge-template/)
Fresh-repo adoption: fetch + checkout forge-template -- . → 16 files, git status clean
```

## Important Decisions

- ADR-001/002/003 unchanged. ADR-004 status → Accepted + executed.
- Template is a branch of the dev repo (user direction), not a separate repo. Branch created as an independent root commit so it contains only template files.
- Template content policy: generic context ships; project state never ships (dev `state.md`/tasks/checkpoints are excluded by design).

## Known Problems

- ~~`forge-template` branch not yet pushed~~ — **pushed 2026-09-05** (remote refs/heads/forge-template = `a944298`). Adopters can now `git fetch origin forge-template` directly.
- Template naming/location (`forge-template` branch) may evolve once the public install flow is exercised.

## Next Steps

1. ~~Push branch~~ — done (`git push origin forge-template` → remote refs/heads/forge-template = `a944298`).
2. Dogfood: use the template in a real project per README Option A; feed issues back to dev (`INIT.md`, context quality).
3. If the `.forge/` contract changes materially, update the template branch (sanitization re-check required).
4. Note: local master is ahead of remote master (remote master = `239ecc3`); pushing master is a separate decision for the user.
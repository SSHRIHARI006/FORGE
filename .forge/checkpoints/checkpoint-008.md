# Checkpoint 008 — V1 Released (forge-template v1.0.0)

Date: 2026-09-05
Type: milestone — stabilization/release, template frozen

## Project State

Forge V1 is released as tag `v1.0.0` on the `forge-template` branch (product artifact). The template has been validated twice (Agent1→Agent2 drill, independent dogfood project), fixed per dogfood findings 1–4, and verified adoptable from the public GitHub URL. `master` remains the development/research history. Per user direction: the template is now **frozen** — no feature additions until a real use case exposes a problem.

## Specification

Dev `FORGE_SPEC.md` unchanged (17 FR / 5 NFR / 6 AC). Template contract unchanged (16 files).

## Current Task

None IN_PROGRESS. Mode transition: design/build → stabilization/release.

## Completed Work

- `forge-template` branch: `a944298` (initial extract) → `3e8299b` (dogfood fixes 1–4), pushed to origin.
- GitHub adoption test (real URL, fresh repo): fetch → checkout → 16 files → clean commit ✓; INIT Quick Start ✓; tasks.md 0 dev IDs ✓; AGENTS optional ✓.
- `master` pushed to origin (ahead 9 commits).
- Tag `v1.0.0` created on `forge-template` tip (`3e8299b`) and pushed.

## Git State

```text
forge-template: 3e8299b (tag v1.0.0) — pushed
master: a8774ec — pushed (all context commits)
origin: both branches + v1.0.0 tag up to date
```

## Verification Results

```text
$ # fresh repo adoption from https://github.com/SSHRIHARI006/FORGE
$ git remote add forge https://github.com/SSHRIHARI006/FORGE
$ git fetch forge forge-template   → new branch forge/forge-template
$ git checkout forge/forge-template -- .
→ 16 files, git status clean after commit
```

## Important Decisions

- Product artifact = `forge-template` branch (+ tags). Dev history = `master`. Separation maintained.
- Template frozen as of v1.0.0. No new features; fixes only if a real use case exposes a problem (then: branch update → sanitize → adoption test → push).
- Finding 5 (verify tool in template) remains deferred.

## Known Problems

- None blocking. Open user confirmations: `FORGE_SPEC.md` accuracy sign-off, `SPEC.md` retention — both carried as low-priority follow-ups.
- Dev `INIT.md` on master lacks the template's Quick Start section (deliberate: template is the artifact; back-port only if the dev repo itself needs it).

## Next Steps

1. (Optional) Final public README/docs pass — template README already serves as product README.
2. Dogfood follow-ups if/when a real project adopts v1.0.0 and reports friction.
3. Watch for real use cases before un-freezing the template.
# Checkpoint 007 — forge-template Fixes Round 2 (Dogfood Findings 1–4)

Date: 2026-09-05
Type: milestone — template branch updated after dogfood drill; not yet pushed (awaiting review)

## Project State

The `forge-template` branch (was `a944298`) now has a follow-up commit `3e8299b` applying dogfood findings 1–4 from `checkpoint-006.md`. All changes live on the `forge-template` branch; the master dev branch content is untouched (only this checkpoint/KICKOFF/state document the work). The branch has NOT been pushed — the GitHub `forge-template` still points at `a944298` until review.

## Specification

Dev `FORGE_SPEC.md` unchanged (17 FR / 5 NFR / 6 AC). Template `.forge/` contract unchanged: same 16 files, no new infra, no CLI/DB/daemon/runtime/dependency (finding 5 explicitly NOT implemented).

## Current Task

None IN_PROGRESS on master. Template-fix round complete, pending user review of the diff + push decision.

## Completed Work

Branch `forge-template` commit `3e8299b` (parent `a944298`) changes exactly 5 files:

1. **`README.md`** — Option A install now works for a genuinely fresh project whose `origin` is the user's own repo: uses the public Forge URL (`https://github.com/SSHRIHARI006/FORGE`), adds Forge as a dedicated remote (`git remote add forge ...`), fetches `forge forge-template`, checks out `forge/forge-template -- .`. Old instructions assumed `origin` pointed at Forge. Also dropped the dev-only "(ADR-004)" provenance reference.
2. **`.forge/tasks.md`** — placeholder TASK-001 no longer cites dev-spec requirement IDs (`FR-001..FR-013`, `AC-001..AC-002`); the init task's Requirements now explain in words that no project IDs exist until `FORGE_SPEC.md` is created. Verification remains a generic `grep` for the ID pattern. Fixed "conformation" → "confirmation" typo.
3. **`AGENTS.md`** — "Every Session" reading order marks `FORGE_SPEC.md` as **(if present)** and directs pre-init agents to `.forge/INIT.md` instead. Adapter purpose unchanged.
4. **`.forge/INIT.md`** — added a 5-line **Quick Start (Do This First)** section at the top summarizing the workflow with section pointers; the full detailed instructions are unchanged and remain authoritative.
5. **`.forge/state.md`** — dropped dev-only "(ADR-004 extract)" reference.

Not done (per instruction): finding 5 (no verification tool shipped in the template), no CLI/DB/daemon, no changes to master's project content.

## Git State

```text
forge-template branch: 3e8299b402016baa58f0d60d98e4787f045f1908 (parent a944298, 16 files)
Local mirror: ../forge-template/ — byte-identical to branch (verified)
master HEAD: 01632b4 (working tree clean)
Remote: origin/forge-template still a944298 (NOT pushed yet — awaiting review)
```

## Verification Results

Sanitization (in `../forge-template/`):
```text
dev task IDs (TASK-008/009/01x)            → clean
Agent1/Agent2                              → clean
dev checkpoints (002..006)                 → clean
concrete dev req IDs FR/NFR/AC-0xx         → only INIT.md:273 ID-format rule (contract, not dev refs)
dev repo state (paths, revs, dogfood/dscan)→ clean
SSHRIHARI006                               → only the intended public URL in README
```

Branch integrity:
```text
$ git ls-tree -r --name-only forge-template | wc -l            → 16
$ git diff --stat a944298 forge-template                       → 5 files, +35/-12
sha1 comparison of every branch blob vs ../forge-template/     → all identical
master working tree after rebuild                             → clean
```

Fresh adoption test (new repo whose `origin` is the user's own):
```text
$ git remote add origin https://github.com/someuser/my-cool-project.git
$ git remote add forge /home/shrihari/Desktop/forge   # stands in for the public URL
$ git fetch forge forge-template && git checkout forge/forge-template -- .
→ 16 files adopted, commit clean
Readiness: INIT "Quick Start" present; tasks.md has 0 dev FR/AC IDs;
AGENTS.md marks FORGE_SPEC.md "if present"; README shows remote-add + public URL.
```

## Important Decisions

- Template fixes live ONLY on `forge-template` (branch + local mirror); master content stays as-is.
- Finding 5 (verify tool in template) explicitly deferred/declined.
- GitHub branch is deliberately NOT updated until the user reviews the final diff.

## Known Problems

- GitHub `forge-template` still points at the pre-fix commit `a944298` — adopters fetching from GitHub get the old template until push.
- `INIT.md` dev-repo copy (master) lacks the Quick Start; the fix exists only in the template. If desired, back-port later (needs a master change + ADR-style note) — deliberately not done here.

## Next Steps

1. User reviews `git diff a944298..forge-template` (shown in session).
2. On approval: `git push origin forge-template` (updates GitHub to `3e8299b`).
3. Re-run the GitHub-URL adoption test after push to confirm the public flow.
4. Optional follow-up: re-init the dogfood project (`../forge-dogfood/`) with the fixed template, or leave it as the pre-fix reference.
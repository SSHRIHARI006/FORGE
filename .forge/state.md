# Current State

> Placeholder — replace with real content during initialization (see `.forge/INIT.md`).

## Active Task

Initialization (see `.forge/INIT.md`). No project task is IN_PROGRESS yet.

## Current Progress

- Forge template installed: `.forge/` convention + `AGENTS.md` adapter.
- No project-specific context created yet (no `FORGE_SPEC.md`, project rules, tasks, or state).

## Completed

- Template installation only.

## Current Problem

None — pre-initialization state.

## Recent Changes

- Template installed from the Forge `forge-template` branch.

## Verification

Installation check (run in the adopting project):
```text
$ ls .forge/
INIT.md KICKOFF.md checkpoints/ decisions/ rules.md skills/ state.md tasks.md taste/
$ test -f .forge/INIT.md && echo "init ok"
```

## Next Action

Follow `.forge/INIT.md`: discovery → interview → confirmation → create `FORGE_SPEC.md` + populate rules/tasks/state → checkpoint + KICKOFF.

## Important Context

- Source of truth order: user instruction > `FORGE_SPEC.md` > `rules.md` > decisions > skills > taste > assumptions.
- V1 single-agent model: exactly one task IN_PROGRESS at a time.
- Record real command output as verification evidence; claims without output are not done.
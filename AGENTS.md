# AGENTS.md — Forge Adapter

> This repo uses **Forge** as its cross-agent project context. This file is a thin adapter; Forge files are the source of truth. Do not duplicate Forge content here.

## First Run (initializing a fresh checkout)

1. Read `.forge/INIT.md` and follow it exactly (read-only discovery → adaptive interview → confirmation → context creation).
2. Do not modify application code during initialization.
3. Confirm direction with the user before writing Forge files.

## Every Session (continuing work)

Read in order:

1. `FORGE_SPEC.md` (living spec — what/why/requirements/constraints)
2. `.forge/KICKOFF.md` (2-minute resume: task, done, broken, verified, next)
3. `.forge/state.md` (full current state + verification evidence)
4. `.forge/tasks.md` (active task + verification command)
5. `.forge/rules.md` (binding behavior)
6. Relevant `.forge/decisions/`, `.forge/skills/` (only what the task needs), `.forge/taste/preferences.md`
7. `git status`, `git diff --stat`, `git log --oneline -10`

## While Working

- One task `IN_PROGRESS` at a time; trace work to `FR-xxx`/`AC-xxx`.
- Load only relevant skills. Record real command output in `state.md` — "tests pass" without output is not done.
- Record important decisions as `.forge/decisions/ADR-*.md`. Update `state.md` + `tasks.md` + `KICKOFF.md` before stopping so the next agent (possibly a different tool) continues without your conversation.

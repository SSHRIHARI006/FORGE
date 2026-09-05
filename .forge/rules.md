# Project Rules

> How agents must behave in this project. Canonical V1 rule set (repo-level).
> Conflict hierarchy: explicit user instruction > `FORGE_SPEC.md` > this file > decisions > skills > taste > assumptions.

## Specification & Context

- Read `FORGE_SPEC.md` and `.forge/KICKOFF.md` + `state.md` + `tasks.md` before starting work; consult relevant `decisions/` before changing architecture.
- Never invent requirements; never treat assumptions as confirmed. Label assumptions explicitly.
- Record important architectural/product changes as `ADR-*.md`; do not silently rewrite project intent in `FORGE_SPEC.md`.

## Engineering Discipline

- Prefer simple solutions; do not overengineer or add infrastructure for hypothetical future needs.
- Do not add dependencies without a stated reason. Follow the existing architecture and patterns.
- Do not modify public API contracts, security policy, or data migrations without explicit approval.
- Every meaningful task needs explicit verification: `command → execution → result → recorded evidence`. Claiming "tests pass" without pasted output is not done.
- Run the task's `Verification:` command and record real output in `state.md` / `tasks.md` before marking `DONE`. Fix failures with bounded retries; never weaken security to make tests pass.
- Keep changes bounded to the active task. Only one task is `IN_PROGRESS` at a time (V1 single-agent model).

## Safety & Scope

- Never expose or commit secrets/credentials. Reference `.env.example`, never `.env` contents.
- Get human confirmation before destructive operations (db wipe, `rm -rf`, prod deploy, credential changes, security-policy changes).
- Do not modify application code during initialization; initialization is discovery + documentation + confirmation.
- Respect `.forge/taste/preferences.md` as guidance only — it never overrides user instructions, requirements, or safety.

## Handoff

- Before stopping, update `state.md`, `tasks.md`, and `KICKOFF.md` so another agent can continue without your conversation. Create a `checkpoints/checkpoint-*.md` at milestones only.
- Load only relevant skills per task (deterministic match on task content / tech / metadata). Do not inject every skill everywhere.

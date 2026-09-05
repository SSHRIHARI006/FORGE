---
name: testing
description: Reliable testing and verification-evidence practices for Forge tasks
tags:
  - testing
  - pytest
  - verification
  - evidence
---

# Testing Skill

## Goal

Prove work is correct with executable checks and recorded evidence, not assertions. Every meaningful task ends with real command output stored in `state.md` / `tasks.md` / checkpoints.

## Rules

- Each task must declare an executable `Verification:` command before implementation starts.
- Prefer the project's existing runner (`pytest`, `npm test`, `cargo test`, `go test`); add lint/typecheck/build (`ruff`, `mypy`, `tsc`, `npm run build`, `docker build`) and E2E where the risk justifies it.
- Paste actual output (pass and fail) — never write "tests pass" without it.
- Fix failures with bounded retries; if still failing, mark task `FAILED`/`BLOCKED` with the failing output and next hypothesis — do not weaken security or scope to force green.
- Keep tests deterministic; no network-dependent assertions unless the project already requires them.

## Workflow

1. Read task Goal + Requirements (`FR-xxx`/`AC-xxx`) and relevant spec section.
2. Locate existing tests/config; run the baseline verification command first and record output.
3. Implement the smallest change satisfying the acceptance criteria.
4. Re-run verification; on failure, diagnose → fix → rerun (bounded, e.g. ≤3 rounds before escalating to `BLOCKED`).
5. Record final command + full relevant output in `state.md` Verification and update task Status.
6. If the change meaningfully altered behavior, update `KICKOFF.md` and consider a checkpoint.

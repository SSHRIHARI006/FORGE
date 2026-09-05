---
name: security
description: Safe handling of secrets, destructive actions, and security-sensitive changes
tags:
  - security
  - secrets
  - safety
  - review
---

# Security Skill

## Goal

Ensure agents never trade safety for speed: no leaked secrets, no unconfirmed destructive actions, no weakened security to pass tests.

## Rules

- Never print, log, or commit secrets, tokens, or credentials. Reference `.env.example` keys only; never `.env` values.
- Require explicit human confirmation before: destructive DB operations, `rm -rf`-class deletes, production deploys, credential rotation, security-policy changes.
- Respect existing auth/authz, crypto, and data-handling requirements in `FORGE_SPEC.md` and `decisions/`; check them before changing security-sensitive code.
- Verify security-sensitive changes with real checks (tests, scanners, or config review appropriate to the project) and record output.
- Never disable auth, widen CORS, skip validation, or downgrade crypto merely to make tests pass.

## Workflow

1. Identify security surface of the task (secrets, auth, input handling, deps, infra, data).
2. Confirm constraints in spec/rules/decisions; flag conflicts to the user before coding.
3. Implement minimal safe change; keep secrets out of diffs and logs.
4. Run relevant verification (test suite subset, linter/security scanner if configured) and record output.
5. Note residual risks and required human approvals in `state.md` Important Context.

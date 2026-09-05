# Project — Forge

## Overview

Forge is a portable, agent-agnostic project context layer for AI coding agents. It is a **filesystem convention + instruction system** centered on `.forge/` plus a living specification at `FORGE_SPEC.md`.

Problem: each coding agent (Freebuff, OpenCode, Antigravity, others) keeps its own transient understanding. Switching agents or hitting a session limit loses project understanding, decisions, requirements, preferences, progress, and learned context.

Solution: persistent project intelligence lives in the repository. Agents are temporary workers; they read Forge context on entry and update it on exit. The canonical input specification is `SPEC.md` (V1 Specification); this file (`FORGE_SPEC.md`) is the living source of truth derived from it.

V1 delivers portable context + an excellent `INIT.md`. No daemon, database, hosted service, runtime, orchestration, or dashboard.

## Goals

- G-01: Any compatible agent can enter a Forge-enabled repo and become productive without the prior conversation.
- G-02: Specification-before-implementation: agents understand what/why/requirements/constraints/architecture/acceptance before significant coding.
- G-03: Decisions, requirements, verification evidence, and next actions survive agent switches and session limits.
- G-04: Remain lightweight: markdown files, no new infrastructure in V1.
- G-05: Enforce evidence over claims (real command output, not assertions).

## Users

- U-01: Developers using one or more AI coding agents on a shared repository.
- U-02: AI coding agents themselves (Freebuff, OpenCode, Antigravity, compatible others) as consumers and maintainers of Forge context.
- U-03: Future maintainers / auditors needing to reconstruct why the project looks the way it does (via `decisions/`, `checkpoints/`).

## User Workflows

- W-01 — Initialize: agent reads `.forge/INIT.md` → read-only discovery → adaptive user interview → challenge/confirm → creates `FORGE_SPEC.md` + `.forge/` context + initial tasks → verifies understanding.
- W-02 — Continue (cold start): new agent reads `FORGE_SPEC.md` → `.forge/KICKOFF.md` → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status/diff/log` → resumes active task.
- W-03 — Implement task: pick active `TASK-xxx` → load only relevant skills → implement per BUILD/VERIFY/ENGINEER → run verification tools → record evidence in `state.md`/`tasks.md` → update `KICKOFF.md` if work meaningfully changed.
- W-04 — Handoff: agent updates `KICKOFF.md`, `state.md`, `tasks.md`, records ADRs/checkpoint as needed, stops. Next agent continues per W-02.
- W-05 — Milestone: agent writes `checkpoints/checkpoint-*.md` capturing state, git ref, verification, decisions, known problems, next steps.

## Functional Requirements

### FR-001
Initialization instruction: `.forge/INIT.md` tells an agent how to perform read-only discovery, adaptive interview, challenge/recommendation, confirmation, context creation, task planning, and verification. Covers all 20 behaviors in SPEC §26.

### FR-002
Repository discovery: agent inspects directory structure, source, dependencies, config/env (without exposing secrets), DB schema, APIs, frontend/backend, tests, CI/CD, Docker, docs, existing agent instructions, and git history before asking questions.

### FR-003
Adaptive user interview: agent asks high-value questions across product, scope, technical direction, engineering quality, constraints, and definition of done, adapted to discovered facts; never asks what the repo already answers.

### FR-004
Challenge and recommendation: when a requested direction has meaningful consequences, agent explains concern, lists alternatives, recommends, and asks for confirmation; explicit user decisions are preserved.

### FR-005
Living specification: `FORGE_SPEC.md` (this file) with Overview, Goals, Users, Workflows, FR/NFR/AC with stable IDs, Scope, Technical Direction, Constraints, Definition of Done; evolves with project, with important changes recorded in `decisions/`.

### FR-006
Project rules: `.forge/rules.md` defines enforceable agent behavior for this repo; repo-level file is canonical for V1.

### FR-007
Task tracking: `.forge/tasks.md` holds bounded tasks `TASK-xxx` with Status (`READY/IN_PROGRESS/BLOCKED/DONE/FAILED`), Goal, Requirements (`FR-xxx AC-xxx`), Verification command; single active task in V1.

### FR-008
Current state: `.forge/state.md` holds Active Task, Current Progress, Completed, Current Problem, Recent Changes, Verification (real output), Next Action, Important Context; kept fresh as cold-session continuation context.

### FR-009
Kickoff: `.forge/KICKOFF.md` lets a new agent answer in ~2 minutes: what are we building, current task, done/recent, broken, verified, decisions to respect, next action, constraints; updated when work meaningfully changes.

### FR-010
Decisions: `.forge/decisions/ADR-*.md` records important architectural/product decisions with Decision, Context, Alternatives, Reason, Status; agents consult before changing architecture.

### FR-011
Skills: `.forge/skills/<skill>/SKILL.md` provides reusable playbooks with frontmatter (`name, description, tags`) + Goal/Rules/Workflow; V1 `SKILL.md`-only; deterministic selection (task content, tech, metadata, mode), no LLM router.

### FR-012
Taste: `.forge/taste/preferences.md` records learned preferences, distinct from rules; never overrides explicit instructions, requirements, or safety; no automatic promotion of single edits.

### FR-013
Checkpoints: `.forge/checkpoints/checkpoint-*.md` captures milestone snapshots (state, spec ref, task, completed work, git state, verification, decisions, problems, next steps); milestone-based, not continuous.

### FR-014
Handoff without conversation: `KICKOFF.md` + `state.md` + `tasks.md` (+ spec, rules, decisions, skills, taste, git status/diff/log) suffice for a different agent to continue; no dedicated handoff file required in V1.

### FR-015
Verification with evidence: tasks define executable verification (`pytest`, `npm test`, `cargo test`, `go test`, `ruff`, `mypy`, `tsc`, `npm run build`, `docker build`, E2E as applicable); results with real output recorded in state/tasks/checkpoints; BUILD/VERIFY/ENGINEER workflows adapted to risk with bounded retries.

### FR-016
Agent coexistence: Forge context coexists with agent-specific files (`AGENTS.md` etc.) as adapters; never depends exclusively on proprietary memory formats.

### FR-017
Security discipline: never expose/commit secrets, careful env handling, human confirmation for destructive/prod/credential/security-policy actions, verify security-sensitive changes, never weaken security to pass tests.

## Non-Functional Requirements

### NFR-001
Agent-agnostic: identical `.forge/` is usable by Freebuff, OpenCode, Antigravity, and other compatible agents without per-agent forks.

### NFR-002
Lightweight: V1 is markdown + filesystem only; no daemon, DB, service, runtime, dashboard, or parallel-agent infra.

### NFR-003
Readability: a human can read and audit every Forge file without tooling; files stay small, scannable, and link rather than duplicate.

### NFR-004
Stability: IDs (`FR-xxx`, `NFR-xxx`, `AC-xxx`, `TASK-xxx`, `ADR-xxx`) are stable and never reused with a different meaning.

### NFR-005
Recoverability: cold-start continuation from files + git alone must feel like resuming, not restarting (fundamental acceptance criterion).

## Acceptance Criteria

### AC-001
Fresh repo → agent reads `.forge/INIT.md` → performs discovery without modifying app code → conducts adaptive interview (no questions answerable from repo).

### AC-002
Initialization produces useful `FORGE_SPEC.md`, `rules.md`, `tasks.md`, `state.md`, ≥1 ADR, usable skills, `taste/preferences.md`, a checkpoint, and `KICKOFF.md`.

### AC-003
Agent implements the active task and records real verification output (not "tests pass") in `state.md`/`tasks.md`.

### AC-004
Agent stops; a *different* agent with no prior conversation reads Forge context + git status/diff/log and correctly states: what is being built, current task, what is done, what is broken, what is verified, decisions to respect, and next action.

### AC-005
Second agent continues the work without re-asking settled questions or contradicting recorded decisions/rules.

### AC-006
No V1 non-goal infrastructure (DB, dashboard, orchestration runtime, proprietary memory, auto-deploy, LLM skill router, etc.) is introduced.

## Scope

### In Scope
- `.forge/` filesystem convention and all V1 files listed in SPEC §2.
- Excellent `INIT.md` initialization prompt and `KICKOFF.md` cold-start path.
- Living spec, rules, bounded traceable tasks, mutable state, ADRs, minimal skills, manual taste, milestone checkpoints.
- Single-active-agent workflow, file-based handoff, BUILD/VERIFY/ENGINEER verification discipline.
- `AGENTS.md` adapter pointing into Forge (coexistence, not replacement).

### Out of Scope
- New coding model, new coding agent, full agent framework, new CLI (beyond trivial setup), parallel multi-agent execution, automatic orchestration, proprietary memory systems, hosted service, database, web dashboard, advanced taste learning, LLM skill routing, automatic production deployment, complex workflow/state-machine/event infrastructure. (Per SPEC §30; candidates for V2+.)

## Technical Direction

- Canonical format: Markdown with stable IDs; directory layout exactly per SPEC §2 (`FORGE_SPEC.md` at root, `.forge/` with `INIT.md`, `KICKOFF.md`, `rules.md`, `state.md`, `tasks.md`, `decisions/`, `skills/<skill>/SKILL.md`, `taste/preferences.md`, `checkpoints/`).
- No build step for Forge itself in V1; verification is `git status`, file-presence checks, and project-appropriate test/lint/build commands recorded as evidence.
- Agent-specific files are thin adapters referencing Forge, never the source of truth.
- Origin: `SPEC.md` is the frozen V1 input; this `FORGE_SPEC.md` is the living spec going forward.

## Constraints

- Must not depend on any single agent's internal architecture or proprietary memory format.
- Must not encourage unsafe behavior (secrets, destructive ops, weakened security).
- Agent assumptions have lowest authority (see hierarchy: user instruction > `FORGE_SPEC.md` > rules > decisions > skills > taste > assumptions).
- Keep Forge itself simple; no speculative infrastructure (SPEC §3.6).

## Definition of Done

V1 is done when the 17-step scenario in SPEC §29 works end-to-end with real evidence: init → interview → spec/rules/tasks/state/decisions/skills/taste/checkpoint/KICKOFF → implement → verify → handoff → second agent continues without original conversation — and the second agent does not feel like it is starting from zero (SPEC §32).

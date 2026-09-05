# Forge Template

The installable starting point for adopting **Forge** — a portable, agent-agnostic project context layer for AI coding agents. This template contains exactly what a project needs to become Forge-enabled: the `.forge/` convention plus the `AGENTS.md` adapter. Nothing else.

> **The agent is temporary. The project context is persistent.**

## What you get

```text
project/
├── README.md          (this file — you may replace it)
├── AGENTS.md          (thin adapter: agents read it first, Forge is source of truth)
└── .forge/
    ├── INIT.md        (master initialization instructions — read first)
    ├── KICKOFF.md     (2-minute cold-start resume)
    ├── rules.md       (how agents must behave in your project)
    ├── state.md       (mutable current state + verification evidence)
    ├── tasks.md       (bounded tasks traceable to requirements)
    ├── decisions/     (ADRs — why decisions were made)
    ├── skills/        (reusable playbooks: testing, security, specification)
    ├── taste/         (user preferences, guidance only)
    └── checkpoints/   (milestone snapshots)
```

No daemon, database, hosted service, agent runtime, orchestration server, or dashboard — V1 is a **filesystem convention + instruction system**.

## Installation

### Option A — install from the template branch (recommended)

The template lives on the `forge-template` branch of the Forge development repo. To adopt it into your project:

```bash
# From your project root (your repo must already exist)
git fetch origin forge-template:forge-template
# Pull the template files into a subdirectory you can review
git checkout forge-template -- .  # or select files explicitly
```

Then review, keep what applies, and commit. You now have a Forge-enabled project.

### Option B — copy the files manually

Copy `README.md`, `AGENTS.md`, and the `.forge/` directory into your project root. No build step, no dependencies, no install script.

## First run in your project

1. Start your coding agent (Freebuff, OpenCode, Antigravity, or any compatible agent).
2. Tell it to read `.forge/INIT.md` and follow it exactly.
3. The agent will: inspect the repository read-only → interview you → challenge consequential decisions → get your confirmation → write your project's `FORGE_SPEC.md` + project-specific rules/tasks/state → create a checkpoint and KICKOFF.
4. Review the generated context, then let the agent begin implementation one bounded task at a time.

## Working procedure (every session after installation)

1. The agent reads, in order: `FORGE_SPEC.md` (if present) → `.forge/KICKOFF.md` → `.forge/state.md` → `.forge/tasks.md` → `.forge/rules.md` → relevant `decisions/`, `skills/`, `taste/` → `git status` / `git diff` / `git log`.
2. It works the single active task, loading only relevant skills.
3. It verifies with real command output (`command → execution → result → recorded evidence`) and pastes it into `state.md` — "tests pass" without output is not done.
4. Before stopping, it updates `state.md`, `tasks.md`, `KICKOFF.md`, and creates a checkpoint at milestones so a **different agent can continue without the previous conversation**.

## Template hygiene

- The `.forge/` files here are **starting points**. Initialization replaces the placeholder state/tasks/KICKOFF with your project's real context.
- Never leak your project's state back into this template. If you improve the template, contribute changes back to the Forge development repo instead.
- Keep V1 non-goals out: no daemon, DB, dashboard, runtime, or proprietary memory.

## Where this template came from

Extracted from the Forge development repo (ADR-004) after the cross-agent continuation drill passed: a second agent successfully continued a task started by a first agent using only this context + git history. Forge is a shared memory, specification, decision, skill, preference, verification, and handoff layer — the agents do the coding.
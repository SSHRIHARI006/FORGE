# Forge

## Universal Project Context Layer for AI Coding Agents

**Status:** V1 Specification
**Purpose:** Build a portable, agent-agnostic project context system that makes existing AI coding agents work more effectively together.

---

# 1. Vision

Forge is **not another AI coding agent**.

Forge is **not another CLI coding assistant**.

Forge is **not an agent runtime or orchestration framework**.

Forge is a persistent project intelligence layer that lives inside a repository and gives different coding agents a shared understanding of the project.

The core principle is:

> **The agent is temporary. The project context is persistent.**

A project should be able to move between:

* Freebuff
* OpenCode
* Google Antigravity
* other compatible coding agents

without losing project understanding, decisions, requirements, engineering preferences, current progress, or learned context.

The primary artifact is therefore:

```text
.forge/
```

---

# 2. Core Architecture

A Forge-enabled repository looks like:

```text
project/
│
├── FORGE_SPEC.md
│
├── .forge/
│   ├── INIT.md
│   ├── KICKOFF.md
│   ├── rules.md
│   ├── state.md
│   ├── tasks.md
│   │
│   ├── decisions/
│   │   └── ADR-*.md
│   │
│   ├── skills/
│   │   └── <skill>/
│   │       └── SKILL.md
│   │
│   ├── taste/
│   │   └── preferences.md
│   │
│   └── checkpoints/
│       └── checkpoint-*.md
│
└── application/
```

Forge is primarily a **filesystem convention + instruction system**.

V1 does not require:

* a daemon
* a database
* a hosted service
* an agent runtime
* a new coding model
* an orchestration server
* parallel agent infrastructure
* a dashboard

---

# 3. Design Principles

## 3.1 Agent Agnostic

Forge must not depend on the internal architecture of a specific coding agent.

The same `.forge/` directory should be understandable by different agents.

---

## 3.2 Project Context Is the Source of Truth

Agents must not be treated as the permanent owner of project knowledge.

Persistent project knowledge belongs in Forge-managed files.

---

## 3.3 Specification Before Implementation

Agents should understand:

1. what is being built
2. why it is being built
3. important requirements
4. constraints
5. architectural direction
6. acceptance criteria

before significant implementation begins.

---

## 3.4 Evidence Over Claims

An agent saying:

> "The tests pass."

is not evidence.

Actual command output is evidence.

Forge should encourage:

```text
command
→ execution
→ result
→ recorded evidence
```

---

## 3.5 Human Intent Has Priority

Agents may:

* investigate
* recommend
* challenge
* propose

Agents must not silently replace explicit user decisions.

---

## 3.6 Avoid Overengineering

Forge itself must remain simple.

Do not introduce infrastructure merely because it could be useful later.

---

# 4. The Initialization System

The most important V1 feature is:

```text
.forge/INIT.md
```

`INIT.md` is the master initialization instruction given to a coding agent.

It should contain a comprehensive instruction set telling the agent how to initialize a Forge project.

The initialization process is:

```text
READ-ONLY DISCOVERY
        ↓
UNDERSTAND REPOSITORY
        ↓
UNDERSTAND PRODUCT
        ↓
INTERVIEW USER
        ↓
IDENTIFY DECISIONS
        ↓
CHALLENGE IMPORTANT ASSUMPTIONS
        ↓
PROPOSE DIRECTION
        ↓
USER CONFIRMATION
        ↓
CREATE FORGE CONTEXT
        ↓
CREATE INITIAL TASK PLAN
        ↓
VERIFY UNDERSTANDING
```

---

# 5. Initialization Rules

During initialization the agent must:

### First inspect the repository

Inspect as appropriate:

* directory structure
* source code
* package/dependency files
* configuration
* environment configuration
* database structure
* APIs
* frontend
* backend
* tests
* CI/CD
* Docker configuration
* documentation
* existing agent instructions
* relevant git history

The agent must not ask questions whose answers can reliably be determined from the repository.

---

### Do not modify application code

Initialization is primarily an understanding and documentation operation.

The agent must not begin implementation while performing initialization.

It may create or update Forge context after sufficient understanding and user confirmation.

---

# 6. User Interview

The initialization prompt should instruct the agent to ask high-value questions.

The agent should investigate:

## Product

* What are we building?
* Who is it for?
* What problem does it solve?
* What are the primary workflows?
* What is the expected outcome?

## Scope

* What is in scope?
* What is explicitly out of scope?
* What should not be built yet?

## Technical Direction

* Which existing technologies should remain?
* Are there technologies that should be avoided?
* What architecture should be followed?
* Are there important integration requirements?

## Engineering Quality

* Prototype, balanced, or production-grade?
* What testing level is expected?
* What security requirements exist?
* What performance requirements matter?
* What deployment environment is expected?

## Constraints

* Dependencies
* Compatibility
* Cost
* Infrastructure
* Security
* Existing architecture
* API compatibility
* Data constraints

## Definition of Done

Determine what must be true before work is considered complete.

---

# 7. Adaptive Questioning

The agent must not ask a fixed questionnaire blindly.

Questions should depend on what it discovers.

Example:

If Redis is found:

```text
Redis is currently used by the project.

What is its intended role?

- caching
- background jobs
- pub/sub
- sessions
- other
```

If an existing architecture is found:

```text
I found a service/repository architecture already in use.

Should new functionality follow this pattern?

- yes
- no
- modify the architecture
```

The goal is:

> Ask about uncertainty and important decisions, not things already known.

---

# 8. Challenge and Recommendation

When the user's requested direction has meaningful consequences, the agent should not blindly execute it.

It should:

1. explain the concern
2. identify alternatives
3. recommend an approach
4. ask the user to confirm

Example:

```text
You requested microservices.

The current repository is a small application with no
independent deployment or scaling requirements.

This would introduce additional:
- deployment complexity
- service communication
- observability
- failure modes

Recommendation:
Use a modular monolith for the current scope.

Proceed with microservices anyway?
```

The user remains the final decision maker.

---

# 9. `FORGE_SPEC.md`

`FORGE_SPEC.md` is the living project specification.

It answers:

> What are we building?

It should contain, when applicable:

```md
# Project

## Overview

## Goals

## Users

## User Workflows

## Functional Requirements

### FR-001
...

## Non-Functional Requirements

### NFR-001
...

## Acceptance Criteria

### AC-001
...

## Scope

### In Scope
...

### Out of Scope
...

## Technical Direction

## Constraints

## Definition of Done
```

Requirements should use stable identifiers such as:

```text
FR-001
NFR-001
AC-001
```

The specification is living and may evolve as the project changes.

However, important changes should be recorded in decisions/history rather than silently rewriting project intent.

---

# 10. `.forge/rules.md`

Rules describe:

> How should agents behave in this project?

Examples:

```md
- Do not add dependencies without a reason.
- Follow the existing service architecture.
- Never commit secrets.
- Run tests before declaring a feature complete.
- Do not modify public API contracts without approval.
- Prefer simple solutions.
```

Rules can be project-specific.

Global personal rules may later be supplied by an external/global Forge installation, but the repository-level `.forge/rules.md` is the canonical V1 project rule set.

---

# 11. `.forge/tasks.md`

Tasks describe:

> What needs to happen?

Tasks should be bounded and traceable to requirements.

Example:

```md
# Tasks

## TASK-001

Status: DONE

Goal:
Implement user authentication.

Requirements:
FR-003
AC-004

Verification:
pytest tests/auth/

---

## TASK-002

Status: IN_PROGRESS

Goal:
Implement refresh token rotation.

Requirements:
FR-004
AC-006

Verification:
pytest tests/auth/test_refresh.py
```

Possible statuses:

```text
READY
IN_PROGRESS
BLOCKED
DONE
FAILED
```

Only one task is actively worked on in the V1 single-agent model.

---

# 12. `.forge/state.md`

`state.md` describes the current state of the project.

It should contain:

```md
# Current State

## Active Task

TASK-002

## Current Progress

...

## Completed

...

## Current Problem

...

## Recent Changes

...

## Verification

...

## Next Action

...

## Important Context

...
```

This file is intentionally mutable.

It is the primary cold-session continuation context.

---

# 13. `.forge/KICKOFF.md`

`KICKOFF.md` is optimized for a new coding agent entering an existing project.

A new agent should be able to read it and quickly understand:

```text
What are we building?
What is the current task?
What has already been done?
What changed recently?
What is currently broken?
What has been verified?
What should I do next?
What decisions must I respect?
```

Example:

```md
# Current KICKOFF

## Project
...

## Current Task
TASK-017

## Goal
...

## Completed
...

## Current Work
...

## Verification
37 tests passed.

## Current Failure
...

## Important Decisions
...

## Next Action
...

## Constraints
...
```

KICKOFF should be updated when the active work meaningfully changes.

---

# 14. Decisions

Important architectural and product decisions should be stored under:

```text
.forge/decisions/
```

Use:

```text
ADR-001.md
ADR-002.md
...
```

Example:

```md
# ADR-001: Modular Monolith

## Decision

Use a modular monolith.

## Context

The current application does not require independent
service deployment or scaling.

## Alternatives

- Microservices
- Traditional monolith

## Reason

The modular monolith provides clear boundaries without
unnecessary operational complexity.

## Status

Accepted
```

Agents should consult relevant decisions before changing architecture.

---

# 15. Skills

Skills represent:

> Explicit reusable knowledge or playbooks for performing specific types of work.

Example:

```text
.forge/skills/
├── testing/
│   └── SKILL.md
├── debugging/
│   └── SKILL.md
├── security/
│   └── SKILL.md
└── sql-safety/
    └── SKILL.md
```

A skill should contain:

```md
---
name: testing
description: Reliable testing practices
tags:
  - testing
  - pytest
  - verification
---

# Testing Skill

## Goal

...

## Rules

...

## Workflow

...
```

Skills may contain supporting files in the future:

```text
skill/
├── SKILL.md
├── examples/
├── templates/
└── scripts/
```

For V1, `SKILL.md` is sufficient.

---

# 16. Skill Selection

Agents should load only relevant skills.

Do not inject every skill into every task.

Selection can initially be deterministic using:

* task content
* project technologies
* skill metadata
* current mode
* explicit task requirements

Do not build an LLM-based skill router in V1.

---

# 17. Taste

Taste represents:

> Learned preferences about how the user likes software to be built.

Taste is different from rules.

### Rule

Explicit:

```text
Never add dependencies without justification.
```

### Taste

Learned:

```text
User tends to prefer small functions and simple abstractions.
```

Store V1 taste in:

```text
.forge/taste/preferences.md
```

Example:

```md
# User Preferences

## Coding

- Prefer simple implementations.
- Prefer readable code over clever abstractions.

## Architecture

- Avoid unnecessary service boundaries.

## Testing

- Prefer pytest.
```

Taste must never override:

1. explicit user instructions
2. project requirements
3. safety constraints

A single edit should not automatically become a permanent preference.

V1 can use manually or explicitly recorded taste.

Sophisticated automatic taste learning is future work.

---

# 18. Checkpoints

Checkpoints preserve meaningful project milestones.

Store them under:

```text
.forge/checkpoints/
```

Example:

```text
checkpoint-001.md
checkpoint-002.md
```

A checkpoint should capture:

```text
Project state
Current specification
Current task
Completed work
Git state
Verification results
Important decisions
Known problems
Next steps
```

Checkpoints are milestone-based.

Do not create them every few minutes.

---

# 19. Agent Handoff

Forge does not require a dedicated handoff file in V1.

Handoff information should live primarily in:

```text
KICKOFF.md
state.md
tasks.md
```

When an agent stops or reaches a usage/session limit, it should leave enough information for another agent to continue.

The next agent should not need the previous conversation.

It should be able to recover context from:

```text
FORGE_SPEC.md
.forge/KICKOFF.md
.forge/state.md
.forge/tasks.md
.forge/rules.md
.forge/decisions/
.forge/skills/
.forge/taste/
git status
git diff
git log
```

---

# 20. Agent Switching

V1 uses:

> **One active coding agent at a time.**

Possible agents:

```text
Freebuff
OpenCode
Antigravity
```

The agents are workers, not owners of the project.

Example:

```text
Freebuff
   ↓
works on TASK-012
   ↓
updates state
   ↓
stops / reaches limit
   ↓
OpenCode
   ↓
reads Forge context
   ↓
continues TASK-012
```

No parallel agent collaboration is required in V1.

No permanent role assignment is required.

---

# 21. Agent-Specific Instructions

Some agents may use their own instruction files such as:

```text
AGENTS.md
```

Forge should coexist with them.

Forge context is the cross-agent project context.

Agent-specific files are adapters for a particular tool.

Forge must not depend exclusively on any one agent's proprietary memory format.

---

# 22. Verification Philosophy

A coding agent must not be the sole judge of completion.

Verification should be performed using actual tools whenever possible.

Examples:

```text
pytest
npm test
cargo test
go test
ruff
mypy
tsc
npm run build
docker build
E2E tests
```

The actual commands depend on the project.

Results should be recorded in state/tasks/checkpoints where useful.

---

# 23. Build / Verify / Engineer

Forge should support three conceptual workflows.

## BUILD

Goal:

> Produce working code quickly.

Flow:

```text
Task
 ↓
Implement
 ↓
Basic syntax/build check
 ↓
Done
```

Minimal process.

---

## VERIFY

Goal:

> Prove that the implementation works.

Flow:

```text
Task
 ↓
Implement
 ↓
Tests
 ↓
Lint/typecheck/build
 ↓
Run application where relevant
 ↓
E2E where relevant
 ↓
Fix failures
 ↓
Rerun
 ↓
Complete
```

Verification failures should be fixed where reasonably possible.

Retries should be bounded.

---

## ENGINEER

Goal:

> Deliver software using professional engineering practices.

Flow:

```text
Requirement
 ↓
Understand
 ↓
Architecture
 ↓
Plan
 ↓
Implementation
 ↓
Unit tests
 ↓
Integration tests
 ↓
E2E where relevant
 ↓
Security checks
 ↓
Review
 ↓
Documentation
 ↓
Verification
 ↓
Complete
```

The exact workflow is adapted to project risk.

Do not perform expensive checks that have no meaningful value for a tiny change.

---

# 24. Proof and Acceptance

Every meaningful task should ideally have explicit verification.

Example:

```text
TASK-021

Goal:
Implement undo for database mutations.

Requirements:
FR-007

Acceptance:
AC-021:
INSERT can be undone.

AC-022:
UPDATE can be undone.

AC-023:
DELETE can be undone.

Verification:
pytest tests/test_undo.py
```

The task should not be marked complete merely because the agent believes the behavior is correct.

---

# 25. Genesis-Inspired Features

Forge should take inspiration from the strongest ideas in Genesis while remaining much lighter.

Adopt:

* repository discovery
* human discovery interview
* specification-first workflow
* functional/non-functional requirements
* acceptance criteria
* architectural decisions
* bounded task planning
* executable verification
* proof/evidence
* checkpoints
* cold-session kickoff
* read-only project adoption
* explicit project state
* human confirmation for consequential decisions

Do not reproduce Genesis's complete runtime machinery in V1.

Specifically avoid initially implementing:

* separate workflow database
* complex state machine
* dashboard
* event database
* elaborate approval engine
* dedicated orchestration runtime
* proprietary agent execution system

---

# 26. Initialization Prompt Requirements

`.forge/INIT.md` must instruct the agent to behave as a project architect during initialization.

The prompt must explicitly tell the agent:

1. Do not immediately code.
2. Inspect the repository deeply.
3. Distinguish known facts from assumptions.
4. Ask the user high-value questions.
5. Do not ask questions already answered by the repository.
6. Understand product goals.
7. Understand technical direction.
8. Understand constraints.
9. Identify non-goals.
10. Identify acceptance criteria.
11. Challenge risky or unnecessary technical decisions.
12. Recommend alternatives where appropriate.
13. Preserve explicit user decisions.
14. Record important decisions.
15. Create/update Forge context.
16. Create an initial task plan.
17. Verify that the generated context accurately represents the project.
18. Never invent requirements.
19. Never treat assumptions as confirmed requirements.
20. Do not modify application code during initialization.

The initialization prompt should also explain the purpose of every Forge file so that the agent knows how to maintain them.

---

# 27. Persistent Context Hierarchy

When information conflicts, use:

```text
Explicit current user instruction
        ↓
FORGE_SPEC.md
        ↓
Project rules
        ↓
Architectural decisions
        ↓
Relevant skills
        ↓
Taste/preferences
        ↓
Agent assumptions
```

Agent assumptions have the lowest authority.

The agent must explicitly distinguish assumptions from confirmed decisions.

---

# 28. Security Rules

Forge itself must not encourage unsafe behavior.

Agents should:

* never expose secrets
* never commit credentials
* avoid destructive operations without appropriate confirmation
* treat environment variables and credentials carefully
* respect existing security requirements
* verify security-sensitive changes
* avoid weakening security merely to make tests pass

Consequential actions such as destructive database operations, production deployment, credential changes, or security-policy changes should require appropriate human control.

---

# 29. V1 Scope

V1 is complete when a fresh repository can be converted into a Forge-enabled project where a coding agent can:

```text
1. Read .forge/INIT.md
2. Inspect the repository
3. Interview the user
4. Understand project direction
5. Produce a useful FORGE_SPEC.md
6. Produce project rules
7. Produce tasks
8. Produce current state
9. Record important decisions
10. Use relevant skills
11. Record useful taste
12. Create a checkpoint
13. Produce a KICKOFF.md
14. Begin implementation
15. Verify actual work
16. Leave enough context for another agent
17. Allow another agent to continue without the original conversation
```

---

# 30. Explicit Non-Goals for V1

Do NOT build:

* a new coding model
* a new coding agent
* a full agent framework
* a new CLI unless required only for installation/setup
* parallel multi-agent execution
* automatic agent orchestration
* agent-specific proprietary memory systems
* a hosted service
* a database
* a web dashboard
* an advanced taste-learning model
* an LLM skill-routing system
* automatic production deployment
* complex workflow infrastructure

These may be considered later.

---

# 31. Future Direction

Potential future versions:

### V1

Portable project context.

```text
.forge/
+
excellent INIT.md
```

### V2

Smarter context and automatic agent handoff.

### V3

Automatic taste learning and better skill discovery.

### V4

Parallel independent agents and specialized workflows.

### V5

Optional autonomous deployment and infrastructure workflows.

Future functionality must not compromise the core principle:

> **Forge should remain a lightweight shared intelligence layer rather than becoming another monolithic coding agent.**

---

# 32. Definition of Success

Forge succeeds if this scenario works:

```text
Fresh repository
       ↓
Agent runs /init
       ↓
Agent reads .forge/INIT.md
       ↓
Deep repository discovery
       ↓
Useful user interview
       ↓
Clear project understanding
       ↓
FORGE_SPEC + context created
       ↓
Agent implements a task
       ↓
Verification produces real evidence
       ↓
Agent updates project context
       ↓
Agent stops
       ↓
Different coding agent starts
       ↓
Reads .forge/
       ↓
Understands the project
       ↓
Continues the work
```

The second agent should **not feel like it is starting from zero**.

That is the fundamental acceptance criterion for Forge.

---

# 33. Final Principle

Forge is a **shared memory, specification, decision, skill, preference, verification, and handoff layer for AI coding agents**.

The agents do the coding.

Forge makes sure they understand **what they are coding, why they are coding it, how the project should be built, what has already happened, what decisions have been made, and what must happen next.**

The project context survives the agent.

The agent does not become the project.

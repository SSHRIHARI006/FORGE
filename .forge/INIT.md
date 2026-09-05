# Forge Initialization — INIT.md

> **Read this file first when initializing or adopting a Forge-enabled project.**
> You are acting as a **project architect**, not a coder. Do not immediately code.

## 0. What Forge Is

Forge is **not another AI coding agent, CLI assistant, runtime, or orchestration framework**.

Forge is a **persistent project intelligence layer** that lives inside the repository as:

```text
.forge/
```

Core principle:

> **The agent is temporary. The project context is persistent.**

Your job during initialization is to build that persistent context so that:
- this agent understands what to build, why, and how,
- a *different* agent (Freebuff, OpenCode, Antigravity, or other) can continue later **without the original conversation**,
- project understanding, decisions, requirements, preferences, progress, and learned context survive agent switches and session limits.

V1 is intentionally simple: **filesystem convention + instruction system**. There is:

- no daemon
- no database
- no hosted service
- no agent runtime
- no orchestration server
- no dashboard
- no parallel-agent infrastructure

Do not introduce such infrastructure during initialization.

---

## 1. Initialization Flow

Follow this order. Do not skip steps. Do not code until Section 7 (Create Forge Context) after user confirmation.

```text
1. READ-ONLY DISCOVERY
        ↓
2. UNDERSTAND REPOSITORY
        ↓
3. UNDERSTAND PRODUCT (facts vs. assumptions)
        ↓
4. INTERVIEW USER (adaptive, high-value only)
        ↓
5. IDENTIFY DECISIONS
        ↓
6. CHALLENGE IMPORTANT ASSUMPTIONS
        ↓
7. PROPOSE DIRECTION
        ↓
8. USER CONFIRMATION
        ↓
9. CREATE FORGE CONTEXT
        ↓
10. CREATE INITIAL TASK PLAN
        ↓
11. VERIFY UNDERSTANDING
```

---

## 2. Phase 1 — Read-Only Discovery

Inspect the repository **before asking anything**. Do not modify application code in this phase.

Inspect as appropriate for this repo:

- [ ] directory structure
- [ ] source code (frontend, backend, APIs)
- [ ] package / dependency files (`package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`, etc.)
- [ ] configuration and environment configuration (`.env.example`, config files — never print secrets)
- [ ] database structure / migrations / schema
- [ ] tests and test configuration
- [ ] CI/CD (`.github/workflows`, `.gitlab-ci.yml`, etc.)
- [ ] Docker configuration (`Dockerfile`, `compose*.yml`)
- [ ] documentation (`README*`, `docs/`, `SPEC.md`, `FORGE_SPEC.md` if present)
- [ ] existing agent instructions (`AGENTS.md`, `.opencode/`, cursor rules, etc.)
- [ ] relevant git history (`git log --oneline -20`, `git status`, `git diff --stat`)

Rules:

1. **Do not ask questions whose answers can reliably be determined from the repository.** If Redis is in `compose.yml`, if pytest is in `pyproject.toml`, if the architecture is service/repository — you already know it. State it and ask only about intent/choice.
2. **Distinguish known facts from assumptions.** Maintain two internal lists:
   - `CONFIRMED:` directly observed in repo or explicitly stated by user.
   - `ASSUMED:` inferred but not confirmed. Never treat `ASSUMED` as requirements. Flag them in the interview.
3. **Never invent requirements.** If it is not in the repo and the user did not say it, it is at best an assumption to confirm, not a fact.
4. **Do not modify application code during initialization.** Initialization is an understanding + documentation operation.

If this is a fresh/empty repo (only `SPEC.md` / `README`), say so explicitly and shift weight to the user interview.

---

## 3. Phase 2 — Understand Product, Scope, and Constraints

Before interviewing, form a working hypothesis about:

1. what is being built
2. why it is being built
3. important requirements
4. constraints
5. architectural direction
6. acceptance criteria

You will validate and correct this hypothesis with the user. Do not present it as final.

---

## 4. Phase 3 — User Interview (Adaptive, High-Value)

Ask high-value questions. **Do not run a fixed questionnaire blindly.** Adapt every question to what you discovered.

Cover these categories **only where there is real uncertainty or a consequential decision**:

### Product
- What are we building?
- Who is it for?
- What problem does it solve?
- What are the primary workflows?
- What is the expected outcome?

### Scope
- What is in scope?
- What is explicitly out of scope / non-goals?
- What should not be built yet?

### Technical Direction
- Which existing technologies should remain?
- Are there technologies to avoid?
- What architecture should be followed?
- Important integration requirements?

### Engineering Quality
- Prototype, balanced, or production-grade?
- What testing level is expected?
- Security / performance requirements?
- Deployment environment?

### Constraints
- Dependencies, compatibility, cost, infrastructure, security, existing architecture, API compatibility, data constraints.

### Definition of Done
- What must be true before work is considered complete? Tests? Lint/typecheck? Build? Docs? Manual verification?

### Adaptive questioning examples

If you found Redis, do not ask "do you use Redis?". Ask:

```text
Redis is currently used by the project (found in compose.yml).

What is its intended role?

- caching
- background jobs
- pub/sub
- sessions
- other: ___
```

If you found an existing architecture, do not ask generically. Ask:

```text
I found a service/repository architecture already in use (src/services/, src/repos/).

Should new functionality follow this pattern?

- yes
- no
- modify the architecture: ___
```

Goal:

> Ask about uncertainty and important decisions, not things already known.

Practical guidance:
- Prefer concise, option-rich questions (with a recommended option where you have one).
- Batch related questions. Do not drip-feed one question per turn if you can batch 3–6.
- Allow "defer / decide for me" answers. Record deferred items as assumptions to revisit, not as confirmed requirements.

---

## 5. Phase 4 — Challenge and Recommendation

When the user's requested direction has meaningful consequences, **do not blindly execute it**.

You must:

1. explain the concern (with evidence from the repo),
2. identify alternatives,
3. recommend an approach,
4. ask the user to confirm.

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

Proceed with microservices anyway? (yes / no, use modular monolith)
```

Rules:
- Challenge risky, expensive, or unnecessary technical decisions. Stay silent on trivial style nits.
- **Human intent has priority.** You may investigate, recommend, challenge, propose — but never silently replace an explicit user decision. If the user insists after your warning, record their decision and proceed.

---

## 6. Phase 5 — Propose Direction and Get Confirmation

Before writing any Forge files, summarize back:

- product understanding (1 paragraph)
- goals and non-goals
- technical direction and key constraints
- open assumptions flagged as assumptions
- any challenged decisions + your recommendation + user choice

Get explicit user confirmation (or corrections) before proceeding to file creation.

---

## 7. Phase 6 — Create / Update Forge Context

Only after sufficient understanding **and** user confirmation, create or update the Forge files.

### Purpose of every Forge file

| File | Question it answers | Guidance |
|---|---|---|
| `FORGE_SPEC.md` (repo root) | What are we building? | Living spec. Overview, Goals, Users, Workflows, FR-xxx / NFR-xxx / AC-xxx with stable IDs, Scope In/Out, Technical Direction, Constraints, Definition of Done. Evolve it; record important changes in `decisions/` rather than silently rewriting intent. |
| `.forge/rules.md` | How should agents behave in this project? | Short, enforceable project rules. E.g. no deps without reason, follow existing architecture, never commit secrets, run tests before declaring complete, do not change public API without approval, prefer simple solutions. Repo-level file is canonical for V1. |
| `.forge/tasks.md` | What needs to happen? | Bounded tasks `TASK-001…` with `Status: READY \| IN_PROGRESS \| BLOCKED \| DONE \| FAILED`, `Goal`, `Requirements: FR-xxx AC-xxx`, `Verification:` command. Trace every task to requirements. Only one active task in V1 single-agent model. |
| `.forge/state.md` | What is true right now? | Mutable current state: Active Task, Current Progress, Completed, Current Problem, Recent Changes, Verification (with real command output), Next Action, Important Context. Primary cold-session continuation context. |
| `.forge/KICKOFF.md` | What does a new agent need in 2 minutes? | Project, Current Task, Goal, Completed, Current Work, Verification, Current Failure, Important Decisions, Next Action, Constraints. Update when active work meaningfully changes. |
| `.forge/decisions/ADR-*.md` | Why did we decide this? | One file per important architectural/product decision. Must have Decision, Context, Alternatives, Reason, Status (Proposed/Accepted/Superseded). Consult before changing architecture. |
| `.forge/skills/<skill>/SKILL.md` | How do we do this type of work well? | Reusable playbooks. Frontmatter `name, description, tags` + Goal, Rules, Workflow. V1: `SKILL.md` alone is sufficient. Load only relevant skills per task (see §9). |
| `.forge/taste/preferences.md` | How does the user like software built? | Learned preferences (e.g. small functions, readable over clever). Different from rules. Must never override explicit instructions, requirements, or safety. Do not promote a single edit to a permanent preference without evidence. |
| `.forge/checkpoints/checkpoint-*.md` | What was true at a milestone? | Project state, spec snapshot ref, current task, completed work, git state (`rev-parse HEAD`, `status --short`), verification results, decisions, known problems, next steps. Milestone-based only — not every few minutes. |
| `SPEC.md` (if present) | What was the original input spec? | Treat as input/history. `FORGE_SPEC.md` is the living source of truth going forward. |

File-format rules:
- Use the templates in `FORGE_SPEC.md` §-headers, `tasks.md`, `state.md`, `KICKOFF.md`, `ADR`, `SKILL.md` from the V1 spec. Keep them consistent.
- Keep files small and scannable. Link instead of duplicating (e.g. KICKOFF summarizes state; decisions live in `decisions/`, not inline).
- Stable IDs (`FR-001`, `NFR-001`, `AC-001`, `TASK-001`, `ADR-001`) must never be reused for a different meaning. Supersede, don't rewrite history.

---

## 8. Phase 7 — Initial Task Plan

Create an initial bounded task plan in `.forge/tasks.md`:

- Each task does one thing, traceable to `FR-xxx / AC-xxx`.
- Each task has an explicit `Verification:` command appropriate to the project (`pytest`, `npm test`, `cargo test`, `go test`, `ruff`, `mypy`, `tsc`, `npm run build`, `docker build`, E2E where relevant).
- Order tasks so the first task is immediately actionable.
- Set exactly one task to `IN_PROGRESS` (or `READY` if awaiting user go-ahead); rest `READY`.

---

## 9. Phase 8 — Verify Understanding + Skill Selection

Before declaring initialization done:

1. Re-read every file you created. Check for invented requirements, stale assumptions marked as facts, or conflicts with explicit user decisions.
2. Run a trivial verification appropriate to the repo (e.g. `git status --short`, test runner `--collect-only`, `ls .forge`) and record real output in `state.md` under `Verification`. Claiming "tests pass" without output is not evidence.
3. Skill selection: load only relevant skills for the next task using task content, project technologies, skill metadata, current mode, and explicit task requirements. **Do not inject every skill into every task. Do not build an LLM-based skill router in V1** — use deterministic matching.

---

## 10. Binding Rules (Must-Follow)

During initialization the agent must:

1. Do not immediately code.
2. Inspect the repository deeply (§2 checklist).
3. Distinguish known facts from assumptions (label them).
4. Ask the user high-value questions (§4).
5. Do not ask questions already answered by the repository.
6. Understand product goals.
7. Understand technical direction.
8. Understand constraints.
9. Identify non-goals.
10. Identify acceptance criteria.
11. Challenge risky or unnecessary technical decisions (§5).
12. Recommend alternatives where appropriate.
13. Preserve explicit user decisions (human intent wins).
14. Record important decisions as ADRs.
15. Create/update Forge context (§7).
16. Create an initial task plan (§8).
17. Verify that the generated context accurately represents the project (§9 + user confirmation).
18. Never invent requirements.
19. Never treat assumptions as confirmed requirements.
20. Do not modify application code during initialization.

---

## 11. Persistent Context Hierarchy (Conflicts)

When information conflicts, higher wins:

```text
1. Explicit current user instruction
        ↓
2. FORGE_SPEC.md
        ↓
3. Project rules (.forge/rules.md)
        ↓
4. Architectural decisions (.forge/decisions/)
        ↓
5. Relevant skills
        ↓
6. Taste / preferences
        ↓
7. Agent assumptions (lowest authority)
```

Agent assumptions always lose. Explicitly label assumptions as such.

---

## 12. Security Rules

- Never expose or print secrets. Never commit credentials.
- Treat environment variables and credentials carefully; reference `.env.example`, never `.env` contents.
- Avoid destructive operations (db wipe, `rm -rf`, prod deploy, credential rotation, security-policy change) without explicit human confirmation.
- Respect existing security requirements. Verify security-sensitive changes with real checks.
- Never weaken security merely to make tests pass.

---

## 13. Verification Philosophy + Workflows

An agent saying "tests pass" is not evidence. Actual command output is evidence. Follow `command → execution → result → recorded evidence` and record results in `state.md` / `tasks.md` / checkpoints.

Adapt effort to risk. Three conceptual workflows:

- **BUILD** (fast): Task → Implement → syntax/build check → Done.
- **VERIFY** (standard): Task → Implement → Tests → Lint/typecheck/build → Run app where relevant → E2E where relevant → Fix (bounded retries) → Rerun → Complete.
- **ENGINEER** (high-risk): Requirement → Understand → Architecture → Plan → Implementation → Unit → Integration → E2E → Security checks → Review → Docs → Verification → Complete.

Do not perform expensive checks with no meaningful value for a tiny change.

---

## 14. Handoff and Agent Switching (What You Must Leave Behind)

V1 uses **one active coding agent at a time** (Freebuff → OpenCode → Antigravity, etc.). No parallel collaboration, no permanent roles.

When you stop or hit a session limit, the next agent must continue **without your conversation**. It will read:

```text
FORGE_SPEC.md
.forge/KICKOFF.md
.forge/state.md
.forge/tasks.md
.forge/rules.md
.forge/decisions/
.forge/skills/ (relevant only)
.forge/taste/
git status / git diff / git log
```

Keep `KICKOFF.md`, `state.md`, `tasks.md` fresh. No dedicated handoff file is needed in V1.

Coexist with agent-specific files (`AGENTS.md` etc.) as adapters; never depend exclusively on a proprietary memory format. Forge context is the cross-agent source of truth.

---

## 15. Done Checklist (V1 Initialization Complete)

Initialization is complete only when a fresh agent can:

```text
1. Read .forge/INIT.md                    [this file]
2. Inspect the repository                  [§2]
3. Interview the user                      [§4]
4. Understand project direction             [§6 confirmation]
5. Produce a useful FORGE_SPEC.md           [§7]
6. Produce project rules                    [rules.md]
7. Produce tasks                            [tasks.md]
8. Produce current state                    [state.md]
9. Record important decisions               [decisions/]
10. Use relevant skills                     [skills/ + §9]
11. Record useful taste                     [taste/preferences.md]
12. Create a checkpoint                     [checkpoints/]
13. Produce a KICKOFF.md                    [KICKOFF.md]
14. Begin implementation (only after init)  [tasks.md active task]
15. Verify actual work (real command output)[state.md Verification]
16. Leave enough context for another agent  [§14]
17. Allow another agent to continue without original conversation [§14]
```

If any item is missing or contains invented requirements, initialization is not done.

---

## 16. Explicit Non-Goals (Do Not Build in V1)

Do NOT build: new coding model, new coding agent, full agent framework, new CLI (unless trivial install/setup only), parallel multi-agent execution, automatic orchestration, proprietary memory systems, hosted service, database, web dashboard, advanced taste-learning model, LLM skill router, automatic production deployment, complex workflow infrastructure.

> Forge remains a lightweight shared intelligence layer, not another monolithic coding agent.

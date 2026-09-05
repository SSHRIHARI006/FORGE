# Forge

Forge is a persistent, agent-agnostic project context layer for AI coding agents. It gives Freebuff, OpenCode, Antigravity, and other compatible agents a shared understanding of the same repository, so project knowledge survives agent switches and session limits.

The core idea:

> **AI coding agents are temporary. Project context should not be.**

## What Forge is not

This distinction matters:

- Forge is **not** another coding agent, LLM, or CLI assistant.
- Forge is **not** a replacement for Freebuff, OpenCode, or Antigravity — those agents do the coding.
- Forge is **not** a new agent runtime, orchestration server, database, dashboard, or hosted service.
- Forge does **not** run agents in parallel in V1.

Forge is a **filesystem convention + instruction system**: a `.forge/` directory plus a living specification at `FORGE_SPEC.md`. Agents read it on entry and update it on exit.

## The problem

When several coding agents work on one repository, the important context tends to live inside one agent's conversation or proprietary memory: what the project is, what was already built, why it was built that way, what remains, what is broken, what to do next.

When that agent stops, hits a usage limit, or is replaced, the next agent rediscovers all of it from scratch.

Forge moves that context into the repository:

```text
Project
   ↓
.forge/  +  FORGE_SPEC.md
   ↓
shared project context
   ↓
Freebuff / OpenCode / Antigravity / other agents
```

## How Forge works

1. **Initialize.** An agent reads `.forge/INIT.md` and performs read-only repository discovery.
2. **Interview.** The agent asks high-value product and engineering questions, adapted to what the repo already answers.
3. **Record.** The agent writes the resulting context: spec, rules, tasks, state, decisions, skills, taste, checkpoint, kickoff.
4. **Work.** Agents implement bounded tasks traced to requirements.
5. **Verify.** Agents run real commands and paste real output as evidence.
6. **Update.** Agents refresh state, tasks, and kickoff before stopping.
7. **Continue.** A different agent later reads the persisted context and resumes without the original conversation.

Initialization is deliberately more than a repo scan. `.forge/INIT.md` instructs the initializing agent to:

- inspect structure, source, dependencies, config, tests, CI/CD, Docker, docs, and git history **before asking anything**;
- separate confirmed facts from assumptions, and never present assumptions as requirements;
- ask only high-value questions, never questions the repo already answers;
- challenge consequential technical decisions with alternatives and a recommendation, while preserving explicit user decisions;
- create the persistent context only after user confirmation;
- **not modify application code during initialization**.

## Repository layout

Based on `SPEC.md` §2 and this repo today:

```text
.
├── FORGE_SPEC.md
├── SPEC.md
├── AGENTS.md
├── tools/
│   └── forge_verify.py
├── tests/
│   └── test_forge_verify.py
└── .forge/
    ├── INIT.md
    ├── KICKOFF.md
    ├── rules.md
    ├── state.md
    ├── tasks.md
    ├── decisions/
    │   ├── ADR-001.md
    │   ├── ADR-002.md
    │   └── ADR-003.md
    ├── skills/
    │   ├── testing/SKILL.md
    │   ├── security/SKILL.md
    │   └── specification/SKILL.md
    ├── taste/
    │   └── preferences.md
    └── checkpoints/
        ├── checkpoint-001.md
        ├── checkpoint-002.md
        └── checkpoint-003.md
```

| File | Purpose |
| ---- | ------- |
| `FORGE_SPEC.md` | Living project specification (goals, users, workflows, FR/NFR/AC with stable IDs, scope, direction, constraints, done) |
| `INIT.md` | Master initialization instructions (discovery → interview → challenge → confirm → create → verify) |
| `KICKOFF.md` | Cold-start summary: task, done, broken, verified, decisions, next action (~2 minutes to resume) |
| `rules.md` | Enforceable project behavior for agents in this repo |
| `state.md` | Mutable current state + pasted verification evidence |
| `tasks.md` | Bounded tasks `TASK-xxx` with status, goal, requirements, verification command |
| `decisions/` | Architecture/product decisions (`ADR-*.md`: Decision, Context, Alternatives, Reason, Status) |
| `skills/` | Reusable playbooks (`SKILL.md` + Goal/Rules/Workflow) |
| `taste/` | Recorded user preferences (guidance only, never overrides requirements/safety) |
| `checkpoints/` | Milestone snapshots (state, git ref, verification, problems, next steps) |

`SPEC.md` is the frozen original V1 input for the Forge project itself. `FORGE_SPEC.md` is the living specification going forward.

Agent entry order (per `AGENTS.md`): `FORGE_SPEC.md` → `KICKOFF.md` → `state.md` → `tasks.md` → `rules.md` → relevant `decisions/` + `skills/` + `taste/` → `git status` / `git diff` / `git log`.

## Multi-agent handoff

The strongest test of Forge is continuity, not parallelism. V1 intentionally supports **one active coding agent at a time** (ADR-002). There is no dedicated handoff file; handoff lives in `KICKOFF.md` + `state.md` + `tasks.md` plus git history.

```text
Freebuff
   ↓
implements TASK-008 (partial)
   ↓
updates .forge/state.md
updates .forge/KICKOFF.md
creates checkpoint-003
   ↓
stops / reaches limit
   ↓
OpenCode (fresh session, no prior conversation)
   ↓
reads .forge/ + git status/diff/log
   ↓
understands previous work
   ↓
continues the task (TASK-009)
```

The handoff succeeds if the second agent can answer — from files alone — what is being built, what was done, why, what remains, what failed, and what to do next, without re-asking settled questions or contradicting recorded decisions.

## Design influences

Forge takes inspiration from disciplined agent-development practices — discovery before implementation, specification-first work, explicit decisions, bounded tasks, executable verification, checkpoints, cold-session handoff — while keeping the implementation lightweight and filesystem-based (ADR-001). It is not a runtime, state machine, event database, or dashboard.

## Skills

Skills are reusable instruction playbooks for kinds of work:

```text
.forge/skills/
└── testing/
    └── SKILL.md
```

This repo has three: `testing`, `security`, `specification`. Each `SKILL.md` carries `name` / `description` / `tags` frontmatter plus Goal, Rules, and Workflow. Agents load **only relevant skills** per task (deterministic match on task content and tech). There is no LLM-based skill router in V1.

## Taste

Taste is separate from skills. Skills are explicit knowledge; taste is preference guidance, for example:

- prefer simple implementations and readable code over clever abstractions;
- no new dependencies without a stated reason;
- keep Forge files small and link instead of duplicating.

Taste never overrides explicit user instructions, requirements, or safety. V1 taste is manually recorded in `.forge/taste/preferences.md`. There is no automatic preference learning.

## Verification

An agent claiming "it works" is not proof. Forge requires `command → execution → result → recorded evidence`, with real output pasted into `state.md` / `tasks.md` / checkpoints.

This repo verifies its own structure today with:

```bash
python3 tools/forge_verify.py
python3 -m unittest discover -s tests -t . -v
```

`tools/forge_verify.py` checks required files/directories exist, counts `FR`/`NFR`/`AC` IDs in `FORGE_SPEC.md` (expected 17/5/6), and counts ADRs/skills/checkpoints. The test suite (stdlib `unittest`, no extra dependencies, Python 3.12) covers the same checks. `check_git_state()` and `check_kickoff_freshness()` are intentionally unimplemented stubs reserved for the TASK-009 continuation exercise.

## Current V1 status

Transparent status as of 2026-09-05 (`TASK-001`–`TASK-007` DONE, `TASK-008` IN_PROGRESS, `TASK-009` READY):

Implemented:

- Forge context structure (`.forge/` + `FORGE_SPEC.md` + `AGENTS.md` adapter)
- Initialization instructions (`.forge/INIT.md`, 20 binding behaviors)
- Living specification (17 FR / 5 NFR / 6 AC), project rules, tasks, state, kickoff
- 3 ADRs, 3 skills, taste preferences, 3 checkpoints
- Structural verification (`tools/forge_verify.py` + tests, green)

Still being validated:

- **Real cross-agent cold-start continuation.** The pilot is set up exactly for this: Agent1 implemented the first half of `tools/forge_verify.py` and stopped at `checkpoint-003`; Agent2 (a different agent, no prior conversation) must implement the two remaining stubs from files + git alone. Until that drill passes, multi-agent continuation is the goal being tested, not a proven result.

## Quick start

There is no Forge CLI and no install mechanism in V1. Do not expect commands like `forge init` — they do not exist. The workflow is repository- and context-based:

1. Copy the `.forge/` convention (plus `FORGE_SPEC.md` and the `AGENTS.md` adapter pattern) into a project.
2. Start your coding agent normally.
3. Have it initialize using `.forge/INIT.md` (discovery → interview → confirmation → context creation).
4. Review the generated spec, rules, tasks, and decisions.
5. Have the agent work one bounded task at a time, verifying with real command output.
6. Have the agent update `state.md`, `tasks.md`, and `KICKOFF.md` before stopping.
7. Later, start a different agent and have it read the Forge context + git history before continuing.

## Design philosophy

Keep the intelligence in the project, not trapped inside the agent.

- Agent-agnostic: same `.forge/` works across tools, no proprietary memory formats.
- Filesystem-first: Markdown + git, readable without tooling.
- Specification-first: what/why/requirements/constraints/acceptance before significant code.
- Evidence over claims: pasted command output, not assertions.
- Explicit decisions: ADRs record the why; assumptions are labeled, never requirements.
- Persistent context: kickoff, state, tasks, and checkpoints outlive any session.
- Minimal infrastructure: no daemon, DB, service, or dashboard in V1.
- Human intent is authoritative (instruction > spec > rules > decisions > skills > taste > assumptions).

## Roadmap

V1: portable shared project context and file-based agent handoff. Nothing more.

Future ideas (not built, no timeline committed): smarter taste learning, automatic context selection, improved handoff ergonomics, optional orchestration, parallel agents, deployment workflows.

---
name: specification
description: Specification-first workflow — FR/NFR/AC with stable IDs, scope control, and decision recording
tags:
  - specification
  - requirements
  - acceptance-criteria
  - adr
---

# Specification Skill

## Goal

Keep `FORGE_SPEC.md` as the living source of truth: well-formed requirements with stable IDs, explicit scope, and traceability from tasks and decisions.

## Rules

- Use stable IDs `FR-xxx` / `NFR-xxx` / `AC-xxx`; never reuse an ID with a new meaning — supersede instead.
- Every task traces to at least one requirement ID; every acceptance criterion is verifiable by a concrete check.
- Separate facts (`CONFIRMED`) from assumptions (`ASSUMED`); never promote an assumption without user confirmation.
- Record consequential changes as ADRs (Decision/Context/Alternatives/Reason/Status); do not silently rewrite intent.
- Keep spec sections small: Overview, Goals, Users, Workflows, Requirements, Scope In/Out, Technical Direction, Constraints, Definition of Done.

## Workflow

1. Extract what/why/requirements/constraints/architecture/acceptance from repo + user before writing.
2. Draft or update `FORGE_SPEC.md` sections with new stable IDs only for genuinely new items.
3. Link tasks (`Requirements: FR-xxx AC-xxx`) and ADRs back to the spec.
4. Ask the user to confirm spec changes that alter scope, direction, or acceptance criteria.
5. After confirmation, update `state.md` / `KICKOFF.md` summaries to match.

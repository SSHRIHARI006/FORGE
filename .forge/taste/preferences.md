# User Preferences

> Learned preferences about how the user likes software built. Guidance only.
> Never overrides: (1) explicit user instructions, (2) project requirements, (3) safety constraints.
> Do not promote a single edit into a permanent preference without repeated evidence. V1 is manual/explicit only.

## Coding

- Prefer simple implementations; readable code over clever abstractions.
- Prefer small, focused functions and clear boundaries (modular monolith over premature services).
- No new dependencies without a stated reason.

## Architecture

- Avoid unnecessary service boundaries and speculative infrastructure.
- Follow existing patterns in the repo unless the user approves a change (recorded as ADR).

## Testing

- Prefer the project's existing runner (e.g. pytest where Python); executable verification with pasted output over claims.
- Fix failures with bounded retries; record blocking failures with evidence rather than forcing green.

## Documentation

- Keep Forge files small and scannable; link instead of duplicating.
- Record the *why* in decisions/, the *what-now* in state/KICKOFF, the *what-next* in tasks.

## Process

- Specification before implementation for consequential work; challenge risky direction with alternatives + recommendation, then defer to explicit user choice.

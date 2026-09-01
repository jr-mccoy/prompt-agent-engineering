# ADR-0015 — The registry carries serving-policy metadata, and its default fails closed

## Status

Accepted. Implemented in Phase 2. Enforcement is deliberately not implemented.

## Context

The PAE Engine does not exist yet, but the registry it will consume is being frozen
now. Some resources here cannot be served the way ordinary documentation is served.

The corpus contains 589 resources marked `intended_use: model-testing` — the
`domain-psychology` prompts, for instance, are authored at full clinical fidelity and
explicitly flagged as not for live clinical use. It contains 64 resources carrying a
`STRONG-GUARD` marker, 110 with a Safety Block heading, 22 authorized-offensive
bug-bounty prompts whose authorization and scope gate *is* the point of the prompt,
and 1,238 resources in safety-sensitive domains.

For every one of those, the disclaimers are not preamble to be trimmed to fit a
context window. They are load-bearing content.

Retrofitting this after identity is frozen and consumers exist would be far harder
than recording it now.

## Decision

Every record carries a `serving_policy` with a value and the list of triggers that
produced it.

```
standard        full content may be served
safety_gated    servable only whole; guard sections must never be truncated
metadata_only   title, description and ID only
excluded        not served at all
```

**The fail-closed default is `metadata_only`.** Generation always populates the
field, so an absent value means a bug — and the failure mode of a bug must be
withholding content, not leaking it.

Values are computed from deterministic triggers, the most restrictive wins, and every
trigger that fired is recorded in `basis`. Safety-gated records additionally carry a
`guard_preservation` block so a future context compiler knows what it may not drop.

**Nothing is `excluded` automatically.** Exclusion is a maintainer decision recorded
in `overrides/`, never an inference.

No serving, gating or truncation behaviour is implemented in this phase. This ADR
records metadata only.

## Consequences

- 1,319 resources are marked `safety_gated` and 56 `metadata_only` at migration, each
  with its reasons attached.
- A future engine has the information it needs to refuse rather than truncate.
- The trigger list is a maintenance surface: a new safety-sensitive domain must be
  added to it, and the summary counts make an unexpected shift visible.

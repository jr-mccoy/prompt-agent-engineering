# ADR-0030 — stdio first; HTTP deferred

## Status

Accepted. Implemented in Phase 6.

## Context

The MCP SDK supports stdio and Streamable HTTP. Supporting both looked like a
configuration flag, and the SDK installs the HTTP stack either way, so the
marginal cost of "just adding `--http`" appeared to be nearly zero.

It is not nearly zero. It is the whole difference between a local tool and a
network service.

## Decision

**Phase 6 is stdio only.** There is no transport flag, no host flag and no port
flag — not disabled ones, none.

stdio matches what the Engine already is: a local, offline, read-only runtime
bound to a checkout on the same filesystem, whose caller is the machine owner.
It opens no listener, needs no authorization, has no bind address and no remote
threat model. Both target hosts drive local servers this way.

**A loopback-only HTTP variant is also rejected.** It would still cross the
no-network architectural line for almost no gain over stdio.

**Prerequisites for any future network transport**, recorded so the work is
scoped rather than discovered:

- authorization — the 2026-07-28 revision rewrote it entirely;
- bind defaults, and whether loopback is enforced;
- `Host` and `Origin` validation;
- TLS, or a documented reverse-proxy termination story;
- rate limiting and concurrency caps;
- a written remote threat model in which the caller is *not* the machine owner;
- observability and audit logging for a service that can be attacked off-box;
- an explicit decision about whether remote callers may read safety-gated bodies
  at all.

That last one is a product question, not an engineering one, and it should be
answered before any code is written.

## Consequences

The Phase 6 attack surface is a pipe. There is nothing to authenticate, nothing
to bind, and no listener to find.

The dependency cost is paid without the benefit — the SDK's HTTP stack ships
unused. That is a real inefficiency and is disclosed in the docs rather than
hidden; there is no stdio-only extra upstream to opt into.

Adding HTTP later is additive: the adapter, the tools, the projections and the
error mapping are transport-independent, so the work is the list above and not a
rewrite.

"""Authoring-firewall tooling for an independently written sealed benchmark.

Nothing in this package authors a task. It prepares the *conditions* under
which someone else can: it picks masked targets deterministically, strips
identity out of their bodies, proves the result carries no identifying trace,
and packages an author-visible export separately from a reviewer-private one.

The split this package exists to enforce:

``author``
    Sees sanitized operational text under opaque packet IDs, and nothing that
    names a resource. Writes tasks.
``reviewer``
    Sees the packet-to-target mapping and generic non-PAE discovery tooling.
    Labels tasks. A different session from the author.
``maintainer``
    Adjudicates disagreements and freezes. Never the author.

A benchmark whose tasks were written by the system under test measures the
system's memory of itself. The firewall is the whole point, so every export
path here ends in an audit that fails closed.
"""

from __future__ import annotations

#: Bumped when a change would alter which targets a given seed selects, or what
#: bytes a given body sanitizes to. Recorded in every manifest, because a
#: selection that cannot name its own algorithm version is not reproducible.
AUTHORING_TOOL_VERSION = "0.1.0"

__all__ = ["AUTHORING_TOOL_VERSION"]

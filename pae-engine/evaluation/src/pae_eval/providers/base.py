"""The provider-neutral participant protocol.

Everything above this layer — conditions, the tool loop, trial records, cost
accounting — is written against these types and never against a vendor SDK. The
adapters translate; nothing else knows which provider ran.

One deliberate omission: there is no field for private chain-of-thought, and no
adapter requests it. Reasoning summaries a provider volunteers in its normal
response are kept inside ``raw``; nothing solicits hidden reasoning, and no
analysis depends on it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence, runtime_checkable


@dataclass(frozen=True)
class ToolSpec:
    """A tool offered to the participant, in provider-neutral form."""

    name: str
    description: str
    input_schema: Mapping[str, Any]

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": dict(self.input_schema),
        }


@dataclass(frozen=True)
class ToolCall:
    """A tool invocation the model asked for."""

    id: str
    name: str
    arguments: Mapping[str, Any]

    def to_json_obj(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "arguments": dict(self.arguments)}


@dataclass(frozen=True)
class ToolResult:
    """What the harness handed back for a ``ToolCall``."""

    call_id: str
    content: str
    is_error: bool = False

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "call_id": self.call_id,
            "content": self.content,
            "is_error": self.is_error,
        }


@dataclass(frozen=True)
class Message:
    """One conversation turn.

    ``content`` is text; ``tool_calls`` and ``tool_results`` carry the
    structured parts. Adapters render this into whatever shape their provider
    wants.
    """

    role: str  # "user" | "assistant"
    content: str = ""
    tool_calls: tuple[ToolCall, ...] = ()
    tool_results: tuple[ToolResult, ...] = ()


@dataclass(frozen=True)
class Usage:
    """Normalized token accounting.

    Unknown fields stay ``None`` rather than becoming zero: "the provider did
    not report cache reads" and "the provider reported zero cache reads" are
    different facts, and a cost model that confuses them is wrong in a way
    nobody notices. ``provenance`` records which fields were actually present.

    **The three input buckets are disjoint.** ``input_tokens`` counts only
    tokens billed at the full input rate; cache reads and cache writes are
    counted in their own fields and are *not* also inside ``input_tokens``.
    Providers disagree about this — Anthropic reports the three separately,
    while the OpenAI Responses API reports a total with the cached part as a
    subset — so each adapter normalizes to this convention and
    :func:`pae_eval.pricing.cost_usd` simply adds the buckets. Any adapter that
    got this wrong would misprice every cached call, in the direction of
    looking cheaper than it is.
    """

    input_tokens: int | None = None
    output_tokens: int | None = None
    cache_read_tokens: int | None = None
    cache_write_tokens: int | None = None
    other_billed_units: Mapping[str, float] = field(default_factory=dict)
    provenance: tuple[str, ...] = ()

    @property
    def total_tokens(self) -> int | None:
        """Every token processed, cached or not.

        All three input buckets are counted, not just ``input_tokens``. This
        is what keeps the efficiency endpoint measuring work instead of
        measuring caching: the buckets are disjoint, so leaving the cached ones
        out would make an identical amount of work report fewer tokens the
        moment caching was switched on — and by a different amount per
        condition, since the conditions differ in how much of their prompt is
        cacheable. That would have quietly moved a reported number.
        """
        parts = [self.input_tokens, self.cache_read_tokens,
                 self.cache_write_tokens, self.output_tokens]
        if all(p is None for p in parts):
            return None
        return sum(p or 0 for p in parts)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_read_tokens": self.cache_read_tokens,
            "cache_write_tokens": self.cache_write_tokens,
            "other_billed_units": dict(self.other_billed_units),
            "provenance": list(self.provenance),
        }

    def plus(self, other: "Usage") -> "Usage":
        """Accumulate across a tool loop's turns."""

        def add(a: int | None, b: int | None) -> int | None:
            if a is None and b is None:
                return None
            return (a or 0) + (b or 0)

        merged = dict(self.other_billed_units)
        for key, value in other.other_billed_units.items():
            merged[key] = merged.get(key, 0.0) + value
        return Usage(
            input_tokens=add(self.input_tokens, other.input_tokens),
            output_tokens=add(self.output_tokens, other.output_tokens),
            cache_read_tokens=add(self.cache_read_tokens, other.cache_read_tokens),
            cache_write_tokens=add(self.cache_write_tokens, other.cache_write_tokens),
            other_billed_units=merged,
            provenance=tuple(sorted(set(self.provenance) | set(other.provenance))),
        )


@dataclass(frozen=True)
class ModelRequest:
    model: str
    system: str
    messages: tuple[Message, ...]
    tools: tuple[ToolSpec, ...] = ()
    max_output_tokens: int = 4096
    effort: str | None = None
    #: Provider-specific knobs the plan chose explicitly. Adapters send only
    #: what they are given; see spec §78 — no adapter invents temperature,
    #: top_p or seed, because the current frontier models reject them outright.
    extra: Mapping[str, Any] = field(default_factory=dict)

    def with_messages(self, messages: Sequence[Message]) -> "ModelRequest":
        return ModelRequest(
            model=self.model,
            system=self.system,
            messages=tuple(messages),
            tools=self.tools,
            max_output_tokens=self.max_output_tokens,
            effort=self.effort,
            extra=self.extra,
        )


@dataclass(frozen=True)
class ModelResponse:
    #: Empty by default: a turn that is only a tool call carries no text, and
    #: requiring one would make every adapter invent a placeholder.
    text: str = ""
    tool_calls: tuple[ToolCall, ...] = ()
    stop_reason: str = "end_turn"
    usage: Usage = field(default_factory=Usage)
    provider_response_id: str | None = None
    #: The provider's own model identifier as returned, when it gives one.
    #: Recorded separately from the configured ID because an alias is not a
    #: snapshot (spec §77).
    reported_model: str | None = None
    raw: Mapping[str, Any] = field(default_factory=dict)

    @property
    def wants_tools(self) -> bool:
        return bool(self.tool_calls)


@runtime_checkable
class ParticipantAdapter(Protocol):
    """What every provider adapter implements."""

    #: Stable provider key, e.g. ``"anthropic"``. Recorded in trials.
    provider: str

    def complete(self, request: ModelRequest) -> ModelResponse: ...

    def describe(self) -> Mapping[str, Any]:
        """Adapter/SDK identification for the run manifest. No secrets."""
        ...

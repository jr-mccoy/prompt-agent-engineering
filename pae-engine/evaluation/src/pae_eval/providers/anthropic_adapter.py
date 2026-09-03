"""Anthropic adapter.

Verified against the Messages API and the `anthropic` Python SDK on 2026-09-02;
see evaluation/README.md -> "Provider SDK verification" for the sources and the
date. Do not treat the model IDs or parameter set here as timeless: this file
names no model, and the plan supplies the ID.

Two current-API facts shape the code:

* ``temperature`` / ``top_p`` / ``top_k`` are **removed** on the current
  frontier models and return 400 if sent. The adapter therefore forwards only
  parameters the plan set explicitly, and never supplies a sampling default of
  its own (spec §78).
* Thinking configuration is deliberately not synthesized here. If a plan wants
  it, it passes it through ``extra``; the harness never opts a run into a
  thinking mode the plan did not ask for.

Prompt caching
--------------

``cache_prompts`` (default on) uses the documented combination of both caching
mechanisms, which occupies three of the four available breakpoint slots:

1. an explicit breakpoint on the **last tool definition** — one breakpoint
   caches the whole catalog, because a cached prefix ends at the block the
   marker sits on. The catalog is byte-identical across every trial of a
   condition;
2. an explicit breakpoint on the **system prompt** — likewise identical across
   every trial of a condition;
3. the **top-level** ``cache_control`` field, which is automatic caching. The
   API places the remaining breakpoint on the last cacheable block and walks it
   forward as the conversation grows, so on turn *k* the first *k*-1 turns are
   a cache read rather than a re-billed resend. That is where the money in
   conditions B and D actually goes, and letting the API track it is both the
   recommended approach and one fewer thing for this file to get wrong.

Three things this deliberately does **not** do:

* It does not change a single token the model sees. ``cache_control`` is
  request metadata; the prompt is identical with it and without it, and so is
  the sampling distribution. Caching is a billing and latency optimization, not
  an experimental variable, and no analysis reads a cache counter.
* It does not opt into the 1-hour TTL. The 5-minute default fits a run that
  works through trials back to back, and the 1-hour extension costs 2x base
  input on writes instead of 1.25x. If a run needs it, the plan can ask.
* It does not hand-roll the rolling conversation breakpoint. An earlier draft
  did; automatic caching supersedes it and would otherwise compete for the same
  slot.

A prefix below the model's minimum cacheable length (512 tokens on Claude Opus
5, more on most others) is silently not cached — no error, and no write to pay
for. Single-call conditions therefore pay one write on the first trial and read
the system prompt back on every trial after it.
"""

from __future__ import annotations

from typing import Any, Mapping

from ..errors import InfrastructureFailure, ProviderNotAvailable
from .base import Message, ModelRequest, ModelResponse, ToolCall, Usage

#: Parameters the plan may set that we pass straight through.
PASSTHROUGH = ("stop_sequences", "thinking", "output_config", "betas", "speed")

#: The 5-minute breakpoint. Written as a literal rather than built from the
#: plan: a TTL is a cost decision, and this file does not make those quietly.
CACHE_CONTROL: Mapping[str, Any] = {"type": "ephemeral"}


def _load():
    try:
        import anthropic  # noqa: PLC0415
    except ImportError as exc:  # pragma: no cover - exercised via monkeypatch
        raise ProviderNotAvailable(
            "the Anthropic SDK is not installed; "
            "install the evaluation project with the [anthropic] extra"
        ) from exc
    return anthropic


def _render_messages(messages: tuple[Message, ...]) -> list[dict[str, Any]]:
    """Neutral messages -> Anthropic content blocks.

    Tool results ride on a ``user`` turn as ``tool_result`` blocks, and all
    results for one assistant turn must arrive in a single message — splitting
    them trains the model out of parallel tool use.

    No cache breakpoint is placed here: the top-level ``cache_control`` field
    handles the conversation, and it moves as the conversation grows.
    """
    rendered: list[dict[str, Any]] = []
    for message in messages:
        if message.tool_results:
            rendered.append({
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": result.call_id,
                        "content": result.content,
                        **({"is_error": True} if result.is_error else {}),
                    }
                    for result in message.tool_results
                ],
            })
            continue

        blocks: list[dict[str, Any]] = []
        if message.content:
            blocks.append({"type": "text", "text": message.content})
        for call in message.tool_calls:
            blocks.append({
                "type": "tool_use",
                "id": call.id,
                "name": call.name,
                "input": dict(call.arguments),
            })
        if blocks:
            rendered.append({"role": message.role, "content": blocks})
    return rendered


def _usage(raw: Any) -> Usage:
    """Normalize provider usage, recording which fields were actually present."""
    present: list[str] = []

    def read(name: str) -> int | None:
        value = getattr(raw, name, None)
        if value is None:
            return None
        present.append(name)
        return int(value)

    return Usage(
        input_tokens=read("input_tokens"),
        output_tokens=read("output_tokens"),
        cache_read_tokens=read("cache_read_input_tokens"),
        cache_write_tokens=read("cache_creation_input_tokens"),
        provenance=tuple(present),
    )


class AnthropicAdapter:
    """Provider adapter. Constructing it does not call the API."""

    provider = "anthropic"

    def __init__(self, *, client: Any = None, timeout_s: float | None = None,
                 cache_prompts: bool = True) -> None:
        self._explicit_client = client
        self._client = client
        self._timeout_s = timeout_s
        self._cache_prompts = bool(cache_prompts)
        self._sdk_version: str | None = None

    def _ensure_client(self) -> Any:
        if self._client is None:
            anthropic = _load()
            # Credentials come from the environment only. Never from a config
            # file, a CLI argument or the plan (spec §47).
            self._client = anthropic.Anthropic()
        return self._client

    def complete(self, request: ModelRequest) -> ModelResponse:
        anthropic = None if self._explicit_client is not None else _load()
        client = self._ensure_client()

        cache = self._cache_prompts
        payload: dict[str, Any] = {
            "model": request.model,
            "max_tokens": request.max_output_tokens,
            "messages": _render_messages(request.messages),
        }
        if cache:
            # Automatic caching. Only useful once there is a conversation to
            # cache; on a single-call trial the tools/system breakpoints below
            # already cover the whole stable prefix.
            if len(request.messages) > 1:
                payload["cache_control"] = dict(CACHE_CONTROL)
        if request.system:
            payload["system"] = (
                [{"type": "text", "text": request.system,
                  "cache_control": dict(CACHE_CONTROL)}]
                if cache else request.system
            )
        if request.tools:
            tools = [
                {
                    "name": spec.name,
                    "description": spec.description,
                    "input_schema": dict(spec.input_schema),
                }
                for spec in request.tools
            ]
            if cache:
                # One breakpoint on the last definition caches the whole
                # catalog; marking each tool would spend breakpoints for
                # nothing, since a prefix ends at the block it is placed on.
                tools[-1]["cache_control"] = dict(CACHE_CONTROL)
            payload["tools"] = tools
        if request.effort is not None:
            # `effort` lives inside output_config, not at the top level.
            config = dict(request.extra.get("output_config") or {})
            config["effort"] = request.effort
            payload["output_config"] = config
        for key in PASSTHROUGH:
            if key in request.extra and key not in payload:
                payload[key] = request.extra[key]
        if self._timeout_s is not None:
            payload["timeout"] = self._timeout_s

        try:
            response = client.messages.create(**payload)
        except Exception as exc:  # translated below
            raise self._translate(exc, anthropic) from exc

        return self._normalize(response, request)

    # -- translation -------------------------------------------------------

    @staticmethod
    def _translate(exc: Exception, anthropic: Any) -> Exception:
        """Vendor exception -> harness failure class.

        Only transport and server-side conditions become retryable. A 400 is a
        harness bug and must surface, not be retried into a rate limit.
        """
        if anthropic is None:  # injected client in tests
            return InfrastructureFailure(str(exc))
        retry_after = None
        response = getattr(exc, "response", None)
        if response is not None:
            try:
                header = response.headers.get("retry-after")
                retry_after = float(header) if header else None
            except Exception:  # pragma: no cover - header shapes vary
                retry_after = None

        if isinstance(exc, getattr(anthropic, "RateLimitError", ())):
            return InfrastructureFailure(str(exc), "rate_limited", retry_after)
        if isinstance(exc, getattr(anthropic, "APITimeoutError", ())):
            return InfrastructureFailure(str(exc), "provider_transport_error", retry_after)
        if isinstance(exc, getattr(anthropic, "APIConnectionError", ())):
            return InfrastructureFailure(str(exc), "connection_error", retry_after)
        status_error = getattr(anthropic, "APIStatusError", None)
        if status_error is not None and isinstance(exc, status_error):
            code = int(getattr(exc, "status_code", 0) or 0)
            if code == 529:
                return InfrastructureFailure(str(exc), "overloaded", retry_after)
            if code >= 500:
                return InfrastructureFailure(str(exc), "server_error", retry_after)
            return exc  # 4xx: our request is wrong; do not retry
        return exc

    def _normalize(self, response: Any, request: ModelRequest) -> ModelResponse:
        text_parts: list[str] = []
        calls: list[ToolCall] = []
        for block in getattr(response, "content", None) or ():
            kind = getattr(block, "type", None)
            if kind == "text":
                text_parts.append(getattr(block, "text", "") or "")
            elif kind == "tool_use":
                calls.append(ToolCall(
                    id=getattr(block, "id", ""),
                    name=getattr(block, "name", ""),
                    arguments=dict(getattr(block, "input", {}) or {}),
                ))
            # `thinking` blocks are ignored on purpose: nothing requests them
            # and no analysis reads them.

        raw: Mapping[str, Any] = {}
        to_dict = getattr(response, "to_dict", None)
        if callable(to_dict):
            try:
                raw = to_dict()
            except Exception:  # pragma: no cover
                raw = {}

        return ModelResponse(
            text="".join(text_parts).strip(),
            tool_calls=tuple(calls),
            stop_reason=getattr(response, "stop_reason", None) or "end_turn",
            usage=_usage(getattr(response, "usage", None)),
            provider_response_id=getattr(response, "_request_id", None)
            or getattr(response, "id", None),
            reported_model=getattr(response, "model", None),
            raw=raw,
        )

    def describe(self) -> Mapping[str, Any]:
        if self._sdk_version is None:
            try:
                import importlib.metadata as md

                self._sdk_version = md.version("anthropic")
            except Exception:  # pragma: no cover
                self._sdk_version = "unknown"
        return {
            "provider": "anthropic",
            "adapter": "pae_eval.providers.anthropic_adapter.AnthropicAdapter",
            "sdk_version": self._sdk_version,
            "credential_env_vars": ["ANTHROPIC_API_KEY"],
            # Recorded so a reader of the run manifest can tell whether the
            # reported cache counters were even asked for.
            "prompt_caching": self._cache_prompts,
            "prompt_cache_ttl": "5m" if self._cache_prompts else None,
        }

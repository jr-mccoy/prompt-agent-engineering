"""OpenAI adapter, written against the Responses API.

Verified against the Responses API reference and the `openai` Python SDK on
2026-09-02; see evaluation/README.md -> "Provider SDK verification". No model
ID appears in this file — the plan supplies it.

Shape notes that differ from the Anthropic adapter and are easy to get wrong:

* the conversation is a flat ``input`` list of items, not role/content pairs
  with nested blocks;
* a tool call comes back as a ``function_call`` item whose ``arguments`` is a
  **JSON string**, not an object, so it is parsed here and a parse failure is
  surfaced as malformed tool arguments rather than crashing the loop;
* a result goes back as a separate ``function_call_output`` item keyed by
  ``call_id``;
* usage reports ``cached_input_tokens``; there is no cache-write counter, so
  that field stays ``None`` rather than being invented as zero.
"""

from __future__ import annotations

import json
from typing import Any, Mapping

from ..errors import InfrastructureFailure, ProviderNotAvailable
from .base import Message, ModelRequest, ModelResponse, ToolCall, Usage

PASSTHROUGH = ("reasoning", "text", "metadata", "store", "truncation")


def _load():
    try:
        import openai  # noqa: PLC0415
    except ImportError as exc:  # pragma: no cover - exercised via monkeypatch
        raise ProviderNotAvailable(
            "the OpenAI SDK is not installed; "
            "install the evaluation project with the [openai] extra"
        ) from exc
    return openai


def _render_input(system: str, messages: tuple[Message, ...]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if system:
        items.append({"role": "system", "content": system})
    for message in messages:
        if message.content:
            items.append({"role": message.role, "content": message.content})
        for call in message.tool_calls:
            items.append({
                "type": "function_call",
                "call_id": call.id,
                "name": call.name,
                "arguments": json.dumps(dict(call.arguments), sort_keys=True),
            })
        for result in message.tool_results:
            items.append({
                "type": "function_call_output",
                "call_id": result.call_id,
                "output": result.content,
            })
    return items


def _usage(raw: Any) -> Usage:
    present: list[str] = []

    def read(name: str) -> int | None:
        value = getattr(raw, name, None)
        if value is None and isinstance(raw, Mapping):
            value = raw.get(name)
        if value is None:
            return None
        present.append(name)
        return int(value)

    return Usage(
        input_tokens=read("input_tokens"),
        output_tokens=read("output_tokens"),
        cache_read_tokens=read("cached_input_tokens"),
        # The Responses API reports no cache-write counter. Leaving this None
        # keeps "not reported" distinct from "reported as zero".
        cache_write_tokens=None,
        provenance=tuple(present),
    )


class OpenAIAdapter:
    provider = "openai"

    def __init__(self, *, client: Any = None, timeout_s: float | None = None) -> None:
        self._explicit_client = client
        self._client = client
        self._timeout_s = timeout_s
        self._sdk_version: str | None = None

    def _ensure_client(self) -> Any:
        if self._client is None:
            openai = _load()
            self._client = openai.OpenAI()
        return self._client

    def complete(self, request: ModelRequest) -> ModelResponse:
        openai = None if self._explicit_client is not None else _load()
        client = self._ensure_client()

        payload: dict[str, Any] = {
            "model": request.model,
            "input": _render_input(request.system, request.messages),
            "max_tokens": request.max_output_tokens,
        }
        if request.tools:
            payload["tools"] = [
                {
                    "type": "function",
                    "name": spec.name,
                    "description": spec.description,
                    "parameters": dict(spec.input_schema),
                }
                for spec in request.tools
            ]
        for key in PASSTHROUGH:
            if key in request.extra:
                payload[key] = request.extra[key]
        if self._timeout_s is not None:
            payload["timeout"] = self._timeout_s

        try:
            response = client.responses.create(**payload)
        except Exception as exc:
            raise self._translate(exc, openai) from exc

        return self._normalize(response)

    @staticmethod
    def _translate(exc: Exception, openai: Any) -> Exception:
        if openai is None:
            return InfrastructureFailure(str(exc))
        retry_after = None
        response = getattr(exc, "response", None)
        if response is not None:
            try:
                header = response.headers.get("retry-after")
                retry_after = float(header) if header else None
            except Exception:  # pragma: no cover
                retry_after = None

        if isinstance(exc, getattr(openai, "RateLimitError", ())):
            return InfrastructureFailure(str(exc), "rate_limited", retry_after)
        if isinstance(exc, getattr(openai, "APITimeoutError", ())):
            return InfrastructureFailure(str(exc), "provider_transport_error", retry_after)
        if isinstance(exc, getattr(openai, "APIConnectionError", ())):
            return InfrastructureFailure(str(exc), "connection_error", retry_after)
        status_error = getattr(openai, "APIStatusError", None)
        if status_error is not None and isinstance(exc, status_error):
            code = int(getattr(exc, "status_code", 0) or 0)
            if code >= 500:
                return InfrastructureFailure(str(exc), "server_error", retry_after)
            return exc
        return exc

    def _normalize(self, response: Any) -> ModelResponse:
        text_parts: list[str] = []
        calls: list[ToolCall] = []
        malformed: list[str] = []

        convenience = getattr(response, "output_text", None)
        for item in getattr(response, "output", None) or ():
            kind = getattr(item, "type", None)
            if kind == "function_call":
                raw_args = getattr(item, "arguments", "") or "{}"
                try:
                    parsed = json.loads(raw_args)
                    if not isinstance(parsed, dict):
                        raise ValueError("arguments must decode to an object")
                except (ValueError, TypeError):
                    # Surfaced as a tool call with no arguments; the loop
                    # records it as malformed model output, which is an
                    # outcome, not an infrastructure fault.
                    malformed.append(getattr(item, "name", "") or "")
                    parsed = {}
                calls.append(ToolCall(
                    id=getattr(item, "call_id", "") or getattr(item, "id", ""),
                    name=getattr(item, "name", "") or "",
                    arguments=parsed,
                ))
            elif kind == "message" and convenience is None:
                for part in getattr(item, "content", None) or ():
                    if getattr(part, "type", None) in ("output_text", "text"):
                        text_parts.append(getattr(part, "text", "") or "")

        text = (convenience if convenience is not None else "".join(text_parts)) or ""

        raw: Mapping[str, Any] = {}
        for attr in ("model_dump", "to_dict"):
            fn = getattr(response, attr, None)
            if callable(fn):
                try:
                    raw = fn()
                    break
                except Exception:  # pragma: no cover
                    continue
        if malformed:
            raw = {**dict(raw), "pae_eval_malformed_tool_arguments": malformed}

        return ModelResponse(
            text=text.strip(),
            tool_calls=tuple(calls),
            stop_reason="tool_use" if calls else (
                getattr(response, "status", None) or "end_turn"
            ),
            usage=_usage(getattr(response, "usage", None)),
            provider_response_id=getattr(response, "id", None),
            reported_model=getattr(response, "model", None),
            raw=raw,
        )

    def describe(self) -> Mapping[str, Any]:
        if self._sdk_version is None:
            try:
                import importlib.metadata as md

                self._sdk_version = md.version("openai")
            except Exception:  # pragma: no cover
                self._sdk_version = "unknown"
        return {
            "provider": "openai",
            "adapter": "pae_eval.providers.openai_adapter.OpenAIAdapter",
            "sdk_version": self._sdk_version,
            "credential_env_vars": ["OPENAI_API_KEY"],
        }

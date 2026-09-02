"""The participant host loop.

One loop drives every condition. Conditions differ only in which tools are
offered and what context is injected — never in prompt style, turn budget or
output limit — because a baseline that is quietly given a worse deal produces a
win that means nothing (spec §30, §32).

The loop is where the retry/outcome boundary is enforced. Infrastructure
failures get bounded retries; model behaviour does not, ever. Retrying a
refusal until the model complies would select for agreeable samples and bias
the arm, so "the model refused" and "the network dropped" take different paths
out of this file.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Sequence

from .errors import (
    CostCeilingError,
    InfrastructureFailure,
    ModelBehaviourFailure,
    TrialFailure,
)
from .providers.base import (
    Message,
    ModelRequest,
    ModelResponse,
    ParticipantAdapter,
    ToolCall,
    ToolResult,
    ToolSpec,
    Usage,
)

#: A tool dispatcher: (name, arguments) -> (content, is_error, observability).
Dispatcher = Callable[[str, Mapping[str, Any]], "ToolExecution"]


@dataclass
class ToolExecution:
    content: str
    is_error: bool = False
    observability: Mapping[str, Any] = field(default_factory=dict)


@dataclass
class LoopLimits:
    max_tool_turns: int = 40
    tool_loop_timeout_s: float = 600.0
    model_call_timeout_s: float = 120.0
    tool_call_timeout_s: float = 30.0


@dataclass
class RetryPolicy:
    max_attempts: int = 3
    base_delay_s: float = 1.0
    max_delay_s: float = 30.0
    jitter: bool = True

    def delay_for(self, attempt: int, retry_after_s: float | None = None,
                  rng: random.Random | None = None) -> float:
        """Backoff for ``attempt`` (1-based). ``retry-after`` always wins."""
        if retry_after_s is not None and retry_after_s >= 0:
            return min(retry_after_s, self.max_delay_s)
        delay = min(self.base_delay_s * (2 ** max(0, attempt - 1)), self.max_delay_s)
        if self.jitter:
            source = rng or random
            delay += source.uniform(0, min(1.0, delay))
        return delay


@dataclass
class Attempt:
    """One request to the provider, successful or not."""

    attempt_no: int
    started_at: float
    ended_at: float
    error_class: str | None = None
    retryable: bool = False
    delay_before_s: float = 0.0
    provider_response_id: str | None = None

    @property
    def latency_ms(self) -> float:
        return (self.ended_at - self.started_at) * 1000.0

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "attempt_no": self.attempt_no,
            "latency_ms": round(self.latency_ms, 2),
            "error_class": self.error_class,
            "retryable": self.retryable,
            "delay_before_s": round(self.delay_before_s, 3),
            "provider_response_id": self.provider_response_id,
        }


@dataclass
class LoopResult:
    """The observable outcome of one trial's conversation."""

    final_answer: str
    stop_reason: str
    usage: Usage
    tool_calls: tuple[dict[str, Any], ...]
    attempts: tuple[Attempt, ...]
    turns: int
    started_at: float
    ended_at: float
    error_class: str | None = None
    provider_response_id: str | None = None
    reported_model: str | None = None
    raw_final: Mapping[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.error_class is None

    @property
    def latency_ms(self) -> float:
        return (self.ended_at - self.started_at) * 1000.0


def _now() -> float:
    return time.monotonic()


class HostLoop:
    """Runs one task, in one condition, to a terminal outcome."""

    def __init__(
        self,
        adapter: ParticipantAdapter,
        *,
        limits: LoopLimits | None = None,
        retry: RetryPolicy | None = None,
        sleep: Callable[[float], None] = time.sleep,
        rng: random.Random | None = None,
        cost_guard: Callable[[], None] | None = None,
    ) -> None:
        self.adapter = adapter
        self.limits = limits or LoopLimits()
        self.retry = retry or RetryPolicy()
        self._sleep = sleep
        self._rng = rng or random.Random(0)
        #: Called before every paid request. Raises CostCeilingError to stop
        #: *before* the money is spent rather than after the invoice.
        self._cost_guard = cost_guard

    # -- one provider call, with bounded infrastructure retries -------------

    def _complete(self, request: ModelRequest, attempts: list[Attempt]) -> ModelResponse:
        last: TrialFailure | None = None
        for attempt_no in range(1, self.retry.max_attempts + 1):
            delay = 0.0
            if last is not None:
                delay = self.retry.delay_for(
                    attempt_no - 1, getattr(last, "retry_after_s", None), self._rng
                )
                self._sleep(delay)
            if self._cost_guard is not None:
                self._cost_guard()
            started = _now()
            try:
                response = self.adapter.complete(request)
            except ModelBehaviourFailure as exc:
                attempts.append(Attempt(attempt_no, started, _now(),
                                        exc.error_class, False, delay))
                raise
            except InfrastructureFailure as exc:
                attempts.append(Attempt(attempt_no, started, _now(),
                                        exc.error_class, True, delay))
                last = exc
                continue
            attempts.append(Attempt(attempt_no, started, _now(), None, False, delay,
                                    response.provider_response_id))
            return response
        assert last is not None
        raise last

    # -- the loop ----------------------------------------------------------

    def run(
        self,
        request: ModelRequest,
        *,
        dispatcher: Dispatcher | None = None,
        tools: Sequence[ToolSpec] = (),
    ) -> LoopResult:
        started = _now()
        attempts: list[Attempt] = []
        messages: list[Message] = list(request.messages)
        usage = Usage()
        observed: list[dict[str, Any]] = []
        tool_names = {spec.name for spec in tools}
        turns = 0
        deadline = started + self.limits.tool_loop_timeout_s

        base = ModelRequest(
            model=request.model, system=request.system, messages=tuple(messages),
            tools=tuple(tools), max_output_tokens=request.max_output_tokens,
            effort=request.effort, extra=request.extra,
        )

        def finish(answer: str, stop_reason: str, error_class: str | None,
                   response: ModelResponse | None) -> LoopResult:
            return LoopResult(
                final_answer=answer, stop_reason=stop_reason, usage=usage,
                tool_calls=tuple(observed), attempts=tuple(attempts), turns=turns,
                started_at=started, ended_at=_now(), error_class=error_class,
                provider_response_id=response.provider_response_id if response else None,
                reported_model=response.reported_model if response else None,
                raw_final=dict(response.raw) if response else {},
            )

        while True:
            if _now() > deadline:
                return finish("", "timeout", "behavioural_timeout", None)

            try:
                response = self._complete(base.with_messages(messages), attempts)
            except ModelBehaviourFailure as exc:
                return finish("", exc.error_class, exc.error_class, None)
            except InfrastructureFailure as exc:
                return finish("", exc.error_class, "infrastructure_failed", None)

            usage = usage.plus(response.usage)

            # A provider content refusal arrives as a successful HTTP response
            # whose stop_reason says no. It is an outcome, never a retry.
            if response.stop_reason == "refusal":
                return finish(response.text or "", "refusal", "refusal", response)

            if not response.wants_tools:
                answer = (response.text or "").strip()
                if not answer:
                    return finish("", "empty", "empty_answer", response)
                return finish(answer, response.stop_reason, None, response)

            if dispatcher is None or not tool_names:
                # The model asked for a tool in a condition that has none. That
                # is a model-behaviour outcome, not a harness error.
                return finish(response.text or "", "unexpected_tool_use",
                              "malformed_tool_arguments", response)

            turns += 1
            if turns > self.limits.max_tool_turns:
                return finish(response.text or "", "turn_budget_exhausted",
                              "turn_budget_exhausted", response)

            messages.append(Message(role="assistant", content=response.text or "",
                                    tool_calls=response.tool_calls))
            results: list[ToolResult] = []
            for call in response.tool_calls:
                results.append(self._dispatch(call, dispatcher, tool_names, observed))
            messages.append(Message(role="user", tool_results=tuple(results)))

    def _dispatch(self, call: ToolCall, dispatcher: Dispatcher,
                  tool_names: set[str], observed: list[dict[str, Any]]) -> ToolResult:
        if call.name not in tool_names:
            content = (
                f"error: unknown tool {call.name!r}. "
                f"Available tools: {', '.join(sorted(tool_names))}."
            )
            observed.append({
                "tool": call.name, "arguments": dict(call.arguments),
                "status": "error", "bytes": len(content.encode("utf-8")),
                "latency_ms": 0.0, "reason": "unknown_tool",
            })
            return ToolResult(call_id=call.id, content=content, is_error=True)

        started = _now()
        try:
            execution = dispatcher(call.name, call.arguments)
        except Exception as exc:  # a tool must never take the loop down
            content = f"error: tool {call.name} failed — {exc}"
            execution = ToolExecution(content=content, is_error=True)
        latency = (_now() - started) * 1000.0

        observed.append({
            "tool": call.name,
            "arguments": dict(call.arguments),
            "status": "error" if execution.is_error else "ok",
            "bytes": len(execution.content.encode("utf-8")),
            "latency_ms": round(latency, 2),
            **dict(execution.observability),
        })
        return ToolResult(call_id=call.id, content=execution.content,
                          is_error=execution.is_error)

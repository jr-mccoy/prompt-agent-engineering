"""Deterministic fake provider — the backbone of CI.

Every path the harness can take must be exercisable without a credential and
without spending money: tool loops, invalid tool calls, refusals, rate limits
that resolve on retry, rate limits that never resolve, timeouts, and usage
accounting. If a behaviour can only be produced by a real provider, it is
untested, and the first time anyone sees it will be during a paid sealed run.

Scripts are consumed in order. A step may be a response or a raised failure,
so a script expresses "429, 429, then success" as three steps and the retry
policy is tested against it rather than against a mock that always succeeds.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Mapping, Sequence

from ..errors import InfrastructureFailure, ModelBehaviourFailure
from .base import ModelRequest, ModelResponse, ToolCall, Usage


@dataclass
class Step:
    """One scripted turn.

    Exactly one of ``response`` or ``raises`` is used; ``raises`` is a
    zero-argument callable so a fresh exception instance is built per attempt.
    """

    response: ModelResponse | None = None
    raises: Callable[[], Exception] | None = None
    #: Recorded so a test can assert what the model was actually asked.
    on_request: Callable[[ModelRequest], None] | None = None


def usage(input_tokens: int = 100, output_tokens: int = 50,
          cache_read: int | None = 0, cache_write: int | None = 0) -> Usage:
    return Usage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_tokens=cache_read,
        cache_write_tokens=cache_write,
        provenance=("fake",),
    )


def text_step(text: str, **kw: Any) -> Step:
    return Step(response=ModelResponse(
        text=text, stop_reason="end_turn", usage=usage(**kw),
        provider_response_id="fake_resp_text", reported_model="fake-model-1",
    ))


def tool_step(name: str, arguments: Mapping[str, Any], call_id: str = "call_1",
              text: str = "", **kw: Any) -> Step:
    return Step(response=ModelResponse(
        text=text,
        tool_calls=(ToolCall(id=call_id, name=name, arguments=dict(arguments)),),
        stop_reason="tool_use", usage=usage(**kw),
        provider_response_id=f"fake_resp_{call_id}", reported_model="fake-model-1",
    ))


def multi_tool_step(calls: Sequence[tuple[str, Mapping[str, Any]]], **kw: Any) -> Step:
    return Step(response=ModelResponse(
        tool_calls=tuple(
            ToolCall(id=f"call_{n}", name=name, arguments=dict(args))
            for n, (name, args) in enumerate(calls)
        ),
        stop_reason="tool_use", usage=usage(**kw),
        provider_response_id="fake_resp_multi", reported_model="fake-model-1",
    ))


def refusal_step() -> Step:
    """A provider content refusal: HTTP 200, ``stop_reason`` says no.

    Modelled as a *response*, not an exception, because that is what it is.
    The loop turns it into a ModelBehaviourFailure; it is never retried.
    """
    return Step(response=ModelResponse(
        text="", stop_reason="refusal", usage=usage(input_tokens=80, output_tokens=0),
        provider_response_id="fake_resp_refusal", reported_model="fake-model-1",
        raw={"stop_details": {"type": "refusal", "category": "fake"}},
    ))


def empty_step() -> Step:
    return Step(response=ModelResponse(
        text="   ", stop_reason="end_turn", usage=usage(output_tokens=1),
        provider_response_id="fake_resp_empty", reported_model="fake-model-1",
    ))


def invalid_tool_step(name: str = "no_such_tool") -> Step:
    return Step(response=ModelResponse(
        tool_calls=(ToolCall(id="call_bad", name=name, arguments={"x": 1}),),
        stop_reason="tool_use", usage=usage(),
        provider_response_id="fake_resp_badtool", reported_model="fake-model-1",
    ))


def rate_limited_step(retry_after_s: float = 0.0) -> Step:
    return Step(raises=lambda: InfrastructureFailure(
        "fake 429", error_class="rate_limited", retry_after_s=retry_after_s))


def server_error_step() -> Step:
    return Step(raises=lambda: InfrastructureFailure(
        "fake 500", error_class="server_error"))


def timeout_step() -> Step:
    return Step(raises=lambda: ModelBehaviourFailure(
        "fake behavioural timeout", error_class="behavioural_timeout"))


class FakeAdapter:
    """A scripted ``ParticipantAdapter``.

    ``scripts`` maps a key to a list of steps. The key is chosen by
    ``key_for(request)``, which defaults to the model name, so one adapter can
    serve several conditions in a single fake run with different behaviour per
    condition.
    """

    provider = "fake"

    def __init__(
        self,
        scripts: Mapping[str, Sequence[Step]] | Sequence[Step] | None = None,
        *,
        key_for: Callable[[ModelRequest], str] | None = None,
        default: Sequence[Step] | None = None,
    ) -> None:
        if scripts is None:
            scripts = {}
        if isinstance(scripts, (list, tuple)):
            scripts = {"*": list(scripts)}
        self._scripts: dict[str, list[Step]] = {k: list(v) for k, v in scripts.items()}
        self._default = list(default) if default is not None else None
        self._key_for = key_for or (lambda request: request.model)
        self._cursor: dict[str, int] = {}
        #: Every request seen, for assertions about what a condition sent.
        self.requests: list[ModelRequest] = []
        self.call_count = 0

    def _script_for(self, key: str) -> list[Step]:
        if key in self._scripts:
            return self._scripts[key]
        if "*" in self._scripts:
            return self._scripts["*"]
        if self._default is not None:
            return self._default
        raise AssertionError(
            f"fake provider has no script for {key!r}; "
            f"known keys: {sorted(self._scripts)}"
        )

    def complete(self, request: ModelRequest) -> ModelResponse:
        self.requests.append(request)
        self.call_count += 1
        key = self._key_for(request)
        script = self._script_for(key)
        index = self._cursor.get(key, 0)
        if index >= len(script):
            # Running off the end of a script is a test bug, not a model
            # behaviour. Say so loudly rather than inventing a reply.
            raise AssertionError(
                f"fake provider script for {key!r} exhausted after {index} steps; "
                "the harness asked for one more completion than the test scripted"
            )
        step = script[index]
        self._cursor[key] = index + 1
        if step.on_request is not None:
            step.on_request(request)
        if step.raises is not None:
            raise step.raises()
        assert step.response is not None, "a Step needs either response or raises"
        return step.response

    def describe(self) -> Mapping[str, Any]:
        return {
            "provider": "fake",
            "adapter": "pae_eval.providers.fake.FakeAdapter",
            "sdk_version": None,
            "note": "deterministic scripted adapter; makes no network call",
        }

    # -- test conveniences -------------------------------------------------

    def remaining(self, key: str = "*") -> int:
        return max(0, len(self._script_for(key)) - self._cursor.get(key, 0))

    def tool_names_seen(self) -> list[str]:
        names: list[str] = []
        for request in self.requests:
            names.extend(spec.name for spec in request.tools)
        return names


class BehaviouralFake(FakeAdapter):
    """A fake that reacts to the request instead of following a fixed script.

    The trial schedule interleaves conditions, so a positional script cannot
    know whether the next request is a tool-loop arm or a single call. This
    adapter looks at the request: if tools are offered and it has not used its
    budget, it calls one; otherwise it answers.

    ``quality`` decides whether the answer satisfies the fixture rubric, which
    is what lets CI drive a known-positive and a known-negative end-to-end run
    through exactly the same code path.
    """

    provider = "fake"

    #: Answer that satisfies the mini-benchmark rubric.
    PASSING = (
        "Summary\n\n"
        "The service is ready for a staged rollout subject to three conditions. "
        "Error budgets are defined, the rollback path has been exercised in "
        "staging, and on-call ownership is documented with an escalation "
        "contact. Remaining risk is concentrated in the migration step, which "
        "should run behind a feature flag for the first week."
    )
    #: Fails the required min_length and required-elements criteria.
    FAILING = "No."

    def __init__(self, *, quality: str = "pass", tool_calls: int = 1,
                 passing_conditions: Sequence[str] = ()) -> None:
        super().__init__(scripts={})
        self.quality = quality
        self.tool_calls = tool_calls
        self.passing_conditions = tuple(passing_conditions)
        self._used_tools = 0

    def _answer_for(self, request: ModelRequest) -> str:
        if self.quality == "pass":
            return self.PASSING
        if self.quality == "fail":
            return self.FAILING
        # Condition-sensitive quality. "by_condition" passes the PAE arms and
        # fails the rest, producing a known-positive run; the inverted form
        # passes the raw-repo arm instead, producing a known-negative run so
        # the report generator can be tested against a result that goes the
        # wrong way for PAE.
        tool_names = {spec.name for spec in request.tools}
        looks_like_pae = any(n.startswith("pae_") for n in tool_names)
        has_bundle = any(
            "Reference material follows" in (m.content or "")
            for m in request.messages
        )
        is_pae_arm = looks_like_pae or has_bundle
        if self.quality == "by_condition_inverted":
            looks_like_raw = any(n.startswith("repo_") for n in tool_names)
            return self.PASSING if looks_like_raw else self.FAILING
        return self.PASSING if is_pae_arm else self.FAILING

    def complete(self, request: ModelRequest) -> ModelResponse:
        self.requests.append(request)
        self.call_count += 1

        already_called = any(m.tool_results for m in request.messages)
        if request.tools and not already_called and self.tool_calls > 0:
            spec = request.tools[0]
            arguments = _plausible_arguments(spec)
            return ModelResponse(
                tool_calls=(ToolCall(id="call_1", name=spec.name,
                                     arguments=arguments),),
                stop_reason="tool_use", usage=usage(input_tokens=1200,
                                                    output_tokens=40),
                provider_response_id="fake_resp_tool",
                reported_model="fake-model-1",
            )

        return ModelResponse(
            text=self._answer_for(request), stop_reason="end_turn",
            usage=usage(input_tokens=2400, output_tokens=180),
            provider_response_id="fake_resp_final", reported_model="fake-model-1",
        )


def _plausible_arguments(spec: Any) -> dict[str, Any]:
    """Arguments a real model would plausibly send for ``spec``."""
    schema = dict(getattr(spec, "input_schema", {}) or {})
    properties = schema.get("properties") or {}
    required = list(schema.get("required") or [])
    defaults = {
        "query": "production readiness review",
        "task": "production readiness review",
        "pattern": "readiness",
        "glob": "*.md",
        "path": "README.md",
        "ref": "technique:ST-01",
    }
    arguments: dict[str, Any] = {}
    for name in required or list(properties)[:1]:
        arguments[name] = defaults.get(name, "readiness")
    return arguments


def always(text: str = "done") -> FakeAdapter:
    """An adapter that answers every request with the same text, forever."""

    class _Always(FakeAdapter):
        def complete(self, request: ModelRequest) -> ModelResponse:
            self.requests.append(request)
            self.call_count += 1
            return ModelResponse(
                text=text, stop_reason="end_turn", usage=usage(),
                provider_response_id="fake_resp_always",
                reported_model="fake-model-1",
            )

    return _Always()


def scripted(*steps: Step) -> FakeAdapter:
    """Shorthand for a single-script adapter."""
    return FakeAdapter(list(steps))


def cycle(steps: Iterable[Step]) -> list[Step]:
    return list(steps)


__all__ = [
    "FakeAdapter", "BehaviouralFake", "Step", "always", "scripted", "cycle", "usage",
    "text_step", "tool_step", "multi_tool_step", "refusal_step", "empty_step",
    "invalid_tool_step", "rate_limited_step", "server_error_step", "timeout_step",
]

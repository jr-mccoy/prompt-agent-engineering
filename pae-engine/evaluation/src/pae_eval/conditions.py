"""Condition construction and the fairness guarantees that make them comparable.

The comparison is only meaningful if the four arms differ in exactly one way:
what the model can reach. Same base prompt, same output constraints, same turn
budget, same timeouts. In particular Condition D does not get persuasive
instructions about how to exploit PAE while Condition B is handed three tools
and no guidance — that asymmetry alone would produce the result we are trying
to measure (spec §30).

Everything a condition may see is assembled here and asserted here, so
isolation is a property of construction rather than a review checklist.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import canonical
from .constants import (
    CONDITION_A,
    CONDITION_B,
    CONDITION_C,
    CONDITION_D,
    CONDITIONS,
)
from .errors import IsolationError, UsageError
from .participant import ToolExecution
from .providers.base import Message, ModelRequest, ToolSpec

# --------------------------------------------------------------------------
# the one base prompt
# --------------------------------------------------------------------------

#: Deliberately says nothing about PAE, the registry, the evaluation, or which
#: condition is running. The tool-use sentence is generic and is rendered
#: identically for B and D; conditions with no tools simply omit it.
BASE_SYSTEM_PROMPT = """\
You are completing a work task for a professional user.

Produce the deliverable the user asked for. Address every part of the request,
and do not substitute a plan or a description of the work for the work itself.

If the request is ambiguous, choose the most reasonable reading, state the
assumption in one sentence, and continue. If the request cannot be completed as
stated, say plainly what is missing and deliver everything that does not depend
on it.

Ground your answer in material you can verify. Do not invent facts, citations,
identifiers, file paths, or authorities. If you are uncertain about something
that matters, say so rather than presenting a guess as established.

Write the deliverable itself as your final response. Do not describe your
process, do not narrate which sources or tools you consulted, and do not name
the systems you used. Do not discuss how your answer is being assessed.
"""

TOOL_GUIDANCE = """\
You have tools available. Use them when they would improve the answer, and stop
using them once you have what you need. Their existence is not a reason to call
them, and the number of calls you make is not a measure of quality.
"""

INJECTED_CONTEXT_HEADER = """\
Reference material follows. Use whatever is relevant to the task and ignore the
rest; it was selected automatically and may include material that does not
apply.
"""


def render_system_prompt(*, has_tools: bool) -> str:
    """The system prompt for a condition.

    Only one bit varies, and it varies on a structural fact — whether tools
    exist — not on which condition is running. A/C get the same text as each
    other; B/D get the same text as each other.
    """
    parts = [BASE_SYSTEM_PROMPT]
    if has_tools:
        parts.append(TOOL_GUIDANCE)
    return "\n".join(parts).strip() + "\n"


def render_user_message(task_query: str, deliverable: str | None,
                        injected_context: str | None) -> str:
    parts = [task_query.strip()]
    if deliverable:
        parts.append(f"\nDeliverable:\n{deliverable.strip()}")
    if injected_context:
        parts.append(f"\n{INJECTED_CONTEXT_HEADER}\n\n{injected_context.strip()}")
    return "\n".join(parts).strip()


# --------------------------------------------------------------------------
# condition context
# --------------------------------------------------------------------------


@dataclass
class ConditionContext:
    """Everything one condition needs to run one task, and nothing else."""

    condition: str
    request: ModelRequest
    tools: tuple[ToolSpec, ...] = ()
    dispatcher: Any | None = None
    #: Condition C only: the compiled bundle's audit record.
    bundle: Mapping[str, Any] | None = None
    #: Per-condition observability, merged into the trial record.
    observability: Mapping[str, Any] = field(default_factory=dict)
    system_prompt_sha256: str = ""
    tool_catalog_sha256: str = ""

    def __post_init__(self) -> None:
        if not self.system_prompt_sha256:
            self.system_prompt_sha256 = canonical.sha256_text(self.request.system)
        if not self.tool_catalog_sha256:
            self.tool_catalog_sha256 = tool_catalog_hash(self.tools)


def tool_catalog_hash(tools: Sequence[ToolSpec]) -> str:
    """Stable hash of an offered tool set, name-ordered."""
    return canonical.sha256_obj([
        spec.to_json_obj() for spec in sorted(tools, key=lambda s: s.name)
    ])


# --------------------------------------------------------------------------
# builders
# --------------------------------------------------------------------------


def build_condition_a(*, model: str, task_query: str, deliverable: str | None,
                      max_output_tokens: int, effort: str | None = None,
                      extra: Mapping[str, Any] | None = None) -> ConditionContext:
    system = render_system_prompt(has_tools=False)
    request = ModelRequest(
        model=model, system=system,
        messages=(Message(role="user",
                          content=render_user_message(task_query, deliverable, None)),),
        tools=(), max_output_tokens=max_output_tokens, effort=effort,
        extra=dict(extra or {}),
    )
    return ConditionContext(condition=CONDITION_A, request=request)


def build_condition_b(*, model: str, task_query: str, deliverable: str | None,
                      max_output_tokens: int, raw_tools: Any,
                      effort: str | None = None,
                      extra: Mapping[str, Any] | None = None) -> ConditionContext:
    from .raw_repo import TOOL_SPECS as RAW_TOOL_SPECS

    system = render_system_prompt(has_tools=True)
    request = ModelRequest(
        model=model, system=system,
        messages=(Message(role="user",
                          content=render_user_message(task_query, deliverable, None)),),
        tools=RAW_TOOL_SPECS, max_output_tokens=max_output_tokens, effort=effort,
        extra=dict(extra or {}),
    )

    def dispatch(name: str, arguments: Mapping[str, Any]) -> ToolExecution:
        outcome = raw_tools.call(name, arguments)
        return ToolExecution(
            content=outcome.content, is_error=outcome.is_error,
            observability={"paths": list(outcome.paths), "matches": outcome.matches,
                           "truncated": outcome.truncated},
        )

    return ConditionContext(
        condition=CONDITION_B, request=request, tools=RAW_TOOL_SPECS,
        dispatcher=dispatch, observability={"raw_repo": raw_tools.describe()},
    )


def build_condition_c(*, model: str, task_query: str, deliverable: str | None,
                      max_output_tokens: int, bundle_result: Any,
                      effort: str | None = None,
                      extra: Mapping[str, Any] | None = None) -> ConditionContext:
    system = render_system_prompt(has_tools=False)
    request = ModelRequest(
        model=model, system=system,
        messages=(Message(
            role="user",
            content=render_user_message(task_query, deliverable, bundle_result.markdown),
        ),),
        tools=(), max_output_tokens=max_output_tokens, effort=effort,
        extra=dict(extra or {}),
    )
    return ConditionContext(
        condition=CONDITION_C, request=request,
        bundle=bundle_result.to_json_obj(),
        observability={"bundle": bundle_result.to_json_obj()},
    )


def build_condition_d(*, model: str, task_query: str, deliverable: str | None,
                      max_output_tokens: int, mcp_session: Any,
                      effort: str | None = None,
                      extra: Mapping[str, Any] | None = None) -> ConditionContext:
    system = render_system_prompt(has_tools=True)
    specs = mcp_session.tool_specs()
    request = ModelRequest(
        model=model, system=system,
        messages=(Message(role="user",
                          content=render_user_message(task_query, deliverable, None)),),
        tools=specs, max_output_tokens=max_output_tokens, effort=effort,
        extra=dict(extra or {}),
    )

    def dispatch(name: str, arguments: Mapping[str, Any]) -> ToolExecution:
        call = mcp_session.call(name, arguments)
        return ToolExecution(
            content=call.content, is_error=call.status != "ok",
            observability={"mcp_latency_ms": round(call.latency_ms, 2)},
        )

    return ConditionContext(
        condition=CONDITION_D, request=request, tools=specs, dispatcher=dispatch,
        observability={"mcp": mcp_session.describe()},
    )


# --------------------------------------------------------------------------
# isolation assertions (spec §40) — fail closed, before any paid request
# --------------------------------------------------------------------------


def assert_condition_isolation(context: ConditionContext, *,
                               expected_mcp_catalog: str | None = None,
                               snapshot_root: Path | None = None) -> None:
    """Verify a built condition can only see what its definition allows."""
    condition = context.condition
    if condition not in CONDITIONS:
        raise UsageError(f"unknown condition: {condition!r}")

    tool_names = tuple(sorted(spec.name for spec in context.tools))

    if condition == CONDITION_A:
        if context.tools or context.dispatcher is not None:
            raise IsolationError("condition A must expose no tools")
        if context.bundle is not None:
            raise IsolationError("condition A must have no injected context")
        _assert_no_injected_context(context)

    elif condition == CONDITION_B:
        from .raw_repo import TOOL_NAMES as RAW_NAMES

        if tool_names != tuple(sorted(RAW_NAMES)):
            raise IsolationError(
                f"condition B must expose exactly {sorted(RAW_NAMES)}; got {list(tool_names)}"
            )
        if context.dispatcher is None:
            raise IsolationError("condition B needs a raw-repo dispatcher")
        if context.bundle is not None:
            raise IsolationError("condition B must not receive a PAE bundle")
        _assert_no_injected_context(context)
        _assert_no_pae_leak(context)
        root = (context.observability.get("raw_repo") or {}).get("root_is_snapshot")
        if snapshot_root is not None and root is not True:
            raise IsolationError("condition B tools are not rooted at the snapshot")

    elif condition == CONDITION_C:
        if context.tools or context.dispatcher is not None:
            raise IsolationError("condition C must expose no tools")
        if context.bundle is None:
            raise IsolationError("condition C requires a compiled bundle")
        text = _user_text(context)
        if not text or len(text) <= 0:
            raise IsolationError("condition C injected no context")

    elif condition == CONDITION_D:
        from .pae_conditions import MCP_TOOL_NAMES

        if tool_names != tuple(sorted(MCP_TOOL_NAMES)):
            raise IsolationError(
                "condition D must expose exactly the four Phase 6 MCP tools; "
                f"got {list(tool_names)}"
            )
        if context.dispatcher is None:
            raise IsolationError("condition D needs an MCP dispatcher")
        if context.bundle is not None:
            raise IsolationError(
                "condition D must not be handed a precompiled bundle; "
                "it is defined by the model choosing to call the tools"
            )
        if expected_mcp_catalog is not None:
            actual = (context.observability.get("mcp") or {}).get("tool_catalog_sha256")
            if actual != expected_mcp_catalog:
                raise IsolationError(
                    "MCP tool catalog does not match the frozen plan: "
                    f"expected {expected_mcp_catalog}, served {actual}"
                )


def _user_text(context: ConditionContext) -> str:
    return "\n".join(m.content for m in context.request.messages if m.content)


def _assert_no_injected_context(context: ConditionContext) -> None:
    if INJECTED_CONTEXT_HEADER.split("\n")[0] in _user_text(context):
        raise IsolationError(
            f"condition {context.condition} must not carry injected reference material"
        )


#: Substrings that must never appear in a non-PAE condition's prompt. Not a
#: security boundary — the structural checks above are — but a cheap tripwire
#: for a prompt-assembly bug that silently tells the baseline about PAE.
_PAE_MARKERS = ("pae_search_resources", "pae_route_task", "pae_compose_bundle",
                "pae_get_resource", "PAE Registry", "ContextBundle")


def _assert_no_pae_leak(context: ConditionContext) -> None:
    haystack = (context.request.system + "\n" + _user_text(context))
    hits = [marker for marker in _PAE_MARKERS if marker in haystack]
    if hits:
        raise IsolationError(
            f"condition {context.condition} prompt mentions PAE internals: {hits}"
        )


def assert_prompt_fairness(contexts: Sequence[ConditionContext]) -> None:
    """Every condition must share one base prompt.

    Conditions with tools legitimately carry the extra tool-guidance paragraph;
    nothing else may differ. This is what stops a well-meaning tweak to "the
    PAE prompt" from becoming the finding.
    """
    by_shape: dict[bool, set[str]] = {}
    for context in contexts:
        has_tools = bool(context.tools)
        by_shape.setdefault(has_tools, set()).add(context.request.system)
    for has_tools, prompts in by_shape.items():
        if len(prompts) > 1:
            raise IsolationError(
                "conditions with the same tool shape must share one system prompt; "
                f"found {len(prompts)} distinct prompts for has_tools={has_tools}"
            )
    expected_tooled = render_system_prompt(has_tools=True)
    expected_bare = render_system_prompt(has_tools=False)
    for context in contexts:
        expected = expected_tooled if context.tools else expected_bare
        if context.request.system != expected:
            raise IsolationError(
                f"condition {context.condition} does not use the base system prompt"
            )

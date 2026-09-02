"""The four tools, and nothing else.

Each handler does the same four things in the same order:

1. accept transport input the SDK has already validated against the advertised
   schema;
2. call one existing Engine API;
3. project the result onto the two channels;
4. map any ``PaeError`` to a typed tool error.

No handler ranks, routes, packs, checks serving policy, opens a file or decides
what a resource is. If search or routing logic ever appears in this module,
something has gone wrong: those live in ``search.py`` and ``routing.py`` and the
adapter is not entitled to a second opinion.

The bounds in the schemas are **imported from the Engine**, never retyped. A
duplicated literal here would drift the day someone tunes a core limit, and the
advertised contract would start lying without anything failing.
"""

from __future__ import annotations

from typing import Annotated, Any, Callable, Literal, Optional, Sequence

from mcp_types import CallToolResult, TextContent, ToolAnnotations
from pydantic import Field

from .._lexical import MAX_LIMIT, MAX_QUERY_CHARS
from ..context import MAX_BUNDLE_BYTES, MAX_MAX_RESOURCES, Budget
from ..errors import PaeError, UsageError
from ..routing import MAX_ROUTE_LIMIT
from ..search import KINDS
from . import results as project
from .errors import error_payload
from .runtime import PaeRuntime

__all__ = ["DEFAULT_BUNDLE_TOKENS", "MAX_MCP_ESTIMATED_TOKENS", "MAX_REFS",
           "MAX_REF_CHARS", "MAX_SCOPES", "READ_ONLY", "register_tools"]

#: Used only when the caller supplies no budget at all. A caller who names a
#: byte budget must not silently also acquire a token cap they never asked for.
DEFAULT_BUNDLE_TOKENS = 8000

#: The largest estimated-token budget that can still bind under the default
#: bytes/4 estimator. Above this the byte ceiling governs regardless, so a
#: larger number would advertise a limit that does nothing.
MAX_MCP_ESTIMATED_TOKENS = MAX_BUNDLE_BYTES // 4

#: Adapter transport bounds. These are abuse protection on the wire, not
#: Registry grammar and not core Search semantics.
MAX_REF_CHARS = 4096
MAX_REFS = MAX_MAX_RESOURCES
MAX_SCOPES = 25

#: Read-only and closed-world are both true of every tool: nothing writes, and
#: the corpus is a fixed local snapshot. They are hints to the host, not
#: enforcement — the guarantees are that the Registry has no write path and the
#: adapter never opens a file.
READ_ONLY = ToolAnnotations(read_only_hint=True, open_world_hint=False)

# A static Literal is required for schema generation, but a second hand-written
# copy of the kind vocabulary is exactly the drift this module refuses to
# create elsewhere. So it is written once and checked against the core tuple at
# import time: if a kind is ever added, this fails immediately and loudly.
Kind = Literal["prompt", "technique", "skill", "agent", "command", "persona"]
_LITERAL_KINDS = ("prompt", "technique", "skill", "agent", "command", "persona")
if set(_LITERAL_KINDS) != set(KINDS):  # pragma: no cover - import-time guard
    raise RuntimeError(
        f"MCP kind literal {_LITERAL_KINDS} has drifted from Engine KINDS {KINDS}"
    )

QueryStr = Annotated[str, Field(min_length=1, max_length=MAX_QUERY_CHARS)]
RefStr = Annotated[str, Field(min_length=1, max_length=MAX_REF_CHARS)]
ScopeList = Annotated[list[str], Field(max_length=MAX_SCOPES)]


def _ok(text: str, structured: dict[str, Any]) -> CallToolResult:
    return CallToolResult(
        content=[TextContent(type="text", text=text)], structured_content=structured
    )


def _fail(exc: BaseException, runtime: PaeRuntime) -> CallToolResult:
    """A recoverable tool error: readable text plus a branchable code.

    ``is_error`` is set so a host renders it as a failure, but the turn is not
    a protocol fault — the model can read the code and try something else.
    """
    payload = error_payload(exc, repo_root=runtime.repository.root)
    message = payload["error"]["message"]
    code = payload["error"]["code"]
    return CallToolResult(
        content=[TextContent(type="text", text=f"[{code}] {message}")],
        structured_content=payload,
        is_error=True,
    )


def _guard(runtime: PaeRuntime, fn: Callable[[], CallToolResult]) -> CallToolResult:
    """Run a handler body, converting any failure into a tool error.

    The bare ``Exception`` arm is deliberate and is why ``error_payload``
    substitutes a fixed message for anything unrecognized: an unexpected fault
    must not reach the model as a traceback, and it must not take down a
    long-lived server either.
    """
    try:
        return fn()
    except PaeError as exc:
        return _fail(exc, runtime)
    except Exception as exc:  # noqa: BLE001 - see docstring
        return _fail(exc, runtime)


def register_tools(server: Any, runtime: PaeRuntime) -> None:
    """Attach the four tools, in a fixed order clients may cache."""

    # ---------------------------------------------------------------- search
    @server.tool(name="pae_search_resources", annotations=READ_ONLY)
    def pae_search_resources(
        query: QueryStr,
        limit: Annotated[int, Field(ge=1, le=MAX_LIMIT)] = 10,
        kinds: Optional[list[Kind]] = None,
        scopes: Optional[ScopeList] = None,
    ) -> CallToolResult:
        """Search the local PAE Registry by description and return ranked resource metadata.

        Lexical match over titles, descriptions, identifiers and tags. Resource
        bodies are neither read nor returned.
        """

        def run() -> CallToolResult:
            runtime.ensure_search_warm()
            found = runtime.search.search(
                query, kinds=kinds or None, scopes=scopes or None, limit=limit
            )
            return _ok(project.search_text(found), found.to_json_obj())

        return _guard(runtime, run)

    # ----------------------------------------------------------------- route
    @server.tool(name="pae_route_task", annotations=READ_ONLY)
    def pae_route_task(
        task: QueryStr,
        limit: Annotated[int, Field(ge=1, le=MAX_ROUTE_LIMIT)] = 5,
        kinds: Optional[list[Kind]] = None,
    ) -> CallToolResult:
        """Decide which scope and kind of PAE resource should handle a task.

        May report the route as ambiguous or weak rather than selecting one.
        Returns metadata only; no resource bodies.
        """

        def run() -> CallToolResult:
            runtime.ensure_search_warm()
            decision = runtime.router.route(task, kinds=kinds or None, limit=limit)
            return _ok(project.route_text(decision), decision.to_json_obj())

        return _guard(runtime, run)

    # ------------------------------------------------------------------- get
    @server.tool(name="pae_get_resource", annotations=READ_ONLY)
    def pae_get_resource(
        ref: RefStr,
        include_content: bool = False,
    ) -> CallToolResult:
        """Return metadata for one PAE resource by UID or public ID.

        With include_content, also returns its whole verified body when serving
        policy allows; some resources are served as metadata only.
        """

        def run() -> CallToolResult:
            # lookup(), not resolve(): resolve() answers for excluded resources
            # too, which is right for identity and wrong for serving.
            resolution, record = runtime.registry.lookup(ref)
            if not include_content:
                return _ok(
                    project.resource_text(record, resolution),
                    project.resource_structured(record, resolution),
                )
            content = runtime.registry.content(ref)
            body = content.text()
            return _ok(
                project.framed_body(record, content, body),
                project.resource_structured(record, resolution, content),
            )

        return _guard(runtime, run)

    # --------------------------------------------------------------- compose
    @server.tool(name="pae_compose_bundle", annotations=READ_ONLY)
    def pae_compose_bundle(
        task: Optional[QueryStr] = None,
        refs: Optional[Annotated[list[RefStr], Field(max_length=MAX_REFS)]] = None,
        budget_estimated_tokens: Optional[
            Annotated[int, Field(ge=1, le=MAX_MCP_ESTIMATED_TOKENS)]
        ] = None,
        budget_bytes: Optional[Annotated[int, Field(ge=1, le=MAX_BUNDLE_BYTES)]] = None,
        max_resources: Annotated[int, Field(ge=1, le=MAX_MAX_RESOURCES)] = MAX_MAX_RESOURCES,
        kinds: Optional[list[Kind]] = None,
        scopes: Optional[ScopeList] = None,
    ) -> CallToolResult:
        """Assemble whole verified PAE resource bodies into one budgeted context bundle.

        Give either a task (routed automatically) or an explicit list of refs.
        Returns the bundle as Markdown for direct use, plus an audit record of
        what was included, omitted and why.
        """

        def run() -> CallToolResult:
            has_task = bool(task)
            has_refs = bool(refs)
            if has_task == has_refs:
                raise UsageError(
                    "give exactly one of 'task' or 'refs'",
                    requested=["task" if has_task else None, "refs" if has_refs else None],
                )

            budget = _budget(budget_estimated_tokens, budget_bytes, max_resources)

            if has_refs:
                # Rejected rather than ignored: silently dropping a filter the
                # caller supplied would answer a question they did not ask.
                if kinds or scopes:
                    raise UsageError(
                        "'kinds' and 'scopes' apply to task mode only; explicit refs "
                        "are compiled exactly as given",
                        requested=sorted(
                            [n for n, v in (("kinds", kinds), ("scopes", scopes)) if v]
                        ),
                    )
                bundle = runtime.compiler.compile_refs(list(refs or ()), budget=budget)
            else:
                runtime.ensure_search_warm()
                decision = runtime.router.route(
                    str(task), kinds=kinds or None, limit=MAX_ROUTE_LIMIT
                )
                bundle = runtime.compiler.compile_route(
                    decision, budget=budget, scopes=list(scopes) if scopes else None
                )

            # Exactly the canonical rendering, with nothing prepended: it already
            # carries its own framing, and Phase 5 defined these bytes.
            return _ok(bundle.render_markdown(), project.bundle_audit(bundle))

        return _guard(runtime, run)


def _budget(
    estimated_tokens: Optional[int], byte_limit: Optional[int], max_resources: int
) -> Budget:
    """Turn the two optional limits into a Budget without inventing one.

    The default only applies when the caller named no limit at all. A caller who
    asked for a byte budget gets a byte budget — attaching a token cap they did
    not request would quietly shrink their bundle for reasons they could not see.
    """
    if estimated_tokens is None and byte_limit is None:
        return Budget(estimated_tokens=DEFAULT_BUNDLE_TOKENS, max_resources=max_resources)
    return Budget(
        estimated_tokens=estimated_tokens,
        bytes=byte_limit,
        max_resources=max_resources,
    )

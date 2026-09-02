"""Conditions C and D — the two arms that actually use PAE.

Condition C runs the Engine *outside* the participant model: route, compile,
render, inject the canonical Markdown. No tools. It isolates the value of
context selection from the value of tool-use behaviour, which is the only way
to tell "the bundle is good" apart from "the agent drove the tools well".

Condition D gives the model the four Phase 6 MCP tools over stdio and lets it
decide. This is the complete agent-native product.

Both bind to the same participant snapshot as Condition B. If they did not, the
comparison would be measuring different corpora and no amount of statistics
would fix it.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import canonical
from .errors import InfrastructureFailure, IsolationError, UsageError
from .providers.base import ToolSpec

#: The four tools Phase 6 serves. Anything else appearing in Condition D is an
#: isolation failure, not a surprise feature.
MCP_TOOL_NAMES = (
    "pae_search_resources",
    "pae_route_task",
    "pae_get_resource",
    "pae_compose_bundle",
)


# ==========================================================================
# Condition C — deterministic bundle
# ==========================================================================


@dataclass
class BundleResult:
    """The audit record for one compiled bundle."""

    markdown: str
    bundle_sha256: str
    route_status: str | None
    selected_scope: str | None
    selected_kind: str | None
    coverage: float | None
    margin: float | None
    included_uids: tuple[str, ...]
    omitted: tuple[dict[str, str], ...]
    budget_report: Mapping[str, Any]
    warnings: tuple[str, ...]

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "bundle_sha256": self.bundle_sha256,
            "route_status": self.route_status,
            "selected_scope": self.selected_scope,
            "selected_kind": self.selected_kind,
            "coverage": self.coverage,
            "margin": self.margin,
            "included_uids": list(self.included_uids),
            "omitted": [dict(o) for o in self.omitted],
            "budget_report": dict(self.budget_report),
            "warnings": list(self.warnings),
        }


class BundleCompiler:
    """Runs Router + ContextCompiler against a snapshot, outside the model."""

    def __init__(self, snapshot_root: Path, *, budget_estimated_tokens: int = 8000,
                 budget_bytes: int | None = None, max_resources: int = 25) -> None:
        # Imported here, not at module scope: `plan` and `validate-benchmark`
        # must work in an environment where the Engine is not installed.
        from pae_engine import Registry, Repository, Router, SearchEngine
        from pae_engine.context import Budget, ContextCompiler

        self.snapshot_root = Path(snapshot_root).resolve()
        self._registry = Registry.open(Repository.at(self.snapshot_root))
        self._engine = SearchEngine(self._registry)
        self._router = Router(self._engine)
        self._compiler = ContextCompiler(self._registry)
        self._budget = Budget(
            estimated_tokens=budget_estimated_tokens,
            bytes=budget_bytes,
            max_resources=max_resources,
        )

    def compile_for(self, task: str) -> BundleResult:
        decision = self._router.route(task)
        bundle = self._compiler.compile_route(decision, budget=self._budget)
        obj = bundle.to_json_obj()
        return BundleResult(
            markdown=bundle.render_markdown(),
            bundle_sha256=obj["bundle_sha256"],
            route_status=obj["route_status"],
            selected_scope=obj["selected_scope"],
            selected_kind=obj["selected_kind"],
            coverage=obj["coverage"],
            margin=obj["margin"],
            included_uids=tuple(item["uid"] for item in obj["included"]),
            omitted=tuple(
                {"uid": o.get("uid", ""), "reason": o.get("reason", "")}
                for o in obj["omitted"]
            ),
            budget_report=obj["budget"],
            warnings=tuple(obj["warnings"]),
        )

    def describe(self) -> Mapping[str, Any]:
        return {
            "budget_estimated_tokens": self._budget.estimated_tokens,
            "budget_bytes": self._budget.bytes,
            "max_resources": self._budget.max_resources,
            "snapshot_root_is_participant": True,
        }


# ==========================================================================
# Condition D — MCP over stdio
# ==========================================================================


@dataclass
class McpCall:
    name: str
    arguments: Mapping[str, Any]
    status: str
    content: str
    latency_ms: float
    bytes_returned: int


@dataclass
class McpLog:
    calls: list[McpCall] = field(default_factory=list)

    def record(self, call: McpCall) -> None:
        self.calls.append(call)

    def summary(self) -> dict[str, Any]:
        return {
            "tool_calls": len(self.calls),
            "unique_tools": len({c.name for c in self.calls}),
            "error_calls": sum(1 for c in self.calls if c.status != "ok"),
            "total_tool_bytes": sum(c.bytes_returned for c in self.calls),
            "sequence": [c.name for c in self.calls],
        }


class McpSession:
    """One ``pae mcp`` subprocess, spoken to over stdio JSON-RPC.

    A minimal client is used rather than the SDK's, for one reason: the harness
    must be able to run Condition D's *isolation checks* — that exactly four
    tools are exposed and their catalog hash matches the frozen plan — in an
    environment where the optional MCP extra is not installed, which is where
    CI lives. The wire protocol here is the same JSON-RPC 2.0 over stdio that
    the SDK speaks; ``use_sdk_client`` switches to the official client when the
    extra is present.

    One process per trial. A server that crashed mid-task must not carry state
    into the next one.
    """

    def __init__(
        self,
        snapshot_root: Path,
        *,
        executable: Sequence[str] | None = None,
        timeout_s: float = 30.0,
        env: Mapping[str, str] | None = None,
    ) -> None:
        self.snapshot_root = Path(snapshot_root).resolve()
        self.timeout_s = timeout_s
        self._argv = list(executable) if executable else [
            sys.executable, "-m", "pae_engine", "mcp", "--repo", str(self.snapshot_root),
        ]
        self._env = dict(env) if env is not None else _clean_env()
        self._proc: subprocess.Popen | None = None
        self._next_id = 0
        self._lock = threading.Lock()
        self.log = McpLog()
        self.tools: tuple[dict[str, Any], ...] = ()

    # -- lifecycle ---------------------------------------------------------

    def __enter__(self) -> "McpSession":
        self.start()
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def start(self) -> None:
        try:
            self._proc = subprocess.Popen(
                self._argv,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                env=self._env, cwd=str(self.snapshot_root), bufsize=0,
            )
        except OSError as exc:
            raise InfrastructureFailure(
                f"could not start the MCP server: {exc}", "mcp_process_died"
            ) from exc

        self._request("initialize", {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "pae-eval", "version": "0.1.0.dev0"},
        })
        self._notify("notifications/initialized", {})
        listed = self._request("tools/list", {})
        self.tools = tuple(listed.get("tools", []))

    def close(self) -> None:
        proc, self._proc = self._proc, None
        if proc is None:
            return
        try:
            if proc.stdin:
                proc.stdin.close()
            proc.wait(timeout=5)
        except (subprocess.TimeoutExpired, OSError):
            proc.kill()
            try:
                proc.wait(timeout=5)
            except Exception:  # pragma: no cover
                pass

    # -- JSON-RPC ----------------------------------------------------------

    def _send(self, payload: Mapping[str, Any]) -> None:
        proc = self._proc
        if proc is None or proc.stdin is None:
            raise InfrastructureFailure("MCP server is not running", "mcp_process_died")
        line = json.dumps(payload, ensure_ascii=False) + "\n"
        try:
            proc.stdin.write(line.encode("utf-8"))
            proc.stdin.flush()
        except (BrokenPipeError, OSError) as exc:
            raise InfrastructureFailure(
                f"MCP server closed its input: {exc}", "mcp_process_died"
            ) from exc

    def _notify(self, method: str, params: Mapping[str, Any]) -> None:
        self._send({"jsonrpc": "2.0", "method": method, "params": dict(params)})

    def _request(self, method: str, params: Mapping[str, Any]) -> dict[str, Any]:
        with self._lock:
            self._next_id += 1
            request_id = self._next_id
            self._send({
                "jsonrpc": "2.0", "id": request_id,
                "method": method, "params": dict(params),
            })
            deadline = time.monotonic() + self.timeout_s
            while True:
                message = self._read_message(deadline)
                if message.get("id") == request_id:
                    if "error" in message:
                        raise UsageError(
                            f"MCP error from {method}: {message['error']}"
                        )
                    return message.get("result", {}) or {}
                # Server-initiated traffic; nothing here needs it.

    def _read_message(self, deadline: float) -> dict[str, Any]:
        proc = self._proc
        if proc is None or proc.stdout is None:
            raise InfrastructureFailure("MCP server is not running", "mcp_process_died")
        while True:
            if time.monotonic() > deadline:
                raise InfrastructureFailure(
                    "timed out waiting for the MCP server", "mcp_process_died"
                )
            raw = proc.stdout.readline()
            if not raw:
                stderr = b""
                if proc.stderr is not None:
                    try:
                        stderr = proc.stderr.read() or b""
                    except Exception:  # pragma: no cover
                        stderr = b""
                raise InfrastructureFailure(
                    "MCP server exited: "
                    + stderr.decode("utf-8", "replace").strip()[:500],
                    "mcp_process_died",
                )
            text = raw.decode("utf-8", "replace").strip()
            if not text:
                continue
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                continue  # non-protocol chatter on stdout

    # -- tools -------------------------------------------------------------

    def tool_specs(self) -> tuple[ToolSpec, ...]:
        return tuple(
            ToolSpec(
                name=tool.get("name", ""),
                description=tool.get("description", "") or "",
                input_schema=tool.get("inputSchema") or tool.get("input_schema") or {},
            )
            for tool in self.tools
        )

    def catalog_hash(self) -> str:
        """Hash of the exposed catalog, for comparison against the frozen plan."""
        return canonical.sha256_obj([
            {
                "name": t.get("name"),
                "description": t.get("description"),
                "input_schema": t.get("inputSchema") or t.get("input_schema") or {},
            }
            for t in sorted(self.tools, key=lambda t: t.get("name", ""))
        ])

    def assert_expected_tools(self) -> None:
        names = tuple(sorted(t.get("name", "") for t in self.tools))
        if names != tuple(sorted(MCP_TOOL_NAMES)):
            raise IsolationError(
                "condition D must expose exactly the four Phase 6 MCP tools; "
                f"server offered {list(names)}"
            )

    def call(self, name: str, arguments: Mapping[str, Any]) -> McpCall:
        started = time.perf_counter()
        status = "ok"
        try:
            result = self._request("tools/call", {"name": name, "arguments": dict(arguments)})
            content = _render_mcp_content(result)
            if result.get("isError"):
                status = "error"
        except UsageError as exc:
            status, content = "error", f"error: {exc}"
        latency = (time.perf_counter() - started) * 1000.0
        call = McpCall(
            name=name, arguments=dict(arguments), status=status, content=content,
            latency_ms=latency, bytes_returned=len(content.encode("utf-8")),
        )
        self.log.record(call)
        return call

    def describe(self) -> Mapping[str, Any]:
        return {
            "argv": list(self._argv[:2]) + ["...", "--repo", "<snapshot>"],
            "tool_names": sorted(t.get("name", "") for t in self.tools),
            "tool_catalog_sha256": self.catalog_hash(),
            "mcp_sdk_version": mcp_sdk_version(),
        }


def _render_mcp_content(result: Mapping[str, Any]) -> str:
    parts: list[str] = []
    for block in result.get("content", []) or []:
        if isinstance(block, Mapping):
            if block.get("type") == "text":
                parts.append(str(block.get("text", "")))
            else:
                parts.append(json.dumps(block, ensure_ascii=False, sort_keys=True))
    if not parts and "structuredContent" in result:
        parts.append(json.dumps(result["structuredContent"], ensure_ascii=False,
                                sort_keys=True))
    return "\n".join(parts)


def _clean_env() -> dict[str, str]:
    """Environment for the server: no inherited ``PAE_*``, no provider keys.

    The server is told which checkout to read through ``--repo``. Letting a
    developer's ``PAE_REPO`` reach it would silently point Condition D at the
    real working tree instead of the snapshot.
    """
    blocked_prefixes = ("PAE_",)
    blocked_exact = {
        "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "OPENAI_API_KEY",
        "ANTHROPIC_BASE_URL", "OPENAI_BASE_URL",
    }
    return {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(blocked_prefixes) and key not in blocked_exact
    }


def mcp_sdk_version() -> str | None:
    try:
        import importlib.metadata as md

        return md.version("mcp")
    except Exception:
        return None

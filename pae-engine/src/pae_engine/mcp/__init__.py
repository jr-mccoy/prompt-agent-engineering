"""The optional MCP server adapter.

**This module must remain importable without the MCP SDK installed.** Nothing at
module level may import ``mcp``, ``mcp_types`` or ``pydantic``, because the CLI
imports this package in order to find out whether the SDK is there at all. The
submodules that do need the SDK — :mod:`.server`, :mod:`.tools` — are reached
only after :func:`require_sdk` has confirmed it is present.

That is also why the base Engine never imports this package. ``import
pae_engine`` stays dependency-free; the adapter is reached exclusively through
``pae mcp``.
"""

from __future__ import annotations

from typing import Any

from ..errors import MissingExtra

__all__ = ["EXTRA_NAME", "INSTALL_HINT", "sdk_available", "require_sdk"]

EXTRA_NAME = "mcp"
INSTALL_HINT = "pip install 'prompt-agent-engineering[mcp]'"


def sdk_available() -> bool:
    """Whether the MCP extra is installed.

    The distinction that matters here is **"the extra is absent"** versus
    **"the extra is installed and broken"**, and only the first is this
    function's business. So a failure is inspected rather than swallowed: if
    the missing module is ``mcp`` itself, the extra was never installed and the
    caller gets a clean usage error naming the install command. If something
    *else* is missing — a transitive dependency of the SDK — that is a genuine
    runtime fault and is re-raised, because telling someone to install a
    package they already have would send them in a circle.

    A trial import rather than a spec lookup, deliberately: ``find_spec`` cannot
    tell a working installation from a broken one, and every caller of this
    function is about to import the SDK anyway, so the import is not wasted.
    """
    try:
        import mcp  # noqa: F401
    except ModuleNotFoundError as exc:
        if (exc.name or "").split(".")[0] == "mcp":
            return False
        raise
    return True


def require_sdk() -> None:
    """Raise :class:`MissingExtra` when the MCP extra is not installed."""
    if not sdk_available():
        raise MissingExtra(
            "the MCP server needs the optional 'mcp' extra, which is not installed",
            extra=EXTRA_NAME,
            install=INSTALL_HINT,
        )


def __getattr__(name: str) -> Any:
    """Expose the SDK-dependent entry points lazily.

    ``from pae_engine.mcp import serve_stdio`` works when the extra is present
    and raises :class:`MissingExtra` when it is not — rather than an
    ``ImportError`` naming a third-party package the caller never asked for.
    """
    if name in ("serve_stdio", "build_server", "SERVER_NAME"):
        require_sdk()
        from . import server as _server

        return getattr(_server, name)
    if name == "PaeRuntime":
        from .runtime import PaeRuntime

        return PaeRuntime
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

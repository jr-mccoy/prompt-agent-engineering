"""Building and serving the PAE MCP server.

Transport is stdio, and only stdio. That is not a placeholder for HTTP: stdio
matches what the Engine already is — a local, offline, read-only runtime bound
to a checkout on the same filesystem — and it opens no listener, needs no
authorization, and has no remote threat model to reason about. Adding HTTP is a
separate product decision with its own prerequisites, recorded in ADR-0030.

The server name and version are not maintained here. The version is
``pae_engine.__version__``, so a second constant can never disagree with the
package about which Engine a client is talking to.
"""

from __future__ import annotations

import asyncio
from typing import Any, Optional

from mcp.server import MCPServer

from .._version import __version__
from ..repository import Repository
from .runtime import PaeRuntime
from .tools import register_tools

__all__ = ["SERVER_NAME", "build_server", "serve_stdio"]

#: Advertised server name. Distinct from the distribution name because a host
#: shows this next to tools from other servers.
SERVER_NAME = "pae"

_INSTRUCTIONS = (
    "Read-only access to a local PAE Registry checkout. Search and routing "
    "return metadata only; compose_bundle returns whole verified resource "
    "bodies assembled into one budgeted context bundle. The server answers "
    "from a single checkout snapshot fixed at startup — restart it to observe "
    "a changed checkout."
)


def build_server(runtime: PaeRuntime) -> MCPServer:
    """Construct the server and register the four tools.

    Construction is deterministic: the same Engine version and the same tool
    definitions always produce the same ``tools/list``. Clients may cache that
    catalog, so nothing here may vary with the corpus, the clock or the
    environment.
    """
    server = MCPServer(
        name=SERVER_NAME,
        version=__version__,
        instructions=_INSTRUCTIONS,
    )
    register_tools(server, runtime)
    return server


def serve_stdio(
    repository: Repository, *, warm: bool = True
) -> None:
    """Serve one checkout over stdio until the client disconnects.

    Warmup starts *after* the server is constructed but does not block serving:
    ``tools/list`` needs no index and should answer immediately, while the
    ~1 s lexical build proceeds on a background thread. A search that arrives
    mid-build waits on the same lock the warmup holds, so exactly one build
    happens no matter how the calls interleave.

    Nothing in this function writes to stdout. That channel belongs to the
    protocol, and a single stray line on it is a spec violation that some hosts
    will not tolerate — diagnostics go to stderr.
    """
    runtime = PaeRuntime(repository)
    server = build_server(runtime)
    if warm:
        runtime.start_background_warmup()
    asyncio.run(server.run_stdio_async())

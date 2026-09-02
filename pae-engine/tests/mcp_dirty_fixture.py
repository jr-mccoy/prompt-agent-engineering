"""A deliberately non-compliant MCP server, used as a negative control.

This exists to prove the stdout purity checker actually detects contamination.
Phase 6A found that the official client *tolerates* malformed stdout lines — it
logs a parse failure and skips them — so "the session succeeded" is not evidence
of purity. Without a fixture that is known-dirty, an assertion that the real
server is clean could pass because the checker never worked.

Every line it prints to stdout before serving is a realistic mistake: a startup
banner, and an absolute repository path.

Never imported by the adapter. Test scaffolding only.
"""

from __future__ import annotations

import asyncio
import os
import sys

from pae_engine import Repository
from pae_engine.mcp.runtime import PaeRuntime
from pae_engine.mcp.server import build_server


def main() -> int:
    root = os.environ["PAE_REPO"]

    # --- the contamination, on purpose ------------------------------------
    print("PAE Engine (dirty fixture)")
    print(f"repository: {root}")
    sys.stdout.flush()
    # ----------------------------------------------------------------------

    server = build_server(PaeRuntime(Repository.at(root)))
    asyncio.run(server.run_stdio_async())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

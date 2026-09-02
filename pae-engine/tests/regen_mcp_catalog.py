"""Regenerate the committed MCP tool-catalog snapshot.

Run deliberately, and read the diff:

    PYTHONPATH=src:tests python3 tests/regen_mcp_catalog.py

The catalog is product API that clients cache, so a change here is a change
users see. This script exists so that updating the snapshot is an explicit act
rather than something a test quietly does for you.
"""

from __future__ import annotations

import asyncio
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fixtures  # noqa: E402
from test_mcp_catalog import SNAPSHOT, normalized_catalog  # noqa: E402

from mcp import Client  # noqa: E402

from pae_engine import Repository  # noqa: E402
from pae_engine.mcp.runtime import PaeRuntime  # noqa: E402
from pae_engine.mcp.server import build_server  # noqa: E402


async def _catalog(server):
    async with Client(server) as client:
        return normalized_catalog((await client.list_tools()).tools)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="pae-catalog-") as tmp:
        root = fixtures.standard_repo(Path(tmp) / "repo")
        server = build_server(PaeRuntime(Repository.at(root)))
        catalog = asyncio.run(_catalog(server))

    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(
        json.dumps(catalog, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"wrote {SNAPSHOT} ({len(catalog)} tools)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

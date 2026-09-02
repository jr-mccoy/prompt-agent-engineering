"""The tool catalog is product API, so it is pinned.

Clients cache ``tools/list``. A silent change to a name, a description, a bound
or an annotation therefore reaches agents that will not re-read it, which makes
the catalog exactly the kind of surface that should be hard to change by
accident and easy to change on purpose.

Two things are checked:

* the catalog is **deterministic** — same Engine, same catalog, every time;
* the advertised bounds are **the Engine's own constants**, not copies. A
  duplicated literal would drift the day someone tunes a core limit, and the
  advertised contract would start lying without any test failing.

The snapshot deliberately drops SDK-generated cosmetics such as ``title``, which
carry no contract and would churn between compatible 2.x releases.
"""

from __future__ import annotations

import asyncio
import json
import unittest
from pathlib import Path

import fixtures
from _support import EngineTestCase

from pae_engine import Repository
from pae_engine.mcp import sdk_available

if not sdk_available():  # pragma: no cover - exercised by the base CI job
    raise unittest.SkipTest("the MCP extra is not installed")

from mcp import Client  # noqa: E402

from pae_engine._lexical import MAX_LIMIT, MAX_QUERY_CHARS  # noqa: E402
from pae_engine.context import MAX_BUNDLE_BYTES, MAX_MAX_RESOURCES  # noqa: E402
from pae_engine.mcp.runtime import PaeRuntime  # noqa: E402
from pae_engine.mcp.server import build_server  # noqa: E402
from pae_engine.mcp.tools import MAX_MCP_ESTIMATED_TOKENS, MAX_REFS  # noqa: E402
from pae_engine.routing import MAX_ROUTE_LIMIT  # noqa: E402

SNAPSHOT = Path(__file__).resolve().parent / "data" / "mcp_tool_catalog.json"

#: Keys the SDK generates for presentation, not contract.
_COSMETIC = {"title"}


def _normalize_schema(node):
    if isinstance(node, dict):
        return {
            key: _normalize_schema(value)
            for key, value in sorted(node.items())
            if key not in _COSMETIC
        }
    if isinstance(node, list):
        return [_normalize_schema(item) for item in node]
    return node


def normalized_catalog(tools) -> list[dict]:
    """Order-preserving, cosmetics-free view of ``tools/list``."""
    out = []
    for tool in tools:
        annotations = tool.annotations
        out.append(
            {
                "name": tool.name,
                "description": (tool.description or "").strip(),
                "input_schema": _normalize_schema(tool.input_schema),
                "annotations": {
                    "read_only_hint": annotations.read_only_hint if annotations else None,
                    "open_world_hint": annotations.open_world_hint if annotations else None,
                },
            }
        )
    return out


class CatalogTestCase(EngineTestCase):
    def catalog(self) -> list[dict]:
        root = fixtures.standard_repo(self.tmp_path())
        server = build_server(PaeRuntime(Repository.at(root)))

        async def run():
            async with Client(server) as client:
                return await client.list_tools()

        return normalized_catalog(asyncio.run(run()).tools)


class TestCatalogDeterminism(CatalogTestCase):
    def test_independent_constructions_produce_an_identical_catalog(self) -> None:
        first = json.dumps(self.catalog(), sort_keys=True)
        second = json.dumps(self.catalog(), sort_keys=True)
        third = json.dumps(self.catalog(), sort_keys=True)
        self.assertEqual(first, second)
        self.assertEqual(second, third)

    def test_catalog_matches_the_committed_snapshot(self) -> None:
        self.assertTrue(
            SNAPSHOT.is_file(),
            f"missing snapshot {SNAPSHOT}; regenerate with tests/regen_mcp_catalog.py",
        )
        expected = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        actual = self.catalog()
        self.assertEqual(
            actual,
            expected,
            "the MCP tool catalog changed. Clients cache this. If the change is "
            "intended, regenerate with tests/regen_mcp_catalog.py and review the diff.",
        )


class TestSchemasReuseEngineConstants(CatalogTestCase):
    """Advertised bounds must be the Engine's, not a second opinion."""

    def setUp(self) -> None:
        super().setUp()
        self.by_name = {tool["name"]: tool for tool in self.catalog()}

    def prop(self, tool: str, name: str) -> dict:
        return self.by_name[tool]["input_schema"]["properties"][name]

    def test_search_query_bound_is_max_query_chars(self) -> None:
        self.assertEqual(self.prop("pae_search_resources", "query")["maxLength"], MAX_QUERY_CHARS)

    def test_route_task_bound_is_max_query_chars(self) -> None:
        self.assertEqual(self.prop("pae_route_task", "task")["maxLength"], MAX_QUERY_CHARS)

    def test_search_limit_bound_is_max_limit(self) -> None:
        self.assertEqual(self.prop("pae_search_resources", "limit")["maximum"], MAX_LIMIT)

    def test_route_limit_bound_is_max_route_limit(self) -> None:
        self.assertEqual(self.prop("pae_route_task", "limit")["maximum"], MAX_ROUTE_LIMIT)

    def test_bundle_byte_bound_is_max_bundle_bytes(self) -> None:
        schema = self.prop("pae_compose_bundle", "budget_bytes")
        self.assertIn(str(MAX_BUNDLE_BYTES), json.dumps(schema))

    def test_bundle_max_resources_bound_is_max_max_resources(self) -> None:
        schema = self.prop("pae_compose_bundle", "max_resources")
        self.assertEqual(schema["maximum"], MAX_MAX_RESOURCES)

    def test_estimated_token_bound_is_derived_from_the_byte_ceiling(self) -> None:
        # Above this the byte ceiling governs regardless under the default
        # bytes/4 estimator, so a larger advertised bound would do nothing.
        self.assertEqual(MAX_MCP_ESTIMATED_TOKENS, MAX_BUNDLE_BYTES // 4)
        schema = self.prop("pae_compose_bundle", "budget_estimated_tokens")
        self.assertIn(str(MAX_MCP_ESTIMATED_TOKENS), json.dumps(schema))

    def test_refs_bound_matches_the_inclusion_ceiling(self) -> None:
        self.assertEqual(MAX_REFS, MAX_MAX_RESOURCES)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

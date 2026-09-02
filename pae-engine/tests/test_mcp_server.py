"""The adapter driven through the official MCP client, in process.

This is the layer that proves the contract a host actually sees: advertised
schemas, the two result channels, typed tool errors, and the invariants that
only appear once real transport validation is in the loop.

Skipped wholesale when the ``mcp`` extra is absent, which is the normal state of
the base CI job.
"""

from __future__ import annotations

import asyncio
import json
import unittest
from pathlib import Path

import fixtures
from _support import EngineTestCase

from pae_engine import Budget, Repository
from pae_engine.mcp import sdk_available

if not sdk_available():  # pragma: no cover - exercised by the base CI job
    raise unittest.SkipTest("the MCP extra is not installed")

from mcp import Client  # noqa: E402

from pae_engine.mcp.runtime import PaeRuntime  # noqa: E402
from pae_engine.mcp.server import build_server  # noqa: E402
from pae_engine.mcp.tools import DEFAULT_BUNDLE_TOKENS  # noqa: E402

ENGINE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_ROOT.parent


def text_of(result) -> str:
    return "".join(getattr(block, "text", "") or "" for block in result.content)


def structured_blob(result) -> str:
    if not result.structured_content:
        return ""
    return json.dumps(result.structured_content, ensure_ascii=False)


class McpClientTestCase(EngineTestCase):
    """Builds a fixture checkout and talks to it through the official client."""

    def build(self, root=None):
        root = root or fixtures.standard_repo(self.tmp_path())
        runtime = PaeRuntime(Repository.at(root))
        return runtime, build_server(runtime)

    def call(self, server, name, args):
        async def run():
            async with Client(server) as client:
                return await client.call_tool(name, args)

        return asyncio.run(run())

    def tools(self, server):
        async def run():
            async with Client(server) as client:
                return await client.list_tools()

        return asyncio.run(run())


class TestToolSurface(McpClientTestCase):
    def test_exactly_four_tools_in_a_fixed_order(self) -> None:
        _runtime, server = self.build()
        names = [t.name for t in self.tools(server).tools]
        self.assertEqual(
            names,
            [
                "pae_search_resources",
                "pae_route_task",
                "pae_get_resource",
                "pae_compose_bundle",
            ],
        )

    def test_every_tool_is_read_only_and_closed_world(self) -> None:
        _runtime, server = self.build()
        for tool in self.tools(server).tools:
            self.assertIsNotNone(tool.annotations, tool.name)
            self.assertTrue(tool.annotations.read_only_hint, tool.name)
            self.assertFalse(tool.annotations.open_world_hint, tool.name)

    def test_no_tool_accepts_a_filesystem_or_repository_argument(self) -> None:
        # The repository is startup configuration. A tool argument that could
        # redirect it would hand repository selection to the model.
        banned = {
            "repo", "repository", "root", "path", "file", "filename",
            "cwd", "directory", "checkout", "dir", "source_path",
        }
        _runtime, server = self.build()
        for tool in self.tools(server).tools:
            for prop in tool.input_schema.get("properties", {}):
                self.assertNotIn(prop.lower(), banned, f"{tool.name}.{prop}")


class TestSearchAndRoute(McpClientTestCase):
    def test_search_returns_ranked_metadata_and_no_body(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_search_resources", {"query": "fixture", "limit": 5})
        self.assertFalse(result.is_error)
        body_marker = fixtures.STANDARD_BODY.decode().strip().splitlines()[-1]
        self.assertNotIn(body_marker, text_of(result))
        self.assertNotIn(body_marker, structured_blob(result))
        self.assertIn("Search:", text_of(result))
        self.assertIn("hits", result.structured_content)

    def test_route_reports_ambiguity_rather_than_guessing(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_route_task", {"task": "fixture resource"})
        self.assertFalse(result.is_error)
        text = text_of(result)
        self.assertIn("Route status:", text)
        self.assertIn("not confidence scores", text)
        status = result.structured_content["status"]
        if status != "matched":
            self.assertIn("No route selected", text)
        else:
            self.assertIn("Selected scope:", text)

    def test_excluded_resources_stay_invisible_to_search(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_search_resources", {"query": "excluded", "limit": 50})
        blob = text_of(result) + structured_blob(result)
        self.assertNotIn(fixtures.EXCLUDED_UID, blob)
        self.assertNotIn("Excluded Fixture", blob)


class TestGetResource(McpClientTestCase):
    def test_metadata_only_by_default(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_get_resource", {"ref": fixtures.STANDARD_ID})
        self.assertFalse(result.is_error)
        self.assertFalse(result.structured_content["content_returned"])
        self.assertNotIn(fixtures.STANDARD_BODY.decode().strip(), text_of(result))

    def test_body_appears_in_text_only_and_unchanged(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_get_resource",
            {"ref": fixtures.SAFETY_ID, "include_content": True},
        )
        body = fixtures.SAFETY_BODY.decode()
        self.assertIn(body, text_of(result))
        self.assertNotIn(body.strip(), structured_blob(result))
        self.assertTrue(result.structured_content["content_returned"])
        self.assertIn("content_sha256", result.structured_content["content_verification"])

    def test_withheld_body_is_a_typed_refusal(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_get_resource",
            {"ref": fixtures.METADATA_ONLY_ID, "include_content": True},
        )
        self.assertTrue(result.is_error)
        self.assertEqual(result.structured_content["error"]["code"], "content_refused")
        self.assertNotIn("This body must never be served", structured_blob(result))
        self.assertNotIn("This body must never be served", text_of(result))

    def test_excluded_resource_yields_only_its_identity_stub(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_get_resource", {"ref": fixtures.EXCLUDED_ID})
        self.assertTrue(result.is_error)
        payload = result.structured_content["error"]
        self.assertEqual(payload["code"], "resource_excluded")
        blob = text_of(result) + structured_blob(result)
        self.assertNotIn("Excluded Fixture", blob)
        self.assertNotIn("Must never be returned", blob)

    def test_technique_reports_no_addressable_body(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_get_resource",
            {"ref": fixtures.TECHNIQUE_ID, "include_content": True},
        )
        self.assertTrue(result.is_error)
        self.assertEqual(
            result.structured_content["error"]["code"], "no_addressable_content"
        )

    def test_tombstone_reports_no_addressable_body(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_get_resource",
            {"ref": fixtures.TOMBSTONE_ID, "include_content": True},
        )
        self.assertTrue(result.is_error)
        self.assertEqual(
            result.structured_content["error"]["code"], "no_addressable_content"
        )


class TestComposeBundle(McpClientTestCase):
    def test_text_is_exactly_the_canonical_rendering(self) -> None:
        runtime, server = self.build()
        result = self.call(
            server, "pae_compose_bundle", {"refs": [fixtures.STANDARD_ID]}
        )
        expected = runtime.compiler.compile_refs(
            [fixtures.STANDARD_ID],
            budget=Budget(estimated_tokens=DEFAULT_BUNDLE_TOKENS, max_resources=25),
        ).render_markdown()
        self.assertEqual(text_of(result), expected)

    def test_structured_audit_is_body_free_but_verifiable(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_compose_bundle",
            {"refs": [fixtures.STANDARD_ID, fixtures.SAFETY_ID]},
        )
        blob = structured_blob(result)
        self.assertNotIn("A body the engine may serve whole", blob)
        self.assertNotIn("Guards are load-bearing", blob)
        for item in result.structured_content["included"]:
            self.assertNotIn("content", item)
            self.assertTrue(item["content_sha256"].startswith("sha256:"))
        self.assertTrue(result.structured_content["bundle_sha256"].startswith("sha256:"))

    def test_task_and_refs_are_mutually_exclusive(self) -> None:
        _runtime, server = self.build()
        for args in ({}, {"task": "x", "refs": [fixtures.STANDARD_ID]}):
            result = self.call(server, "pae_compose_bundle", args)
            self.assertTrue(result.is_error, args)
            self.assertEqual(result.structured_content["error"]["code"], "usage_error")

    def test_filters_are_rejected_in_refs_mode_not_ignored(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_compose_bundle",
            {"refs": [fixtures.STANDARD_ID], "kinds": ["prompt"]},
        )
        self.assertTrue(result.is_error)
        self.assertEqual(result.structured_content["error"]["code"], "usage_error")

    def test_byte_only_budget_gets_no_hidden_token_cap(self) -> None:
        _runtime, server = self.build()
        result = self.call(
            server, "pae_compose_bundle",
            {"refs": [fixtures.STANDARD_ID], "budget_bytes": 200000},
        )
        report = result.structured_content["budget"]
        self.assertIsNone(report["requested_estimated_tokens"])
        self.assertEqual(report["requested_bytes"], 200000)
        self.assertEqual(report["byte_ceiling_source"], "explicit")

    def test_absent_budgets_use_the_documented_default(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_compose_bundle", {"refs": [fixtures.STANDARD_ID]})
        report = result.structured_content["budget"]
        self.assertEqual(report["requested_estimated_tokens"], DEFAULT_BUNDLE_TOKENS)
        self.assertIsNone(report["requested_bytes"])

    def test_excluded_resource_is_refused_when_named_explicitly(self) -> None:
        _runtime, server = self.build()
        result = self.call(server, "pae_compose_bundle", {"refs": [fixtures.EXCLUDED_ID]})
        self.assertTrue(result.is_error)
        self.assertEqual(
            result.structured_content["error"]["code"], "resource_excluded"
        )


class TestTransportSafety(McpClientTestCase):
    def test_unknown_properties_cannot_redirect_the_repository(self) -> None:
        runtime, server = self.build()
        other = fixtures.standard_repo(self.tmp_path("elsewhere"))
        result = self.call(
            server, "pae_search_resources",
            {"query": "fixture", "limit": 3, "repo": str(other), "root": "/etc"},
        )
        self.assertFalse(result.is_error)
        # Still answering from the checkout the server was started against.
        self.assertTrue(runtime.repository.root.samefile(Path(str(runtime.repository.root))))
        self.assertNotIn(str(other), structured_blob(result))

    def test_schema_violations_are_rejected_before_the_handler(self) -> None:
        _runtime, server = self.build()
        for args in (
            {"query": "x", "limit": 5000},
            {"query": ""},
            {"query": "x" * 5000},
            {"query": "x", "kinds": ["not-a-kind"]},
        ):
            result = self.call(server, "pae_search_resources", args)
            self.assertTrue(result.is_error, args)

    def test_no_model_facing_output_names_the_checkout(self) -> None:
        runtime, server = self.build()
        root = str(runtime.repository.root)
        calls = [
            ("pae_search_resources", {"query": "fixture"}),
            ("pae_route_task", {"task": "fixture"}),
            ("pae_get_resource", {"ref": fixtures.STANDARD_ID, "include_content": True}),
            ("pae_get_resource", {"ref": "!!!bad!!!"}),
            ("pae_get_resource", {"ref": fixtures.EXCLUDED_ID}),
            ("pae_compose_bundle", {"refs": [fixtures.STANDARD_ID]}),
        ]
        for name, args in calls:
            result = self.call(server, name, args)
            blob = text_of(result) + structured_blob(result)
            self.assertNotIn(root, blob, f"{name} leaked the checkout root")
            self.assertNotIn("Traceback", blob, name)


class TestConcurrency(McpClientTestCase):
    def test_concurrent_cold_calls_build_the_index_once(self) -> None:
        runtime, server = self.build()
        builds: list[int] = []
        original = runtime.search._ensure_index

        def counting():
            if runtime.search._index is None:
                builds.append(1)
            return original()

        runtime.search._ensure_index = counting  # type: ignore[method-assign]

        async def burst():
            async with Client(server) as client:
                calls = []
                for i in range(8):
                    if i % 3 == 0:
                        calls.append(client.call_tool(
                            "pae_search_resources", {"query": f"fixture {i}"}))
                    elif i % 3 == 1:
                        calls.append(client.call_tool(
                            "pae_route_task", {"task": f"fixture {i}"}))
                    else:
                        calls.append(client.call_tool(
                            "pae_compose_bundle", {"task": f"fixture {i}"}))
                return await asyncio.gather(*calls, return_exceptions=True)

        results = asyncio.run(burst())
        self.assertEqual(
            [r for r in results if isinstance(r, Exception)], [], "a concurrent call raised"
        )
        self.assertEqual(len(results), 8)
        self.assertEqual(len(builds), 1, "the lexical index was built more than once")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

"""The MCP adapter's own logic, tested without the MCP SDK.

Deliberately SDK-free. ``runtime``, ``results`` and ``errors`` import nothing
but the core, so the projections, the sanitizer and the warmup lock can be
exercised in the base CI job — the one that proves the package installs with no
dependencies. Only the tool and server layers need the SDK, and those are
covered in ``test_mcp_server.py``.
"""

from __future__ import annotations

import threading
import time
import unittest
from pathlib import Path

import fixtures
from _support import EngineTestCase

from pae_engine import Budget, ContextCompiler, MissingExtra, Repository, SearchEngine
from pae_engine.errors import (
    ChecksumMismatch,
    PathSecurityError,
    RegistryValidationError,
    ResourceExcluded,
)
from pae_engine.mcp import require_sdk, sdk_available
from pae_engine.mcp.errors import (
    DETAIL_ALLOWLIST,
    INTERNAL_ERROR_MESSAGE,
    REDACTION,
    error_payload,
    scrub,
)
from pae_engine.mcp.results import (
    AUTHORITY_NOTE,
    bundle_audit,
    framed_body,
    resource_structured,
    resource_text,
    route_text,
    search_text,
)
from pae_engine.mcp.runtime import PaeRuntime

ENGINE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_ROOT.parent


class TestErrorSanitization(unittest.TestCase):
    """Nothing about the machine may reach the model."""

    def test_scrub_removes_repo_root_in_both_separator_styles(self) -> None:
        root = Path("/home/someone/checkout")
        text = "failed at /home/someone/checkout/a.md and \\home\\someone\\checkout\\b.md"
        cleaned = scrub(text, root)
        self.assertNotIn("/home/someone/checkout", cleaned)
        self.assertIn(REDACTION, cleaned)

    def test_path_security_never_names_the_resolved_target(self) -> None:
        # The escape target is outside the root by definition, so scrubbing the
        # root cannot remove it. A fixed message is the only safe answer.
        exc = PathSecurityError(
            "source path resolves outside the repository root: 'a.md' -> /etc/shadow",
            uid="pae_x", id="prompt:x", path="a.md",
            resolved="/etc/shadow", root="/home/someone/checkout",
        )
        payload = error_payload(exc, repo_root=Path("/home/someone/checkout"))
        blob = repr(payload)
        self.assertEqual(payload["error"]["code"], "source_path_refused")
        self.assertNotIn("/etc/shadow", blob)
        self.assertNotIn("/home/someone/checkout", blob)
        self.assertNotIn("resolved", payload["error"]["details"])
        self.assertNotIn("root", payload["error"]["details"])

    def test_registry_validation_drops_the_absolute_registry_path(self) -> None:
        exc = RegistryValidationError(
            "registry could not be read: /home/someone/checkout/meta/registry/registry.jsonl",
            path="/home/someone/checkout/meta/registry/registry.jsonl",
            line=12,
        )
        payload = error_payload(exc, repo_root=Path("/home/someone/checkout"))
        self.assertNotIn("path", payload["error"]["details"])
        self.assertEqual(payload["error"]["details"]["line"], 12)
        self.assertNotIn("/home/someone/checkout", payload["error"]["message"])

    def test_checksum_mismatch_keeps_only_repo_relative_identity(self) -> None:
        exc = ChecksumMismatch(
            "mismatch", uid="pae_x", id="prompt:x", path="domain/a.md",
            expected="sha256:aaa", actual="sha256:bbb",
        )
        details = error_payload(exc)["error"]["details"]
        self.assertEqual(details["path"], "domain/a.md")
        self.assertEqual(sorted(details), ["actual", "expected", "id", "path", "uid"])

    def test_excluded_returns_only_the_identity_stub(self) -> None:
        exc = ResourceExcluded(
            "excluded", ref="prompt:x", uid="pae_x", serving_policy="excluded",
            resource={
                "uid": "pae_x", "id": "prompt:x", "kind": "prompt",
                "lifecycle": "live", "serving_policy": "excluded",
                # Anything beyond the stub must be dropped even if an upstream
                # caller mistakenly puts it here.
                "title": "SECRET TITLE", "description": "SECRET DESCRIPTION",
            },
        )
        payload = error_payload(exc)
        blob = repr(payload)
        self.assertNotIn("SECRET TITLE", blob)
        self.assertNotIn("SECRET DESCRIPTION", blob)
        self.assertEqual(
            sorted(payload["error"]["details"]["resource"]),
            ["id", "kind", "lifecycle", "serving_policy", "uid"],
        )

    def test_unexpected_exception_becomes_a_fixed_message(self) -> None:
        payload = error_payload(ValueError("secret internal state /home/me/x"))
        self.assertEqual(payload["error"]["code"], "internal_error")
        self.assertEqual(payload["error"]["message"], INTERNAL_ERROR_MESSAGE)
        self.assertEqual(payload["error"]["details"], {})
        self.assertNotIn("secret internal state", repr(payload))

    def test_every_allowlist_entry_is_a_frozenset(self) -> None:
        for code, allowed in DETAIL_ALLOWLIST.items():
            self.assertIsInstance(allowed, frozenset, code)
            for banned in ("root", "resolved", "cwd", "home", "venv", "interpreter"):
                self.assertNotIn(banned, allowed, f"{code} must not expose {banned}")


class TestProjections(EngineTestCase):
    """Body-once, framing, and text that stands on its own."""

    def setUp(self) -> None:
        super().setUp()
        self.root = fixtures.standard_repo(self.tmp_path())
        self.registry = Repository.at(self.root).registry()

    def test_direct_body_is_framed_and_left_byte_identical(self) -> None:
        record = self.registry.get(fixtures.SAFETY_ID)
        content = self.registry.content(fixtures.SAFETY_ID)
        body = content.text()
        framed = framed_body(record, content, body)

        self.assertTrue(framed.startswith(AUTHORITY_NOTE))
        self.assertIn(body, framed)                      # unchanged, in full
        self.assertIn(content.content_sha256, framed)    # provenance stated
        self.assertIn("BEGIN PAE RESOURCE BODY", framed)
        self.assertIn("END PAE RESOURCE BODY", framed)
        # Guard metadata surfaced rather than silently dropped.
        self.assertIn("Guard preservation", framed)
        # No immunity claim.
        self.assertNotIn("injection", framed.lower())

    def test_marker_avoids_a_body_that_contains_it(self) -> None:
        record = self.registry.get(fixtures.STANDARD_ID)
        content = self.registry.content(fixtures.STANDARD_ID)
        digest = content.content_sha256.split(":", 1)[-1]
        # A body that already contains the shortest candidate marker.
        hostile = f"prefix PAE RESOURCE BODY {digest[:12]} suffix"
        framed = framed_body(record, content, hostile)
        self.assertIn(hostile, framed)  # body still verbatim
        begin = [ln for ln in framed.splitlines() if ln.startswith("----- BEGIN")][0]
        marker = begin[len("----- BEGIN "):-len(" -----")]
        self.assertNotIn(marker, hostile)

    def test_resource_structured_never_carries_the_body(self) -> None:
        record = self.registry.get(fixtures.STANDARD_ID)
        content = self.registry.content(fixtures.STANDARD_ID)
        obj = resource_structured(record, None, content)
        blob = repr(obj)
        self.assertNotIn("A body the engine may serve whole", blob)
        self.assertTrue(obj["content_returned"])
        self.assertEqual(obj["content_verification"]["content_sha256"], content.content_sha256)

    def test_metadata_text_explains_why_a_body_is_absent(self) -> None:
        record = self.registry.get(fixtures.METADATA_ONLY_ID)
        text = resource_text(record)
        self.assertIn("metadata_only", text)
        self.assertIn("withheld", text.lower())
        self.assertNotIn("This body must never be served", text)

    def test_bundle_audit_drops_bodies_and_keeps_everything_else(self) -> None:
        compiler = ContextCompiler(self.registry)
        bundle = compiler.compile_refs(
            [fixtures.STANDARD_ID, fixtures.SAFETY_ID], budget=Budget(estimated_tokens=8000)
        )
        audit = bundle_audit(bundle)
        blob = repr(audit)

        self.assertNotIn("A body the engine may serve whole", blob)
        self.assertNotIn("Guards are load-bearing", blob)
        for item in audit["included"]:
            self.assertNotIn("content", item)
            self.assertIn("content_sha256", item)
            self.assertIn("byte_length", item)
        self.assertEqual(audit["bundle_sha256"], bundle.bundle_sha256)
        self.assertIn("budget", audit)
        self.assertIn("omitted", audit)
        self.assertIn("ordering", audit)

    def test_bundle_audit_does_not_mutate_the_bundle(self) -> None:
        compiler = ContextCompiler(self.registry)
        bundle = compiler.compile_refs([fixtures.STANDARD_ID], budget=Budget(estimated_tokens=8000))
        before = bundle.render_markdown()
        bundle_audit(bundle)
        self.assertEqual(bundle.render_markdown(), before)
        self.assertTrue(bundle.included[0].content)

    def test_search_and_route_text_stand_alone(self) -> None:
        search = SearchEngine(self.registry)
        results = search.search("fixture", limit=5)
        text = search_text(results)
        self.assertIn("Search:", text)
        self.assertIn("Matches:", text)

        from pae_engine import Router

        decision = Router(search).route("fixture resource")
        rtext = route_text(decision)
        self.assertIn("Route status:", rtext)
        self.assertIn("Coverage:", rtext)
        # Coverage and margin are never described as confidence.
        self.assertIn("not confidence scores", rtext)
        if decision.status != "matched":
            self.assertIn("No route selected", rtext)


class TestWarmupLock(EngineTestCase):
    """The Phase 6A thundering herd must be impossible."""

    def test_concurrent_cold_callers_build_the_index_exactly_once(self) -> None:
        root = fixtures.standard_repo(self.tmp_path())
        runtime = PaeRuntime(Repository.at(root))

        builds: list[int] = []
        original = runtime.search._ensure_index

        def slow_build():
            # A real build takes ~1 s on the production corpus; the fixture
            # corpus is instant, so the race is made observable rather than
            # left to chance.
            if runtime.search._index is None:
                builds.append(1)
                time.sleep(0.05)
            return original()

        runtime.search._ensure_index = slow_build  # type: ignore[method-assign]

        errors: list[BaseException] = []

        def worker() -> None:
            try:
                runtime.ensure_search_warm()
            except BaseException as exc:  # noqa: BLE001
                errors.append(exc)

        threads = [threading.Thread(target=worker) for _ in range(8)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=30)

        self.assertEqual(errors, [])
        self.assertEqual(len(builds), 1, "the lexical index was built more than once")
        self.assertTrue(runtime.index_built)

    def test_background_warmup_starts_once_and_completes(self) -> None:
        root = fixtures.standard_repo(self.tmp_path())
        runtime = PaeRuntime(Repository.at(root))
        self.assertFalse(runtime.index_built)
        runtime.start_background_warmup()
        runtime.start_background_warmup()  # idempotent
        runtime.join_warmup(timeout=30)
        self.assertTrue(runtime.index_built)

    def test_runtime_construction_reads_nothing(self) -> None:
        root = fixtures.standard_repo(self.tmp_path())
        runtime = PaeRuntime(Repository.at(root))
        self.assertFalse(runtime.index_built)


class TestOptionalExtraContract(unittest.TestCase):
    """The adapter's front door must work whether or not the SDK is installed."""

    def test_sdk_probe_matches_require(self) -> None:
        if sdk_available():
            require_sdk()  # must not raise
        else:
            with self.assertRaises(MissingExtra) as caught:
                require_sdk()
            self.assertIn("prompt-agent-engineering[mcp]", caught.exception.details["install"])
            self.assertEqual(caught.exception.exit_code, 2)

    def test_importing_the_adapter_package_needs_no_sdk(self) -> None:
        # Reaching this line at all proves it: this module imported
        # pae_engine.mcp at the top, and the base CI job has no SDK.
        import pae_engine.mcp as adapter

        self.assertEqual(adapter.EXTRA_NAME, "mcp")


class TestCoreStaysIndependent(unittest.TestCase):
    """The base Engine must not learn that MCP exists."""

    CORE = (
        "repository.py", "registry.py", "search.py", "routing.py",
        "context.py", "models.py", "_lexical.py", "_context_render.py",
        "validate.py", "errors.py", "__init__.py",
    )
    BANNED = ("import mcp", "from mcp", "import pydantic", "from pydantic",
              "import jsonschema", "import starlette", "import anyio")

    def test_core_modules_import_no_third_party_or_adapter_code(self) -> None:
        src = ENGINE_ROOT / "src" / "pae_engine"
        for name in self.CORE:
            text = (src / name).read_text(encoding="utf-8")
            for banned in self.BANNED:
                self.assertNotIn(banned, text, f"{name} must not contain {banned!r}")
            self.assertNotIn("from .mcp", text, f"{name} must not import the adapter")

    def test_importing_pae_engine_does_not_load_the_sdk(self) -> None:
        import subprocess
        import sys

        code = (
            "import sys, pae_engine; "
            "assert 'mcp' not in sys.modules, sorted(m for m in sys.modules if 'mcp' in m); "
            "print('clean')"
        )
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True,
            env={**__import__("os").environ, "PYTHONPATH": str(ENGINE_ROOT / "src")},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("clean", result.stdout)


class TestMcpCommandWithoutExtra(EngineTestCase):
    """`pae mcp` on a base install is a clean usage error, not a traceback."""

    def test_help_works_and_writes_nothing_to_stderr_path(self) -> None:
        result = self.run_cli(["mcp", "--help"])
        self.assertEqual(result.code, 0)
        self.assertIn("stdio", result.stdout)

    @unittest.skipIf(sdk_available(), "the MCP extra is installed in this environment")
    def test_missing_extra_exits_two_with_an_install_hint_on_stderr(self) -> None:
        root = fixtures.standard_repo(self.tmp_path())
        result = self.run_cli(["mcp", "--repo", str(root)])
        self.assertEqual(result.code, 2)
        self.assertTrue(result.stdout_empty, "stdout must stay clean")
        self.assertIn("missing_extra", result.stderr)
        self.assertIn("prompt-agent-engineering[mcp]", result.stderr)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

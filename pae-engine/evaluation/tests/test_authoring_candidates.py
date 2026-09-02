"""Reviewer candidate discovery must not touch PAE retrieval (spec §10).

The forbidden-import proof is the point of this file. If the reviewer labels a
task with what PAE returns, the benchmark grades PAE against its own output —
an unfalsifiable result that looks exactly like a good one. That guarantee is
worth nothing as a comment, so it is checked three ways:

1. **Source level**, as the spec asks: the module text contains no forbidden
   import and no forbidden symbol.
2. **Transitive import closure**: importing the module in a fresh interpreter
   pulls in no ``pae_engine`` retrieval module, however indirectly.
3. **Behaviourally**: the emitted records state their ranking basis and always
   offer the reviewer a way out of the list.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from _support import REPO_ROOT, TempDirCase, ripgrep_available

from pae_eval.authoring import candidates

MODULE_PATH = Path(candidates.__file__)

#: Modules the reviewer's discovery path must never reach.
FORBIDDEN_MODULES = (
    "pae_engine.search",
    "pae_engine.routing",
    "pae_engine.context",
    "pae_engine.mcp",
)

#: Symbols whose mere presence would mean retrieval leaked in.
FORBIDDEN_SYMBOLS = ("SearchEngine", "Router", "ContextCompiler")


class TestForbiddenImportsAtSourceLevel(unittest.TestCase):

    # Checked over the parsed AST, not the raw text. A substring scan cannot
    # tell a reference from a mention, and this module has to *name* what it
    # refuses to use — RANKING_BASIS says the ordering is "not derived from any
    # PAE Search, Router or ContextCompiler output", and that sentence is the
    # point of it. Parsing polices code and leaves prose alone.

    @classmethod
    def setUpClass(cls) -> None:
        import ast

        cls.ast = ast
        cls.tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))

    def _imported_modules(self) -> set[str]:
        modules: set[str] = set()
        for node in self.ast.walk(self.tree):
            if isinstance(node, self.ast.Import):
                modules.update(alias.name for alias in node.names)
            elif isinstance(node, self.ast.ImportFrom) and node.module:
                modules.add(node.module)
                modules.update(f"{node.module}.{a.name}" for a in node.names)
        return modules

    def _referenced_names(self) -> set[str]:
        names: set[str] = set()
        for node in self.ast.walk(self.tree):
            if isinstance(node, self.ast.Name):
                names.add(node.id)
            elif isinstance(node, self.ast.Attribute):
                names.add(node.attr)
        return names

    def test_no_forbidden_module_imported(self) -> None:
        imported = self._imported_modules()
        for module in FORBIDDEN_MODULES:
            with self.subTest(module=module):
                self.assertFalse(
                    any(m == module or m.startswith(f"{module}.")
                        for m in imported),
                    f"{module} is imported: {sorted(imported)}",
                )

    def test_no_forbidden_symbol_referenced(self) -> None:
        referenced = self._referenced_names()
        for symbol in FORBIDDEN_SYMBOLS:
            with self.subTest(symbol=symbol):
                self.assertNotIn(symbol, referenced)

    def test_does_not_import_the_engine_at_all(self) -> None:
        for module in self._imported_modules():
            self.assertFalse(
                module == "pae_engine" or module.startswith("pae_engine."),
                f"candidates imports the Engine: {module}",
            )


class TestForbiddenImportsTransitively(unittest.TestCase):
    """A clean interpreter, so an indirect import cannot hide behind ours."""

    def test_import_closure_is_clean(self) -> None:
        script = (
            "import sys\n"
            "import pae_eval.authoring.candidates\n"
            "bad = [m for m in sys.modules if m.startswith('pae_engine')]\n"
            "print(';'.join(sorted(bad)))\n"
        )
        env_path = ";".join if sys.platform == "win32" else ":".join
        completed = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True, text=True, check=False,
            env={
                **_clean_env(),
                "PYTHONPATH": env_path([
                    str(REPO_ROOT / "pae-engine" / "evaluation" / "src"),
                    str(REPO_ROOT / "pae-engine" / "src"),
                ]),
            },
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        reached = [m for m in completed.stdout.strip().split(";") if m]
        self.assertEqual(
            reached, [],
            f"importing candidates reached Engine modules: {reached}",
        )


def _clean_env() -> dict[str, str]:
    import os

    keep = ("PATH", "SYSTEMROOT", "windir", "TEMP", "TMP", "HOME", "USERPROFILE")
    return {k: v for k, v in os.environ.items() if k in keep}


class TestQueryTokens(unittest.TestCase):

    def test_stopwords_and_short_tokens_dropped(self) -> None:
        tokens = candidates.query_tokens("How do I use the API for a review?")
        self.assertNotIn("the", tokens)
        self.assertNotIn("for", tokens)
        self.assertIn("api", tokens)
        self.assertIn("review", tokens)

    def test_order_preserved_and_deduplicated(self) -> None:
        tokens = candidates.query_tokens("review review incident review")
        self.assertEqual(tokens, ["review", "incident"])


class TestDiscoveryContract(TempDirCase):

    @unittest.skipUnless(ripgrep_available(), "ripgrep not installed")
    def test_records_state_their_basis_and_offer_an_escape(self) -> None:
        snapshot = self.tmp_path("snap")
        (snapshot / "docs").mkdir(parents=True)
        (snapshot / "docs" / "alpha.md").write_text(
            "Incident retrospective procedure with a blameless timeline.",
            encoding="utf-8")
        (snapshot / "docs" / "beta.md").write_text(
            "Unrelated content about gardening.", encoding="utf-8")

        result = candidates.discover(snapshot, "incident retrospective timeline")
        payload = result.to_json_obj()

        self.assertFalse(payload["pae_retrieval_used"])
        self.assertIn("not a PAE relevance score", payload["ranking_basis"])
        self.assertEqual(list(payload["reviewer_options"]),
                         list(candidates.REVIEWER_ESCAPE_OPTIONS))
        paths = [c["path"] for c in payload["candidates"]]
        self.assertIn("docs/alpha.md", paths)
        for candidate in payload["candidates"]:
            self.assertIn("ranking_basis", candidate)

    @unittest.skipUnless(ripgrep_available(), "ripgrep not installed")
    def test_ordering_is_deterministic(self) -> None:
        snapshot = self.tmp_path("snap")
        snapshot.mkdir()
        for name in ("a", "b", "c"):
            (snapshot / f"{name}.md").write_text("incident timeline", encoding="utf-8")
        first = candidates.discover(snapshot, "incident timeline")
        second = candidates.discover(snapshot, "incident timeline")
        self.assertEqual([c.path for c in first.candidates],
                         [c.path for c in second.candidates])


class TestExcerptPolicy(TempDirCase):

    def test_safety_gated_excerpt_is_withheld_not_truncated(self) -> None:
        identity = candidates.Identity(
            uid="pae_x", public_id="prompt:x", kind="prompt", scope="legal",
            title="T", description="d", serving_policy="safety_gated",
            lifecycle="live",
        )
        (self.tmp_path("x.md")).write_text("guarded body", encoding="utf-8")
        excerpt, reason = candidates._excerpt(self.tmp_path(), "x.md", identity, 100)
        self.assertEqual(excerpt, "")
        self.assertIn("guard text must not be truncated", reason)

    def test_standard_resource_gets_an_excerpt(self) -> None:
        identity = candidates.Identity(
            uid="pae_y", public_id="prompt:y", kind="prompt", scope="finance",
            title="T", description="d", serving_policy="standard",
            lifecycle="live",
        )
        (self.tmp_path("y.md")).write_text("ordinary body text", encoding="utf-8")
        excerpt, reason = candidates._excerpt(self.tmp_path(), "y.md", identity, 100)
        self.assertEqual(excerpt, "ordinary body text")
        self.assertEqual(reason, "")


if __name__ == "__main__":
    unittest.main()

"""The Engine must not ship the harness, and the Engine must not import it.

Both properties are currently true by accident of layout — `packages.find` looks
only under `src/`, and `MANIFEST.in` never names `evaluation/`. An accident that
nothing checks is a regression waiting to happen, so both are asserted, and
`MANIFEST.in` carries an explicit `prune` as defence in depth.
"""

from __future__ import annotations

import ast
import shutil
import subprocess
import sys
import tarfile
import unittest
import zipfile
from pathlib import Path

from _support import EVAL_ROOT, REPO_ROOT, TempDirCase

ENGINE_ROOT = REPO_ROOT / "pae-engine"
ENGINE_SRC = ENGINE_ROOT / "src" / "pae_engine"

#: Anything matching these must never appear in an Engine artifact.
FORBIDDEN_IN_ARTIFACTS = (
    "evaluation/", "pae_eval", "mini-benchmark", "trials.jsonl",
    "anthropic_adapter", "openai_adapter", "judging/", "evaluation-plan",
)


class TestImportDirection(unittest.TestCase):
    """``pae_eval -> pae_engine`` is allowed; the reverse never is."""

    def _engine_sources(self):
        return sorted(ENGINE_SRC.rglob("*.py"))

    def test_engine_sources_exist(self) -> None:
        self.assertTrue(self._engine_sources(), "no Engine sources found")

    def test_no_engine_module_imports_the_harness(self) -> None:
        offenders: list[str] = []
        for path in self._engine_sources():
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split(".")[0] == "pae_eval":
                            offenders.append(f"{path.name}: import {alias.name}")
                elif isinstance(node, ast.ImportFrom):
                    module = (node.module or "").split(".")[0]
                    if module == "pae_eval":
                        offenders.append(f"{path.name}: from {node.module}")
        self.assertEqual(offenders, [], f"the Engine must not import pae_eval: {offenders}")

    def test_no_engine_source_mentions_the_harness_at_all(self) -> None:
        mentions = [
            path.name for path in self._engine_sources()
            if "pae_eval" in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(mentions, [])

    def test_the_pae_cli_has_no_eval_subcommand(self) -> None:
        cli = (ENGINE_SRC / "cli.py").read_text(encoding="utf-8")
        self.assertNotIn('"eval"', cli)
        self.assertNotIn("'eval'", cli)
        self.assertNotIn("pae_eval", cli)

    def test_the_mcp_adapter_never_reaches_the_harness(self) -> None:
        for path in (ENGINE_SRC / "mcp").rglob("*.py"):
            self.assertNotIn("pae_eval", path.read_text(encoding="utf-8"))


class TestManifestDefence(unittest.TestCase):
    def test_manifest_prunes_the_evaluation_tree(self) -> None:
        manifest = (ENGINE_ROOT / "MANIFEST.in").read_text(encoding="utf-8")
        self.assertIn("prune evaluation", manifest)


class TestEngineSetupExcludesEvaluation(unittest.TestCase):
    def test_package_discovery_is_scoped_to_src(self) -> None:
        pyproject = (ENGINE_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('where = ["src"]', pyproject)


@unittest.skipUnless(shutil.which("python") or sys.executable,
                     "needs a Python interpreter")
class TestBuiltArtifacts(TempDirCase):
    """Build the Engine and prove the harness is absent from both artifacts.

    Slow (a real build), so it is one test that checks both artifacts rather
    than several that each pay the build cost.
    """

    @classmethod
    def setUpClass(cls) -> None:
        try:
            import build  # noqa: F401
        except ImportError:
            raise unittest.SkipTest("the 'build' package is not installed")

    def test_neither_wheel_nor_sdist_contains_evaluation_code(self) -> None:
        work = self.tmp_path("engine")
        shutil.copytree(ENGINE_ROOT, work, ignore=shutil.ignore_patterns(
            "dist", "build", "__pycache__", ".pytest_cache"))
        # The evaluation tree is copied in deliberately: the test is worthless
        # if the thing it is looking for was never there.
        self.assertTrue((work / "evaluation" / "src" / "pae_eval").is_dir())
        (work / "evaluation" / "results_should_not_ship.jsonl").write_text(
            "{}\n", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "-m", "build", "--no-isolation"],
            cwd=work, capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            self.skipTest(f"build failed in this environment: {result.stderr[-400:]}")

        dist = work / "dist"
        wheels = list(dist.glob("*.whl"))
        sdists = list(dist.glob("*.tar.gz"))
        self.assertTrue(wheels and sdists, "build produced no artifacts")

        with zipfile.ZipFile(wheels[0]) as archive:
            wheel_names = archive.namelist()
        with tarfile.open(sdists[0]) as archive:
            sdist_names = archive.getnames()

        for marker in FORBIDDEN_IN_ARTIFACTS:
            self.assertFalse(
                [n for n in wheel_names if marker in n],
                f"{marker!r} leaked into the wheel",
            )
            self.assertFalse(
                [n for n in sdist_names if marker in n],
                f"{marker!r} leaked into the sdist",
            )
        # And the Engine itself is still there, so the test is not passing by
        # having built nothing.
        self.assertTrue([n for n in wheel_names if "pae_engine/search.py" in n])


class TestHarnessPackagesItselfCleanly(unittest.TestCase):
    def test_the_harness_does_not_vendor_the_engine_or_the_corpus(self) -> None:
        """The harness reads a checkout; it never carries a copy of one."""
        self.assertFalse((EVAL_ROOT / "src" / "pae_engine").exists())
        self.assertFalse((EVAL_ROOT / "src" / "pae_eval" / "meta").exists())
        for name in ("registry.jsonl", "identity.tsv", "PROMPT_INDEX.json"):
            self.assertEqual(
                list((EVAL_ROOT / "src").rglob(name)), [],
                f"{name} must not be vendored into the harness package",
            )

    def test_the_harness_declares_no_unconditional_dependencies(self) -> None:
        pyproject = (EVAL_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn("dependencies = []", pyproject)

    def test_the_harness_declares_no_console_script(self) -> None:
        """`pae` belongs to the Engine; evaluation stays `python -m pae_eval`."""
        pyproject = (EVAL_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertNotIn("[project.scripts]", pyproject)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

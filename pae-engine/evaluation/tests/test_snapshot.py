"""The participant snapshot: what it must contain, and what it must never.

The exclusion is the point. Once `pae-engine/evaluation/` is committed, a
raw-repository agent pointed at the developer checkout could read the condition
definitions, the participant prompt and the judge logic. Excluding too much is
equally wrong: a snapshot without the registry is not the product, and every
condition would be measuring an empty repository.
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

from _support import REPO_ROOT, TempDirCase, engine_available, git_repo_available

from pae_eval.errors import IsolationError, UsageError
from pae_eval.snapshot import (
    SNAPSHOT_EXCLUDED_PREFIXES,
    Snapshot,
    SnapshotFile,
    assert_no_evaluation_infrastructure,
    assert_product_present,
    build_snapshot,
    is_excluded,
    resolve_commit,
    write_manifest,
)


class TestExclusionRule(unittest.TestCase):
    def test_evaluation_tree_is_excluded(self) -> None:
        self.assertTrue(is_excluded("pae-engine/evaluation/src/pae_eval/cli.py",
                                    SNAPSHOT_EXCLUDED_PREFIXES))

    def test_evaluation_runs_are_excluded(self) -> None:
        self.assertTrue(is_excluded("evaluation-runs/trials.jsonl",
                                    SNAPSHOT_EXCLUDED_PREFIXES))

    def test_the_engine_runtime_is_not_excluded(self) -> None:
        self.assertFalse(is_excluded("pae-engine/src/pae_engine/search.py",
                                     SNAPSHOT_EXCLUDED_PREFIXES))

    def test_the_registry_is_not_excluded(self) -> None:
        self.assertFalse(is_excluded("meta/registry/registry.jsonl",
                                     SNAPSHOT_EXCLUDED_PREFIXES))

    def test_agent_docs_are_not_excluded(self) -> None:
        for path in ("CLAUDE.md", "AGENTS.md", "START_HERE_FOR_AI.md"):
            self.assertFalse(is_excluded(path, SNAPSHOT_EXCLUDED_PREFIXES))

    def test_a_similarly_named_path_is_not_over_excluded(self) -> None:
        """'evaluation-guide.md' is not the evaluation tree."""
        self.assertFalse(is_excluded("domain-AI-ML/evaluation-guide.md",
                                     SNAPSHOT_EXCLUDED_PREFIXES))


class TestAssertions(unittest.TestCase):
    def _snapshot(self, paths) -> Snapshot:
        return Snapshot(
            root=Path("."), commit="abc", excluded_prefixes=(), excluded_count=0,
            aggregate_sha256="sha256:x",
            files=tuple(SnapshotFile(p, "sha256:y", 1, False) for p in paths),
        )

    def test_leaked_evaluation_code_is_caught(self) -> None:
        snapshot = self._snapshot(["pae-engine/evaluation/src/pae_eval/cli.py"])
        with self.assertRaises(IsolationError):
            assert_no_evaluation_infrastructure(snapshot)

    def test_a_clean_snapshot_passes(self) -> None:
        assert_no_evaluation_infrastructure(
            self._snapshot(["pae-engine/src/pae_engine/search.py"]))

    def test_missing_registry_is_caught(self) -> None:
        snapshot = self._snapshot(["CLAUDE.md", "domain-x/a.md"])
        with self.assertRaises(IsolationError) as caught:
            assert_product_present(snapshot)
        self.assertIn("registry", str(caught.exception))

    def test_missing_corpus_is_caught(self) -> None:
        snapshot = self._snapshot([
            "meta/registry/registry.jsonl", "meta/registry/identity.tsv",
            "pae-engine/src/pae_engine/__init__.py", "CLAUDE.md",
        ])
        with self.assertRaises(IsolationError) as caught:
            assert_product_present(snapshot)
        self.assertIn("corpus", str(caught.exception))


class TestBuildFromGit(TempDirCase):
    """Extraction comes from Git objects, so a dirty file cannot leak in."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = self.tmp_path("repo")
        self.repo.mkdir(parents=True, exist_ok=True)
        self._git("init", "-q")
        self._git("config", "user.email", "t@example.com")
        self._git("config", "user.name", "t")
        (self.repo / "CLAUDE.md").write_text("guide\n", encoding="utf-8")
        (self.repo / "meta" / "registry").mkdir(parents=True, exist_ok=True)
        (self.repo / "meta" / "registry" / "registry.jsonl").write_text(
            "{}\n", encoding="utf-8")
        (self.repo / "meta" / "registry" / "identity.tsv").write_text(
            "uid\n", encoding="utf-8")
        (self.repo / "pae-engine" / "src" / "pae_engine").mkdir(
            parents=True, exist_ok=True)
        (self.repo / "pae-engine" / "src" / "pae_engine" / "__init__.py").write_text(
            "", encoding="utf-8")
        (self.repo / "domain-x").mkdir(parents=True, exist_ok=True)
        (self.repo / "domain-x" / "a.md").write_text("corpus\n", encoding="utf-8")
        evaluation = self.repo / "pae-engine" / "evaluation" / "src" / "pae_eval"
        evaluation.mkdir(parents=True, exist_ok=True)
        (evaluation / "cli.py").write_text("SECRET HARNESS\n", encoding="utf-8")
        self._git("add", "-A")
        self._git("commit", "-q", "-m", "initial")

    def _git(self, *args: str) -> str:
        result = subprocess.run(["git", "-C", str(self.repo), *args],
                                capture_output=True, text=True, check=False)
        return result.stdout

    def test_evaluation_tree_never_reaches_the_snapshot(self) -> None:
        dest = self.tmp_path("snap")
        snapshot = build_snapshot(self.repo, dest)
        paths = {f.path for f in snapshot.files}
        self.assertNotIn("pae-engine/evaluation/src/pae_eval/cli.py", paths)
        self.assertEqual(snapshot.excluded_count, 1)
        self.assertFalse((dest / "pae-engine" / "evaluation").exists())
        assert_no_evaluation_infrastructure(snapshot)
        assert_product_present(snapshot)

    def test_product_files_do_reach_the_snapshot(self) -> None:
        snapshot = build_snapshot(self.repo, self.tmp_path("snap2"))
        paths = {f.path for f in snapshot.files}
        for expected in ("CLAUDE.md", "meta/registry/registry.jsonl",
                         "domain-x/a.md",
                         "pae-engine/src/pae_engine/__init__.py"):
            self.assertIn(expected, paths)

    def test_uncommitted_changes_cannot_enter(self) -> None:
        (self.repo / "domain-x" / "a.md").write_text(
            "DIRTY EDIT\n", encoding="utf-8")
        (self.repo / "domain-x" / "untracked.md").write_text(
            "UNTRACKED\n", encoding="utf-8")
        dest = self.tmp_path("snap3")
        snapshot = build_snapshot(self.repo, dest)
        self.assertEqual((dest / "domain-x" / "a.md").read_text(encoding="utf-8"),
                         "corpus\n")
        self.assertNotIn("domain-x/untracked.md", {f.path for f in snapshot.files})

    def test_sealed_mode_refuses_a_dirty_checkout(self) -> None:
        (self.repo / "domain-x" / "a.md").write_text("DIRTY\n", encoding="utf-8")
        with self.assertRaises(IsolationError):
            build_snapshot(self.repo, self.tmp_path("snap4"), require_clean=True)

    def test_the_aggregate_hash_is_path_independent(self) -> None:
        """Two builds of one commit must agree, wherever they were built."""
        a = build_snapshot(self.repo, self.tmp_path("snapA"))
        b = build_snapshot(self.repo, self.tmp_path("snapB"))
        self.assertEqual(a.aggregate_sha256, b.aggregate_sha256)
        self.assertNotEqual(str(a.root), str(b.root))

    def test_manifest_contains_no_absolute_path(self) -> None:
        snapshot = build_snapshot(self.repo, self.tmp_path("snap5"))
        destination = self.tmp_path("participant-snapshot.json")
        write_manifest(snapshot, destination)
        text = destination.read_text(encoding="utf-8")
        self.assertNotIn(str(self.repo), text)
        self.assertNotIn(str(snapshot.root), text)

    def test_a_non_empty_destination_is_refused(self) -> None:
        dest = self.tmp_path("snap6")
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "leftover.txt").write_text("x", encoding="utf-8")
        with self.assertRaises(UsageError):
            build_snapshot(self.repo, dest)


@unittest.skipUnless(git_repo_available() and engine_available(),
                     "needs the real checkout and the Engine")
class TestAgainstTheRealRepository(TempDirCase):
    def test_the_engine_accepts_the_snapshot_as_a_checkout(self) -> None:
        from pae_engine import Registry, Repository

        snapshot = build_snapshot(REPO_ROOT, self.tmp_path("snap"))
        assert_no_evaluation_infrastructure(snapshot)
        assert_product_present(snapshot)
        registry = Registry.open(Repository.at(snapshot.root))
        self.assertIsNotNone(registry)

    def test_commit_resolution(self) -> None:
        commit = resolve_commit(REPO_ROOT)
        self.assertEqual(len(commit), 40)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

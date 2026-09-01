"""Repository discovery: precedence, marker detection, incompatible schemas."""

from __future__ import annotations

import json
import unittest

from _support import EngineTestCase
from fixtures import SUMMARY_RELPATH, standard_repo

from pae_engine import IncompatibleRegistry, RepositoryNotFound, Repository
from pae_engine.repository import (
    DISCOVERY_ANCESTOR,
    DISCOVERY_ENVIRONMENT,
    DISCOVERY_EXPLICIT,
    REPO_ENV_VAR,
)


class TestDiscoveryPrecedence(EngineTestCase):
    def test_explicit_path_resolves(self) -> None:
        root = standard_repo(self.tmp_path())
        repo = Repository.discover(root)
        self.assertEqual(repo.root, root.resolve())
        self.assertEqual(repo.discovery_source, DISCOVERY_EXPLICIT)

    def test_environment_variable_resolves(self) -> None:
        root = standard_repo(self.tmp_path())
        elsewhere = self.tmp_path("elsewhere")
        repo = Repository.discover(env={REPO_ENV_VAR: str(root)}, cwd=elsewhere)
        self.assertEqual(repo.root, root.resolve())
        self.assertEqual(repo.discovery_source, DISCOVERY_ENVIRONMENT)

    def test_ancestor_walk_finds_the_root(self) -> None:
        root = standard_repo(self.tmp_path())
        deep = root / "domain-x" / "sub" / "deeper"
        deep.mkdir(parents=True)
        repo = Repository.discover(env={}, cwd=deep)
        self.assertEqual(repo.root, root.resolve())
        self.assertEqual(repo.discovery_source, DISCOVERY_ANCESTOR)
        self.assertEqual(repo.search_start, deep.resolve())

    def test_no_repository_anywhere(self) -> None:
        empty = self.tmp_path("empty")
        with self.assertRaises(RepositoryNotFound) as ctx:
            Repository.discover(env={}, cwd=empty)
        self.assertEqual(ctx.exception.exit_code, 3)

    def test_explicit_invalid_path_does_not_fall_through(self) -> None:
        """A named checkout that holds no registry is an error, not a hint.

        Falling back to the environment or the working directory here would let
        an agent believe it had queried the checkout it named.
        """
        good = standard_repo(self.tmp_path("good"))
        bad = self.tmp_path("bad")
        with self.assertRaises(RepositoryNotFound):
            Repository.discover(bad, env={REPO_ENV_VAR: str(good)}, cwd=good)

    def test_environment_invalid_path_does_not_fall_through(self) -> None:
        good = standard_repo(self.tmp_path("good"))
        bad = self.tmp_path("bad")
        with self.assertRaises(RepositoryNotFound):
            Repository.discover(env={REPO_ENV_VAR: str(bad)}, cwd=good)

    def test_partial_marker_is_not_a_root(self) -> None:
        root = standard_repo(self.tmp_path())
        (root / SUMMARY_RELPATH).unlink()
        with self.assertRaises(RepositoryNotFound):
            Repository.at(root)


class TestIncompatibleSchema(EngineTestCase):
    def _make_incompatible(self, name: str = "repo") -> "object":
        root = standard_repo(self.tmp_path(name))
        summary = json.loads((root / SUMMARY_RELPATH).read_text(encoding="utf-8"))
        summary["schema"] = "pae-registry-summary/2"
        (root / SUMMARY_RELPATH).write_text(json.dumps(summary), encoding="utf-8")
        return root

    def test_explicit_incompatible_registry_is_not_not_found(self) -> None:
        root = self._make_incompatible()
        with self.assertRaises(IncompatibleRegistry) as ctx:
            Repository.at(root)
        self.assertEqual(ctx.exception.exit_code, 8)
        self.assertEqual(ctx.exception.details["declared_schema"], "pae-registry-summary/2")

    def test_ancestor_walk_stops_at_an_incompatible_root(self) -> None:
        """The walk must not step over a PAE root it cannot serve.

        Continuing upward could silently answer from a different checkout than
        the one the caller is standing in.
        """
        outer = standard_repo(self.tmp_path("outer"))
        inner = self._make_incompatible("outer/nested")
        deep = inner / "a" / "b"
        deep.mkdir(parents=True)
        with self.assertRaises(IncompatibleRegistry):
            Repository.discover(env={}, cwd=deep)
        self.assertTrue(outer.exists())

    def test_unparsable_summary_is_incompatible_not_missing(self) -> None:
        root = standard_repo(self.tmp_path())
        (root / SUMMARY_RELPATH).write_text("{not json", encoding="utf-8")
        with self.assertRaises(IncompatibleRegistry):
            Repository.at(root)


class TestCliDiscovery(EngineTestCase):
    def test_where_reports_source_and_root(self) -> None:
        root = standard_repo(self.tmp_path())
        result = self.run_cli(["where", "--repo", str(root), "--json"])
        self.assertEqual(result.code, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["root"], str(root.resolve()))
        self.assertEqual(payload["discovery_source"], "explicit")

    def test_where_reads_no_registry_records(self) -> None:
        """``where`` must stay cheap even against a corrupt registry."""
        root = standard_repo(self.tmp_path())
        (root / "meta/registry/registry.jsonl").write_text("{ broken\n", encoding="utf-8")
        result = self.run_cli(["where", "--repo", str(root)])
        self.assertEqual(result.code, 0)

    def test_missing_repository_exits_3(self) -> None:
        empty = self.tmp_path("empty")
        result = self.run_cli(["where", "--repo", str(empty), "--json"])
        self.assertFails(result, 3)
        self.assertEqual(json.loads(result.stderr)["error"], "repository_not_found")

    def test_incompatible_registry_exits_8(self) -> None:
        root = standard_repo(self.tmp_path())
        summary = json.loads((root / SUMMARY_RELPATH).read_text(encoding="utf-8"))
        summary["schema"] = "pae-registry-summary/9"
        (root / SUMMARY_RELPATH).write_text(json.dumps(summary), encoding="utf-8")
        result = self.run_cli(["where", "--repo", str(root), "--json"])
        self.assertFails(result, 8)
        self.assertEqual(json.loads(result.stderr)["error"], "incompatible_registry")


if __name__ == "__main__":
    unittest.main()

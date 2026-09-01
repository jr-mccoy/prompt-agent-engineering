"""Search and routing against the repository's own registry.

Two jobs. First, the security boundary: search and routing must never reach for
a resource body, and the only way to prove that is to make reaching for one
fail loudly. Second, regression floors — conservative internal guards, not
public benchmark claims, and deliberately set below the measured numbers so a
one-query wobble does not turn CI red.

Skipped when there is no checkout alongside the engine, which is exactly the
situation the packaging smoke tests exercise separately.
"""

from __future__ import annotations

import json
import statistics
import time
import unittest
from pathlib import Path

from pae_engine import Registry, Repository, RepositoryNotFound, Router, SearchEngine

import run_search_routing_diagnostics as diagnostics

ENGINE_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_ROOT.parent

#: Conservative floors. The measured values sit above every one of these; the
#: gap is deliberate headroom so an ordinary corpus edit cannot fail the build.
FLOORS = {
    "task_r@1": 0.65,
    "r@1": 0.72,
    "r@5": 0.84,
    "scope@1": 0.80,
    "kind@1": 0.93,
}
MAX_FALSE_CONFIDENT = 1


def _repository():
    try:
        return Repository.at(REPO_ROOT)
    except (RepositoryNotFound, OSError):
        return None


class RealRegistryCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        repository = _repository()
        if repository is None:
            raise unittest.SkipTest("no PAE checkout alongside the engine")
        cls.registry = Registry.open(repository)
        cls.engine = SearchEngine(cls.registry)
        cls.router = Router(cls.engine)
        cls.cases = json.loads(
            (Path(__file__).parent / "data" / "search_routing_regression.v1.json").read_text(
                encoding="utf-8"
            )
        )["cases"]


class TestNoBodyIsEverRead(RealRegistryCase):
    """The load-bearing safety property of this whole phase."""

    def _forbid_content(self):
        original = Registry.content

        def refuse(self, ref):  # noqa: ANN001 - patched method
            raise AssertionError(
                f"search/routing called Registry.content({ref!r}); relevance must "
                "never depend on a resource body"
            )

        Registry.content = refuse
        self.addCleanup(setattr, Registry, "content", original)

    def test_searching_never_reads_a_body(self) -> None:
        self._forbid_content()
        engine = SearchEngine(Registry.open(_repository()))
        for query in (
            "android security audit",
            "write a sermon on this passage",
            "prompt:software-engineering/api/api-rest-design-review",
            "technique:ST-01",
            "zzzzqqq wobblegonk",
        ):
            engine.search(query, limit=25)

    def test_routing_never_reads_a_body(self) -> None:
        self._forbid_content()
        router = Router(SearchEngine(Registry.open(_repository())))
        for task in (
            "my model drifted in production",
            "help me negotiate a raise",
            "zzzzqqq wobblegonk",
        ):
            router.route(task)

    def test_no_hit_or_route_payload_carries_a_source_path(self) -> None:
        payload = json.dumps(self.engine.search("android security audit").to_json_obj())
        self.assertNotIn("source_path", payload)
        self.assertNotIn(".md", payload)
        route_payload = json.dumps(self.router.route("android security audit").to_json_obj())
        self.assertNotIn("source_path", route_payload)


class TestRegressionFloors(RealRegistryCase):
    """Internal guards. NOT an independently authored benchmark — see the
    disclosure in ``tests/data/search_routing_regression.v1.json``."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.search_result = diagnostics.score_cases(cls.engine, cls.cases)
        cls.summary = diagnostics.summarize(cls.search_result)
        cls.routing_result = diagnostics.score_routing(cls.router, cls.cases)

    def test_every_label_resolves(self) -> None:
        self.assertEqual(diagnostics.validate_labels(self.registry, self.cases), [])

    def test_the_dataset_has_the_intended_composition(self) -> None:
        counts: dict[str, int] = {}
        for case in self.cases:
            counts[case["class"]] = counts.get(case["class"], 0) + 1
        self.assertGreaterEqual(len(self.cases), 120)
        for name in diagnostics.CLASSES:
            self.assertGreater(counts.get(name, 0), 0, name)

    def test_resource_retrieval_floors(self) -> None:
        self.assertGreaterEqual(self.summary["r@1"], FLOORS["r@1"])
        self.assertGreaterEqual(self.summary["r@5"], FLOORS["r@5"])

    def test_natural_language_task_floor(self) -> None:
        task = self.search_result["per_class"]["task"]
        self.assertGreaterEqual(task.rate("r@1", "n_resource"), FLOORS["task_r@1"])

    def test_scope_and_kind_floors(self) -> None:
        self.assertGreaterEqual(self.summary["scope@1"], FLOORS["scope@1"])
        self.assertGreaterEqual(self.summary["kind@1"], FLOORS["kind@1"])

    def test_no_ineligible_resource_leaks(self) -> None:
        self.assertEqual(self.summary["deprecated_leaks"], 0)
        self.assertEqual(self.summary["tombstone_leaks"], 0)
        self.assertEqual(self.summary["excluded_leaks"], 0)

    def test_cluster_deduplication_actually_suppresses_duplicates(self) -> None:
        """The metric is measured with suppression off, so a nonzero count is
        evidence the default is doing work rather than decorating."""
        self.assertGreater(self.summary["duplicate_cluster_leaks"], 0)

    def test_the_router_does_not_sound_certain_on_ambiguous_tasks(self) -> None:
        self.assertLessEqual(
            len(self.routing_result["false_confident"]),
            MAX_FALSE_CONFIDENT,
            self.routing_result["false_confident"],
        )

    def test_bm25f_still_beats_the_rejected_baselines(self) -> None:
        """Phase 4A chose BM25F over two simpler rankers. If a corpus change
        ever inverts that, the choice should be revisited, not inherited."""
        scores = {
            name: diagnostics.summarize(
                diagnostics.score_cases(self.engine, self.cases, scorer=scorer)
            )
            for name, scorer in diagnostics.BASELINES.items()
        }
        shipped = scores["BM25F uniform (shipped)"]
        overlap = scores["weighted token overlap"]
        flat = scores["flat BM25"]
        self.assertGreater(shipped["r@1"], overlap["r@1"] + 0.10)
        self.assertGreaterEqual(shipped["r@1"], flat["r@1"])
        self.assertGreaterEqual(shipped["scope@1"], flat["scope@1"])


class TestRealRegistryBehaviour(RealRegistryCase):
    def test_scope_vocabulary_is_derived_consistently(self) -> None:
        scopes = self.engine.scopes
        self.assertIn("software-engineering", scopes)
        self.assertIn("agentic-resources/cloud-infrastructure", scopes)
        self.assertNotIn("agentic-resources", scopes)
        # A technique's scope is its category, never its own ID.
        self.assertNotIn("st-01", scopes)

    def test_exact_reference_does_not_build_the_index(self) -> None:
        engine = SearchEngine(Registry.open(_repository()))
        results = engine.search("technique:ST-01")
        self.assertEqual([hit.id for hit in results.hits], ["technique:ST-01"])
        self.assertFalse(engine.index_info["built"])

    def test_a_registered_copy_and_its_canonical_collapse(self) -> None:
        results = self.engine.search("calculate TAM SAM SOM market size", limit=25)
        clusters = [hit.canonical_uid for hit in results.hits]
        self.assertEqual(len(clusters), len(set(clusters)))

    def test_repeated_queries_are_byte_identical(self) -> None:
        first = json.dumps(
            self.engine.search("android security audit").to_json_obj(), sort_keys=True
        )
        for _ in range(3):
            self.assertEqual(
                first,
                json.dumps(
                    self.engine.search("android security audit").to_json_obj(), sort_keys=True
                ),
            )

    def test_warm_search_is_not_pathologically_slow(self) -> None:
        """A generous sanity bound, not a performance gate: wall-clock numbers
        vary far too much between machines to gate correctness on."""
        self.engine.search("warm up the index")
        samples = []
        for query in ("android security audit", "write a sermon", "negotiate a raise"):
            started = time.perf_counter()
            self.engine.search(query)
            samples.append(time.perf_counter() - started)
        self.assertLess(statistics.median(samples), 1.0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

"""SearchEngine behaviour: eligibility, copies, exact references, determinism.

Production has no aliases and no excluded records, so the interesting policy
paths exist only in synthetic checkouts. Real-registry behaviour is covered in
``test_search_regression.py``.
"""

from __future__ import annotations

import json
import unittest

import fixtures
from _support import EngineTestCase
from pae_engine import Registry, Repository, SearchEngine, UsageError
from pae_engine._lexical import MAX_LIMIT, MAX_QUERY_CHARS

#: Crockford base32 omits i, l, o and u, so a readable mnemonic has to be
#: transliterated before it can be a valid UID.
_CROCKFORD = str.maketrans({"i": "1", "l": "1", "o": "0", "u": "v"})


def _uid(mnemonic: str) -> str:
    """A valid UID: ``pae_`` plus twelve Crockford base32 characters."""
    body = (mnemonic.translate(_CROCKFORD) + "0" * 12)[:12]
    return "pae_" + body


class SearchFixtureCase(EngineTestCase):
    """A checkout holding one of every policy and lifecycle case."""

    def build(self, **engine_kwargs) -> SearchEngine:
        root = self.tmp_path()
        records = [
            fixtures.record(
                uid=_uid("standard"),
                id="prompt:alpha/standard-widget",
                title="Standard Widget Review",
                description="Review a widget for quality problems.",
                path="alpha/standard.md",
                native={"category": "alpha", "tags": ["widget", "review"]},
            ),
            fixtures.record(
                uid=_uid("gated"),
                id="prompt:alpha/gated-widget",
                title="Gated Widget Protocol",
                description="A safety gated widget protocol.",
                policy="safety_gated",
                path="alpha/gated.md",
                native={"category": "alpha", "tags": ["widget"]},
            ),
            fixtures.record(
                uid=_uid("metaonly"),
                id="prompt:alpha/metadata-only-widget",
                title="Metadata Only Widget",
                description="A widget whose body is withheld.",
                policy="metadata_only",
                path="alpha/metaonly.md",
                native={"category": "alpha", "tags": ["widget"]},
            ),
            fixtures.record(
                uid=_uid("excluded"),
                id="prompt:alpha/excluded-widget",
                title="Excluded Widget Secret",
                description="An excluded widget nobody may search.",
                policy="excluded",
                path="alpha/excluded.md",
                native={"category": "alpha", "tags": ["widget"]},
            ),
            fixtures.record(
                uid=_uid("tombstone"),
                id="prompt:alpha/retired-widget",
                title="Retired Widget Guide",
                description="A retired widget guide.",
                lifecycle="tombstone",
                maturity="deprecated",
                native={"category": "alpha", "tags": ["widget"]},
            ),
            fixtures.record(
                uid=_uid("deprecat"),
                id="technique:WD-01",
                kind="technique",
                title="Deprecated Widget Technique",
                maturity="deprecated",
                defined_in="techniques/MASTER_TECHNIQUE_INDEX.md",
                native={"category": "WD", "state": "deprecated"},
            ),
            fixtures.record(
                uid=_uid("renamed"),
                id="prompt:alpha/renamed-widget",
                title="Renamed Widget Helper",
                description="A widget helper that was renamed.",
                aliases=["prompt:alpha/old-widget-helper"],
                path="alpha/renamed.md",
                native={"category": "alpha", "tags": ["widget"]},
            ),
            # A canonical and its registered copy. The copy is deliberately
            # richer so it out-scores the canonical and represents the cluster.
            fixtures.record(
                uid=_uid("canon"),
                id="prompt:beta/sprocket-planner",
                title="Sprocket Planner",
                description="Plan a sprocket.",
                path="beta/sprocket.md",
                native={"category": "beta", "tags": ["sprocket"]},
                relationships={"copies": [_uid("copy")]},
            ),
            fixtures.record(
                uid=_uid("copy"),
                id="prompt:toolkit/sprocket-planner",
                title="Sprocket Planner",
                description="Plan a sprocket inside the toolkit sprocket pipeline.",
                path="toolkit/sprocket.md",
                native={"category": "toolkit", "tags": ["sprocket", "toolkit"]},
                relationships={"copy_of": _uid("canon")},
            ),
            # A copy whose canonical is excluded: its cluster metadata must
            # never surface the excluded record.
            fixtures.record(
                uid=_uid("hiddenc"),
                id="prompt:alpha/hidden-canonical",
                title="Hidden Canonical Gadget",
                policy="excluded",
                path="alpha/hidden.md",
                relationships={"copies": [_uid("visiblec")]},
            ),
            fixtures.record(
                uid=_uid("visiblec"),
                id="prompt:toolkit/visible-gadget",
                title="Visible Gadget Copy",
                description="A gadget copy whose canonical is excluded.",
                path="toolkit/gadget.md",
                relationships={"copy_of": _uid("hiddenc")},
            ),
        ]
        fixtures.build_repo(root, records)
        registry = Registry.open(Repository.at(root))
        return SearchEngine(registry, **engine_kwargs)


class TestEligibility(SearchFixtureCase):
    def test_excluded_is_never_searchable(self) -> None:
        engine = self.build(include_deprecated=True, include_tombstones=True)
        results = engine.search("excluded widget secret", limit=MAX_LIMIT)
        self.assertNotIn(
            "prompt:alpha/excluded-widget", [hit.id for hit in results.hits]
        )

    def test_no_flag_combination_reveals_an_excluded_record(self) -> None:
        for deprecated in (False, True):
            for tombstones in (False, True):
                engine = self.build(
                    include_deprecated=deprecated, include_tombstones=tombstones
                )
                blob = json.dumps(
                    engine.search("widget", limit=MAX_LIMIT).to_json_obj()
                )
                self.assertNotIn("excluded-widget", blob)
                self.assertNotIn(_uid("excluded"), blob)

    def test_metadata_only_and_safety_gated_are_searchable(self) -> None:
        engine = self.build()
        ids = [hit.id for hit in engine.search("widget", limit=MAX_LIMIT).hits]
        self.assertIn("prompt:alpha/metadata-only-widget", ids)
        self.assertIn("prompt:alpha/gated-widget", ids)

    def test_tombstones_are_hidden_by_default(self) -> None:
        engine = self.build()
        ids = [hit.id for hit in engine.search("retired widget guide").hits]
        self.assertNotIn("prompt:alpha/retired-widget", ids)

    def test_include_tombstones_alone_is_enough(self) -> None:
        """Every tombstone is also deprecated; requiring both flags would make
        ``include_tombstones`` useless on its own."""
        engine = self.build(include_tombstones=True)
        ids = [hit.id for hit in engine.search("retired widget guide").hits]
        self.assertIn("prompt:alpha/retired-widget", ids)

    def test_live_deprecated_is_hidden_by_default_and_included_by_its_flag(self) -> None:
        hidden = self.build()
        self.assertNotIn(
            "technique:WD-01",
            [hit.id for hit in hidden.search("deprecated widget technique").hits],
        )
        shown = self.build(include_deprecated=True)
        self.assertIn(
            "technique:WD-01",
            [hit.id for hit in shown.search("deprecated widget technique").hits],
        )

    def test_include_tombstones_does_not_reveal_live_deprecated(self) -> None:
        engine = self.build(include_tombstones=True)
        ids = [hit.id for hit in engine.search("deprecated widget technique").hits]
        self.assertNotIn("technique:WD-01", ids)


class TestCopyClusters(SearchFixtureCase):
    def test_default_returns_one_hit_per_cluster(self) -> None:
        engine = self.build()
        hits = engine.search("sprocket planner", limit=MAX_LIMIT).hits
        ids = [hit.id for hit in hits]
        self.assertEqual(
            len([i for i in ids if i.endswith("sprocket-planner")]),
            1,
            f"cluster was not collapsed: {ids}",
        )

    def test_the_higher_scoring_copy_represents_the_cluster(self) -> None:
        engine = self.build()
        hits = engine.search("toolkit sprocket", limit=MAX_LIMIT).hits
        self.assertEqual(hits[0].id, "prompt:toolkit/sprocket-planner")
        self.assertEqual(hits[0].canonical_uid, _uid("canon"))
        self.assertIn(_uid("canon"), hits[0].copy_uids)

    def test_include_copies_returns_both_physical_members(self) -> None:
        engine = self.build()
        ids = [
            hit.id
            for hit in engine.search(
                "sprocket planner", limit=MAX_LIMIT, include_copies=True
            ).hits
        ]
        self.assertIn("prompt:beta/sprocket-planner", ids)
        self.assertIn("prompt:toolkit/sprocket-planner", ids)

    def test_both_cluster_members_score(self) -> None:
        engine = self.build()
        results = engine.search("sprocket", limit=MAX_LIMIT, include_copies=True)
        scores = {hit.id: hit.score for hit in results.hits}
        self.assertGreater(scores["prompt:beta/sprocket-planner"], 0.0)
        self.assertGreater(scores["prompt:toolkit/sprocket-planner"], 0.0)

    def test_an_excluded_canonical_never_leaks_through_cluster_metadata(self) -> None:
        engine = self.build()
        hits = engine.search("visible gadget copy", limit=MAX_LIMIT).hits
        gadget = next(h for h in hits if h.id == "prompt:toolkit/visible-gadget")
        self.assertEqual(gadget.copy_uids, ())
        self.assertNotIn(_uid("hiddenc"), json.dumps(gadget.to_json_obj()))

    def test_total_matched_counts_logical_results(self) -> None:
        engine = self.build()
        logical = engine.search("sprocket", limit=1)
        physical = engine.search("sprocket", limit=1, include_copies=True)
        self.assertEqual(logical.total_matched + 1, physical.total_matched)


class TestExactReference(SearchFixtureCase):
    def test_exact_public_id_returns_rank_one_without_building_the_index(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/standard-widget")
        self.assertEqual([hit.id for hit in results.hits], ["prompt:alpha/standard-widget"])
        self.assertEqual(results.hits[0].matched_fields, ("exact_reference",))
        self.assertFalse(engine.index_info["built"])

    def test_exact_uid_resolves(self) -> None:
        engine = self.build()
        results = engine.search(_uid("standard"))
        self.assertEqual([hit.id for hit in results.hits], ["prompt:alpha/standard-widget"])
        self.assertFalse(engine.index_info["built"])

    def test_a_retired_alias_resolves_and_says_so(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/old-widget-helper")
        self.assertEqual([hit.id for hit in results.hits], ["prompt:alpha/renamed-widget"])
        self.assertTrue(any("retired alias" in notice for notice in results.notices))

    def test_an_exact_copy_reference_returns_that_physical_copy(self) -> None:
        """Naming a copy outright must not silently hand back its canonical."""
        engine = self.build()
        results = engine.search("prompt:toolkit/sprocket-planner")
        self.assertEqual([hit.id for hit in results.hits], ["prompt:toolkit/sprocket-planner"])
        self.assertEqual(results.hits[0].canonical_uid, _uid("canon"))

    def test_an_excluded_reference_returns_nothing_and_reveals_nothing(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/excluded-widget")
        self.assertEqual(results.hits, ())
        self.assertEqual(results.notices, ())
        blob = json.dumps(results.to_json_obj())
        self.assertNotIn(_uid("excluded"), blob)
        self.assertNotIn("Excluded Widget Secret", blob)

    def test_a_tombstone_reference_is_hidden_but_explained(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/retired-widget")
        self.assertEqual(results.hits, ())
        self.assertTrue(any("tombstone" in notice for notice in results.notices))
        included = self.build(include_tombstones=True)
        self.assertEqual(
            [hit.id for hit in included.search("prompt:alpha/retired-widget").hits],
            ["prompt:alpha/retired-widget"],
        )

    def test_a_deprecated_reference_is_hidden_but_explained(self) -> None:
        engine = self.build()
        results = engine.search("technique:WD-01")
        self.assertEqual(results.hits, ())
        self.assertTrue(any("deprecated" in notice for notice in results.notices))

    def test_a_reference_shaped_query_that_resolves_to_nothing_falls_back(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/no-such-widget")
        self.assertTrue(engine.index_info["built"])
        self.assertTrue(results.hits)

    def test_a_kind_filter_still_applies_to_an_exact_reference(self) -> None:
        engine = self.build()
        results = engine.search("prompt:alpha/standard-widget", kinds=["skill"])
        self.assertEqual(results.hits, ())
        self.assertTrue(any("kind filter" in notice for notice in results.notices))


class TestFiltersAndBounds(SearchFixtureCase):
    def test_unknown_kind_is_a_usage_error(self) -> None:
        engine = self.build()
        with self.assertRaises(UsageError):
            engine.search("widget", kinds=["nonsense"])

    def test_unknown_scope_is_a_usage_error(self) -> None:
        engine = self.build()
        with self.assertRaises(UsageError):
            engine.search("widget", scopes=["no-such-scope"])

    def test_scope_filter_subsets_results(self) -> None:
        engine = self.build()
        hits = engine.search("sprocket planner", scopes=["toolkit"], limit=MAX_LIMIT).hits
        self.assertTrue(hits)
        self.assertTrue(all(hit.scope == "toolkit" for hit in hits))

    def test_empty_and_stopword_only_queries_are_usage_errors(self) -> None:
        engine = self.build()
        for query in ("", "   ", "the and of", "!!!"):
            with self.assertRaises(UsageError, msg=query):
                engine.search(query)

    def test_query_and_limit_bounds(self) -> None:
        engine = self.build()
        with self.assertRaises(UsageError):
            engine.search("x" * (MAX_QUERY_CHARS + 1))
        with self.assertRaises(UsageError):
            engine.search(" ".join(f"term{i}" for i in range(200)))
        for bad in (0, -1, MAX_LIMIT + 1):
            with self.assertRaises(UsageError):
                engine.search("widget", limit=bad)

    def test_zero_results_is_a_normal_answer(self) -> None:
        engine = self.build()
        results = engine.search("zzzzqqq wobblegonk")
        self.assertEqual(results.hits, ())
        self.assertEqual(results.total_matched, 0)


class TestDeterminism(SearchFixtureCase):
    def test_repeated_queries_are_byte_identical(self) -> None:
        engine = self.build()
        first = json.dumps(engine.search("widget", limit=MAX_LIMIT).to_json_obj(), sort_keys=True)
        for _ in range(5):
            again = json.dumps(
                engine.search("widget", limit=MAX_LIMIT).to_json_obj(), sort_keys=True
            )
            self.assertEqual(first, again)

    def test_independent_engines_agree(self) -> None:
        a = json.dumps(self.build().search("widget", limit=MAX_LIMIT).to_json_obj(), sort_keys=True)
        b = json.dumps(self.build().search("widget", limit=MAX_LIMIT).to_json_obj(), sort_keys=True)
        self.assertEqual(a, b)

    def test_ties_break_on_public_id_ascending(self) -> None:
        """Two records with identical searchable text must order by ID."""
        root = self.tmp_path("ties")
        records = [
            fixtures.record(uid=_uid("zzz"), id="prompt:alpha/zulu", title="Identical Twin"),
            fixtures.record(uid=_uid("aaa"), id="prompt:alpha/alfa", title="Identical Twin"),
        ]
        fixtures.build_repo(root, records)
        engine = SearchEngine(Registry.open(Repository.at(root)))
        hits = engine.search("identical twin").hits
        self.assertEqual([hit.id for hit in hits], ["prompt:alpha/alfa", "prompt:alpha/zulu"])
        self.assertEqual(hits[0].score, hits[1].score)


class TestIndexLifecycle(SearchFixtureCase):
    def test_index_is_not_built_until_a_lexical_search(self) -> None:
        engine = self.build()
        self.assertFalse(engine.index_info["built"])
        self.assertNotIn("records_indexed", engine.index_info)
        engine.search("widget")
        self.assertTrue(engine.index_info["built"])
        self.assertGreater(engine.index_info["records_indexed"], 0)
        self.assertGreater(engine.index_info["distinct_terms"], 0)

    def test_index_reports_what_policy_removed(self) -> None:
        engine = self.build()
        engine.search("widget")
        info = engine.index_info
        self.assertEqual(info["records_excluded_by_policy"], 2)
        self.assertLess(info["records_indexed"], info["records_loaded"])

    def test_a_snapshot_is_not_reloaded(self) -> None:
        """The engine represents the registry it read, not the one on disk now."""
        engine = self.build()
        before = engine.search("widget", limit=MAX_LIMIT).total_matched
        registry_path = engine.registry.repository.registry_path
        registry_path.write_text("", encoding="utf-8")
        self.assertEqual(engine.search("widget", limit=MAX_LIMIT).total_matched, before)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

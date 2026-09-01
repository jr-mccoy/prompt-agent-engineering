"""Router behaviour: aggregation, thresholds, and refusing to guess.

The failure this file exists to prevent is not "the router picked the second
best scope". It is "the router sounded certain when the evidence was thin".
"""

from __future__ import annotations

import json
import unittest

import fixtures
from _support import EngineTestCase
from pae_engine import Registry, Repository, Router, SearchEngine, UsageError
from pae_engine.routing import COVERAGE_THRESHOLD, MARGIN_THRESHOLD

_CROCKFORD = str.maketrans({"i": "1", "l": "1", "o": "0", "u": "v"})


def _uid(mnemonic: str) -> str:
    return "pae_" + (mnemonic.translate(_CROCKFORD) + "0" * 12)[:12]


class RouterCase(EngineTestCase):
    def router_for(self, records, **kwargs) -> Router:
        root = self.tmp_path(f"repo{len(records)}-{id(records) % 9973}")
        fixtures.build_repo(root, records)
        engine = SearchEngine(Registry.open(Repository.at(root)), **kwargs)
        return Router(engine)


class TestStatuses(RouterCase):
    def test_a_clear_winner_is_matched(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("alpha"),
                    id="prompt:alpha/kubernetes-cluster-upgrade",
                    title="Kubernetes Cluster Upgrade Runbook",
                    description="Upgrade a kubernetes cluster safely.",
                    native={"category": "alpha", "tags": ["kubernetes", "cluster"]},
                ),
                fixtures.record(
                    uid=_uid("beta"),
                    id="prompt:beta/unrelated-topic",
                    title="Something Entirely Different",
                    description="Nothing to do with the query.",
                ),
            ]
        )
        decision = router.route("kubernetes cluster upgrade")
        self.assertEqual(decision.status, "matched")
        self.assertEqual(decision.selected_scope, "alpha")
        self.assertEqual(decision.selected_kind, "prompt")
        self.assertGreaterEqual(decision.coverage, COVERAGE_THRESHOLD)

    def test_two_close_scopes_are_ambiguous_and_select_nothing(self) -> None:
        """The important half is the second: no selection when it is close."""
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("gamma"),
                    id="prompt:gamma/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                ),
                fixtures.record(
                    uid=_uid("delta"),
                    id="prompt:delta/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                ),
            ]
        )
        decision = router.route("widget review")
        self.assertEqual(decision.status, "ambiguous")
        self.assertIsNone(decision.selected_scope)
        self.assertIsNone(decision.selected_kind)
        self.assertLess(decision.margin, MARGIN_THRESHOLD)
        self.assertEqual(len(decision.candidate_scopes), 2)

    def test_thin_overlap_is_weak_and_selects_nothing(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("eps"),
                    id="prompt:epsilon/widget",
                    title="Widget",
                    description="A widget.",
                )
            ]
        )
        decision = router.route("widget sourdough starter hydration schedule bakery")
        self.assertEqual(decision.status, "weak")
        self.assertIsNone(decision.selected_scope)
        self.assertLess(decision.coverage, COVERAGE_THRESHOLD)

    def test_nothing_matching_is_no_route(self) -> None:
        router = self.router_for(
            [fixtures.record(uid=_uid("zeta"), id="prompt:zeta/widget", title="Widget")]
        )
        decision = router.route("zzzzqqq wobblegonk")
        self.assertEqual(decision.status, "no_route")
        self.assertEqual(decision.resources, ())
        self.assertEqual(decision.candidate_scopes, ())
        self.assertEqual(decision.coverage, 0.0)
        self.assertEqual(decision.margin, 0.0)

    def test_a_single_scope_gets_full_margin(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("eta"),
                    id="prompt:eta/kubernetes-runbook",
                    title="Kubernetes Runbook",
                    description="A kubernetes runbook.",
                )
            ]
        )
        decision = router.route("kubernetes runbook")
        self.assertEqual(decision.margin, 1.0)
        self.assertEqual(decision.status, "matched")

    def test_every_status_is_a_declared_one(self) -> None:
        from pae_engine import ROUTE_STATUSES

        router = self.router_for(
            [fixtures.record(uid=_uid("theta"), id="prompt:theta/widget", title="Widget Review")]
        )
        for query in ("widget review", "zzzzqqq wobblegonk", "widget unrelated words here now"):
            self.assertIn(router.route(query).status, ROUTE_STATUSES)


class TestAggregation(RouterCase):
    def test_population_size_never_wins(self) -> None:
        """A summing router hands this to ``prompt`` forty times out of forty."""
        records = [
            fixtures.record(
                uid=_uid(f"bulk{n:03d}"),
                id=f"prompt:bulk/helm-note-{n:03d}",
                title="Helm Note",
                description="A passing mention of helm.",
            )
            for n in range(40)
        ]
        records.append(
            fixtures.record(
                uid=_uid("skill1"),
                id="skill:agentic-resources/cloud-infrastructure/helm-chart-scaffolding",
                kind="skill",
                title="Helm Chart Scaffolding",
                description="Generate a production ready helm chart with helm best practice.",
                native={"name": "helm-chart-scaffolding", "tags": ["helm", "chart"]},
            )
        )
        decision = self.router_for(records).route("helm chart scaffolding")
        self.assertEqual(decision.candidate_kinds[0].name, "skill")
        self.assertEqual(decision.selected_kind, "skill")
        self.assertEqual(decision.selected_scope, "agentic-resources/cloud-infrastructure")

    def test_hit_count_is_reported_but_never_scored(self) -> None:
        records = [
            fixtures.record(
                uid=_uid(f"many{n:03d}"),
                id=f"prompt:many/widget-{n:03d}",
                title="Widget Mention",
                description="A widget.",
            )
            for n in range(12)
        ]
        records.append(
            fixtures.record(
                uid=_uid("one"),
                id="prompt:single/widget-review-deep-dive",
                title="Widget Review Deep Dive",
                description="A deep dive widget review of widget review practice.",
                native={"tags": ["widget", "review"]},
            )
        )
        decision = self.router_for(records).route("widget review deep dive")
        winner = decision.candidate_scopes[0]
        self.assertEqual(winner.name, "single")
        self.assertEqual(winner.hit_count, 1)
        self.assertGreater(decision.candidate_scopes[1].hit_count, winner.hit_count)

    def test_a_copy_does_not_vote_twice_for_its_toolkit(self) -> None:
        """Cluster suppression happens before aggregation, so a registered copy
        cannot inflate its scope's evidence."""
        base = [
            fixtures.record(
                uid=_uid("canon"),
                id="prompt:home/sprocket-planner",
                title="Sprocket Planner",
                description="Plan a sprocket.",
                native={"tags": ["sprocket"]},
            ),
            fixtures.record(
                uid=_uid("rival"),
                id="prompt:rival/sprocket-planning-guide",
                title="Sprocket Planning Guide",
                description="Plan a sprocket, in a rival scope.",
                native={"tags": ["sprocket"]},
            ),
        ]
        without_copy = self.router_for(list(base)).route("sprocket planner")
        with_copy = self.router_for(
            base
            + [
                fixtures.record(
                    uid=_uid("cpy"),
                    id="prompt:toolkit/sprocket-planner",
                    title="Sprocket Planner",
                    description="Plan a sprocket.",
                    native={"tags": ["sprocket"]},
                    relationships={"copy_of": _uid("canon")},
                )
            ]
        ).route("sprocket planner")
        # The copy may represent its cluster, but it must not add a scope.
        self.assertEqual(
            len(with_copy.candidate_scopes), len(without_copy.candidate_scopes)
        )
        self.assertEqual(
            sum(c.hit_count for c in with_copy.candidate_scopes),
            sum(c.hit_count for c in without_copy.candidate_scopes),
        )

    def test_equal_scores_tie_break_by_name(self) -> None:
        router = self.router_for(
            [
                fixtures.record(uid=_uid("zulu"), id="prompt:zulu/widget", title="Widget Review"),
                fixtures.record(uid=_uid("alfa"), id="prompt:alfa/widget", title="Widget Review"),
            ]
        )
        decision = router.route("widget review")
        names = [candidate.name for candidate in decision.candidate_scopes]
        self.assertEqual(names, ["alfa", "zulu"])
        self.assertEqual(decision.margin, 0.0)


class TestRouterContract(RouterCase):
    def test_limit_bounds(self) -> None:
        router = self.router_for(
            [fixtures.record(uid=_uid("lim"), id="prompt:lim/widget", title="Widget")]
        )
        for bad in (0, -3, 26):
            with self.assertRaises(UsageError):
                router.route("widget", limit=bad)

    def test_unknown_kind_is_a_usage_error(self) -> None:
        router = self.router_for(
            [fixtures.record(uid=_uid("kin"), id="prompt:kin/widget", title="Widget")]
        )
        with self.assertRaises(UsageError):
            router.route("widget", kinds=["nonsense"])

    def test_resources_carry_durable_identity_not_paths(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("idy"),
                    id="prompt:idy/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                    path="idy/widget.md",
                )
            ]
        )
        decision = router.route("widget review")
        payload = decision.to_json_obj()
        self.assertTrue(decision.resources[0].uid.startswith("pae_"))
        self.assertNotIn("idy/widget.md", json.dumps(payload))
        self.assertNotIn("source_path", json.dumps(payload))

    def test_reasons_are_evidence_and_the_numbers_are_authoritative(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("rea"),
                    id="prompt:rea/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                )
            ]
        )
        decision = router.route("widget review")
        self.assertTrue(decision.reasons)
        self.assertTrue(any("coverage" in reason for reason in decision.reasons))
        self.assertIsInstance(decision.coverage, float)
        self.assertIsInstance(decision.margin, float)

    def test_no_confidence_or_probability_is_reported(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("cnf"),
                    id="prompt:cnf/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                )
            ]
        )
        payload = json.dumps(router.route("widget review").to_json_obj()).lower()
        for banned in ("confidence", "probability", "certainty", "%"):
            self.assertNotIn(banned, payload)

    def test_repeated_routes_are_byte_identical(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("det"),
                    id="prompt:det/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                ),
                fixtures.record(
                    uid=_uid("det2"),
                    id="prompt:other/widget-notes",
                    title="Widget Notes",
                    description="Notes about a widget.",
                ),
            ]
        )
        first = json.dumps(router.route("widget review").to_json_obj(), sort_keys=True)
        for _ in range(5):
            self.assertEqual(
                first, json.dumps(router.route("widget review").to_json_obj(), sort_keys=True)
            )

    def test_an_exact_reference_route_is_not_reported_as_uncertain(self) -> None:
        router = self.router_for(
            [
                fixtures.record(
                    uid=_uid("exa"),
                    id="prompt:exa/widget-review",
                    title="Widget Review",
                    description="Review a widget.",
                )
            ]
        )
        decision = router.route("prompt:exa/widget-review")
        self.assertEqual(decision.coverage, 1.0)
        self.assertEqual(decision.status, "matched")
        self.assertEqual(decision.selected_scope, "exa")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

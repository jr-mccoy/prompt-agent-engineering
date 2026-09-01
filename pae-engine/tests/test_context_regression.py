"""Packing floors against the live checkout, pinned so a regression is loud.

A fast subset of what ``run_context_compiler_diagnostics.py`` reports in full.
The floors are deliberately qualitative — the exact figures move whenever the
renderer or the corpus changes, and pinning them exactly would turn ordinary
content edits into red builds.

This is **packing regression, not task-quality evaluation.** It measures
whether the packer keeps what the ranking ranked highest and honours the
budget it reports. It says nothing about whether those resources answer the
task.
"""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pae_engine import (  # noqa: E402
    ApproximateTokenCounterV1,
    Budget,
    ContextCompiler,
    Registry,
    Repository,
    Router,
    SearchEngine,
)

DATA = Path(__file__).parent / "data" / "search_routing_regression.v1.json"
REPO = Path(__file__).resolve().parents[2]
SAMPLE = 30


class TestPackingFloors(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        registry = Registry.open(Repository.at(REPO))
        router = Router(SearchEngine(registry))
        compiler = ContextCompiler(registry)
        cases = json.loads(DATA.read_text(encoding="utf-8"))["cases"][:SAMPLE]
        cls.counter = ApproximateTokenCounterV1()
        cls.bundles = []
        for case in cases:
            decision = router.route(case["query"], limit=25)
            if not decision.resources:
                continue
            cls.bundles.append(
                (
                    decision,
                    compiler.compile_route(decision, budget=Budget(estimated_tokens=8000)),
                )
            )

    def test_the_sample_actually_produced_bundles(self) -> None:
        self.assertGreaterEqual(len(self.bundles), 20)

    def test_no_rendered_bundle_exceeds_the_budget_it_reports(self) -> None:
        """The load-bearing promise of the whole phase."""
        for decision, bundle in self.bundles:
            with self.subTest(task=decision.query[:40]):
                markdown = bundle.render_markdown()
                self.assertLessEqual(
                    len(markdown.encode("utf-8")), bundle.budget.effective_byte_ceiling
                )
                self.assertLessEqual(self.counter.count(markdown), 8000)
                self.assertEqual(bundle.budget.used_bytes, len(markdown.encode("utf-8")))

    def test_no_guarded_body_is_ever_shortened(self) -> None:
        guarded = 0
        for _, bundle in self.bundles:
            for item in bundle.included:
                if item.serving_policy != "safety_gated":
                    continue
                guarded += 1
                encoded = item.content.encode("utf-8")
                self.assertEqual(
                    "sha256:" + hashlib.sha256(encoded).hexdigest(), item.content_sha256
                )
                self.assertEqual(len(encoded), item.byte_length)
        self.assertGreater(guarded, 0, "the sample must exercise the guarded path")

    def test_top_hit_retention_at_eight_thousand_tokens(self) -> None:
        possible = kept = 0
        for decision, bundle in self.bundles:
            included = {item.uid for item in bundle.included}
            servable = included | {
                o.uid for o in bundle.omitted if o.reason in ("budget", "oversized")
            }
            top = decision.resources[0].uid
            if top in servable:
                possible += 1
                kept += top in included
        self.assertGreater(possible, 0)
        self.assertGreaterEqual(kept / possible, 0.90, f"top-1 retention {kept}/{possible}")

    def test_every_bundle_is_non_empty_or_had_nothing_servable(self) -> None:
        for decision, bundle in self.bundles:
            with self.subTest(task=decision.query[:40]):
                if bundle.included:
                    continue
                self.assertTrue(bundle.omitted)

    def test_route_status_is_never_rewritten_by_compilation(self) -> None:
        for decision, bundle in self.bundles:
            self.assertEqual(bundle.route_status, decision.status)
            if decision.status != "matched":
                self.assertIsNone(bundle.selected_scope)

    def test_every_candidate_is_accounted_for_exactly_once(self) -> None:
        for decision, bundle in self.bundles:
            with self.subTest(task=decision.query[:40]):
                seen = [i.uid for i in bundle.included] + [o.uid for o in bundle.omitted]
                self.assertEqual(len(seen), len(bundle.candidates))
                self.assertEqual(set(seen), set(bundle.candidates))

    def test_compilation_is_reproducible_against_the_live_registry(self) -> None:
        registry = Registry.open(Repository.at(REPO))
        compiler = ContextCompiler(registry)
        for decision, bundle in self.bundles[:5]:
            again = compiler.compile_route(decision, budget=Budget(estimated_tokens=8000))
            self.assertEqual(again.bundle_sha256, bundle.bundle_sha256)
            self.assertEqual(again.render_markdown(), bundle.render_markdown())


if __name__ == "__main__":
    unittest.main()

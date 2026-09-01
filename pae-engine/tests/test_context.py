"""Context compilation: budgets, body policy, packing, rendering and identity.

The synthetic checkout in ``fixtures`` is used wherever a negative case is
needed, because production has no excluded record and no checksum mismatch to
borrow. Behaviour that must hold against the real corpus lives in
``test_real_registry.py`` and in the diagnostics runner.
"""

from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import fixtures as fx  # noqa: E402
from _support import EngineTestCase  # noqa: E402

from pae_engine import (  # noqa: E402
    ApproximateTokenCounterV1,
    Budget,
    ContextCompiler,
    Registry,
    Repository,
)
from pae_engine._context_render import (  # noqa: E402
    MARKDOWN_OMISSION_DETAIL_LIMIT,
    _marker_pair,
)
from pae_engine.context import MAX_BUNDLE_BYTES  # noqa: E402
from pae_engine.errors import (  # noqa: E402
    BudgetTooSmall,
    ChecksumMismatch,
    ContentRefused,
    InvalidBudget,
    NoAddressableContent,
    ResourceExcluded,
    ResourceNotFound,
    UsageError,
)
from pae_engine.models import (  # noqa: E402
    OMISSION_REASONS,
    BundleItem,
    RouteCandidate,
    RouteDecision,
    SearchHit,
    SearchResults,
)

BIG = 1_000_000


def hit(uid: str, *, rank: int, scope: str = "alpha", score: float = 10.0) -> SearchHit:
    return SearchHit(
        uid=uid,
        id=f"prompt:{scope}/{uid}",
        kind="prompt",
        title=f"Title {uid}",
        scope=scope,
        rank=rank,
        score=score,
        maturity="experimental",
        serving_policy="standard",
        metadata_completeness="full",
        matched_fields=("title",),
        match_terms={"title": ("x",)},
        canonical_uid=uid,
        copy_uids=(),
    )


def decision(hits, *, status="matched", scopes=()) -> RouteDecision:
    candidates = tuple(
        RouteCandidate(name=name, score=score, hit_count=1, top_resource_uid=uid)
        for name, score, uid in scopes
    )
    return RouteDecision(
        query="a task",
        normalized_terms=("task",),
        status=status,
        selected_scope=candidates[0].name if (status == "matched" and candidates) else None,
        selected_kind="prompt" if status == "matched" else None,
        candidate_scopes=candidates,
        candidate_kinds=(),
        resources=tuple(hits),
        coverage=0.5,
        margin=0.1,
        reasons=("fixture",),
    )


class ContextTestCase(EngineTestCase):
    """A compiler over the synthetic every-policy checkout."""

    def setUp(self) -> None:
        super().setUp()
        self.root = fx.standard_repo(self.tmp_path())
        self.registry = Registry.open(Repository.at(self.root))
        self.compiler = ContextCompiler(self.registry)

    def compile_refs(self, refs, **kw):
        budget = kw.pop("budget", Budget(estimated_tokens=BIG))
        return self.compiler.compile_refs(refs, budget=budget, **kw)


# --------------------------------------------------------------------------
# budget model and byte ceiling
# --------------------------------------------------------------------------


class TestBudget(unittest.TestCase):
    def test_a_budget_needs_at_least_one_limit(self) -> None:
        with self.assertRaises(InvalidBudget):
            Budget()

    def test_limits_must_be_positive_integers(self) -> None:
        for kwargs in (
            {"estimated_tokens": 0},
            {"estimated_tokens": -1},
            {"bytes": 0},
            {"bytes": -5},
        ):
            with self.subTest(**kwargs), self.assertRaises(InvalidBudget):
                Budget(**kwargs)

    def test_bool_is_rejected_where_an_integer_is_required(self) -> None:
        """``True`` is an int subclass. A budget of ``True`` is a bug."""
        for kwargs in ({"estimated_tokens": True}, {"bytes": True}):
            with self.subTest(**kwargs), self.assertRaises(InvalidBudget):
                Budget(**kwargs)
        with self.assertRaises(InvalidBudget):
            Budget(estimated_tokens=10, max_resources=True)

    def test_max_resources_is_bounded(self) -> None:
        for value in (0, -1, 26, 1000):
            with self.subTest(value=value), self.assertRaises(InvalidBudget):
                Budget(estimated_tokens=10, max_resources=value)
        self.assertEqual(Budget(estimated_tokens=10).max_resources, 25)

    def test_both_limits_may_be_supplied(self) -> None:
        budget = Budget(estimated_tokens=10, bytes=100)
        self.assertEqual((budget.estimated_tokens, budget.bytes), (10, 100))

    def test_invalid_budget_maps_to_exit_two(self) -> None:
        self.assertEqual(InvalidBudget.exit_code, 2)


class TestByteCeiling(ContextTestCase):
    def test_explicit_bytes_win_and_are_capped_by_the_engine_ceiling(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID], budget=Budget(bytes=9000))
        self.assertEqual(bundle.budget.byte_ceiling_source, "explicit")
        self.assertEqual(bundle.budget.effective_byte_ceiling, 9000)

        bundle = self.compile_refs([fx.STANDARD_ID], budget=Budget(bytes=MAX_BUNDLE_BYTES * 4))
        self.assertEqual(bundle.budget.effective_byte_ceiling, MAX_BUNDLE_BYTES)

    def test_tokens_with_the_default_estimator_derive_an_exact_byte_ceiling(self) -> None:
        """``ceil(b/4) <= T`` is exactly ``b <= 4T`` — for this estimator only."""
        bundle = self.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=2000))
        self.assertEqual(bundle.budget.byte_ceiling_source, "derived_from_default_estimator")
        self.assertEqual(bundle.budget.effective_byte_ceiling, 8000)

    def test_a_custom_counter_without_bytes_falls_back_to_the_engine_ceiling(self) -> None:
        compiler = ContextCompiler(self.registry, token_counter=WordCounter())
        bundle = compiler.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.budget.byte_ceiling_source, "engine_safety_ceiling")
        self.assertEqual(bundle.budget.effective_byte_ceiling, MAX_BUNDLE_BYTES)

    def test_the_most_restrictive_limit_is_enforced_and_all_inputs_reported(self) -> None:
        bundle = self.compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG, bytes=MAX_BUNDLE_BYTES)
        )
        self.assertEqual(bundle.budget.requested_estimated_tokens, BIG)
        self.assertEqual(bundle.budget.requested_bytes, MAX_BUNDLE_BYTES)


class TestEstimator(unittest.TestCase):
    def test_the_default_counter_never_claims_exactness(self) -> None:
        counter = ApproximateTokenCounterV1()
        self.assertFalse(counter.exact)
        self.assertEqual(counter.count(""), 0)
        self.assertEqual(counter.count("abcd"), 1)
        self.assertEqual(counter.count("abcde"), 2)

    def test_multibyte_text_is_counted_by_bytes_not_characters(self) -> None:
        counter = ApproximateTokenCounterV1()
        self.assertEqual(counter.count("中"), 1)  # 3 UTF-8 bytes
        self.assertEqual(counter.count("中" * 4), 3)  # 12 bytes

    def test_no_public_text_claims_a_safe_or_exact_token_fit(self) -> None:
        """The estimator's truthfulness is part of the contract, not a caveat."""
        from pae_engine import context

        prose = (context.__doc__ or "") + (ApproximateTokenCounterV1.__doc__ or "")
        lowered = prose.lower()
        self.assertIn("estimate", lowered)
        for claim in ("guaranteed upper bound", "safe upper bound and", "exact token"):
            self.assertNotIn(claim, lowered.replace("not a safe upper bound", ""))


class WordCounter:
    """A deterministic exact counter, standing in for a provider tokenizer.

    Deliberately not a real tokenizer: the point is that *any* conforming
    counter changes the budget arithmetic and the bundle identity.
    """

    name = "fixture-words"
    version = "1"
    exact = True

    def count(self, text: str) -> int:
        return len(text.split())


class TestCustomCounter(ContextTestCase):
    def test_exactness_propagates_and_drives_the_token_limit(self) -> None:
        compiler = ContextCompiler(self.registry, token_counter=WordCounter())
        bundle = compiler.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG))
        self.assertTrue(bundle.budget.estimator_exact)
        self.assertEqual(bundle.budget.estimator_name, "fixture-words")
        markdown = bundle.render_markdown()
        self.assertEqual(bundle.budget.used_estimated_tokens, len(markdown.split()))

    def test_the_byte_ceiling_still_applies_under_a_custom_counter(self) -> None:
        compiler = ContextCompiler(self.registry, token_counter=WordCounter())
        bundle = compiler.compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG, bytes=MAX_BUNDLE_BYTES)
        )
        self.assertLessEqual(
            len(bundle.render_markdown().encode("utf-8")),
            bundle.budget.effective_byte_ceiling,
        )

    def test_the_counter_identity_changes_the_bundle_hash(self) -> None:
        default = self.compile_refs([fx.STANDARD_ID])
        custom = ContextCompiler(self.registry, token_counter=WordCounter()).compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG)
        )
        self.assertNotEqual(default.bundle_sha256, custom.bundle_sha256)

    def test_the_same_counter_is_reproducible(self) -> None:
        one = ContextCompiler(self.registry, token_counter=WordCounter()).compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG)
        )
        two = ContextCompiler(self.registry, token_counter=WordCounter()).compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG)
        )
        self.assertEqual(one.bundle_sha256, two.bundle_sha256)


# --------------------------------------------------------------------------
# body policy
# --------------------------------------------------------------------------


class TestBodyFidelity(ContextTestCase):
    def test_an_included_body_is_the_registry_body_exactly(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID])
        item = bundle.included[0]
        content = self.registry.content(fx.STANDARD_ID)
        self.assertEqual(item.content, content.text())
        self.assertEqual(item.content_sha256, content.content_sha256)
        self.assertEqual(item.byte_length, content.byte_length)
        self.assertTrue(item.verified)

    def test_the_body_appears_verbatim_in_the_rendering(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID])
        self.assertIn(fx.STANDARD_BODY.decode("utf-8"), bundle.render_markdown())

    def test_frontmatter_is_retained(self) -> None:
        root = self.tmp_path("frontmatter")
        body = b"---\ntitle: Kept\nserving_policy: standard\n---\n\n# Body\n\ntext\n"
        path, sha = fx.with_source(root, "fixtures/fm.md", body)
        fx.build_repo(root, [fx.record("pae_0000000000fm", "prompt:fixtures/fm",
                                       path=path, content_sha256=sha)])
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        bundle = compiler.compile_refs(["prompt:fixtures/fm"], budget=Budget(estimated_tokens=BIG))
        self.assertIn("---\ntitle: Kept", bundle.included[0].content)
        self.assertIn("---\ntitle: Kept", bundle.render_markdown())

    def test_there_is_no_truncation_path_anywhere_in_the_public_surface(self) -> None:
        from pae_engine import context, models
        from pae_engine.models import BundleItem

        for name in ("truncate", "excerpt", "head", "tail", "summarize"):
            self.assertFalse(hasattr(BundleItem, name))
            self.assertFalse(hasattr(context.ContextCompiler, name))
            self.assertFalse(hasattr(models.ContextBundle, name))


class TestSafetyGated(ContextTestCase):
    def test_a_guarded_body_is_served_whole_with_its_guard_metadata(self) -> None:
        bundle = self.compile_refs([fx.SAFETY_ID])
        item = bundle.included[0]
        self.assertEqual(item.serving_policy, "safety_gated")
        self.assertEqual(item.content, fx.SAFETY_BODY.decode("utf-8"))
        self.assertTrue(item.guard_preservation["must_not_truncate"])
        self.assertIn("truncation is not permitted", bundle.render_markdown())

    def test_a_guarded_body_that_does_not_fit_is_absent_rather_than_shortened(self) -> None:
        """The whole point of ``must_not_truncate``: present in full, or gone."""
        budget = Budget(bytes=1200)
        bundle = self.compiler.compile_refs([fx.SAFETY_ID], budget=budget)
        body = fx.SAFETY_BODY.decode("utf-8")
        if bundle.included:
            self.assertEqual(bundle.included[0].content, body)
        else:
            markdown = bundle.render_markdown()
            self.assertNotIn(body[:40], markdown)
            self.assertEqual(bundle.omitted[0].reason, "oversized")

    def test_packing_continues_past_a_guarded_resource_that_did_not_fit(self) -> None:
        hits = [hit(fx.SAFETY_UID, rank=1), hit(fx.STANDARD_UID, rank=2)]
        results = SearchResults(
            query="q", normalized_terms=(), hits=tuple(hits), total_matched=2, filters={}
        )
        # Room for the smaller body but not the guarded one plus framing.
        bundle = self.compiler.compile_search(results, budget=Budget(bytes=1600))
        self.assertTrue(
            any(o.uid == fx.SAFETY_UID for o in bundle.omitted)
            or any(i.uid == fx.SAFETY_UID for i in bundle.included)
        )
        self.assertEqual(len(bundle.candidates), 2)


class TestNonBodyResources(ContextTestCase):
    """Search and route candidates degrade to omissions; explicit refs raise."""

    def _search_bundle(self, uid: str):
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit(uid, rank=1),),
            total_matched=1,
            filters={},
        )
        return self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))

    def test_metadata_only_becomes_an_omission_not_a_body(self) -> None:
        bundle = self._search_bundle(fx.METADATA_ONLY_UID)
        self.assertEqual(bundle.included, ())
        self.assertEqual(bundle.omitted[0].reason, "metadata_only")
        self.assertNotIn(fx.METADATA_ONLY_BODY.decode("utf-8"), bundle.render_markdown())

    def test_a_technique_reports_no_addressable_body(self) -> None:
        bundle = self._search_bundle(fx.TECHNIQUE_UID)
        self.assertEqual(bundle.omitted[0].reason, "no_addressable_body")

    def test_a_tombstone_is_distinguished_from_a_bodiless_resource(self) -> None:
        bundle = self._search_bundle(fx.TOMBSTONE_UID)
        self.assertEqual(bundle.omitted[0].reason, "tombstone")

    def test_an_excluded_resource_reveals_only_policy_safe_identity(self) -> None:
        bundle = self._search_bundle(fx.EXCLUDED_UID)
        omission = bundle.omitted[0]
        self.assertEqual(omission.reason, "excluded")
        self.assertIsNone(omission.title)
        payload = str(bundle.to_json_obj())
        self.assertNotIn("Excluded Fixture", payload)
        self.assertNotIn("fixtures/excluded.md", payload)

    def test_explicit_references_raise_instead_of_omitting(self) -> None:
        cases = [
            (fx.METADATA_ONLY_ID, ContentRefused),
            (fx.TECHNIQUE_ID, NoAddressableContent),
            (fx.TOMBSTONE_ID, NoAddressableContent),
            (fx.EXCLUDED_ID, ResourceExcluded),
            ("prompt:fixtures/no-such-resource", ResourceNotFound),
        ]
        for ref, expected in cases:
            with self.subTest(ref=ref), self.assertRaises(expected):
                self.compile_refs([ref])

    def test_a_body_is_never_substituted_by_metadata(self) -> None:
        with self.assertRaises(ContentRefused):
            self.compile_refs([fx.METADATA_ONLY_ID])


class TestIntegrityAborts(EngineTestCase):
    def test_a_checksum_mismatch_aborts_the_whole_compile(self) -> None:
        """A registry that disagrees with disk cannot produce a trustworthy
        bundle, so this is never downgraded to an omission."""
        root = self.tmp_path("drift")
        path, sha = fx.with_source(root, "fixtures/drift.md", b"# Before\n")
        fx.build_repo(root, [fx.record("pae_0000000000dr", "prompt:fixtures/drift",
                                       path=path, content_sha256=sha)])
        (root / path).write_bytes(b"# After an uncommitted local edit\n")
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit("pae_0000000000dr", rank=1),),
            total_matched=1,
            filters={},
        )
        with self.assertRaises(ChecksumMismatch):
            compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))


class TestSkillAttachmentBoundary(EngineTestCase):
    def test_only_the_skill_body_is_compiled_never_its_attachments(self) -> None:
        root = self.tmp_path("skill")
        body = b"# Skill\n\nSee references/deep.md and scripts/run.sh for detail.\n"
        path, sha = fx.with_source(root, "skills/demo/SKILL.md", body)
        fx.with_source(root, "skills/demo/references/deep.md", b"ATTACHMENT_SENTINEL_DOC\n")
        fx.with_source(root, "skills/demo/scripts/run.sh", b"#!/bin/sh\nATTACHMENT_SENTINEL_SH\n")
        fx.build_repo(
            root,
            [
                fx.record(
                    "pae_0000000000sk",
                    "skill:demo",
                    kind="skill",
                    path=path,
                    content_sha256=sha,
                    relationships={
                        "attachments": [
                            "skills/demo/references/deep.md",
                            "skills/demo/scripts/run.sh",
                        ]
                    },
                )
            ],
        )
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        bundle = compiler.compile_refs(["skill:demo"], budget=Budget(estimated_tokens=BIG))
        markdown = bundle.render_markdown()
        self.assertEqual(bundle.included[0].content, body.decode("utf-8"))
        for sentinel in ("ATTACHMENT_SENTINEL_DOC", "ATTACHMENT_SENTINEL_SH"):
            self.assertNotIn(sentinel, markdown)
            self.assertNotIn(sentinel, str(bundle.to_json_obj()))


# --------------------------------------------------------------------------
# packing
# --------------------------------------------------------------------------


class TestPacking(ContextTestCase):
    def _results(self, *uids):
        hits = tuple(hit(uid, rank=i) for i, uid in enumerate(uids, start=1))
        return SearchResults(
            query="q", normalized_terms=(), hits=hits, total_matched=len(hits), filters={}
        )

    def test_rank_order_is_preserved_by_default(self) -> None:
        results = self._results(fx.STANDARD_UID, fx.SAFETY_UID, fx.RENAMED_UID)
        bundle = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        self.assertEqual([i.source_rank for i in bundle.included], [1, 2, 3])
        self.assertEqual(bundle.ordering, "rank")

    def test_rank_and_score_are_preserved_never_recomputed(self) -> None:
        results = self._results(fx.STANDARD_UID)
        bundle = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.included[0].source_score, 10.0)

    def test_explicit_refs_carry_no_rank_or_score(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID])
        self.assertIsNone(bundle.included[0].source_rank)
        self.assertIsNone(bundle.included[0].source_score)
        self.assertEqual(bundle.ordering, "input")

    def test_max_resources_is_an_inclusion_ceiling_not_a_silent_drop(self) -> None:
        results = self._results(fx.STANDARD_UID, fx.SAFETY_UID, fx.RENAMED_UID)
        bundle = self.compiler.compile_search(
            results, budget=Budget(estimated_tokens=BIG, max_resources=1)
        )
        self.assertEqual(len(bundle.included), 1)
        reasons = [o.reason for o in bundle.omitted]
        self.assertEqual(reasons, ["max_resources", "max_resources"])
        self.assertEqual(len(bundle.candidates), 3)

    def test_an_oversized_candidate_is_skipped_and_packing_continues(self) -> None:
        """Never stop after one non-fitting item."""
        root = self.tmp_path("sizes")
        big_path, big_sha = fx.with_source(root, "fixtures/big.md", b"# Big\n" + b"x" * 4000)
        small_path, small_sha = fx.with_source(root, "fixtures/small.md", b"# Small\n")
        fx.build_repo(
            root,
            [
                fx.record("pae_0000000000bg", "prompt:fixtures/big",
                          path=big_path, content_sha256=big_sha),
                fx.record("pae_0000000000sm", "prompt:fixtures/small",
                          path=small_path, content_sha256=small_sha),
            ],
        )
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit("pae_0000000000bg", rank=1), hit("pae_0000000000sm", rank=2)),
            total_matched=2,
            filters={},
        )
        bundle = compiler.compile_search(results, budget=Budget(bytes=2500))
        self.assertEqual([i.uid for i in bundle.included], ["pae_0000000000sm"])
        self.assertEqual(bundle.omitted[0].uid, "pae_0000000000bg")
        self.assertEqual(bundle.omitted[0].reason, "oversized")

    def test_a_missing_top_hit_is_surfaced_rather_than_left_to_be_noticed(self) -> None:
        root = self.tmp_path("tophit")
        big_path, big_sha = fx.with_source(root, "fixtures/big.md", b"# Big\n" + b"x" * 4000)
        small_path, small_sha = fx.with_source(root, "fixtures/small.md", b"# Small\n")
        fx.build_repo(
            root,
            [
                fx.record("pae_0000000000bg", "prompt:fixtures/big",
                          path=big_path, content_sha256=big_sha),
                fx.record("pae_0000000000sm", "prompt:fixtures/small",
                          path=small_path, content_sha256=small_sha),
            ],
        )
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit("pae_0000000000bg", rank=1), hit("pae_0000000000sm", rank=2)),
            total_matched=2,
            filters={},
        )
        bundle = compiler.compile_search(results, budget=Budget(bytes=2500))
        self.assertIn("top_hit_omitted", bundle.warnings)
        self.assertIn("top_hit_omitted", bundle.render_markdown())

    def test_every_omission_carries_a_reason_from_the_closed_set(self) -> None:
        results = self._results(
            fx.STANDARD_UID, fx.METADATA_ONLY_UID, fx.TECHNIQUE_UID, fx.TOMBSTONE_UID
        )
        bundle = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        self.assertTrue(bundle.omitted)
        for omission in bundle.omitted:
            self.assertIn(omission.reason, OMISSION_REASONS)
            self.assertTrue(omission.detail)

    def test_a_duplicate_reference_keeps_the_first_and_records_the_rest(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID, fx.STANDARD_UID, fx.STANDARD_ID])
        self.assertEqual(len(bundle.included), 1)
        self.assertEqual([o.reason for o in bundle.omitted], ["duplicate", "duplicate"])

    def test_a_canonical_and_its_copy_are_both_kept_when_both_are_named(self) -> None:
        """Two distinct resources the caller asked for by hand, not an accident."""
        root = self.tmp_path("copies")
        can_path, can_sha = fx.with_source(root, "fixtures/canon.md", b"# Canonical\n")
        cp_path, cp_sha = fx.with_source(root, "fixtures/copy.md", b"# Vendored copy\n")
        fx.build_repo(
            root,
            [
                fx.record("pae_0000000000cn", "prompt:fixtures/canon", path=can_path,
                          content_sha256=can_sha,
                          relationships={"copies": ["pae_0000000000cp"]}),
                fx.record("pae_0000000000cp", "prompt:fixtures/copy", path=cp_path,
                          content_sha256=cp_sha,
                          relationships={"copy_of": "pae_0000000000cn"}),
            ],
        )
        compiler = ContextCompiler(Registry.open(Repository.at(root)))
        bundle = compiler.compile_refs(
            ["prompt:fixtures/canon", "prompt:fixtures/copy"],
            budget=Budget(estimated_tokens=BIG),
        )
        self.assertEqual(len(bundle.included), 2)
        self.assertEqual(bundle.included[1].canonical_uid, "pae_0000000000cn")
        self.assertNotEqual(bundle.included[1].canonical_uid, bundle.included[1].uid)


class TestMinimumBudget(ContextTestCase):
    def test_a_budget_too_small_for_the_framing_is_a_usage_error(self) -> None:
        with self.assertRaises(BudgetTooSmall) as caught:
            self.compile_refs([fx.STANDARD_ID], budget=Budget(bytes=200))
        self.assertEqual(caught.exception.exit_code, 2)
        self.assertIn("minimum_bytes", caught.exception.details)

    def test_a_bundle_with_zero_bodies_is_a_valid_result(self) -> None:
        """Distinct from a budget that could never have been answered."""
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit(fx.TECHNIQUE_UID, rank=1),),
            total_matched=1,
            filters={},
        )
        bundle = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.included, ())
        self.assertEqual(len(bundle.omitted), 1)

    def test_a_low_token_budget_warns_without_refusing(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=1000))
        self.assertIn("low_estimated_token_budget", bundle.warnings)
        self.assertTrue(bundle.included)


# --------------------------------------------------------------------------
# route states and ambiguity
# --------------------------------------------------------------------------


class TestRouteStates(ContextTestCase):
    def test_a_weak_route_compiles_and_keeps_its_status(self) -> None:
        d = decision([hit(fx.STANDARD_UID, rank=1)], status="weak",
                     scopes=[("alpha", 3.0, fx.STANDARD_UID)])
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.route_status, "weak")
        self.assertIn("weak_route", bundle.warnings)
        self.assertTrue(bundle.included)

    def test_no_route_returns_a_valid_empty_bundle_with_provenance(self) -> None:
        d = decision([], status="no_route")
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.route_status, "no_route")
        self.assertEqual(bundle.included, ())
        self.assertEqual(bundle.candidates, ())
        self.assertIn("no_route", bundle.render_markdown())

    def test_an_ambiguous_route_is_never_rewritten_as_matched(self) -> None:
        d = decision(
            [hit(fx.STANDARD_UID, rank=1), hit(fx.SAFETY_UID, rank=2, scope="beta")],
            status="ambiguous",
            scopes=[("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.6, fx.SAFETY_UID)],
        )
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.route_status, "ambiguous")
        self.assertIsNone(bundle.selected_scope)
        self.assertIsNone(bundle.selected_kind)
        self.assertIn("ambiguous_route", bundle.warnings)


class TestAmbiguityDiversity(ContextTestCase):
    def _decision(self):
        """rank1 A, rank2 A, rank3 B, rank4 A — the spec's worked example."""
        hits = [
            hit(fx.STANDARD_UID, rank=1, scope="alpha"),
            hit(fx.SAFETY_UID, rank=2, scope="alpha"),
            hit(fx.RENAMED_UID, rank=3, scope="beta"),
            hit(fx.METADATA_ONLY_UID, rank=4, scope="alpha"),
        ]
        return decision(
            hits,
            status="ambiguous",
            scopes=[("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.7, fx.RENAMED_UID)],
        )

    def test_exactly_one_candidate_from_the_other_close_scope_is_promoted(self) -> None:
        bundle = self.compiler.compile_route(
            self._decision(), budget=Budget(estimated_tokens=BIG)
        )
        self.assertEqual(bundle.ordering, "rank+top2-scope-diversity")
        self.assertEqual([i.source_rank for i in bundle.included], [1, 3, 2])
        self.assertEqual([i.scope for i in bundle.included], ["alpha", "beta", "alpha"])

    def test_the_original_rank_is_always_preserved_on_the_item(self) -> None:
        bundle = self.compiler.compile_route(
            self._decision(), budget=Budget(estimated_tokens=BIG)
        )
        self.assertEqual(bundle.included[1].source_rank, 3)

    def test_a_matched_route_keeps_plain_rank_order(self) -> None:
        d = replace(self._decision(), status="matched", selected_scope="alpha")
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.ordering, "rank")
        self.assertEqual([i.source_rank for i in bundle.included], [1, 2, 3])

    def test_there_is_no_round_robin_over_every_scope(self) -> None:
        hits = [
            hit(fx.STANDARD_UID, rank=1, scope="alpha"),
            hit(fx.SAFETY_UID, rank=2, scope="alpha"),
            hit(fx.RENAMED_UID, rank=3, scope="beta"),
            hit(fx.METADATA_ONLY_UID, rank=4, scope="gamma"),
        ]
        d = decision(
            hits,
            status="ambiguous",
            scopes=[("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.7, fx.RENAMED_UID),
                    ("gamma", 8.0, fx.METADATA_ONLY_UID)],
        )
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        # Only the second top-two scope is promoted; gamma stays where it was.
        self.assertEqual([i.source_rank for i in bundle.included], [1, 3, 2])

    def test_diversity_falls_back_and_warns_when_the_other_scope_has_no_resource(self) -> None:
        hits = [hit(fx.STANDARD_UID, rank=1, scope="alpha"),
                hit(fx.SAFETY_UID, rank=2, scope="alpha")]
        d = decision(
            hits,
            status="ambiguous",
            scopes=[("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.7, "pae_absent")],
        )
        bundle = self.compiler.compile_route(d, budget=Budget(estimated_tokens=BIG))
        self.assertEqual(bundle.ordering, "rank")
        self.assertIn("ambiguity_diversity_unavailable", bundle.warnings)


class TestScopeFilter(ContextTestCase):
    def _decision(self):
        hits = [
            hit(fx.STANDARD_UID, rank=1, scope="alpha"),
            hit(fx.RENAMED_UID, rank=2, scope="beta"),
        ]
        return decision(
            hits,
            status="ambiguous",
            scopes=[("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.7, fx.RENAMED_UID)],
        )

    def test_filtered_candidates_become_filtered_omissions(self) -> None:
        bundle = self.compiler.compile_route(
            self._decision(), budget=Budget(estimated_tokens=BIG), scopes=["alpha"]
        )
        self.assertEqual([i.uid for i in bundle.included], [fx.STANDARD_UID])
        self.assertEqual([o.reason for o in bundle.omitted], ["filtered"])
        self.assertEqual(bundle.ordering, "rank+scope-filter")
        self.assertIn("scope_filter_applied", bundle.warnings)

    def test_the_route_status_is_not_rewritten_by_a_filter(self) -> None:
        bundle = self.compiler.compile_route(
            self._decision(), budget=Budget(estimated_tokens=BIG), scopes=["alpha"]
        )
        self.assertEqual(bundle.route_status, "ambiguous")

    def test_a_filter_disables_diversity_promotion(self) -> None:
        bundle = self.compiler.compile_route(
            self._decision(), budget=Budget(estimated_tokens=BIG), scopes=["alpha", "beta"]
        )
        self.assertEqual(bundle.ordering, "rank+scope-filter")

    def test_an_unknown_scope_is_a_usage_error(self) -> None:
        with self.assertRaises(UsageError):
            self.compiler.compile_route(
                self._decision(), budget=Budget(estimated_tokens=BIG), scopes=["delta"]
            )


# --------------------------------------------------------------------------
# rendering, identity and determinism
# --------------------------------------------------------------------------


class TestRendering(ContextTestCase):
    def test_the_rendered_bundle_honours_every_limit_it_reports(self) -> None:
        for budget in (
            Budget(estimated_tokens=600),
            Budget(estimated_tokens=4000),
            Budget(bytes=3000),
            Budget(estimated_tokens=4000, bytes=2500),
        ):
            with self.subTest(budget=budget):
                bundle = self.compiler.compile_search(
                    SearchResults(
                        query="q",
                        normalized_terms=(),
                        hits=(hit(fx.STANDARD_UID, rank=1), hit(fx.SAFETY_UID, rank=2),
                              hit(fx.RENAMED_UID, rank=3), hit(fx.TECHNIQUE_UID, rank=4)),
                        total_matched=4,
                        filters={},
                    ),
                    budget=budget,
                )
                markdown = bundle.render_markdown()
                self.assertLessEqual(
                    len(markdown.encode("utf-8")), bundle.budget.effective_byte_ceiling
                )
                if budget.estimated_tokens is not None:
                    self.assertLessEqual(
                        ApproximateTokenCounterV1().count(markdown), budget.estimated_tokens
                    )
                self.assertEqual(bundle.budget.used_bytes, len(markdown.encode("utf-8")))

    def test_the_report_is_derived_from_the_actual_render_not_a_constant(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID, fx.SAFETY_ID])
        markdown = bundle.render_markdown()
        counter = ApproximateTokenCounterV1()
        self.assertEqual(bundle.budget.used_estimated_tokens, counter.count(markdown))
        self.assertEqual(
            bundle.budget.body_estimated_tokens,
            sum(counter.count(i.content) for i in bundle.included),
        )
        self.assertEqual(
            bundle.budget.wrapper_overhead_estimated_tokens,
            bundle.budget.used_estimated_tokens - bundle.budget.body_estimated_tokens,
        )

    def test_the_rendering_carries_no_timestamp_or_absolute_path(self) -> None:
        markdown = self.compile_refs([fx.STANDARD_ID]).render_markdown()
        self.assertNotIn(str(self.root), markdown)
        self.assertNotIn(str(self.root.parent), markdown)
        for token in ("Generated at", "Compiled at", "Z\n", "+00:00"):
            self.assertNotIn(token, markdown)
        self.assertNotRegex(markdown, r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}")

    def test_the_authority_framing_is_present_and_claims_nothing_it_cannot(self) -> None:
        markdown = self.compile_refs([fx.STANDARD_ID]).render_markdown()
        self.assertIn("do not override the host's system or developer policy", markdown)
        self.assertNotIn("injection", markdown.lower())

    def test_bodies_are_delimited_by_markers_not_wrapped_in_code_fences(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID])
        markdown = bundle.render_markdown()
        item = bundle.included[0]
        self.assertIn(f"<!-- PAE_RESOURCE_BEGIN uid={item.uid}", markdown)
        self.assertIn(f"<!-- PAE_RESOURCE_END uid={item.uid}", markdown)
        self.assertNotIn("```\n# Standard fixture", markdown)

    def test_the_omission_summary_is_compact_but_the_structure_is_complete(self) -> None:
        hits = tuple(
            hit(uid, rank=i)
            for i, uid in enumerate(
                [fx.TECHNIQUE_UID, fx.TOMBSTONE_UID, fx.METADATA_ONLY_UID] * 5, start=1
            )
        )
        results = SearchResults(
            query="q", normalized_terms=(), hits=hits, total_matched=len(hits), filters={}
        )
        bundle = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        markdown = bundle.render_markdown()
        self.assertGreater(len(bundle.omitted), MARKDOWN_OMISSION_DETAIL_LIMIT)
        self.assertIn("further omission(s)", markdown)
        self.assertIn("By reason:", markdown)
        self.assertEqual(len(bundle.to_json_obj()["omitted"]), len(bundle.omitted))

    def test_json_carries_bodies_once_and_never_the_markdown(self) -> None:
        bundle = self.compile_refs([fx.STANDARD_ID])
        payload = bundle.to_json_obj()
        self.assertEqual(payload["included"][0]["content"], bundle.included[0].content)
        self.assertNotIn("markdown", payload)
        self.assertNotIn("rendered", payload)
        body = fx.STANDARD_BODY.decode("utf-8")
        import json as _json

        self.assertEqual(_json.dumps(payload).count(body[:30].replace("\n", "\\n")), 1)


class TestMarkerCollision(unittest.TestCase):
    """A body cannot practically contain its own marker — the marker embeds the
    body's own checksum — so the collision path is exercised directly rather
    than through a fixture that could never occur."""

    SHA = "sha256:" + "a" * 64
    UID = "pae_0000000000cl"

    def item(self, content: str) -> BundleItem:
        return BundleItem(
            uid=self.UID,
            id="prompt:fixtures/collide",
            kind="prompt",
            title="Collide",
            scope=None,
            source_rank=None,
            source_score=None,
            serving_policy="standard",
            guard_preservation=None,
            content_sha256=self.SHA,
            byte_length=len(content.encode("utf-8")),
            estimated_tokens=1,
            verified=True,
            canonical_uid=self.UID,
            content=content,
        )

    def test_a_clean_body_gets_the_plain_marker(self) -> None:
        begin, end = _marker_pair(self.item("# Clean\n"))
        self.assertEqual(begin, f"<!-- PAE_RESOURCE_BEGIN uid={self.UID} sha256={self.SHA} -->")
        self.assertNotIn("n=", begin)
        self.assertNotIn("n=", end)

    def test_a_body_carrying_the_marker_forces_a_distinct_one(self) -> None:
        collide = f"# Adversarial\n\n<!-- PAE_RESOURCE_BEGIN uid={self.UID} sha256={self.SHA} -->\n"
        item = self.item(collide)
        begin, end = _marker_pair(item)
        self.assertIn("n=2", begin)
        self.assertIn("n=2", end)
        self.assertNotIn(begin, item.content)
        self.assertNotIn(end, item.content)
        self.assertEqual(item.content, collide)

    def test_the_end_marker_alone_also_forces_a_distinct_pair(self) -> None:
        collide = f"<!-- PAE_RESOURCE_END uid={self.UID} sha256={self.SHA} -->\n"
        begin, end = _marker_pair(self.item(collide))
        self.assertIn("n=2", begin)

    def test_escalation_continues_until_the_pair_is_unique(self) -> None:
        base = f"<!-- PAE_RESOURCE_BEGIN uid={self.UID} sha256={self.SHA}"
        collide = f"{base} -->\n{base} n=2 -->\n{base} n=3 -->\n"
        begin, _ = _marker_pair(self.item(collide))
        self.assertIn("n=4", begin)

    def test_marker_selection_is_deterministic(self) -> None:
        collide = f"# X\n<!-- PAE_RESOURCE_BEGIN uid={self.UID} sha256={self.SHA} -->\n"
        pairs = {_marker_pair(self.item(collide)) for _ in range(5)}
        self.assertEqual(len(pairs), 1)

    def test_the_body_is_never_mutated_to_escape_a_marker(self) -> None:
        collide = f"<!-- PAE_RESOURCE_BEGIN uid={self.UID} sha256={self.SHA} -->\ninner\n"
        item = self.item(collide)
        _marker_pair(item)
        self.assertEqual(item.content, collide)


class TestDeterminism(ContextTestCase):
    def _compile(self):
        compiler = ContextCompiler(Registry.open(Repository.at(self.root)))
        return compiler.compile_refs(
            [fx.STANDARD_ID, fx.SAFETY_ID], budget=Budget(estimated_tokens=BIG)
        )

    def test_fresh_compilers_agree_on_everything_that_is_observable(self) -> None:
        import json as _json

        one, two = self._compile(), self._compile()
        self.assertEqual(one.bundle_sha256, two.bundle_sha256)
        self.assertEqual(one.render_markdown(), two.render_markdown())
        self.assertEqual(_json.dumps(one.to_json_obj(), sort_keys=True),
                         _json.dumps(two.to_json_obj(), sort_keys=True))
        self.assertEqual(one.budget.to_json_obj(), two.budget.to_json_obj())

    def test_the_checkout_location_does_not_change_the_hash(self) -> None:
        here = self._compile()
        other_root = fx.standard_repo(self.tmp_path("elsewhere"))
        elsewhere = ContextCompiler(Registry.open(Repository.at(other_root))).compile_refs(
            [fx.STANDARD_ID, fx.SAFETY_ID], budget=Budget(estimated_tokens=BIG)
        )
        self.assertEqual(here.bundle_sha256, elsewhere.bundle_sha256)


class TestBundleHash(ContextTestCase):
    def base(self):
        return self.compile_refs([fx.STANDARD_ID, fx.SAFETY_ID])

    def test_selection_order_changes_the_hash(self) -> None:
        a = self.compile_refs([fx.STANDARD_ID, fx.SAFETY_ID])
        b = self.compile_refs([fx.SAFETY_ID, fx.STANDARD_ID])
        self.assertNotEqual(a.bundle_sha256, b.bundle_sha256)

    def test_the_included_set_changes_the_hash(self) -> None:
        self.assertNotEqual(
            self.base().bundle_sha256, self.compile_refs([fx.STANDARD_ID]).bundle_sha256
        )

    def test_the_budget_configuration_changes_the_hash(self) -> None:
        a = self.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG))
        b = self.compile_refs([fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG - 1))
        self.assertNotEqual(a.bundle_sha256, b.bundle_sha256)

    def test_a_changed_source_body_changes_the_hash(self) -> None:
        """Bodies enter the manifest through their checksums."""
        before = self.compile_refs([fx.STANDARD_ID]).bundle_sha256
        root = self.tmp_path("mutated")
        path, sha = fx.with_source(root, "fixtures/standard.md", b"# Different body\n")
        fx.build_repo(root, [fx.record(fx.STANDARD_UID, fx.STANDARD_ID,
                                       path=path, content_sha256=sha)])
        after = ContextCompiler(Registry.open(Repository.at(root))).compile_refs(
            [fx.STANDARD_ID], budget=Budget(estimated_tokens=BIG)
        ).bundle_sha256
        self.assertNotEqual(before, after)

    def test_route_provenance_and_scope_filter_change_the_hash(self) -> None:
        hits = [hit(fx.STANDARD_UID, rank=1, scope="alpha"),
                hit(fx.RENAMED_UID, rank=2, scope="beta")]
        scopes = [("alpha", 9.0, fx.STANDARD_UID), ("beta", 8.7, fx.RENAMED_UID)]
        matched = decision(hits, status="matched", scopes=scopes)
        weak = decision(hits, status="weak", scopes=scopes)
        budget = Budget(estimated_tokens=BIG)
        a = self.compiler.compile_route(matched, budget=budget)
        b = self.compiler.compile_route(weak, budget=budget)
        c = self.compiler.compile_route(matched, budget=budget, scopes=["alpha"])
        self.assertEqual(len({a.bundle_sha256, b.bundle_sha256, c.bundle_sha256}), 3)

    def test_an_omission_reason_changes_the_hash(self) -> None:
        results = SearchResults(
            query="q",
            normalized_terms=(),
            hits=(hit(fx.STANDARD_UID, rank=1), hit(fx.TECHNIQUE_UID, rank=2)),
            total_matched=2,
            filters={},
        )
        with_omission = self.compiler.compile_search(results, budget=Budget(estimated_tokens=BIG))
        without = self.compile_refs([fx.STANDARD_ID])
        self.assertNotEqual(with_omission.bundle_sha256, without.bundle_sha256)

    def test_the_hash_is_a_prefixed_sha256(self) -> None:
        digest = self.base().bundle_sha256
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), len("sha256:") + 64)


if __name__ == "__main__":
    unittest.main()

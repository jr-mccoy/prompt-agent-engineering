"""Condition isolation. Every check here must fail closed.

These are the tests that decide whether a result means anything. If Condition B
can reach the gold labels, or Condition A quietly receives context, the numbers
are measuring the harness rather than the product — and unlike a statistical
mistake, that failure is invisible in the output.
"""

from __future__ import annotations

import unittest

from _support import TempDirCase, load_mini_benchmark

from pae_eval.conditions import (
    ConditionContext,
    assert_condition_isolation,
    assert_prompt_fairness,
    build_condition_a,
    build_condition_b,
    build_condition_c,
    render_system_prompt,
)
from pae_eval.errors import IsolationError
from pae_eval.isolation import gold_markers_for, scan_request, serialize_request
from pae_eval.providers.base import Message, ModelRequest, ToolSpec
from pae_eval.raw_repo import RawRepoTools


class _FakeBundle:
    markdown = "## Reference\nSome corpus body text about readiness."

    def to_json_obj(self):
        return {"bundle_sha256": "sha256:test", "included": [], "omitted": [],
                "budget": {}, "warnings": [], "route_status": "matched",
                "selected_scope": "software-engineering", "selected_kind": "prompt",
                "coverage": 0.5, "margin": 0.2, "candidates": []}


class TestConditionStructure(TempDirCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path("snap")
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "a.md").write_text("hello", encoding="utf-8")
        self.raw = RawRepoTools(self.root, require_ripgrep=False, files=("a.md",))
        self.common = dict(model="m", task_query="do the thing",
                           deliverable="a note", max_output_tokens=1000)

    def test_condition_a_has_no_tools_and_no_context(self) -> None:
        context = build_condition_a(**self.common)
        assert_condition_isolation(context)
        self.assertEqual(context.tools, ())
        self.assertIsNone(context.dispatcher)

    def test_condition_a_with_a_tool_is_refused(self) -> None:
        context = build_condition_a(**self.common)
        tampered = ConditionContext(
            condition="A", request=context.request,
            tools=(ToolSpec("x", "d", {}),), dispatcher=lambda *a: None,
        )
        with self.assertRaises(IsolationError):
            assert_condition_isolation(tampered)

    def test_condition_b_exposes_exactly_the_three_generic_tools(self) -> None:
        context = build_condition_b(raw_tools=self.raw, **self.common)
        assert_condition_isolation(context)
        self.assertEqual(
            sorted(s.name for s in context.tools),
            ["repo_list", "repo_read", "repo_search"],
        )

    def test_condition_b_must_not_receive_a_bundle(self) -> None:
        context = build_condition_b(raw_tools=self.raw, **self.common)
        tampered = ConditionContext(
            condition="B", request=context.request, tools=context.tools,
            dispatcher=context.dispatcher, bundle={"bundle_sha256": "x"},
        )
        with self.assertRaises(IsolationError):
            assert_condition_isolation(tampered)

    def test_condition_b_prompt_never_mentions_pae(self) -> None:
        context = build_condition_b(raw_tools=self.raw, **self.common)
        payload = serialize_request(context.request)
        for marker in ("pae_search_resources", "pae_route_task", "PAE Registry",
                       "ContextBundle"):
            self.assertNotIn(marker, payload)

    def test_condition_c_injects_context_and_has_no_tools(self) -> None:
        context = build_condition_c(bundle_result=_FakeBundle(), **self.common)
        assert_condition_isolation(context)
        self.assertEqual(context.tools, ())
        self.assertIn("Reference material follows", serialize_request(context.request))

    def test_condition_d_must_not_be_handed_a_bundle(self) -> None:
        context = build_condition_c(bundle_result=_FakeBundle(), **self.common)
        tampered = ConditionContext(
            condition="D", request=context.request,
            tools=(ToolSpec("pae_search_resources", "d", {}),
                   ToolSpec("pae_route_task", "d", {}),
                   ToolSpec("pae_get_resource", "d", {}),
                   ToolSpec("pae_compose_bundle", "d", {})),
            dispatcher=lambda *a: None, bundle={"bundle_sha256": "x"},
        )
        with self.assertRaises(IsolationError) as caught:
            assert_condition_isolation(tampered)
        self.assertIn("precompiled bundle", str(caught.exception))

    def test_condition_d_requires_exactly_the_four_tools(self) -> None:
        request = build_condition_a(**self.common).request
        tampered = ConditionContext(
            condition="D", request=request,
            tools=(ToolSpec("pae_search_resources", "d", {}),),
            dispatcher=lambda *a: None,
        )
        with self.assertRaises(IsolationError):
            assert_condition_isolation(tampered)

    def test_mcp_catalog_mismatch_is_refused(self) -> None:
        request = build_condition_a(**self.common).request
        names = ("pae_search_resources", "pae_route_task",
                 "pae_get_resource", "pae_compose_bundle")
        context = ConditionContext(
            condition="D", request=request,
            tools=tuple(ToolSpec(n, "d", {}) for n in names),
            dispatcher=lambda *a: None,
            observability={"mcp": {"tool_catalog_sha256": "sha256:actual"}},
        )
        with self.assertRaises(IsolationError) as caught:
            assert_condition_isolation(context, expected_mcp_catalog="sha256:frozen")
        self.assertIn("does not match the frozen plan", str(caught.exception))


class TestPromptFairness(TempDirCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path("snap")
        self.root.mkdir(parents=True, exist_ok=True)
        self.raw = RawRepoTools(self.root, require_ripgrep=False, files=())
        self.common = dict(model="m", task_query="q", deliverable="d",
                           max_output_tokens=1000)

    def test_tooled_conditions_share_one_prompt(self) -> None:
        b = build_condition_b(raw_tools=self.raw, **self.common)
        # A hand-built D with the same shape must use the identical prompt.
        self.assertEqual(b.request.system, render_system_prompt(has_tools=True))

    def test_bare_conditions_share_one_prompt(self) -> None:
        a = build_condition_a(**self.common)
        c = build_condition_c(bundle_result=_FakeBundle(), **self.common)
        self.assertEqual(a.request.system, c.request.system)
        assert_prompt_fairness([a, c])

    def test_a_special_pae_prompt_is_refused(self) -> None:
        a = build_condition_a(**self.common)
        tampered = ConditionContext(
            condition="C",
            request=ModelRequest(
                model="m",
                system=a.request.system + "\nRemember to use the PAE tools well.",
                messages=a.request.messages,
            ),
            bundle={"bundle_sha256": "x"},
        )
        with self.assertRaises(IsolationError) as caught:
            assert_prompt_fairness([a, tampered])
        self.assertIn("system prompt", str(caught.exception))


class TestGoldMarkerScan(unittest.TestCase):
    def setUp(self) -> None:
        self.benchmark = load_mini_benchmark()
        self.task = self.benchmark.tasks[0]

    def test_generic_vocabulary_is_not_treated_as_a_secret(self) -> None:
        """A scope name is a directory, not an answer key.

        Treating it as one produced constant false positives on Condition C,
        whose injected corpus bodies naturally contain their own scope name.
        """
        markers = gold_markers_for(self.task)
        self.assertNotIn("software-engineering", markers)
        self.assertNotIn("weak", markers)
        self.assertNotIn("matched", markers)

    def test_label_field_names_are_treated_as_secrets(self) -> None:
        markers = gold_markers_for(self.task)
        self.assertIn("acceptable_resource_uids", markers)
        self.assertIn("label_rationale", markers)

    def test_a_leaked_label_is_caught(self) -> None:
        request = ModelRequest(
            model="m", system="s",
            messages=(Message(
                role="user",
                content="Here is the acceptable_resource_uids list you should hit.",
            ),),
        )
        context = ConditionContext(condition="A", request=request)
        checks = scan_request(context, self.task)
        failed = [c for c in checks if not c.passed]
        self.assertTrue(failed, "a leaked label field name must be caught")

    def test_a_clean_request_passes(self) -> None:
        request = ModelRequest(
            model="m", system="s",
            messages=(Message(role="user", content="Draft a readiness note."),),
        )
        context = ConditionContext(condition="A", request=request)
        self.assertTrue(all(c.passed for c in scan_request(context, self.task)))

    def test_a_condition_label_in_the_prompt_is_caught(self) -> None:
        request = ModelRequest(
            model="m", system="You are running in condition B.",
            messages=(Message(role="user", content="Do the thing."),),
        )
        context = ConditionContext(condition="B", request=request)
        failed = [c for c in scan_request(context, self.task) if not c.passed]
        self.assertTrue(any("name a condition" in c.name for c in failed))


class TestBenchmarkContainment(TempDirCase):
    def test_benchmark_inside_the_snapshot_is_refused(self) -> None:
        from pae_eval.snapshot import assert_benchmark_outside

        snapshot = self.tmp_path("snap")
        snapshot.mkdir(parents=True, exist_ok=True)
        inside = snapshot / "benchmark"
        inside.mkdir(parents=True, exist_ok=True)
        with self.assertRaises(IsolationError):
            assert_benchmark_outside(inside, snapshot)

    def test_benchmark_outside_is_allowed(self) -> None:
        from pae_eval.snapshot import assert_benchmark_outside

        snapshot = self.tmp_path("snap")
        snapshot.mkdir(parents=True, exist_ok=True)
        outside = self.tmp_path("bench")
        outside.mkdir(parents=True, exist_ok=True)
        assert_benchmark_outside(outside, snapshot)  # must not raise

    def test_a_symlinked_benchmark_cannot_alias_inside(self) -> None:
        from pae_eval.snapshot import assert_benchmark_outside

        snapshot = self.tmp_path("snap")
        snapshot.mkdir(parents=True, exist_ok=True)
        real = snapshot / "hidden-bench"
        real.mkdir(parents=True, exist_ok=True)
        link = self.tmp_path("link-bench")
        try:
            link.symlink_to(real, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable on this platform/account")
        # Resolution, not string comparison, is what catches this.
        with self.assertRaises(IsolationError):
            assert_benchmark_outside(link, snapshot)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

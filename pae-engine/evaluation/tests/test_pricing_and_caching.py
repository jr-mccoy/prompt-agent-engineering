"""The paid path: prompt caching, token accounting, and the pre-flight gates.

Everything here guards the same thing — that money is spent on a number worth
having. Caching is the optimization that made the run affordable, and it is
tested from two directions at once:

* **it must not change the prompt.** A cached request and an uncached one have
  to differ only in metadata. If enabling caching altered a single token the
  model sees, it would stop being a billing optimization and become an
  experimental variable — silently, and in a way no analysis would surface.
* **it must not make the run look cheaper than it was.** The two providers
  disagree about whether ``input_tokens`` includes the cached part, and getting
  that backwards double-counts or under-counts every cached call. The
  arithmetic is therefore pinned to hand-computed numbers rather than to
  whatever the code currently returns.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from pae_eval.pricing import (
    ModelPrice,
    PricingSnapshot,
    cost_usd,
    estimate_trial_cost,
    example_snapshot,
)
from pae_eval.providers.anthropic_adapter import AnthropicAdapter
from pae_eval.providers.anthropic_adapter import _usage as anthropic_usage
from pae_eval.providers.base import Message, ModelRequest, ToolSpec, Usage
from pae_eval.providers.openai_adapter import _usage as openai_usage

OPUS = ModelPrice(
    provider="anthropic", model="claude-opus-5",
    input_per_million=5.0, cached_input_per_million=0.5,
    cache_write_per_million=6.25, output_per_million=25.0,
)

TOOLS = (
    ToolSpec("repo_search", "search", {"type": "object", "properties": {}}),
    ToolSpec("repo_read", "read", {"type": "object", "properties": {}}),
)


class RecordingClient:
    """Stands in for ``anthropic.Anthropic()`` and keeps the payload."""

    def __init__(self) -> None:
        self.payloads: list[dict] = []
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **payload):
        self.payloads.append(payload)
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text="done")],
            stop_reason="end_turn",
            usage=SimpleNamespace(input_tokens=10, output_tokens=5),
            id="msg_1", model="claude-opus-5",
        )


def send(*, cache_prompts=True, tools=TOOLS, turns=1, system="you are a participant"):
    client = RecordingClient()
    adapter = AnthropicAdapter(client=client, cache_prompts=cache_prompts)
    messages = [Message(role="user", content="do the thing")]
    for i in range(turns - 1):
        messages.append(Message(role="assistant", content=f"step {i}"))
    adapter.complete(ModelRequest(
        model="claude-opus-5", system=system, messages=tuple(messages),
        tools=tuple(tools), max_output_tokens=6000,
    ))
    return client.payloads[-1]


# --------------------------------------------------------------------------
# what caching puts on the wire
# --------------------------------------------------------------------------


class TestCacheBreakpoints(unittest.TestCase):
    def test_system_carries_a_breakpoint(self):
        payload = send()
        self.assertEqual(payload["system"], [{
            "type": "text",
            "text": "you are a participant",
            "cache_control": {"type": "ephemeral"},
        }])

    def test_only_the_last_tool_carries_a_breakpoint(self):
        tools = send()["tools"]
        self.assertNotIn("cache_control", tools[0])
        self.assertEqual(tools[-1]["cache_control"], {"type": "ephemeral"})

    def test_automatic_caching_engages_once_there_is_a_conversation(self):
        # Mid-loop the API should manage the rolling breakpoint...
        self.assertEqual(send(turns=3)["cache_control"], {"type": "ephemeral"})
        # ...but a single-call trial would only pay for a write nobody reads.
        self.assertNotIn("cache_control", send(turns=1))

    def test_no_breakpoint_is_placed_inside_the_conversation(self):
        # The rolling breakpoint is the API's job. Hand-placing one here would
        # compete with automatic caching for the same slot.
        for message in send(turns=4)["messages"]:
            for block in message["content"]:
                self.assertNotIn("cache_control", block)

    def test_the_1_hour_ttl_is_never_requested(self):
        # 2x base input on writes instead of 1.25x, and nothing asked for it.
        payload = send(turns=3)
        markers = [payload["cache_control"], payload["tools"][-1]["cache_control"]]
        markers.append(payload["system"][0]["cache_control"])
        for marker in markers:
            self.assertNotIn("ttl", marker)

    def test_disabling_caching_restores_the_plain_shape(self):
        payload = send(cache_prompts=False, turns=3)
        self.assertEqual(payload["system"], "you are a participant")
        self.assertNotIn("cache_control", payload)
        for tool in payload["tools"]:
            self.assertNotIn("cache_control", tool)

    def test_caching_changes_no_token_the_model_sees(self):
        """The whole safety argument for enabling this by default."""
        cached = send(cache_prompts=True, turns=4)
        plain = send(cache_prompts=False, turns=4)

        self.assertEqual(cached["messages"], plain["messages"])
        self.assertEqual(cached["max_tokens"], plain["max_tokens"])
        self.assertEqual(cached["model"], plain["model"])
        # Same system text, same tools, same order — only metadata differs.
        self.assertEqual(cached["system"][0]["text"], plain["system"])
        self.assertEqual(
            [{k: v for k, v in t.items() if k != "cache_control"}
             for t in cached["tools"]],
            plain["tools"],
        )

    def test_a_toolless_request_still_caches_the_system_prompt(self):
        payload = send(tools=())
        self.assertNotIn("tools", payload)
        self.assertIn("cache_control", payload["system"][0])

    def test_describe_records_whether_caching_was_requested(self):
        on = AnthropicAdapter(client=RecordingClient(), cache_prompts=True).describe()
        off = AnthropicAdapter(client=RecordingClient(), cache_prompts=False).describe()
        self.assertTrue(on["prompt_caching"])
        self.assertEqual(on["prompt_cache_ttl"], "5m")
        self.assertFalse(off["prompt_caching"])
        self.assertIsNone(off["prompt_cache_ttl"])


# --------------------------------------------------------------------------
# normalizing two providers that disagree
# --------------------------------------------------------------------------


class TestUsageNormalization(unittest.TestCase):
    def test_anthropic_buckets_pass_through_disjoint(self):
        usage = anthropic_usage(SimpleNamespace(
            input_tokens=50, output_tokens=900,
            cache_read_input_tokens=100_000, cache_creation_input_tokens=7_000,
        ))
        # Anthropic already reports the three as a partition; nothing to adjust.
        self.assertEqual(usage.input_tokens, 50)
        self.assertEqual(usage.cache_read_tokens, 100_000)
        self.assertEqual(usage.cache_write_tokens, 7_000)

    def test_openai_details_are_read_and_subtracted_out(self):
        usage = openai_usage(SimpleNamespace(
            input_tokens=10_000, output_tokens=500,
            input_tokens_details=SimpleNamespace(
                cached_tokens=8_000, cache_write_tokens=1_500,
            ),
        ))
        # The documented arithmetic: ordinary = total - cached - written.
        self.assertEqual(usage.input_tokens, 500)
        self.assertEqual(usage.cache_read_tokens, 8_000)
        self.assertEqual(usage.cache_write_tokens, 1_500)
        self.assertEqual(
            usage.input_tokens + usage.cache_read_tokens
            + usage.cache_write_tokens, 10_000,
        )

    def test_openai_cache_counters_are_not_at_the_top_level(self):
        """The bug this file exists to prevent coming back.

        Reading the counters off ``usage`` instead of ``input_tokens_details``
        returns None forever — no error, and every cached token billed at the
        full rate.
        """
        usage = openai_usage(SimpleNamespace(
            input_tokens=10_000, output_tokens=500,
            input_tokens_details=SimpleNamespace(
                cached_tokens=9_000, cache_write_tokens=None,
            ),
        ))
        self.assertEqual(usage.cache_read_tokens, 9_000)
        self.assertIn("cached_tokens", usage.provenance)

    def test_missing_details_leave_the_total_alone(self):
        usage = openai_usage(SimpleNamespace(input_tokens=700, output_tokens=20))
        self.assertEqual(usage.input_tokens, 700)
        self.assertIsNone(usage.cache_read_tokens)
        self.assertIsNone(usage.cache_write_tokens)

    def test_not_reported_stays_distinct_from_zero(self):
        usage = openai_usage(SimpleNamespace(input_tokens=700, output_tokens=20))
        self.assertNotIn("cached_tokens", usage.provenance)


# --------------------------------------------------------------------------
# money
# --------------------------------------------------------------------------


class TestCostAccounting(unittest.TestCase):
    def test_the_three_buckets_are_added_not_subtracted(self):
        usage = Usage(input_tokens=1_000, output_tokens=2_000,
                      cache_read_tokens=100_000, cache_write_tokens=10_000)
        expected = (
            1_000 * 5.0 + 100_000 * 0.5 + 10_000 * 6.25 + 2_000 * 25.0
        ) / 1_000_000
        self.assertAlmostEqual(cost_usd(usage, OPUS), round(expected, 6))

    def test_cache_writes_cost_more_than_plain_input(self):
        write = cost_usd(Usage(cache_write_tokens=1_000_000), OPUS)
        plain = cost_usd(Usage(input_tokens=1_000_000), OPUS)
        self.assertGreater(write, plain)
        self.assertAlmostEqual(write / plain, 1.25)

    def test_cache_reads_cost_a_tenth_of_plain_input(self):
        read = cost_usd(Usage(cache_read_tokens=1_000_000), OPUS)
        plain = cost_usd(Usage(input_tokens=1_000_000), OPUS)
        self.assertAlmostEqual(read / plain, 0.1)

    def test_an_unpriced_cache_bucket_falls_back_to_full_input(self):
        # Wrong, but wrong in the safe direction, and never silently free.
        bare = ModelPrice(provider="x", model="y", input_per_million=5.0,
                          output_per_million=25.0)
        usage = Usage(cache_read_tokens=1_000, cache_write_tokens=1_000)
        self.assertAlmostEqual(cost_usd(usage, bare), 2_000 * 5.0 / 1_000_000)

    def test_cache_write_rate_round_trips_through_json(self):
        restored = ModelPrice.from_json_obj(OPUS.to_json_obj())
        self.assertEqual(restored.cache_write_per_million, 6.25)
        self.assertEqual(restored, OPUS)

    def test_a_snapshot_without_the_field_still_loads(self):
        obj = OPUS.to_json_obj()
        del obj["cache_write_per_million"]
        self.assertIsNone(ModelPrice.from_json_obj(obj).cache_write_per_million)


class TestTrialEstimates(unittest.TestCase):
    SHAPE = dict(expected_input_tokens=3000, max_output_tokens=6000, tool_turns=10)

    def test_the_uncached_estimate_is_unchanged(self):
        """Pinned, because the cost guard is checked against this number.

        11 turns resending a 3k delta bounds the input at 3000*66 = 198k, and
        the output at one full 6k answer plus ten 200-token tool calls.
        """
        self.assertAlmostEqual(
            estimate_trial_cost(OPUS, **self.SHAPE),
            (198_000 * 5.0 + 8_000 * 25.0) / 1_000_000,
        )

    def test_the_cached_estimate_re_prices_the_same_tokens(self):
        # 11 writes of the delta, and n(n-1)/2 = 55 deltas read back.
        self.assertAlmostEqual(
            estimate_trial_cost(OPUS, **self.SHAPE, cache_reads=True),
            (33_000 * 6.25 + 165_000 * 0.5 + 8_000 * 25.0) / 1_000_000,
        )

    def test_caching_is_the_cheaper_of_the_two(self):
        plain = estimate_trial_cost(OPUS, **self.SHAPE)
        cached = estimate_trial_cost(OPUS, **self.SHAPE, cache_reads=True)
        self.assertLess(cached, plain)
        # Worth doing at all: better than a third off the trial.
        self.assertLess(cached / plain, 0.67)

    def test_the_guard_default_assumes_no_cache_hits(self):
        """A ceiling that assumes hits is not a ceiling.

        Every cache entry can expire between turns. The default must therefore
        be the pessimistic figure, or a run walks past the limit it was given.
        """
        self.assertEqual(
            estimate_trial_cost(OPUS, **self.SHAPE),
            estimate_trial_cost(OPUS, **self.SHAPE, cache_reads=False),
        )

    def test_a_single_call_trial_gains_nothing_from_the_flag(self):
        shape = dict(expected_input_tokens=3000, max_output_tokens=6000)
        plain = estimate_trial_cost(OPUS, **shape)
        cached = estimate_trial_cost(OPUS, **shape, cache_reads=True)
        # One turn: the whole prompt is a write, so caching cannot help within
        # the trial. It helps across trials, which this function does not model.
        self.assertGreaterEqual(cached, plain)


class TestCachingDoesNotMoveAReportedNumber(unittest.TestCase):
    """`total_tokens` is a reported endpoint. It must measure work, not caching.

    The efficiency claim is a function of `total_tokens` for the two conditions
    in the primary comparison. Since the three input buckets are disjoint,
    counting only `input_tokens` would make identical work report fewer tokens
    once caching is on — and by a *different* amount per condition, because the
    conditions differ in how much of their prompt is cacheable. Condition B's
    long agentic loops cache their transcript heavily; Condition D's short ones
    do not. That is enough to move, and conceivably to reverse, the sign of the
    efficiency claim, from a change that is supposed to be billing-only.

    So the invariant is asserted directly: same work, same total, either way.
    """

    # 101,000 tokens of work, reported two ways.
    UNCACHED = Usage(input_tokens=100_000, output_tokens=1_000)
    CACHED = Usage(input_tokens=50, cache_read_tokens=92_000,
                   cache_write_tokens=7_950, output_tokens=1_000)

    def test_usage_total_is_caching_invariant(self):
        self.assertEqual(self.UNCACHED.total_tokens, 101_000)
        self.assertEqual(self.CACHED.total_tokens, 101_000)

    def test_the_cost_of_the_same_work_does_differ(self):
        # The whole point: identical work, identical token total, cheaper bill.
        self.assertLess(cost_usd(self.CACHED, OPUS), cost_usd(self.UNCACHED, OPUS))

    def test_the_efficiency_endpoint_is_caching_invariant(self):
        from pae_eval.analysis import efficiency_by_condition

        rows = [
            {"trial_id": "t1", "condition": "D", "state": "completed",
             "usage": self.UNCACHED.to_json_obj()},
            {"trial_id": "t2", "condition": "B", "state": "completed",
             "usage": self.CACHED.to_json_obj()},
        ]
        efficiency = efficiency_by_condition(rows)
        self.assertEqual(efficiency["D"]["total_tokens"],
                         efficiency["B"]["total_tokens"])

    def test_all_reported_tokens_are_still_visible_separately(self):
        from pae_eval.analysis import efficiency_by_condition

        rows = [{"trial_id": "t1", "condition": "B", "state": "completed",
                 "usage": self.CACHED.to_json_obj()}]
        row = efficiency_by_condition(rows)["B"]
        # The breakdown survives, so a reader can see how much was cached
        # rather than having to infer it.
        self.assertEqual(row["cached_input_tokens"], 92_000)
        self.assertEqual(row["cache_write_tokens"], 7_950)
        self.assertEqual(row["input_tokens"], 50)

    def test_a_provider_reporting_nothing_still_yields_none(self):
        self.assertIsNone(Usage().total_tokens)


class TestExampleSnapshot(unittest.TestCase):
    def test_every_entry_prices_both_cache_buckets(self):
        for price in example_snapshot().prices:
            with self.subTest(model=price.model):
                self.assertIsNotNone(price.cached_input_per_million)
                self.assertIsNotNone(price.cache_write_per_million)

    def test_cache_multipliers_match_the_published_ratios(self):
        for price in example_snapshot().prices:
            if not price.input_per_million:
                continue  # the free fake provider
            with self.subTest(model=price.model):
                self.assertAlmostEqual(
                    price.cache_write_per_million / price.input_per_million, 1.25)
                self.assertAlmostEqual(
                    price.cached_input_per_million / price.input_per_million, 0.1)

    def test_it_still_says_it_is_an_example(self):
        # A sealed run must pin its own snapshot; this one must never pass for
        # one that was retrieved at freeze time.
        self.assertIn("EXAMPLE ONLY", example_snapshot().notes)

    def test_the_plan_default_models_are_all_priced(self):
        snapshot = example_snapshot()
        for provider, model in (("anthropic", "claude-opus-5"),
                                ("openai", "gpt-5.6-terra")):
            with self.subTest(model=model):
                self.assertIsNotNone(snapshot.get(provider, model))

    def test_the_shipped_example_file_matches_the_code(self):
        import json
        from pathlib import Path

        path = (Path(__file__).resolve().parents[1]
                / "examples" / "pricing-snapshot.example.json")
        on_disk = PricingSnapshot.from_json_obj(
            json.loads(path.read_text(encoding="utf-8")))
        self.assertEqual(on_disk.sha256, example_snapshot().sha256)


class TestSealedRunRequiresRipgrep(unittest.TestCase):
    """Condition B is ripgrep-backed search, so a sealed run needs the binary.

    Without it, `RawRepoTools` still constructs when `require_ripgrep` is off
    and only fails when the participant first calls `repo_search` — partway
    into a paid run, on the baseline half of the primary comparison. Opting out
    is a development convenience; in sealed mode it is only a way to find the
    problem expensively.
    """

    def setUp(self):
        from dataclasses import replace

        from pae_eval.plan import example_plan

        self.replace = replace
        self.plan = example_plan()

    def test_sealed_mode_overrides_an_opt_out(self):
        from pae_eval.runner import _sealed_requires_ripgrep

        sealed = self.replace(self.plan, mode="sealed")
        self.assertTrue(_sealed_requires_ripgrep(sealed, False))

    def test_development_mode_respects_the_opt_out(self):
        from pae_eval.runner import _sealed_requires_ripgrep

        development = self.replace(self.plan, mode="development")
        self.assertFalse(_sealed_requires_ripgrep(development, False))

    def test_a_sealed_plan_without_condition_b_does_not_need_it(self):
        from pae_eval.runner import _sealed_requires_ripgrep

        sealed = self.replace(self.plan, mode="sealed", conditions=("A", "C", "D"),
                              primary_comparison=("D", "C"))
        self.assertFalse(_sealed_requires_ripgrep(sealed, False))

    def test_an_explicit_request_is_never_downgraded(self):
        from pae_eval.runner import _sealed_requires_ripgrep

        development = self.replace(self.plan, mode="development")
        self.assertTrue(_sealed_requires_ripgrep(development, True))


if __name__ == "__main__":
    unittest.main()

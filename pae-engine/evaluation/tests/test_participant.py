"""The host loop, and the retry-versus-outcome boundary.

The single most consequential rule in the harness lives here: infrastructure
failures may be retried, model behaviour may not. Retrying a refusal until the
model complies would silently select for agreeable samples and bias the arm,
which is a bias that never shows up in the output. So it is tested directly,
in both directions.
"""

from __future__ import annotations

import unittest

from _support import TempDirCase

from pae_eval.participant import (
    HostLoop,
    LoopLimits,
    RetryPolicy,
    ToolExecution,
)
from pae_eval.providers.base import Message, ModelRequest, ToolSpec
from pae_eval.providers.fake import (
    FakeAdapter,
    empty_step,
    invalid_tool_step,
    rate_limited_step,
    refusal_step,
    scripted,
    server_error_step,
    text_step,
    timeout_step,
    tool_step,
)

TOOL = ToolSpec("repo_read", "read a file",
                {"type": "object", "properties": {"path": {"type": "string"}}})


def request(tools=()) -> ModelRequest:
    return ModelRequest(
        model="fake-model-1", system="system",
        messages=(Message(role="user", content="do the thing"),),
        tools=tuple(tools), max_output_tokens=1000,
    )


def loop(adapter, **kw) -> HostLoop:
    return HostLoop(adapter, sleep=lambda _s: None, **kw)


class TestPlainCompletion(unittest.TestCase):
    def test_a_simple_answer_completes(self) -> None:
        result = loop(scripted(text_step("Summary\n\nthe answer"))).run(request())
        self.assertTrue(result.ok)
        self.assertIn("the answer", result.final_answer)
        self.assertEqual(result.turns, 0)

    def test_usage_is_accumulated(self) -> None:
        adapter = scripted(
            tool_step("repo_read", {"path": "a.md"}, input_tokens=100, output_tokens=10),
            text_step("Summary done", input_tokens=200, output_tokens=20),
        )
        result = loop(adapter).run(
            request([TOOL]),
            dispatcher=lambda n, a: ToolExecution("file body"),
            tools=[TOOL],
        )
        self.assertEqual(result.usage.input_tokens, 300)
        self.assertEqual(result.usage.output_tokens, 30)


class TestRetryBoundary(unittest.TestCase):
    """Infrastructure retries; model behaviour does not."""

    def test_rate_limit_is_retried_then_succeeds(self) -> None:
        adapter = scripted(rate_limited_step(), rate_limited_step(),
                           text_step("Summary recovered"))
        result = loop(adapter).run(request())
        self.assertTrue(result.ok)
        self.assertEqual(len(result.attempts), 3)
        self.assertEqual(
            [a.error_class for a in result.attempts],
            ["rate_limited", "rate_limited", None],
        )

    def test_server_error_is_retried(self) -> None:
        adapter = scripted(server_error_step(), text_step("Summary recovered"))
        self.assertTrue(loop(adapter).run(request()).ok)

    def test_exhausted_infrastructure_retries_is_recorded_not_hidden(self) -> None:
        adapter = scripted(rate_limited_step(), rate_limited_step(),
                           rate_limited_step())
        result = loop(adapter).run(request())
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "infrastructure_failed")
        self.assertEqual(len(result.attempts), 3)

    def test_a_refusal_is_never_retried(self) -> None:
        adapter = scripted(refusal_step(), text_step("Summary would have passed"))
        result = loop(adapter).run(request())
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "refusal")
        # The second step must remain unconsumed: retrying here would select
        # for compliant samples.
        self.assertEqual(adapter.call_count, 1)

    def test_a_behavioural_timeout_is_never_retried(self) -> None:
        adapter = scripted(timeout_step(), text_step("Summary would have passed"))
        result = loop(adapter).run(request())
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "behavioural_timeout")
        self.assertEqual(adapter.call_count, 1)

    def test_an_empty_answer_is_an_outcome(self) -> None:
        result = loop(scripted(empty_step())).run(request())
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "empty_answer")

    def test_retry_after_is_honoured(self) -> None:
        delays: list[float] = []
        adapter = scripted(rate_limited_step(retry_after_s=7.0),
                           text_step("Summary ok"))
        HostLoop(adapter, sleep=delays.append,
                 retry=RetryPolicy(jitter=False)).run(request())
        self.assertEqual(delays, [7.0])

    def test_backoff_grows_without_retry_after(self) -> None:
        delays: list[float] = []
        adapter = scripted(server_error_step(), server_error_step(),
                           text_step("Summary ok"))
        HostLoop(adapter, sleep=delays.append,
                 retry=RetryPolicy(jitter=False, base_delay_s=1.0)).run(request())
        self.assertEqual(len(delays), 2)
        self.assertGreater(delays[1], delays[0])


class TestToolLoop(unittest.TestCase):
    def test_a_tool_call_is_dispatched_and_fed_back(self) -> None:
        seen: list[tuple[str, dict]] = []

        def dispatcher(name, arguments):
            seen.append((name, dict(arguments)))
            return ToolExecution("the file body")

        adapter = scripted(tool_step("repo_read", {"path": "a.md"}),
                           text_step("Summary based on the file"))
        result = loop(adapter).run(request([TOOL]), dispatcher=dispatcher, tools=[TOOL])
        self.assertTrue(result.ok)
        self.assertEqual(seen, [("repo_read", {"path": "a.md"})])
        self.assertEqual(len(result.tool_calls), 1)

    def test_an_unknown_tool_is_reported_back_not_fatal(self) -> None:
        adapter = scripted(invalid_tool_step("no_such_tool"),
                           text_step("Summary recovered"))
        result = loop(adapter).run(
            request([TOOL]), dispatcher=lambda n, a: ToolExecution("x"), tools=[TOOL])
        self.assertTrue(result.ok)
        self.assertEqual(result.tool_calls[0]["status"], "error")
        self.assertEqual(result.tool_calls[0]["reason"], "unknown_tool")

    def test_a_raising_tool_does_not_take_down_the_loop(self) -> None:
        def explode(name, arguments):
            raise RuntimeError("tool blew up")

        adapter = scripted(tool_step("repo_read", {"path": "a.md"}),
                           text_step("Summary recovered"))
        result = loop(adapter).run(request([TOOL]), dispatcher=explode, tools=[TOOL])
        self.assertTrue(result.ok)
        self.assertEqual(result.tool_calls[0]["status"], "error")

    def test_turn_budget_is_enforced(self) -> None:
        steps = [tool_step("repo_read", {"path": "a.md"}, call_id=f"c{n}")
                 for n in range(10)]
        adapter = scripted(*steps)
        result = HostLoop(adapter, sleep=lambda _s: None,
                          limits=LoopLimits(max_tool_turns=3)).run(
            request([TOOL]), dispatcher=lambda n, a: ToolExecution("x"), tools=[TOOL])
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "turn_budget_exhausted")

    def test_a_tool_call_in_a_toolless_condition_is_an_outcome(self) -> None:
        adapter = scripted(tool_step("repo_read", {"path": "a.md"}))
        result = loop(adapter).run(request())  # no tools, no dispatcher
        self.assertFalse(result.ok)
        self.assertEqual(result.error_class, "malformed_tool_arguments")


class TestCostGuardIntegration(unittest.TestCase):
    def test_the_guard_stops_before_the_request(self) -> None:
        from pae_eval.errors import CostCeilingError

        calls = {"n": 0}

        def guard():
            calls["n"] += 1
            raise CostCeilingError("ceiling")

        adapter = scripted(text_step("Summary never reached"))
        with self.assertRaises(CostCeilingError):
            HostLoop(adapter, sleep=lambda _s: None, cost_guard=guard).run(request())
        self.assertEqual(adapter.call_count, 0, "no request may be sent")
        self.assertEqual(calls["n"], 1)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

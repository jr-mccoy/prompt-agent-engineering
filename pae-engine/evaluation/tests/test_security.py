"""Secret redaction, trial storage and resume.

Redaction is tested by planting recognizable fake secrets in every place one
could realistically arrive from — the environment, a provider exception, a raw
response fixture, HTTP-style headers — and proving none survives to disk. A
redactor tested only against the values it already knows about is a redactor
that has been tested against nothing.
"""

from __future__ import annotations

import json
import unittest

from _support import TempDirCase

from pae_eval.errors import FrozenPlanError
from pae_eval.redaction import (
    PLACEHOLDER,
    known_secrets,
    redact,
    redact_text,
    safe_environment_names,
)
from pae_eval.trials import (
    TrialRecord,
    TrialStore,
    model_config_hash,
    new_run_id,
    trial_id,
)

FAKE_ENV = {
    "ANTHROPIC_API_KEY": "sk-ant-fake0123456789abcdefFAKE",
    "OPENAI_API_KEY": "sk-proj-fake0123456789abcdefFAKE",
    "GITHUB_TOKEN": "ghp_fake0123456789abcdefghijklmn",
    "PATH": "/usr/bin",
}


class TestRedaction(unittest.TestCase):
    def test_environment_values_are_found(self) -> None:
        secrets = known_secrets(FAKE_ENV)
        self.assertIn(FAKE_ENV["ANTHROPIC_API_KEY"], secrets)
        self.assertNotIn("/usr/bin", secrets)

    def test_longest_first_so_a_prefix_cannot_leave_a_tail(self) -> None:
        env = {"ANTHROPIC_API_KEY": "sk-ant-abcdefgh",
               "OPENAI_API_KEY": "sk-ant-abcdefghIJKLMNOP"}
        text = "key=sk-ant-abcdefghIJKLMNOP"
        redacted = redact_text(text, known_secrets(env))
        self.assertNotIn("IJKLMNOP", redacted)

    def test_a_planted_key_in_free_text_is_removed(self) -> None:
        text = f"request failed with key {FAKE_ENV['ANTHROPIC_API_KEY']}"
        self.assertNotIn("FAKE", redact_text(text, env=FAKE_ENV))

    def test_secret_shaped_values_are_removed_even_if_unknown(self) -> None:
        """A key from a source we never enumerated must still be caught."""
        text = "authorization: Bearer abcdefghijklmnopqrstuvwxyz012345"
        self.assertIn(PLACEHOLDER, redact_text(text, env={}))

    def test_an_unknown_openai_style_key_is_removed(self) -> None:
        text = "sk-Zz09aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertIn(PLACEHOLDER, redact_text(text, env={}))

    def test_keys_are_redacted_by_name(self) -> None:
        payload = {"api_key": "anything at all", "Authorization": "Bearer x",
                   "nested": {"refresh_token": "zzz"}}
        redacted = redact(payload, env={})
        self.assertEqual(redacted["api_key"], PLACEHOLDER)
        self.assertEqual(redacted["Authorization"], PLACEHOLDER)
        self.assertEqual(redacted["nested"]["refresh_token"], PLACEHOLDER)

    def test_a_provider_exception_message_is_redacted(self) -> None:
        payload = {"error": {
            "message": f"401 from provider using {FAKE_ENV['OPENAI_API_KEY']}"}}
        self.assertNotIn("FAKE", json.dumps(redact(payload, env=FAKE_ENV)))

    def test_a_raw_response_fixture_is_redacted(self) -> None:
        payload = {"request": {"headers": {
            "x-api-key": FAKE_ENV["ANTHROPIC_API_KEY"],
            "user-agent": "pae-eval/0.1",
        }}, "body": {"note": FAKE_ENV["GITHUB_TOKEN"]}}
        blob = json.dumps(redact(payload, env=FAKE_ENV))
        self.assertNotIn("FAKE", blob)
        self.assertNotIn("ghp_fake", blob)
        self.assertIn("pae-eval/0.1", blob)  # non-secrets survive

    def test_lists_and_tuples_are_walked(self) -> None:
        payload = [{"token": "x"}, [FAKE_ENV["ANTHROPIC_API_KEY"]]]
        self.assertNotIn("FAKE", json.dumps(redact(payload, env=FAKE_ENV)))

    def test_only_names_are_reported_never_values(self) -> None:
        names = safe_environment_names(FAKE_ENV)
        self.assertIn("ANTHROPIC_API_KEY", names)
        for value in FAKE_ENV.values():
            self.assertNotIn(value, names)

    def test_short_values_are_not_treated_as_secrets(self) -> None:
        """Otherwise a variable set to 'true' would censor the word 'true'."""
        self.assertEqual(known_secrets({"ANTHROPIC_API_KEY": "x"}), ())


def make_record(**overrides) -> TrialRecord:
    base = dict(
        trial_id="t-1:D:r0:abc", run_id="run-x", task_id="t-1", condition="D",
        repeat_index=0, attempt_no=1, evaluation_version="1", benchmark_version="1",
        benchmark_sha256="sha256:b", plan_sha256="sha256:p",
        participant_provider="fake", participant_model="fake-model-1",
        model_parameters={}, model_parameters_sha256="sha256:m",
        system_prompt_sha256="sha256:s", task_sha256="sha256:t",
        pae_commit="abc", pae_dirty=False, engine_version="0.4.0.dev0",
        mcp_sdk_version=None, tool_catalog_sha256="sha256:c",
        participant_snapshot_sha256="sha256:snap", pricing_snapshot_sha256="sha256:pr",
        started_at="2026-09-02T00:00:00Z", ended_at="2026-09-02T00:00:01Z",
        latency_ms=1000.0, state="completed", stop_reason="end_turn",
        final_answer="Summary ok", observable_tool_calls=[], usage={},
        error_class=None, retry_state={}, estimated_cost_usd=0.0,
    )
    base.update(overrides)
    return TrialRecord(**base)


class TestTrialIdentity(unittest.TestCase):
    def test_ids_are_deterministic(self) -> None:
        kwargs = dict(evaluation_version="1", benchmark_sha256="sha256:b",
                      task_id="t-1", condition="D", model_config_sha256="sha256:m",
                      repeat_index=0, plan_sha256="sha256:p")
        self.assertEqual(trial_id(**kwargs), trial_id(**kwargs))

    def test_changing_any_component_changes_the_id(self) -> None:
        kwargs = dict(evaluation_version="1", benchmark_sha256="sha256:b",
                      task_id="t-1", condition="D", model_config_sha256="sha256:m",
                      repeat_index=0, plan_sha256="sha256:p")
        base = trial_id(**kwargs)
        for field, value in (("condition", "B"), ("repeat_index", 1),
                             ("plan_sha256", "sha256:other"),
                             ("benchmark_sha256", "sha256:other")):
            self.assertNotEqual(base, trial_id(**{**kwargs, field: value}), field)

    def test_the_id_is_readable(self) -> None:
        value = trial_id(evaluation_version="1", benchmark_sha256="sha256:b",
                         task_id="t-1", condition="D", model_config_sha256="sha256:m",
                         repeat_index=2, plan_sha256="sha256:p")
        self.assertTrue(value.startswith("t-1:D:r2:"))

    def test_model_config_hash_ignores_credentials(self) -> None:
        a = model_config_hash({"provider": "x", "model": "y"})
        b = model_config_hash({"provider": "x", "model": "y", "api_key": "secret"})
        self.assertEqual(a, b)

    def test_run_id_is_derived_from_the_design(self) -> None:
        args = dict(plan_sha256="sha256:p", benchmark_sha256="sha256:b",
                    snapshot_sha256="sha256:s")
        self.assertEqual(new_run_id(**args), new_run_id(**args))
        self.assertNotEqual(new_run_id(**args), new_run_id(**args, label="dev"))


class TestAppendOnlyStore(TempDirCase):
    def test_records_append_and_never_overwrite(self) -> None:
        store = TrialStore(self.tmp_path("out/trials.jsonl"))
        store.append(make_record(attempt_no=1, state="infrastructure_failed",
                                 error_class="rate_limited"))
        store.append(make_record(attempt_no=2, state="completed"))
        rows = list(store.read())
        self.assertEqual(len(rows), 2)
        self.assertEqual([r["attempt_no"] for r in rows], [1, 2])

    def test_written_records_are_redacted(self) -> None:
        store = TrialStore(self.tmp_path("out2/trials.jsonl"))
        store.append(make_record(final_answer="key sk-ant-aaaaaaaaaaaaaaaaaaaa"))
        text = store.path.read_text(encoding="utf-8")
        self.assertIn(PLACEHOLDER, text)
        self.assertNotIn("sk-ant-aaaaaaaaaaaaaaaaaaaa", text)

    def test_no_chain_of_thought_field_exists(self) -> None:
        payload = make_record().to_json_obj()
        for forbidden in ("thinking", "chain_of_thought", "reasoning",
                          "redacted_thinking"):
            self.assertNotIn(forbidden, payload)

    def test_completed_ids_are_the_resume_set(self) -> None:
        store = TrialStore(self.tmp_path("out3/trials.jsonl"))
        store.append(make_record(trial_id="a", state="completed"))
        store.append(make_record(trial_id="b", state="infrastructure_failed"))
        self.assertEqual(store.completed_trial_ids(), {"a"})

    def test_resume_refuses_a_changed_plan(self) -> None:
        store = TrialStore(self.tmp_path("out4/trials.jsonl"))
        store.append(make_record())
        with self.assertRaises(FrozenPlanError) as caught:
            store.assert_resumable(plan_sha256="sha256:DIFFERENT",
                                   benchmark_sha256="sha256:b",
                                   snapshot_sha256="sha256:snap")
        self.assertIn("evaluation plan", str(caught.exception))

    def test_resume_refuses_a_changed_benchmark(self) -> None:
        store = TrialStore(self.tmp_path("out5/trials.jsonl"))
        store.append(make_record())
        with self.assertRaises(FrozenPlanError):
            store.assert_resumable(plan_sha256="sha256:p",
                                   benchmark_sha256="sha256:DIFFERENT",
                                   snapshot_sha256="sha256:snap")

    def test_resume_accepts_a_matching_configuration(self) -> None:
        store = TrialStore(self.tmp_path("out6/trials.jsonl"))
        store.append(make_record())
        store.assert_resumable(plan_sha256="sha256:p", benchmark_sha256="sha256:b",
                               snapshot_sha256="sha256:snap")

    def test_reading_an_absent_file_is_empty_not_an_error(self) -> None:
        self.assertEqual(list(TrialStore(self.tmp_path("nope/trials.jsonl")).read()), [])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

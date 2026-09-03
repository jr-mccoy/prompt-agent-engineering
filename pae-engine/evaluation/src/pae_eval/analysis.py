"""Analysis: trials plus scores in, a machine-readable analysis object out.

The report generator reads only this object and never re-derives a number, so
"what the report says" and "what the analysis computed" cannot drift apart.

Aggregation order is deliberate and enforced: repeats collapse to one value per
task-condition *first*, and only then does anything statistical happen. The
alternative — pouring repeats into the test as independent observations —
multiplies n by the repeat count and shrinks every interval, which is the
easiest way to manufacture significance without noticing.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence

from .constants import ANALYSIS_SCHEMA, CONDITIONS
from .statistics import (
    aggregate_repeats,
    holm_bonferroni,
    mean_pass_proportion,
    non_inferiority,
    paired_bootstrap_ci,
    paired_continuous,
    primary_endpoint,
)


@dataclass
class AnalysisInputs:
    trials: Sequence[Mapping[str, Any]]
    scores: Sequence[Mapping[str, Any]]
    plan: Any
    retrieval: Mapping[str, Any] | None = None
    reliability: Mapping[str, Any] | None = None
    pairwise: Sequence[Mapping[str, Any]] = field(default_factory=tuple)


def _index_scores(scores: Iterable[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    return {str(s.get("trial_id")): s for s in scores}


def _terminal_trials(trials: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    """Latest attempt per trial id, so retries do not double-count."""
    latest: dict[str, Mapping[str, Any]] = {}
    for row in trials:
        key = str(row.get("trial_id"))
        current = latest.get(key)
        if current is None or int(row.get("attempt_no", 0)) >= int(
            current.get("attempt_no", 0)
        ):
            latest[key] = row
    return list(latest.values())


def build_pairs(
    trials: Sequence[Mapping[str, Any]],
    scores: Sequence[Mapping[str, Any]],
    *,
    first_condition: str,
    second_condition: str,
    repeat_strategy: str,
    model_filter: str | None = None,
) -> tuple[dict[str, tuple[bool, bool]], dict[str, Any]]:
    """Task-level paired outcomes for the primary contrast.

    Returns the pairs plus an accounting of what was dropped and why, so the
    report can state exclusions rather than silently losing tasks.
    """
    by_trial = _index_scores(scores)
    # task -> condition -> repeat_index -> passed
    collected: dict[str, dict[str, dict[int, bool]]] = defaultdict(
        lambda: defaultdict(dict)
    )
    missing_score = 0
    non_terminal = 0

    for row in _terminal_trials(trials):
        condition = str(row.get("condition"))
        if condition not in (first_condition, second_condition):
            continue
        if model_filter and str(row.get("participant_model")) != model_filter:
            continue
        if row.get("state") != "completed":
            # A refusal or behavioural timeout is a *failure*, not a missing
            # observation: it counts as not passing.
            collected[str(row.get("task_id"))][condition][
                int(row.get("repeat_index", 0))
            ] = False
            non_terminal += 1
            continue
        score = by_trial.get(str(row.get("trial_id")))
        if score is None:
            missing_score += 1
            continue
        collected[str(row.get("task_id"))][condition][
            int(row.get("repeat_index", 0))
        ] = bool(score.get("passed"))

    pairs: dict[str, tuple[bool, bool]] = {}
    incomplete: list[str] = []
    for task_id, conditions in collected.items():
        first = conditions.get(first_condition) or {}
        second = conditions.get(second_condition) or {}
        if not first or not second:
            incomplete.append(task_id)
            continue
        a = aggregate_repeats([first[k] for k in sorted(first)], repeat_strategy)
        b = aggregate_repeats([second[k] for k in sorted(second)], repeat_strategy)
        if a is None or b is None:
            incomplete.append(task_id)
            continue
        pairs[task_id] = (a, b)

    accounting = {
        "paired_tasks": len(pairs),
        "incomplete_pairs": sorted(incomplete),
        "trials_without_score": missing_score,
        "non_completed_trials_counted_as_failures": non_terminal,
    }
    return pairs, accounting


def efficiency_by_condition(trials: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Separate axes, never a composite score (spec §70)."""
    buckets: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for row in _terminal_trials(trials):
        condition = str(row.get("condition"))
        usage = row.get("usage") or {}
        bucket = buckets[condition]
        bucket["input_tokens"].append(float(usage.get("input_tokens") or 0))
        bucket["output_tokens"].append(float(usage.get("output_tokens") or 0))
        bucket["cached_input_tokens"].append(float(usage.get("cache_read_tokens") or 0))
        bucket["cache_write_tokens"].append(float(usage.get("cache_write_tokens") or 0))
        # Every input bucket, not just the full-rate one. The buckets are
        # disjoint, so summing only input+output would report fewer tokens for
        # identical work as soon as caching is enabled — and unevenly across
        # conditions, because they differ in how cacheable their prompts are.
        # This endpoint measures work; `cost_usd` is where the discount shows.
        bucket["total_tokens"].append(
            float(usage.get("input_tokens") or 0)
            + float(usage.get("cache_read_tokens") or 0)
            + float(usage.get("cache_write_tokens") or 0)
            + float(usage.get("output_tokens") or 0)
        )
        bucket["latency_ms"].append(float(row.get("latency_ms") or 0))
        bucket["cost_usd"].append(float(row.get("estimated_cost_usd") or 0))
        calls = row.get("observable_tool_calls") or []
        bucket["tool_calls"].append(float(len(calls)))
        bucket["tool_bytes"].append(
            float(sum(int(c.get("bytes") or 0) for c in calls))
        )

    def mean(values: Sequence[float]) -> float | None:
        return (sum(values) / len(values)) if values else None

    return {
        condition: {
            "n": len(metrics["total_tokens"]),
            **{key: (round(mean(values), 3) if mean(values) is not None else None)
               for key, values in metrics.items()},
        }
        for condition, metrics in sorted(buckets.items())
    }


def failure_accounting(trials: Sequence[Mapping[str, Any]],
                       planned: int | None = None) -> dict[str, Any]:
    """Every trial is accounted for. Nothing is silently deleted (spec §81)."""
    terminal = _terminal_trials(trials)
    states = Counter(str(row.get("state")) for row in terminal)
    errors = Counter(
        str(row.get("error_class")) for row in terminal if row.get("error_class")
    )
    attempts = sum(int(row.get("attempt_no") or 1) for row in terminal)
    invalid_tool_calls = sum(
        1
        for row in terminal
        for call in (row.get("observable_tool_calls") or [])
        if call.get("status") != "ok"
    )
    return {
        "planned_trials": planned,
        "recorded_trials": len(terminal),
        "total_attempts": attempts,
        "states": dict(sorted(states.items())),
        "error_classes": dict(sorted(errors.items())),
        "provider_refusals": errors.get("refusal", 0),
        "infrastructure_failures": states.get("infrastructure_failed", 0),
        "timeouts": errors.get("behavioural_timeout", 0),
        "turn_budget_exhausted": errors.get("turn_budget_exhausted", 0),
        "invalid_tool_calls": invalid_tool_calls,
    }


def condition_a_sensitivity(trials: Sequence[Mapping[str, Any]],
                            scores: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Tasks Condition A already passes discriminate poorly (spec §95).

    Reported, never excluded: dropping them after seeing results would be an
    unregistered exclusion rule.
    """
    by_trial = _index_scores(scores)
    passed_a: set[str] = set()
    all_a: set[str] = set()
    for row in _terminal_trials(trials):
        if str(row.get("condition")) != "A":
            continue
        task = str(row.get("task_id"))
        all_a.add(task)
        score = by_trial.get(str(row.get("trial_id")))
        if score and score.get("passed"):
            passed_a.add(task)
    return {
        "tasks_with_condition_a": len(all_a),
        "tasks_condition_a_passed": len(passed_a),
        "low_discrimination_task_ids": sorted(passed_a),
        "note": (
            "Retained in the primary analysis. Listed so a reader can see how "
            "much of the benchmark the corpus was not needed for."
        ),
    }


def analyze(inputs: AnalysisInputs, *, planned_trials: int | None = None
            ) -> dict[str, Any]:
    """The full analysis object."""
    plan = inputs.plan
    first, second = plan.primary_comparison
    primary_model = plan.model_for("primary")
    robustness = plan.model_for("robustness")

    pairs, accounting = build_pairs(
        inputs.trials, inputs.scores,
        first_condition=first, second_condition=second,
        repeat_strategy=plan.repeat_strategy,
        model_filter=primary_model.model if primary_model else None,
    )
    result = primary_endpoint(
        pairs, first_condition=first, second_condition=second,
        repeat_strategy=plan.repeat_strategy,
        resamples=plan.bootstrap_resamples, seed=plan.randomization_seed,
        minimum_meaningful_effect=plan.minimum_meaningful_effect_pp / 100.0,
    )

    # -- secondary: continuous rubric score -------------------------------
    by_trial = _index_scores(inputs.scores)
    continuous: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for row in _terminal_trials(inputs.trials):
        score = by_trial.get(str(row.get("trial_id")))
        if score is None:
            continue
        continuous[str(row.get("task_id"))][str(row.get("condition"))].append(
            float(score.get("continuous_score") or 0.0)
        )
    shared = sorted(
        t for t, c in continuous.items() if first in c and second in c
    )
    secondary_continuous = None
    if shared:
        secondary_continuous = paired_continuous(
            [sum(continuous[t][first]) / len(continuous[t][first]) for t in shared],
            [sum(continuous[t][second]) / len(continuous[t][second]) for t in shared],
            resamples=plan.bootstrap_resamples, seed=plan.randomization_seed,
        ).to_json_obj()

    # -- efficiency, gated on quality non-inferiority ----------------------
    efficiency = efficiency_by_condition(inputs.trials)
    gate = non_inferiority(result.ci, plan.non_inferiority_margin_pp / 100.0)
    token_reduction = None
    first_tokens = (efficiency.get(first) or {}).get("total_tokens")
    second_tokens = (efficiency.get(second) or {}).get("total_tokens")
    if first_tokens and second_tokens:
        token_reduction = (second_tokens - first_tokens) / second_tokens

    efficiency_claim = {
        "quality_non_inferiority": gate.to_json_obj(),
        "token_reduction": (
            None if token_reduction is None else round(token_reduction, 4)
        ),
        "target_token_reduction": plan.efficiency_target_token_reduction,
        "claim_supported": bool(
            gate.passed
            and token_reduction is not None
            and token_reduction >= plan.efficiency_target_token_reduction
        ),
        "note": (
            "An efficiency claim requires the quality non-inferiority gate to "
            "pass first. Cheaper-but-worse is not an efficiency result."
        ),
    }

    # -- multiplicity ------------------------------------------------------
    secondary_p: dict[str, float] = {}
    if secondary_continuous and secondary_continuous["wilcoxon"]["p_value"] is not None:
        secondary_p["continuous_rubric_score"] = float(
            secondary_continuous["wilcoxon"]["p_value"]
        )
    adjusted = [t.to_json_obj() for t in holm_bonferroni(secondary_p)]

    # -- exploratory (labelled, never promoted) ----------------------------
    per_class: dict[str, dict[str, Any]] = {}
    task_class = {
        str(t.task_id): t.task_class
        for t in getattr(getattr(plan, "_benchmark", None), "tasks", ())
    }
    if not task_class:
        task_class = {}
    for task_id, (a, b) in pairs.items():
        klass = task_class.get(task_id, "unclassified")
        bucket = per_class.setdefault(klass, {"n": 0, f"{first}_pass": 0,
                                              f"{second}_pass": 0})
        bucket["n"] += 1
        bucket[f"{first}_pass"] += int(a)
        bucket[f"{second}_pass"] += int(b)

    return {
        "schema_version": ANALYSIS_SCHEMA,
        "plan_sha256": plan.sha256,
        "evaluation_version": plan.evaluation_version,
        "mode": plan.mode,
        "primary": result.to_json_obj(),
        "primary_accounting": accounting,
        "primary_model": primary_model.to_json_obj() if primary_model else None,
        "robustness_model": robustness.to_json_obj() if robustness else None,
        "secondary": {
            "continuous_rubric_score": secondary_continuous,
            "holm_bonferroni": adjusted,
            "policy": plan.multiple_comparison_policy,
        },
        "efficiency": efficiency,
        "efficiency_claim": efficiency_claim,
        "retrieval": dict(inputs.retrieval) if inputs.retrieval else None,
        "judge_reliability": dict(inputs.reliability) if inputs.reliability else None,
        "failures": failure_accounting(inputs.trials, planned_trials),
        "condition_a_sensitivity": condition_a_sensitivity(
            inputs.trials, inputs.scores),
        "exploratory": {
            "note": (
                "Exploratory. Hypothesis-generating only; not corrected, not "
                "confirmatory, and not to be quoted as a finding."
            ),
            "per_task_class": per_class,
        },
    }

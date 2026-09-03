"""Report generation.

The generator reads the analysis object and nothing else. It contains no canned
sentence asserting that PAE improved, won or saved money; every such statement
is built from a number and is emitted only when that number supports it. A null
result and a negative result get the same template, the same section order and
the same prominence as a positive one (spec §88).

The rule that makes this hold under maintenance: **no comparative wording is
written by hand.** Direction words come from `_direction()`, which reads the
confidence interval. If the interval straddles zero, the only sentence
available says so.
"""

from __future__ import annotations

import datetime as _dt
from typing import Any, Mapping, Sequence

from .constants import CONDITION_LABELS, FIXTURE_MARKER, REPORT_SCHEMA


def _pp(value: float | None) -> str:
    return "n/a" if value is None else f"{value * 100:+.1f} pp"


def _pct(value: float | None) -> str:
    return "n/a" if value is None else f"{value * 100:.1f}%"


def _num(value: float | None, digits: int = 1) -> str:
    return "n/a" if value is None else f"{value:,.{digits}f}"


def _direction(ci: Mapping[str, Any]) -> str:
    """The only place a comparative claim is allowed to originate."""
    lower = ci.get("ci_lower")
    upper = ci.get("ci_upper")
    if lower is None or upper is None:
        return "indeterminate"
    if lower > 0:
        return "higher"
    if upper < 0:
        return "lower"
    return "indistinguishable"


def _primary_sentence(primary: Mapping[str, Any], plan: Any) -> str:
    first, second = primary["primary_contrast"]
    ci = primary["ci"]
    direction = _direction(ci)
    diff = primary["absolute_difference"]
    first_rate = primary.get(f"{first}_pass_rate")
    second_rate = primary.get(f"{second}_pass_rate")
    mcnemar = primary["mcnemar"]

    core = (
        f"Condition {first} passed {_pct(first_rate)} of {primary['n_tasks']} tasks "
        f"and condition {second} passed {_pct(second_rate)} "
        f"({_pp(diff)}; paired 95% CI {_pp(ci['ci_lower'])} to {_pp(ci['ci_upper'])}; "
        f"exact McNemar p = {mcnemar['p_value']:.4g}, "
        f"{mcnemar['discordant']} discordant pairs)."
    )

    if direction == "indistinguishable":
        verdict = (
            f" The interval includes zero, so this run does not distinguish "
            f"condition {first} from condition {second} on the primary endpoint."
        )
    elif direction == "higher":
        meets = primary.get("meets_minimum_meaningful_effect")
        if meets:
            verdict = (
                f" The interval excludes zero and clears the pre-registered "
                f"minimum meaningful effect of "
                f"{plan.minimum_meaningful_effect_pp:+.0f} pp."
            )
        else:
            verdict = (
                f" The interval excludes zero but does not clear the "
                f"pre-registered minimum meaningful effect of "
                f"{plan.minimum_meaningful_effect_pp:+.0f} pp, so the difference "
                "is measurable without being large enough to have been declared "
                "meaningful in advance."
            )
    else:
        verdict = (
            f" The interval lies below zero: condition {first} performed worse "
            f"than condition {second} on the primary endpoint."
        )
    return core + verdict


def render_markdown(analysis: Mapping[str, Any], *, plan: Any,
                    manifest: Mapping[str, Any] | None = None,
                    benchmark_composition: Mapping[str, Any] | None = None,
                    is_fixture: bool = False) -> str:
    primary = analysis["primary"]
    first, second = primary["primary_contrast"]
    lines: list[str] = []
    add = lines.append

    if is_fixture:
        add(f"> **{FIXTURE_MARKER}**\n")
    if plan.mode != "sealed":
        add(
            "> **Development run.** Produced in development mode against an "
            "unsealed plan. Not evidence about PAE's effect on task quality.\n"
        )

    add("# PAE evaluation report\n")
    add(f"Evaluation version `{analysis['evaluation_version']}` · "
        f"plan `{analysis['plan_sha256'][:19]}…` · mode **{plan.mode}**\n")

    # -- executive summary -------------------------------------------------
    add("## Executive summary\n")
    add(_primary_sentence(primary, plan) + "\n")
    claim = analysis.get("efficiency_claim") or {}
    if claim:
        if claim.get("claim_supported"):
            add(
                f"Condition {first} also met the pre-registered efficiency target: "
                f"{_pct(claim.get('token_reduction'))} fewer total tokens than "
                f"condition {second}, with quality non-inferiority satisfied.\n"
            )
        elif claim.get("token_reduction") is not None:
            gate = (claim.get("quality_non_inferiority") or {})
            reason = (
                "the quality non-inferiority gate did not pass"
                if not gate.get("quality_non_inferior")
                else "the reduction did not reach the pre-registered target"
            )
            add(
                f"No efficiency claim is made: token reduction was "
                f"{_pct(claim.get('token_reduction'))} and {reason}.\n"
            )
    add("")

    # -- design ------------------------------------------------------------
    add("## Evaluation design\n")
    add(f"- Conditions: {', '.join(f'**{c}** ({CONDITION_LABELS.get(c, c)})' for c in plan.conditions)}")
    add(f"- Primary comparison: **{first} vs {second}**, paired, unit = task")
    add(f"- Primary endpoint: `{plan.primary_endpoint}`")
    add(f"- Repeat strategy: `{plan.repeat_strategy}`")
    add(f"- Minimum meaningful effect: {plan.minimum_meaningful_effect_pp:+.0f} pp")
    add(f"- Non-inferiority margin: {plan.non_inferiority_margin_pp:+.0f} pp")
    add(f"- Bootstrap resamples: {plan.bootstrap_resamples:,} (seed "
        f"{plan.randomization_seed})")
    add(f"- Multiplicity: {plan.multiple_comparison_policy}\n")

    # -- benchmark composition --------------------------------------------
    if benchmark_composition:
        add("## Benchmark composition\n")
        add(f"- Tasks: {benchmark_composition.get('task_count')}")
        add(f"- Distinct scopes: {benchmark_composition.get('distinct_scopes')}")
        classes = benchmark_composition.get("class_distribution") or {}
        if classes:
            add("\n| Task class | n |\n|---|---:|")
            for name, count in classes.items():
                add(f"| {name} | {count} |")
        modes = benchmark_composition.get("authoring_modes") or {}
        if modes:
            add("\n| Authoring mode | n |\n|---|---:|")
            for name, count in modes.items():
                add(f"| {name} | {count} |")
        add("")

    # -- primary endpoint --------------------------------------------------
    add("## Primary endpoint\n")
    ci = primary["ci"]
    add("| Quantity | Value |\n|---|---|")
    add(f"| Tasks paired | {primary['n_tasks']} |")
    add(f"| Condition {first} pass rate | {_pct(primary.get(f'{first}_pass_rate'))} |")
    add(f"| Condition {second} pass rate | {_pct(primary.get(f'{second}_pass_rate'))} |")
    add(f"| Absolute difference | {_pp(primary['absolute_difference'])} |")
    add(f"| Paired 95% CI | {_pp(ci['ci_lower'])} to {_pp(ci['ci_upper'])} |")
    add(f"| Exact McNemar p | {primary['mcnemar']['p_value']:.4g} |")
    add(f"| Discordant pairs | {primary['mcnemar']['discordant']} "
        f"(b={primary['mcnemar']['b_first_only']}, "
        f"c={primary['mcnemar']['c_second_only']}) |")
    add(f"| Meets minimum meaningful effect | "
        f"{primary.get('meets_minimum_meaningful_effect')} |\n")

    accounting = analysis.get("primary_accounting") or {}
    if accounting.get("incomplete_pairs"):
        add(f"{len(accounting['incomplete_pairs'])} task(s) had no complete pair and "
            "are excluded from the primary; they are listed in the analysis JSON.\n")

    # -- condition comparison ---------------------------------------------
    add("## Condition comparison\n")
    efficiency = analysis.get("efficiency") or {}
    if efficiency:
        # `total tok` is every token processed, cached or not, so it stays
        # comparable across conditions and is unaffected by caching. The cache
        # columns are shown rather than folded away so a reader can see where
        # the cost difference came from instead of inferring it.
        add("| Condition | n | input tok | cache read | cache write | output tok "
            "| total tok | tool calls | latency ms | cost USD |"
            "\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for condition in sorted(efficiency):
            row = efficiency[condition]
            add(
                f"| {condition} | {row.get('n')} | {_num(row.get('input_tokens'), 0)} "
                f"| {_num(row.get('cached_input_tokens'), 0)} "
                f"| {_num(row.get('cache_write_tokens'), 0)} "
                f"| {_num(row.get('output_tokens'), 0)} "
                f"| {_num(row.get('total_tokens'), 0)} "
                f"| {_num(row.get('tool_calls'), 2)} "
                f"| {_num(row.get('latency_ms'), 0)} "
                f"| {_num(row.get('cost_usd'), 4)} |"
            )
        add("")

    # -- model families ----------------------------------------------------
    add("## Model-family results\n")
    add(f"- Primary (confirmatory): "
        f"{(analysis.get('primary_model') or {}).get('model', 'n/a')}")
    robustness = analysis.get("robustness_model")
    add(f"- Robustness replication: "
        f"{(robustness or {}).get('model', 'not run')}")
    add("\nThe confirmatory analysis uses the primary family only. Families are "
        "not averaged into a single headline.\n")

    # -- retrieval ---------------------------------------------------------
    add("## Retrieval and routing (Layer A)\n")
    retrieval = analysis.get("retrieval")
    if not retrieval:
        add("Not run.\n")
    else:
        if retrieval.get("disclosure"):
            add(f"> {retrieval['disclosure']}\n")
        metrics = retrieval.get("metrics") or {}
        add("| Metric | Value |\n|---|---|")
        for key in ("n", "recall_at_1", "recall_at_5", "mrr", "scope_at_1",
                    "kind_at_1", "route_status_accuracy", "false_confident_rate"):
            value = metrics.get(key)
            rendered = (
                f"{value}" if key == "n"
                else ("n/a" if value is None else f"{value:.3f}")
            )
            add(f"| {key} | {rendered} |")
        add("")

    # -- efficiency --------------------------------------------------------
    add("## Efficiency\n")
    add("Reported as separate axes. No composite efficiency score is computed.\n")
    if claim:
        add(f"- Quality non-inferiority: "
            f"{(claim.get('quality_non_inferiority') or {}).get('quality_non_inferior')}")
        add(f"- Token reduction: {_pct(claim.get('token_reduction'))} "
            f"(target {_pct(claim.get('target_token_reduction'))})")
        add(f"- Efficiency claim supported: {claim.get('claim_supported')}\n")

    # -- safety ------------------------------------------------------------
    add("## Safety and governance\n")
    add("Deterministic Engine and MCP invariants are reported separately from "
        "behavioural model outcomes: the first are properties of the product, "
        "the second are properties of a model on a day.\n")

    # -- failures ----------------------------------------------------------
    add("## Failure accounting\n")
    failures = analysis.get("failures") or {}
    add("| Quantity | Count |\n|---|---:|")
    for key in ("planned_trials", "recorded_trials", "total_attempts",
                "provider_refusals", "infrastructure_failures", "timeouts",
                "turn_budget_exhausted", "invalid_tool_calls"):
        add(f"| {key} | {failures.get(key)} |")
    states = failures.get("states") or {}
    if states:
        add("\n| Terminal state | n |\n|---|---:|")
        for name, count in states.items():
            add(f"| {name} | {count} |")
    add("\nNo trial is deleted. Every planned trial is either recorded or listed "
        "as skipped.\n")

    # -- judge reliability -------------------------------------------------
    add("## Judge reliability\n")
    reliability = analysis.get("judge_reliability")
    if not reliability:
        add("Not measured in this run.\n")
    else:
        add(f"Measured on: {reliability.get('measured_on')}. "
            f"Passed calibration gates: **{reliability.get('passed')}**\n")
        metrics = reliability.get("metrics") or {}
        if metrics:
            add("| Metric | Value | Threshold |\n|---|---:|---:|")
            thresholds = reliability.get("thresholds") or {}
            for key, value in metrics.items():
                add(f"| {key} | {value:.3f} | {thresholds.get(key, '—')} |")
        for violation in reliability.get("violations") or []:
            add(f"\n- Gate failed: {violation}")
        add("")

    # -- uncertainty -------------------------------------------------------
    add("## Statistical uncertainty\n")
    add(f"- The primary interval is a paired percentile bootstrap over tasks "
        f"({plan.bootstrap_resamples:,} resamples, seed "
        f"{plan.randomization_seed}).")
    add("- The p-value is an exact test, not a normal approximation.")
    add("- Repeats are aggregated per task before testing; they are never "
        "counted as independent observations.")
    secondary = (analysis.get("secondary") or {}).get("continuous_rubric_score")
    if secondary and not secondary["wilcoxon"]["available"]:
        add("- Wilcoxon was not computed: the `analysis` extra (SciPy) is not "
            "installed. The bootstrap interval is still reported.")
    add("")

    # -- exploratory -------------------------------------------------------
    add("## Exploratory results\n")
    exploratory = analysis.get("exploratory") or {}
    add(f"> {exploratory.get('note', '')}\n")
    per_class = exploratory.get("per_task_class") or {}
    if per_class:
        add(f"| Task class | n | {first} passed | {second} passed |\n|---|---:|---:|---:|")
        for name in sorted(per_class):
            row = per_class[name]
            add(f"| {name} | {row.get('n')} | {row.get(f'{first}_pass')} "
                f"| {row.get(f'{second}_pass')} |")
        add("")

    sensitivity = analysis.get("condition_a_sensitivity") or {}
    if sensitivity.get("tasks_with_condition_a"):
        add(f"Condition A alone passed "
            f"{sensitivity.get('tasks_condition_a_passed')} of "
            f"{sensitivity.get('tasks_with_condition_a')} tasks. "
            f"{sensitivity.get('note')}\n")

    # -- limitations -------------------------------------------------------
    add("## Limitations\n")
    for limitation in _limitations(plan, analysis):
        add(f"- {limitation}")
    add("")

    # -- reproduction ------------------------------------------------------
    add("## Reproduction\n")
    add("```bash")
    add("python -m pae_eval validate-benchmark --benchmark-root <root> --repo <repo>")
    add("python -m pae_eval plan --benchmark-root <root> --repo <repo> --out plan.json")
    add("python -m pae_eval run --execute --plan plan.json --benchmark-root <root> \\")
    add("    --repo <repo> --output-dir <out> --max-cost-usd <n> --max-trials <n>")
    add("python -m pae_eval judge --output-dir <out> --benchmark-root <root>")
    add("python -m pae_eval analyze --output-dir <out> --benchmark-root <root>")
    add("python -m pae_eval report --output-dir <out> --benchmark-root <root>")
    add("```\n")
    if manifest:
        add(f"- PAE commit: `{manifest.get('pae_commit')}`")
        add(f"- Benchmark: `{manifest.get('benchmark_sha256', '')[:19]}…`")
        add(f"- Participant snapshot: "
            f"`{manifest.get('participant_snapshot_sha256', '')[:19]}…`")
        add(f"- Schedule: `{manifest.get('schedule_sha256', '')[:19]}…`")
        add(f"- Pricing snapshot: "
            f"`{manifest.get('pricing_snapshot_sha256', '')[:19]}…`")
    add("")
    return "\n".join(lines)


def _limitations(plan: Any, analysis: Mapping[str, Any]) -> list[str]:
    items = [
        "Results are specific to this benchmark, this corpus, this PAE commit "
        "and the models named above. They do not generalize to other corpora.",
        "Participant outputs are nondeterministic. The current frontier models "
        "do not accept a seed or temperature, so run-to-run variation cannot be "
        "eliminated — only measured. Reproducibility here means the inputs and "
        "the procedure are frozen, not that outputs repeat.",
        "Provider APIs, model identifiers and prices drift. Token counts are the "
        "durable measurement; dollar figures are derived from the dated pricing "
        "snapshot recorded in the manifest.",
        "The raw-repository baseline depends on ripgrep; a different search tool "
        "would be a different baseline.",
        "LLM judging remains imperfect even after calibration. Deterministic "
        "criteria carry as much rubric weight as the rubric allows.",
    ]
    if plan.mode != "sealed":
        items.append(
            "This was a development run against an unsealed plan and is not "
            "evidence for any public claim."
        )
    if analysis.get("judge_reliability") is None:
        items.append("Judge reliability was not measured for this run.")
    robustness = analysis.get("robustness_model")
    if not robustness:
        items.append(
            "Only one model family was run, so the result cannot separate "
            "'PAE helps' from 'PAE helps this family'."
        )
    return items


def claim_sentence(analysis: Mapping[str, Any], *, plan: Any,
                   manifest: Mapping[str, Any]) -> str | None:
    """A claim-ready sentence, or ``None`` when the numbers do not support one.

    Emitted only for a sealed run whose interval excludes zero. There is no
    generic "PAE accuracy = X" output, by design (spec §89).
    """
    if plan.mode != "sealed":
        return None
    primary = analysis["primary"]
    ci = primary["ci"]
    if _direction(ci) != "higher":
        return None
    first, second = primary["primary_contrast"]
    model = (analysis.get("primary_model") or {}).get("model", "the participant model")
    repeats = plan.repeats_for(first)
    return (
        f"On sealed benchmark {analysis.get('evaluation_version')} "
        f"({primary['n_tasks']} tasks) at PAE commit "
        f"{manifest.get('pae_commit', '')[:12]}, {model} completed "
        f"{_pct(primary.get(f'{first}_pass_rate'))} of tasks under condition "
        f"{first} versus {_pct(primary.get(f'{second}_pass_rate'))} under "
        f"condition {second} ({_pp(primary['absolute_difference'])}; paired 95% CI "
        f"{_pp(ci['ci_lower'])} to {_pp(ci['ci_upper'])}; "
        f"{repeats} repeat(s)/task, confirmatory repeat only)."
    )

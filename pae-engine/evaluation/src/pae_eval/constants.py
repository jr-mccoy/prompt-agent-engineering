"""Schema identifiers, enumerations and defaults.

Schema IDs are independent of the Registry's and the ContextBundle's: the
evaluation format versions on its own clock, and reusing a Registry ID would
tie a benchmark rev to an Engine rev for no reason (spec §12, ADR-0035).

Numbers that belong to a *decision* rather than to the code — sample size,
minimum meaningful effect, tool budgets, judge thresholds — deliberately do not
live here. They live in the frozen evaluation plan, where they are hashed and
auditable. What is here is either a schema constant or an example-plan default
clearly marked as such.
"""

from __future__ import annotations

from typing import Final

HARNESS_VERSION: Final = "0.1.0.dev0"

# --------------------------------------------------------------------------
# schema identifiers
# --------------------------------------------------------------------------
BENCHMARK_SCHEMA: Final = "pae-eval-benchmark/1"
PLAN_SCHEMA: Final = "pae-eval-plan/1"
RUN_MANIFEST_SCHEMA: Final = "pae-eval-run-manifest/1"
TRIAL_SCHEMA: Final = "pae-eval-trial/1"
SCORE_SCHEMA: Final = "pae-eval-score/1"
PRICING_SCHEMA: Final = "pae-eval-pricing/1"
REPORT_SCHEMA: Final = "pae-eval-report/1"
SNAPSHOT_SCHEMA: Final = "pae-eval-snapshot/1"
SCHEDULE_SCHEMA: Final = "pae-eval-schedule/1"
ANALYSIS_SCHEMA: Final = "pae-eval-analysis/1"

# --------------------------------------------------------------------------
# conditions
# --------------------------------------------------------------------------
CONDITION_A: Final = "A"  # model only
CONDITION_B: Final = "B"  # generic read-only raw repository
CONDITION_C: Final = "C"  # deterministic PAE ContextBundle, injected
CONDITION_D: Final = "D"  # PAE MCP agent

CONDITIONS: Final = (CONDITION_A, CONDITION_B, CONDITION_C, CONDITION_D)

CONDITION_LABELS: Final = {
    CONDITION_A: "model only",
    CONDITION_B: "raw repository (ripgrep/list/read)",
    CONDITION_C: "deterministic PAE bundle",
    CONDITION_D: "PAE MCP agent",
}

#: Conditions that run a tool loop. The others are a single model call.
TOOL_LOOP_CONDITIONS: Final = (CONDITION_B, CONDITION_D)

# --------------------------------------------------------------------------
# benchmark vocabulary
# --------------------------------------------------------------------------
TASK_CLASSES: Final = (
    "ordinary_task",
    "multi_resource_composition",
    "non_prompt_kind",
    "safety_gated",
    "weak_no_route",
    "cross_domain_ambiguous",
    "technique_discovery",
    "acronym_format_typo",
    "long_complex",
    "adversarial_governance",
)

#: Behavioural tags a task may additionally carry (spec §91).
TASK_TAGS: Final = ("safety_behavior", "adversarial_governance")

SCORED_DIMENSIONS: Final = ("resource", "scope", "kind", "route_status")

#: Router statuses, mirroring pae_engine.routing.
ROUTE_STATUSES: Final = ("matched", "ambiguous", "weak", "no_route")

RESOURCE_KINDS: Final = ("prompt", "technique", "skill", "agent", "command", "persona")

RESOURCE_GRADES: Final = ("primary", "acceptable")

CANONICAL_POLICIES: Final = (
    "canonical_or_registered_copy_both_credited",
    "canonical_only",
)

AUTHORING_MODES: Final = ("natural_external", "masked_resource_derived")

AUTHOR_KINDS: Final = ("human", "ai")

# --------------------------------------------------------------------------
# rubric
# --------------------------------------------------------------------------
CRITERION_TYPES: Final = ("deterministic", "judge")

#: The example rubric weighting from the Phase 7A design. A benchmark may use
#: any weighting; this is what the example plan ships with.
EXAMPLE_RUBRIC_WEIGHTS: Final = {
    "required_elements": 0.35,
    "correctness": 0.20,
    "constraint_adherence": 0.15,
    "completeness": 0.10,
    "safety_governance": 0.10,
    "fabrication_penalty": 0.10,
}

# --------------------------------------------------------------------------
# failure taxonomy (spec §52)
# --------------------------------------------------------------------------
#: Retryable: the request never reached a model outcome.
INFRASTRUCTURE_FAILURES: Final = (
    "rate_limited",
    "server_error",
    "overloaded",
    "connection_error",
    "provider_transport_error",
    "mcp_process_died",
)

#: Not retryable: the model produced an outcome and the outcome is the datum.
MODEL_BEHAVIOUR_FAILURES: Final = (
    "refusal",
    "malformed_tool_arguments",
    "tool_loop",
    "empty_answer",
    "turn_budget_exhausted",
    "behavioural_timeout",
)

TERMINAL_STATES: Final = ("completed", "infrastructure_failed", *MODEL_BEHAVIOUR_FAILURES)

# --------------------------------------------------------------------------
# example-plan defaults (spec §23, §39, §72) — NOT sealed values
# --------------------------------------------------------------------------
EXAMPLE_PLAN_DEFAULTS: Final = {
    "sealed_tasks": 150,
    "development_tasks": 30,
    "primary_comparison": [CONDITION_D, CONDITION_B],
    "primary_endpoint": "task_pass",
    "minimum_meaningful_effect_pp": 10.0,
    "non_inferiority_margin_pp": -5.0,
    "efficiency_target_token_reduction": 0.20,
    "repeats": {CONDITION_A: 1, CONDITION_B: 2, CONDITION_C: 1, CONDITION_D: 2},
    "max_tool_turns": 40,
    "tool_loop_timeout_s": 600,
    "model_call_timeout_s": 120,
    "tool_call_timeout_s": 30,
    "bootstrap_resamples": 10000,
}

#: Raw-repository tool limits (spec §33–§35).
RAW_REPO_LIMITS: Final = {
    "search_max_matches": 200,
    "search_max_line_chars": 120,
    "search_max_result_bytes": 64 * 1024,
    "list_max_paths": 500,
    "list_max_result_bytes": 64 * 1024,
    "read_max_result_bytes": 100 * 1024,
    "read_default_max_lines": 2000,
}

#: Judge calibration gates (spec §64). Configurable; frozen in the plan.
EXAMPLE_JUDGE_THRESHOLDS: Final = {
    "self_consistency_weighted_kappa": 0.75,
    "inter_judge_weighted_kappa": 0.60,
    "manual_review_spearman_rho": 0.70,
    "position_flip_rate_max": 0.15,
    "verbosity_correlation_abs_max": 0.30,
}

#: Benchmark leakage gates (spec §21). Configurable; frozen in the plan.
EXAMPLE_LEAKAGE_THRESHOLDS: Final = {
    "median_target_overlap_max": 0.50,
    "median_target_overlap_masked_derived_max": 0.55,
    "title_token_containment_max": 0,
    "id_tail_containment_max": 0,
    "routing_reference_jaccard_threshold": 0.60,
    "routing_reference_jaccard_share_max": 0.05,
}

#: Repeat-aggregation strategies for the paired binary primary (spec §66, §109).
REPEAT_STRATEGIES: Final = (
    "first_repeat_confirmatory",  # example-plan default
    "all_repeats_must_pass",
    "any_repeat_passes",
    "mean_pass_proportion",
)

#: Paths never included in a participant snapshot (spec §15).
SNAPSHOT_EXCLUDED_PREFIXES: Final = (
    "pae-engine/evaluation/",
    "evaluation-runs/",
    "pae-engine/evaluation-runs/",
)

#: Marker stamped on every synthetic fixture so sample output is never mistaken
#: for evidence (spec §105).
FIXTURE_MARKER: Final = "SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE"

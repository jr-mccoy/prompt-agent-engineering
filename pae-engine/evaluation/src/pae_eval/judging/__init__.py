"""Scoring: deterministic first, a model only for what is genuinely qualitative.

Order matters. Deterministic checks run first and cannot be overridden by a
judge; the judge is then asked only about criteria a rule cannot decide. This
keeps the majority of rubric weight free, stable and immune to judge drift, and
means a judge outage degrades the score rather than destroying it.
"""

from .deterministic import CheckResult, available_rules, run_rule
from .llm import (
    Judge,
    JudgeVerdict,
    OpaqueAnswer,
    assert_judge_family_separation,
    build_absolute_payload,
    build_pairwise_payload,
    parse_json_object,
    resolve_pairwise_winner,
)
from .reliability import (
    ReliabilityReport,
    cohen_kappa,
    evaluate_reliability,
    pearson_r,
    position_flip_rate,
    self_consistency,
    spearman_rho,
    verbosity_correlation,
    weighted_kappa,
)
from .rubric import (
    CriterionScore,
    TaskScore,
    deterministic_weight_share,
    merge_judge_scores,
    score_deterministic,
    score_task,
)

__all__ = [
    "CheckResult", "available_rules", "run_rule",
    "Judge", "JudgeVerdict", "OpaqueAnswer", "assert_judge_family_separation",
    "build_absolute_payload", "build_pairwise_payload", "parse_json_object",
    "resolve_pairwise_winner",
    "ReliabilityReport", "cohen_kappa", "evaluate_reliability", "pearson_r",
    "position_flip_rate", "self_consistency", "spearman_rho",
    "verbosity_correlation", "weighted_kappa",
    "CriterionScore", "TaskScore", "deterministic_weight_share",
    "merge_judge_scores", "score_deterministic", "score_task",
]

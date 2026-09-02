"""Rubric scoring and the primary pass endpoint.

The binary endpoint is derived from the frozen rubric, not from a judge's
overall impression: a task passes when every required criterion passes, the
format gate passes, the safety gate passes and no critical fabrication penalty
fired. A judge's holistic "this feels like an 8" can never rescue a deterministic
required failure (spec §58).

Continuous rubric score is retained as the pre-registered secondary. Both are
computed from the same criterion results, so they can never disagree about what
happened — only about how to summarize it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from ..constants import SCORE_SCHEMA
from .deterministic import CheckResult, run_rule


@dataclass(frozen=True)
class CriterionScore:
    criterion_id: str
    type: str
    weight: float
    required: bool
    failure_gate: bool
    passed: bool
    score: float          # 0.0 - 1.0
    detail: str = ""
    source: str = "deterministic"   # "deterministic" | "judge" | "missing"

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "criterion_id": self.criterion_id,
            "type": self.type,
            "weight": self.weight,
            "required": self.required,
            "failure_gate": self.failure_gate,
            "passed": self.passed,
            "score": round(self.score, 6),
            "detail": self.detail,
            "source": self.source,
        }


@dataclass
class TaskScore:
    task_id: str
    trial_id: str
    condition: str
    criteria: tuple[CriterionScore, ...]
    fabrication_flagged: bool = False
    judge_model: str | None = None
    judge_provider: str | None = None
    notes: tuple[str, ...] = field(default_factory=tuple)

    # -- endpoints ---------------------------------------------------------

    @property
    def continuous_score(self) -> float:
        """Weighted rubric score in [0, 1]."""
        total_weight = sum(c.weight for c in self.criteria)
        if total_weight <= 0:
            return 0.0
        return sum(c.score * c.weight for c in self.criteria) / total_weight

    @property
    def required_failures(self) -> tuple[str, ...]:
        return tuple(c.criterion_id for c in self.criteria if c.required and not c.passed)

    @property
    def gate_failures(self) -> tuple[str, ...]:
        return tuple(
            c.criterion_id for c in self.criteria if c.failure_gate and not c.passed
        )

    @property
    def passed(self) -> bool:
        """The primary binary endpoint."""
        if self.required_failures or self.gate_failures:
            return False
        if self.fabrication_flagged:
            return False
        return True

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": SCORE_SCHEMA,
            "task_id": self.task_id,
            "trial_id": self.trial_id,
            "condition": self.condition,
            "passed": self.passed,
            "continuous_score": round(self.continuous_score, 6),
            "required_failures": list(self.required_failures),
            "gate_failures": list(self.gate_failures),
            "fabrication_flagged": self.fabrication_flagged,
            "judge_provider": self.judge_provider,
            "judge_model": self.judge_model,
            "criteria": [c.to_json_obj() for c in self.criteria],
            "notes": list(self.notes),
        }


def score_deterministic(task: Any, answer: str, context: Mapping[str, Any]
                        ) -> list[CriterionScore]:
    """Score every deterministic criterion. No model involved."""
    scores: list[CriterionScore] = []
    for criterion in task.criteria:
        if criterion.type != "deterministic":
            continue
        rule = criterion.deterministic_rule or {}
        try:
            result: CheckResult = run_rule(rule, answer, context)
        except Exception as exc:  # a broken rule must not pass silently
            result = CheckResult(False, f"rule error: {exc}", str(rule.get("kind", "?")))
        scores.append(CriterionScore(
            criterion_id=criterion.criterion_id,
            type="deterministic",
            weight=criterion.weight,
            required=criterion.required,
            failure_gate=criterion.failure_gate,
            passed=result.passed,
            score=1.0 if result.passed else 0.0,
            detail=result.detail,
            source="deterministic",
        ))
    return scores


def merge_judge_scores(task: Any, deterministic: Sequence[CriterionScore],
                       judge_payload: Mapping[str, Any] | None
                       ) -> list[CriterionScore]:
    """Combine deterministic results with a judge's structured verdict.

    A judge criterion with no verdict scores zero and is marked ``missing``
    rather than being dropped. Dropping it would quietly raise the mean by
    removing the criterion the judge failed to answer.
    """
    merged = list(deterministic)
    judged: Mapping[str, Any] = (judge_payload or {}).get("criteria") or {}
    for criterion in task.criteria:
        if criterion.type != "judge":
            continue
        verdict = judged.get(criterion.criterion_id)
        if not isinstance(verdict, Mapping):
            merged.append(CriterionScore(
                criterion_id=criterion.criterion_id, type="judge",
                weight=criterion.weight, required=criterion.required,
                failure_gate=criterion.failure_gate, passed=False, score=0.0,
                detail="no judge verdict for this criterion", source="missing",
            ))
            continue
        raw = verdict.get("score")
        score = 0.0 if raw is None else max(0.0, min(1.0, float(raw)))
        passed = bool(verdict.get("passed", score >= 0.5))
        merged.append(CriterionScore(
            criterion_id=criterion.criterion_id, type="judge",
            weight=criterion.weight, required=criterion.required,
            failure_gate=criterion.failure_gate, passed=passed, score=score,
            detail=str(verdict.get("evidence", ""))[:500], source="judge",
        ))
    return merged


def score_task(task: Any, *, trial: Mapping[str, Any],
               judge_payload: Mapping[str, Any] | None = None) -> TaskScore:
    """Full score for one trial's answer."""
    answer = str(trial.get("final_answer") or "")
    context = {
        "observable_tool_calls": trial.get("observable_tool_calls") or [],
        "route_bundle": trial.get("route_bundle"),
        "acceptable_resource_uids": [
            r.uid for r in getattr(task, "acceptable_resource_uids", ())
        ],
        "condition": trial.get("condition"),
    }
    deterministic = score_deterministic(task, answer, context)
    criteria = merge_judge_scores(task, deterministic, judge_payload)

    fabrication = bool((judge_payload or {}).get("fabrication_flagged", False))
    return TaskScore(
        task_id=str(trial.get("task_id", "")),
        trial_id=str(trial.get("trial_id", "")),
        condition=str(trial.get("condition", "")),
        criteria=tuple(criteria),
        fabrication_flagged=fabrication,
        judge_provider=(judge_payload or {}).get("judge_provider"),
        judge_model=(judge_payload or {}).get("judge_model"),
    )


def deterministic_weight_share(tasks: Sequence[Any]) -> float:
    """Share of total rubric weight that needs no model. Reported, not gated."""
    total = 0.0
    deterministic = 0.0
    for task in tasks:
        for criterion in task.criteria:
            total += criterion.weight
            if criterion.type == "deterministic":
                deterministic += criterion.weight
    return (deterministic / total) if total else 0.0

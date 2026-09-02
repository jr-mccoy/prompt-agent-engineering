"""The evaluation plan: pre-registration as a hashable artifact.

Everything that could be tuned after seeing results lives here and is hashed:
the benchmark, the prompts, the tool definitions, the conditions, the models,
the judge configuration, the primary endpoint, the minimum meaningful effect,
the retry policy, the exclusion rules, the randomization seed. Freezing it makes
"we decided this in advance" checkable rather than remembered.

The harness cannot stop anyone committing to the repository after a freeze. What
it can do — and does — is refuse to *execute* a sealed run when the world no
longer matches the plan: wrong commit, changed tool catalog, changed prompt,
changed benchmark. That turns an honour system into a gate (spec §25).

No secret ever enters a plan. Provider credentials are named by environment
variable, never valued.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import canonical
from .constants import (
    CONDITIONS,
    EXAMPLE_JUDGE_THRESHOLDS,
    EXAMPLE_LEAKAGE_THRESHOLDS,
    EXAMPLE_PLAN_DEFAULTS,
    HARNESS_VERSION,
    PLAN_SCHEMA,
    REPEAT_STRATEGIES,
)
from .errors import FrozenPlanError, UsageError, ValidationError


@dataclass(frozen=True)
class ModelConfig:
    provider: str
    model: str
    role: str = "primary"  # "primary" | "robustness" | "judge"
    max_output_tokens: int = 6000
    effort: str | None = None
    extra: Mapping[str, Any] = field(default_factory=dict)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "role": self.role,
            "max_output_tokens": self.max_output_tokens,
            "effort": self.effort,
            "extra": dict(self.extra),
        }

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "ModelConfig":
        for forbidden in ("api_key", "credential", "token", "secret"):
            if forbidden in obj:
                raise ValidationError(
                    f"model configuration must not contain {forbidden!r}; "
                    "credentials come from the environment only"
                )
        return cls(
            provider=str(obj.get("provider", "")),
            model=str(obj.get("model", "")),
            role=str(obj.get("role", "primary")),
            max_output_tokens=int(obj.get("max_output_tokens", 6000)),
            effort=obj.get("effort"),
            extra=dict(obj.get("extra") or {}),
        )


@dataclass(frozen=True)
class JudgeConfig:
    provider: str
    model: str
    max_output_tokens: int = 2000
    effort: str | None = None
    allow_same_family: bool = False
    pairwise_on_primary: bool = True
    second_judge: Mapping[str, Any] | None = None
    audit_sample_share: float = 0.20
    thresholds: Mapping[str, float] = field(
        default_factory=lambda: dict(EXAMPLE_JUDGE_THRESHOLDS)
    )

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "max_output_tokens": self.max_output_tokens,
            "effort": self.effort,
            "allow_same_family": self.allow_same_family,
            "pairwise_on_primary": self.pairwise_on_primary,
            "second_judge": dict(self.second_judge) if self.second_judge else None,
            "audit_sample_share": self.audit_sample_share,
            "thresholds": dict(self.thresholds),
        }

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "JudgeConfig":
        return cls(
            provider=str(obj.get("provider", "")),
            model=str(obj.get("model", "")),
            max_output_tokens=int(obj.get("max_output_tokens", 2000)),
            effort=obj.get("effort"),
            allow_same_family=bool(obj.get("allow_same_family", False)),
            pairwise_on_primary=bool(obj.get("pairwise_on_primary", True)),
            second_judge=obj.get("second_judge"),
            audit_sample_share=float(obj.get("audit_sample_share", 0.20)),
            thresholds={**EXAMPLE_JUDGE_THRESHOLDS, **(obj.get("thresholds") or {})},
        )


@dataclass(frozen=True)
class EvaluationPlan:
    evaluation_version: str
    mode: str  # "development" | "sealed"
    benchmark_version: str
    benchmark_sha256: str
    pae_commit: str
    participant_snapshot_sha256: str
    conditions: tuple[str, ...]
    models: tuple[ModelConfig, ...]
    judge: JudgeConfig
    repeats: Mapping[str, int]
    repeat_strategy: str
    system_prompt_sha256: Mapping[str, str]
    tool_catalog_sha256: Mapping[str, str]
    bundle_budget: Mapping[str, Any]
    limits: Mapping[str, Any]
    primary_comparison: tuple[str, str]
    primary_endpoint: str
    secondary_endpoints: tuple[str, ...]
    exploratory_endpoints: tuple[str, ...]
    minimum_meaningful_effect_pp: float
    non_inferiority_margin_pp: float
    efficiency_target_token_reduction: float
    multiple_comparison_policy: str
    retry_policy: Mapping[str, Any]
    exclusion_policy: Mapping[str, Any]
    randomization_seed: int
    pricing_snapshot_sha256: str
    cost_ceiling_policy: Mapping[str, Any]
    leakage_thresholds: Mapping[str, Any]
    bootstrap_resamples: int
    harness_version: str = HARNESS_VERSION
    notes: str = ""

    # -- serialization -----------------------------------------------------

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": PLAN_SCHEMA,
            "evaluation_version": self.evaluation_version,
            "harness_version": self.harness_version,
            "mode": self.mode,
            "benchmark_version": self.benchmark_version,
            "benchmark_sha256": self.benchmark_sha256,
            "pae_commit": self.pae_commit,
            "participant_snapshot_sha256": self.participant_snapshot_sha256,
            "conditions": list(self.conditions),
            "models": [m.to_json_obj() for m in self.models],
            "judge": self.judge.to_json_obj(),
            "repeats": dict(self.repeats),
            "repeat_strategy": self.repeat_strategy,
            "system_prompt_sha256": dict(self.system_prompt_sha256),
            "tool_catalog_sha256": dict(self.tool_catalog_sha256),
            "bundle_budget": dict(self.bundle_budget),
            "limits": dict(self.limits),
            "primary_comparison": list(self.primary_comparison),
            "primary_endpoint": self.primary_endpoint,
            "secondary_endpoints": list(self.secondary_endpoints),
            "exploratory_endpoints": list(self.exploratory_endpoints),
            "minimum_meaningful_effect_pp": self.minimum_meaningful_effect_pp,
            "non_inferiority_margin_pp": self.non_inferiority_margin_pp,
            "efficiency_target_token_reduction": self.efficiency_target_token_reduction,
            "multiple_comparison_policy": self.multiple_comparison_policy,
            "retry_policy": dict(self.retry_policy),
            "exclusion_policy": dict(self.exclusion_policy),
            "randomization_seed": self.randomization_seed,
            "pricing_snapshot_sha256": self.pricing_snapshot_sha256,
            "cost_ceiling_policy": dict(self.cost_ceiling_policy),
            "leakage_thresholds": dict(self.leakage_thresholds),
            "bootstrap_resamples": self.bootstrap_resamples,
            "notes": self.notes,
        }

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    @property
    def is_sealed(self) -> bool:
        return self.mode == "sealed"

    def model_for(self, role: str) -> ModelConfig | None:
        for model in self.models:
            if model.role == role:
                return model
        return None

    def repeats_for(self, condition: str) -> int:
        return int(self.repeats.get(condition, 1))

    def trial_count(self) -> int:
        participants = [m for m in self.models if m.role != "judge"]
        return sum(
            self.repeats_for(condition) for condition in self.conditions
        ) * max(1, len(participants))

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "EvaluationPlan":
        schema = obj.get("schema_version")
        if schema != PLAN_SCHEMA:
            raise ValidationError(
                f"unsupported plan schema {schema!r}; expected {PLAN_SCHEMA}"
            )
        primary = list(obj.get("primary_comparison") or [])
        if len(primary) != 2:
            raise ValidationError("primary_comparison must name exactly two conditions")
        return cls(
            evaluation_version=str(obj["evaluation_version"]),
            harness_version=str(obj.get("harness_version", HARNESS_VERSION)),
            mode=str(obj.get("mode", "development")),
            benchmark_version=str(obj.get("benchmark_version", "")),
            benchmark_sha256=str(obj.get("benchmark_sha256", "")),
            pae_commit=str(obj.get("pae_commit", "")),
            participant_snapshot_sha256=str(obj.get("participant_snapshot_sha256", "")),
            conditions=tuple(obj.get("conditions") or ()),
            models=tuple(ModelConfig.from_json_obj(m) for m in obj.get("models") or ()),
            judge=JudgeConfig.from_json_obj(obj.get("judge") or {}),
            repeats=dict(obj.get("repeats") or {}),
            repeat_strategy=str(obj.get("repeat_strategy", "first_repeat_confirmatory")),
            system_prompt_sha256=dict(obj.get("system_prompt_sha256") or {}),
            tool_catalog_sha256=dict(obj.get("tool_catalog_sha256") or {}),
            bundle_budget=dict(obj.get("bundle_budget") or {}),
            limits=dict(obj.get("limits") or {}),
            primary_comparison=(str(primary[0]), str(primary[1])),
            primary_endpoint=str(obj.get("primary_endpoint", "task_pass")),
            secondary_endpoints=tuple(obj.get("secondary_endpoints") or ()),
            exploratory_endpoints=tuple(obj.get("exploratory_endpoints") or ()),
            minimum_meaningful_effect_pp=float(
                obj.get("minimum_meaningful_effect_pp", 10.0)),
            non_inferiority_margin_pp=float(obj.get("non_inferiority_margin_pp", -5.0)),
            efficiency_target_token_reduction=float(
                obj.get("efficiency_target_token_reduction", 0.20)),
            multiple_comparison_policy=str(
                obj.get("multiple_comparison_policy", "holm_bonferroni_on_secondary")),
            retry_policy=dict(obj.get("retry_policy") or {}),
            exclusion_policy=dict(obj.get("exclusion_policy") or {}),
            randomization_seed=int(obj.get("randomization_seed", 0)),
            pricing_snapshot_sha256=str(obj.get("pricing_snapshot_sha256", "")),
            cost_ceiling_policy=dict(obj.get("cost_ceiling_policy") or {}),
            leakage_thresholds={
                **EXAMPLE_LEAKAGE_THRESHOLDS, **(obj.get("leakage_thresholds") or {})
            },
            bootstrap_resamples=int(obj.get("bootstrap_resamples", 10000)),
            notes=str(obj.get("notes", "")),
        )

    @classmethod
    def load(cls, path: Path) -> "EvaluationPlan":
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise UsageError(f"evaluation plan not found: {path}") from exc
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{path} is not valid JSON: {exc}") from exc
        return cls.from_json_obj(data)

    def write(self, path: Path) -> str:
        """Write the plan and its sidecar digest. Returns the digest."""
        path = Path(path)
        digest = canonical.write_canonical(path, self.to_json_obj())
        path.with_suffix(path.suffix + ".sha256").write_text(
            digest + "\n", encoding="utf-8"
        )
        return digest


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------


def validate_plan(plan: EvaluationPlan) -> list[str]:
    problems: list[str] = []

    unknown = [c for c in plan.conditions if c not in CONDITIONS]
    if unknown:
        problems.append(f"unknown conditions: {unknown}")
    if not plan.conditions:
        problems.append("a plan must name at least one condition")

    for condition in plan.primary_comparison:
        if condition not in plan.conditions:
            problems.append(
                f"primary comparison names condition {condition!r}, "
                "which the plan does not run"
            )
    if plan.primary_comparison[0] == plan.primary_comparison[1]:
        problems.append("primary comparison must name two different conditions")

    if plan.repeat_strategy not in REPEAT_STRATEGIES:
        problems.append(
            f"unknown repeat_strategy {plan.repeat_strategy!r}; "
            f"expected one of {sorted(REPEAT_STRATEGIES)}"
        )
    for condition in plan.conditions:
        if plan.repeats_for(condition) < 1:
            problems.append(f"condition {condition} must have at least one repeat")

    participants = [m for m in plan.models if m.role != "judge"]
    if not participants:
        problems.append("a plan needs at least one participant model")
    if not plan.model_for("primary"):
        problems.append(
            "no model has role 'primary'; the confirmatory analysis needs one "
            "designated family rather than an unplanned average of several"
        )
    for model in plan.models:
        if not model.provider or not model.model:
            problems.append("every model needs a provider and a model id")

    if plan.judge.provider and participants:
        primary = plan.model_for("primary")
        if (primary and primary.provider == plan.judge.provider
                and not plan.judge.allow_same_family):
            problems.append(
                "judge provider matches the primary participant family; set "
                "judge.allow_same_family to accept that bias explicitly"
            )

    if plan.minimum_meaningful_effect_pp <= 0:
        problems.append("minimum_meaningful_effect_pp must be positive")
    if plan.non_inferiority_margin_pp > 0:
        problems.append(
            "non_inferiority_margin_pp is a tolerance for being *worse* and "
            "should be negative or zero"
        )
    if plan.bootstrap_resamples < 1000:
        problems.append("bootstrap_resamples below 1000 gives an unstable interval")

    if plan.is_sealed:
        if not plan.benchmark_sha256:
            problems.append("a sealed plan must pin benchmark_sha256")
        if not plan.pae_commit:
            problems.append("a sealed plan must pin pae_commit")
        if not plan.participant_snapshot_sha256:
            problems.append("a sealed plan must pin participant_snapshot_sha256")
        if not plan.pricing_snapshot_sha256:
            problems.append(
                "a sealed plan must pin pricing_snapshot_sha256; without it, "
                "reported dollars cannot be recomputed"
            )
    return problems


def assert_matches_world(
    plan: EvaluationPlan,
    *,
    benchmark_sha256: str | None = None,
    pae_commit: str | None = None,
    snapshot_sha256: str | None = None,
    tool_catalog_sha256: Mapping[str, str] | None = None,
    system_prompt_sha256: Mapping[str, str] | None = None,
    development: bool = False,
) -> list[str]:
    """Compare the frozen plan against what is actually about to run.

    In sealed mode a mismatch raises. In development mode it is returned as a
    warning list so a developer can iterate, and the run carries a distinct
    development identity so its results can never be mistaken for sealed ones.
    """
    mismatches: list[str] = []

    def compare(label: str, expected: str | None, actual: str | None) -> None:
        if expected and actual and expected != actual:
            mismatches.append(f"{label}: plan has {expected}, world has {actual}")

    compare("benchmark_sha256", plan.benchmark_sha256, benchmark_sha256)
    compare("pae_commit", plan.pae_commit, pae_commit)
    compare("participant_snapshot_sha256",
            plan.participant_snapshot_sha256, snapshot_sha256)

    for name, expected in (plan.tool_catalog_sha256 or {}).items():
        actual = (tool_catalog_sha256 or {}).get(name)
        compare(f"tool_catalog_sha256[{name}]", expected, actual)
    for name, expected in (plan.system_prompt_sha256 or {}).items():
        actual = (system_prompt_sha256 or {}).get(name)
        compare(f"system_prompt_sha256[{name}]", expected, actual)

    if mismatches and plan.is_sealed and not development:
        raise FrozenPlanError(
            "refusing to execute a sealed run: the world no longer matches the "
            "frozen plan.\n  " + "\n  ".join(mismatches)
            + "\nCreate a new evaluation version rather than editing this one."
        )
    return mismatches


# --------------------------------------------------------------------------
# example plan
# --------------------------------------------------------------------------


def example_plan(*, mode: str = "development", **overrides: Any) -> EvaluationPlan:
    """The Phase 7A recommendation as a runnable template.

    Not the sealed plan. Model identifiers in particular are placeholders that
    must be re-verified against live provider documentation before any freeze —
    an alias is not a snapshot, and provider line-ups move.
    """
    defaults = EXAMPLE_PLAN_DEFAULTS
    plan = EvaluationPlan(
        evaluation_version="0.1.0-example",
        mode=mode,
        benchmark_version="",
        benchmark_sha256="",
        pae_commit="",
        participant_snapshot_sha256="",
        conditions=tuple(CONDITIONS),
        models=(
            ModelConfig(provider="anthropic", model="claude-opus-5", role="primary",
                        max_output_tokens=6000, effort="high"),
            ModelConfig(provider="openai", model="gpt-5.6-terra", role="robustness",
                        max_output_tokens=6000),
        ),
        judge=JudgeConfig(provider="openai", model="gpt-5.6-terra"),
        repeats=dict(defaults["repeats"]),
        repeat_strategy="first_repeat_confirmatory",
        system_prompt_sha256={},
        tool_catalog_sha256={},
        bundle_budget={"estimated_tokens": 8000, "max_resources": 25},
        limits={
            "max_tool_turns": defaults["max_tool_turns"],
            "tool_loop_timeout_s": defaults["tool_loop_timeout_s"],
            "model_call_timeout_s": defaults["model_call_timeout_s"],
            "tool_call_timeout_s": defaults["tool_call_timeout_s"],
        },
        primary_comparison=tuple(defaults["primary_comparison"]),
        primary_endpoint=str(defaults["primary_endpoint"]),
        secondary_endpoints=(
            "continuous_rubric_score", "recall_at_1", "recall_at_5", "scope_at_1",
            "kind_at_1", "safety_pass_rate", "total_tokens", "tool_calls",
        ),
        exploratory_endpoints=("per_task_class", "per_scope"),
        minimum_meaningful_effect_pp=float(defaults["minimum_meaningful_effect_pp"]),
        non_inferiority_margin_pp=float(defaults["non_inferiority_margin_pp"]),
        efficiency_target_token_reduction=float(
            defaults["efficiency_target_token_reduction"]),
        multiple_comparison_policy="holm_bonferroni_on_secondary",
        retry_policy={
            "infrastructure_max_attempts": 3,
            "base_delay_s": 1.0,
            "max_delay_s": 30.0,
            "jitter": True,
            "model_behaviour_retried": False,
        },
        exclusion_policy={
            "exclude_exhausted_infrastructure_failures": True,
            "retain_refusals_as_failures": True,
            "retain_non_discriminating_tasks": True,
        },
        randomization_seed=20260902,
        pricing_snapshot_sha256="",
        cost_ceiling_policy={
            "requires_explicit_max_cost_usd": True,
            "requires_explicit_max_trials": True,
            "abort_before_exceeding": True,
        },
        leakage_thresholds=dict(EXAMPLE_LEAKAGE_THRESHOLDS),
        bootstrap_resamples=int(defaults["bootstrap_resamples"]),
        notes=(
            "EXAMPLE PLAN — reflects the Phase 7A recommendation. Model ids, "
            "pricing and hashes must be re-verified and re-pinned before any "
            "sealed run. The second B/D repeat is a pre-planned robustness "
            "measurement; only repeat 0 enters the confirmatory McNemar."
        ),
    )
    if overrides:
        from dataclasses import replace

        plan = replace(plan, **overrides)
    return plan

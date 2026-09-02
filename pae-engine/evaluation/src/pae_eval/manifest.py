"""Run manifests and the trial schedule.

The schedule is materialized and hashed **before the first paid request**.
Generating order lazily as results arrive would make the execution order a
function of the results, which is the kind of degree of freedom that turns an
experiment into a story. Conditions are interleaved rather than blocked, so
provider drift over the course of a run cannot line up with the primary
contrast (spec §42, §79).

The manifest records everything a reviewer needs to answer "what exactly ran":
plan and benchmark hashes, the PAE commit, the snapshot digest, versions of
every moving part, the seed, and the pricing snapshot the dollars came from.
Never a credential — only the *names* of the variables that were required.
"""

from __future__ import annotations

import platform
import random
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from . import canonical
from .constants import HARNESS_VERSION, RUN_MANIFEST_SCHEMA, SCHEDULE_SCHEMA
from .redaction import safe_environment_names


# --------------------------------------------------------------------------
# schedule
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class ScheduledTrial:
    position: int
    task_id: str
    condition: str
    provider: str
    model: str
    model_config_sha256: str
    repeat_index: int
    trial_id: str
    #: For pairwise judging: whether this condition is shown on the left.
    judge_left: bool = False

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "position": self.position,
            "task_id": self.task_id,
            "condition": self.condition,
            "provider": self.provider,
            "model": self.model,
            "model_config_sha256": self.model_config_sha256,
            "repeat_index": self.repeat_index,
            "trial_id": self.trial_id,
            "judge_left": self.judge_left,
        }


@dataclass(frozen=True)
class TrialSchedule:
    trials: tuple[ScheduledTrial, ...]
    seed: int
    #: task_id -> which condition is shown on the left in pairwise judging.
    judge_order: Mapping[str, str] = field(default_factory=dict)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEDULE_SCHEMA,
            "seed": self.seed,
            "trial_count": len(self.trials),
            "judge_order": dict(self.judge_order),
            "trials": [t.to_json_obj() for t in self.trials],
        }

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    def write(self, path: Path) -> str:
        path = Path(path)
        digest = canonical.write_canonical(path, self.to_json_obj())
        path.with_suffix(path.suffix + ".sha256").write_text(
            digest + "\n", encoding="utf-8"
        )
        return digest


def build_schedule(
    *,
    task_ids: Sequence[str],
    plan: Any,
    trial_id_for: Any,
) -> TrialSchedule:
    """Materialize every planned trial in a seeded, interleaved order.

    Interleaving is not cosmetic. Running all of condition B and then all of
    condition D would confound the primary contrast with anything that changes
    between the two blocks — a provider deploy, a rate-limit regime, time of
    day. Shuffling the flat list of (task, condition, repeat) tuples removes
    that coupling.
    """
    rng = random.Random(plan.randomization_seed)
    participants = [m for m in plan.models if m.role != "judge"]

    entries: list[tuple[str, str, Any, int]] = []
    for task_id in task_ids:
        for condition in plan.conditions:
            for model in participants:
                for repeat in range(plan.repeats_for(condition)):
                    entries.append((task_id, condition, model, repeat))

    ordered = list(entries)
    rng.shuffle(ordered)

    first, second = plan.primary_comparison
    judge_order = {
        task_id: (first if rng.random() < 0.5 else second) for task_id in task_ids
    }

    trials: list[ScheduledTrial] = []
    for position, (task_id, condition, model, repeat) in enumerate(ordered):
        trials.append(ScheduledTrial(
            position=position,
            task_id=task_id,
            condition=condition,
            provider=model.provider,
            model=model.model,
            model_config_sha256=model.sha256,
            repeat_index=repeat,
            trial_id=trial_id_for(
                task_id=task_id, condition=condition, repeat_index=repeat,
                model_config_sha256=model.sha256,
            ),
            judge_left=judge_order.get(task_id) == condition,
        ))
    return TrialSchedule(trials=tuple(trials), seed=plan.randomization_seed,
                         judge_order=judge_order)


# --------------------------------------------------------------------------
# run manifest
# --------------------------------------------------------------------------


@dataclass
class RunManifest:
    run_id: str
    mode: str
    plan_sha256: str
    benchmark_sha256: str
    benchmark_version: str
    participant_snapshot_sha256: str
    schedule_sha256: str
    pae_commit: str
    pae_dirty: bool
    engine_version: str | None
    harness_version: str
    python_version: str
    platform: str
    dependency_inventory: Mapping[str, str]
    provider_models: Sequence[Mapping[str, Any]]
    provider_adapters: Sequence[Mapping[str, Any]]
    mcp_sdk_version: str | None
    ripgrep_version: str | None
    tool_catalog_sha256: Mapping[str, str]
    system_prompt_sha256: Mapping[str, str]
    judge_prompt_sha256: Mapping[str, str]
    randomization_seed: int
    retry_policy: Mapping[str, Any]
    pricing_snapshot_sha256: str
    output_dir: str
    credential_env_names: Sequence[str]
    started_at: str = ""
    notes: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": RUN_MANIFEST_SCHEMA,
            "run_id": self.run_id,
            "mode": self.mode,
            "started_at": self.started_at,
            "plan_sha256": self.plan_sha256,
            "benchmark_sha256": self.benchmark_sha256,
            "benchmark_version": self.benchmark_version,
            "participant_snapshot_sha256": self.participant_snapshot_sha256,
            "schedule_sha256": self.schedule_sha256,
            "pae_commit": self.pae_commit,
            "pae_dirty": self.pae_dirty,
            "engine_version": self.engine_version,
            "harness_version": self.harness_version,
            "python_version": self.python_version,
            "platform": self.platform,
            "dependency_inventory": dict(self.dependency_inventory),
            "provider_models": [dict(m) for m in self.provider_models],
            "provider_adapters": [dict(a) for a in self.provider_adapters],
            "mcp_sdk_version": self.mcp_sdk_version,
            "ripgrep_version": self.ripgrep_version,
            "tool_catalog_sha256": dict(self.tool_catalog_sha256),
            "system_prompt_sha256": dict(self.system_prompt_sha256),
            "judge_prompt_sha256": dict(self.judge_prompt_sha256),
            "randomization_seed": self.randomization_seed,
            "retry_policy": dict(self.retry_policy),
            "pricing_snapshot_sha256": self.pricing_snapshot_sha256,
            # Identity, not a local path: an absolute developer path is not
            # reproducible and is mild information leakage in a published
            # evidence package.
            "output_dir_identity": canonical.sha256_text(self.output_dir),
            "credential_env_names": list(self.credential_env_names),
            "notes": self.notes,
        }

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    def write(self, path: Path) -> str:
        path = Path(path)
        digest = canonical.write_canonical(path, self.to_json_obj())
        path.with_suffix(path.suffix + ".sha256").write_text(
            digest + "\n", encoding="utf-8"
        )
        return digest


def dependency_inventory(names: Iterable[str] = ()) -> dict[str, str]:
    """Installed versions of the packages that could change a result."""
    import importlib.metadata as md

    wanted = list(names) or ["mcp", "anthropic", "openai", "scipy"]
    found: dict[str, str] = {}
    for name in wanted:
        try:
            found[name] = md.version(name)
        except Exception:
            found[name] = "not installed"
    return found


def engine_version() -> str | None:
    try:
        from pae_engine._version import __version__

        return __version__
    except Exception:
        return None


def environment_summary() -> dict[str, Any]:
    return {
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "credential_env_names": safe_environment_names(),
        "harness_version": HARNESS_VERSION,
    }

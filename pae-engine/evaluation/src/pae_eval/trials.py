"""Trial identity, append-only storage and resume.

Three properties, each chosen to make a result hard to quietly change.

**Identity is derived, not random.** A trial ID is a hash of the things that
define it — evaluation version, benchmark, task, condition, model config,
repeat, plan. Two runs of the same design produce the same IDs, so resume is
exact and a result cannot be silently re-attributed. A random UUID would make
every run incomparable to every other.

**Storage is append-only.** Every attempt writes one line. Nothing is ever
rewritten in place, so a re-run cannot overwrite the record of what happened
the first time; §53 requires the original run survive.

**Resume is conservative.** It skips only trial IDs already recorded as
terminal, and only when the plan, benchmark and model hashes still match. A
changed config is a different experiment and gets a different run.
"""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence

from . import canonical
from .constants import TRIAL_SCHEMA
from .errors import FrozenPlanError, UsageError
from .redaction import redact

TRIALS_FILENAME = "trials.jsonl"


# --------------------------------------------------------------------------
# identity
# --------------------------------------------------------------------------


def trial_id(
    *,
    evaluation_version: str,
    benchmark_sha256: str,
    task_id: str,
    condition: str,
    model_config_sha256: str,
    repeat_index: int,
    plan_sha256: str,
) -> str:
    """Deterministic, collision-resistant, and readable at a glance."""
    digest = canonical.sha256_obj({
        "evaluation_version": evaluation_version,
        "benchmark_sha256": benchmark_sha256,
        "task_id": task_id,
        "condition": condition,
        "model_config_sha256": model_config_sha256,
        "repeat_index": repeat_index,
        "plan_sha256": plan_sha256,
    })
    return f"{task_id}:{condition}:r{repeat_index}:{canonical.short(digest, 10)}"


def model_config_hash(config: Mapping[str, Any]) -> str:
    """Hash of a model configuration, credentials excluded by construction."""
    return canonical.sha256_obj({
        k: v for k, v in sorted(config.items())
        if k not in ("api_key", "credential", "token")
    })


# --------------------------------------------------------------------------
# records
# --------------------------------------------------------------------------


@dataclass
class TrialRecord:
    """One attempt. Written once, never edited."""

    trial_id: str
    run_id: str
    task_id: str
    condition: str
    repeat_index: int
    attempt_no: int
    evaluation_version: str
    benchmark_version: str
    benchmark_sha256: str
    plan_sha256: str
    participant_provider: str
    participant_model: str
    model_parameters: Mapping[str, Any]
    model_parameters_sha256: str
    system_prompt_sha256: str
    task_sha256: str
    pae_commit: str
    pae_dirty: bool
    engine_version: str | None
    mcp_sdk_version: str | None
    tool_catalog_sha256: str
    participant_snapshot_sha256: str
    pricing_snapshot_sha256: str
    started_at: str
    ended_at: str
    latency_ms: float
    state: str
    stop_reason: str
    final_answer: str
    observable_tool_calls: Sequence[Mapping[str, Any]]
    usage: Mapping[str, Any]
    error_class: str | None
    retry_state: Mapping[str, Any]
    estimated_cost_usd: float
    reported_model: str | None = None
    provider_response_id: str | None = None
    route_bundle: Mapping[str, Any] | None = None
    condition_observability: Mapping[str, Any] = field(default_factory=dict)
    raw_provider_payload: Mapping[str, Any] | None = None

    def to_json_obj(self) -> dict[str, Any]:
        obj = {
            "schema_version": TRIAL_SCHEMA,
            "evaluation_version": self.evaluation_version,
            "benchmark_version": self.benchmark_version,
            "run_id": self.run_id,
            "trial_id": self.trial_id,
            "attempt_no": self.attempt_no,
            "task_id": self.task_id,
            "condition": self.condition,
            "repeat_index": self.repeat_index,
            "participant_provider": self.participant_provider,
            "participant_model": self.participant_model,
            "reported_model": self.reported_model,
            "model_parameters": dict(self.model_parameters),
            "model_parameters_sha256": self.model_parameters_sha256,
            "system_prompt_sha256": self.system_prompt_sha256,
            "task_sha256": self.task_sha256,
            "benchmark_sha256": self.benchmark_sha256,
            "plan_sha256": self.plan_sha256,
            "pae_commit": self.pae_commit,
            "pae_dirty": self.pae_dirty,
            "engine_version": self.engine_version,
            "mcp_sdk_version": self.mcp_sdk_version,
            "tool_catalog_sha256": self.tool_catalog_sha256,
            "participant_snapshot_sha256": self.participant_snapshot_sha256,
            "pricing_snapshot_sha256": self.pricing_snapshot_sha256,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "latency_ms": round(self.latency_ms, 2),
            "provider_response_id": self.provider_response_id,
            "state": self.state,
            "stop_reason": self.stop_reason,
            "final_answer": self.final_answer,
            "observable_tool_calls": [dict(c) for c in self.observable_tool_calls],
            "usage": dict(self.usage),
            "error_class": self.error_class,
            "retry_state": dict(self.retry_state),
            "estimated_cost_usd": self.estimated_cost_usd,
            "condition_observability": dict(self.condition_observability),
        }
        if self.route_bundle is not None:
            obj["route_bundle"] = dict(self.route_bundle)
        if self.raw_provider_payload is not None:
            obj["raw_provider_payload"] = dict(self.raw_provider_payload)
        # No chain-of-thought field exists, and none is ever populated.
        return obj


# --------------------------------------------------------------------------
# append-only store
# --------------------------------------------------------------------------


class TrialStore:
    """Append-only JSONL. One line per attempt, flushed and fsynced."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: TrialRecord) -> str:
        """Write one record, redacted. Returns its canonical line."""
        payload = redact(record.to_json_obj())
        line = canonical.canonical_json(payload)
        with open(self.path, "a", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return line

    def read(self) -> Iterator[dict[str, Any]]:
        if not self.path.exists():
            return iter(())
        def _iter() -> Iterator[dict[str, Any]]:
            with open(self.path, encoding="utf-8") as handle:
                for number, raw in enumerate(handle, 1):
                    raw = raw.strip()
                    if not raw:
                        continue
                    try:
                        yield json.loads(raw)
                    except json.JSONDecodeError as exc:
                        raise UsageError(
                            f"{self.path}:{number} is not valid JSON: {exc}"
                        ) from exc
        return _iter()

    # -- resume ------------------------------------------------------------

    def completed_trial_ids(self, *, terminal_states: Iterable[str] = ()) -> set[str]:
        """Trial IDs already recorded in a terminal state.

        An attempt that failed retryably is not terminal: resuming should try
        it again, because the run never got an answer for it.
        """
        terminal = set(terminal_states) or {"completed"}
        done: set[str] = set()
        for row in self.read():
            if row.get("state") in terminal:
                done.add(str(row.get("trial_id")))
        return done

    def assert_resumable(self, *, plan_sha256: str, benchmark_sha256: str,
                         snapshot_sha256: str) -> None:
        """Refuse to resume into a run whose design has moved."""
        for row in self.read():
            mismatches = []
            if row.get("plan_sha256") not in (None, plan_sha256):
                mismatches.append("evaluation plan")
            if row.get("benchmark_sha256") not in (None, benchmark_sha256):
                mismatches.append("benchmark")
            if row.get("participant_snapshot_sha256") not in (None, snapshot_sha256):
                mismatches.append("participant snapshot")
            if mismatches:
                raise FrozenPlanError(
                    "refusing to resume: the "
                    + ", ".join(mismatches)
                    + " changed since these trials were written. "
                    "A different configuration is a different run — start a new "
                    "run id rather than mixing evidence."
                )
            break  # every row carries the same hashes; one is enough


def new_run_id(*, plan_sha256: str, benchmark_sha256: str, snapshot_sha256: str,
               label: str = "") -> str:
    """A run id derived from the design, so the same design resumes itself."""
    digest = canonical.sha256_obj({
        "plan": plan_sha256,
        "benchmark": benchmark_sha256,
        "snapshot": snapshot_sha256,
        "label": label,
    })
    return f"run-{canonical.short(digest, 12)}"

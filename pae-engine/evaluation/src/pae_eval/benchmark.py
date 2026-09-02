"""Benchmark loading, validation and label semantics.

This phase does not author the sealed benchmark; it defines the contract a
later, independently authored benchmark must satisfy, and refuses one that
does not.

The load-bearing schema decision is that **an empty list is never ambiguous**.
``acceptable_scopes: []`` could mean "no scope is acceptable" or "scope is not
scored here", and a scorer that guesses will silently mark correct answers
wrong on a whole stratum. So ``scored_dimensions`` states which dimensions are
graded, and an empty acceptable-list on a *scored* dimension is a validation
error rather than a silent zero (spec §18).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from . import canonical
from .constants import (
    AUTHOR_KINDS,
    AUTHORING_MODES,
    BENCHMARK_SCHEMA,
    CANONICAL_POLICIES,
    RESOURCE_GRADES,
    RESOURCE_KINDS,
    ROUTE_STATUSES,
    SCORED_DIMENSIONS,
    TASK_CLASSES,
    TASK_TAGS,
)
from .errors import UsageError, ValidationError


# --------------------------------------------------------------------------
# records
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class AcceptableResource:
    uid: str
    grade: str = "primary"

    def to_json_obj(self) -> dict[str, Any]:
        return {"uid": self.uid, "grade": self.grade}


@dataclass(frozen=True)
class Criterion:
    criterion_id: str
    description: str
    type: str  # "deterministic" | "judge"
    weight: float = 0.0
    required: bool = False
    deterministic_rule: Mapping[str, Any] | None = None
    judge_instruction: str = ""
    failure_gate: bool = False

    def to_json_obj(self) -> dict[str, Any]:
        obj: dict[str, Any] = {
            "criterion_id": self.criterion_id,
            "description": self.description,
            "type": self.type,
            "weight": self.weight,
            "required": self.required,
            "failure_gate": self.failure_gate,
        }
        if self.deterministic_rule is not None:
            obj["deterministic_rule"] = dict(self.deterministic_rule)
        if self.judge_instruction:
            obj["judge_instruction"] = self.judge_instruction
        return obj


@dataclass(frozen=True)
class Task:
    task_id: str
    benchmark_version: str
    task_class: str
    query: str
    deliverable: str
    criteria: tuple[Criterion, ...]
    scored_dimensions: tuple[str, ...]
    acceptable_resource_uids: tuple[AcceptableResource, ...] = ()
    acceptable_scopes: tuple[str, ...] = ()
    acceptable_kinds: tuple[str, ...] = ()
    acceptable_route_statuses: tuple[str, ...] = ()
    canonical_policy: str = "canonical_or_registered_copy_both_credited"
    label_rationale: str = ""
    label_provenance: Mapping[str, Any] = field(default_factory=dict)
    leakage_audit: Mapping[str, Any] = field(default_factory=dict)
    tags: tuple[str, ...] = ()

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    def scores(self, dimension: str) -> bool:
        return dimension in self.scored_dimensions

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "benchmark_version": self.benchmark_version,
            "class": self.task_class,
            "query": self.query,
            "deliverable": self.deliverable,
            "rubric": {"criteria": [c.to_json_obj() for c in self.criteria]},
            "scored_dimensions": list(self.scored_dimensions),
            "acceptable_resource_uids": [
                r.to_json_obj() for r in self.acceptable_resource_uids
            ],
            "acceptable_scopes": list(self.acceptable_scopes),
            "acceptable_kinds": list(self.acceptable_kinds),
            "acceptable_route_statuses": list(self.acceptable_route_statuses),
            "canonical_policy": self.canonical_policy,
            "label_rationale": self.label_rationale,
            "label_provenance": dict(self.label_provenance),
            "leakage_audit": dict(self.leakage_audit),
            "tags": list(self.tags),
        }

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "Task":
        rubric = obj.get("rubric") or {}
        criteria = tuple(
            Criterion(
                criterion_id=str(c.get("criterion_id", "")),
                description=str(c.get("description", "")),
                type=str(c.get("type", "judge")),
                weight=float(c.get("weight", 0.0) or 0.0),
                required=bool(c.get("required", False)),
                deterministic_rule=c.get("deterministic_rule"),
                judge_instruction=str(c.get("judge_instruction", "")),
                failure_gate=bool(c.get("failure_gate", False)),
            )
            for c in (rubric.get("criteria") or [])
        )
        return cls(
            task_id=str(obj.get("task_id", "")),
            benchmark_version=str(obj.get("benchmark_version", "")),
            task_class=str(obj.get("class", "")),
            query=str(obj.get("query", "")),
            deliverable=str(obj.get("deliverable", "")),
            criteria=criteria,
            scored_dimensions=tuple(obj.get("scored_dimensions") or ()),
            acceptable_resource_uids=tuple(
                AcceptableResource(uid=str(r.get("uid", "")),
                                   grade=str(r.get("grade", "primary")))
                if isinstance(r, Mapping) else AcceptableResource(uid=str(r))
                for r in (obj.get("acceptable_resource_uids") or ())
            ),
            acceptable_scopes=tuple(obj.get("acceptable_scopes") or ()),
            acceptable_kinds=tuple(obj.get("acceptable_kinds") or ()),
            acceptable_route_statuses=tuple(obj.get("acceptable_route_statuses") or ()),
            canonical_policy=str(
                obj.get("canonical_policy", "canonical_or_registered_copy_both_credited")
            ),
            label_rationale=str(obj.get("label_rationale", "")),
            label_provenance=dict(obj.get("label_provenance") or {}),
            leakage_audit=dict(obj.get("leakage_audit") or {}),
            tags=tuple(obj.get("tags") or ()),
        )


@dataclass(frozen=True)
class Benchmark:
    version: str
    tasks: tuple[Task, ...]
    manifest: Mapping[str, Any] = field(default_factory=dict)
    root: Path | None = None

    @property
    def sha256(self) -> str:
        """Hash of the task set, independent of file layout on disk."""
        return canonical.sha256_obj({
            "schema_version": BENCHMARK_SCHEMA,
            "benchmark_version": self.version,
            "tasks": [t.to_json_obj() for t in
                      sorted(self.tasks, key=lambda t: t.task_id)],
        })

    def __len__(self) -> int:
        return len(self.tasks)

    def by_id(self, task_id: str) -> Task | None:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------


def load_benchmark(root: Path) -> Benchmark:
    """Load ``manifest.json`` plus ``tasks/*.json`` from a benchmark root."""
    root = Path(root)
    if not root.is_dir():
        raise UsageError(f"benchmark root is not a directory: {root}")

    manifest_path = root / "manifest.json"
    manifest: dict[str, Any] = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{manifest_path} is not valid JSON: {exc}") from exc

    tasks_dir = root / "tasks"
    files = sorted(tasks_dir.glob("*.json")) if tasks_dir.is_dir() else []
    if not files:
        raise ValidationError(
            f"no task files found under {tasks_dir}; a benchmark needs tasks/*.json"
        )

    tasks: list[Task] = []
    problems: list[str] = []
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"{path.name}: not valid JSON: {exc}")
            continue
        entries = payload if isinstance(payload, list) else [payload]
        for entry in entries:
            if not isinstance(entry, Mapping):
                problems.append(f"{path.name}: task entries must be objects")
                continue
            tasks.append(Task.from_json_obj(entry))
    if problems:
        raise ValidationError("benchmark could not be loaded", problems)

    version = str(manifest.get("benchmark_version")
                  or (tasks[0].benchmark_version if tasks else "0.0.0"))
    return Benchmark(version=version, tasks=tuple(tasks), manifest=manifest, root=root)


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------


def validate_benchmark(
    benchmark: Benchmark,
    *,
    known_uids: Iterable[str] | None = None,
    known_scopes: Iterable[str] | None = None,
    require_provenance: bool = True,
) -> list[str]:
    """Structural and semantic validation. Returns problems; empty means valid."""
    problems: list[str] = []
    uids = set(known_uids) if known_uids is not None else None
    scopes = set(known_scopes) if known_scopes is not None else None

    seen: set[str] = set()
    for task in benchmark.tasks:
        where = task.task_id or "<missing task_id>"

        if not task.task_id:
            problems.append("a task has no task_id")
        elif task.task_id in seen:
            problems.append(f"{where}: duplicate task_id")
        seen.add(task.task_id)

        if task.task_class not in TASK_CLASSES:
            problems.append(
                f"{where}: unknown class {task.task_class!r}; "
                f"expected one of {sorted(TASK_CLASSES)}"
            )
        if not task.query.strip():
            problems.append(f"{where}: query is empty")
        if not task.deliverable.strip():
            problems.append(f"{where}: deliverable is empty")

        for tag in task.tags:
            if tag not in TASK_TAGS:
                problems.append(f"{where}: unknown tag {tag!r}")

        # -- scored dimensions: the anti-ambiguity rule --------------------
        unknown_dims = [d for d in task.scored_dimensions if d not in SCORED_DIMENSIONS]
        if unknown_dims:
            problems.append(f"{where}: unknown scored_dimensions {unknown_dims}")

        pairs = (
            ("resource", task.acceptable_resource_uids),
            ("scope", task.acceptable_scopes),
            ("kind", task.acceptable_kinds),
            ("route_status", task.acceptable_route_statuses),
        )
        for dimension, values in pairs:
            if dimension in task.scored_dimensions and not values:
                problems.append(
                    f"{where}: '{dimension}' is listed in scored_dimensions but its "
                    "acceptable list is empty — state the acceptable answers, or "
                    "drop the dimension from scored_dimensions"
                )
            if dimension not in task.scored_dimensions and values:
                problems.append(
                    f"{where}: acceptable values given for unscored dimension "
                    f"'{dimension}' — add it to scored_dimensions or remove them"
                )

        for kind in task.acceptable_kinds:
            if kind not in RESOURCE_KINDS:
                problems.append(f"{where}: unknown kind {kind!r}")
        for status in task.acceptable_route_statuses:
            if status not in ROUTE_STATUSES:
                problems.append(f"{where}: unknown route status {status!r}")
        for resource in task.acceptable_resource_uids:
            if resource.grade not in RESOURCE_GRADES:
                problems.append(
                    f"{where}: unknown grade {resource.grade!r} on {resource.uid}"
                )
            if uids is not None and resource.uid not in uids:
                problems.append(f"{where}: label does not resolve: {resource.uid}")
        if scopes is not None:
            for scope in task.acceptable_scopes:
                if scope not in scopes:
                    problems.append(f"{where}: unknown scope {scope!r}")

        if task.canonical_policy not in CANONICAL_POLICIES:
            problems.append(f"{where}: unknown canonical_policy {task.canonical_policy!r}")

        # -- no-route tasks must not also demand a resource ----------------
        if task.acceptable_route_statuses and set(task.acceptable_route_statuses) <= {
            "weak", "no_route"
        } and task.acceptable_resource_uids:
            problems.append(
                f"{where}: a weak/no_route task must not also require a resource; "
                "the correct behaviour there is declining to route"
            )

        problems.extend(_validate_rubric(task))
        if require_provenance:
            problems.extend(_validate_provenance(task))

    return problems


def _validate_rubric(task: Task) -> list[str]:
    problems: list[str] = []
    where = task.task_id
    if not task.criteria:
        problems.append(f"{where}: rubric has no criteria")
        return problems

    ids: set[str] = set()
    for criterion in task.criteria:
        if not criterion.criterion_id:
            problems.append(f"{where}: a criterion has no criterion_id")
        elif criterion.criterion_id in ids:
            problems.append(f"{where}: duplicate criterion_id {criterion.criterion_id!r}")
        ids.add(criterion.criterion_id)

        if criterion.type not in ("deterministic", "judge"):
            problems.append(
                f"{where}/{criterion.criterion_id}: type must be "
                "'deterministic' or 'judge'"
            )
        if criterion.type == "deterministic" and not criterion.deterministic_rule:
            problems.append(
                f"{where}/{criterion.criterion_id}: a deterministic criterion "
                "needs a deterministic_rule"
            )
        if criterion.type == "judge" and not criterion.judge_instruction:
            problems.append(
                f"{where}/{criterion.criterion_id}: a judge criterion needs a "
                "judge_instruction"
            )
        if criterion.weight < 0:
            problems.append(f"{where}/{criterion.criterion_id}: negative weight")

    total = sum(c.weight for c in task.criteria)
    if total > 0 and abs(total - 1.0) > 1e-6:
        problems.append(
            f"{where}: criterion weights sum to {total:.4f}, expected 1.0"
        )
    if not any(c.required for c in task.criteria):
        problems.append(
            f"{where}: no criterion is marked required, so the binary pass "
            "endpoint would be undefined for this task"
        )
    return problems


def _validate_provenance(task: Task) -> list[str]:
    problems: list[str] = []
    where = task.task_id
    provenance = task.label_provenance or {}

    mode = provenance.get("authoring_mode")
    if mode not in AUTHORING_MODES:
        problems.append(
            f"{where}: label_provenance.authoring_mode must be one of "
            f"{sorted(AUTHORING_MODES)}, got {mode!r}"
        )

    for role in ("author", "reviewer"):
        actor = provenance.get(role)
        if not isinstance(actor, Mapping):
            problems.append(f"{where}: label_provenance.{role} is missing")
            continue
        kind = actor.get("kind")
        if kind not in AUTHOR_KINDS:
            problems.append(
                f"{where}: label_provenance.{role}.kind must be 'human' or 'ai'"
            )
        if kind == "ai":
            # An AI-authored task set must never be describable as
            # human-authored, so the fields that make that visible are required.
            for required in ("provider", "model", "date", "prompt_sha256"):
                if not actor.get(required):
                    problems.append(
                        f"{where}: label_provenance.{role} is AI-authored and "
                        f"must record {required}"
                    )
            if actor.get("saw_pae_metadata") is None:
                problems.append(
                    f"{where}: label_provenance.{role} must record "
                    "saw_pae_metadata (true or false)"
                )
    if not task.label_rationale.strip():
        problems.append(f"{where}: label_rationale is empty")
    return problems


# --------------------------------------------------------------------------
# label semantics (spec §19)
# --------------------------------------------------------------------------


def resource_is_correct(task: Task, retrieved_uid: str,
                        cluster_of: Mapping[str, str] | None = None) -> bool:
    """Whether a retrieved UID satisfies the task's resource label.

    Under the default policy a canonical resource and a registered copy are one
    logical answer: either earns credit, and credit is per cluster so returning
    both is not worth double.
    """
    acceptable = {r.uid for r in task.acceptable_resource_uids}
    if retrieved_uid in acceptable:
        return True
    if task.canonical_policy != "canonical_or_registered_copy_both_credited":
        return False
    if not cluster_of:
        return False
    retrieved_cluster = cluster_of.get(retrieved_uid)
    if retrieved_cluster is None:
        return False
    return any(cluster_of.get(uid) == retrieved_cluster for uid in acceptable)


def collapse_clusters(uids: Sequence[str],
                      cluster_of: Mapping[str, str] | None) -> list[str]:
    """Deduplicate a ranked list by cluster, preserving order."""
    if not cluster_of:
        return list(dict.fromkeys(uids))
    seen: set[str] = set()
    out: list[str] = []
    for uid in uids:
        key = cluster_of.get(uid, uid)
        if key in seen:
            continue
        seen.add(key)
        out.append(uid)
    return out


def route_status_is_correct(task: Task, status: str) -> bool:
    """Whether a router status satisfies the task.

    Where a task accepts only ``ambiguous``, a confident ``matched`` is wrong.
    That asymmetry is the entire point of the false-confidence stratum.
    """
    if not task.scores("route_status"):
        return True
    return status in task.acceptable_route_statuses


def expects_no_route(task: Task) -> bool:
    return bool(task.acceptable_route_statuses) and set(
        task.acceptable_route_statuses
    ) <= {"weak", "no_route"}


# --------------------------------------------------------------------------
# composition (spec §94)
# --------------------------------------------------------------------------


def composition_report(benchmark: Benchmark,
                       records: Mapping[str, Mapping[str, Any]] | None = None
                       ) -> dict[str, Any]:
    """What is actually in a benchmark, computable before any model runs."""
    from collections import Counter

    classes = Counter(t.task_class for t in benchmark.tasks)
    modes = Counter(
        (t.label_provenance or {}).get("authoring_mode", "unknown")
        for t in benchmark.tasks
    )
    author_kinds = Counter(
        ((t.label_provenance or {}).get("author") or {}).get("kind", "unknown")
        for t in benchmark.tasks
    )

    scopes: Counter = Counter()
    kinds: Counter = Counter()
    policies: Counter = Counter()
    descriptionless = 0
    for task in benchmark.tasks:
        scopes.update(task.acceptable_scopes)
        kinds.update(task.acceptable_kinds)
        if records:
            for resource in task.acceptable_resource_uids:
                record = records.get(resource.uid) or {}
                policy = (record.get("serving_policy") or {}).get("value")
                if policy:
                    policies[policy] += 1
                if not record.get("description"):
                    descriptionless += 1

    multi = sum(1 for t in benchmark.tasks if len(t.acceptable_resource_uids) > 1)
    exact_title = sum(
        1 for t in benchmark.tasks
        if (t.leakage_audit or {}).get("title_token_containment") is True
    )

    return {
        "task_count": len(benchmark.tasks),
        "class_distribution": dict(sorted(classes.items())),
        "scope_distribution": dict(sorted(scopes.items())),
        "kind_distribution": dict(sorted(kinds.items())),
        "serving_policy_distribution": dict(sorted(policies.items())),
        "authoring_modes": dict(sorted(modes.items())),
        "author_kinds": dict(sorted(author_kinds.items())),
        "descriptionless_target_count": descriptionless,
        "multi_acceptable_count": multi,
        "exact_title_count": exact_title,
        "distinct_scopes": len(scopes),
        "tagged_safety_behavior": sum(
            1 for t in benchmark.tasks if "safety_behavior" in t.tags
        ),
        "tagged_adversarial_governance": sum(
            1 for t in benchmark.tasks if "adversarial_governance" in t.tags
        ),
    }

"""Deterministic masked-target selection (spec §4).

The selection must be defensible after the fact, which rules out anything that
could have been re-rolled. So there is no random number generator here at all.
A target's position in the draw is ``SHA256(seed || uid)``, sorted ascending:
the order is a pure function of the seed and the eligible population, the seed
is a pure function of the commit, and re-running the selection on the same
commit reproduces it exactly. "We resampled until the mix looked right" is not
a statement anyone can make about this code.

Two rules keep it honest when a chosen target turns out to be unusable:

* **Mechanical ineligibility only.** A target is skipped for a structural
  reason — dead body, wrong serving policy, reserved by the development set —
  and every skip is recorded with its reason. Inconvenience is not a reason.
* **Next candidate, not a new draw.** The replacement is the next resource in
  the same deterministic order, so a skip perturbs one slot rather than
  reshuffling the benchmark.

## Why the recommended kind allocation is not the implemented one

Phase 8A recommends ``skill 12 / agent 8 / command 8 / persona 5 / prompt 12``
alongside a hard requirement of *exactly 18 safety-gated class packets*. In
this corpus those cannot both hold: ``serving_policy == "safety_gated"`` occurs
on prompts and on nothing else (1319 prompts; zero skills, agents, commands or
personas). Eighteen safety-gated packets therefore require eighteen prompts,
and a twelve-prompt allocation is unreachable.

The class counts are stated as requirements and the kind allocation as a
recommendation, so the requirements win. ``DEFAULT_KIND_QUOTAS`` holds prompts
at the forced minimum of 18 and distributes the remaining 27 slots across the
non-prompt kinds in the recommendation's own ratio (12:8:8:5 → 10:7:6:4). That
is the closest achievable point to the recommendation, and it preserves what
the recommendation was for: over-weighting the kinds the corpus under-weights.
The deviation is reported rather than silently absorbed.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .. import canonical
from ..errors import UsageError, ValidationError

#: Bumped whenever a change would move a target between slots for a fixed seed.
SELECTION_ALGORITHM_VERSION = "masked-target-selection/1"

#: The domain-separation prefix from spec §4. Changing this string changes
#: every selection, which is why it is a constant and not a parameter.
SEED_PREFIX = "pae-independent-benchmark-masked-targets-v1"

#: Serving policies whose bodies may be masked into an author packet.
#: ``metadata_only`` is absent on purpose: there is no body to sanitize.
ELIGIBLE_SERVING_POLICIES = ("standard", "safety_gated")

#: Techniques have no independently addressable body — a technique's content
#: lives inside the master index rather than in a file of its own — so they can
#: never be a masked-body target (spec §4).
INELIGIBLE_KINDS = ("technique",)

#: Class → how many packets, from the spec's masked-derived allocation (§3).
DEFAULT_CLASS_QUOTAS: Mapping[str, int] = {
    "safety_gated": 18,
    "non_prompt_kind": 20,
    "ordinary_task": 7,
}

#: Kind → how many of the 45. See the module docstring for why this is not the
#: literal recommendation.
DEFAULT_KIND_QUOTAS: Mapping[str, int] = {
    "prompt": 18,
    "skill": 10,
    "agent": 7,
    "command": 6,
    "persona": 4,
}

#: No single scope may dominate the masked half (spec §4).
DEFAULT_MAX_PER_SCOPE = 4

#: The masked half must span at least this many scopes (spec §4).
DEFAULT_MIN_DISTINCT_SCOPES = 20

#: Strata are filled in a fixed order because the per-scope cap is global: a
#: different order would give a different (still deterministic) answer, and the
#: order therefore belongs in the algorithm rather than in a caller's argument
#: list. Safety-gated goes first because it is by far the most constrained —
#: ten scopes for eighteen packets.
STRATUM_ORDER = ("safety_gated", "skill", "agent", "command", "persona")

_SPLIT_SCOPE = "agentic-resources"


# --------------------------------------------------------------------------
# registry access
# --------------------------------------------------------------------------


def registry_path(repo: Path) -> Path:
    return Path(repo) / "meta" / "registry" / "registry.jsonl"


def load_registry_records(repo: Path) -> list[dict[str, Any]]:
    """Every Registry record, as plain JSON.

    Read from the generated artifact with the standard library rather than
    through the Engine. Selection is not search: it needs identity, lifecycle
    and serving policy, none of which the ranking layer should be involved in
    deciding.
    """
    path = registry_path(repo)
    if not path.is_file():
        raise UsageError(f"registry not found: {path}")
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValidationError(f"{path}:{number}: invalid JSON: {exc}") from exc
    return records


def derive_scope(record: Mapping[str, Any]) -> str:
    """The routing unit for a record, computed from its public ID.

    Deliberately a local reimplementation over raw JSON rather than an import
    of the Engine's ``derive_scope``: this module and the reviewer's candidate
    discovery both need scopes without depending on the search layer.
    ``test_authoring_selection`` asserts the two agree on every record in the
    Registry, so the duplication cannot drift unnoticed.
    """
    kind = str(record.get("kind") or "")
    public_id = str(record.get("id") or "")
    rest = public_id.split(":", 1)[1] if ":" in public_id else public_id
    segments = [s for s in rest.split("/") if s]

    if kind == "technique":
        category = (record.get("native") or {}).get("category") or ""
        if isinstance(category, (list, tuple)):
            category = " ".join(str(c) for c in category)
        category = str(category).strip()
        if category:
            return category.casefold()
        return segments[0].casefold() if segments else ""

    if not segments:
        return ""
    if segments[0] == _SPLIT_SCOPE and len(segments) > 1:
        return f"{_SPLIT_SCOPE}/{segments[1]}".casefold()
    return segments[0].casefold()


def cluster_key(record: Mapping[str, Any]) -> str:
    """Canonical cluster of a record: a copy joins its canonical's cluster.

    Exclusions are recorded per cluster, not per UID, so reserving a resource
    for the development set also reserves its registered copies. Otherwise the
    sealed benchmark could draw a copy of a development target and the two sets
    would silently overlap.
    """
    relationships = record.get("relationships") or {}
    copy_of = relationships.get("copy_of")
    if isinstance(copy_of, str) and copy_of:
        return copy_of
    return str(record.get("uid") or "")


# --------------------------------------------------------------------------
# seed and order
# --------------------------------------------------------------------------


def selection_seed(target_pae_commit: str) -> str:
    """``SHA256(prefix + "\\n" + commit)`` — spec §4, verbatim."""
    commit = str(target_pae_commit).strip()
    if not commit:
        raise UsageError("a selection seed needs the target PAE commit")
    payload = f"{SEED_PREFIX}\n{commit}".encode("utf-8")
    return canonical.DIGEST_PREFIX + hashlib.sha256(payload).hexdigest()


def draw_position(seed: str, uid: str) -> str:
    """Where ``uid`` sits in the draw. Pure function of (seed, uid)."""
    payload = f"{seed}\n{uid}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# --------------------------------------------------------------------------
# eligibility
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Candidate:
    uid: str
    public_id: str
    kind: str
    scope: str
    cluster: str
    serving_policy: str
    source_path: str
    position: str

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "uid": self.uid,
            "public_id": self.public_id,
            "kind": self.kind,
            "scope": self.scope,
            "cluster": self.cluster,
            "serving_policy": self.serving_policy,
            "source_path": self.source_path,
            "draw_position": self.position,
        }


@dataclass(frozen=True)
class Exclusion:
    uid: str
    reason: str
    detail: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        return {"uid": self.uid, "reason": self.reason, "detail": self.detail}


def _verify_body(repo: Path, record: Mapping[str, Any]) -> str:
    """Empty string when the body is addressable and matches its checksum.

    A target whose file has moved, emptied or drifted from its recorded digest
    cannot be masked into a packet: the author would receive bytes the Registry
    does not vouch for. Checking here rather than at export time means the
    replacement is drawn deterministically instead of patched in by hand.
    """
    source = record.get("source") or {}
    rel = str(source.get("path") or "")
    if not rel:
        return "record has no source path"
    path = Path(repo) / rel
    if not path.is_file():
        return f"source path does not exist: {rel}"
    try:
        actual = canonical.sha256_file(path)
    except OSError as exc:
        return f"source path unreadable: {exc}"
    expected = str(source.get("content_sha256") or "")
    if expected and actual != expected:
        return "body does not match its recorded content_sha256"
    if path.stat().st_size == 0:
        return "source body is empty"
    return ""


def eligible_candidates(
    records: Sequence[Mapping[str, Any]],
    repo: Path,
    *,
    seed: str,
    excluded_clusters: Iterable[str] = (),
    excluded_uids: Iterable[str] = (),
) -> tuple[list[Candidate], list[Exclusion], dict[str, int]]:
    """Eligible population in draw order, plus every exclusion and the counts.

    Exclusion reasons are recorded for the whole population, not just for
    resources that would have been drawn early, so the manifest can state how
    large the eligible pool actually was.
    """
    reserved_clusters = {str(c) for c in excluded_clusters}
    reserved_uids = {str(u) for u in excluded_uids}

    candidates: list[Candidate] = []
    exclusions: list[Exclusion] = []
    counts: dict[str, int] = {
        "records_total": len(records),
        "eligible": 0,
    }

    for record in records:
        uid = str(record.get("uid") or "")
        kind = str(record.get("kind") or "")
        policy = str((record.get("serving_policy") or {}).get("value") or "")
        cluster = cluster_key(record)

        if str(record.get("lifecycle") or "") != "live":
            exclusions.append(Exclusion(uid, "not_live", str(record.get("lifecycle"))))
            continue
        if kind in INELIGIBLE_KINDS:
            exclusions.append(
                Exclusion(uid, "ineligible_kind",
                          f"{kind} has no independently addressable body")
            )
            continue
        if policy not in ELIGIBLE_SERVING_POLICIES:
            exclusions.append(Exclusion(uid, "serving_policy", policy))
            continue
        if uid in reserved_uids:
            exclusions.append(Exclusion(uid, "development_reserved_uid", uid))
            continue
        if cluster in reserved_clusters:
            exclusions.append(
                Exclusion(uid, "development_reserved_cluster", cluster)
            )
            continue
        problem = _verify_body(repo, record)
        if problem:
            exclusions.append(Exclusion(uid, "unverified_body", problem))
            continue

        candidates.append(
            Candidate(
                uid=uid,
                public_id=str(record.get("id") or ""),
                kind=kind,
                scope=derive_scope(record),
                cluster=cluster,
                serving_policy=policy,
                source_path=str((record.get("source") or {}).get("path") or ""),
                position=draw_position(seed, uid),
            )
        )

    candidates.sort(key=lambda c: (c.position, c.uid))
    counts["eligible"] = len(candidates)
    for exclusion in exclusions:
        key = f"excluded_{exclusion.reason}"
        counts[key] = counts.get(key, 0) + 1
    return candidates, exclusions, counts


# --------------------------------------------------------------------------
# selection
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class SelectedTarget:
    candidate: Candidate
    task_class: str
    stratum: str
    rank: int

    def to_json_obj(self) -> dict[str, Any]:
        obj = self.candidate.to_json_obj()
        obj.update({
            "task_class": self.task_class,
            "stratum": self.stratum,
            "selection_rank": self.rank,
        })
        return obj


@dataclass(frozen=True)
class SelectionResult:
    seed: str
    target_pae_commit: str
    algorithm_version: str
    targets: tuple[SelectedTarget, ...]
    exclusions: tuple[Exclusion, ...]
    population: Mapping[str, int]
    kind_quotas: Mapping[str, int]
    class_quotas: Mapping[str, int]
    max_per_scope: int
    problems: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    development_exclusion_sha256: str = ""

    @property
    def ok(self) -> bool:
        return not self.problems

    def composition(self) -> dict[str, Any]:
        from collections import Counter

        kinds = Counter(t.candidate.kind for t in self.targets)
        classes = Counter(t.task_class for t in self.targets)
        scopes = Counter(t.candidate.scope for t in self.targets)
        policies = Counter(t.candidate.serving_policy for t in self.targets)
        return {
            "selected": len(self.targets),
            "kind_distribution": dict(sorted(kinds.items())),
            "class_distribution": dict(sorted(classes.items())),
            "serving_policy_distribution": dict(sorted(policies.items())),
            "distinct_scopes": len(scopes),
            "max_scope_count": max(scopes.values()) if scopes else 0,
            "scope_distribution": dict(sorted(scopes.items())),
        }

    def to_json_obj(self) -> dict[str, Any]:
        """The full record, including target identity. Reviewer-private."""
        return {
            "algorithm_version": self.algorithm_version,
            "target_pae_commit": self.target_pae_commit,
            "selection_seed": self.seed,
            "development_exclusion_sha256": self.development_exclusion_sha256,
            "kind_quotas": dict(self.kind_quotas),
            "class_quotas": dict(self.class_quotas),
            "max_per_scope": self.max_per_scope,
            "population": dict(self.population),
            "composition": self.composition(),
            "targets": [t.to_json_obj() for t in self.targets],
            "mechanical_exclusions": [
                e.to_json_obj() for e in self.exclusions
                if e.reason in ("unverified_body", "development_reserved_cluster",
                                "development_reserved_uid")
            ],
            "problems": list(self.problems),
            "notes": list(self.notes),
        }

    def public_summary(self) -> dict[str, Any]:
        """Counts only. Safe for the public PAE repo — names no target.

        The 45 UIDs are the answer key. A public report may say how the draw was
        shaped and how large the pool was; it may not say who was drawn.
        """
        composition = self.composition()
        composition.pop("scope_distribution", None)
        return {
            "algorithm_version": self.algorithm_version,
            "target_pae_commit": self.target_pae_commit,
            "selection_seed": self.seed,
            "population": dict(self.population),
            "composition": composition,
            "mechanical_replacement_count": sum(
                1 for e in self.exclusions if e.reason == "unverified_body"
            ),
            "development_reserved_count": sum(
                1 for e in self.exclusions
                if e.reason in ("development_reserved_cluster",
                                "development_reserved_uid")
            ),
            "problems": list(self.problems),
            "notes": list(self.notes),
        }


def _stratum_pool(candidates: Sequence[Candidate], stratum: str) -> list[Candidate]:
    """Candidates a stratum may draw from, in draw order.

    ``safety_gated`` draws on serving policy; the kind strata draw on kind and
    are restricted to ``standard`` so a safety-gated resource can never be
    served to an author under a class that does not preserve its guards.
    """
    if stratum == "safety_gated":
        return [c for c in candidates if c.serving_policy == "safety_gated"]
    return [
        c for c in candidates
        if c.kind == stratum and c.serving_policy == "standard"
    ]


def _fill(
    pool: Sequence[Candidate],
    quota: int,
    scope_counts: dict[str, int],
    taken: set[str],
    max_per_scope: int,
) -> list[Candidate]:
    """Two deterministic passes: unseen scopes first, then fill under the cap.

    The diversity pass is what makes the ">=20 distinct scopes" requirement a
    property of the algorithm rather than something checked afterwards and
    fixed by hand. Both passes walk the same fixed draw order, so the result is
    still a pure function of the seed.
    """
    chosen: list[Candidate] = []

    for candidate in pool:  # pass 1 — one packet per previously unseen scope
        if len(chosen) >= quota:
            break
        if candidate.uid in taken or scope_counts.get(candidate.scope, 0) > 0:
            continue
        chosen.append(candidate)
        taken.add(candidate.uid)
        scope_counts[candidate.scope] = 1

    for candidate in pool:  # pass 2 — fill the stratum under the per-scope cap
        if len(chosen) >= quota:
            break
        if candidate.uid in taken:
            continue
        if scope_counts.get(candidate.scope, 0) >= max_per_scope:
            continue
        chosen.append(candidate)
        taken.add(candidate.uid)
        scope_counts[candidate.scope] = scope_counts.get(candidate.scope, 0) + 1

    return chosen


def select_targets(
    records: Sequence[Mapping[str, Any]],
    repo: Path,
    *,
    target_pae_commit: str,
    excluded_clusters: Iterable[str] = (),
    excluded_uids: Iterable[str] = (),
    kind_quotas: Mapping[str, int] | None = None,
    class_quotas: Mapping[str, int] | None = None,
    max_per_scope: int = DEFAULT_MAX_PER_SCOPE,
    min_distinct_scopes: int = DEFAULT_MIN_DISTINCT_SCOPES,
    development_exclusion_sha256: str = "",
) -> SelectionResult:
    """Draw the masked-target set. Deterministic in ``target_pae_commit``."""
    kinds = dict(kind_quotas or DEFAULT_KIND_QUOTAS)
    classes = dict(class_quotas or DEFAULT_CLASS_QUOTAS)
    seed = selection_seed(target_pae_commit)

    candidates, exclusions, population = eligible_candidates(
        records, repo,
        seed=seed,
        excluded_clusters=excluded_clusters,
        excluded_uids=excluded_uids,
    )

    # The safety-gated stratum is sized by its class quota; the non-prompt
    # strata are sized by their kind quotas and then carved into classes.
    scope_counts: dict[str, int] = {}
    taken: set[str] = set()
    problems: list[str] = []
    selected: list[SelectedTarget] = []

    safety_quota = classes.get("safety_gated", 0)
    prompt_quota = kinds.get("prompt", 0)
    if prompt_quota != safety_quota:
        problems.append(
            f"prompt quota {prompt_quota} must equal the safety_gated class "
            f"quota {safety_quota}: every safety-gated resource in this corpus "
            "is a prompt, and no other class draws prompts"
        )

    rank = 0
    for stratum in STRATUM_ORDER:
        quota = safety_quota if stratum == "safety_gated" else kinds.get(stratum, 0)
        if quota <= 0:
            continue
        pool = _stratum_pool(candidates, stratum)
        drawn = _fill(pool, quota, scope_counts, taken, max_per_scope)
        if len(drawn) < quota:
            problems.append(
                f"stratum {stratum!r} wanted {quota} targets but only "
                f"{len(drawn)} eligible candidates satisfied the scope cap "
                f"(pool size {len(pool)})"
            )
        for candidate in drawn:
            selected.append(
                SelectedTarget(
                    candidate=candidate,
                    task_class="safety_gated" if stratum == "safety_gated" else "",
                    stratum=stratum,
                    rank=rank,
                )
            )
            rank += 1

    # Class assignment for the non-prompt half. Deterministic by draw rank:
    # the first ``non_prompt_kind`` quota of them take that class, the rest
    # become ordinary tasks. An ordinary task derived from a skill is still an
    # ordinary task, so nothing about the class depends on which kind it is.
    non_prompt = [t for t in selected if t.stratum != "safety_gated"]
    non_prompt_quota = classes.get("non_prompt_kind", 0)
    reclassified: list[SelectedTarget] = []
    for index, target in enumerate(non_prompt):
        task_class = "non_prompt_kind" if index < non_prompt_quota else "ordinary_task"
        reclassified.append(
            SelectedTarget(
                candidate=target.candidate,
                task_class=task_class,
                stratum=target.stratum,
                rank=target.rank,
            )
        )
    targets = tuple(
        sorted(
            [t for t in selected if t.stratum == "safety_gated"] + reclassified,
            key=lambda t: t.rank,
        )
    )

    problems.extend(
        _check_requirements(targets, classes, kinds, max_per_scope,
                            min_distinct_scopes)
    )

    notes = [
        "Kind allocation deviates from the Phase 8A recommendation "
        "(skill 12 / agent 8 / command 8 / persona 5 / prompt 12) because every "
        "safety_gated resource in this corpus is a prompt, so 'exactly 18 "
        "safety_gated packets' forces at least 18 prompts. Prompts are held at "
        "that forced minimum and the remaining 27 slots keep the "
        "recommendation's 12:8:8:5 ratio.",
    ]

    return SelectionResult(
        seed=seed,
        target_pae_commit=str(target_pae_commit),
        algorithm_version=SELECTION_ALGORITHM_VERSION,
        targets=targets,
        exclusions=tuple(exclusions),
        population=population,
        kind_quotas=kinds,
        class_quotas=classes,
        max_per_scope=max_per_scope,
        problems=tuple(problems),
        notes=tuple(notes),
        development_exclusion_sha256=development_exclusion_sha256,
    )


def _check_requirements(
    targets: Sequence[SelectedTarget],
    classes: Mapping[str, int],
    kinds: Mapping[str, int],
    max_per_scope: int,
    min_distinct_scopes: int,
) -> list[str]:
    """The spec §4 requirements, checked against what was actually drawn."""
    from collections import Counter

    problems: list[str] = []
    total_wanted = sum(classes.values())
    if len(targets) != total_wanted:
        problems.append(f"selected {len(targets)} targets, expected {total_wanted}")

    class_counts = Counter(t.task_class for t in targets)
    for name, wanted in classes.items():
        got = class_counts.get(name, 0)
        if got != wanted:
            problems.append(f"class {name!r}: selected {got}, required exactly {wanted}")

    kind_counts = Counter(t.candidate.kind for t in targets)
    for name, wanted in kinds.items():
        got = kind_counts.get(name, 0)
        if got != wanted:
            problems.append(f"kind {name!r}: selected {got}, required {wanted}")

    for target in targets:
        if target.task_class == "safety_gated" \
                and target.candidate.serving_policy != "safety_gated":
            problems.append(
                f"{target.candidate.uid}: safety_gated class packet whose target "
                f"serving policy is {target.candidate.serving_policy!r}; the class "
                "exists to test guard preservation and is meaningless otherwise"
            )
        if target.task_class == "non_prompt_kind" and target.candidate.kind == "prompt":
            problems.append(
                f"{target.candidate.uid}: non_prompt_kind class packet whose target "
                "is a prompt"
            )

    scopes = Counter(t.candidate.scope for t in targets)
    if len(scopes) < min_distinct_scopes:
        problems.append(
            f"masked targets span {len(scopes)} scopes, requirement is "
            f">= {min_distinct_scopes}"
        )
    over = {scope: count for scope, count in scopes.items() if count > max_per_scope}
    if over:
        problems.append(f"scopes exceeding the per-scope cap {max_per_scope}: {over}")

    uids = [t.candidate.uid for t in targets]
    if len(set(uids)) != len(uids):
        problems.append("a target was selected twice")
    clusters = [t.candidate.cluster for t in targets]
    if len(set(clusters)) != len(clusters):
        problems.append(
            "two selected targets share a canonical cluster; they would be one "
            "logical answer and the packet count would overstate coverage"
        )
    return problems


# --------------------------------------------------------------------------
# development exclusions (spec §2)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class DevelopmentExclusions:
    clusters: tuple[str, ...]
    uids: tuple[str, ...]
    source_path: Path | None = None
    raw: Mapping[str, Any] = field(default_factory=dict)

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj({
            "clusters": sorted(self.clusters),
            "uids": sorted(self.uids),
        })

    @classmethod
    def load(cls, path: Path) -> "DevelopmentExclusions":
        path = Path(path)
        if not path.is_file():
            raise UsageError(f"development exclusions not found: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{path}: invalid JSON: {exc}") from exc
        clusters = tuple(str(c) for c in (payload.get("excluded_clusters") or ()))
        uids = tuple(str(u) for u in (payload.get("excluded_uids") or ()))
        return cls(clusters=clusters, uids=uids, source_path=path, raw=payload)

    @classmethod
    def empty(cls) -> "DevelopmentExclusions":
        return cls(clusters=(), uids=())

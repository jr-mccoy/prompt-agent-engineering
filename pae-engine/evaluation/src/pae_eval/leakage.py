"""Deterministic benchmark leakage audit.

A benchmark authored against resource bodies tends to echo their vocabulary,
and BM25F is a lexical ranker — so a benchmark that leaks title words measures
echo rather than retrieval. Phase 7A quantified this on the Phase 4 set:
resource-derived cases showed a median query-to-target overlap of 0.71 against
0.44 for phrases written before the search implementation existed. That is the
gap these metrics exist to keep out of the sealed set.

Everything here is deterministic and model-free, so it runs in CI for free and
returns the same numbers for the same inputs forever.

What this deliberately does *not* do is strip ordinary domain vocabulary. A
clinical task contains clinical words; that is the domain, not leakage. The
gates target echo of a specific target's *identifiers* — its title, its public
ID — and statistical over-similarity, not topical overlap.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from statistics import median
from typing import Any, Iterable, Mapping, Sequence

from .constants import EXAMPLE_LEAKAGE_THRESHOLDS

#: Function words carry no retrieval signal; leaving them in would inflate
#: every overlap score toward a meaningless constant.
STOPWORDS = frozenset("""
a an the of to for and or in on with by from as at is are be been being this that
these those how do does did i my me you your we us our it its if not no can could
should would will shall may might must have has had help make made get set new
more most best good better want need using use used about into over under than
then there here what when where which who whom whose why
""".split())

TOKEN = re.compile(r"[a-z0-9]+")
MIN_TOKEN_LENGTH = 3


def normalize_tokens(text: str) -> set[str]:
    """Content tokens of ``text``: NFKC, casefolded, stopped, length-filtered."""
    if not text:
        return set()
    folded = unicodedata.normalize("NFKC", text).casefold()
    return {
        token for token in TOKEN.findall(folded)
        if len(token) >= MIN_TOKEN_LENGTH and token not in STOPWORDS
    }


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def containment(subset: set[str], superset: set[str]) -> float:
    """Share of ``subset`` present in ``superset``."""
    if not subset:
        return 0.0
    return len(subset & superset) / len(subset)


def id_tail_tokens(uid_or_id: str) -> set[str]:
    """Tokens of a public ID's final segment, e.g. ``.../api-rest-design-review``."""
    tail = uid_or_id.rsplit("/", 1)[-1]
    return normalize_tokens(tail.replace("-", " ").replace("_", " "))


# --------------------------------------------------------------------------
# corpus of things a task might echo
# --------------------------------------------------------------------------


@dataclass
class LeakageCorpus:
    """Everything a benchmark task must not be a copy of."""

    #: uid -> {"title": ..., "description": ..., "id": ...}
    records: Mapping[str, Mapping[str, Any]] = field(default_factory=dict)
    #: Phase 4 tuning queries.
    tuning_queries: tuple[str, ...] = ()
    #: Quoted "user phrase" rows from meta/ROUTING_REFERENCE.md.
    routing_phrases: tuple[str, ...] = ()

    _phrase_tokens: tuple[set[str], ...] = field(default_factory=tuple, repr=False)
    _tuning_tokens: tuple[set[str], ...] = field(default_factory=tuple, repr=False)

    def __post_init__(self) -> None:
        # Tokenized once: an audit compares every task against every phrase,
        # so re-tokenizing ~1,100 phrases per task would dominate the run.
        self._phrase_tokens = tuple(normalize_tokens(p) for p in self.routing_phrases)
        self._tuning_tokens = tuple(normalize_tokens(q) for q in self.tuning_queries)

    @classmethod
    def from_repo(cls, repo: Path, *, regression_set: Path | None = None,
                  routing_reference: Path | None = None) -> "LeakageCorpus":
        repo = Path(repo)
        records: dict[str, dict[str, Any]] = {}
        registry = repo / "meta" / "registry" / "registry.jsonl"
        if registry.exists():
            with open(registry, encoding="utf-8") as handle:
                for line in handle:
                    line = line.strip()
                    if not line:
                        continue
                    row = json.loads(line)
                    records[row["uid"]] = {
                        "id": row.get("id", ""),
                        "title": row.get("title", ""),
                        "description": row.get("description", "") or "",
                    }

        queries: list[str] = []
        regression = regression_set or (
            repo / "pae-engine" / "tests" / "data" / "search_routing_regression.v1.json"
        )
        if regression.exists():
            payload = json.loads(regression.read_text(encoding="utf-8"))
            queries = [c.get("query", "") for c in payload.get("cases", [])]

        phrases: list[str] = []
        reference = routing_reference or (repo / "meta" / "ROUTING_REFERENCE.md")
        if reference.exists():
            text = reference.read_text(encoding="utf-8")
            phrases = re.findall(r'^\|\s*"([^"]{6,160})"\s*\|', text, re.M)
            phrases += re.findall(r'Example:\s*"([^"]{6,180})"', text)

        return cls(
            records=records,
            tuning_queries=tuple(queries),
            routing_phrases=tuple(phrases),
        )

    def target_tokens(self, uid: str) -> set[str]:
        record = self.records.get(uid) or {}
        return normalize_tokens(record.get("title", "")) | normalize_tokens(
            record.get("description", "")
        )

    def title_tokens(self, uid: str) -> set[str]:
        return normalize_tokens((self.records.get(uid) or {}).get("title", ""))

    def public_id(self, uid: str) -> str:
        return (self.records.get(uid) or {}).get("id", "")


# --------------------------------------------------------------------------
# per-task audit
# --------------------------------------------------------------------------


@dataclass
class TaskLeakage:
    task_id: str
    authoring_mode: str
    query_target_overlap: float
    title_token_containment: bool
    id_tail_containment: bool
    max_routing_reference_jaccard: float
    max_tuning_query_jaccard: float
    exact_duplicate_of: str | None
    near_duplicate_of: str | None

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "authoring_mode": self.authoring_mode,
            "query_target_overlap": round(self.query_target_overlap, 4),
            "title_token_containment": self.title_token_containment,
            "id_tail_containment": self.id_tail_containment,
            "max_routing_reference_jaccard": round(self.max_routing_reference_jaccard, 4),
            "max_tuning_query_jaccard": round(self.max_tuning_query_jaccard, 4),
            "exact_duplicate_of": self.exact_duplicate_of,
            "near_duplicate_of": self.near_duplicate_of,
        }


def audit_task(task: Any, corpus: LeakageCorpus, *,
               near_duplicate_threshold: float = 0.85) -> TaskLeakage:
    query = normalize_tokens(task.query)
    mode = (task.label_provenance or {}).get("authoring_mode", "unknown")

    overlap = 0.0
    title_hit = False
    id_hit = False
    for resource in task.acceptable_resource_uids:
        target = corpus.target_tokens(resource.uid)
        if target:
            overlap = max(overlap, containment(query, target))
        title = corpus.title_tokens(resource.uid)
        if title and title <= query:
            title_hit = True
        tail = id_tail_tokens(corpus.public_id(resource.uid) or resource.uid)
        if tail and tail <= query:
            id_hit = True

    max_phrase = 0.0
    exact: str | None = None
    near: str | None = None
    for phrase, tokens in zip(corpus.routing_phrases, corpus._phrase_tokens):
        score = jaccard(query, tokens)
        if score > max_phrase:
            max_phrase = score
        if score >= 1.0 and exact is None:
            exact = phrase
        elif score >= near_duplicate_threshold and near is None:
            near = phrase

    max_tuning = 0.0
    for tuning, tokens in zip(corpus.tuning_queries, corpus._tuning_tokens):
        score = jaccard(query, tokens)
        if score > max_tuning:
            max_tuning = score
        if score >= 1.0 and exact is None:
            exact = tuning
        elif score >= near_duplicate_threshold and near is None:
            near = tuning

    return TaskLeakage(
        task_id=task.task_id,
        authoring_mode=mode,
        query_target_overlap=overlap,
        title_token_containment=title_hit,
        id_tail_containment=id_hit,
        max_routing_reference_jaccard=max_phrase,
        max_tuning_query_jaccard=max_tuning,
        exact_duplicate_of=exact,
        near_duplicate_of=near,
    )


# --------------------------------------------------------------------------
# benchmark-level report and gates
# --------------------------------------------------------------------------


@dataclass
class LeakageReport:
    per_task: tuple[TaskLeakage, ...]
    thresholds: Mapping[str, Any]
    metrics: Mapping[str, Any]
    violations: tuple[str, ...]

    @property
    def passed(self) -> bool:
        return not self.violations

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "thresholds": dict(self.thresholds),
            "metrics": dict(self.metrics),
            "violations": list(self.violations),
            "passed": self.passed,
            "per_task": [t.to_json_obj() for t in self.per_task],
        }


def audit_benchmark(tasks: Sequence[Any], corpus: LeakageCorpus, *,
                    thresholds: Mapping[str, Any] | None = None) -> LeakageReport:
    """Audit a whole benchmark against the frozen thresholds.

    Thresholds are passed in from the evaluation plan, never read from a
    constant here: a gate that lives in code can be edited without leaving a
    trace in the hashed plan (spec §21).
    """
    gates = {**EXAMPLE_LEAKAGE_THRESHOLDS, **(thresholds or {})}
    audited = tuple(audit_task(task, corpus) for task in tasks)

    overlaps = [a.query_target_overlap for a in audited if a.query_target_overlap > 0]
    derived = [
        a.query_target_overlap for a in audited
        if a.authoring_mode == "masked_resource_derived" and a.query_target_overlap > 0
    ]
    title_hits = sum(1 for a in audited if a.title_token_containment)
    id_hits = sum(1 for a in audited if a.id_tail_containment)
    jaccard_gate = float(gates["routing_reference_jaccard_threshold"])
    over_jaccard = sum(
        1 for a in audited if a.max_routing_reference_jaccard >= jaccard_gate
    )
    exact_dupes = [a.task_id for a in audited if a.exact_duplicate_of]
    near_dupes = [a.task_id for a in audited if a.near_duplicate_of]

    metrics = {
        "task_count": len(audited),
        "median_target_overlap": round(median(overlaps), 4) if overlaps else 0.0,
        "median_target_overlap_masked_derived": (
            round(median(derived), 4) if derived else 0.0
        ),
        "title_token_containment_count": title_hits,
        "id_tail_containment_count": id_hits,
        "routing_reference_jaccard_over_threshold_count": over_jaccard,
        "routing_reference_jaccard_over_threshold_share": (
            round(over_jaccard / len(audited), 4) if audited else 0.0
        ),
        "exact_duplicate_task_ids": exact_dupes,
        "near_duplicate_task_ids": near_dupes,
    }

    violations: list[str] = []
    if metrics["median_target_overlap"] > float(gates["median_target_overlap_max"]):
        violations.append(
            f"median query->target overlap {metrics['median_target_overlap']} "
            f"exceeds {gates['median_target_overlap_max']}"
        )
    if derived and metrics["median_target_overlap_masked_derived"] > float(
        gates["median_target_overlap_masked_derived_max"]
    ):
        violations.append(
            "median overlap in the masked-resource-derived stratum "
            f"{metrics['median_target_overlap_masked_derived']} exceeds "
            f"{gates['median_target_overlap_masked_derived_max']}"
        )
    if title_hits > int(gates["title_token_containment_max"]):
        violations.append(
            f"{title_hits} task(s) contain a target's full title tokens "
            f"(limit {gates['title_token_containment_max']})"
        )
    if id_hits > int(gates["id_tail_containment_max"]):
        violations.append(
            f"{id_hits} task(s) contain a target's public-ID tail "
            f"(limit {gates['id_tail_containment_max']})"
        )
    if metrics["routing_reference_jaccard_over_threshold_share"] > float(
        gates["routing_reference_jaccard_share_max"]
    ):
        violations.append(
            f"{metrics['routing_reference_jaccard_over_threshold_share']:.1%} of tasks "
            f"are >= {jaccard_gate} Jaccard against a routing-reference phrase "
            f"(limit {float(gates['routing_reference_jaccard_share_max']):.1%})"
        )
    if exact_dupes:
        violations.append(
            f"{len(exact_dupes)} task(s) duplicate a tuning query or routing phrase: "
            + ", ".join(exact_dupes[:5])
        )

    return LeakageReport(
        per_task=audited, thresholds=gates, metrics=metrics,
        violations=tuple(violations),
    )

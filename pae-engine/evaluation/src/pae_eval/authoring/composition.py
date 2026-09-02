"""The sealed composition plan, acceptance checks and the dev/sealed firewall.

Three things that all answer "is the finished benchmark the one we planned?":

* §3 — what the 150 sealed tasks are meant to be made of;
* §13 — the broad acceptance checks a completed benchmark must pass before it
  is frozen;
* §14 — the firewall proving the development set did not bleed into it.

None of these can run yet, because the sealed tasks do not exist. They are
written now so the acceptance bar is fixed **before** anyone sees the tasks it
will judge. A quota invented after the data is a quota chosen to be met.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

#: Spec §3 — the whole sealed benchmark.
SEALED_TOTAL = 150
SEALED_CLASS_TARGET: Mapping[str, int] = {
    "ordinary_task": 38,
    "multi_resource_composition": 18,
    "non_prompt_kind": 20,
    "safety_gated": 18,
    "weak_no_route": 15,
    "cross_domain_ambiguous": 15,
    "technique_discovery": 8,
    "acronym_format_typo": 6,
    "long_complex": 6,
    "adversarial_governance": 6,
}

#: Spec §3 — the masked-derived half.
MASKED_CLASS_ALLOCATION: Mapping[str, int] = {
    "ordinary_task": 7,
    "non_prompt_kind": 20,
    "safety_gated": 18,
}

#: Spec §3 — the natural/external half.
NATURAL_CLASS_ALLOCATION: Mapping[str, int] = {
    "ordinary_task": 31,
    "multi_resource_composition": 18,
    "weak_no_route": 15,
    "cross_domain_ambiguous": 15,
    "technique_discovery": 8,
    "acronym_format_typo": 6,
    "long_complex": 6,
    "adversarial_governance": 6,
}

MASKED_TOTAL = sum(MASKED_CLASS_ALLOCATION.values())
NATURAL_TOTAL = sum(NATURAL_CLASS_ALLOCATION.values())

#: Spec §13 — acceptance gates for the eventual completed benchmark.
ACCEPTANCE_THRESHOLDS: Mapping[str, float] = {
    "min_distinct_scopes": 25,
    "max_scope_share": 0.08,
    "max_prompt_share_of_target_roles": 0.60,
    "min_descriptionless_targets": 12,
    "min_multi_acceptable_tasks": 8,
    "max_exact_title_style_tasks": 10,
}


def plan_reconciliation() -> dict[str, Any]:
    """Prove the three allocation tables agree before anything is authored."""
    combined: dict[str, int] = {}
    for table in (MASKED_CLASS_ALLOCATION, NATURAL_CLASS_ALLOCATION):
        for name, count in table.items():
            combined[name] = combined.get(name, 0) + count
    problems: list[str] = []
    for name, wanted in SEALED_CLASS_TARGET.items():
        got = combined.get(name, 0)
        if got != wanted:
            problems.append(
                f"class {name!r}: masked+natural = {got}, sealed target {wanted}"
            )
    for name in combined:
        if name not in SEALED_CLASS_TARGET:
            problems.append(f"class {name!r} allocated but not in the sealed target")
    total = sum(SEALED_CLASS_TARGET.values())
    if total != SEALED_TOTAL:
        problems.append(f"sealed class target sums to {total}, expected {SEALED_TOTAL}")
    if MASKED_TOTAL + NATURAL_TOTAL != SEALED_TOTAL:
        problems.append(
            f"masked {MASKED_TOTAL} + natural {NATURAL_TOTAL} != {SEALED_TOTAL}"
        )
    return {
        "sealed_total": SEALED_TOTAL,
        "masked_total": MASKED_TOTAL,
        "natural_total": NATURAL_TOTAL,
        "class_target": dict(SEALED_CLASS_TARGET),
        "masked_allocation": dict(MASKED_CLASS_ALLOCATION),
        "natural_allocation": dict(NATURAL_CLASS_ALLOCATION),
        "reconciled": not problems,
        "problems": problems,
    }


def natural_class_table() -> str:
    """Markdown rows for the author brief."""
    return "\n".join(
        f"| `{name}` | {count} |"
        for name, count in sorted(NATURAL_CLASS_ALLOCATION.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
    )


# --------------------------------------------------------------------------
# §13 acceptance
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    observed: Any
    required: str

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "passed": self.passed,
            "observed": self.observed,
            "required": self.required,
        }


def acceptance_checks(
    tasks: Sequence[Any],
    records: Mapping[str, Mapping[str, Any]] | None = None,
    *,
    thresholds: Mapping[str, float] | None = None,
) -> list[Check]:
    """Run the §13 checks over a loaded benchmark.

    Returns checks rather than raising: a shortfall is a thing to report before
    freeze and then fix by authoring more tasks, not an error to swallow. Spec
    §13 is explicit that quotas must never be met by inventing labels.
    """
    from collections import Counter

    limits = {**ACCEPTANCE_THRESHOLDS, **(thresholds or {})}
    total = len(tasks) or 1

    scopes: Counter = Counter()
    kinds: Counter = Counter()
    descriptionless = 0
    for task in tasks:
        scopes.update(task.acceptable_scopes)
        for resource in task.acceptable_resource_uids:
            record = (records or {}).get(resource.uid) or {}
            kind = record.get("kind")
            if kind:
                kinds[kind] += 1
            if records is not None and not record.get("description"):
                descriptionless += 1

    labelled_roles = sum(kinds.values())
    prompt_share = (kinds.get("prompt", 0) / labelled_roles) if labelled_roles else 0.0
    max_scope_share = (max(scopes.values()) / total) if scopes else 0.0
    multi = sum(1 for t in tasks if len(t.acceptable_resource_uids) > 1)
    exact_title = sum(
        1 for t in tasks
        if (t.leakage_audit or {}).get("title_token_containment") is True
    )

    return [
        Check("distinct_scopes", len(scopes) >= limits["min_distinct_scopes"],
              len(scopes), f">= {int(limits['min_distinct_scopes'])}"),
        Check("max_scope_share", max_scope_share <= limits["max_scope_share"],
              round(max_scope_share, 4),
              f"<= {limits['max_scope_share']:.0%} of {total} tasks"),
        Check("prompt_share_of_target_roles",
              prompt_share <= limits["max_prompt_share_of_target_roles"],
              round(prompt_share, 4),
              f"<= {limits['max_prompt_share_of_target_roles']:.0%} "
              f"of {labelled_roles} labelled target roles"),
        Check("descriptionless_targets",
              descriptionless >= limits["min_descriptionless_targets"],
              descriptionless, f">= {int(limits['min_descriptionless_targets'])}"),
        Check("multi_acceptable_tasks",
              multi >= limits["min_multi_acceptable_tasks"],
              multi, f">= {int(limits['min_multi_acceptable_tasks'])}"),
        Check("exact_title_style_tasks",
              exact_title <= limits["max_exact_title_style_tasks"],
              exact_title, f"<= {int(limits['max_exact_title_style_tasks'])}"),
    ]


# --------------------------------------------------------------------------
# §14 development / sealed firewall
# --------------------------------------------------------------------------


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").casefold()).strip()


def firewall_checks(
    development_tasks: Sequence[Any],
    sealed_tasks: Sequence[Any],
    *,
    development_clusters: Sequence[str] = (),
    sealed_clusters: Mapping[str, str] | None = None,
    author_export_findings: int | None = None,
) -> list[Check]:
    """§14 — no duplicated task text, no reused clusters, no mapping leak.

    Generic rubric structure may be shared between the two sets; a rubric is a
    grading form, not content, and requiring two incompatible forms would only
    make the development set stop predicting the sealed one.
    """
    dev_text = {_normalize(f"{t.query}\n{t.deliverable}") for t in development_tasks}
    sealed_text = [_normalize(f"{t.query}\n{t.deliverable}") for t in sealed_tasks]
    duplicates = sorted(set(sealed_text) & dev_text)

    reserved = {str(c) for c in development_clusters}
    cluster_of = dict(sealed_clusters or {})
    reused: list[str] = []
    for task in sealed_tasks:
        for resource in task.acceptable_resource_uids:
            cluster = cluster_of.get(resource.uid, resource.uid)
            if cluster in reserved:
                reused.append(f"{task.task_id}: {resource.uid} (cluster {cluster})")

    checks = [
        Check("no_duplicate_task_text", not duplicates, len(duplicates), "== 0"),
        Check("no_reused_development_clusters", not reused, sorted(set(reused)), "== 0"),
    ]
    if author_export_findings is not None:
        checks.append(Check(
            "no_reviewer_mapping_in_author_export",
            author_export_findings == 0, author_export_findings, "== 0",
        ))
    return checks

"""Deterministic, budget-aware context compilation.

The compiler turns candidates — explicit references, ``SearchResults`` or a
``RouteDecision`` — into a ``ContextBundle`` of whole, verified resource
bodies that fits a stated budget.

Three properties are load-bearing:

* **It is not a second search engine.** It owns no ``SearchEngine`` and no
  ``Router``, cannot rank, and never re-scores what it was handed. Whatever
  uncertainty the Router expressed survives compilation intact.
* **Every body arrives through** :meth:`Registry.content`. No path is opened,
  no attachment is read, no link is followed. Serving policy and integrity
  stay Registry responsibilities.
* **Whole resource or absent.** There is no truncation API here. A body that
  does not fit becomes an ``OmittedItem`` with a closed reason code, and the
  next candidate is tried.

The budget is measured against the *canonical Markdown rendering*, because
that is the artifact a model actually receives. JSON is transport.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, replace
from typing import Any, Mapping, Optional, Protocol, Sequence, runtime_checkable

from ._version import __version__
from .errors import (
    BudgetTooSmall,
    ContentRefused,
    InvalidBudget,
    NoAddressableContent,
    ResourceExcluded,
    SourceIntegrityError,
    UsageError,
)
from .models import (
    BUNDLE_SCHEMA,
    MARKDOWN_RENDERER,
    RECORD_SCHEMA,
    SUMMARY_SCHEMA,
    BudgetReport,
    BundleItem,
    ContextBundle,
    OmittedItem,
    Record,
    RouteDecision,
    SearchResults,
    _plain,
)
from .registry import Registry

__all__ = [
    "MAX_BUNDLE_BYTES",
    "DEFAULT_MAX_RESOURCES",
    "LOW_TOKEN_BUDGET_THRESHOLD",
    "TokenCounter",
    "ApproximateTokenCounterV1",
    "Budget",
    "ContextCompiler",
]

#: The engine's own hard ceiling on a rendered bundle, mirroring the
#: per-resource ``MAX_CONTENT_BYTES``. A caller may ask for less, never more.
MAX_BUNDLE_BYTES = 4 * 1024 * 1024

#: Inclusion ceiling. Also the maximum, so a caller cannot ask the compiler to
#: assemble an unbounded bundle.
DEFAULT_MAX_RESOURCES = 25
MAX_MAX_RESOURCES = 25

#: Below this, the corpus measurements say a typical PAE resource usually will
#: not fit. Advisory only — a small budget is answerable, just rarely useful.
LOW_TOKEN_BUDGET_THRESHOLD = 4000


@runtime_checkable
class TokenCounter(Protocol):
    """How a caller's tokenizer is plugged in.

    Implementations must be deterministic, return a non-negative integer, and
    count exactly the string passed. Bundle reproducibility depends on
    ``name`` and ``version``: two counters that disagree must not share them.
    """

    name: str
    version: str
    #: ``False`` for an estimate. A bundle never claims an exact model-token
    #: fit on the strength of an estimator.
    exact: bool

    def count(self, text: str) -> int:  # pragma: no cover - protocol
        ...


@dataclass(frozen=True)
class ApproximateTokenCounterV1:
    """The built-in estimator: UTF-8 bytes divided by four, rounded up.

    This is an **estimate**, not a safe upper bound and not any provider's
    tokenizer. Measured against real BPE tokenizers over the live corpus it
    tracks the mean closely and still underestimates a minority of resources;
    content that tokenizes densely — CJK, base64, hex, emoji — defeats any
    fixed divisor. The enforced guarantee is the exact byte ceiling, never
    this number. Callers needing exactness inject their own counter.
    """

    name: str = "utf8-bytes-div4"
    version: str = "1"
    exact: bool = False

    def count(self, text: str) -> int:
        return math.ceil(len(text.encode("utf-8")) / 4)


def _require_int(value: Any, label: str) -> int:
    # bool is an int subclass; True as a byte limit is a bug, not a limit.
    if isinstance(value, bool) or not isinstance(value, int):
        raise InvalidBudget(f"{label} must be an integer, got {type(value).__name__}")
    return value


@dataclass(frozen=True)
class Budget:
    """What the caller is willing to spend on one bundle.

    At least one limit is required. The compiler never invents a model context
    size, because it does not know the model, the system prompt, the tools or
    the length of the reply.
    """

    estimated_tokens: Optional[int] = None
    bytes: Optional[int] = None
    max_resources: int = DEFAULT_MAX_RESOURCES

    def __post_init__(self) -> None:
        if self.estimated_tokens is None and self.bytes is None:
            raise InvalidBudget("a budget needs an estimated-token limit, a byte limit, or both")
        for label, value in (("estimated_tokens", self.estimated_tokens), ("bytes", self.bytes)):
            if value is None:
                continue
            _require_int(value, label)
            if value <= 0:
                raise InvalidBudget(f"{label} must be greater than zero, got {value}")
        _require_int(self.max_resources, "max_resources")
        if not 1 <= self.max_resources <= MAX_MAX_RESOURCES:
            raise InvalidBudget(
                f"max_resources must be between 1 and {MAX_MAX_RESOURCES}, "
                f"got {self.max_resources}"
            )


@dataclass(frozen=True)
class _Candidate:
    """One thing to try, before anything is known about whether it has a body.

    Ranked modes arrive carrying the identity Search already disclosed, so the
    compiler resolves each candidate exactly once — through ``content()`` —
    instead of looking the same record up a second time to re-derive a title
    it was already given.
    """

    ref: str
    rank: Optional[int]
    score: Optional[float]
    scope: Optional[str]
    id: Optional[str] = None
    kind: Optional[str] = None
    title: Optional[str] = None
    canonical_uid: Optional[str] = None


def _from_hit(hit: Any) -> _Candidate:
    return _Candidate(
        ref=hit.uid,
        rank=hit.rank,
        score=hit.score,
        scope=hit.scope,
        id=hit.id,
        kind=hit.kind,
        title=hit.title,
        canonical_uid=hit.canonical_uid,
    )


def _canonical_uid(record: Record) -> str:
    """The logical cluster a record belongs to, from its own relationships."""
    relationships = record.raw.get("relationships") or {}
    copy_of = relationships.get("copy_of") if isinstance(relationships, Mapping) else None
    return copy_of if isinstance(copy_of, str) and copy_of else record.uid


_DETAIL = {
    "budget": "did not fit in the remaining budget",
    "oversized": "does not fit the budget even as the only resource",
    "metadata_only": "served as metadata only; its body is withheld",
    "excluded": "excluded from serving; identity only",
    "tombstone": "a tombstone; the historical body no longer exists",
    "no_addressable_body": "has no independently addressable body",
    "duplicate": "already included under the same resolved UID",
    "max_resources": "beyond the max_resources inclusion ceiling",
    "filtered": "removed by the requested scope filter",
}


class ContextCompiler:
    """Assembles bundles. Holds a Registry and a counter, and nothing else.

    It has no ``SearchEngine`` and no ``Router`` by construction, so it cannot
    quietly re-run retrieval on a caller's behalf.
    """

    def __init__(
        self,
        registry: Registry,
        *,
        token_counter: Optional[TokenCounter] = None,
    ) -> None:
        self._registry = registry
        self._counter: TokenCounter = token_counter or ApproximateTokenCounterV1()

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"ContextCompiler(counter={self._counter.name}/{self._counter.version})"

    # -- public entry points -----------------------------------------------

    def compile_refs(self, refs: Sequence[str], *, budget: Budget) -> ContextBundle:
        """Compile exactly what the caller named, in the order they named it.

        Caller intent is authoritative here: a resource that cannot be served
        raises rather than quietly becoming an omission, because the caller
        asked for that specific thing by hand.
        """
        if not refs:
            raise UsageError("compile_refs needs at least one reference")
        candidates = tuple(
            _Candidate(ref=ref, rank=None, score=None, scope=None) for ref in refs
        )
        return self._compile(
            candidates=candidates,
            budget=budget,
            source_mode="refs",
            ordering="input",
            explicit=True,
            task=None,
        )

    def compile_search(self, results: SearchResults, *, budget: Budget) -> ContextBundle:
        """Compile ranked search hits, preserving their rank, score and scope."""
        candidates = tuple(_from_hit(hit) for hit in results.hits)
        return self._compile(
            candidates=candidates,
            budget=budget,
            source_mode="search",
            ordering="rank",
            explicit=False,
            task=results.query,
        )

    def compile_route(
        self,
        decision: RouteDecision,
        *,
        budget: Budget,
        scopes: Optional[Sequence[str]] = None,
    ) -> ContextBundle:
        """Compile a routing decision without ever re-routing it.

        ``scopes`` is a packing filter, not a re-route: the decision's status,
        candidate scopes and kinds are reported exactly as the Router produced
        them, and filtered candidates become ``filtered`` omissions.
        """
        candidates = tuple(_from_hit(hit) for hit in decision.resources)
        warnings: list[str] = []
        ordering = "rank"
        filtered: set[str] = set()

        wanted = tuple(scopes) if scopes else ()
        if wanted:
            known = {c.scope for c in candidates if c.scope}
            unknown = [s for s in wanted if s not in known]
            if unknown:
                raise UsageError(
                    "requested scope is not among this decision's candidates: "
                    + ", ".join(sorted(unknown)),
                    requested=list(wanted),
                    available=sorted(known),
                )
            filtered = {c.ref for c in candidates if c.scope not in wanted}
            ordering = "rank+scope-filter"
            warnings.append("scope_filter_applied")

        if decision.status == "weak":
            warnings.append("weak_route")
        if decision.status == "ambiguous":
            warnings.append("ambiguous_route")
            if not wanted:
                candidates, promoted = _top_two_scope_diversity(candidates, decision)
                if promoted:
                    ordering = "rank+top2-scope-diversity"
                else:
                    warnings.append("ambiguity_diversity_unavailable")

        return self._compile(
            candidates=candidates,
            budget=budget,
            source_mode="route",
            ordering=ordering,
            explicit=False,
            task=decision.query,
            decision=decision,
            filtered=filtered,
            filter_scopes=wanted,
            warnings=warnings,
        )

    # -- compilation -------------------------------------------------------

    def _compile(
        self,
        *,
        candidates: tuple[_Candidate, ...],
        budget: Budget,
        source_mode: str,
        ordering: str,
        explicit: bool,
        task: Optional[str],
        decision: Optional[RouteDecision] = None,
        filtered: Optional[set[str]] = None,
        filter_scopes: tuple[str, ...] = (),
        warnings: Optional[list[str]] = None,
    ) -> ContextBundle:
        ceiling, ceiling_source = self._byte_ceiling(budget)
        base_notes = list(warnings or [])
        if (
            budget.estimated_tokens is not None
            and budget.estimated_tokens < LOW_TOKEN_BUDGET_THRESHOLD
            and isinstance(self._counter, ApproximateTokenCounterV1)
        ):
            base_notes.append("low_estimated_token_budget")

        filtered = filtered or set()
        included: list[BundleItem] = []
        omitted: list[OmittedItem] = []
        seen: dict[str, str] = {}
        candidate_uids: list[str] = []

        def frame(inc: Sequence[BundleItem], om: Sequence[OmittedItem]) -> ContextBundle:
            # The best-hit warning depends on the final selection, and the
            # warning itself is rendered and hashed. Deriving it here keeps
            # every frame internally consistent, so the fit loop converges on
            # a bundle whose text, hash and report all agree.
            notes = list(base_notes)
            if _top_hit_omitted(candidate_uids, inc, om):
                notes.append("top_hit_omitted")
            return self._assemble(
                included=tuple(inc),
                omitted=tuple(om),
                candidates=tuple(candidate_uids),
                budget=budget,
                ceiling=ceiling,
                ceiling_source=ceiling_source,
                source_mode=source_mode,
                ordering=ordering,
                task=task,
                decision=decision,
                warnings=tuple(notes),
                filter_scopes=filter_scopes,
            )

        for candidate in candidates:
            if candidate.ref in filtered:
                candidate_uids.append(candidate.ref)
                omitted.append(self._omission(candidate, "filtered", None))
                continue

            outcome = self._resolve(candidate, explicit=explicit)
            uid = outcome.uid
            candidate_uids.append(uid)

            if outcome.omission is not None:
                omitted.append(outcome.omission)
                continue

            if uid in seen:
                omitted.append(
                    self._omission(candidate, "duplicate", outcome.record, uid=uid)
                )
                continue
            seen[uid] = candidate.ref

            if len(included) >= budget.max_resources:
                omitted.append(
                    self._omission(
                        candidate,
                        "max_resources",
                        outcome.record,
                        uid=uid,
                        estimated_tokens=outcome.item.estimated_tokens if outcome.item else None,
                    )
                )
                continue

            item = outcome.item
            if item is None:  # pragma: no cover - no omission implies a body
                continue
            trial = frame(included + [item], omitted)
            if self._fits(trial, budget, ceiling):
                included.append(item)
                continue

            # "Oversized" must mean the body itself is too big, not that this
            # candidate happened to be tried after a long omission list had
            # accumulated. Testing it in a minimal frame keeps the distinction
            # independent of processing order.
            alone = frame([item], [])
            reason = "budget" if self._fits(alone, budget, ceiling) else "oversized"
            omitted.append(
                self._omission(
                    candidate,
                    reason,
                    outcome.record,
                    uid=uid,
                    estimated_tokens=item.estimated_tokens,
                )
            )

        # The complete bundle carries omission lines the trial frames did not.
        # Re-measure against the real article and shed the lowest-priority
        # body until the rendered artifact honours what the report will claim.
        while True:
            bundle = frame(included, omitted)
            markdown = bundle.render_markdown()
            used_bytes = len(markdown.encode("utf-8"))
            used_tokens = self._counter.count(markdown)
            if self._within(used_bytes, used_tokens, budget, ceiling):
                break
            if not included:
                raise BudgetTooSmall(
                    "the requested budget cannot hold this bundle's framing and manifest "
                    "even with no resource bodies",
                    requested_estimated_tokens=budget.estimated_tokens,
                    requested_bytes=budget.bytes,
                    effective_byte_ceiling=ceiling,
                    minimum_bytes=used_bytes,
                    minimum_estimated_tokens=used_tokens,
                )
            dropped = included.pop()
            omitted.append(
                OmittedItem(
                    uid=dropped.uid,
                    id=dropped.id,
                    kind=dropped.kind,
                    title=dropped.title,
                    source_rank=dropped.source_rank,
                    reason="budget",
                    detail=_DETAIL["budget"],
                    estimated_tokens=dropped.estimated_tokens,
                )
            )

        report = self._report(
            budget=budget,
            ceiling=ceiling,
            ceiling_source=ceiling_source,
            included=included,
            used_bytes=used_bytes,
            used_tokens=used_tokens,
        )
        # Only the report changes here, and the report is never rendered, so
        # the Markdown measured above is the Markdown this bundle emits.
        return replace(bundle, budget=report)

    # -- resolution --------------------------------------------------------

    def _resolve(self, candidate: _Candidate, *, explicit: bool) -> "_Outcome":
        ref = candidate.ref
        record: Optional[Record] = None
        try:
            # Explicit references carry no upstream metadata, so identity has to
            # be resolved before the body. Ranked candidates already have it.
            if candidate.id is None:
                record = self._registry.get(ref)
        except ResourceExcluded as exc:
            if explicit:
                raise
            stub = exc.details.get("resource") or {}
            return _Outcome(
                uid=str(stub.get("uid") or exc.details.get("uid") or ref),
                record=None,
                item=None,
                omission=OmittedItem(
                    uid=str(stub.get("uid") or exc.details.get("uid") or ref),
                    id=stub.get("id"),
                    kind=stub.get("kind"),
                    title=None,
                    source_rank=candidate.rank,
                    reason="excluded",
                    detail=_DETAIL["excluded"],
                    estimated_tokens=None,
                ),
            )

        try:
            content = self._registry.content(ref)
        except SourceIntegrityError:
            # A registry that disagrees with disk cannot produce a trustworthy
            # bundle. This is never downgraded to an omission.
            raise
        except ResourceExcluded:
            if explicit:
                raise
            return _Outcome(
                uid=record.uid if record else ref,
                record=record,
                item=None,
                omission=self._omission(candidate, "excluded", record, policy_safe=True),
            )
        except ContentRefused:
            if explicit:
                raise
            return _Outcome(
                uid=record.uid if record else ref,
                record=record,
                item=None,
                omission=self._omission(candidate, "metadata_only", record),
            )
        except NoAddressableContent as exc:
            if explicit:
                raise
            tombstone = exc.details.get("lifecycle") == "tombstone"
            return _Outcome(
                uid=record.uid if record else ref,
                record=record,
                item=None,
                omission=self._omission(
                    candidate,
                    "tombstone" if tombstone else "no_addressable_body",
                    record,
                ),
            )

        text = content.text()
        item = BundleItem(
            uid=content.uid,
            id=content.id,
            kind=record.kind if record else (candidate.kind or ""),
            title=record.title if record else (candidate.title or content.id),
            scope=candidate.scope,
            source_rank=candidate.rank,
            source_score=candidate.score,
            serving_policy=content.serving_policy,
            guard_preservation=content.guard_preservation,
            content_sha256=content.content_sha256,
            byte_length=content.byte_length,
            estimated_tokens=self._counter.count(text),
            verified=content.verified,
            canonical_uid=(
                _canonical_uid(record) if record else (candidate.canonical_uid or content.uid)
            ),
            content=text,
        )
        return _Outcome(uid=content.uid, record=record, item=item, omission=None)

    def _omission(
        self,
        candidate: _Candidate,
        reason: str,
        record: Optional[Record],
        *,
        uid: Optional[str] = None,
        estimated_tokens: Optional[int] = None,
        policy_safe: bool = False,
    ) -> OmittedItem:
        # An excluded resource contributes policy-safe identity and nothing
        # else — never a title, and never one carried in from a search hit.
        if policy_safe or reason == "excluded":
            stub = record.identity_stub() if record is not None else {}
            return OmittedItem(
                uid=stub.get("uid") or uid or candidate.ref,
                id=stub.get("id") or candidate.id,
                kind=stub.get("kind") or candidate.kind,
                title=None,
                source_rank=candidate.rank,
                reason=reason,
                detail=_DETAIL[reason],
                estimated_tokens=None,
            )
        return OmittedItem(
            uid=uid or (record.uid if record else candidate.ref),
            id=record.id if record else candidate.id,
            kind=record.kind if record else candidate.kind,
            title=record.title if record else candidate.title,
            source_rank=candidate.rank,
            reason=reason,
            detail=_DETAIL[reason],
            estimated_tokens=estimated_tokens,
        )

    # -- budget ------------------------------------------------------------

    def _byte_ceiling(self, budget: Budget) -> tuple[int, str]:
        if budget.bytes is not None:
            return min(budget.bytes, MAX_BUNDLE_BYTES), "explicit"
        if budget.estimated_tokens is not None and isinstance(
            self._counter, ApproximateTokenCounterV1
        ):
            # Exact for this estimator only: ceil(b/4) <= T is equivalent to
            # b <= 4T. It says nothing about any model's real tokenizer.
            return min(budget.estimated_tokens * 4, MAX_BUNDLE_BYTES), (
                "derived_from_default_estimator"
            )
        return MAX_BUNDLE_BYTES, "engine_safety_ceiling"

    def _within(self, used_bytes: int, used_tokens: int, budget: Budget, ceiling: int) -> bool:
        if used_bytes > ceiling:
            return False
        if budget.estimated_tokens is not None and used_tokens > budget.estimated_tokens:
            return False
        return True

    def _fits(self, bundle: ContextBundle, budget: Budget, ceiling: int) -> bool:
        markdown = bundle.render_markdown()
        return self._within(
            len(markdown.encode("utf-8")), self._counter.count(markdown), budget, ceiling
        )

    def _report(
        self,
        *,
        budget: Budget,
        ceiling: int,
        ceiling_source: str,
        included: Sequence[BundleItem],
        used_bytes: int,
        used_tokens: int,
    ) -> BudgetReport:
        body = sum(self._counter.count(item.content) for item in included)
        remaining_tokens = (
            budget.estimated_tokens - used_tokens if budget.estimated_tokens is not None else None
        )
        return BudgetReport(
            requested_estimated_tokens=budget.estimated_tokens,
            requested_bytes=budget.bytes,
            effective_byte_ceiling=ceiling,
            byte_ceiling_source=ceiling_source,
            used_estimated_tokens=used_tokens,
            remaining_estimated_tokens=remaining_tokens,
            used_bytes=used_bytes,
            remaining_bytes=ceiling - used_bytes,
            body_estimated_tokens=body,
            wrapper_overhead_estimated_tokens=used_tokens - body,
            estimator_name=self._counter.name,
            estimator_version=self._counter.version,
            estimator_exact=bool(self._counter.exact),
        )

    # -- assembly ----------------------------------------------------------

    def _assemble(
        self,
        *,
        included: tuple[BundleItem, ...],
        omitted: tuple[OmittedItem, ...],
        candidates: tuple[str, ...],
        budget: Budget,
        ceiling: int,
        ceiling_source: str,
        source_mode: str,
        ordering: str,
        task: Optional[str],
        decision: Optional[RouteDecision],
        warnings: tuple[str, ...],
        filter_scopes: tuple[str, ...],
    ) -> ContextBundle:
        placeholder = BudgetReport(
            requested_estimated_tokens=budget.estimated_tokens,
            requested_bytes=budget.bytes,
            effective_byte_ceiling=ceiling,
            byte_ceiling_source=ceiling_source,
            used_estimated_tokens=0,
            remaining_estimated_tokens=None,
            used_bytes=0,
            remaining_bytes=0,
            body_estimated_tokens=0,
            wrapper_overhead_estimated_tokens=0,
            estimator_name=self._counter.name,
            estimator_version=self._counter.version,
            estimator_exact=bool(self._counter.exact),
        )
        shell = ContextBundle(
            schema_version=BUNDLE_SCHEMA,
            compiler_version=__version__,
            renderer=MARKDOWN_RENDERER,
            task=task,
            source_mode=source_mode,
            route_status=decision.status if decision else None,
            selected_scope=decision.selected_scope if decision else None,
            selected_kind=decision.selected_kind if decision else None,
            candidate_scopes=(
                tuple(c.name for c in decision.candidate_scopes) if decision else ()
            ),
            candidate_kinds=(
                tuple(c.name for c in decision.candidate_kinds) if decision else ()
            ),
            coverage=decision.coverage if decision else None,
            margin=decision.margin if decision else None,
            candidates=candidates,
            included=included,
            omitted=omitted,
            budget=placeholder,
            ordering=ordering,
            bundle_sha256="",
            warnings=warnings,
        )
        digest = _bundle_digest(shell, budget=budget, filter_scopes=filter_scopes)
        return replace(shell, bundle_sha256=digest)


@dataclass(frozen=True)
class _Outcome:
    uid: str
    record: Optional[Record]
    item: Optional[BundleItem]
    omission: Optional[OmittedItem]


def _top_two_scope_diversity(
    candidates: tuple[_Candidate, ...], decision: RouteDecision
) -> tuple[tuple[_Candidate, ...], bool]:
    """Promote one candidate from the other close scope, and nothing more.

    The Router said two scopes were close. Preserving exactly that — rank 1,
    then the best candidate from the *other* top-two scope, then everything
    else in rank order — is the smallest intervention that stops an ambiguous
    route from silently collapsing into one scope. It is deliberately not a
    round robin over every scope the query touched.
    """
    if len(candidates) < 2 or len(decision.candidate_scopes) < 2:
        return candidates, False
    top_two = [c.name for c in decision.candidate_scopes[:2]]
    first = candidates[0]
    others = [name for name in top_two if name != first.scope]
    if not others:
        return candidates, False
    target = others[0]
    promoted = next((c for c in candidates[1:] if c.scope == target), None)
    if promoted is None:
        return candidates, False
    rest = [c for c in candidates[1:] if c is not promoted]
    return (first, promoted, *rest), True


def _top_hit_omitted(
    candidates: Sequence[str],
    included: Sequence[BundleItem],
    omitted: Sequence[OmittedItem],
) -> bool:
    """Was the best-ranked candidate left out for a budget reason?

    A bundle whose top hit silently vanished looks exactly like one where it
    fit, so this is surfaced rather than left for the reader to notice.
    """
    if not candidates:
        return False
    top = candidates[0]
    if any(item.uid == top for item in included):
        return False
    return any(o.uid == top and o.reason in ("budget", "oversized") for o in omitted)


def _bundle_digest(
    bundle: ContextBundle, *, budget: Budget, filter_scopes: tuple[str, ...]
) -> str:
    """A reproducible identity for one compilation.

    Binds the decisions, not the wall clock: same snapshot, candidates, budget
    and options produce the same hash on any machine, in any checkout, at any
    time. Bodies enter through their source checksums rather than in full.
    """
    manifest: dict[str, Any] = {
        "bundle_schema": bundle.schema_version,
        "compiler_version": bundle.compiler_version,
        "renderer": bundle.renderer,
        "registry_record_schema": RECORD_SCHEMA,
        "registry_summary_schema": SUMMARY_SCHEMA,
        "source_mode": bundle.source_mode,
        "task": bundle.task,
        "route": {
            "status": bundle.route_status,
            "selected_scope": bundle.selected_scope,
            "selected_kind": bundle.selected_kind,
            "candidate_scopes": list(bundle.candidate_scopes),
            "candidate_kinds": list(bundle.candidate_kinds),
            "coverage": bundle.coverage,
            "margin": bundle.margin,
        },
        "candidates": list(bundle.candidates),
        "filters": {
            "scopes": list(filter_scopes),
            "max_resources": budget.max_resources,
        },
        "ordering": bundle.ordering,
        "included": [
            {
                "uid": item.uid,
                "id": item.id,
                "kind": item.kind,
                "scope": item.scope,
                "source_rank": item.source_rank,
                "serving_policy": item.serving_policy,
                "guard_preservation": _plain(item.guard_preservation),
                "content_sha256": item.content_sha256,
                "byte_length": item.byte_length,
            }
            for item in bundle.included
        ],
        "omitted": [
            {"uid": o.uid, "id": o.id, "reason": o.reason} for o in bundle.omitted
        ],
        "budget": {
            "requested_estimated_tokens": budget.estimated_tokens,
            "requested_bytes": budget.bytes,
            "max_resources": budget.max_resources,
            "effective_byte_ceiling": bundle.budget.effective_byte_ceiling,
            "byte_ceiling_source": bundle.budget.byte_ceiling_source,
        },
        "counter": {
            "name": bundle.budget.estimator_name,
            "version": bundle.budget.estimator_version,
            "exact": bundle.budget.estimator_exact,
        },
        "warnings": list(bundle.warnings),
    }
    payload = json.dumps(
        manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

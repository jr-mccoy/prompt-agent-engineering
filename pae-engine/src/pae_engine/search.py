"""Deterministic lexical search over registry metadata.

The Engine's second read path. :class:`~pae_engine.registry.Registry` answers
"what is this reference?"; :class:`SearchEngine` answers "which resources look
like this description?" — and answers it from metadata alone.

What search deliberately does not do:

* **It never reads a body.** ``Registry.content()`` is not called from here, so
  what a resource says cannot influence where it ranks and a search can never
  become a way to read something policy withholds.
* **It never overrides serving policy.** An excluded resource is absent from
  the index and no flag brings it back.
* **It never scores governance.** Maturity, review, eval, licence, provenance
  and quality assertions filter and display; they do not rank. There are no
  quality tiers here to boost.
"""

from __future__ import annotations

import time
from typing import Any, Iterable, Mapping, Optional, Sequence

from ._lexical import (
    DEFAULT_LIMIT,
    FIELDS,
    MAX_LIMIT,
    MAX_QUERY_CHARS,
    MAX_QUERY_TOKENS,
    SCORE_PRECISION,
    Document,
    LexicalIndex,
    derive_scope,
    normalize,
)
from .errors import MalformedReference, ResourceExcluded, ResourceNotFound, UsageError
from .models import SearchHit, SearchResults
from .registry import Registry

__all__ = ["SearchEngine", "KINDS"]

#: The six registry kinds. Fixed, so a kind filter can be validated without
#: reading a single record.
KINDS: tuple[str, ...] = ("prompt", "technique", "skill", "agent", "command", "persona")


class SearchEngine:
    """Lexical search over one checkout's registry.

    Construction is cheap and reads nothing. The index is built on the first
    ordinary lexical search and reused immutably afterwards, so a process that
    only ever resolves an exact reference never pays for one — the same lazy
    contract :class:`Registry` already keeps.

    Eligibility belongs on the constructor because it changes the corpus
    statistics every score depends on. Query-time filters only subset an
    existing ranking, so they belong on :meth:`search`.
    """

    def __init__(
        self,
        registry: Registry,
        *,
        include_deprecated: bool = False,
        include_tombstones: bool = False,
    ) -> None:
        self.registry = registry
        self.include_deprecated = bool(include_deprecated)
        self.include_tombstones = bool(include_tombstones)
        self._index: Optional[LexicalIndex] = None
        self._clusters: dict[str, tuple[int, ...]] = {}
        self._indexed_uids: frozenset[str] = frozenset()
        self._scopes: frozenset[str] = frozenset()
        self._build_ms: Optional[float] = None
        self._records_loaded = 0
        self._records_excluded = 0

    @classmethod
    def open(cls, registry: Registry, **kwargs: Any) -> "SearchEngine":
        return cls(registry, **kwargs)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        state = "built" if self._index is not None else "unbuilt"
        return f"SearchEngine(root={self.registry.repository.root!s}, index={state})"

    # -- eligibility -------------------------------------------------------

    def _eligible(self, record: Any) -> bool:
        """Whether a record may appear in search results at all.

        Order is load-bearing. Exclusion is absolute. A tombstone is then
        judged purely on lifecycle: every tombstone is also marked deprecated,
        so consulting maturity first would make ``include_tombstones`` useless
        on its own.
        """
        if record.serving_policy == "excluded":
            return False
        if record.lifecycle == "tombstone":
            return self.include_tombstones
        if record.maturity == "deprecated":
            return self.include_deprecated
        return True

    # -- index -------------------------------------------------------------

    @property
    def index_info(self) -> Mapping[str, Any]:
        """Enough to debug a ranking without reading the implementation."""
        info: dict[str, Any] = {
            "built": self._index is not None,
            "include_deprecated": self.include_deprecated,
            "include_tombstones": self.include_tombstones,
            "registry_root": str(self.registry.repository.root),
            "summary_schema": "pae-registry-summary/1",
        }
        if self._index is None:
            return info
        info.update(
            {
                "build_duration_ms": self._build_ms,
                "distinct_terms": self._index.distinct_terms,
                "records_excluded_by_policy": self._records_excluded,
                "records_indexed": self._index.size,
                "records_loaded": self._records_loaded,
                "scopes": len(self._scopes),
            }
        )
        return info

    def _ensure_index(self) -> LexicalIndex:
        if self._index is not None:
            return self._index
        started = time.perf_counter()
        documents: list[Document] = []
        loaded = 0
        excluded = 0
        for record in self.registry.load_all():
            loaded += 1
            if record.serving_policy == "excluded":
                excluded += 1
                continue
            if not self._eligible(record):
                continue
            documents.append(Document(record))
        index = LexicalIndex(documents)

        clusters: dict[str, list[int]] = {}
        for position, document in enumerate(index.documents):
            clusters.setdefault(document.cluster_key, []).append(position)

        self._index = index
        self._clusters = {key: tuple(value) for key, value in clusters.items()}
        self._indexed_uids = frozenset(d.uid for d in index.documents)
        self._scopes = frozenset(d.scope for d in index.documents if d.scope)
        self._records_loaded = loaded
        self._records_excluded = excluded
        self._build_ms = round((time.perf_counter() - started) * 1000.0, 3)
        return index

    @property
    def scopes(self) -> frozenset[str]:
        """Every scope present in the eligible population. Builds the index."""
        self._ensure_index()
        return self._scopes

    # -- query validation --------------------------------------------------

    @staticmethod
    def _check_limit(limit: int, *, maximum: int = MAX_LIMIT, label: str = "limit") -> int:
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise UsageError(f"{label} must be an integer", limit=limit)
        if limit < 1:
            raise UsageError(f"{label} must be at least 1", limit=limit)
        if limit > maximum:
            raise UsageError(f"{label} must be at most {maximum}", limit=limit, maximum=maximum)
        return limit

    @staticmethod
    def _check_kinds(kinds: Optional[Sequence[str]]) -> Optional[frozenset[str]]:
        if kinds is None:
            return None
        wanted = frozenset(kinds)
        unknown = sorted(wanted - frozenset(KINDS))
        if unknown:
            raise UsageError(
                f"unknown kind(s): {', '.join(unknown)}", unknown=unknown, valid=list(KINDS)
            )
        return wanted or None

    def _check_scopes(self, scopes: Optional[Sequence[str]]) -> Optional[frozenset[str]]:
        if scopes is None:
            return None
        wanted = frozenset(s.casefold() for s in scopes)
        if not wanted:
            return None
        # Validating a scope means knowing the scope universe, which means
        # loading the population. A scope-filtered query therefore always
        # builds the index; a kind-filtered one does not.
        known = self.scopes
        unknown = sorted(wanted - known)
        if unknown:
            raise UsageError(f"unknown scope(s): {', '.join(unknown)}", unknown=unknown)
        return wanted

    @staticmethod
    def _normalized_query(query: str) -> tuple[str, ...]:
        if not isinstance(query, str) or not query.strip():
            raise UsageError("query is empty")
        if len(query) > MAX_QUERY_CHARS:
            raise UsageError(
                f"query is {len(query)} characters, above the {MAX_QUERY_CHARS}-character bound",
                chars=len(query),
                maximum=MAX_QUERY_CHARS,
            )
        terms = normalize(query)
        if not terms:
            raise UsageError(
                "query contains no searchable terms after normalization "
                "(it may be entirely stopwords or punctuation)",
                query=query,
            )
        if len(terms) > MAX_QUERY_TOKENS:
            raise UsageError(
                f"query normalizes to {len(terms)} terms, above the "
                f"{MAX_QUERY_TOKENS}-term bound",
                terms=len(terms),
                maximum=MAX_QUERY_TOKENS,
            )
        return tuple(terms)

    # -- search ------------------------------------------------------------

    def search(
        self,
        query: str,
        *,
        kinds: Optional[Sequence[str]] = None,
        scopes: Optional[Sequence[str]] = None,
        limit: int = DEFAULT_LIMIT,
        include_copies: bool = False,
    ) -> SearchResults:
        """Rank eligible resources against a query. Zero hits is a valid result."""
        limit = self._check_limit(limit)
        wanted_kinds = self._check_kinds(kinds)
        terms = self._normalized_query(query)
        wanted_scopes = self._check_scopes(scopes)

        filters = {
            "include_copies": bool(include_copies),
            "include_deprecated": self.include_deprecated,
            "include_tombstones": self.include_tombstones,
            "kinds": sorted(wanted_kinds) if wanted_kinds else None,
            "limit": limit,
            "scopes": sorted(wanted_scopes) if wanted_scopes else None,
        }

        if wanted_scopes is None:
            exact = self._exact_reference(query, terms, wanted_kinds, filters)
            if exact is not None:
                return exact

        return self._lexical_search(query, terms, wanted_kinds, wanted_scopes, limit,
                                    bool(include_copies), filters)

    # -- exact reference ---------------------------------------------------

    def _exact_reference(
        self,
        query: str,
        terms: tuple[str, ...],
        wanted_kinds: Optional[frozenset[str]],
        filters: dict[str, Any],
    ) -> Optional[SearchResults]:
        """Resolve a query that is entirely one UID, public ID or retired alias.

        A shortcut, not a score bonus: the resource is returned because it was
        named, not because it out-ranked anything. It still obeys every
        eligibility rule, so this can never become a way around
        :meth:`Registry.get`'s access gate.

        Returns ``None`` when the query is not an exact reference, so the
        caller falls through to ordinary lexical search — and, crucially,
        without having built the index.
        """
        reference = query.strip()
        try:
            resolution, record = self.registry.lookup(reference)
        except ResourceExcluded:
            # The identity exists and is withheld. Saying so here would leak
            # exactly what exclusion is for; search reports nothing at all.
            return SearchResults(
                query=query,
                normalized_terms=terms,
                hits=(),
                total_matched=0,
                filters=filters,
                notices=(),
            )
        except (MalformedReference, ResourceNotFound):
            return None

        if not self._eligible(record):
            reason = (
                "tombstone" if record.lifecycle == "tombstone" else "deprecated"
            )
            flag = "--include-tombstones" if reason == "tombstone" else "--include-deprecated"
            return SearchResults(
                query=query,
                normalized_terms=terms,
                hits=(),
                total_matched=0,
                filters=filters,
                notices=(
                    f"exact reference {record.id} resolves but is hidden by default "
                    f"because it is {reason}; pass {flag} to include it",
                ),
            )

        if wanted_kinds is not None and record.kind not in wanted_kinds:
            return SearchResults(
                query=query,
                normalized_terms=terms,
                hits=(),
                total_matched=0,
                filters=filters,
                notices=(
                    f"exact reference {record.id} resolves but its kind "
                    f"({record.kind}) is excluded by the kind filter",
                ),
            )

        relationships = record.raw.get("relationships") or {}
        copy_of = relationships.get("copy_of")
        canonical_uid = record.uid
        notices: list[str] = []
        if isinstance(copy_of, str) and copy_of:
            canonical_uid = self._visible_canonical(copy_of, record.uid)

        if relationships.get("copies"):
            # Listing sibling copies means checking each one's eligibility,
            # which means loading the population — the cost this path exists to
            # avoid. Reporting none is accurate about what was checked and
            # cannot leak an excluded record.
            notices.append(
                "copy cluster not expanded on the exact-reference path; "
                "run a lexical search to see sibling copies"
            )
        if resolution.ref_kind == "alias":
            notices.append(
                f"resolved via retired alias {resolution.matched_alias} -> {record.id}"
            )

        hit = SearchHit(
            uid=record.uid,
            id=record.id,
            kind=record.kind,
            title=record.title,
            scope=derive_scope(record),
            rank=1,
            score=0.0,
            maturity=record.maturity,
            serving_policy=record.serving_policy,
            metadata_completeness=record.metadata_completeness,
            matched_fields=("exact_reference",),
            match_terms={"exact_reference": (reference,)},
            canonical_uid=canonical_uid,
            copy_uids=(),
        )
        return SearchResults(
            query=query,
            normalized_terms=terms,
            hits=(hit,),
            total_matched=1,
            filters=filters,
            notices=tuple(notices),
        )

    def _visible_canonical(self, canonical_uid: str, fallback_uid: str) -> str:
        """The canonical's UID, but only when search may admit it exists.

        A copy whose canonical is excluded must not report that canonical's
        UID. Doing so would let a caller enumerate excluded resources by
        collecting cluster pointers that resolve to nothing — exactly the
        disclosure path exclusion exists to close. Within the searchable world
        such a copy simply is its own cluster, which is what gets reported.
        """
        try:
            _resolution, canonical = self.registry.lookup(canonical_uid)
        except (ResourceExcluded, ResourceNotFound, MalformedReference):
            return fallback_uid
        return canonical_uid if self._eligible(canonical) else fallback_uid

    # -- lexical -----------------------------------------------------------

    def _lexical_search(
        self,
        query: str,
        terms: tuple[str, ...],
        wanted_kinds: Optional[frozenset[str]],
        wanted_scopes: Optional[frozenset[str]],
        limit: int,
        include_copies: bool,
        filters: dict[str, Any],
    ) -> SearchResults:
        index = self._ensure_index()
        scored = index.score(terms)

        ranked: list[tuple[float, str, int]] = []
        for position, raw_score in scored.items():
            document = index.documents[position]
            if wanted_kinds is not None and document.kind not in wanted_kinds:
                continue
            if wanted_scopes is not None and document.scope not in wanted_scopes:
                continue
            ranked.append((round(raw_score, SCORE_PRECISION), document.id, position))

        # Deterministic order: score descending, then public ID ascending.
        # Never dict, set or filesystem iteration order.
        ranked.sort(key=lambda entry: (-entry[0], entry[1]))

        if not include_copies:
            ranked = self._collapse_clusters(ranked)

        total_matched = len(ranked)
        hits: list[SearchHit] = []
        for rank, (score, _public_id, position) in enumerate(ranked[:limit], start=1):
            hits.append(self._hit(index, position, rank, score, terms, include_copies))

        return SearchResults(
            query=query,
            normalized_terms=terms,
            hits=tuple(hits),
            total_matched=total_matched,
            filters=filters,
            notices=(),
        )

    def _collapse_clusters(
        self, ranked: Sequence[tuple[float, str, int]]
    ) -> list[tuple[float, str, int]]:
        """One result per registered canonical/copy cluster.

        The highest-scoring eligible member represents the cluster, which may
        be a toolkit-local copy — usually the one a caller working inside that
        toolkit actually wants. Because the list is already sorted, keeping the
        first member seen is the same as keeping the best, and the tie-break is
        inherited rather than re-invented.
        """
        assert self._index is not None
        seen: set[str] = set()
        kept: list[tuple[float, str, int]] = []
        for entry in ranked:
            key = self._index.documents[entry[2]].cluster_key
            if key in seen:
                continue
            seen.add(key)
            kept.append(entry)
        return kept

    def _hit(
        self,
        index: LexicalIndex,
        position: int,
        rank: int,
        score: float,
        terms: tuple[str, ...],
        include_copies: bool,
    ) -> SearchHit:
        document = index.documents[position]
        evidence = document.matched(terms)
        siblings = tuple(
            index.documents[other].uid
            for other in self._clusters.get(document.cluster_key, ())
            if other != position
        )
        # Cluster keys are kept even when the canonical is not searchable, so
        # two copies of an excluded canonical still collapse to one result. The
        # *reported* canonical is suppressed in that case — see
        # ``_visible_canonical``.
        canonical_uid = (
            document.cluster_key
            if document.cluster_key in self._indexed_uids
            else document.uid
        )
        return SearchHit(
            uid=document.uid,
            id=document.id,
            kind=document.kind,
            title=document.title,
            scope=document.scope,
            rank=rank,
            score=score,
            maturity=document.maturity,
            serving_policy=document.serving_policy,
            metadata_completeness=document.metadata_completeness,
            matched_fields=tuple(evidence),
            match_terms=evidence,
            canonical_uid=canonical_uid,
            copy_uids=siblings,
        )

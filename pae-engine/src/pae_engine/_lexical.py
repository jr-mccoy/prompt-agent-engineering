"""Deterministic lexical internals: normalization, scope, index and BM25F.

Private to the Engine. Everything public about search lives in :mod:`search`
and :mod:`routing`; this module is where the arithmetic and the data structures
sit so that neither of those files has to explain both at once.

Three invariants shape the code below:

* **Metadata only.** Documents are built from the normalized registry record
  and nothing else. ``Registry.content()`` is never called from here, so what a
  resource *says* can never influence where it ranks.
* **Deterministic.** No hashing order, no set iteration, no wall-clock, no
  randomness reaches a score or a tie-break.
* **Standard library only.** BM25F is implemented directly rather than pulled
  in, because a scoring library would become a runtime dependency and the
  Engine has none.
"""

from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter, defaultdict
from typing import Any, Iterable, Mapping, Optional, Sequence

__all__ = [
    "FIELDS",
    "K1",
    "B",
    "STOPWORDS",
    "MAX_QUERY_CHARS",
    "MAX_QUERY_TOKENS",
    "DEFAULT_LIMIT",
    "MAX_LIMIT",
    "SCORE_PRECISION",
    "normalize",
    "derive_scope",
    "Document",
    "LexicalIndex",
]

#: The indexed fields, in a fixed order so iteration is reproducible.
#:
#: Every field carries weight 1.0. Phase 4A measured every hand-tuned weighting
#: and none beat uniform: the configuration sits on a plateau where perturbing
#: one field moves top-1 accuracy by at most a single query. Shipping tuned
#: coefficients would freeze arbitrary numbers into a public contract in
#: exchange for nothing measurable.
FIELDS: tuple[str, ...] = (
    "title",
    "pid",
    "alias",
    "desc",
    "cat",
    "tags",
    "tech",
    "path",
    "kind",
    "name",
)

#: BM25F saturation and length-normalization constants. Standard values; Phase
#: 4A found a broad plateau for ``b`` in [0.5, 0.9] and ``k1`` in [0.9, 1.6],
#: and a clear cliff at ``b = 0`` (length normalization is doing real work).
K1 = 1.2
B = 0.75

#: Scores are rounded to this many decimal places before ordering, so float
#: noise below the precision of the arithmetic cannot reorder two hits that are
#: genuinely tied.
SCORE_PRECISION = 9

#: One explicit, conservative English stopword list. It is source-controlled
#: rather than imported: a stopword set that changes underneath the index would
#: silently change every score.
STOPWORDS: frozenset[str] = frozenset(
    """
    a an and are as at be by for from has have how i in is it of on or
    that the this to was what when where which who why with you your me my
    we our can could should would do does need
    """.split()
)

#: Request-size ceiling. Unchanged: this bound is about how much text a caller
#: may send, and nothing measured in Phase 8B argued for moving it.
MAX_QUERY_CHARS = 2000

#: How many *normalized terms* a query may reach after stopwords and
#: depluralization. Raised from 64 in Phase 8B, from measurement rather than
#: from taste.
#:
#: 64 rejected realistic requests. A person describing a real problem in full
#: prose — constraints, context, what they have already tried — normalizes to
#: 90–130 terms: three of the thirty development benchmark tasks landed at 97,
#: 106 and 113, and five independently written long requests spanned 92–125.
#: Those are not abusive inputs, and rejecting them made the Engine unusable
#: for exactly the requests context compilation is most valuable for.
#:
#: 256 is the smallest candidate that clears the largest realistic query
#: measured (125 terms) with better than a 2x margin. 128 clears it by three
#: terms, which is not a margin.
#:
#: The security case is that this bound was never the load-bearing control.
#: ``MAX_QUERY_CHARS`` is. Against the true adversarial input — the terms with
#: the highest document-frequency-per-character, which maximise posting-list
#: work per byte sent — 2000 characters hold at most 340 distinct terms, so a
#: cap of 512 could never bind at all. Measured worst case over the real
#: corpus (5217 documents), search and route each:
#:
#:     terms      64      128      256      340 (char-bound maximum)
#:     latency  ~99ms   ~124ms   ~153ms   ~173ms
#:     peak      4.1MB    4.6MB    5.7MB    6.1MB
#:
#: Cost is strongly sublinear in term count because scoring against the corpus
#: dominates: eight high-frequency terms already cost ~48ms. Moving 64 -> 256
#: therefore buys realistic requests at +54ms and +1.6MB in the worst case,
#: which is not a material change to the denial-of-service surface of a
#: single-request read-only API that is already spending ~99ms on that input.
#:
#: The bound is kept rather than removed because term length is a property of
#: this corpus's vocabulary, not an invariant. Short high-frequency tokens
#: exist here in quantity ("md", "st", "01", "qa"), and 2000 characters of
#: those pack 555 terms; a corpus that drifted shorter would raise the
#: character bound's implied term ceiling without anyone noticing. An explicit
#: term bound holds regardless.
MAX_QUERY_TOKENS = 256

DEFAULT_LIMIT = 10
MAX_LIMIT = 100

#: One or more characters that are not lowercase alphanumerics. Splitting on
#: this handles hyphens, underscores, slashes, dots and punctuation uniformly,
#: which is why ``curriculum-architecture``, ``curriculum_architecture`` and
#: ``curriculum architecture`` all produce the same terms — and why acronyms
#: and codes need no special layer: ``ST-01`` splits to ``st``/``01`` on both
#: the query side and the index side.
_SPLIT = re.compile(r"[^0-9a-z]+")

_PLURAL_KEEP = ("ss", "us", "is", "as")


def _depluralize(token: str) -> str:
    """Minimal, symmetric plural folding.

    Not a stemmer. Phase 4A measured this single rule as worth about ten points
    of top-1 accuracy — by far the highest-value normalization step — while a
    real stemmer would add a dependency and a large behavioural surface for no
    measured gain.
    """
    if len(token) > 3:
        if token.endswith("ies"):
            return token[:-3] + "y"
        if token.endswith("s") and not token.endswith(_PLURAL_KEEP):
            return token[:-1]
    return token


def normalize(text: Optional[str]) -> list[str]:
    """The one tokenizer. Indexing and querying must never diverge.

    NFKC → casefold → split on non-alphanumerics → drop stopwords →
    depluralize. Order matters: stopwords are matched before folding so the
    list stays readable as ordinary English words.
    """
    if not text:
        return []
    folded = unicodedata.normalize("NFKC", str(text)).casefold()
    out: list[str] = []
    for raw in _SPLIT.split(folded):
        if not raw or raw in STOPWORDS:
            continue
        out.append(_depluralize(raw))
    return out


def _flatten(value: Any) -> str:
    """Deterministic text for a registry-native value of unknown shape.

    Native metadata is normalized but not schema-locked, so a field that is a
    string in one record can be a list in another. Nested containers are
    flattened one level and joined; anything else is stringified. Nothing is
    indexed recursively — arbitrary nested metadata is not a search field.
    """
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        return " ".join(_flatten(item) for item in value)
    if isinstance(value, Mapping):
        return " ".join(_flatten(item) for item in value.values())
    return str(value)


#: Resources under this scope are split one level deeper. ``agentic-resources``
#: alone holds hundreds of unrelated skills, agents, commands and personas, so
#: routing a caller to it answers nothing; the informative unit is the category
#: beneath it.
_SPLIT_SCOPE = "agentic-resources"


def derive_scope(record: Any) -> str:
    """The routing unit for a record. One helper, used everywhere.

    Search hits, ``--scope`` filtering, router aggregation and the diagnostics
    all call this. A second implementation anywhere would let them disagree
    about what a scope is.
    """
    kind = getattr(record, "kind", "") or ""
    public_id = getattr(record, "id", "") or ""
    rest = public_id.split(":", 1)[1] if ":" in public_id else public_id
    segments = [s for s in rest.split("/") if s]

    if kind == "technique":
        # A technique's public ID is ``technique:ST-01``. Treating ``ST-01`` as
        # a scope would invent 336 single-member scopes; the technique category
        # is the real grouping.
        native = getattr(record, "raw", {}).get("native") or {}
        category = _flatten(native.get("category")).strip()
        if category:
            return category.casefold()
        return segments[0].casefold() if segments else ""

    if not segments:
        return ""
    if segments[0] == _SPLIT_SCOPE and len(segments) > 1:
        return f"{_SPLIT_SCOPE}/{segments[1]}".casefold()
    return segments[0].casefold()


class Document:
    """One indexed record: its searchable terms plus what filtering needs.

    Holds no reference to the source file and no body. ``raw`` is deliberately
    not retained — a document is the *searchable projection* of a record, and
    keeping the whole record here would invite ranking on fields that are
    excluded from relevance by design.
    """

    __slots__ = (
        "uid",
        "id",
        "kind",
        "title",
        "scope",
        "lifecycle",
        "maturity",
        "serving_policy",
        "metadata_completeness",
        "copy_of",
        "cluster_key",
        "fields",
        "lengths",
    )

    def __init__(self, record: Any) -> None:
        raw = record.raw
        native = raw.get("native") or {}
        relationships = raw.get("relationships") or {}

        self.uid = record.uid
        self.id = record.id
        self.kind = record.kind
        self.title = record.title or ""
        self.scope = derive_scope(record)
        self.lifecycle = record.lifecycle
        self.maturity = record.maturity
        self.serving_policy = record.serving_policy
        self.metadata_completeness = record.metadata_completeness

        copy_of = relationships.get("copy_of")
        self.copy_of = copy_of if isinstance(copy_of, str) and copy_of else None
        # A canonical is its own cluster. A copy joins its canonical's.
        self.cluster_key = self.copy_of or self.uid

        rest = record.id.split(":", 1)[1] if ":" in record.id else record.id
        # The scope string joins ``cat`` because agents, personas and most
        # skills carry no native category at all; without it they would have no
        # subject-level term beyond their title.
        category_text = " ".join(
            part for part in (_flatten(native.get("category")), self.scope) if part
        )

        raw_fields = {
            "title": self.title,
            "pid": rest,
            "alias": " ".join(record.aliases),
            "desc": record.description or "",
            "cat": category_text,
            "tags": _flatten(native.get("tags")),
            "tech": _flatten(native.get("techniques")),
            # Techniques have no addressable file. Nothing is synthesized for
            # them: an absent path indexes as an empty field.
            "path": record.source_path or "",
            "kind": record.kind,
            "name": _flatten(native.get("name")),
        }
        self.fields: dict[str, Counter] = {
            field: Counter(normalize(text)) for field, text in raw_fields.items()
        }
        self.lengths: dict[str, int] = {
            field: sum(counter.values()) for field, counter in self.fields.items()
        }

    def matched(self, terms: Iterable[str]) -> dict[str, tuple[str, ...]]:
        """Which query terms each field matched. Observable evidence only."""
        wanted = set(terms)
        evidence: dict[str, tuple[str, ...]] = {}
        for field in FIELDS:
            hits = sorted(wanted & set(self.fields[field]))
            if hits:
                evidence[field] = tuple(hits)
        return evidence


class LexicalIndex:
    """An immutable inverted index over one eligible document population.

    Built once per :class:`~pae_engine.search.SearchEngine`, on first lexical
    search. It represents the registry snapshot read at build time and is never
    invalidated, watched or rebuilt: a caller who wants a newer snapshot builds
    a new engine.
    """

    __slots__ = ("documents", "postings", "doc_freq", "avg_lengths", "size", "distinct_terms")

    def __init__(self, documents: Sequence[Document]) -> None:
        self.documents: tuple[Document, ...] = tuple(documents)
        self.size = len(self.documents)

        postings: dict[str, dict[str, list[tuple[int, int]]]] = {
            field: defaultdict(list) for field in FIELDS
        }
        doc_freq: Counter = Counter()
        totals: Counter = Counter()

        for position, document in enumerate(self.documents):
            seen: set[str] = set()
            for field in FIELDS:
                counter = document.fields[field]
                totals[field] += document.lengths[field]
                for term, frequency in counter.items():
                    postings[field][term].append((position, frequency))
                    seen.add(term)
            # Document frequency is per *document*, not per field occurrence: a
            # term in both the title and the description is still one document.
            for term in seen:
                doc_freq[term] += 1

        self.postings: dict[str, dict[str, tuple[tuple[int, int], ...]]] = {
            field: {term: tuple(entries) for term, entries in terms.items()}
            for field, terms in postings.items()
        }
        self.doc_freq: Mapping[str, int] = dict(doc_freq)
        self.avg_lengths: Mapping[str, float] = {
            field: (totals[field] / self.size if self.size else 0.0) for field in FIELDS
        }
        self.distinct_terms = len(doc_freq)

    def idf(self, term: str) -> float:
        df = self.doc_freq.get(term, 0)
        return math.log(1.0 + (self.size - df + 0.5) / (df + 0.5))

    def score(self, terms: Sequence[str]) -> dict[int, float]:
        """BM25F over the indexed fields. Returns positive scores only.

        ``pseudo_tf`` accumulates each field's length-normalized contribution
        before a single saturation is applied, which is what keeps a forty-word
        description from drowning a one-word title match — the property that
        made BM25F beat flat BM25 on scope accuracy in the Phase 4A trials.
        """
        unique = sorted(set(terms))
        pseudo: dict[int, dict[str, float]] = defaultdict(dict)

        for term in unique:
            for field in FIELDS:
                entries = self.postings[field].get(term)
                if not entries:
                    continue
                average = self.avg_lengths[field]
                if not average:
                    # No document has this field populated, so it cannot
                    # discriminate; contributing here would divide by zero.
                    continue
                for position, frequency in entries:
                    length = self.documents[position].lengths[field]
                    contribution = frequency / (1.0 - B + B * length / average)
                    bucket = pseudo[position]
                    bucket[term] = bucket.get(term, 0.0) + contribution

        scores: dict[int, float] = {}
        for position, contributions in pseudo.items():
            total = 0.0
            for term, value in contributions.items():
                total += self.idf(term) * value / (K1 + value)
            if total > 0.0:
                scores[position] = total
        return scores

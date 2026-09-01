"""Normalization and scope derivation.

These are the two places where search and routing agree about what a term is
and what a scope is. A change here silently changes every score, so the
behaviour is pinned rather than described.
"""

from __future__ import annotations

import unittest

import fixtures
from pae_engine._lexical import (
    MAX_QUERY_TOKENS,
    STOPWORDS,
    Document,
    LexicalIndex,
    derive_scope,
    normalize,
)
from pae_engine.models import Record


def _record(**kwargs):
    return Record.from_raw(fixtures.record(**kwargs))


class TestNormalization(unittest.TestCase):
    def test_delimiters_are_interchangeable(self) -> None:
        """The single most common way a user's spelling differs from a path."""
        expected = ["curriculum", "architecture"]
        for spelling in (
            "curriculum-architecture",
            "curriculum_architecture",
            "curriculum architecture",
            "curriculum/architecture",
            "Curriculum-Architecture",
        ):
            self.assertEqual(normalize(spelling), expected, spelling)

    def test_minimal_depluralization(self) -> None:
        cases = {
            "skills": "skill",
            "stories": "story",
            "prompts": "prompt",
            "business": "business",
            "analysis": "analysis",
            "status": "status",
            "bias": "bias",
            "gas": "gas",
            "css": "css",
            "campus": "campus",
        }
        for given, expected in cases.items():
            self.assertEqual(normalize(given), [expected], given)

    def test_short_words_are_never_depluralized(self) -> None:
        # Three characters or fewer stay whole, so "ops" does not become "op".
        self.assertEqual(normalize("ops"), ["ops"])
        self.assertEqual(normalize("tools"), ["tool"])
        # "apis" is spared by the ``-is`` guard that protects "analysis".
        # A known cost of keeping the rule this small.
        self.assertEqual(normalize("apis"), ["apis"])

    def test_codes_and_acronyms_need_no_special_layer(self) -> None:
        """Both sides split identically, so no code-expansion step is needed."""
        self.assertEqual(normalize("ST-01"), ["st", "01"])
        self.assertEqual(normalize("st_01"), ["st", "01"])
        self.assertEqual(normalize("R8"), ["r8"])
        self.assertEqual(normalize("MCP"), ["mcp"])
        self.assertEqual(normalize("PACU"), ["pacu"])
        self.assertEqual(normalize("CI/CD"), ["ci", "cd"])

    def test_technique_id_matches_its_record_spelling(self) -> None:
        self.assertEqual(normalize("technique:ST-01"), ["technique", "st", "01"])
        self.assertEqual(normalize("ST-01"), normalize("st 01"))

    def test_compatibility_forms_are_folded(self) -> None:
        # NFKC turns full-width characters into their ASCII equivalents, so a
        # pasted-from-elsewhere query still matches.
        self.assertEqual(normalize("Ｒ８"), ["r8"])

    def test_non_ascii_letters_are_dropped(self) -> None:
        """A documented limitation, pinned so it cannot change unnoticed.

        The pipeline splits on everything outside ``[0-9a-z]``, so accented and
        non-Latin characters are discarded. Indexing and querying do it
        identically, so ``café`` still finds ``café`` — but it will not find
        ``cafe``, and a query with no ASCII alphanumerics at all normalizes to
        nothing and is rejected as a usage error.
        """
        self.assertEqual(normalize("CAFÉ"), ["caf"])
        self.assertEqual(normalize("café"), normalize("caf"))
        self.assertEqual(normalize("naïve"), ["na", "ve"])
        self.assertEqual(normalize("日本語"), [])

    def test_stopwords_are_dropped(self) -> None:
        self.assertEqual(normalize("what is the best way to do this"), ["best", "way"])
        self.assertEqual(normalize("the and of"), [])

    def test_empty_and_punctuation_only(self) -> None:
        for text in ("", "   ", "---", "!!!", None):
            self.assertEqual(normalize(text), [])

    def test_stopword_list_is_lowercase_and_non_empty(self) -> None:
        self.assertTrue(STOPWORDS)
        self.assertTrue(all(word == word.casefold() for word in STOPWORDS))


class TestScopeDerivation(unittest.TestCase):
    def test_ordinary_resource_uses_the_first_path_segment(self) -> None:
        self.assertEqual(
            derive_scope(_record(uid="pae_00000000scp", id="prompt:software-engineering/api/x")),
            "software-engineering",
        )

    def test_toolkit_scopes_are_first_class(self) -> None:
        for public_id, expected in (
            ("skill:financial-records-toolkit/a", "financial-records-toolkit"),
            ("agent:childrens-book-studio/b", "childrens-book-studio"),
        ):
            record = _record(
                uid="pae_00000000tk1", id=public_id, kind=public_id.split(":")[0]
            )
            self.assertEqual(derive_scope(record), expected)

    def test_agentic_resources_splits_one_level_deeper(self) -> None:
        """``agentic-resources`` alone spans hundreds of unrelated resources."""
        record = _record(
            uid="pae_00000000ag1",
            id="skill:agentic-resources/cloud-infrastructure/helm-chart-scaffolding",
            kind="skill",
        )
        self.assertEqual(derive_scope(record), "agentic-resources/cloud-infrastructure")

    def test_agentic_resources_without_a_category_does_not_crash(self) -> None:
        record = _record(uid="pae_00000000ag2", id="skill:agentic-resources", kind="skill")
        self.assertEqual(derive_scope(record), "agentic-resources")

    def test_technique_scope_is_its_category_not_its_id(self) -> None:
        """``technique:ST-01`` must not invent a scope called ``ST-01``."""
        record = _record(
            uid="pae_00000000tq1",
            id="technique:ST-01",
            kind="technique",
            defined_in="techniques/MASTER_TECHNIQUE_INDEX.md",
            native={"category": "ST", "state": "active"},
        )
        self.assertEqual(derive_scope(record), "st")

    def test_technique_without_a_category_falls_back_to_its_id(self) -> None:
        record = _record(
            uid="pae_00000000tq2",
            id="technique:ZZ-99",
            kind="technique",
            defined_in="techniques/MASTER_TECHNIQUE_INDEX.md",
        )
        self.assertEqual(derive_scope(record), "zz-99")


class TestDocument(unittest.TestCase):
    def test_a_technique_has_no_synthesized_path(self) -> None:
        record = _record(
            uid="pae_00000000tq3",
            id="technique:ST-04",
            kind="technique",
            title="Delimited Sections",
            defined_in="techniques/MASTER_TECHNIQUE_INDEX.md",
            native={"category": "ST"},
        )
        document = Document(record)
        self.assertEqual(document.lengths["path"], 0)
        self.assertIn("delimited", document.fields["title"])

    def test_native_values_of_odd_shape_are_flattened_deterministically(self) -> None:
        record = _record(
            uid="pae_00000000fl1",
            id="prompt:fixtures/odd-native",
            native={"tags": ["alpha", ["beta", "gamma"]], "name": 12, "category": None},
        )
        document = Document(record)
        self.assertEqual(set(document.fields["tags"]), {"alpha", "beta", "gamma"})
        self.assertIn("12", document.fields["name"])

    def test_a_copy_joins_its_canonical_cluster(self) -> None:
        canonical = _record(uid="pae_00000000cn1", id="prompt:fixtures/canonical")
        copy = _record(
            uid="pae_00000000cp1",
            id="prompt:toolkit/copy",
            relationships={"copy_of": "pae_00000000cn1"},
        )
        self.assertEqual(Document(canonical).cluster_key, "pae_00000000cn1")
        self.assertEqual(Document(copy).cluster_key, "pae_00000000cn1")


class TestIndexArithmetic(unittest.TestCase):
    def test_an_empty_field_contributes_nothing(self) -> None:
        record = _record(uid="pae_00000000em1", id="prompt:fixtures/empty", title="alpha")
        index = LexicalIndex([Document(record)])
        self.assertEqual(index.avg_lengths["alias"], 0.0)
        # Scoring a term that exists only in an empty-average field must not
        # divide by zero.
        self.assertEqual(index.score(["nothing"]), {})

    def test_document_frequency_counts_documents_not_field_occurrences(self) -> None:
        record = _record(
            uid="pae_00000000df1",
            id="prompt:fixtures/alpha",
            title="alpha",
            description="alpha alpha alpha",
        )
        index = LexicalIndex([Document(record)])
        self.assertEqual(index.doc_freq["alpha"], 1)

    def test_scores_are_positive_only(self) -> None:
        record = _record(uid="pae_00000000ps1", id="prompt:fixtures/beta", title="beta")
        index = LexicalIndex([Document(record)])
        self.assertEqual(index.score(["gamma"]), {})
        self.assertGreater(index.score(["beta"])[0], 0.0)

    def test_query_token_bound_is_a_sane_constant(self) -> None:
        self.assertGreaterEqual(MAX_QUERY_TOKENS, 16)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

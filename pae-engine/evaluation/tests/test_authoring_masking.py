"""Body sanitization and the author-packet leakage audit (spec §5, §6).

The invariant tied together here is the one that actually makes the firewall
hold: **anything the audit would flag as a title leak, the masker has already
removed.** The two use the same token boundaries, and a regression that let
them disagree would produce exports that pass masking and fail audit — or, far
worse, the reverse.
"""

from __future__ import annotations

import unittest

from _support import TempDirCase

from pae_eval.authoring import audit, masking

FRONTMATTER_DOC = """---
title: "Geriatric Intake with Polypharmacy Review"
description: "A structured intake."
tags:
  - geriatric
related_prompts:
  - domain-psychology/populations/geriatric/other_thing.md
---

# Geriatric Intake with Polypharmacy Review

## Objective

Produce an intake record. See `domain-psychology/documentation/note.md`.

## When NOT to Use

- When acute delirium is suspected, stabilize first.

## Related

- domain-psychology/risk-crisis/other.md
- pae_008wn0yc495j
"""


class TestSanitizationSteps(unittest.TestCase):

    def setUp(self) -> None:
        self.result = masking.sanitize_body(
            FRONTMATTER_DOC,
            identifying_phrases=["Geriatric Intake with Polypharmacy Review"],
        )

    def test_frontmatter_removed(self) -> None:
        self.assertIn("remove_frontmatter", self.result.operations)
        self.assertNotIn("related_prompts", self.result.text)
        self.assertNotIn("difficulty", self.result.text)

    def test_title_heading_removed(self) -> None:
        self.assertIn("remove_title_heading", self.result.operations)
        self.assertNotIn("# Geriatric", self.result.text)

    def test_uid_redacted(self) -> None:
        self.assertNotIn("pae_008wn0yc495j", self.result.text)

    def test_repository_paths_redacted(self) -> None:
        self.assertNotIn("domain-psychology", self.result.text)
        self.assertNotIn("note.md", self.result.text)

    def test_related_section_removed(self) -> None:
        self.assertIn("remove_metadata_sections", self.result.operations)
        self.assertIn("Related", self.result.removed_sections)

    def test_operational_content_preserved_verbatim(self) -> None:
        self.assertIn("## Objective", self.result.text)
        self.assertIn("Produce an intake record", self.result.text)

    def test_safety_guard_heading_preserved(self) -> None:
        self.assertIn("## When NOT to Use", self.result.text)
        self.assertIn("acute delirium", self.result.text)

    def test_hashes_and_retention_recorded(self) -> None:
        obj = self.result.to_json_obj()
        self.assertTrue(obj["original_sha256"].startswith("sha256:"))
        self.assertTrue(obj["sanitized_sha256"].startswith("sha256:"))
        self.assertGreater(obj["retention"], 0.0)

    def test_is_deterministic(self) -> None:
        again = masking.sanitize_body(
            FRONTMATTER_DOC,
            identifying_phrases=["Geriatric Intake with Polypharmacy Review"],
        )
        self.assertEqual(again.sanitized_sha256, self.result.sanitized_sha256)


class TestGuardPreservation(unittest.TestCase):

    def test_protected_headings_are_never_treated_as_metadata(self) -> None:
        doc = "# T\n\n## References\n\nx\n\n## Limitations\n\nDo not rely on this.\n"
        result = masking.sanitize_body(doc)
        self.assertNotIn("## References", result.text)
        self.assertIn("## Limitations", result.text)
        self.assertIn("Do not rely on this.", result.text)

    def test_guard_check_reports_a_dropped_heading(self) -> None:
        ok, missing = masking.guard_text_preserved(
            "## Safety\n\nx\n", "nothing here\n")
        self.assertFalse(ok)
        self.assertEqual(missing, ["Safety"])

    def test_guard_check_passes_when_preserved(self) -> None:
        ok, missing = masking.guard_text_preserved(
            "## Safety\n\nx\n", "## Safety\n\nx\n")
        self.assertTrue(ok)
        self.assertEqual(missing, [])


class TestSeparatorInsensitiveRedaction(unittest.TestCase):
    """The corpus writes one name three ways; all three must go."""

    CASES = (
        "spec-to-code-compliance",
        "Spec-to-Code Compliance",
        "spec to code compliance",
        "spec_to_code_compliance",
    )

    def test_every_separator_form_is_redacted(self) -> None:
        for written in self.CASES:
            with self.subTest(written=written):
                result = masking.sanitize_body(
                    f"# X\n\nThe {written} checker runs first.\n",
                    identifying_phrases=["spec-to-code-compliance"],
                )
                self.assertNotIn(written.casefold(), result.text.casefold())
                self.assertIn(masking.REDACTION, result.text)

    def test_matches_inside_a_hyphenated_compound(self) -> None:
        """``C4 Component-level`` contains the title ``c4-component``."""
        result = masking.sanitize_body(
            "# X\n\nYou are a C4 Component-level specialist.\n",
            identifying_phrases=["c4-component"],
        )
        self.assertNotIn("C4 Component", result.text)
        self.assertIn("-level", result.text)

    def test_a_longer_word_is_not_redacted(self) -> None:
        result = masking.sanitize_body(
            "# X\n\nWe track issues carefully.\n",
            identifying_phrases=["issue"],
        )
        self.assertIn("issues", result.text)


class TestMaskerAndAuditAgree(unittest.TestCase):
    """The load-bearing invariant between the two halves of the firewall."""

    TITLES = (
        "spec-to-code-compliance",
        "c4-component",
        "let-fate-decide",
        "Geriatric Intake with Polypharmacy Review",
        "UX Researcher",
    )

    def test_audit_never_flags_what_the_masker_kept(self) -> None:
        for title in self.TITLES:
            for separator in ("-", " ", "_"):
                written = title.replace("-", separator).replace(" ", separator)
                with self.subTest(title=title, written=written):
                    sanitized = masking.sanitize_body(
                        f"# X\n\nA body mentioning {written} once.\n",
                        identifying_phrases=[title],
                    )
                    identity = audit.TargetIdentity(
                        packet_id="PKT-0001", uid="pae_x", public_id="skill:x",
                        source_path="", title=title, description="",
                    )
                    flagged = audit.contains_sequence(
                        audit.tokens(sanitized.text), identity.title_tokens)
                    self.assertFalse(
                        flagged,
                        f"audit would flag {written!r} that masking left behind",
                    )


class TestIdentifyingPhrases(unittest.TestCase):

    def test_title_alias_and_filename_stem_are_all_collected(self) -> None:
        record = {
            "title": "Geriatric Intake Review",
            "aliases": ["Older Adult Intake"],
            "source": {"path": "domain-psychology/x/psychology_geriatric_intake.md"},
        }
        phrases = masking.identifying_phrases(record)
        self.assertIn("Geriatric Intake Review", phrases)
        self.assertIn("Older Adult Intake", phrases)
        self.assertIn("psychology_geriatric_intake", phrases)
        self.assertIn("psychology geriatric intake", phrases)

    def test_short_single_words_are_not_collected(self) -> None:
        """Redacting ``issue`` would gut ordinary prose for no benefit."""
        record = {"title": "issue", "source": {"path": "a/b/issue.md"}}
        self.assertEqual(masking.identifying_phrases(record), [])


class TestAuditGates(TempDirCase):

    def _identity(self, **kwargs) -> audit.TargetIdentity:
        base = dict(packet_id="PKT-0001", uid="pae_abc123def456",
                    public_id="skill:security/spec-to-code-compliance",
                    source_path="domain-agentic-resources/skills/security/SKILL.md",
                    title="Spec to Code Compliance", description="Checks compliance.")
        base.update(kwargs)
        return audit.TargetIdentity(**base)

    def _audit(self, text: str, **kwargs) -> audit.AuditReport:
        (self.tmp_path("packet.md")).write_text(text, encoding="utf-8")
        return audit.audit_export(self.tmp_path(), [self._identity(**kwargs)])

    def test_clean_packet_passes(self) -> None:
        report = self._audit("A body about verifying implementations.\n")
        self.assertTrue(report.passed)
        self.assertEqual(report.readiness, "READY FOR INDEPENDENT TASK AUTHORING")

    def test_uid_is_caught(self) -> None:
        report = self._audit("See pae_abc123def456 for details.\n")
        self.assertEqual(report.counts["uid"], 1)
        self.assertFalse(report.passed)
        self.assertEqual(report.readiness, "NOT READY FOR INDEPENDENT TASK AUTHORING")

    def test_public_id_is_caught(self) -> None:
        report = self._audit("skill:security/spec-to-code-compliance\n")
        self.assertGreaterEqual(report.counts["public_id"], 1)

    def test_source_path_is_caught(self) -> None:
        report = self._audit(
            "domain-agentic-resources/skills/security/SKILL.md\n")
        self.assertGreaterEqual(report.counts["source_path"], 1)

    def test_ordered_title_is_caught(self) -> None:
        report = self._audit("This is the spec to code compliance checker.\n")
        self.assertEqual(report.counts["full_title"], 1)

    def test_scattered_title_tokens_are_not_gated(self) -> None:
        """Overlap is measured, not gated — spec §5 requires content preserved."""
        report = self._audit(
            "Compliance matters. The spec is long. Write code that matches.\n")
        self.assertEqual(report.counts["full_title"], 0)
        self.assertTrue(report.passed)
        # High overlap — three of the title's four tokens are present — and the
        # export still ships. That is the whole point of measuring rather than
        # gating: a body about its own subject shares its title's vocabulary.
        self.assertGreaterEqual(report.overlap["title_token_overlap"]["max"], 0.7)

    def test_single_word_title_is_reported_not_gated(self) -> None:
        report = self._audit("We triage every issue that comes in.\n",
                             title="issue", source_path="", public_id="", uid="")
        self.assertEqual(report.counts["full_title"], 0)
        self.assertEqual(report.overlap["single_token_title_count"], 1)
        self.assertIn("PKT-0001", report.overlap["single_token_title_packets"])

    def test_gold_label_marker_is_caught(self) -> None:
        report = self._audit('{"acceptable_resource_uids": []}\n')
        self.assertGreaterEqual(report.counts["gold_label"], 1)

    def test_search_router_output_is_caught(self) -> None:
        report = self._audit("route_status: matched\n")
        self.assertGreaterEqual(report.counts["search_router_output"], 1)

    def test_reviewer_map_marker_is_caught(self) -> None:
        report = self._audit("see target_uid mapping\n")
        self.assertGreaterEqual(report.counts["reviewer_map"], 1)

    def test_unreadable_binary_is_a_problem_not_a_pass(self) -> None:
        (self.tmp_path("blob.bin")).write_bytes(b"\x00\x01\x02")
        report = audit.audit_export(self.tmp_path(), [self._identity()])
        self.assertTrue(any("non-text file" in p for p in report.problems))
        self.assertFalse(report.passed)


class TestDisjointness(TempDirCase):

    def setUp(self) -> None:
        super().setUp()
        self.author = self.tmp_path("author")
        self.reviewer = self.tmp_path("reviewer")
        self.author.mkdir()
        self.reviewer.mkdir()

    def test_disjoint_exports_pass(self) -> None:
        (self.author / "a.md").write_text("author side", encoding="utf-8")
        (self.reviewer / "b.md").write_text("reviewer side", encoding="utf-8")
        self.assertEqual(audit.assert_disjoint(self.author, self.reviewer), [])

    def test_shared_path_is_caught(self) -> None:
        (self.author / "x.md").write_text("one", encoding="utf-8")
        (self.reviewer / "x.md").write_text("two", encoding="utf-8")
        problems = audit.assert_disjoint(self.author, self.reviewer)
        self.assertTrue(any("present in both" in p for p in problems))

    def test_renamed_copy_is_caught_by_digest(self) -> None:
        (self.author / "innocent.md").write_text("the map", encoding="utf-8")
        (self.reviewer / "map.json").write_text("the map", encoding="utf-8")
        problems = audit.assert_disjoint(self.author, self.reviewer)
        self.assertTrue(any("byte-identical" in p for p in problems))


if __name__ == "__main__":
    unittest.main()

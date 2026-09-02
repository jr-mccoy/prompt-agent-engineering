"""Deterministic body sanitization for author packets (spec §5).

The author must be able to write a realistic task *about the work a resource
does* without being able to tell which resource it is. That is a narrow target:
strip too little and the packet names its own answer; strip too much and the
author is writing about nothing.

So this module removes **identity** and preserves **operation**. Frontmatter,
the title heading, UIDs, public IDs, repository paths and related-resource
lists go. Objectives, procedures, examples, constraints, thresholds and every
safety guard stay, byte for byte. Nothing is summarized and nothing is
rewritten — a paraphrase would put this module's words in front of the author
instead of the corpus's, and the tasks would then be about the paraphrase.

Every removal is a named operation recorded per packet, so a reviewer can see
what was taken out of a body without being shown the body it came from.

## Safety guards are never removed

A safety-gated resource's guard text is load-bearing content, not metadata
(``serving_policy.guard_preservation.must_not_truncate`` in the Registry). The
section remover carries an explicit protected list, and ``PROTECTED_HEADINGS``
is checked before any structural removal. A packet that silently dropped a
guard would produce a task that rewards unguarded output.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence

from .. import canonical

#: Bumped when a change would alter the sanitized bytes of a given body.
MASKING_ALGORITHM_VERSION = "author-masking/1"

#: What replaces a removed identifier. A fixed string, so two different targets
#: redact to the same token and the placeholder itself carries no signal.
REDACTION = "[identifier removed]"
PATH_REDACTION = "[path removed]"
SECTION_REDACTION = "[related-resource list removed]"

#: Headings whose sections are metadata or cross-references rather than
#: operational content. Matched case-insensitively against the heading text.
METADATA_HEADINGS = (
    "related",
    "related prompts",
    "related prompt",
    "related resources",
    "related resource",
    "related skills",
    "related work",
    "see also",
    "cross-references",
    "cross references",
    "references",
    "further reading",
    "metadata",
    "index",
    "changelog",
    "version history",
    "provenance",
    "attribution",
)

#: Never removed, whatever else matches. Guard text, limits and refusal
#: conditions are the content a safety-gated task exists to test.
PROTECTED_HEADINGS = (
    "safety",
    "safety guards",
    "safety notes",
    "guardrails",
    "guard rails",
    "guards",
    "disclaimer",
    "disclaimers",
    "limitations",
    "limits",
    "scope and limits",
    "authorization",
    "authorisation",
    "when not to use",
    "when to escalate",
    "escalation",
    "contraindications",
    "cautions",
    "warnings",
    "warning",
    "ethics",
    "ethical considerations",
    "privacy",
    "confidentiality",
    "compliance",
    "red flags",
    "refusal",
    "refusal conditions",
    "do not",
    "prohibited",
    "risk",
    "risks",
)

_FRONTMATTER = re.compile(r"\A﻿?---\r?\n.*?\r?\n---[ \t]*\r?\n?", re.DOTALL)
_UID = re.compile(r"\bpae_[0-9a-z]{6,}\b")
_PUBLIC_ID = re.compile(
    r"\b(?:prompt|skill|agent|command|persona|technique):[A-Za-z0-9][A-Za-z0-9/_.-]*"
)
#: A path with at least one separator and a repository-ish extension.
_REPO_PATH = re.compile(
    r"\b(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.(?:md|json|jsonl|ya?ml|py|tsv|txt|toml)\b"
)
#: A bare corpus filename. ``snake_case.md`` and ``SKILL.md`` both name a
#: resource file, and the first also spells out its title in words.
_BARE_FILE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9_.-]*\.(?:md|json|jsonl|ya?ml|tsv)\b")
#: A bare directory reference such as ``domain-psychology/`` or
#: ``domain-agentic-resources/skills/marketing/``.
_BARE_DIR = re.compile(r"\bdomain-[A-Za-z0-9_-]+(?:/[A-Za-z0-9_.-]+)*/?")
_HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*#*[ \t]*$")


@dataclass(frozen=True)
class SanitizedBody:
    text: str
    operations: tuple[str, ...]
    original_sha256: str
    sanitized_sha256: str
    original_bytes: int
    sanitized_bytes: int
    removed_sections: tuple[str, ...] = ()
    phrase_redactions: int = 0

    @property
    def retention(self) -> float:
        """Sanitized bytes as a fraction of the original.

        Reported per packet. A body that sanitizes down to a fragment is not a
        usable authoring brief, and the number is how that becomes visible
        instead of being discovered by an author with nothing to write about.
        """
        if not self.original_bytes:
            return 0.0
        return self.sanitized_bytes / self.original_bytes

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "algorithm_version": MASKING_ALGORITHM_VERSION,
            "operations": list(self.operations),
            "original_sha256": self.original_sha256,
            "sanitized_sha256": self.sanitized_sha256,
            "original_bytes": self.original_bytes,
            "sanitized_bytes": self.sanitized_bytes,
            "retention": round(self.retention, 4),
            "phrase_redactions": self.phrase_redactions,
            "removed_sections": list(self.removed_sections),
        }


def _heading_is_protected(text: str) -> bool:
    normalized = re.sub(r"[^a-z0-9 ]+", " ", text.casefold()).strip()
    normalized = re.sub(r"\s+", " ", normalized)
    if normalized in PROTECTED_HEADINGS:
        return True
    # A compound heading such as "Safety and Escalation" keeps its protection.
    return any(
        normalized.startswith(f"{p} ") or normalized.endswith(f" {p}") or p in
        normalized.split(" and ")
        for p in PROTECTED_HEADINGS
    )


def _heading_is_metadata(text: str) -> bool:
    normalized = re.sub(r"[^a-z0-9 ]+", " ", text.casefold()).strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized in METADATA_HEADINGS


def _strip_frontmatter(text: str) -> tuple[str, bool]:
    """Step 1 — remove YAML frontmatter.

    Frontmatter is pure identity: title, category, description, tags, technique
    codes and the related-prompt list all live there, and every one of them
    would name the target.
    """
    stripped = _FRONTMATTER.sub("", text, count=1)
    return stripped, stripped != text


def _strip_title_heading(text: str) -> tuple[str, bool]:
    """Step 2 — remove the identifying first H1.

    Only the *first* level-1 heading, and only when it precedes any other
    content-bearing heading. Lower headings are structure the author needs.
    """
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        match = _HEADING.match(line.rstrip("\r\n"))
        if match is None:
            return text, False  # prose before any heading: nothing to strip
        if len(match.group(1)) != 1:
            return text, False  # first heading is not an H1
        del lines[index]
        while index < len(lines) and not lines[index].strip():
            del lines[index]
        return "".join(lines), True
    return text, False


def _remove_metadata_sections(text: str) -> tuple[str, list[str]]:
    """Step 5 — remove related-resource and metadata sections.

    A section runs from its heading to the next heading of the same or higher
    level. Protected headings are skipped even when they also match a metadata
    name, because guard text outranks tidiness.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    removed: list[str] = []
    index = 0
    while index < len(lines):
        match = _HEADING.match(lines[index].rstrip("\r\n"))
        if match is None:
            out.append(lines[index])
            index += 1
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        if not _heading_is_metadata(title) or _heading_is_protected(title):
            out.append(lines[index])
            index += 1
            continue

        removed.append(title)
        index += 1
        while index < len(lines):
            inner = _HEADING.match(lines[index].rstrip("\r\n"))
            if inner is not None and len(inner.group(1)) <= level:
                break
            index += 1
        if out and out[-1].strip():
            out.append("\n")
        out.append(f"{SECTION_REDACTION}\n\n")
    return "".join(out), removed


def _redact_identifiers(text: str) -> tuple[str, bool]:
    """Step 3 — remove UID and public-ID strings wherever they appear."""
    redacted, uid_count = _UID.subn(REDACTION, text)
    redacted, pid_count = _PUBLIC_ID.subn(REDACTION, redacted)
    return redacted, bool(uid_count or pid_count)


def _redact_paths(text: str) -> tuple[str, bool]:
    """Step 4 — remove identity-revealing repository paths.

    A sibling reference like ``domain-psychology/.../foo_bar.md`` names a
    neighbour and, through the shared naming convention, most of the target's
    own title. Bare corpus filenames go for the same reason.
    """
    redacted, a = _REPO_PATH.subn(PATH_REDACTION, text)
    redacted, b = _BARE_DIR.subn(PATH_REDACTION, redacted)
    redacted, c = _BARE_FILE.subn(PATH_REDACTION, redacted)
    return redacted, bool(a or b or c)


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    """A separator-insensitive matcher for one identifying phrase.

    The corpus writes the same name three ways — ``spec-to-code-compliance`` in
    a filename, ``Spec-to-Code Compliance`` in a heading, ``spec to code
    compliance`` in prose. A literal matcher catches one of the three and
    reports the export clean while the title sits in the body in its other two
    forms, which is worse than not checking. So any run of non-alphanumeric
    characters in the phrase matches any such run in the text.

    The boundary classes are ``[A-Za-z0-9]`` rather than ``\\w`` on purpose:
    they must agree exactly with the audit's tokenizer, which splits on
    everything that is not alphanumeric. If the masker treated ``-`` as part of
    a word and the audit treated it as a separator, then ``C4 Component-level``
    would survive masking and still be flagged as containing the title
    ``c4-component`` — the two halves of the firewall disagreeing about what a
    word is. The invariant this preserves is simple and testable: **anything
    the audit would flag, the masker has already removed.**
    """
    parts = [re.escape(p) for p in re.split(r"[^A-Za-z0-9]+", phrase.strip()) if p]
    if not parts:
        return re.compile(r"(?!)")  # matches nothing
    return re.compile(
        r"(?<![A-Za-z0-9])" + r"[^A-Za-z0-9]+".join(parts) + r"(?![A-Za-z0-9])",
        re.IGNORECASE,
    )


def _redact_phrases(text: str, phrases: Iterable[str]) -> tuple[str, int]:
    """Remove identifying phrases — the target's title, aliases and filename.

    A title that survives in prose ("This *Geriatric Intake with Polypharmacy
    and Falls-Risk Review* produces…") hands the author the answer as directly
    as the frontmatter would.

    Returns the number of redactions, not just whether any happened, because a
    body whose own subject phrase appears forty times comes out heavily
    perforated and the caller needs to be able to say so.
    """
    total = 0
    for phrase in sorted({p.strip() for p in phrases if p and p.strip()},
                         key=len, reverse=True):
        text, count = _phrase_pattern(phrase).subn(REDACTION, text)
        total += count
    return text, total


def _collapse_blank_runs(text: str) -> str:
    """Whitespace hygiene only. Never touches a non-blank line."""
    return re.sub(r"\n{4,}", "\n\n\n", text).strip() + "\n"


def sanitize_body(
    text: str,
    *,
    identifying_phrases: Sequence[str] = (),
) -> SanitizedBody:
    """Run the §5 protocol in order and report which steps changed anything."""
    original = text
    operations: list[str] = []

    text, did = _strip_frontmatter(text)
    if did:
        operations.append("remove_frontmatter")

    text, did = _strip_title_heading(text)
    if did:
        operations.append("remove_title_heading")

    text, removed_sections = _remove_metadata_sections(text)
    if removed_sections:
        operations.append("remove_metadata_sections")

    text, did = _redact_identifiers(text)
    if did:
        operations.append("redact_identifiers")

    text, did = _redact_paths(text)
    if did:
        operations.append("redact_repository_paths")

    text, phrase_redactions = _redact_phrases(text, identifying_phrases)
    if phrase_redactions:
        operations.append("redact_identifying_phrases")

    text = _collapse_blank_runs(text)
    operations.append("collapse_blank_runs")

    return SanitizedBody(
        text=text,
        operations=tuple(operations),
        original_sha256=canonical.sha256_text(original),
        sanitized_sha256=canonical.sha256_text(text),
        original_bytes=len(original.encode("utf-8")),
        sanitized_bytes=len(text.encode("utf-8")),
        removed_sections=tuple(removed_sections),
        phrase_redactions=phrase_redactions,
    )


def identifying_phrases(record: Mapping[str, Any]) -> list[str]:
    """Every phrase that would name this target if it survived into a packet.

    Title, aliases and the filename stem rendered as words — ``psychology_
    geriatric_intake_with_polypharmacy_review`` spells out its own title once
    the underscores become spaces, so the stem is treated as a phrase too.
    """
    phrases: list[str] = []
    title = str(record.get("title") or "").strip()
    if title:
        phrases.append(title)
    for alias in record.get("aliases") or ():
        if isinstance(alias, str) and alias.strip():
            phrases.append(alias.strip())
    source = record.get("source") or {}
    stem = str(source.get("path") or "").rsplit("/", 1)[-1]
    stem = re.sub(r"\.[A-Za-z0-9]+$", "", stem)
    if stem:
        phrases.append(stem)
        spaced = stem.replace("_", " ").replace("-", " ").strip()
        if spaced and spaced.casefold() != stem.casefold():
            phrases.append(spaced)
    # Long phrases only. A one-word "title" like "Risk" would redact ordinary
    # prose and damage the operational content this module exists to keep.
    return [p for p in phrases if len(p.split()) >= 2 or len(p) >= 12]


def guard_text_preserved(original: str, sanitized: str) -> tuple[bool, list[str]]:
    """Whether every protected heading in the original survives sanitization.

    Checked per packet and enforced at export. This is the assertion that the
    masking protocol cannot quietly strip a safety guard.
    """
    def protected_headings(text: str) -> list[str]:
        found = []
        for line in text.splitlines():
            match = _HEADING.match(line.rstrip("\r\n"))
            if match and _heading_is_protected(match.group(2).strip()):
                found.append(match.group(2).strip())
        return found

    before = protected_headings(original)
    after = set(protected_headings(sanitized))
    missing = [h for h in before if h not in after]
    return (not missing), missing

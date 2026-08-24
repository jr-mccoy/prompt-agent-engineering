---
title: "Document Review Coding Taxonomy"
category: legal/discovery
description: "Design a document-review coding taxonomy — responsiveness, issue codes, privilege, hot, key, confidentiality — with definitions, decision rules, and quality-control checks calibrated to the matter and review platform."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - discovery
  - document-review
  - coding
  - taxonomy
  - privilege-review
  - tar
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
  - domain-legal/discovery/legal_privilege_log_generator.md
  - domain-legal/depositions/legal_deposition_outline_witness.md
---

**Purpose:** Build the coding scheme reviewers will apply across hundreds of thousands of documents — clear enough to be applied consistently by a junior reviewer, structured enough to support QC sampling, and rich enough to surface what matters for depositions, motion practice, and trial.

**When to use:** Standing up a review for a new matter; revising a taxonomy mid-review when the issue map has changed; harmonizing a multi-vendor or multi-firm review.

---

## Your Input

- **Matter type:** [Commercial litigation / regulatory investigation / antitrust / employment / IP / etc.]
- **Theories and claims:** [Plaintiff and defense]
- **Custodian and source set:** [Counts and platforms]
- **Review platform:** [Relativity / Reveal / Everlaw / DISCO / etc.]
- **TAR posture:** [Linear review / TAR 1.0 / TAR 2.0 / hybrid]
- **Production protocol terms:** [Confidentiality designations, family-handling rules, redaction conventions]
- **Privilege scope:** [Attorney-client; work product; common-interest; state-specific]
- **Issue list seed:** [Subjects, transactions, counterparties, time-bound events]
- **Audience for the QC:** [Senior associates and partners — who else?]

---

## Constraints

**Must:**
- Define every code with: a name, a one-sentence definition, examples (positive and negative), and decision rules for ambiguous cases.
- Make codes **mutually exclusive** within a tier where the platform's data model requires single-select; allow **multi-select** for issue tags.
- Tier the taxonomy:
  1. **Responsiveness** (Responsive / Not Responsive / Technical Non-Responsive)
  2. **Privilege** (Privileged-Withhold / Privileged-Redact / Not Privileged / Privilege-Hold-for-2L Review)
  3. **Issue codes** (multi-select, per theory)
  4. **Hot / Key / Notable** signals
  5. **Confidentiality** designations (per protective order)
  6. **Family handling** (Produce / Withhold / Redact at family level)
- Provide **decision rules** for the recurring ambiguities: forwarded news clippings; calendar invites; mass distributions; documents responsive only because of attachments; near-duplicates; chat-message threading.
- Define **escalation paths**: when a reviewer should escalate to second-level (2L) review.
- Define **QC sampling**: pre-production sampling, on-production sampling, privilege-log sampling, with target precision/recall thresholds.
- Provide a **change-management protocol** for modifying the taxonomy mid-review.

**Must Not:**
- Use vague codes ("important," "interesting") without a decision rule for inclusion.
- Allow a code that is purely subjective with no objective referent.
- Mix responsiveness and issue tagging in a single field.
- Build an issue map with so many codes (e.g., 80+ tags) that consistency collapses.
- Use privilege codes without a clawback / redaction policy tied to the review platform's affordances.
- Skip the family-handling rules; they are the single biggest source of inconsistent productions.

---

## Instructions

1. **Responsiveness layer.** Define Responsive, Not Responsive, Technical Non-Responsive (e.g., file system noise, encrypted with no key) — and the family-level treatment of each.
2. **Privilege layer.** Define Privileged-Withhold, Privileged-Redact, Privilege-Hold-for-2L. State the privileges in scope and any common-interest agreements.
3. **Issue codes.** Limit to a defensible number — typical is 8–25. Each issue gets a code, definition, examples, and decision rule. Group thematically.
4. **Signals layer.** Hot / Key / Notable — define each in terms of how the document would be used (motion practice, deposition exhibit, trial exhibit) and require a brief reviewer note.
5. **Confidentiality.** Match the protective order's tiers. Provide examples for each tier.
6. **Family handling.** Define how parent and attachment relationships affect responsiveness, privilege, and confidentiality.
7. **Special document types.** Define rules for: spreadsheets with multiple tabs, calendar invites, voicemails, audio/video, chat messages and threads, encrypted documents, near-duplicates, embedded objects.
8. **Escalation paths.** Reviewers escalate when: (a) privilege is plausible but uncertain; (b) confidentiality is unclear; (c) the document is hot; (d) responsiveness depends on a fact the reviewer cannot verify; (e) a known-counsel-name appears in metadata.
9. **QC sampling.** Pre-production responsiveness sample; pre-production privilege sample; on-production confidentiality sample; privilege-log spot-check.
10. **Change management.** Versioned taxonomy with date, owner, and rationale for each change; reviewer re-training protocol when codes change.

---

## Output Format

```markdown
# DOCUMENT REVIEW CODING TAXONOMY — {Matter}
**Version:** {N}
**Effective date:** {date}
**Owner:** {name, role}

## 1. Responsiveness

| Code | Definition | Examples | Decision rules |
|------|------------|----------|----------------|
| Responsive | Document or attachment that bears on a claim, defense, or theory in this matter, including documents reflecting communications, decisions, or events relating to {topic list}. | {examples} | Code Responsive at the document level; family-level treatment described in §6. |
| Not Responsive | Document with no bearing on the claims, defenses, or theories. | {examples} | If the document is part of a Responsive family, see §6. |
| Technical Non-Responsive | File-system or system-generated content with no usable communicative content. | {examples} | Confirm with senior reviewer when ambiguous. |

## 2. Privilege

| Code | Definition | Action | Examples |
|------|------------|--------|----------|
| Privileged-Withhold | Privilege element fully satisfied; no responsive non-privileged content. | Withhold; log per privilege-log protocol. | {...} |
| Privileged-Redact | Privileged content within a partly responsive document. | Redact privileged content; produce balance. | {...} |
| Not Privileged | No privilege element satisfied. | Produce. | {...} |
| Privilege-Hold-for-2L | Reviewer suspects privilege; cannot resolve. | Route to second-level review. | {...} |

Privileges in scope: Attorney-Client (A-C), Work Product (Opinion / Ordinary), Common-Interest (per agreement dated {date}).

## 3. Issue Codes (multi-select)

| Code | Definition | Examples (positive) | Examples (negative — Not this code) |
|------|------------|----------------------|--------------------------------------|
| ISS-01 — {Issue} | {one-sentence definition} | {...} | {...} |
| ISS-02 — {Issue} | {...} | {...} | {...} |
| ... | ... | ... | ... |

## 4. Signals

| Code | Definition | Reviewer-note required |
|------|------------|------------------------|
| Hot | Document likely to be a key exhibit at deposition, motion, or trial. | Yes — 1–2 sentences why. |
| Key | Important to the matter; not trial-exhibit-grade but consequential. | Yes. |
| Notable | Worth flagging for senior review. | Optional. |

## 5. Confidentiality

Per the Protective Order:

| Tier | Definition (per PO) | Examples |
|------|----------------------|----------|
| Confidential | {...} | {...} |
| Highly Confidential — Attorneys' Eyes Only | {...} | {...} |
| Source Code (if applicable) | {...} | {...} |

## 6. Family Handling

- A Responsive parent renders all attachments part of the produced family unless an attachment is itself privileged or wholly non-responsive and within an established carve-out.
- A Not-Responsive parent with a Responsive attachment: produce the attachment in family; treat parent per protocol (often produced as the family parent).
- A Privileged attachment within a non-privileged family: redact or withhold the attachment; produce the rest of the family.

## 7. Special Document Types

- **Spreadsheets:** apply codes at the document level; flag tab-level relevance in reviewer notes.
- **Calendar invites:** code based on the meeting's subject and the invite body; if Responsive, family includes attached agendas and slide decks.
- **Audio/video:** flag for transcription before responsive coding if practical.
- **Chat messages:** apply codes at the message-thread level; threading defined as messages within {time window} between same participants on same topic.
- **Encrypted with no key:** Technical Non-Responsive; escalate to recovery.
- **Near-duplicates:** code on the master; propagate to near-dupes with a senior-reviewer audit sample.
- **Embedded objects:** extract and code separately if the platform supports it; otherwise note in reviewer field.

## 8. Escalation Paths

Escalate to 2L when:
- Privilege is plausible but uncertain.
- Confidentiality tier is unclear.
- Document is Hot.
- Responsiveness depends on an external fact the reviewer cannot verify.
- A known-counsel name appears in author/recipient metadata.
- The document discusses litigation strategy.
- The document references an unusual data source not previously collected.

## 9. QC Sampling Plan

| Stage | Sample basis | Sample size | Pass threshold |
|-------|--------------|-------------|----------------|
| Pre-production responsiveness | Random over Responsive set | {N} | {target precision/recall} |
| Pre-production responsiveness — adverse | Random over Not Responsive set | {N} | {target} |
| Pre-production privilege | Random over Not Privileged set | {N} | {target} |
| Privilege log | Random over Privileged set | {N} | {target} |

## 10. Change Management

- Version the taxonomy. Each version carries a date, owner, and a one-paragraph rationale.
- On any code added, removed, or redefined, retrain reviewers and re-code the affected sample of completed documents.
```

---

## Verification

- [ ] Every code has definition + examples + decision rule.
- [ ] Responsiveness, privilege, issues, signals, confidentiality, and family-handling each in separate tiers.
- [ ] Issue codes are limited to a defensible number with thematic grouping.
- [ ] Family-handling rules cover responsive-parent, non-responsive-parent-with-responsive-attachment, and privileged-attachment cases.
- [ ] Special document types covered (spreadsheets, calendars, audio/video, chat, encrypted, near-dupes, embeds).
- [ ] Escalation paths defined.
- [ ] QC sampling plan with thresholds.
- [ ] Change-management protocol with versioning.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Vague codes ("important," "interesting") | Define against use ("trial-exhibit-grade," "deposition-likely") with reviewer-note requirement |
| Mixing responsiveness and issue tagging in one field | Separate fields/tiers |
| Issue tags exploding to 80+ | Cap thematically; merge near-duplicates |
| Privilege codes without redaction policy | Codes must map to platform actions (withhold / redact / produce) |
| No family-handling rules | The single biggest production-consistency failure point |
| Chat messages coded one-by-one without threading | Define the threading window and apply at thread level |
| Near-duplicate propagation without audit | Always audit-sample the propagation |
| QC thresholds without remediation plan | When sampling fails, the plan must specify re-review |
| Codes changed mid-review without re-training and re-coding | Version + retrain + recode the affected sample |

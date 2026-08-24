---
title: "Responsible AI Use in Research Audit"
category: science/ethics-integrity
description: "Inventory every way AI/LLMs were used across a research project, classify each use as acceptable-with-disclosure or unacceptable under current ICMJE/COPE/publisher consensus, draft a compliant AI-use disclosure statement, and flag any use needing remediation before submission."
techniques:
  - ST-01
  - RT-01
  - CM-02
  - QA-01
  - QA-02
  - ST-03
difficulty: advanced
tags:
  - responsible-ai
  - llm-disclosure
  - research-integrity
  - icmje
  - cope
  - ai-authorship
  - generative-ai
  - publication-ethics
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/ethics-integrity/science_authorship_and_credit_resolver.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Responsible AI Use in Research Audit

**Objective:** Build a complete inventory of how AI and large language models were used across a research project — ideation, literature search, coding, data analysis, writing, editing, and image generation — and classify each use against current ICMJE, COPE, and publisher consensus as acceptable-with-disclosure or unacceptable. It produces a use-inventory table, a draft disclosure statement, and a remediation list. It organizes and flags; it does not certify compliance with any specific venue.

**When to use:** Before manuscript submission, before posting a preprint, and whenever a coauthor or the target venue asks how AI was used in the work.

**Required inputs:**
- **Discipline.** <field; affects which AI uses are sensitive, e.g., image-heavy life sciences>
- **Study / manuscript context.** <working title, output type, target venue if known; user-supplied, never invented>
- **AI-use account.** <for each task, which tool and version, when, and what it did, in the user's own words; `[user-supplied]` for anything not stated>

**Optional inputs:**
- Target venue's current AI policy text (if known).
- Funder or institutional AI-use policy.
- Whether any AI output was published verbatim (text, figure, table, code).
- Coauthor awareness of the AI use.

**Constraints — Must:**
- Apply the current cross-publisher consensus: AI/LLMs **cannot be listed as authors**; AI use **must be disclosed** (tool, version, date, purpose, and which section/task); **authors remain fully responsible** for accuracy, integrity, and originality of all content including anything AI-assisted.
- Treat AI-fabricated or unverified citations, quotations, data, or results as integrity violations (potential misconduct), not acceptable-with-disclosure.
- Flag AI image generation and AI-altered figures separately, noting that many venues restrict or prohibit generative-AI images in scientific figures.
- Classify each use as **acceptable with disclosure / acceptable but verify-against-venue / unacceptable — remediate**, with the rationale tied to the consensus rules.
- Add a verify-against-the-target-venue's-current-policy note, since policies vary and change.

**Constraints — Must Not:**
- Do not invent facts, results, image data, institutional/journal policies, or biosecurity determinations. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not give a final biosecurity, legal, or editorial determination, and does not replace the IBC / institutional biosafety / DURC committee / journal editor / COPE process. Route formal decisions there.
- Do not assert that any specific venue permits or forbids a use unless the user supplied that policy text; otherwise mark it verify-against-venue.
- Do not certify that the work is compliant; produce the audit and flags only.
- Do not use "novel," "groundbreaking," or "first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope.** Restate discipline, output type, and venue. List every AI use the user reported; mark missing tool/version/date/purpose as `[user-supplied]`.
2. **Build the use inventory.** For each use, capture task, tool, version, date, purpose, the section/artifact affected, and whether any AI output appears verbatim in the work.
3. **Classify each use.** Apply the consensus rules to assign acceptable-with-disclosure / acceptable-but-verify / unacceptable-remediate. Be explicit when an AI listed as author, an undisclosed material use, or fabricated content is present.
4. **Scan for fabrication risk (adversarial).** Specifically check AI-assisted citations, quotes, numbers, and code for whether the author independently verified them. Unverified AI-sourced references are a remediation flag.
5. **Handle images separately.** Identify any AI-generated or AI-altered figure and flag the venue restriction; route real integrity concerns to the image-integrity self-check and correction process.
6. **Draft the disclosure statement.** Produce a concise, venue-agnostic AI-use disclosure (tool, version, date, purpose, section) plus an author-responsibility affirmation, in calibrated language.
7. **List remediation actions.** For each unacceptable/verify item, state the concrete fix (verify and re-cite, remove AI image, add disclosure, obtain coauthor sign-off, consult venue policy).
8. **Add the venue-policy note.** Remind the user to reconcile the draft disclosure with the target venue's current published policy before submission.
9. **Self-check.** Confirm no tool, version, policy, or use was invented and that every gap is `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation
[discipline, output type, venue; AI uses as reported; gaps flagged]

## AI-Use Inventory
| Task | Tool | Version | Date | Purpose | Section/Artifact | Output used verbatim? | Classification |
[acceptable w/ disclosure | acceptable — verify venue | unacceptable — remediate]

## Fabrication / Verification Scan
[citations, quotes, data, code checked for independent author verification; flags]

## Image / Figure AI Use
[AI-generated or AI-altered figures; venue-restriction flag; route to image-integrity check if needed; or "none reported"]

## Draft AI-Use Disclosure Statement
[tool + version + date + purpose + section, per use] + [author-responsibility affirmation]
Note: AI is not and cannot be listed as an author.

## Remediation List
- [item] → concrete fix → owner
...

## Venue-Policy Reconciliation Note
[verify draft disclosure against the target venue's current AI policy before submission]

## Open Items
- [ ] [user-supplied gap]
```

**Standard alignment:** ICMJE recommendations on AI/LLM use (AI cannot be an author; disclose use; authors are responsible); COPE position on authorship and AI tools; major-publisher generative-AI policies including restrictions on AI-generated images in scientific figures; research-integrity norms treating fabricated citations/data as misconduct.

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured before classification.
- [ ] Every reported AI use inventoried with tool, version, date, purpose, and affected section.
- [ ] AI not listed as an author anywhere; any such instance flagged unacceptable.
- [ ] AI-assisted citations/quotes/data/code checked for independent verification.
- [ ] AI image generation/alteration flagged against venue restrictions.
- [ ] Disclosure statement drafted with author-responsibility affirmation.
- [ ] Remediation actions concrete and assigned.
- [ ] Venue-policy reconciliation note included; nothing asserted as venue-specific without supplied policy.
- [ ] No tool, version, policy, or use invented; gaps marked `[user-supplied]`; drafted text free of "novel/groundbreaking/first-ever."

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Disclosure-as-cure | Assuming any AI use is fine once disclosed | Fabricated content and AI authorship are never curable by disclosure |
| Verbatim citations | Trusting AI-supplied references that read plausibly | Flag every AI-sourced citation for independent verification |
| Venue assumption | Stating a journal "allows" a use from memory | Mark verify-against-venue unless the user supplied the policy |
| Silent image AI | Treating a touched-up figure as ordinary editing | Flag AI generation/alteration; route to image-integrity check |
| Compliance claim | Declaring the manuscript AI-compliant | Produce audit + flags only; the editor/venue decides |

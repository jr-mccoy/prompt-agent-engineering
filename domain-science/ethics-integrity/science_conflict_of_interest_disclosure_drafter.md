---
title: "Conflict of Interest Disclosure Drafter"
category: science/ethics-integrity
description: "Elicit each author's financial and non-financial interests for a manuscript, grant, IRB submission, or peer review and draft ICMJE-form-aligned disclosure statements, defaulting to over-disclosure when in doubt."
techniques:
  - ST-01
  - RT-01
  - ST-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - conflict-of-interest
  - disclosure
  - icmje
  - financial-interests
  - non-financial-interests
  - research-ethics
  - transparency
  - integrity
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_authorship_and_credit_resolver.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/ethics-integrity/science_open_science_practices_self_audit.md
---

# Conflict of Interest Disclosure Drafter

**Objective:** Systematically elicit each author's financial and non-financial interests relevant to a specific output and venue, then draft disclosure statements aligned with the ICMJE COI form and journal/funder requirements. It produces per-author disclosures and a combined statement, with a clean "nothing to declare" branch gated by a confirmation question. It structures and drafts disclosures; it does not judge whether a conflict disqualifies anyone.

**When to use:** At manuscript submission or revision, at grant application, at IRB/ethics submission, or when accepting a peer-review or editorial assignment — and whenever a relationship changes during a project under review.

**Required inputs:**
- **Discipline.** <field; affects what funders, sponsors, and competing interests are typical>
- **Study / manuscript context.** <output type and venue: manuscript / grant / IRB / peer-review; the subject matter (e.g., a drug, device, method, company); user-supplied, never invented>
- **Author list.** <each author whose interests must be disclosed; `[user-supplied]` for any unstated relationship>

**Optional inputs:**
- The venue's specific COI policy or form fields (if not ICMJE).
- Disclosure look-back window required by the venue (e.g., 36 months).
- Funding/sponsor details and grant numbers.
- The role of any sponsor in design, conduct, analysis, or write-up.

**Constraints — Must:**
- Probe both categories per author: **financial** (research funding/grants, employment, equity/stock/options, patents/royalties/IP, honoraria, consulting/advisory, speaker fees, travel/gifts, expert testimony) and **non-financial** (personal/family relationships, academic competition, institutional interests, ideological/advocacy positions).
- Tailor the elicitation and statement to the venue type (manuscript vs. grant vs. IRB vs. peer review) and align field labels to the ICMJE disclosure form where applicable.
- Default to over-disclosure: when a relationship is borderline or its relevance is uncertain, include it and note the uncertainty.
- Provide an explicit "nothing to declare" branch that is only reachable after the user affirmatively answers a confirmation question for that author.
- Record the look-back window applied and the sponsor's role in the work.

**Constraints — Must Not:**
- Do not invent facts, contributions, financial relationships, citations, or institutional policies. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not adjudicate guilt, give a legal/HR determination, or replace the institution's research-integrity office / ORI / COPE process. Route formal allegations there.
- Do not decide whether a disclosed interest is disqualifying, nor advise concealing or minimizing a relationship.
- Do not omit a relationship the user supplied, and do not soften it with "novel/groundbreaking/first-ever" or evasive language.

**Instructions:**

1. **Confirm scope.** Restate discipline, output type, venue, subject matter, author list, and the look-back window. Mark anything missing `[user-supplied]`.
2. **Run the financial checklist per author.** For each financial category, ask whether a relationship exists within the look-back window; capture entity, nature, amount band if provided, and whether it relates to the subject matter.
3. **Run the non-financial checklist per author.** Probe personal/family ties, academic competition, institutional interests, and ideological/advocacy positions tied to the topic.
4. **Capture sponsor role.** Record funding sources and whether any sponsor influenced design, data, analysis, interpretation, or the decision to publish.
5. **Apply the over-disclosure default.** For each borderline item, include it and annotate the uncertainty rather than dropping it.
6. **Branch on "nothing to declare."** For any author with no items, present the confirmation question and only then generate the "nothing to declare" statement.
7. **Draft statements (locked).** Produce per-author disclosures and a combined statement aligned to the venue/ICMJE fields, in neutral calibrated language.
8. **Adversarial pass (QA-02).** Re-read each statement asking "what relationship might a reader later find that this omits?" and flag any gap as `[user-supplied]` to confirm.
9. **Self-check.** Confirm nothing was invented, no supplied relationship was dropped, and the look-back window and sponsor role are stated.

**Output format (locked):**

```
## Scope Confirmation
[discipline, output type, venue, subject matter, authors, look-back window]

## Per-Author Interest Table
| Author | Category (Financial/Non-financial) | Type | Entity | Relates to subject? | Within window? | Notes / uncertainty |
[`[user-supplied]` where unknown]

## Sponsor / Funder Role Statement
[funding sources, grant numbers, and sponsor influence on the work — or "no sponsor role"]

## Per-Author Disclosure Statements
- [Author]: [drafted statement, or confirmed "nothing to declare"]

## Combined Disclosure Statement (venue-ready)
[single statement aligned to ICMJE / venue fields]

## Items to Confirm Before Submission
- [ ] [user-supplied gap / borderline item flagged for over-disclosure]
```

**Standard alignment:** ICMJE COI disclosure form (financial and non-financial interests); journal- and funder-specific COI policies; WCRI Singapore/Hong Kong principles on transparency of interests.

**Verification checklist (before delivering):**
- [ ] Discipline, venue type, and subject matter captured before drafting.
- [ ] Both financial and non-financial categories probed for every author.
- [ ] Look-back window recorded and applied consistently.
- [ ] Sponsor's role in the work explicitly stated.
- [ ] Over-disclosure default applied to all borderline items.
- [ ] "Nothing to declare" only after the per-author confirmation question.
- [ ] No relationship invented or omitted; gaps marked `[user-supplied]`.
- [ ] Statements neutral, non-evasive, and free of "novel/groundbreaking/first-ever."
- [ ] No determination made about whether any interest is disqualifying.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Silent omission | A clean statement that drops a borderline tie | Over-disclose; flag uncertainty rather than exclude |
| Premature "nothing to declare" | Empty disclosure with no confirmation | Gate the branch behind an explicit confirmation question |
| Invented funder/entity | Filling a grant number or company name to look complete | Mark unknown entities `[user-supplied]`; never fabricate |
| Financial-only scan | Treating non-financial interests as out of scope | Always run the non-financial checklist per author |
| Disqualification call | Implying an interest bars participation | Disclose only; route any judgment to the venue/institution |

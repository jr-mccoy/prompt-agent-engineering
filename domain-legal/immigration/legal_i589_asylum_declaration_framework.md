---
title: "I-589 Asylum Declaration Framework"
category: legal/immigration
description: "Attorney-facing framework for structuring an asylum applicant's declaration from the applicant's own account — mapping facts to the elements (harm rising to persecution, protected ground and nexus, government actor or inability/unwillingness to protect, well-founded fear, internal relocation), checking consistency with the I-589 and every prior statement, identifying corroboration, and flagging the one-year filing deadline and bars for verification — without supplying, embellishing, or suggesting facts."
techniques:
  - ST-03
  - CM-02
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - legal
  - immigration
  - asylum
  - i-589
  - declaration
  - credibility
  - trauma-informed
  - afraid-to-return
updated: "2026-09-24"
reasoning:
  styles: [evidential, structural, protective]
  stakes: critical
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [structured, narrative]
  user_role: [lawyer]
  mode: [document, audit]
related_prompts:
  - domain-legal/immigration/legal_naturalization_eligibility_analysis.md
  - domain-legal/depositions/legal_deposition_witness_prep_script.md
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
---

# I-589 Asylum Declaration Framework

**Objective:** Help counsel turn the applicant's own account — gathered through interviews and documents — into a declaration organized around what the adjudicator must decide, in the applicant's voice, chronologically clear, and consistent with the I-589 and every prior statement. Alongside the declaration outline, produce an element map (which facts support which element and where the gaps are), a consistency audit against prior statements, a corroboration plan, and a list of legal questions for counsel (particular social group formulation, bars, deadline exceptions). The framework organizes facts; it never supplies them.

> **Scope guard — attorney-facing only.** For a licensed attorney or accredited representative preparing a client's filing. It does not evaluate anyone's eligibility or advise an individual. If the person running it is the applicant, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` to find qualified, low-cost representation.

**When to use:**
- Drafting the declaration for an affirmative asylum application or a defensive application in removal proceedings.
- Revising a declaration after new evidence, a credible fear or border interview record is obtained, or a prior filing is discovered.
- Preparing a client for testimony by identifying inconsistencies before the adjudicator does.

**Distinct from:**
- `domain-legal/depositions/legal_deposition_witness_prep_script.md` — preparing a witness for adversarial questioning in civil discovery; this is the client's own sworn narrative.
- `domain-legal/litigation/legal_trial_theme_and_narrative_designer.md` — persuasive themes for a jury; a declaration must be the applicant's truthful account, not a crafted theme.
- Country-conditions research — referenced as corroboration here; the research itself is a separate task.

**Audience:** Immigration attorneys, accredited representatives, and supervised legal staff.

---

## Your Input

- **Posture:** [Affirmative (asylum office) / defensive (immigration court); hearing or interview date]
- **Applicant's account:** [Interview notes or transcript in the applicant's words, with interpreter used and language]
- **I-589 as drafted or filed:** [Relevant answers]
- **Prior statements:** [Credible fear / reasonable fear record, border or entry statements, visa applications, prior applications — list what exists and what has been requested]
- **Dates:** [Last arrival date; filing date or planned filing date; any changed or extraordinary circumstances claimed]
- **Documents:** [Identity, medical, police, membership, threats, photos, witness statements, country-conditions sources]
- **Counsel's legal theory (if any):** [Protected ground(s), proposed particular social group formulation, persecutor identity]
- **Controlling authority supplied:** [Circuit and Board precedent the attorney has selected — otherwise placeholders]

---

## Constraints

### Must
- Use **only facts in the applicant's account or documents**; every gap becomes a question for the next client interview, never a filled-in detail.
- Keep the declaration in the **applicant's voice**, first person, with interpreter certification noted; avoid legal conclusions and terms of art in the applicant's mouth.
- Organize around the **elements** the adjudicator must decide `[VERIFY: INA §208 and 8 CFR 1208.13 / 208.13]`: harm rising to persecution (past) and/or well-founded fear (future); a protected ground that is at least one central reason for the harm; persecutor is the government or an actor the government is unable or unwilling to control; internal relocation reasonableness.
- Run a **consistency audit** line by line against the I-589 and every prior statement: dates, names, places, sequence, injuries, and omissions. For each discrepancy, record the explanation the applicant gives — do not supply one.
- Identify **corroboration** reasonably available for each key fact, and what explains unavailability `[VERIFY: corroboration standard]`.
- **Flag high-stakes deadlines and bars for counsel verification**: the one-year filing deadline and any exception claimed, and potential bars (e.g., persecutor, serious nonpolitical crime, firm resettlement) `[VERIFY: INA §208(a)(2), (b)(2)]`.
- Use **trauma-informed** structure: note where memory gaps, sequence uncertainty, or reluctance may occur and how the declaration truthfully reflects uncertainty ("I do not remember the exact date; it was after the harvest").

### Must Not
- Invent, embellish, intensify, or "strengthen" any fact, date, injury, threat, or motive.
- Harmonize inconsistencies by choosing the more favorable version; surface them for counsel and client.
- Import language from other declarations, templates, or country reports as if it were the applicant's experience.
- Formulate a particular social group or assert a legal conclusion as settled; mark `[NEED HOLDING: circuit / Board authority]`.
- Compute the one-year deadline or evaluate an exception as decided; mark `[VERIFY — attorney determination]`.
- Communicate with or advise the applicant; outputs are for counsel.

---

## Instructions

1. **Timeline extraction.** Build a dated (or relatively dated) chronology from the account; mark each entry with its source (interview date, page).
2. **Element map.** For each element, list the facts that support it, with source, and the gaps.
3. **Nexus analysis for counsel.** What the account says about why the persecutor acted (statements made, targeting pattern) — the applicant's words, not inferences. Legal formulation left to counsel.
4. **State action / protection.** Reports to police or authorities, their response, or why the applicant did not report — in the applicant's words.
5. **Relocation.** Whether the applicant moved within the country, what happened, and why relocation was or was not possible.
6. **Consistency audit** against the I-589 and prior statements.
7. **Corroboration plan** — key fact → document → status → explanation if unavailable.
8. **Declaration outline** in the applicant's voice: background and identity → the protected characteristic in the applicant's life → escalating incidents in order → reports / protection sought → flight → fear of return → closing attestation.
9. **Counsel question list** — legal theory choices, bars, deadline, follow-up interview questions.

---

## Output Format

```markdown
# Declaration Framework — {Applicant initials} — {A-Number if any}
**Posture:** {…}  |  **Next date:** {…}  |  **Interpreter / language:** {…}  |  **Attorney Work Product**

## 1. Chronology
| # | Date (or relative) | Event (applicant's words) | Source |
## 2. Element Map
| Element | Supporting facts (source) | Gaps / follow-up questions |
## 3. Consistency Audit
| Topic | Declaration | I-589 | Prior statement (which) | Discrepancy | Applicant's explanation |
## 4. Corroboration Plan
| Fact | Evidence | Status | If unavailable — why |
## 5. Declaration Outline (applicant's voice)
## 6. Deadlines and Bars — for Attorney Verification
- One-year filing deadline: arrival {date} / filing {date} → [VERIFY — attorney determination; exception claimed?]
- Potential bars flagged: {…} [VERIFY]
## 7. Counsel Question List
```

---

## Worked Example

**Input (abridged, fictional):** Applicant "R.M.," a journalist from Country A. Account: after publishing articles on local officials in 2024, received phone threats; in March 2025, men in plain clothes detained and beat R.M. for two days; R.M. moved to the capital, was found and threatened again in June 2025; fled, arriving in the U.S. on 2025-08-10. Credible fear record states the detention lasted "one night."

**Output (excerpt):**

> **Element map — nexus:** Supporting: interview p. 4 — "they said I would stop writing about the mayor or disappear" (statement linking harm to reporting). Gap: whether the detainers identified themselves or whom they worked for → follow-up question 3. Legal characterization (political opinion, actual or imputed) → counsel `[NEED HOLDING: circuit authority on journalism as political opinion]`.
>
> **Consistency audit:** Detention length — declaration draft "two days" vs. credible fear record "one night." Applicant's explanation, asked at the second interview: *[not yet asked — add to follow-up list]*. Do not resolve in the draft.
>
> **Relocation:** Applicant moved to the capital and was located within three months — facts relevant to whether internal relocation is reasonable; counsel to assess the presumption that applies if past persecution is established `[VERIFY: 8 CFR 1208.13(b)]`.
>
> **Deadlines:** Arrival 2025-08-10. The one-year filing date (on or about 2026-08-10) **appears to have passed** as of this framework's date — confirm first whether, and on what date, an I-589 was filed (including any filing with the court or a prior affirmative filing) `[NEED: I-589 filing date and forum]`. If none was filed in time, list for attorney decision the possible exceptions and the facts that would support them: changed circumstances (e.g., new events in Country A or in R.M.'s own situation), extraordinary circumstances (e.g., serious illness, trauma-related incapacity, ineffective assistance, maintained lawful status), and whether the application was filed within a reasonable period after the circumstance; note that withholding of removal and CAT protection carry no one-year bar `[VERIFY: INA §208(a)(2)(B), (D); 8 C.F.R. §208.4(a) — attorney determination]`.

---

## Verification

- [ ] Jurisdiction lock: forum (asylum office / immigration court) and circuit identified; authority limited to supplied or placeholders.
- [ ] Every fact in the declaration traces to the applicant's account or a document.
- [ ] No embellishment, harmonization, or imported template language.
- [ ] Every element mapped with gaps listed.
- [ ] Consistency audit covers the I-589 and every prior statement; discrepancies unresolved unless the applicant explained them.
- [ ] Corroboration plan with unavailability explanations.
- [ ] One-year deadline and bars flagged for attorney verification.
- [ ] Outputs addressed to counsel only.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Filling a gap with a plausible detail | Convert every gap into a follow-up interview question |
| Picking the more favorable version of an inconsistent fact | Surface both versions and the applicant's explanation, if any |
| Writing legal conclusions in the applicant's voice ("I was persecuted on account of…") | Describe events and what persecutors said; leave legal characterization to counsel's brief |
| Borrowing phrasing from country reports or other declarations | Use only the applicant's words; country conditions go in exhibits |
| Treating the one-year deadline as computed or an exception as established | Flag for attorney determination with dates |
| Ignoring prior statements not yet obtained | List them as outstanding and hold finalization until reviewed |
| Smoothing over memory gaps | State uncertainty truthfully; trauma can affect recall and sequence |

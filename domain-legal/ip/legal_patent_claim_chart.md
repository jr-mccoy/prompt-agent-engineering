---
title: "Patent Claim Chart (Infringement and Invalidity)"
category: legal/ip
description: "Element-by-element claim chart mapping each asserted claim element to evidence in an accused product (infringement) or to disclosures in a prior-art reference (invalidity), with literal/DOE analysis, §112(f) treatment, and prosecution-history estoppel flags."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - ip
  - patent
  - claim-chart
  - infringement
  - invalidity
updated: "2026-05-11"
related_prompts:
  - domain-legal/ip/legal_trademark_clearance_analysis.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-legal/research/legal_precedent_comparison_table.md
---

**Purpose:** Produce a row-per-element claim chart that maps each asserted claim element to specific cited evidence — for **infringement** (accused product / process) or **invalidity** (prior-art reference). Output must be defensible in an ITC investigation, district-court contention, IPR petition, or PTAB proceeding.

**When to use:** Drafting initial / final infringement contentions, invalidity contentions, IPR/PGR petitions before the PTAB, Federal Circuit appendix exhibits, pre-suit Rule 11 investigations, freedom-to-operate analyses, licensing negotiations.

---

## Your Input

- **Jurisdiction / forum:** [US federal district + division / ITC (337 investigation) / PTAB IPR/PGR/CBM / Federal Circuit / foreign — note that this chart assumes US patent law unless otherwise specified]
- **Chart purpose:** [Infringement (literal / DOE) / Invalidity (§102 anticipation / §103 obviousness / §112 written description, enablement, indefiniteness)]
- **Asserted patent:** [Patent number — use `[CITE: U.S. Pat. No. _______]` if unknown; do not fabricate]
- **Asserted claim(s):** [Independent and dependent claim numbers, with full claim text as supplied — quote verbatim; do not paraphrase]
- **Claim construction posture:** [Plain and ordinary meaning / Markman order issued? / proposed constructions / agreed constructions / disputed terms]
- **§112(f) means-plus-function elements:** [Identified means/step terms, if any, with corresponding structure from spec]
- **Accused instrumentality (infringement) OR prior-art reference (invalidity):** [Product name and version, or reference identifier — patent, publication, product, public use, on-sale activity]
- **Evidence sources:** [Datasheets, user manuals, source code printouts (with Bates), deposition transcripts, expert declarations, photographs, marketing materials, schematics, FOIA records — each with citation pinpoint]
- **Theory:** [Direct infringement §271(a) / induced §271(b) / contributory §271(c) / §271(f) / §271(g); or §102(a)(1) anticipation / §102(a)(2) AIA / §103 obviousness / §112 invalidity]
- **Priority date / critical date:** [For invalidity — pre-AIA vs AIA controls which §102 framework applies]
- **DOE posture (infringement):** [Whether DOE is being asserted; element(s) under DOE; function/way/result articulation OR insubstantial-differences theory]
- **Prosecution history:** [Amendments narrowing claim scope; arguments distinguishing prior art — flag PHE exposure for any element]
- **Obviousness combination (invalidity §103):** [Primary reference + secondary reference(s); motivation to combine; reasonable expectation of success; secondary considerations evidence]

---

## Constraints

**Must:**
- Quote each claim element **verbatim** from the patent — do not paraphrase, summarize, or renumber.
- One **claim element** per row. Break long elements at natural sub-clause boundaries only when the construction supports it.
- Cite specific evidence with pinpoint (page, line, column, figure, deposition page:line, source-code file:line, Bates number).
- Apply the **controlling claim construction** if one exists; otherwise plain and ordinary meaning to a POSITA at the priority date.
- For **§112(f) elements**, identify the disclosed structure in the specification and apply the two-step *Williamson*/*Aristocrat* test (identical or equivalent structure performing identical function).
- For **DOE**, articulate function/way/result for each element OR apply the insubstantial-differences test. Flag every DOE assertion separately from literal infringement.
- For **§102 anticipation**, every element must be disclosed in a single reference, arranged as in the claim.
- For **§103 obviousness**, identify the combination, the motivation to combine (with citation), reasonable expectation of success, and address known secondary considerations (commercial success, long-felt need, failure of others, copying, unexpected results, skepticism, praise).
- Flag **prosecution-history estoppel** (*Festo*) for any element where the applicant narrowed scope by amendment or argument — and identify whether DOE is foreclosed for that element.
- Use `[CITE: ...]` for any authority you cannot verify and `[NEED: ...]` for missing evidence.

**Must Not:**
- Fabricate patent numbers, claim text, evidence citations, prior-art identifiers, or case citations.
- Conflate literal infringement and DOE in the same row without separate analysis.
- Cite *Festo* / *Warner-Jenkinson* / *KSR* / *Graham* / *Phillips* without verifying the proposition — use `[CITE: ...]` if uncertain.
- Use "the accused product practices this element" as a conclusion without cited evidence.
- Apply the pre-AIA §102 framework to an AIA patent (effective filing date on or after March 16, 2013), or vice versa.
- Omit the §112(f) analysis for any means-plus-function or step-plus-function element.
- Treat dependent claims as automatically infringed/anticipated when the independent claim is — each dependent element gets its own row.

---

## Instructions

1. **Header block.** Patent number, claim asserted, accused instrumentality or prior-art reference, chart purpose, claim construction posture, priority/critical date.
2. **Preamble row.** Quote the preamble. State whether it is limiting under the applicable test (*Catalina Marketing*, structural-vs-purpose). Map evidence only if limiting.
3. **Element rows (one per element).** For each element, three columns minimum:
   - **Claim Element (verbatim):** Exact claim language with sub-letter labels (1[a], 1[b], 1[c]...).
   - **Construction Applied:** Plain meaning, or the construction from a Markman order, or the proposed construction with citation.
   - **Evidence in Accused Product / Prior-Art Reference:** Cited proof with pinpoint. For infringement, include source (datasheet col:line, source file:line, deposition pg:line, photograph fig:N). For invalidity, the reference column with col:line / pg:line.
4. **§112(f) handling.** For each means/step element, add a sub-row identifying the corresponding structure from the specification and the alleged identical-or-equivalent structure in the accused product (or its absence, for non-infringement / indefiniteness).
5. **DOE analysis (infringement only).** Separate row beneath any element where literal infringement is contested. State function/way/result for the claim element and for the accused feature. Conclude substantial-identity or insubstantial-differences. Flag PHE foreclosure if applicable.
6. **Prosecution-history estoppel flag.** For each amendment or argument identified, state the surrendered subject matter and which DOE theories are foreclosed.
7. **Anticipation (§102) summary row.** Confirm single reference, arranged-as-in-the-claim, enablement of the reference, public availability before the critical date.
8. **Obviousness (§103) summary block.** Primary + secondary references; what each teaches; motivation to combine with cited basis (problem to be solved, *KSR* rationales, market pressure); reasonable expectation of success; secondary considerations table with nexus.
9. **Dependent claims.** Repeat the row structure for each additional limitation. Do not re-chart the incorporated independent-claim elements.
10. **Open issues / NEEDs.** Bullet list of missing evidence, disputed constructions, and unresolved doctrinal questions.

---

## Output Format

```markdown
# Claim Chart — U.S. Pat. No. {patent} — Claim {N}
**Purpose:** {Infringement | Invalidity — §102 / §103 / §112}
**Accused instrumentality / Prior-art reference:** {name + version | reference ID}
**Claim construction posture:** {Markman order entered {date} | proposed constructions | plain meaning}
**Priority/critical date:** {date} ({pre-AIA | AIA})

## Preamble
> "{Verbatim preamble text}"
**Limiting?** {Yes/No — basis: [CITE: applicable authority]}
**Evidence (if limiting):** {citation}

## Element 1[a]: "{verbatim element text}"
| Construction Applied | Evidence (Accused Product / Prior Art) |
|---|---|
| {Construction or "plain and ordinary meaning"} | {Citation with pinpoint, e.g., "Product Datasheet at 12 (Fig. 3) [Bates DEF-00045]"; or "Smith Patent col. 4:23-37"} |

**§112(f) analysis (if applicable):**
- Function: {...}
- Corresponding structure (spec): {col:line citation}
- Accused structure: {citation} — {identical | equivalent under Odetics | absent}

**DOE analysis (if asserted):**
- Function / Way / Result of claim element: {...}
- Function / Way / Result of accused feature: {...}
- Conclusion: {substantial identity | insubstantial differences | not equivalent}
- PHE: {No estoppel | Estoppel applies — amendment on {date} surrendered {scope}; DOE foreclosed for {range}}

## Element 1[b]: "{verbatim}"
{...same row structure...}

## §102 Anticipation Summary (invalidity only)
- Single reference: {ref ID}
- Arranged as in the claim: {Yes — see elements above}
- Enablement of reference: {citation showing POSITA could practice without undue experimentation}
- Public availability before critical date: {evidence + date}

## §103 Obviousness Summary (invalidity only)
| Reference | Teaches | Pinpoint |
|---|---|---|
| {Primary} | {limitations a, c, d} | {col:line} |
| {Secondary} | {limitation b} | {col:line} |

**Motivation to combine:** {Articulated reason — KSR rationale: design need, market pressure, predictable variation, obvious-to-try [CITE: ...]}
**Reasonable expectation of success:** {basis}
**Secondary considerations (with nexus to claimed invention):**
- Commercial success: {evidence | [NEED: sales data]}
- Long-felt need: {evidence | None known}
- Failure of others: {...}
- Copying: {...}
- Unexpected results: {...}

## Dependent Claim {N+1} — Additional Limitation
**Element {N+1}[a]:** "{verbatim added limitation}"
{row structure}

## Open Issues / NEEDs
- [NEED: Source-code excerpt for {module} to confirm Element 1[c]]
- [NEED: Deposition of {engineer} on the structure of {accused feature}]
- Disputed construction of "{term}" — {party A position vs party B position}
- PHE scope of {date} amendment unresolved
```

---

## Verification

- [ ] Every claim element is quoted verbatim — none paraphrased.
- [ ] One claim element per row; sub-elements labeled (1[a], 1[b]...).
- [ ] Each element row has a cited pinpoint to evidence (or `[NEED: ...]`).
- [ ] Claim construction applied is identified (Markman order, agreed, proposed, or plain meaning).
- [ ] §112(f) means/step elements have corresponding structure identified from the specification.
- [ ] DOE rows are separate from literal-infringement rows; function/way/result or insubstantial-differences articulated.
- [ ] Prosecution-history estoppel evaluated for every DOE assertion.
- [ ] §102 anticipation chart confirms single reference + arranged-as-in-the-claim + enablement + public availability.
- [ ] §103 obviousness chart identifies motivation to combine, reasonable expectation of success, and secondary considerations with nexus.
- [ ] Pre-AIA vs AIA framework applied based on effective filing date.
- [ ] No fabricated patent numbers, claim text, citations, or evidence pinpoints.
- [ ] Dependent claims charted only for the additional limitation, not the incorporated independent-claim elements.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Paraphrasing claim language ("the system has a controller that...") | Quote claim language verbatim; paraphrase only in the "construction applied" column |
| Asserting DOE without function/way/result or insubstantial-differences | Articulate the test for the specific element; conclusory equivalence is not a contention |
| Ignoring §112(f) for a "means for" or "step for" element | Identify corresponding structure in the spec; if none, the element is indefinite under *Williamson* |
| Citing the accused product spec sheet generally ("the product does this") | Pinpoint citation — page, figure, column, Bates number |
| Combining literal infringement and DOE in one analysis | Separate rows; PHE may foreclose DOE even where literal fails |
| §102 anticipation pieced together from multiple references | Anticipation requires a single reference disclosing every element arranged as in the claim — multi-reference is §103 |
| §103 obviousness without articulated motivation to combine | Post-*KSR* still requires articulated reasoning with rational underpinning; conclusory obviousness fails |
| Treating dependent claims as automatically following the independent | Each added limitation requires its own evidence row |
| Applying pre-AIA §102(b) one-year grace period to an AIA patent | AIA §102(b)(1) has a different scope — verify filing date |
| Fabricating *Festo* / *KSR* / *Phillips* quotations | Use `[CITE: ...]` placeholder if not verified from the opinion |
| Asserting secondary considerations without nexus | Sales, copying, praise must be tied to the claimed features, not the product generally (*Fox Factory*) |

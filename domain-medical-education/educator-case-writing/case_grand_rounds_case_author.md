---
title: "Grand Rounds Case Author"
category: medical-education/educator-case-writing
description: "Author a complete grand rounds case package: progressive case presentation with diagnostic reveal at the right moment, integrated literature review with cited evidence, audience-facing discussion questions, and 3 teaching takeaways. Includes a source-fidelity audit and refuses to invent literature citations or guideline thresholds."
techniques:
  - ST-02
  - ST-03
  - DT-04
  - CM-02
  - RT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - program-director
  - assessment-faculty
  - curriculum-designer
tags:
  - grand-rounds
  - case-presentation
  - literature-review
  - cme
  - teaching-takeaways
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_morning_report_case_author.md
  - domain-medical-education/educator-case-writing/case_mm_case_author.md
  - domain-medical-education/educator-case-writing/case_progressive_disclosure_case_author.md
  - domain-healthcare-clinical/prompts/education/medicine_literature_synthesizer.md
---

## Objective

Produce a complete grand rounds case package: (1) progressive case presentation in 4–6 stages, (2) diagnostic reveal at the engineered tension point (not Stage 1), (3) integrated literature review (≥ 3 cited sources) on the case's teaching axis, (4) 5–8 audience-facing discussion questions interleaved through the slides, (5) 3 teaching takeaways the audience leaves with, (6) source-fidelity audit table.

## Your Role

Grand rounds case author with a senior-faculty habit: the audience leaves with three things they didn't know before AND a question they wish they'd thought of. You build for the senior attending in the third row who has seen the disease before — *they're* your toughest audience.

## Inputs

- `specialty`: e.g., "internal medicine," "pediatrics," "general surgery"
- `clinical_theme`: the teaching axis — e.g., "diagnostic delay in atypical TTP," "post-op anastomotic leak recognition," "thyroid storm in pregnancy"
- `case_type`: `index case (well-known dx, surprising path) | rare dx (zebra) | common dx with twist | quality / safety event`
- `audience`: `attendings + residents + students | residents + students | specialty section only`
- `duration_min`: 45 / 60 (default 60)
- `lit_focus`: 1–2 PICO questions or named guidelines the audience should walk away knowing about
- `include_pathology_imaging`: bool — adds slide stubs for path / imaging if relevant
- `include_audience_polling`: bool — adds polling questions interspersed

## Method

1. **Plan the diagnostic-reveal arc (DT-04 — multi-layer).** Engineer the case in stages so the diagnosis is unclear until ~stage 4 of 5/6. The reveal should *teach the discriminator*, not just announce the answer.
   - Stage 1: presentation + initial workup. Diagnosis ambiguous.
   - Stage 2: more data. A red herring should resolve here.
   - Stage 3: new finding that pivots the differential.
   - Stage 4: confirmatory test / diagnosis.
   - Stage 5: management course + complications.
   - Stage 6 (optional): outcome + lessons learned.

2. **Engineer the tension point.** What's the moment the audience sits up? Often:
   - A test result inconsistent with the working dx.
   - A failed first-line therapy.
   - An unexpected complication.
   - A history detail elicited late.
   - State the tension point explicitly in the script.

3. **Literature review (RT-05 evidence-based reasoning).** Identify the 2–3 most cite-worthy studies for the case's `clinical_theme`:
   - Landmark trial / meta-analysis.
   - Current guideline (with edition + year).
   - 1 recent paper (≤ 3 yr) updating practice.
   - Each citation: author, journal, year, key finding in 1 sentence, applicability to the case in 1 sentence.

4. **Discussion questions.** 5–8 questions placed at decision points in the case:
   - 1–2 diagnostic ("at this point, what's on your differential?").
   - 1–2 workup ("what's the next test?").
   - 1–2 management ("what would you do?").
   - 1–2 outside-the-case ("how would this change if…").
   - Each Q has a 2–3 sentence facilitator's note.

5. **Teaching takeaways (3 exactly).** Each takeaway is:
   - A behavioral change ("From now on, when I see X, I will Y"), not "be aware."
   - 1 sentence.
   - Anchored to the case + the literature.

6. **Source-fidelity audit (QA-12).** All clinical facts, lab values, drug doses, citations traceable. No invented sources, no "Smith et al. 2018" without verification. Audit table:
   - Claim → Source → Verified Y/N (with PMID / DOI when possible).
   - Marked `[verify before presentation]` if not directly confirmable.

7. **Anti-pattern check.** Reject if:
   - Diagnosis revealed in Stage 1 (no tension).
   - More than 3 takeaways (audience won't remember).
   - "Be aware of" or "consider" as a takeaway.
   - Citation without journal + year + sentence.

## Output Format

```
GRAND ROUNDS CASE — [title]
Specialty: [...]   Theme: [...]   Type: [...]   Audience: [...]   Duration: [N] min

>>> CASE ARC (4–6 stages)
Stage 1 — [title]
  Presentation: [content]
  Working dx: [list]
Stage 2 — [title]
  New data: [...]
  Working dx update: [...]
Stage 3 — [title]
  Tension point — [explicit description]
  New data: [pivoting finding]
  Working dx update: [...]
Stage 4 — [title]
  Confirmatory: [test / dx]
  Diagnosis revealed.
Stage 5 — [title]
  Management: [...]
  Complications: [...]
Stage 6 (optional) — [title]
  Outcome: [...]

>>> TENSION POINT
[Explicit description of the moment the audience pivots; e.g., "ferritin 4,500 with otherwise unremarkable infection workup forces HLH onto the differential, displacing sepsis"]

>>> LITERATURE REVIEW
1. [Author, Journal, Year]. PMID/DOI.
   Key finding: [1 sentence].
   Applies because: [1 sentence].
2. [Guideline, edition, year].
   Key recommendation: [1 sentence].
   Applies because: [1 sentence].
3. [Recent paper, ≤ 3 yr].
   Key finding: [1 sentence].
   Applies because: [1 sentence].

>>> DISCUSSION QUESTIONS (5–8)
Q1 (after Stage 1): "At this point, what's on your differential? What rules in/out [...]?"
  Facilitator note: [...]
Q2 (after Stage 2): ...
Q3 (after Stage 3): ...
Q4 (after Stage 4): ...
Q5 (after Stage 5): ...
Q6 (outside the case): "How would your approach change if the patient were [...]?"
  Facilitator note: [...]
...

>>> 3 TEACHING TAKEAWAYS
T1: "When I see [finding], I will [behavior]." (anchored to [literature item])
T2: "When [X], I will [Y]."
T3: "When [X], I will [Y]."

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Verified |
|---|---|---|
| Ferritin > 500 + cytopenia + hepatosplenomegaly → HLH spectrum (H-Score) | PMID 24935898 (Fardet 2014) | Y |
| Anakinra dose in HLH | Eloseily 2020 ART | Y, dose verified per literature; institution-specific |
| ... | ... | ... |
[verify before presentation]: rows that need final confirmation.

>>> ANTI-PATTERN CHECK
Stage 1 reveal: pass
Takeaway count: 3
Takeaway form: behavioral ("I will…"), not "be aware"
Citation format: author + journal + year + 1-sentence finding + applicability — pass

>>> REJECTED ELEMENTS (≥ 1)
Considered: ending with "this case reminds us to keep a broad differential."
Rejected: not a behavioral takeaway; not actionable.
Replaced with: T3: "When sepsis workup is negative but ferritin > 5,000, I will calculate H-score before continuing antibiotics."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `case_type` | Zebra cases lean on rare-disease pattern; common-with-twist leans on premature-closure teaching |
| `audience` | Mixed audience requires defining specialty terms; specialty-only allows tighter jargon |
| `duration_min` | 45-min trims literature to 2 sources + 5 questions |
| `lit_focus` | Forces literature to a specific PICO |
| `include_pathology_imaging` | Adds slide stubs for path / imaging with caption + teaching point |
| `include_audience_polling` | Adds polling stems (clicker / Poll Everywhere format) |
| `align_to_MOC` | Adds CME / MOC eligibility note + ABMS-style learning objectives |

## Verification Checklist

- [ ] Diagnosis not revealed until ≥ Stage 4 of the arc.
- [ ] Tension point is named explicitly.
- [ ] ≥ 3 literature citations with author, journal, year, 1-sentence finding, 1-sentence applicability.
- [ ] Discussion questions placed at decision points, not at the end.
- [ ] Exactly 3 takeaways, each in behavioral "I will" form anchored to literature.
- [ ] Source-fidelity audit table populated with verification status.
- [ ] No invented PMIDs / DOIs / studies.
- [ ] No "be aware" / "keep in mind" / "consider" takeaways.
- [ ] Anti-pattern check passes.
- [ ] At least one rejected element shown.
- [ ] If `align_to_MOC`, the learning objectives are written in measurable form.

## Worked Example (compact)

**Input:** `specialty = "internal medicine"`, `clinical_theme = "secondary HLH in adults"`, `case_type = "zebra (rare dx)"`, `audience = "attendings + residents + students"`, `duration_min = 60`, `lit_focus = "diagnosis criteria (H-Score) and anakinra in adult HLH"`.

**Output (abbreviated):**

```
GRAND ROUNDS — "Fever, Pancytopenia, Ferritin 5000: Beyond Sepsis"
Specialty: IM   Theme: secondary HLH   Type: zebra   Audience: mixed   Duration: 60 min

>>> CASE ARC
S1: 42M, 2 wk fever, fatigue, RUQ pain. Initial labs: WBC 2.1, Hgb 9.0, Plt 80. AST 200, ALT 180. UA normal. Working dx: viral hepatitis / sepsis.
S2: Blood cx negative × 48 h. Vanc/cef started empirically. Persistent fever. HSV PCR neg, hepatitis serologies neg. CT shows splenomegaly. Working dx: occult infection, lymphoma.
S3 [TENSION]: Ferritin returns at 5,800 ng/mL. Triglycerides 350. Fibrinogen 140. — Audience sit-up moment. Working dx pivots: HLH.
S4: H-Score 250 (~99% probability). Bone marrow biopsy shows hemophagocytosis. Soluble IL-2R elevated. Diagnosis: secondary HLH.
S5: Investigated trigger — EBV PCR + 10,000 copies. Started dex + etoposide; later switched to anakinra given liver dysfunction. Improved over 14 days.
S6: 6-mo follow-up: in remission.

>>> TENSION POINT
Ferritin 5,800 with negative infection workup forces audience to ask "is this still sepsis?" The pivot is the discriminator: marked hyperferritinemia + cytopenias + organomegaly meet H-Score threshold.

>>> LITERATURE
1. Fardet 2014, Arthritis Rheum. PMID 24935898.
   H-Score for HLH diagnosis (≥ 169 sens 93%, spec 86%).
   Applies: provides quantitative threshold; our case scored 250.
2. ACR / Adult HLH consensus 2021.
   Recommendation: H-Score for screening; bone marrow + soluble IL-2R for confirmation.
   Applies: anchors our workup sequence.
3. Eloseily 2020, Arthritis Rheumatol.
   Anakinra in sec HLH — 80% response, lower liver toxicity than HLH-94 etoposide.
   Applies: justified our switch when LFTs worsened on etoposide.

>>> DISCUSSION
Q1 (after S1): DDx? Facilitator note: surface sepsis, viral hepatitis, lymphoma. If "HLH" comes up, push back: "what makes you think HLH this early?"
Q2 (after S2): why is empiric antibiotic without source not yet sufficient?
Q3 (after S3 — tension): What single lab made you pivot?
Q4 (after S4): What's the H-Score threshold? What does score 250 mean?
Q5 (after S5): When would you choose anakinra over HLH-94 dex/etoposide?
Q6 (outside): If patient were 7 yr old, what changes about Dx & Rx?

>>> 3 TAKEAWAYS
T1: "When sepsis workup is negative AND ferritin > 5,000 AND cytopenias persist, I will calculate H-Score before continuing broad-spectrum antibiotics." (Fardet 2014)
T2: "When HLH is suspected, I will order soluble IL-2R + triglycerides + fibrinogen with bone marrow consideration, not just ferritin alone." (ACR 2021)
T3: "When etoposide-based HLH therapy is limited by hepatic dysfunction, I will consider anakinra as an alternative." (Eloseily 2020)

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Verified |
|---|---|---|
| H-Score thresholds | PMID 24935898 | Y |
| Anakinra response rate ~80% | Eloseily 2020 ART | Y, narrow population — flag as institutional |
| ACR consensus recommendation order | ACR 2021 consensus | Y |
| Ferritin 5800 in our patient | case (de-identified) | Y |

>>> ANTI-PATTERN CHECK
Stage 1 reveal: pass (revealed at S4).
Takeaways: 3.
Takeaway form: all behavioral.
Citation format: ok.

>>> REJECTED
Considered: takeaway "consider HLH in unexplained fever."
Rejected: not actionable.
Replaced with: T1.
```

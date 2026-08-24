---
title: "Problem List Builder from Notes"
category: domain-healthcare-clinical/workflow
description: "Reconstruct and reconcile a clean, prioritized, ICD-codable problem list from unstructured notes — collapsing duplicates, resolving stale entries, and surfacing undocumented problems."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - workflow
  - problem-list
  - documentation
  - ehr
updated: "2026-06-19"
---

## Objective

Take unstructured clinical narrative — progress notes, consult notes, discharge summaries — and build a reconciled problem list: active problems with the right specificity, duplicates merged, resolved problems retired, and clinically present problems that were never formally listed surfaced. The output is the structured backbone other workflows (care gaps, coding, summarization) depend on, so accuracy and specificity matter more than brevity.

## Inputs

- The source notes (paste or reference)
- The existing problem list, if any (to reconcile against rather than rebuild blind)
- Whether ICD-10 coding specificity is required (billing context) or a clinical problem list suffices
- Any known conditions the clinician wants confirmed present/absent

## Role

Attending cleaning up an inherited problem list that has accreted duplicates and vague entries over years of different documenters.

## Reasoning Steps

1. **Extract every candidate problem from the narrative,** including diagnoses, chronic conditions, significant historical events, and active symptoms without a diagnosis yet. Cast wide on the first pass.

2. **Promote specificity.** Replace vague entries with the most specific supportable diagnosis. "Diabetes" → "Type 2 diabetes mellitus with diabetic chronic kidney disease" if the notes support it. "CKD" → "CKD stage 3b (eGFR 38)." Specificity drives both clinical clarity and coding accuracy — but only assert the specificity the record supports. Do not invent a stage, type, or complication the notes don't document.

3. **Merge duplicates and synonyms.** "CHF," "heart failure," "HFrEF," and "systolic dysfunction" scattered across notes are one problem. Collapse them into a single best-specified entry. Watch for near-duplicates that are actually distinct (CKD vs. AKI-on-CKD).

4. **Classify status: active vs. resolved vs. historical.** Active changes current care. Resolved means truly done (treated infection, healed fracture). Historical-but-relevant (prior cancer in surveillance, prior VTE) stays as an active or surveillance item, not "resolved," because it changes future decisions. Retire genuinely stale entries (a UTI from 2019 still listed active).

5. **Surface undocumented-but-present problems.** If the notes mention an eGFR of 35 across multiple visits but CKD is not on the list, add it. If recurrent A1c values >9 appear but "uncontrolled diabetes" isn't captured, flag it. These omissions are where the list fails the next reader.

6. **Prioritize the list** by current clinical weight, not alphabetically or by code. The problem driving the most decisions goes first.

7. **Link complications to their root** where the relationship is clinically meaningful (diabetic nephropathy under diabetes; AFib with the relevant anticoagulation consideration noted). This preserves the reasoning, not just the labels.

8. **Flag reconciliation actions** — entries you merged, retired, added, or up-specified — so the clinician can review the changes rather than trust a silent rewrite. Note anything ambiguous that needs chart confirmation.

## Output Format

```
RECONCILED PROBLEM LIST (prioritized by current clinical weight):

ACTIVE:
1. [Specific problem] [ICD-10 if required] — [supporting evidence + date]
   - [linked complication, if applicable]
2. ...

SURVEILLANCE / HISTORICAL-RELEVANT:
- [prior cancer, prior VTE, etc. — why retained]

RESOLVED (retired from active):
- [problem] — [why resolved]

RECONCILIATION ACTIONS (for clinician review):
- MERGED: [entries → single entry]
- UP-SPECIFIED: [vague → specific, with supporting data]
- ADDED (present but unlisted): [problem + evidence]
- RETIRED: [stale entry + reason]
- AMBIGUOUS / NEEDS CONFIRMATION: [item + what's unclear]
```

## Worked Example

**Input:** Existing list reads: "Diabetes; CHF; Heart failure; Hypertension; CKD; UTI; Hyperlipidemia; Anemia." Notes over the last year document: T2DM with A1c 8.1, persistent eGFR 36–39, urine ACR 220; HFrEF EF 35% on GDMT; BP controlled; LDL 70 on statin; Hgb 10.8 with low iron sat and ferritin 40 (no GI source found); a single treated UTI 14 months ago, asymptomatic since. ICD coding specificity required.

**Output:**

```
RECONCILED PROBLEM LIST (prioritized):

ACTIVE:
1. HFrEF, EF 35% (I50.22, chronic systolic HF) — echo on file; on GDMT, NYHA II.
2. Type 2 diabetes mellitus with diabetic CKD (E11.22) — A1c 8.1; links to CKD below.
   - Diabetic nephropathy / albuminuria (urine ACR 220).
3. CKD stage 3b (N18.32, eGFR 36–39) — persistent across visits; attributed to diabetes + HTN.
4. Anemia of CKD vs. iron deficiency (D63.1 / D50.9) — Hgb 10.8, low iron sat, ferritin 40; no GI source identified. Likely mixed; iron studies favor iron-deficient component.
5. Essential hypertension (I10) — currently controlled.
6. Hyperlipidemia (E78.5) — LDL 70 on statin, at goal for this risk profile.

SURVEILLANCE / HISTORICAL-RELEVANT: None.

RESOLVED (retired from active):
- UTI — single episode 14 months ago, treated, asymptomatic since. Retire from active list.

RECONCILIATION ACTIONS (for clinician review):
- MERGED: "CHF" + "Heart failure" → single entry "HFrEF, EF 35%."
- UP-SPECIFIED: "Diabetes" → "T2DM with diabetic CKD"; "CKD" → "CKD stage 3b (eGFR 36–39)"; "Anemia" → "anemia of CKD vs. iron deficiency."
- ADDED (present but unlisted): Diabetic nephropathy/albuminuria (ACR 220) was not on the list but is documented and links the diabetes-CKD relationship.
- RETIRED: UTI (resolved, stale).
- AMBIGUOUS / NEEDS CONFIRMATION: Anemia etiology is mixed (CKD vs. iron deficiency) — confirm whether GI workup was completed before finalizing the code; ferritin 40 with CKD is not reliably "iron replete," so iron-deficiency component is plausible and may warrant treatment.
```

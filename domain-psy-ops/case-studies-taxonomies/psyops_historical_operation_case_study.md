---
title: "Historical Operation Case Study — Studying a Documented Campaign Without Inventing It"
category: psy-ops/case-studies-taxonomies
description: "Build a rigorous case study of a documented, publicly attributed influence operation, anchored to primary sources and named investigations, with an explicit evidence-quality layer distinguishing what was established from what was alleged, reported, or assumed. Every factual specific must be sourced or bracketed, because a fabricated detail in a case study becomes someone else's citation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - case-study
  - history
  - research
  - education
updated: "2026-07-28"
reasoning:
  styles: [analytic, historical, evidential]
  stakes: moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: sourced_case_study
  user_role: [researcher, educator, analyst, student]
  mode: [document, teach, synthesize]
related_prompts:
  - domain-psy-ops/case-studies-taxonomies/psyops_technique_taxonomy_reference.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
  - domain-research-academic/research_source_triangulation.md
---

# Historical Operation Case Study

**Objective:** Build a rigorous case study of a **documented, publicly attributed** influence operation — one with a real evidentiary record: declassified material, a named investigation, platform disclosures, court proceedings, or substantial peer-reviewed research. The structure follows the operation from objective through method to effect, with an **evidence-quality layer** running alongside that distinguishes what was established, what was alleged, what was reported once and repeated since, and what has been assumed into the record.

The anti-fabrication constraint here is stricter than elsewhere in the domain, for a specific reason: **a case study is a citable artifact**. A fabricated date, an invented operation name, a plausible-sounding participant count, or a confidently stated effect becomes someone else's footnote, and this literature already suffers badly from figures that trace back to nothing. Every specific in the output must be sourced or bracketed as `[VERIFY]`. Producing a case study full of brackets is a correct and honest outcome; producing a smooth one from recall is not.

The most valuable and most neglected section is **effect**. Influence operations are routinely described in terms of scale — accounts, posts, reach — and almost never in terms of demonstrated impact on belief or behavior, because that evidence is genuinely hard to obtain and often does not exist. A case study that reports reach as though it were effect misteaches the central analytic lesson of the field.

**When to use:**
- You are teaching with a worked example and need it to be accurate.
- You are researching a documented operation and want a structure that keeps evidence quality visible.
- You are drawing lessons from a historical case for current defensive work.
- You want to check a case study someone else has written.

**When NOT to use:**
- You are assessing live, ongoing activity — use `../influence-operations/psyops_influence_operation_analysis.md`.
- The operation is alleged but not documented. Then there is no case study to write, and saying so is the honest output.
- You want to compare analytic frameworks — use `psyops_technique_taxonomy_reference.md`.

**Audience:** Researchers, educators, students, and analysts drawing on historical cases.

---

## Inputs / Context

1. **The operation.** Which one, and why it qualifies as documented — what the evidentiary basis actually is.
2. **Sources available to you.** Declassified records, investigation reports, platform disclosures, court filings, academic work, journalism. Note which you have read directly.
3. **Your purpose.** Teaching, research, or drawing defensive lessons, which determines depth and emphasis.
4. **Known contested points.** Where researchers, governments, or the accused parties disagree.
5. **Language and archive access.** What you cannot reach, which bounds the study.

---

## Constraints

### Must
- Establish that the operation is **genuinely documented** before writing anything, and name the evidentiary basis.
- Attach a **source and an evidence grade** to every factual claim: established (primary/court/declassified), reported (credible secondary), alleged (asserted by a party), or assumed (in circulation without an identifiable basis).
- Bracket every unverified specific as `[VERIFY]` rather than supplying a plausible value.
- Report **scale and effect separately**, and state plainly where effect is undemonstrated — which is the usual case.
- Present the **contested points** as contested, including the accused party's position.
- Distinguish what was known **at the time** from what was established **afterwards**, since hindsight makes detection look easier than it was.
- Draw **defensive lessons** explicitly, since that is what justifies the study.
- State the **study's limits**: archives, languages, and classifications you could not access.

### Must Not
- Write a case study of an operation that is alleged rather than documented. Say there is no adequate record instead.
- Supply any date, name, figure, account count, budget, or participant number from recall as established. Bracket it.
- Report reach, impressions, or account counts as though they demonstrated effect.
- Present one government's or one platform's account as neutral fact. Note the source's position.
- Describe operational methods in a form that functions as instruction rather than history. Describe what was done and how it was detected; do not produce a manual.
- Fabricate a source, an investigation name, a report title, or a citation.
- Present hindsight detection as evidence that contemporaries were negligent.

---

## Instructions

### Step 1 — Verify the operation is documented
Name the evidentiary basis: declassification, indictment, platform disclosure, parliamentary or congressional investigation, peer-reviewed research. If the basis is journalism repeating a single unsourced claim, stop — this is not a case study subject.

### Step 2 — Build the source inventory with positions
List every source, whether you read it directly, and what interest it has. A government report on an adversary's operation, a platform's disclosure about its own service, and an accused state's denial each have positions worth stating.

### Step 3 — Reconstruct objective and context
What was the operation trying to achieve, and against what backdrop? Grade each element. Stated objectives from primary documents are strong; inferred objectives are inference and must be labeled.

### Step 4 — Document method
Channels, content, infrastructure, personas, and duration — each sourced and graded. Describe at the level of history, not instruction: what was done and how investigators found it, not how to replicate it.

### Step 5 — Report scale, precisely and separately
Accounts, posts, spend, reach — each with a source, and each with the measurement's limits. Note where a figure originates from a single disclosure and has been repeated since without independent verification, which is extremely common.

### Step 6 — Assess effect honestly
What changed in belief, behavior, or outcome, and what evidence establishes it? For most documented operations the honest answer is that effect was never established. Say so; it is the most important lesson in the study.

### Step 7 — Separate contemporaneous knowledge from hindsight
What was visible at the time versus what emerged later. This is what makes the case useful defensively — the question is what could have been noticed, not what is obvious now.

### Step 8 — Draw defensive lessons and state limits
What detection, structure, or resilience would have mattered. Then state what you could not access, and list every `[VERIFY]` remaining.

---

## False-Positive Prevention

1. **Specifics from recall.** Dates, figures, account counts, and operation names stated from memory. They become citations. Bracket everything unverified.
2. **Reach reported as effect.** The field's dominant misteaching. Scale is not impact, and impact is usually unestablished.
3. **Alleged treated as documented.** Building a case study on a contested allegation. If the record is inadequate, that is the finding.
4. **Single-source figures laundered.** A number from one disclosure, repeated across a literature, presented as established. Trace it.
5. **Government or platform account as neutral.** Every source in this field has a position; state it.
6. **Hindsight bias.** Presenting detection as obvious because the operation is now documented, which produces false confidence about current detection.
7. **Case study as manual.** Describing method at operational granularity. History explains what happened and how it was found; it does not need to be replicable.
8. **Fabricated citations.** Inventing a report title, investigation name, or author. The most damaging possible error in a citable artifact.

---

## Output Format

```
# Case study — [operation]

## Documentation basis
[What makes this documented: declassification / indictment / platform disclosure / investigation / research]
**If the basis is inadequate: stop. State that no adequate record exists.**

## Source inventory
| Source | Read directly? | Position / interest | Type |
|---|---|---|---|
| [...] | yes | [state / platform / accused party / independent] | primary / secondary |

## Objective and context
| Element | Claim | Source | Grade |
|---|---|---|---|
| [...] | [...] | [...] | established / reported / alleged / assumed |

## Method
| Element | Description (historical, not instructional) | Source | Grade |
|---|---|---|---|
| Channels | | | |
| Content | | | |
| Infrastructure | | | |
| Duration | | | |

## Scale
| Measure | Figure | Source | Independently verified? | Limits of the measurement |
|---|---|---|---|---|
| Accounts | [n or [VERIFY]] | | no — single disclosure, repeated since | |

## Effect (reported separately from scale)
| Claimed effect | Evidence | Grade |
|---|---|---|
| [...] | [...] | **undemonstrated** |

*If effect was never established, state it plainly — that is the central lesson.*

## Contested points
| Point | Position A | Position B | Status |
|---|---|---|---|

## Known at the time vs established later
| What was visible contemporaneously | What emerged afterwards |
|---|---|

## Defensive lessons
[What detection, structure, or resilience would have mattered — the reason for the study]

## Limits of this study
[Archives, languages, classifications not accessible]

## Outstanding [VERIFY] items
[Every unverified specific, listed — a long list here is honest, not a failure]
```

---

## Verification

- [ ] The operation's documentation basis is established before the study, and inadequate records produce a "no case study" result.
- [ ] Every factual claim carries a source and an evidence grade.
- [ ] Every unverified specific is bracketed `[VERIFY]` rather than filled with a plausible value.
- [ ] Scale and effect are reported separately, and undemonstrated effect is stated plainly.
- [ ] Single-source figures repeated across the literature are identified as such.
- [ ] Every source's position or interest is stated; no government or platform account is presented as neutral.
- [ ] Contemporaneous knowledge is separated from what emerged later, and hindsight is not treated as negligence.
- [ ] Method is described historically, not at a granularity that functions as instruction.
- [ ] No source, report title, investigation name, or citation was fabricated.
- [ ] The study's access limits are stated and all outstanding `[VERIFY]` items are listed.

---
title: "Custody Evaluation Prep and Response"
category: legal/custody
description: "Prepare a client for a court-ordered custody evaluation and critique the evaluator's report: explain the evaluation process and what is assessed, prepare the client for interviews/observation/testing without coaching dishonesty, assemble relevant collateral and records, and analyze the completed report for methodology gaps, bias, unsupported conclusions, and best-interests-factor alignment — producing a preparation guide and a report-critique memo with cross-examination points."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - custody-evaluation
  - report-critique
  - best-interests
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_guardian_ad_litem_report_response.md
  - domain-legal/custody/legal_custody_trial_prep_and_factor_proof_plan.md
  - domain-legal/depositions/legal_expert_deposition_prep.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
---

**Purpose:** Help a client engage effectively with a court-ordered custody evaluation and, when the report arrives, analyze it for methodological soundness and best-interests alignment — producing a preparation guide and a critique memo with cross-examination points. Output supports the attorney's strategy; it does not coach dishonesty and does not substitute for a rebuttal expert where one is warranted.

**When to use:** A custody evaluation (psychological evaluation, §730/CCE/forensic evaluation) has been ordered; preparing the client; or critiquing the evaluator's completed report before settlement or trial.

---

## Your Input

- **Jurisdiction:** [State; the rule authorizing the evaluation and the evaluator's mandate; admissibility standard for the report `[CITE: …]`]
- **Evaluation type & scope:** [Full evaluation, focused issue, psychological testing; the questions the evaluator must answer]
- **Evaluator:** [Name, discipline, appointment basis; deadlines]
- **Client posture:** [Strengths, vulnerabilities, concerns about the process]
- **Best-interests factors:** [The state's factors the report should address `[NEED FACTOR LIST: …]`]
- **Collateral sources:** [Teachers, doctors, therapists, relatives the evaluator may contact]
- **The report (if completed):** [The evaluator's findings, methodology, data sources, and recommendation]
- **Concerns:** [Suspected bias, gaps, reliance on one party, ignored evidence]

---

## Constraints

**Must:**
- Explain the **evaluation process** (interviews, home visit/observation, testing, collateral contacts, records review) and what the evaluator assesses.
- Prepare the client to be **honest, child-focused, and non-disparaging** — coach **presentation and preparation, not deception**; advise against attempting to manipulate testing or coach the child.
- Help assemble **relevant collateral and records** that fairly inform the evaluation.
- When critiquing the report, assess **methodology** (data sources balanced across parties, testing properly administered/interpreted, collateral contacts adequate), **bias/one-sidedness**, **unsupported conclusions**, and **alignment with the state's best-interests factors** `[NEED FACTOR LIST: …]`.
- Identify **cross-examination points** and whether a **rebuttal expert** is warranted (cross-reference expert deposition prep).
- Frame critiques as **methodological challenges**, not attacks on the conclusion's bottom line alone (QA-12).
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority, factors, or facts.

**Must Not:**
- Coach the client to lie, conceal, manipulate testing, or script the child.
- Contact or improperly influence the evaluator or collateral sources outside proper channels.
- Assert the report is biased or wrong without identifying the specific methodological basis.
- Invent the evaluation rule, admissibility standard, or the best-interests factors.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Process explainer.** Walk through each evaluation component and what it assesses.
2. **Client preparation.** Honest, child-focused presentation; what to expect in interviews/observation/testing; what not to do (manipulation, coaching the child, disparagement).
3. **Collateral & records.** Identify appropriate collateral sources and records to provide.
4. **Report critique — methodology.** Assess data balance, testing administration/interpretation, and collateral adequacy.
5. **Report critique — bias & support.** Identify one-sidedness, unsupported leaps, and ignored evidence.
6. **Factor alignment.** Map the report against the state's best-interests factors; flag gaps.
7. **Cross-exam & rebuttal.** List cross-examination points; assess the need for a rebuttal expert.

---

## Output Format

```markdown
# CUSTODY EVALUATION — PREP & RESPONSE — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Evaluator / scope:** {…}

## PART 1 — CLIENT PREPARATION
- Process: {interviews / observation / testing / collateral / records}
- Do: {honest, child-focused, organized, non-disparaging}
- Don't: {manipulate testing, coach the child, disparage the other parent}
- Collateral/records to provide: {…}

## PART 2 — REPORT CRITIQUE (if completed)
### Methodology
| Issue | Finding | Basis |
|---|---|---|
| Data balance across parties | {…} | {…} |
| Testing administration/interpretation | {…} | {…} |
| Collateral adequacy | {…} | {…} |

### Bias / Unsupported Conclusions
- {One-sidedness / unsupported leaps / ignored evidence}

### Best-Interests Factor Alignment
- {Factor-by-factor: addressed / gap} [NEED FACTOR LIST]

### Cross-Examination Points & Rebuttal
- {Cross points}; rebuttal expert warranted? {…}
```

---

## Verification

- [ ] Evaluation process explained component by component.
- [ ] Client preparation is honest and child-focused; no coaching of deception or the child.
- [ ] Appropriate collateral and records identified.
- [ ] Report methodology assessed (data balance, testing, collateral adequacy).
- [ ] Bias/unsupported-conclusion analysis grounded in specifics.
- [ ] Report mapped against the state's best-interests factors.
- [ ] Cross-examination points listed; rebuttal-expert need assessed.
- [ ] No invented rule, standard, or factors; critiques are methodological.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Coaching the client to lie or manipulate testing | Prepare honest, child-focused presentation only |
| Scripting the child for the evaluation | Never; advise against any child coaching |
| Calling the report "biased" with no basis | Identify the specific methodological/data flaw |
| Attacking only the bottom-line recommendation | Challenge methodology, data balance, and unsupported leaps |
| Ignoring whether the report addressed the state's factors | Map the report to each best-interests factor |
| Improperly contacting the evaluator/collaterals | Use proper channels; do not influence sources |
| Assuming a rebuttal expert is unnecessary | Assess whether the flaws warrant a rebuttal expert |
| Inventing the admissibility standard | Use [CITE]/[NEED] placeholders |
| Overlooking testing administration/interpretation issues | Scrutinize how instruments were given and read |
| Treating the report as conclusive | It is evidence to be weighed; identify its limits |

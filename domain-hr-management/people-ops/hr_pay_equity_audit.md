---
title: "Pay Equity Audit — Method, Handoffs, and Remediation, With Determinations Left to Experts"
category: hr-management/people-ops
description: "Run the people-ops side of a pay equity audit: privilege and counsel arranged before any analysis, comparator groups and legitimate pay factors declared in advance, a data-quality pass, raw and adjusted gaps specified for an analyst rather than computed by guesswork, an individual outlier review, and a remediation plan with budget, raise-only adjustments and a recurrence fix — statistical significance and legal conclusions are explicitly flagged for a statistician and counsel; distinct from hr_compensation_banding, whose pattern check only detects the problem and routes it here."
techniques:
  - RT-23
  - RT-05
  - QA-04
  - DD-05
  - CM-09
difficulty: advanced
tags:
  - pay-equity
  - compensation
  - equal-pay
  - audit
  - remediation
  - legally-careful
  - gender-pay-gap
  - unfair-salaries
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/people-ops/hr_compensation_banding.md
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
  - domain-science/statistics/science_statistical_test_selector.md
---

# Pay Equity Audit

**Objective:** Organise a pay equity audit so that it produces corrections rather than a
discoverable memo. Arrange counsel and privilege first. Declare comparator groups and
legitimate pay factors before looking at results. Specify the raw and adjusted analyses
for a qualified analyst, review individual outliers, and fund a remediation plan that
also fixes the mechanism that created the gaps. The prompt does not determine
statistical significance or legal compliance. It marks every point where a statistician
or counsel must decide.

**When to Use:**
- `hr_compensation_banding.md` Step 5 found unexplained gaps that correlate with a
  protected characteristic.
- A pay-transparency or equal-pay reporting obligation now applies.
- Leadership wants to know whether pay is fair before publishing ranges.

**Distinct from:**
- `hr_compensation_banding.md` — designs the structure and runs a quick pattern check.
  When that check fires, it stops and routes to advice. This prompt is the structured
  audit that follows.
- `../../domain-legal/employment-labor/` — the legal analysis. This prompt prepares
  inputs for it and does not replace it.

**Authority boundary (CM-09).**
- **This prompt may:** structure the audit, specify analyses, organise data and draft a
  remediation plan.
- **A statistician decides:** model specification, significance and whether a gap is
  explained.
- **Counsel decides:** privilege, legal exposure, reporting obligations and what may be
  written down.
- **This prompt must not:** state that pay is "compliant", "fair" or "discriminatory".

---

## Inputs

1. **Per-employee data:** base pay, variable pay, level, role family, location, hire date,
   time in level, performance ratings, and the characteristics counsel has approved for
   analysis. Tag each field with its source.
2. **The pay structure**, if one exists (bands, placement rules).
3. **Counsel's instructions** on privilege and who may see what.
4. **Remediation budget envelope**, if known.

---

## Method

1. **Gate: counsel and privilege first.** No analysis runs until counsel has decided how
   the work is commissioned and who sees it. An informal spreadsheet showing a gap can be
   discoverable. If counsel is not engaged, stop here and say so.

2. **Declare comparators and factors in advance (RT-05).** Comparator groups: people doing
   substantially similar work, usually the same level, role family and location. List the
   legitimate factors expected to explain pay (level, location, time in level, documented
   performance), with a reason for each. Record the list with a date before results are
   seen, so a factor cannot be added later because it happens to close a gap.

3. **Treat tainted factors as suspect.** Performance ratings and starting-pay negotiation
   can carry the same bias the audit is looking for. Flag them. Ask the analyst for
   results both with and without them.

4. **Check data quality (RT-23).** Tag every field `[data]`, `[estimate]` or `[guess]`.
   Resolve missing levels, stale job codes, and pay not normalised to full-time. A
   `[guess]` in a pay field stops the analysis for that record.

5. **Specify the analyses for the analyst (DD-05).**
   - **Raw gap:** median and mean pay by group, overall and by level.
   - **Adjusted gap:** a model of pay on the declared factors plus group membership. The
     analyst chooses the model form, reports the estimate with an interval and states
     assumptions. See `../../domain-science/statistics/science_statistical_test_selector.md`
     for choosing the analysis.
   - **Individual review:** everyone whose pay is more than a stated threshold (for
     example, 5%) below the model's prediction, in any group.

6. **Review individual outliers (QA-04).** For each person below threshold, look for a
   documented, job-related reason. "Negotiated less" and "was paid less at a previous
   employer" are not reasons that survive in many jurisdictions. Mark each as explained,
   unexplained or needs counsel.

7. **Plan remediation.** Adjust unexplained cases **upward** to at least the predicted
   pay. Never adjust down to close a gap. Cost it as a total and as a share of payroll.
   Set an effective date. Then fix the mechanism: usually placement-on-hire and
   within-band movement rules, which live in `hr_compensation_banding.md`.

8. **Schedule the re-audit.** Annually, and after any large hiring wave.

---

## Output Format

```markdown
## Pay equity audit — [org], [date] · PRIVILEGED per counsel ([name]) · distribution: [...]

### Scope
Comparator groups: [...] · Factors declared [date]: [factor — reason] · Suspect factors: [...]

### Data quality
| Field | Source | Tag | Issues resolved |
|---|---|---|---|

### Analyses (from analyst [name])
| Measure | Group A | Group B | Gap | Interval / note | Decided by |
|---|---|---|---|---|---|
| Raw median | | | | | |
| Adjusted (with ratings) | | | | | Statistician |
| Adjusted (without ratings) | | | | | Statistician |

### Individual review
| Employee ID | % below predicted | Documented reason | Status |
|---|---|---|---|

### Remediation
Total: [x] = [y%] of payroll · Effective: [date] · Adjust down: never
Mechanism fix: [...] · Re-audit: [date]

### For counsel / statistician
[each open determination, stated as a question]
```

---

## Verification

- [ ] Counsel engaged and privilege arranged before any analysis
- [ ] Comparators and factors were declared and dated before results were seen
- [ ] Suspect factors are flagged and run both with and without
- [ ] Every data field carries a provenance tag, and no `[guess]` remains in pay fields
- [ ] Significance and "explained" judgements are attributed to the statistician
- [ ] Every individual below threshold has a status
- [ ] Remediation is raise-only, costed as a total and as a share of payroll, and dated
- [ ] A mechanism fix is named, not only individual adjustments
- [ ] No sentence concludes the organisation is compliant, fair or discriminatory

## False-Positive Prevention

1. **A small adjusted gap is not proof of equity.** If level assignment itself is
   biased, controlling for level hides the gap. Ask whether groups reach levels at
   similar rates.
2. **A raw gap is not proof of discrimination.** It may reflect level mix. Report both,
   and let the analyst explain the difference.
3. **Factors added after seeing results are not factors.** They are explanations chosen
   to fit.
4. **Do not "remediate" by lowering anyone's pay.** It may be unlawful and it is always
   corrosive.
5. **Aggregate parity can hide individual cases.** Run the individual review even when
   the group gap is small.
6. **Do not compute significance by eye.** The prompt reports what the analyst provides.
   "Looks significant" is not a finding.
7. **Small groups cannot be analysed reliably and can identify people.** Where a
   comparator group is under the analyst's minimum, say so. Do not publish it.

**This is not legal or statistical advice.** Equal-pay law, permitted justifications,
audit privilege and reporting duties vary by jurisdiction.

---

## Example

**Context:** 200 employees, payroll $20.0M `[data]`. Counsel engaged 3 Mar and analyses
commissioned through counsel. Factors declared 5 Mar: level, role family, location, time
in level, and FY rating (suspect). Analysis by gender, as approved by counsel.

| Measure | Women | Men | Gap | Note |
|---|---|---|---|---|
| Raw median base | $86,000 | $100,000 | 14.0% | Level mix differs |
| Adjusted, with ratings | — | — | 3.1% | Analyst: interval 1.2–5.0%; significance for statistician |
| Adjusted, without ratings | — | — | 3.4% | Ratings explain little |

(100,000 − 86,000) / 100,000 = 14.0%.

- **Level access:** 22% of women are at level 4+ versus 35% of men. Flagged to counsel as
  a possible level-assignment issue that the adjusted gap cannot see.
- **Individual review:** 11 people are more than 5% below predicted pay. 2 turn out to be
  data errors: part-time pay not normalised to full-time. After correction both are
  within 1% of predicted. The other 9 are unexplained.
- **Remediation:** raise all 9 to predicted pay. Total $86,000 = 0.43% of payroll,
  effective 1 Apr. Mechanism fix: placement-on-hire rule in `hr_compensation_banding.md`
  (placement by scope, not negotiation). Re-audit Mar next year.
- **For counsel:** is the level-access difference a separate matter? What may be said to
  the nine?

---

## Techniques Used

- **RT-23 Input Provenance Tagging** — every pay field tagged; guesses stop the analysis.
- **RT-05 Evidence-Based Reasoning** — factors declared in advance with reasons; outliers need documented reasons.
- **QA-04 Uncertainty Acknowledgment** — intervals reported, small groups excluded, significance deferred.
- **DD-05 Human Review Flags** — statistician and counsel decisions separated from checkable work.
- **CM-09 Authority Boundary Specification** — what the prompt may do, and what only experts decide.

## Related Prompts

- `hr_compensation_banding.md` — the structure, and the pattern check that routes here
- `../performance-reviews/hr_calibration_facilitator.md` — the ratings treated here as a suspect factor
- `../../domain-science/statistics/science_statistical_test_selector.md` — choosing the analysis
- `../../domain-legal/employment-labor/` — legal analysis of findings

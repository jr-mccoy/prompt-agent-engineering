---
title: "PIP and Termination Risk Review"
category: legal/employment-labor
description: "Pre-termination legal risk review of a performance improvement plan or proposed termination — surfaces protected-class exposure, retaliation timing, comparator analysis, and documentation gaps under the McDonnell Douglas framework, with concrete fixes before separation."
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
  - employment
  - termination
  - pip
  - retaliation
  - mcdonnell-douglas
updated: "2026-05-11"
related_prompts:
  - domain-legal/employment-labor/legal_employment_offer_and_separation_package.md
  - domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md
  - domain-legal/employment-labor/legal_eeoc_position_statement_drafter.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Conduct a pre-action legal risk review of a proposed Performance Improvement Plan (PIP) or termination — identify exposure under Title VII, ADEA, ADA, FMLA, state FEHA-equivalents, and retaliation statutes; analyze the proposed action through the **McDonnell Douglas** burden-shifting frame; surface comparator and documentation gaps; and produce concrete remediation steps the employer can take before the action.

**When to use:** Before delivering a PIP, before a termination decision is finalized, during workforce reductions when individual selections require justification, or when an employee has recently engaged in protected activity (complaint, leave request, accommodation request, agency charge, wage complaint).

---

## Your Input

- **Jurisdiction:** [State + federal — controls protected-category list, comparator requirements, and burden-shifting variations]
- **Federal coverage:** [Title VII (15+) / ADEA (20+) / ADA (15+) / FMLA (50+ within 75 miles) / FLSA / Section 1981 (any employer)]
- **Industry / role:** [Position, level, department, length of service]
- **Posture:** [Considering PIP / PIP in flight / final-warning stage / proposed termination / RIF selection]
- **Employee characteristics (protected classes):** [Race, color, sex, age (if 40+), disability (and accommodations history), religion, national origin, pregnancy/childbirth/lactation, genetic information, citizenship status, sexual orientation, gender identity, marital status, military/veteran status, state-protected categories (e.g., off-duty conduct, political affiliation, marijuana use where protected)]
- **Recent protected activity (any party):** [Internal complaint of discrimination/harassment; participation in another's complaint or investigation; EEOC/state agency charge; ADA accommodation request; FMLA leave / pregnancy leave / state leave; wage complaint / FLSA complaint; whistleblower / SOX / Dodd-Frank report; OSHA complaint; union/§7 NLRA activity; political/petition activity]
- **Performance history:** [Reviews on file, prior PIPs, prior discipline, awards/promotions, last review rating, manager turnover]
- **Decision-maker(s):** [Names, roles, awareness of protected activity, any prior friction with employee]
- **Stated reason for action:** [Specific deficiencies — quantified where possible]
- **Comparators:** [Other employees in similar roles with similar conduct/performance — including those outside the protected class]
- **Documentation available:** [Performance reviews, written warnings, emails, project records, metrics, customer complaints, attendance]
- **Existing agreements:** [Employment agreement with cause definition, severance plan, equity vesting conditions, restrictive covenants, arbitration agreement]

---

## Constraints

**Must:**
- Apply the **McDonnell Douglas** framework explicitly:
  1. Could the employee establish a prima facie case (protected class membership, qualified for position, adverse action, circumstances giving rise to inference of discrimination — e.g., similarly-situated comparator outside the class treated more favorably)?
  2. Can the employer articulate a **legitimate, non-discriminatory reason** with specificity (not "poor performance" — specific failures, metrics, dates)?
  3. Could the employee show **pretext** (shifting reasons, comparator evidence, departures from policy, temporal proximity, decision-maker bias, statistical evidence)?
- Identify each protected class the employee falls into, including state-protected categories often missed (e.g., California's lawful off-duty conduct, NY caregiver status, Colorado lawful product use, Washington's marital status).
- Conduct a **retaliation timing analysis**: list every protected activity and the time interval to the proposed adverse action. Time intervals matter:
  - **≤ 3 months:** courts often find temporal proximity alone sufficient for prima facie inference.
  - **3–6 months:** weaker but supportable with corroborating evidence.
  - **> 6 months:** generally requires additional evidence of causation.
  - Document decision-maker **awareness** of the protected activity at the time of the decision — without awareness, no causation.
- Conduct a **comparator analysis**: identify employees outside the protected class with comparable conduct/performance and document whether they were treated similarly. Comparators must be similarly situated in all material respects (same supervisor, same standards, comparable conduct severity). State the gaps explicitly.
- Conduct a **documentation gap analysis**: are the performance issues contemporaneously documented? Are reviews on file consistent with the stated reason? Are warnings escalating and signed/acknowledged? Are metrics objective and applied consistently?
- For employees with **disability-related performance issues or accommodation history**: confirm an interactive process occurred; confirm reasonable accommodations were considered; confirm performance issues are not attributable to a denied accommodation; assess whether the conduct is a manifestation of the disability requiring further accommodation analysis under the ADA and state FEHA-equivalent.
- For employees on or returning from **FMLA / state leave / pregnancy leave**: apply heightened scrutiny — interference and retaliation claims under FMLA and state equivalents do not require pretext. The action should withstand "would have happened anyway" analysis.
- For **age 40+** employees, especially in RIFs: conduct disparate-impact analysis on the selection pool; confirm reasons are based on factors other than age (RFOA defense under ADEA); document the decisional unit clearly for any OWBPA disclosure if severance with release is contemplated.
- For RIFs: document the **decisional unit** (which employees were considered for selection), the **selection criteria**, the **scoring or ranking**, and the **disparate-impact analysis** by protected class.
- Identify any **cat's-paw** liability risk: a decision-maker without bias may still create liability if influenced by a biased subordinate. Audit the chain of recommendation.
- Identify any **mixed-motive** risk under Title VII (protected characteristic as motivating factor, even if other lawful reasons exist) and ADEA's "but-for" standard.
- For unionized workforces, confirm CBA grievance procedures, just-cause standards, and progressive-discipline requirements.
- Use `[CITE: ...]` placeholders for any statutory or case authority not independently verified.

**Must Not:**
- Treat "performance is bad" as a legitimate non-discriminatory reason without specifics; conclusory reasons collapse under pretext analysis.
- Recommend proceeding when documentation post-dates the protected activity in a way that suggests construction-after-the-fact.
- Ignore comparator gaps; gaps are findings, not annoyances.
- Recommend a PIP designed to fail (unachievable metrics, shifting goalposts) — courts and juries see through this.
- Treat at-will employment as a defense; at-will is the default rule, not a shield against discrimination/retaliation claims.
- Generic "consult counsel" disclaimers in lieu of substantive guardrails.
- Cite cases or statutes not verified — use `[CITE: ...]`.

---

## Instructions

1. **Map protected statuses.** List every protected class the employee falls into across federal, state, and local law.
2. **Build a protected-activity timeline.** For each protected activity, capture date, recipient, decision-maker awareness, and time interval to the proposed action.
3. **Articulate the stated reason with specificity.** Convert "poor performance" into specific, dated, quantified failures with evidence.
4. **Run the McDonnell Douglas analysis** at each step and grade the strength of the employer's position (strong / moderate / weak / unsupportable).
5. **Run the comparator analysis.** For each material element of the stated reason, identify similarly-situated employees and document outcomes. Flag asymmetries.
6. **Run the documentation gap analysis.** For each performance deficiency, identify the contemporaneous documentation; flag gaps and timing of creation.
7. **Run the retaliation proximity analysis.** Combine timeline and awareness; assign risk level.
8. **Special-status analyses.**
   - ADA: accommodation history, interactive process, conduct-as-manifestation.
   - FMLA / leave: interference and retaliation; "would have happened anyway" stress test.
   - Pregnancy: PDA + state pregnancy accommodation laws.
   - Age 40+: RFOA defense; OWBPA implications if release proposed.
   - RIF: decisional unit, criteria, scoring, disparate-impact run.
9. **Cat's-paw audit.** Map the chain of recommendation. Identify any subordinate with potential bias whose input materially influenced the decision.
10. **Identify fixes the employer can take before action.**
    - Strengthen documentation with contemporaneous records (do not backdate).
    - Treat comparators consistently before acting.
    - Extend PIP timeline to defensible duration.
    - Make PIP metrics objective and achievable.
    - Run a higher-level review by an independent decision-maker.
    - Wait out a too-close-in-time proximity window with a paused, documented monitoring period (only if otherwise supported).
    - Offer separation with release calibrated under `legal_employment_offer_and_separation_package.md`.
11. **Score overall risk.** Low / moderate / high / very high — with the dominant risk factors.
12. **Recommend a path.** Proceed as planned / proceed with modifications / pause and remediate / pivot to negotiated separation / abandon.

---

## Output Format

```markdown
# PIP / TERMINATION RISK REVIEW — {Employee} | {Role} | {State}

[Privilege Legend if counsel-directed: Attorney-Client Privileged / Attorney Work Product]

## 1. Executive Summary
- Posture: {PIP / final warning / termination / RIF selection}
- Overall risk: {LOW / MODERATE / HIGH / VERY HIGH}
- Dominant risk factors: {short list}
- Recommendation: {proceed / modify / pause / negotiated separation / abandon}

## 2. Protected Status Map
| Protected class | Federal authority | State/local authority |
|---|---|---|
| {e.g., Age 40+} | ADEA [CITE: 29 U.S.C. § 623] | {state FEHA-equivalent} [CITE: ...] |
| {Disability} | ADA [CITE: 42 U.S.C. § 12112] | {state} [CITE: ...] |
| {...} | | |

## 3. Protected Activity Timeline
| Date | Activity | Recipient | Decision-maker aware? | Days to proposed action |
|---|---|---|---|---|
| {date} | {complaint / leave / accommodation / charge} | {name} | {yes/no/unknown} | {N} |

Retaliation proximity assessment: {≤90 days = high / 90–180 = moderate / >180 = lower}.

## 4. Stated Reason — Specificity Check
| Deficiency | Date / period | Quantified? | Contemporaneous documentation? | Source |
|---|---|---|---|---|
| {specific failure} | {dates} | {metric} | {yes/no — timing of creation} | {document} |

Specificity grade: {strong / moderate / weak / conclusory}.

## 5. McDonnell Douglas Analysis
- Prima facie: {can employee establish — protected class, qualified, adverse action, inference}
- Legitimate non-discriminatory reason: {employer's articulation — specificity grade}
- Pretext risk: {shifting reasons / comparator gaps / policy departures / proximity / bias}

Verdict: {strong / moderate / weak / unsupportable}.

## 6. Comparator Analysis
| Comparator | Protected class status | Conduct/performance | Outcome | Material similarity |
|---|---|---|---|---|
| {name/role} | {in/out of class} | {summary} | {what happened} | {same supervisor / standards / severity} |

Asymmetries identified: {list}.

## 7. Documentation Gap Analysis
- Performance reviews on file: {summary, ratings, signed?}
- Warnings: {dates, signed/acknowledged, escalating?}
- Metrics: {objective? consistently applied?}
- Gaps: {list — and risk of construction-after-the-fact}

## 8. Special-Status Analyses (as applicable)
- ADA: {accommodation history, interactive process, conduct-as-manifestation}
- FMLA / leave: {interference / retaliation analysis}
- Pregnancy: {PDA + state pregnancy accommodation}
- Age 40+: {RFOA; OWBPA implications}
- RIF: {decisional unit, criteria, scoring, disparate-impact}

## 9. Cat's-Paw Audit
Chain of recommendation: {subordinate → manager → decision-maker}
Bias risk in chain: {flagged inputs}

## 10. Recommended Fixes Before Action
- {Specific, dated steps the employer should take pre-action}

## 11. Path Forward
- Recommendation: {proceed / modify / pause / negotiated separation / abandon}
- If negotiated separation: refer to `legal_employment_offer_and_separation_package.md` for calibrated release.
- If proceeding: pre-action checklist.

## 12. Decision-Maker Briefing Notes
{Items the decision-maker must understand before signing off}
```

---

## Verification

- [ ] All federal and state protected classes mapped.
- [ ] Every protected activity captured with date, decision-maker awareness, and proximity to proposed action.
- [ ] Stated reason articulated with specificity (dated, quantified, documented), not as conclusion.
- [ ] McDonnell Douglas analysis run end-to-end with strength grade.
- [ ] Comparator analysis done with material-similarity check.
- [ ] Documentation gap analysis flags any post-protected-activity creation.
- [ ] ADA / FMLA / pregnancy / age / RIF analyses run where applicable.
- [ ] Cat's-paw chain reviewed.
- [ ] Concrete pre-action fixes proposed (not just risk-rated).
- [ ] `[CITE: ...]` placeholders used for unverified authority.
- [ ] Privilege legend applied where counsel-directed.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Performance" as the stated reason without specifics | Convert into dated, quantified, documented failures or pause |
| Documentation created within days of the termination decision | Flag as construction-after-the-fact risk; build a contemporaneous record going forward |
| Comparators outside the class treated more leniently for similar conduct | Treat consistently before acting, or expect a pretext finding |
| Treating at-will as a defense | At-will is the default rule, not a defense to discrimination/retaliation |
| Ignoring decision-maker awareness of protected activity | Without awareness, no causation; with awareness within 90 days, high risk |
| Disability-related conduct treated as performance issue without interactive-process check | Run ADA conduct-vs-manifestation analysis first |
| FMLA returnee terminated within weeks for "performance" | Interference + retaliation risk is acute; document a "would have happened anyway" record |
| RIF without disparate-impact analysis on the decisional unit | Run the analysis; document RFOA defense for ADEA |
| Cat's-paw input from a biased subordinate not surfaced | Audit the chain of recommendation; insulate decision |
| PIP with unachievable metrics or shifting goalposts | Set objective, achievable metrics with reasonable duration; preserves defense |
| Fabricated cites | Use `[CITE: ...]` placeholders |
| Generic "consult counsel" closing | Replace with specific pre-action steps |

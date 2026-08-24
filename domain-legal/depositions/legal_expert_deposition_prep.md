---
title: "Expert Witness Deposition Preparation (Examining the Other Side's Expert)"
category: legal/depositions
description: "Build a Daubert-targeted deposition plan for the opposing expert — qualifications, methodology, application to facts, prior testimony and writings, and reliable bases — usable to cross-examine and to ground a Daubert / Rule 702 (or state analog) motion to exclude."
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
  - depositions
  - expert-witness
  - daubert
  - rule-702
  - cross-examination
updated: "2026-05-08"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_witness.md
  - domain-legal/depositions/legal_deposition_witness_prep_script.md
  - domain-legal/litigation/legal_motion_for_summary_judgment.md
---

**Purpose:** Develop the record at the opposing expert's deposition that supports either (a) exclusion under Daubert / Rule 702 (or controlling state analog) or (b) effective cross-examination at trial. Output is a deposition plan plus a Daubert-grounded question bank.

**When to use:** After receiving the expert's report and reliance materials; before the close of expert discovery; in advance of a motion to exclude.

---

## Your Input

- **Expert:** [Name, field, current affiliations]
- **Report and reliance materials:** [Provided to deposition under controlling rule]
- **Opinions stated in the report:** [Each opinion paraphrased / quoted]
- **Methodology described in the report:** [As stated]
- **Prior testimony, writings, and public statements:** [Where available]
- **Our retained expert's posture:** [Where the experts agree, disagree, and where opposing expert has stretched]
- **Controlling reliability standard:** [Daubert / Frye / state-codified Rule 702 — supply controlling articulation]
- **Theories the deposition serves:** [Exclusion / cross-only / both; targeted opinions]
- **Time budget:** [Hours]

---

## Constraints

**Must:**
- Open with **qualifications** — degrees, training, certifications, professional discipline, peer-review record, publications, prior testimony — to assess Rule 702(a) qualification.
- Cover **methodology** systematically: name the methodology, ask whether it is generally accepted in the field, ask for the standard text describing it, ask whether the expert applied each step.
- Examine **application to facts**: was the methodology reliably applied to the facts of this case? Identify any deviations.
- Examine **reliable bases**: what facts and data did the expert rely on; were they sufficient under the field's standards; did the expert independently verify or accept assumptions; whose assumptions were they.
- Examine **prior testimony and writings** for inconsistency. Pin material conflicts.
- Examine **alternative explanations** — did the expert consider and rule out competing explanations.
- Examine **fee, hours, and case history** — for bias and Rule 26(a)(2)(B)(vi) compliance.
- Capture **opinions outside the report** — the expert is generally limited to opinions in the report; surface anything new or expanded.

**Must Not:**
- Argue with the expert. The transcript reads worst when the lawyer fights the expert.
- Skip foundation. Foundation questions on methodology and bases are the meat of a Daubert deposition.
- Ask broad "is your methodology reliable" questions. Specific methodology questions get useful answers; broad ones get rehearsed answers.
- Skip the bias/fee module out of politeness.
- Confuse Daubert and Frye standards. Use the standard controlling in the venue.
- Miss the chance to lock in the **specific opinions** the expert holds; without lock-in, the expert can re-frame at trial.

---

## Instructions

1. **Pre-deposition prep.**
   - Build a topic-tied summary of every opinion in the report.
   - Build the bias dossier (prior cases, prior fees, side ratio).
   - Build the methodology dossier (standard texts; known critiques; the expert's prior writings).
   - Identify the two or three strongest grounds for exclusion (qualification gap; methodological flaw; application flaw; insufficient basis).
2. **Open: identification, ground rules, and acknowledgments.**
3. **Qualifications module.** Education; training; certifications; experience in the specific sub-area at issue; teaching; peer-reviewed publications.
4. **Prior testimony module.** Prior reports and depositions in the past four (or more) years (Rule 26(a)(2)(B)(v)); side ratio (plaintiff vs. defense / movant vs. respondent); subject-matter overlap; outcomes.
5. **Engagement and fee module.** Retention date; hourly rate; total fees in this matter; total fees with retaining counsel firm over time.
6. **Reliance and assumptions module.** Documents reviewed; not reviewed; assumptions; whose assumptions; verification.
7. **Methodology module.**
   - Name the methodology.
   - Standard reference texts.
   - Steps in the methodology — ask each.
   - Application: was each step performed; if not, why.
   - Alternative methodologies considered and rejected.
   - Generally-accepted-in-the-field articulation.
   - Peer-reviewed support for the methodology.
   - Known limitations and error rates.
8. **Application to facts module.** For each opinion, walk the steps the expert took. Surface any departure from the methodology as described.
9. **Alternative explanations module.** Did the expert consider and rule out competing explanations; if so, on what basis.
10. **Lock-in module.** For each opinion, lock the precise statement of the opinion and the supporting bases.
11. **Catch-all.** Opinions outside the report; communications with retaining counsel about opinions; supplementation expected.
12. **Close.**

---

## Output Format

```markdown
# EXPERT DEPOSITION PLAN — {Expert} — {Matter}
**Privileged & Confidential — Attorney Work Product**

## Pre-Deposition Brief
- Two or three strongest exclusion theories: {...}
- Cross themes for trial if not excluded: {...}
- Bias dossier highlights: {...}
- Methodology dossier highlights: {...}

## I. Identification, Ground Rules, Acknowledgments
- Q: You understand you are testifying as a retained expert under Rule 26(a)(2)(B)? A.
- Q: Your report dated {date} reflects your opinions in this matter? A.
- Q: Are there any opinions you intend to offer at trial that are not in your report? A.

## II. Qualifications
- Degrees, dates, institutions; relevant coursework.
- Training and certifications; date and renewal.
- Years of experience in the specific sub-area at issue.
- Teaching, supervisory, and clinical/practical roles.
- Publications: peer-reviewed vs. industry; relevance to opinions in this case.
- Memberships and committees.
- Disciplinary history (if any).

## III. Prior Testimony
- Cases under Rule 26(a)(2)(B)(v) (last four years; longer if state):
  - {Caption — court — date — side — subject — opinions offered}
- Side ratio: {plaintiff/defense / movant/respondent}.
- Disqualification or exclusion in any prior case: when and why.

## IV. Engagement and Fee
- Retention date; how engaged; prior work with retaining counsel firm.
- Hourly rate; rate for deposition; rate for trial.
- Hours and fees in this matter to date.
- Cumulative fees with retaining counsel firm.

## V. Reliance and Assumptions
- Documents and data reviewed (per appendix).
- Documents not reviewed that the expert is aware of.
- Assumptions made; source of each assumption (counsel-supplied vs. independently determined).
- Verification of factual predicates.

## VI. Methodology
- Q: What is the name of the methodology you used to reach Opinion 1? A.
- Q: What standard text or peer-reviewed source describes that methodology? A.
- Q: Is the methodology generally accepted in the field of {field}? A.
- Q: What are the steps in the methodology? Walk through.
- Q: Did you perform each step in this matter? A.
- Q: For any step not performed, why?
- Q: What alternative methodologies were available?
- Q: Why did you select the methodology you used?
- Q: What are the known limitations and error rates of the methodology?
- Q: Has the methodology been peer-reviewed? Where?

## VII. Application to Facts
- For Opinion 1:
  - Walk the data inputs.
  - Walk the methodology application step by step.
  - Identify any deviation from the methodology.
  - Identify any data the expert did not have or chose not to use.

(Repeat for each opinion.)

## VIII. Alternative Explanations
- For each conclusion: what alternative explanations did you consider?
- How did you rule out each?
- What evidence would change your opinion?

## IX. Lock-Ins
- Opinion 1, stated precisely: "{...}"
- Opinion 1's bases: {...}
- Opinion 2, stated precisely: "{...}"
- (etc.)

## X. Catch-All
- Opinions outside the report? A.
- Supplementation expected? A.
- Communications with retaining counsel relevant to opinions {only as the controlling rule permits}? A.
- Documents you have brought today? A.

## XI. Close
- Q: Apart from the opinions you have stated and the bases you have identified, do you intend to offer any other opinion at trial in this matter? A.
- Q: If you supplement before trial, will you produce a supplemental report? A.
```

## Daubert Question Bank — Targeted Modules

(Selected modules; deploy based on the strongest ground for exclusion.)

### Qualification gap — Rule 702(a)
- Q: Have you ever performed {specific task at issue} in a real-world setting? Yes / No / How often?
- Q: Have you ever been published, peer-reviewed, on {specific sub-area}?
- Q: Have you ever testified about {sub-area} before? Cases?

### Methodological reliability — Rule 702(c)
- Q: Is your methodology reproducible by an independent expert with the same data?
- Q: What is the error rate?
- Q: Has the methodology been validated in a peer-reviewed setting?
- Q: Are there published critiques of the methodology? Did you address them?

### Reliable application — Rule 702(d)
- Q: Show me where in your work papers each step of the methodology appears.
- Q: For data inputs you assumed, what is the source?
- Q: Did you independently verify {specific factual predicate}?

### Sufficient basis
- Q: How many {samples / records / documents} did you review?
- Q: What is the field's standard for sufficient {sample size / record review}?
- Q: Is your sample representative of the population?

### Alternative explanations
- Q: Could {alternative cause} also explain {observation}?
- Q: How did you rule that out?
- Q: What evidence would change your opinion?

---

## Verification

- [ ] Qualifications module covers degrees, training, certifications, experience, publications, prior testimony, and discipline.
- [ ] Methodology module asks for name, standard texts, steps, application, alternatives, peer review, error rates.
- [ ] Application module walks each opinion through its data, steps, and any deviations.
- [ ] Alternative-explanations module asks what was considered and ruled out.
- [ ] Lock-in module captures each opinion precisely and its bases.
- [ ] Bias / fee module included.
- [ ] Catch-all addresses opinions outside the report and expected supplementation.
- [ ] Daubert question bank deployed for the strongest exclusion grounds.
- [ ] Controlling reliability standard correctly identified.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Arguing with the expert | The transcript reads worst when the lawyer fights; ask, do not argue |
| Asking broad "is your methodology reliable" questions | Specific questions on steps, error rates, peer review yield useful answers |
| Skipping foundational methodology questions to "get to the good stuff" | The foundation is the good stuff for Daubert |
| Confusing Daubert and Frye | Use the standard controlling in the venue |
| Missing the lock-in for each opinion | Without lock-in, the expert can re-frame at trial |
| Skipping prior-testimony and side-ratio modules | Bias evidence is admissible and changes credibility weight |
| Not asking about opinions outside the report | Limits at trial depend on a clean record now |
| Failing to capture data the expert did not review | The "did not review" list is often the strongest exclusion lever |
| Treating peer review as binary | Ask where, when, by whom, and whether critiques were addressed |

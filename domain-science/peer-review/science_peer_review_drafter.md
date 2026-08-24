---
title: "Peer Review Drafter"
category: science/peer-review
description: "Draft a structured, constructive peer review with a comprehension summary, significance assessment, triaged major and minor concerns each tied to evidence, an Open-Science check, and a calibrated recommendation."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - peer-review
  - manuscript-evaluation
  - cope
  - reporting-standards
  - open-science
  - reproducibility
  - constructive-critique
  - editorial-process
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_self_check.md
  - domain-science/peer-review/science_editorial_decision_drafter.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_threats_to_validity_walkthrough.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Peer Review Drafter

**Objective:** Produce a complete, structured peer review of a scientific manuscript that demonstrates genuine comprehension of the work, separates threats to the validity of the conclusions (major concerns) from improvements of degree (minor concerns), grounds every criticism in a specific manuscript location and a stated reason, checks reporting-standard and Open-Science adherence, and ends with a calibrated recommendation. The review must be constructive and actionable, never ad hominem.

**When to use:** You have been invited to review a manuscript (or have agreed to peer review one) and need to write the review itself. Use after confirming you have no disqualifying conflict of interest and can keep the manuscript confidential.

**Required inputs:**
- **Discipline.** The field and subfield (e.g., cognitive neuroscience, organic chemistry, epidemiology, computational climate modeling).
- **Study type.** Observational / experimental / randomized controlled trial / computational-simulation / theoretical / systematic review / meta-analysis / qualitative / mixed-methods.
- **Manuscript text or detailed content.** The abstract plus methods, results, and key claims (or the full manuscript). Reviews are drafted only from supplied content.

**Optional inputs:**
- The journal's specific review criteria, scope statement, or recommendation categories `[user-supplied]`.
- The relevant EQUATOR reporting checklist if the venue mandates one (CONSORT, STROBE, PRISMA, ARRIVE, etc.).
- Stated data/code availability, preregistration link, or supplementary materials.
- The authors' cover letter or stated novelty claims (to assess, not to echo).

**Constraints — Must:**
- Follow the COPE Ethical Guidelines for Peer Reviewers: be objective and constructive, declare conflicts, maintain confidentiality, and base every comment on evidence rather than personal preference or reputation.
- Open with a summary that demonstrates comprehension of the paper's aims, methods, and findings before raising any critique.
- Anchor each concern to a specific manuscript location (section, page/line, figure, table, or equation) and a stated reason.
- Triage concerns into **major** (threats to the validity of the conclusions) vs **minor** (clarity, presentation, references), and label whether each claim being critiqued is confirmatory/preregistered or exploratory.
- Check adherence to the relevant EQUATOR reporting checklist for the study type and the TOP-guideline Open-Science dimensions (data availability, code/analysis-script availability, materials, preregistration adherence).
- Keep comments-to-authors and confidential comments-to-editor in separate, clearly labeled sections.
- Provide a calibrated recommendation drawn from standard categories: accept / minor revision / major revision / reject.

**Constraints — Must Not:**
- Do not invent citations, prior-literature claims, data, or facts about the manuscript not supplied by the user. If a criticism needs a reference the authors "missed," mark it `[user-supplied]` or phrase it as a question to the authors ("Have the authors considered…?").
- Do not use ad hominem, dismissive, or hostile language; do not comment on the authors rather than the work.
- Do not use promotional language in the drafted review — ban "novel," "groundbreaking," "first-ever," and "gold standard."
- Do not demand a fundamentally different study (scope creep); confine requests to what would strengthen the validity of *this* manuscript's stated claims.
- Do not breach confidentiality (no sharing, no reuse of unpublished ideas/data) or review where an undisclosed conflict of interest exists.

**Instructions:**

1. **Confirm reviewability.** State the discipline and study type. Flag any conflict-of-interest or competence-mismatch concern that should be raised with the editor before proceeding (COPE confidentiality/COI norms).
2. **Write the comprehension summary.** In 4–8 sentences, restate the manuscript's research question, design, principal methods, and headline findings in your own words. This shows the editor and authors the review is informed; raise no critique here.
3. **Assess significance and scope fit.** Describe what the work would contribute *if* its claims hold, and whether it fits the venue's stated scope `[user-supplied if criteria provided]`. Calibrate language; do not inflate.
4. **Identify major concerns.** Surface threats to the validity of the conclusions: design flaws, missing/inadequate controls, confounding, inappropriate or under-powered analysis, over-claiming beyond the data, causal language on observational data, failure to distinguish confirmatory from exploratory results, and reproducibility gaps. For each, give the location, the reason it threatens validity, and a concrete, actionable remedy. Mark genuinely fatal flaws distinctly from serious-but-addressable ones.
5. **Identify minor concerns.** List clarity, figure/table, statistics-reporting, and reference issues that improve the paper by degree. Each still gets a location and a reason.
6. **Run the reporting-standard check.** Map the manuscript against the relevant EQUATOR checklist for the study type; note any required item that appears missing or under-reported, phrased as a verifiable observation or a query.
7. **Run the Open-Science check.** Per TOP guidelines, note whether data, analysis code/scripts, and materials are available and whether any preregistration is adhered to (deviations disclosed). Phrase absences as questions where you cannot verify from the supplied text.
8. **Write confidential comments to the editor.** Summarize your overall judgment, the one or two decisive issues, your confidence, and your recommendation rationale — content you would not put directly to authors.
9. **State the recommendation.** Choose accept / minor revision / major revision / reject, and justify it from the triaged concerns rather than overall impression.

**Output format (locked):**

```
## Review Summary (comprehension)
[4–8 sentences restating aim, design, methods, findings in the reviewer's words]

## Significance and Scope Assessment
[What the work contributes if valid; fit to venue if criteria supplied]

## Major Concerns (threats to validity)
1. [Location: §/page/line/figure] — [Concern]
   - Claim type: [confirmatory/preregistered | exploratory]
   - Why it threatens the conclusions: [reason]
   - Fatal flaw vs addressable: [which, and why]
   - Suggested remedy: [actionable]
2. ...

## Minor Concerns (improvements of degree)
1. [Location] — [Issue] — [Reason] — [Suggested fix]
2. ...

## Reporting-Standard Check
- Checklist applied: [CONSORT/STROBE/PRISMA/ARRIVE/other or [user-supplied]]
- Items missing/under-reported: [list with locations, or "none identified from supplied text"]

## Open-Science Check (TOP)
- Data availability: [stated/observed | unverifiable — query to authors]
- Code/analysis-script availability: [...]
- Materials availability: [...]
- Preregistration adherence: [adhered | deviations disclosed | not applicable | unverifiable]

## Confidential Comments to the Editor
[Overall judgment, decisive issues, reviewer confidence, recommendation rationale]

## Recommendation
[Accept | Minor revision | Major revision | Reject] — [justification from concerns above]
```

**Reporting-standard alignment:** COPE Ethical Guidelines for Peer Reviewers; ICMJE recommendations on the review of manuscripts; the EQUATOR reporting checklist matching the study type (CONSORT for RCTs, STROBE for observational, PRISMA for systematic reviews/meta-analyses, ARRIVE for animal research); TOP guidelines for the Open-Science dimensions.

**Verification checklist (before delivering):**
- [ ] The summary demonstrates comprehension and contains no critique.
- [ ] Every concern cites a specific manuscript location and a stated reason.
- [ ] Major vs minor concerns are correctly triaged (validity threats vs degree).
- [ ] Fatal flaws are distinguished from addressable issues.
- [ ] Confirmatory vs exploratory status is labeled for each critiqued claim.
- [ ] No invented citations, data, or manuscript facts; gaps are `[user-supplied]` or author queries.
- [ ] Reporting-standard and Open-Science checks are both present.
- [ ] Comments-to-authors and confidential comments-to-editor are separate; no banned promotional terms; no ad hominem.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Preference dressed as flaw | A stylistic or "I'd have done it differently" comment placed under Major Concerns | Require a stated validity threat and location before any item is "major"; otherwise demote to minor or drop |
| Invented missing literature | Listing specific papers the authors "failed to cite" from memory | Mark `[user-supplied]` or phrase as "Have the authors considered…?"; never assert a citation |
| Scope creep | Demanding a new experiment that would constitute a different paper | Limit remedies to strengthening the manuscript's own stated claims |
| Over-claiming critique while over-claiming the review | Confident verdicts unsupported by the supplied text | Tie confidence to supplied evidence; mark unverifiable points as queries |
| Halo/prestige bias | Softening major flaws because the work or authors seem impressive | Triage on evidence and validity only; ignore reputation cues |

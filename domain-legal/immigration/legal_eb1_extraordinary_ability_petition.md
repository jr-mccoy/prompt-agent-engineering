---
title: "EB-1A Extraordinary Ability Petition Builder"
category: legal/immigration
description: "Attorney-facing EB-1A petition analysis and brief outline — evidence mapped to each regulatory criterion (or a one-time major internationally recognized award), per-exhibit quality scoring, comparable-evidence analysis, and a separate final-merits argument for sustained acclaim and top-of-field standing — with every regulatory and policy-manual reference marked for verification and no inflated or invented credentials."
techniques:
  - DS-01
  - RT-05
  - QA-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - immigration
  - eb-1a
  - extraordinary-ability
  - i-140
  - evidence-mapping
  - final-merits
  - green-card
updated: "2026-09-24"
reasoning:
  styles: [evidential, evaluative, adversarial]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [matrix, memo]
  user_role: [lawyer]
  mode: [assess, document]
related_prompts:
  - domain-legal/immigration/legal_h1b_rfe_response.md
  - domain-legal/immigration/legal_perm_audit_response.md
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/ip/legal_patent_landscape_scan.md
---

# EB-1A Extraordinary Ability Petition Builder

**Objective:** Decide with counsel whether an EB-1A petition is ready to file and, if so, build its spine. Step one maps the evidence to each regulatory criterion and scores every exhibit for how well it proves the criterion *as the regulation defines it* — not as the beneficiary describes it. Step two, which is separate and must not be skipped, argues the final merits: that the evidence as a whole shows sustained national or international acclaim and that the beneficiary is among the small percentage at the very top of the field. The output is a criteria matrix, an evidence-gap list, a readiness rating, and a brief outline.

> **Scope guard — attorney-facing only.** For immigration counsel evaluating and preparing a petition. It does not tell an individual whether they qualify. If the person running it is the prospective beneficiary without counsel, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

**When to use:**
- Evaluating a prospective EB-1A client's evidence before engagement or filing.
- Drafting the petition brief and exhibit index.
- Responding to an RFE or NOID on an EB-1A petition (use the matrix to target the officer's criterion-level and final-merits findings).

**Distinct from:**
- `legal_h1b_rfe_response.md` (this folder) — nonimmigrant specialty occupation; different standard and evidence.
- `legal_perm_audit_response.md` (this folder) — labor-certification route; EB-1A needs no labor certification or job offer.
- `domain-legal/ip/legal_patent_landscape_scan.md` — freedom-to-operate; patents here are evidence of original contributions only if their significance is shown.

**Audience:** Immigration attorneys and supervised legal staff.

---

## Your Input

- **Field:** [Precise field of endeavor — the definition affects every comparison]
- **Beneficiary evidence:** [Awards, memberships, media coverage, judging, original contributions, authorship, exhibitions, leading/critical roles, high salary, commercial success — with documents]
- **Citation and impact data:** [Citation counts, h-index, downloads, adoption, licensing, revenue — with source and date]
- **Recommendation letters:** [Drafts or list of recommenders with independence (independent vs. collaborator)]
- **Comparable field data:** [Salary surveys, award prestige information, journal rankings, membership criteria]
- **Continuing work in the field:** [Plans and evidence]
- **Current rules you have verified:** [Regulatory criteria text and current policy manual guidance — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- Map evidence to the **regulatory criteria** `[VERIFY: 8 CFR 204.5(h)(3)(i)–(x)]` or to a **one-time major, internationally recognized award** `[VERIFY: 8 CFR 204.5(h)(3)]`; at least the required number of criteria must be met `[VERIFY: number]`.
- For each criterion, apply its **defined terms** (e.g., memberships requiring outstanding achievements judged by recognized experts; published material *about* the beneficiary in major media; original contributions *of major significance*; salary *high relative to others in the field*).
- Score each exhibit **Strong / Adequate / Weak / Not probative** with the reason.
- Consider **comparable evidence** only where a criterion does not readily apply to the occupation, and explain why `[VERIFY: 8 CFR 204.5(h)(4)]`.
- Run the **final-merits** analysis separately, weighing the totality: sustained acclaim, top-of-field standing, and continuing work in the area `[VERIFY: current USCIS Policy Manual guidance on the two-step analysis]`.
- Distinguish **independent** from **collaborator** recommenders and weight accordingly.
- Deliver a **readiness rating** (File now / File after gaps / Not ready) with the specific gaps.

### Must Not
- Inflate evidence (a conference speaking slot is not an award; a paid membership is not a qualifying association; a citation count is not "major significance" without context).
- Invent citation counts, rankings, award prestige, salary percentiles, or media circulation — use supplied data or `[NEED: …]`.
- Draft recommendation letters that attribute claims the recommender has not made or cannot support; provide question prompts for recommenders instead.
- Treat meeting the criteria count as approval; the final-merits step is independent.
- Cite AAO decisions or cases not supplied.

---

## Instructions

1. **Define the field** narrowly enough to compare but not so narrowly that "top of the field" becomes trivial.
2. **Criteria matrix.** For each criterion: evidence, defined-term test, exhibit scores, criterion verdict (Met / Arguable / Not met).
3. **Comparable evidence** where justified.
4. **Recommender map.** Independence, standing, what each can credibly attest.
5. **Final-merits argument.** Totality: trajectory over time (sustained), comparison to peers (top of field), and continuing work.
6. **Gap list.** What evidence would move an Arguable criterion to Met or strengthen final merits, and whether it exists.
7. **Readiness rating.**
8. **Brief outline** with headings for each criterion claimed and the final-merits section.

---

## Output Format

```markdown
# EB-1A Petition Analysis — {Beneficiary} — Field: {…}
**Prepared:** {date}  |  **Attorney Work Product**

## 1. Field Definition
## 2. Criteria Matrix
| Criterion [VERIFY cite] | Evidence (exhibit) | Defined-term test | Exhibit score | Verdict |
## 3. Comparable Evidence (if any)
## 4. Recommenders
| Name | Independent / collaborator | Standing | Can credibly attest to |
## 5. Final-Merits Analysis
- Sustained acclaim: {…}
- Top of field: {…}
- Continuing work: {…}
## 6. Gaps and How to Close Them
## 7. Readiness Rating: {File now / File after gaps / Not ready}
## 8. Brief Outline
```

---

## Worked Example

**Input (abridged):** Machine-learning researcher at a large tech company. Evidence: 14 peer-reviewed papers (1,900 total citations, one paper with 1,100); reviewer for three major conferences; one best-paper award at a workshop; quoted in two trade-publication articles about a product launch; salary at the employer's senior band; two patents granted; five recommendation letters (three co-authors, two independent).

**Output (excerpt):**

> | Criterion | Evidence | Test | Score | Verdict |
> |---|---|---|---|---|
> | Judging | Conference reviewer invitations | Participation as a judge of others' work | Adequate (add review counts and invitation letters) | Met |
> | Authorship | 14 papers in peer-reviewed venues | Scholarly articles in professional publications | Strong | Met |
> | Original contributions of major significance | 1,100-citation paper; patents | Significance to the field, not just novelty | Adequate — citations alone don't show significance; need evidence of adoption (open-source use, other groups building on it) `[NEED]` | Arguable |
> | Published material about the beneficiary | Two trade articles quoting the beneficiary about a product | Must be *about* the beneficiary and their work, in major media | Weak | Not met |
> | Awards | Workshop best-paper award | Nationally or internationally recognized prize for excellence | Weak — workshop-level; prestige data needed | Arguable |
>
> **Final merits:** Citation record is concentrated in one paper (sustained acclaim question); two of five letters are independent. **Readiness: File after gaps** — obtain adoption evidence for the major-contribution criterion and at least two more independent recommenders who can explain the work's influence from outside the beneficiary's network.

---

## Verification

- [ ] Jurisdiction lock: USCIS I-140 adjudication; criteria text and policy guidance marked `[VERIFY]` unless supplied.
- [ ] Each criterion tested against its defined terms, not its label.
- [ ] Every exhibit scored with a reason.
- [ ] Comparable evidence used only with a stated justification.
- [ ] Final-merits analysis present and separate from the criteria count.
- [ ] Recommenders classified by independence.
- [ ] No invented metrics, prestige claims, or letter content.
- [ ] Readiness rating with specific gaps.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Counting criteria and stopping | Run the final-merits totality analysis every time |
| Treating citation counts as major significance | Show how the field relied on or adopted the work |
| Counting trade quotes about a product as media about the beneficiary | Material must be about the beneficiary's work in qualifying media |
| Treating every membership or award as qualifying | Apply selectivity and recognition tests |
| Relying on collaborator letters | Weight independent recommenders; collaborators corroborate, not establish acclaim |
| Drafting letters with claims the recommender cannot support | Provide question prompts; the recommender supplies the substance |
| Defining the field so narrowly the beneficiary is trivially "top" | Use a field definition an adjudicator will accept |

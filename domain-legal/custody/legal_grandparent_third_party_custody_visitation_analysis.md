---
title: "Grandparent / Third-Party Custody and Visitation Analysis"
category: legal/custody
description: "Analyze a non-parent's standing and substantive claim for custody or visitation under the controlling state's third-party statute and the constitutional Troxel framework: assess statutory standing (grandparent, de facto/psychological parent, relative caregiver), apply the heightened standard that respects a fit parent's presumption and decision-making, address required findings (harm, parental unfitness, or the state's threshold), and produce a position memo with the proof required and the likelihood of success."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - grandparent-visitation
  - third-party-custody
  - troxel
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_paternity_parentage_establishment_and_custody.md
  - domain-legal/custody/legal_custody_petition_or_motion_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Evaluate whether a non-parent (grandparent, relative caregiver, de facto/psychological parent) has standing and a viable claim for custody or visitation, under the state's third-party statute and the constitutional limits of *Troxel v. Granville*, and frame the proof required. Output is a standing-and-merits position memo, not a guaranteed result; third-party rights are constitutionally constrained and highly state-specific.

**When to use:** A grandparent or other non-parent seeks visitation or custody; a parent opposes a non-parent's petition; assessing standing before filing; advising a relative caregiver.

---

## Your Input

- **Jurisdiction:** [State; the third-party custody/visitation statute and its standing categories and standard `[CITE: …]`]
- **Petitioner relationship:** [Grandparent, relative, de facto/psychological parent, stepparent, caregiver]
- **Parent status:** [Whether the parents are fit, living, married/divorced, deceased; intact family or not]
- **Existing relationship:** [The non-parent's caregiving history and bond with the child]
- **Threshold facts:** [Facts relevant to the state's threshold — prior caregiving, parental death/incapacity, harm to the child if denied]
- **Parental position:** [Whether a fit parent objects, and the parent's stated reasons]
- **Triggering event:** [Death of a parent, divorce, parent's denial of contact]
- **Child(ren):** [Ages, current placement, ties to the non-parent]

---

## Constraints

**Must:**
- Address **standing first** under the state's statute — many states limit standing to specific categories and triggering circumstances (e.g., a parent's death, family no longer intact); no standing ends the inquiry `[CITE: …]`.
- Apply the **constitutional framework of *Troxel***: a **fit parent's decisions about third-party contact get special weight (a presumption)**; the state cannot override them on a mere best-interests preference `[CITE: …]`.
- Apply the state's **substantive standard** — often requiring a showing beyond best interests, such as **harm/detriment to the child** if contact/custody is denied, or **parental unfitness** for third-party custody `[CITE: …]`.
- For **de facto/psychological parent** claims, apply the state's multi-factor test for that status.
- Distinguish **visitation** (lesser intrusion) from **custody** (greater intrusion, higher bar) and the differing standards.
- Provide **standing strength**, **merits strength**, and **overall confidence**; frame as a position (QA-12).
- Confirm **UCCJEA jurisdiction** as for any custody matter.
- Use placeholders `[CITE: ...]`, `[NEED STANDARD: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Apply a plain best-interests test as if the non-parent were on equal footing with a fit parent (this violates *Troxel*).
- Assume grandparents have a general right to visitation — many statutes are narrow and several have been narrowed or struck post-*Troxel*.
- Skip the standing analysis.
- Invent the state's standing categories or substantive standard.
- Treat visitation and custody claims as governed by the same standard.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Standing.** Apply the state's standing categories and triggering circumstances; determine whether the petitioner qualifies `[CITE: …]`.
2. **Constitutional overlay.** Apply *Troxel*'s fit-parent presumption and special weight.
3. **Substantive standard.** Identify and apply the state's standard (harm/detriment, unfitness, or threshold) for visitation vs. custody `[CITE: …]`.
4. **De facto parent (if applicable).** Apply the state's psychological/de facto parent test.
5. **Proof required.** List the evidence needed to meet standing and the substantive standard.
6. **Jurisdiction.** Confirm UCCJEA jurisdiction.
7. **Position & confidence.** Assess standing strength, merits strength, and overall likelihood.

---

## Output Format

```markdown
# THIRD-PARTY CUSTODY/VISITATION ANALYSIS — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Petitioner:** {relationship}   **Relief:** {visitation / custody}

## 1. Standing
- Statutory category: {…}; triggering circumstance: {…}; standing: {yes/no} [CITE]

## 2. Constitutional Overlay (Troxel)
- Fit-parent presumption / special weight: {application} [CITE]

## 3. Substantive Standard
- State standard: {harm-detriment / unfitness / threshold}; visitation vs. custody bar: {…} [CITE]

## 4. De Facto / Psychological Parent (if applicable)
- Multi-factor test application: {…}

## 5. Proof Required
- Standing proof: {…}; substantive proof: {…}

## 6. Jurisdiction (UCCJEA)
- {Basis}

## 7. Position & Confidence
- Standing strength: {…}; merits strength: {…}; overall likelihood: {…}
```

---

## Verification

- [ ] Standing analyzed first under the state's categories and triggers.
- [ ] *Troxel* fit-parent presumption/special weight applied.
- [ ] State's substantive standard (harm/unfitness/threshold) applied, with the visitation-vs-custody distinction.
- [ ] De facto/psychological parent test applied where relevant.
- [ ] Proof required for standing and merits listed.
- [ ] UCCJEA jurisdiction confirmed.
- [ ] Standing strength, merits strength, and overall likelihood assessed.
- [ ] No plain best-interests shortcut; no invented standing categories or standards.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Applying a plain best-interests test against a fit parent | Apply *Troxel*'s presumption and the state's heightened standard |
| Assuming grandparents have a general visitation right | Most statutes are narrow and post-*Troxel*-constrained; check standing |
| Skipping the standing analysis | No standing ends the inquiry; analyze it first |
| Treating visitation and custody claims alike | Custody carries a higher bar than visitation |
| Inventing the state's standing categories/standard | Use [CITE]/[NEED STANDARD] placeholders |
| Ignoring the fit-parent's stated reasons | A fit parent's decision gets special weight; address it |
| Overlooking the de facto-parent test where it applies | Apply the state's psychological-parent factors |
| Assuming a best-interests win equals a constitutional win | The constitutional presumption must be overcome first |
| Skipping UCCJEA | Confirm jurisdiction as for any custody matter |
| Overstating likelihood | Provide calibrated standing/merits strength and confidence |

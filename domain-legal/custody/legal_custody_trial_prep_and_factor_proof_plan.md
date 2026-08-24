---
title: "Custody Trial Prep and Factor-Proof Plan"
category: legal/custody
description: "Prepare a contested custody case for trial: a factor-by-factor proof plan mapping each best-interests factor to the evidence and witnesses that establish it, a witness list (parties, teachers, therapists, evaluators, fact witnesses) with the points each makes, an exhibit list with authentication and admissibility notes, a child-testimony/in-camera strategy, and proposed findings tied to the factors — sized to the controlling state's custody-trial procedure."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - trial-preparation
  - best-interests
  - proof-plan
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_custody_evaluation_prep_and_response.md
  - domain-legal/custody/legal_guardian_ad_litem_report_response.md
  - domain-legal/divorce/legal_divorce_trial_prep_and_findings_plan.md
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
---

**Purpose:** Turn a contested custody case into a trial-ready proof plan organized around the state's best-interests factors — mapping each factor to evidence and witnesses, planning testimony and exhibits, addressing the child's voice, and drafting proposed findings. Output is an internal trial plan with proposed findings, not a brief or advice.

**When to use:** A custody dispute is going to trial; building the factor-by-factor proof; identifying evidentiary gaps before the discovery cutoff; preparing witnesses and the child-testimony strategy.

---

## Your Input

- **Jurisdiction:** [State; custody-trial procedure; the best-interests factors; child-testimony and in-camera rules `[CITE: …]` `[NEED FACTOR LIST: …]`]
- **The dispute:** [Legal/physical custody and parenting time at issue; each side's proposal]
- **Best-interests facts:** [The facts relevant to each factor]
- **Witnesses:** [Parties, teachers/childcare, therapists/doctors, evaluator/GAL, relatives, fact witnesses]
- **Documents:** [School/medical records, communications, photos, calendars, evaluation/GAL report]
- **Child's voice:** [Age/maturity; whether the child will be heard; in-camera/GAL approach]
- **Safety facts:** [DV/abuse/substance evidence]
- **Theme:** [The child-centered narrative the evidence supports]

---

## Constraints

**Must:**
- Organize the plan around the state's **enumerated best-interests factors** `[NEED FACTOR LIST: …]`; build a **proof matrix** mapping each factor to the evidence and the witness that establishes it; flag **gaps**.
- Plan **witnesses** with the specific points each establishes and which factors they support; for **professional witnesses** (teachers, therapists, evaluator, GAL), note their qualifications, scope, and any privilege/consent issues.
- Build an **exhibit list** with sponsor, authentication, and admissibility (hearsay/foundation) notes.
- Address the **child's voice** per the state's rule — in-camera interview, GAL, or testimony — and the protections involved; avoid putting the child in the middle.
- Keep every conclusion tied to the **child's** interests and a coherent **child-centered theme**.
- Handle **safety evidence** (DV/abuse/substance) with the proof the state requires and any presumption.
- Draft **proposed findings** tracking the factors and the proof.
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority, factors, or facts.

**Must Not:**
- Build the plan around parental grievances rather than the factors and the child.
- Propose findings unsupported by the proof matrix.
- Call the child as a witness contrary to the state's rule or where it would harm the child.
- Assume privileged records (therapy) are admissible without addressing privilege/consent.
- Invent the factors, procedure, or child-testimony rules.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Factor framework.** State the best-interests factors and the trial/child-testimony procedure `[CITE: …]`.
2. **Proof matrix.** Map each factor to the evidence and witness; flag gaps and needed discovery.
3. **Witness plan.** For each witness, the points and factors they support; for professionals, qualifications/scope/privilege.
4. **Exhibit list.** Sponsor, authentication, admissibility notes; privilege/consent for sensitive records.
5. **Child's voice.** Plan the in-camera/GAL/testimony approach and protections.
6. **Safety proof.** Plan DV/abuse/substance evidence and any presumption.
7. **Theme & proposed findings.** State the child-centered theme; draft proposed findings tied to the factors.
8. **Gap remediation.** Identify missing evidence and how to obtain it before cutoff.

---

## Output Format

```markdown
# CUSTODY TRIAL PLAN — PRIVILEGED WORK PRODUCT — Case No. {____}
**State:** {…} [CITE: …]   **At issue:** {legal/physical custody, parenting time}   **Theme:** {…}

## 1. Best-Interests Factors & Procedure
{Factors} [NEED FACTOR LIST]; child-testimony/in-camera rule: {…}

## 2. Factor Proof Matrix
| Factor | Facts to prove | Evidence | Witness | Exhibit | Status/gap |
|---|---|---|---|---|---|
| {Factor 1} | {…} | {…} | {…} | {Ex.} | {have/gap} |

## 3. Witness Plan
- {Witness} — points/factors: {…}; {qualifications/privilege if professional}

## 4. Exhibit List
| # | Exhibit | Sponsor | Authentication | Admissibility / privilege |
|---|---|---|---|---|

## 5. Child's Voice
- Approach: {in-camera / GAL / testimony}; protections: {…}

## 6. Safety Proof
- {DV/abuse/substance evidence; presumption}

## 7. Proposed Findings
- FOF tied to {Factor}: {…} (supported by {evidence}).

## 8. Gap Remediation
- [ ] {Evidence needed} via {device} by {deadline}
```

---

## Verification

- [ ] Plan organized around the state's best-interests factors.
- [ ] Proof matrix maps each factor to evidence and a witness; gaps flagged.
- [ ] Witness plan specifies points/factors and handles professional qualifications/privilege.
- [ ] Exhibit list includes authentication, admissibility, and privilege/consent notes.
- [ ] Child's-voice approach conforms to the state's rule with protections; child not put in the middle.
- [ ] Safety evidence planned with any presumption.
- [ ] Proposed findings track the factors and the proof.
- [ ] No grievance-driven framing; no invented factors/procedure; no unsupported findings.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Building the case around parental grievances | Organize around the best-interests factors and the child |
| Proposed findings unsupported by the evidence | Tie each finding to a proof-matrix entry |
| Calling the child as a witness improperly | Follow the state's child-testimony/in-camera rule; avoid harm |
| Assuming therapy/medical records are admissible | Address privilege and consent before relying on them |
| Generic best-interests list | Use the state's enumerated factors [NEED FACTOR LIST] |
| Exhibits without authentication/admissibility analysis | Note sponsor, foundation, and hearsay issues |
| Ignoring safety presumptions | Plan DV/abuse/substance proof and apply any presumption |
| Discovering gaps after the cutoff | Identify and remediate gaps before the deadline |
| No coherent child-centered theme | Anchor the proof to a single child-focused narrative |
| Inventing the trial/child-testimony procedure | Use [CITE]/[NEED] placeholders |

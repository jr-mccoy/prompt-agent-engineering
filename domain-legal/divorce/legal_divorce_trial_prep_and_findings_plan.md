---
title: "Divorce Trial Prep and Findings Plan"
category: legal/divorce
description: "Prepare a contested divorce for trial: an issue list with the burden and standard for each contested issue (grounds, characterization, valuation, support, custody), a witness and exhibit plan tied to each issue, a proof matrix mapping evidence to the elements/factors, proposed findings of fact and conclusions of law, and an order of proof — sized to the controlling state's family-trial procedure."
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
  - divorce
  - family-law
  - trial-preparation
  - findings-of-fact
  - proof-matrix
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_divorce_discovery_plan_and_requests.md
  - domain-legal/custody/legal_custody_trial_prep_and_factor_proof_plan.md
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
---

**Purpose:** Turn a contested dissolution into a trial-ready plan: identify each contested issue with its burden and standard, build a proof matrix that maps evidence to the elements/factors, plan witnesses and exhibits, and draft proposed findings the court can adopt. Output is an internal trial plan with draft proposed findings, not a brief or advice.

**When to use:** A dissolution is heading to trial on grounds, property, support, or custody; preparing the proof and proposed findings; identifying evidentiary gaps before the discovery cutoff.

---

## Your Input

- **Jurisdiction:** [State; family-trial procedure; whether findings of fact/conclusions of law are required or requested `[CITE: …]`]
- **Property regime:** [Community / equitable distribution]
- **Contested issues:** [Grounds, characterization, valuation, division, spousal support, child support, custody/parenting]
- **Governing standards:** [The factors/elements for each contested issue `[NEED FACTOR LIST: …]`]
- **Evidence available:** [Documents, valuations, financial affidavits, expert reports, witness statements]
- **Witnesses:** [Parties, experts (valuation, forensic, custody), fact witnesses]
- **Disputed facts:** [The specific facts the court must resolve]
- **Relief sought:** [The orders requested on each issue]

---

## Constraints

**Must:**
- List each **contested issue** with the **burden of proof** and **governing standard/factors** for the state `[CITE: …]`.
- Build a **proof matrix** mapping each element/factor to the specific evidence and witness that establishes it; flag **gaps**.
- Plan **witnesses** (direct outline themes, expert qualifications/opinions) and an **exhibit list** with authentication and admissibility notes.
- Draft **proposed findings of fact and conclusions of law** that track the issues and the evidence, written so the court can adopt them.
- Provide an **order of proof** sequencing the case efficiently.
- Keep **custody proof** anchored to the best-interests factors (cross-reference the custody trial-prep prompt).
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority, factors, or facts.

**Must Not:**
- Assert facts not in evidence or fabricate testimony, exhibits, or expert opinions.
- Propose findings unsupported by the proof matrix.
- Ignore the burden of proof on any issue.
- Invent the state's factors, standards, or procedure.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Issue list.** Enumerate contested issues; state the burden and standard/factors for each `[CITE: …]`.
2. **Proof matrix.** For each element/factor, map the evidence and witness; mark gaps and needed discovery.
3. **Witness plan.** Outline each witness's purpose and the points they establish; for experts, qualifications and opinions.
4. **Exhibit list.** List exhibits with sponsor, authentication, and admissibility notes.
5. **Proposed findings.** Draft findings of fact and conclusions of law tracking the issues and proof.
6. **Order of proof.** Sequence witnesses/exhibits for an efficient presentation.
7. **Gap remediation.** List the evidence still needed and how to obtain it before cutoff.

---

## Output Format

```markdown
# DIVORCE TRIAL PLAN — PRIVILEGED WORK PRODUCT — Case No. {____}
**State / procedure:** {…} [CITE: …]   **Regime:** {…}

## 1. Contested Issues, Burden & Standard
| Issue | Burden | Standard / factors |
|---|---|---|
| {Characterization of {asset}} | {movant} | {state rule [CITE]} |
| {Spousal support} | {…} | {factors [NEED FACTOR LIST]} |

## 2. Proof Matrix
| Issue → Element/Factor | Evidence | Witness | Exhibit | Status / gap |
|---|---|---|---|---|
| {…} | {…} | {…} | {Ex. } | {have/gap} |

## 3. Witness Plan
- {Witness} — purpose: {…}; establishes: {…}; {expert qualifications/opinions}

## 4. Exhibit List
| # | Exhibit | Sponsor | Authentication | Admissibility note |
|---|---|---|---|---|

## 5. Proposed Findings of Fact & Conclusions of Law
- FOF 1: {…} (supported by {evidence}). … COL 1: {…} [CITE].

## 6. Order of Proof
- {Sequence}

## 7. Gap Remediation
- [ ] {Evidence needed} via {device} by {deadline}
```

---

## Verification

- [ ] Each contested issue listed with burden and governing standard/factors.
- [ ] Proof matrix maps every element/factor to evidence and a witness; gaps flagged.
- [ ] Witness and exhibit plans include authentication/admissibility notes.
- [ ] Proposed findings track the issues and are supported by the proof matrix.
- [ ] Order of proof provided.
- [ ] Custody proof anchored to best-interests factors.
- [ ] No facts asserted without evidence; no fabricated testimony/exhibits.
- [ ] No invented factors, standards, or procedure.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Proposing findings the evidence does not support | Tie every proposed finding to a proof-matrix entry |
| Ignoring the burden of proof on an issue | State who bears the burden for each contested issue |
| Listing exhibits without authentication/admissibility analysis | Note sponsor, authentication, and any hearsay/foundation issue |
| Fabricating expert opinions or witness testimony | Use only disclosed opinions and actual witness statements |
| Custody proof untethered to the statutory factors | Map custody evidence to each best-interests factor |
| Inventing the state's standards or factors | Use [CITE]/[NEED FACTOR LIST] placeholders |
| Discovering gaps after the cutoff | Identify gaps now and remediate before the deadline |
| One undifferentiated narrative instead of issue-by-issue proof | Organize the plan by contested issue and element |
| Overlooking valuation-date or characterization disputes at trial | Include them as discrete issues with their own proof |
| Proposed findings the court cannot adopt as written | Draft neutral, record-grounded findings in adoptable form |

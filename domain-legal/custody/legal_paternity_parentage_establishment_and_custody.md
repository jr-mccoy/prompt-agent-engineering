---
title: "Paternity / Parentage Establishment and Custody"
category: legal/custody
description: "Analyze and draft paternity/parentage establishment and its custody and support consequences: identify the legal parentage bases (marital presumption, voluntary acknowledgment, genetic testing, holding-out, assisted reproduction/surrogacy, second-parent and de facto parentage), address standing and limitations to establish or disestablish, and connect an adjudication of parentage to custody, parenting time, and child-support rights — sized to the controlling state's parentage act."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - paternity
  - parentage
  - child-support
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_petition_or_motion_drafter.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_third_party_custody_visitation_analysis.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
---

**Purpose:** Determine the available bases to establish (or disestablish) legal parentage and connect a parentage adjudication to custody, parenting time, and child support. Output is a parentage analysis and the petition/relief framework, not a guaranteed result; parentage law is state-specific and increasingly addresses assisted reproduction and non-biological parents.

**When to use:** Establishing paternity/parentage for custody or support; disestablishing paternity; parentage disputes involving the marital presumption, acknowledgment, assisted reproduction, surrogacy, or a second/de facto parent; connecting parentage to custody and support.

---

## Your Input

- **Jurisdiction:** [State; the state's parentage act (e.g., UPA-based or state-specific) and its bases, standing, and limitations `[CITE: …]`]
- **Objective:** [Establish parentage / disestablish parentage / determine parentage among competing claimants]
- **Marital status:** [Whether the child was born to married parents (marital presumption) or unmarried]
- **Acknowledgment:** [Whether a voluntary acknowledgment of parentage was signed; when]
- **Genetic testing:** [Whether testing has been done or is sought]
- **Conduct facts:** [Holding-out/residence with the child; assumption of the parental role]
- **Assisted reproduction / surrogacy:** [Donor, intended parents, surrogacy agreement, same-sex couple, second-parent adoption status]
- **Competing claimants:** [More than one person claiming or denying parentage]
- **Custody/support goal:** [The custody, parenting-time, or support relief tied to the parentage finding]

---

## Constraints

**Must:**
- Identify the **bases for legal parentage** under the state's act: the **marital presumption**, a **voluntary acknowledgment of parentage (VAP)**, **genetic testing/adjudication**, **holding-out/conduct presumption**, **assisted-reproduction and surrogacy** rules, and **second-parent/de facto/intended-parent** parentage where the state recognizes it `[CITE: …]`.
- Address **standing and limitations periods** to establish or **disestablish/rescind** (a VAP typically has a short rescission window and then limited challenge grounds) `[CITE: …]`.
- Address **competing presumptions** and how the state resolves them (often by a best-interests/policy weighing, not biology alone).
- Recognize that **assisted reproduction and surrogacy** are governed by specific provisions (donor non-parentage, intended-parent status, gestational-carrier agreements) — not the default biological rules.
- Connect the parentage adjudication to **custody, parenting time, and child support** consequences, including retroactive support where allowed.
- Confirm **UCCJEA** jurisdiction for any custody relief and the proper **venue/joinder** (including the state child-support agency where involved).
- Use placeholders `[CITE: ...]`, `[NEED ACT: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Assume biology controls parentage — presumptions, acknowledgments, and intended-parent rules may override genetics.
- Ignore the limitations period or rescission window for acknowledgments and disestablishment.
- Apply default rules to assisted-reproduction/surrogacy cases.
- Assume disestablishment ends a support obligation automatically (some states bar disestablishment after reliance).
- Invent the state's parentage act, standing rules, or limitations periods.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Objective & status.** State the objective and the family/marital/assisted-reproduction context.
2. **Parentage bases.** Identify each applicable basis under the state's act and which establishes (or defeats) parentage `[CITE: …]`.
3. **Standing & limitations.** Determine standing and any limitations/rescission window for establishment or disestablishment.
4. **Competing presumptions.** Resolve competing claims under the state's weighing rule.
5. **Assisted reproduction/surrogacy.** Apply the specific provisions where relevant.
6. **Custody/support consequences.** Connect the parentage finding to custody, parenting time, and support (including retroactive support if allowed).
7. **Jurisdiction & procedure.** Confirm UCCJEA, venue, joinder (child-support agency), and the relief framework.
8. **Petition/relief.** Frame the parentage petition and the linked custody/support requests.

---

## Output Format

```markdown
# PARENTAGE ESTABLISHMENT & CUSTODY ANALYSIS — Case No. {____}
**State / act:** {…} [CITE: …] [NEED ACT: …]   **Objective:** {establish/disestablish/determine}

## 1. Context
- Marital status: {…}; acknowledgment: {…}; assisted reproduction/surrogacy: {…}

## 2. Parentage Bases
| Basis | Applies? | Effect |
|---|---|---|
| Marital presumption | {…} | {establishes} |
| Voluntary acknowledgment | {…} | {…} |
| Genetic testing/adjudication | {…} | {…} |
| Holding-out/conduct | {…} | {…} |
| Assisted reproduction/intended parent | {…} | {…} |

## 3. Standing & Limitations
- Standing: {…}; limitations/rescission window: {…} [CITE]

## 4. Competing Presumptions
- Resolution under {state weighing rule}: {…}

## 5. Assisted Reproduction / Surrogacy (if applicable)
- {Donor non-parentage / intended-parent status / carrier agreement}

## 6. Custody / Support Consequences
- Custody/parenting time: {…}; child support: {prospective + retroactive if allowed}

## 7. Jurisdiction & Procedure
- UCCJEA: {…}; venue/joinder (incl. child-support agency): {…}

## 8. Petition / Relief Framework
- {Parentage petition + linked custody/support requests}
```

---

## Verification

- [ ] Applicable parentage bases identified under the state's act.
- [ ] Standing and limitations/rescission windows addressed for establishment/disestablishment.
- [ ] Competing presumptions resolved under the state's rule (not biology alone).
- [ ] Assisted-reproduction/surrogacy provisions applied where relevant.
- [ ] Custody, parenting-time, and support consequences connected (including retroactive support if allowed).
- [ ] UCCJEA, venue, and joinder (child-support agency) confirmed.
- [ ] Petition/relief framework provided.
- [ ] No biology-controls assumption; no invented act, standing, or limitations rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Assuming genetics alone determines parentage | Presumptions, acknowledgments, and intended-parent rules may override biology |
| Ignoring the VAP rescission window/limitations | Check the short rescission period and limited later-challenge grounds |
| Applying default rules to assisted reproduction/surrogacy | Use the act's specific donor/intended-parent/carrier provisions |
| Assuming disestablishment ends support automatically | Some states bar disestablishment after reliance; check the rule |
| Overlooking competing presumptions | Apply the state's weighing rule to resolve them |
| Inventing the state's parentage act | Use [CITE]/[NEED ACT] placeholders |
| Forgetting retroactive support | Address retroactive support where the state allows it |
| Skipping UCCJEA for the custody piece | Confirm jurisdiction for any custody relief |
| Omitting the child-support agency as a party | Join the agency where it is involved |
| Treating second-parent/de facto claims as unavailable | Apply the state's recognition of non-biological parentage |

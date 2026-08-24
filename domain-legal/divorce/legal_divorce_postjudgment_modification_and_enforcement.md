---
title: "Post-Judgment Modification and Enforcement"
category: legal/divorce
description: "Analyze and draft post-judgment relief in a dissolution: modification of spousal support, child support, or custody based on a substantial change in circumstances; enforcement of property-division, support, or QDRO obligations through contempt, judgment, wage withholding, or liens; and the threshold question of what is modifiable vs. fixed (property division is generally final) — sized to the controlling state's modification standards and enforcement remedies."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - modification
  - enforcement
  - contempt
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
  - domain-legal/custody/legal_parenting_time_enforcement_and_contempt_motion.md
---

**Purpose:** Determine what post-judgment relief is available and draft the motion to obtain it — modifying support or custody on a substantial change in circumstances, or enforcing unpaid support, unfulfilled property transfers, or an unexecuted QDRO. Output is an analysis and a filing-ready motion, distinguishing modifiable obligations from final ones.

**When to use:** A party seeks to change support or custody after judgment; a party needs to enforce unpaid support, an unperformed property transfer, or a stalled QDRO; assessing whether a term can be revisited at all.

---

## Your Input

- **Jurisdiction:** [State; modification standards for support/custody; enforcement remedies; statute of limitations on arrears `[CITE: …]`]
- **Relief sought:** [Modify spousal support / child support / custody; OR enforce support arrears / property transfer / QDRO]
- **The judgment/MSA:** [The relevant terms; whether the MSA merged or survived; any non-modifiability language]
- **Change in circumstances:** [The facts said to be a substantial/material change since the last order]
- **Compliance facts:** [What was paid/performed; arrears amount; missed transfers]
- **Children:** [Ages, current arrangement, the change affecting them, if custody/support is at issue]
- **Enforcement history:** [Prior demands, wage withholding, liens, contempt history]

---

## Constraints

**Must:**
- Determine **modifiability first**: spousal support (modifiable unless made non-modifiable), child support and custody (always modifiable in the child's interest), and **property division (generally final and not modifiable)** — and apply the state's rule `[CITE: …]`.
- For modification, apply the state's **substantial/material change in circumstances** standard and the **best-interests** overlay for custody `[CITE: …]`; address whether the change was anticipated or self-induced.
- For enforcement, identify the available **remedies** (money judgment on arrears, contempt, wage withholding/income assignment, liens, license suspension, interest on arrears) and the **statute of limitations** on arrears `[CITE: …]`.
- For **contempt**, confirm a clear order, the ability to comply (inability is a defense), and willfulness.
- For a stalled **QDRO**, frame enforcement of the obligation to execute/submit the order (cross-reference the QDRO framework).
- Use placeholders `[CITE: ...]`, `[NEED STANDARD: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Seek modification of a **final property division** as if it were support (it generally cannot be modified absent fraud/limited grounds).
- Treat a self-induced or anticipated change as automatically qualifying.
- Pursue contempt where the obligor lacks the ability to comply (raise it, don't ignore it).
- Invent the modification standard, limitations period, or remedies.
- Threaten criminal contempt or incarceration as leverage outside the proper standard.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Modifiability threshold.** Classify the obligation as modifiable or final; apply the state's rule and any non-modifiability language.
2. **Modification analysis.** Apply the change-in-circumstances standard (and best interests for custody); assess whether the change is substantial, unanticipated, and not self-induced.
3. **Recompute (if support).** Apply the support guideline/factors to the new circumstances (cross-reference support/child-support prompts).
4. **Enforcement analysis.** Identify the remedy for each unmet obligation; compute arrears and interest; check the limitations period.
5. **Contempt elements.** Confirm a clear order, willfulness, and ability to comply.
6. **QDRO enforcement.** Frame relief to compel execution/submission of the order.
7. **Draft the motion.** Caption, grounds, supporting declaration, requested relief, and proposed order.

---

## Output Format

```markdown
# POST-JUDGMENT {MODIFICATION / ENFORCEMENT} — Case No. {____}
**State:** {…} [CITE: …]   **Relief:** {…}

## 1. Modifiability Threshold
- Obligation: {support/custody/property}; modifiable: {yes/no — property generally final} [CITE: …]

## 2. Modification Analysis (if applicable)
- Standard: {substantial change [CITE]}; change: {…}; anticipated/self-induced? {…}; best interests (custody): {…}

## 3. Recomputation (if support)
- New guideline/factor result: {$} [see support prompt]

## 4. Enforcement Analysis (if applicable)
- Unmet obligation: {…}; arrears: {$} + interest {$}; limitations: {…} [CITE]
- Remedies: {money judgment / wage withholding / lien / license suspension / contempt}

## 5. Contempt Elements
- Clear order: {…}; willfulness: {…}; ability to comply: {…}

## 6. QDRO Enforcement (if applicable)
- Relief to compel execution/submission: {…}

## 7. Motion
{Caption}
MOTION TO {MODIFY / ENFORCE}
Grounds: {…}. Declaration of {movant}: {personal-knowledge facts}. Relief requested: {…}.
[PROPOSED] ORDER: {…}
```

---

## Verification

- [ ] Modifiability determined first; property division treated as generally final.
- [ ] Change-in-circumstances standard (and best interests for custody) applied; anticipation/self-inducement addressed.
- [ ] Support recomputed under the guideline/factors where modification is sought.
- [ ] Enforcement remedies identified; arrears and interest computed; limitations checked.
- [ ] Contempt elements (clear order, willfulness, ability to comply) confirmed.
- [ ] QDRO enforcement framed where applicable.
- [ ] Motion includes grounds, supporting declaration, relief, and proposed order.
- [ ] No invented standards, limitations, or remedies.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Trying to modify a final property division | Property division is generally final; identify the narrow fraud/error grounds if any |
| Treating any change as a "substantial change" | Apply the state's standard; address anticipation and self-inducement |
| Pursuing contempt despite the obligor's inability to pay | Inability to comply is a defense; assess it before seeking contempt |
| Ignoring the statute of limitations on arrears | Check the limitations period before suing on old arrears |
| Forgetting interest on support arrears | Compute statutory interest where it accrues |
| Modifying child support/custody without best-interests analysis | Apply the best-interests overlay for child-related modifications |
| Invented modification standard or remedies | Use [CITE]/[NEED STANDARD] placeholders |
| Threatening incarceration as leverage | Confine contempt to the proper willfulness/ability standard |
| Overlooking wage withholding/income assignment | Include administrative remedies, not just contempt |
| Confusing merged vs. surviving MSA for enforcement | The merger/survival election affects available remedies |

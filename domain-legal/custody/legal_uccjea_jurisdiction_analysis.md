---
title: "UCCJEA Jurisdiction Analysis"
category: legal/custody
description: "Analyze custody jurisdiction under the Uniform Child Custody Jurisdiction and Enforcement Act: determine the child's home state, apply initial-jurisdiction, exclusive-continuing-jurisdiction, modification, and temporary-emergency-jurisdiction rules, resolve competing-state and inconvenient-forum questions, and frame registration and enforcement of an out-of-state custody order — producing a jurisdiction memo with the controlling basis and the steps to invoke or contest it."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - uccjea
  - jurisdiction
  - home-state
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_petition_or_motion_drafter.md
  - domain-legal/custody/legal_temporary_and_emergency_custody_motion.md
  - domain-legal/custody/legal_relocation_move_away_analysis.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
  - domain-legal/divorce/legal_divorce_petition_complaint_drafter.md
---

**Purpose:** Determine which state has jurisdiction to make or modify a custody determination under the UCCJEA, and frame the steps to invoke, contest, register, or enforce it. Output is a jurisdiction memo identifying the controlling basis and confidence, not advice and not a substitute for the specific state's enactment of the UCCJEA.

**When to use:** Parents live in or have moved between different states; a custody order exists in another state; an interstate (or international) custody dispute; before filing a custody petition or modification to confirm the forum has authority.

---

## Your Input

- **States involved:** [Each state where the child or a parent lives or recently lived; the state's UCCJEA enactment `[CITE: …]`]
- **Child's residence history:** [Where the child has lived for the past 6 months and longer, with dates and caregivers]
- **Existing orders:** [Any custody order, the state that issued it, and whether that court retains jurisdiction]
- **Parent locations:** [Current residence of each parent and the child]
- **Posture:** [Initial determination / modification of another state's order / emergency / registration / enforcement]
- **Emergency facts:** [Abandonment, abuse, or threat supporting temporary emergency jurisdiction]
- **Connections:** [Significant connections to a state and substantial evidence located there]
- **International facts:** [Any foreign-country involvement; Hague Convention considerations]

---

## Constraints

**Must:**
- Determine the **home state** — where the child lived with a parent for **at least six consecutive months** immediately before the proceeding (or since birth for an infant), including the extended/recent-departure rule `[CITE: …]`.
- Apply the correct UCCJEA basis in order: **initial child-custody jurisdiction** (home state priority), **exclusive continuing jurisdiction** (the original decree state retains it until conditions end), **jurisdiction to modify** another state's order, and **temporary emergency jurisdiction** (limited, child present + emergency) `[CITE: …]`.
- Address **simultaneous proceedings** and **inconvenient forum / declined jurisdiction** and the duty to communicate between courts.
- For an existing out-of-state order, analyze whether the issuing state retains **exclusive continuing jurisdiction** before assuming the new state can modify.
- Frame **registration and enforcement** of an out-of-state order and expedited enforcement remedies.
- Treat **emergency jurisdiction as temporary** — it does not become permanent without satisfying another basis.
- Assign **confidence** to the controlling-basis conclusion.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for the state's specific enactment or unsupplied facts.

**Must Not:**
- Assume the state where the petition is filed has jurisdiction without the home-state and continuing-jurisdiction analysis.
- Treat temporary emergency jurisdiction as a basis for a permanent custody determination.
- Ignore another state's exclusive continuing jurisdiction over an existing order.
- Invent the six-month/home-state rule's application or the state's enactment specifics.
- Conflate the UCCJEA (jurisdiction) with the substantive best-interests analysis.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Residence timeline.** Build the child's residence history with dates; identify the home state (or none).
2. **Existing-order check.** If an order exists, analyze the issuing state's exclusive continuing jurisdiction.
3. **Basis selection.** Apply initial / continuing / modification / emergency jurisdiction in order; identify the controlling basis.
4. **Competing proceedings & forum.** Address simultaneous filings, inconvenient forum, and inter-court communication.
5. **Emergency (if applicable).** Confirm the child's presence and the emergency; frame the temporary order and the duty to defer to the home state.
6. **Registration/enforcement (if applicable).** Frame registration of the out-of-state order and expedited enforcement.
7. **Conclusion & steps.** State the controlling basis, confidence, and the procedural steps to invoke or contest it.

---

## Output Format

```markdown
# UCCJEA JURISDICTION ANALYSIS — PRIVILEGED WORK PRODUCT
**States involved:** {…}   **Posture:** {…}   **Enactment:** {…} [CITE: …]

## 1. Child's Residence Timeline
| Period | State | With whom |
|---|---|---|
| {dates} | {…} | {…} |
- Home state: {state / none}; basis: six-month rule [CITE]

## 2. Existing Order / Continuing Jurisdiction
- Issuing state: {…}; retains exclusive continuing jurisdiction? {yes/no — analysis} [CITE]

## 3. Controlling Basis
- {Initial / Continuing / Modification / Emergency}; reasoning: {…}; confidence: {…}

## 4. Competing Proceedings & Forum
- Simultaneous proceedings: {…}; inconvenient forum: {…}; court communication: {…}

## 5. Emergency Jurisdiction (if applicable)
- Child present + emergency: {…}; temporary only; defer to home state {…}

## 6. Registration / Enforcement (if applicable)
- Registration steps: {…}; expedited enforcement: {…}

## 7. Conclusion & Steps
- Controlling state: {…}; steps to invoke/contest: {…}
```

---

## Verification

- [ ] Child's residence timeline built; home state identified (or none) under the six-month rule.
- [ ] Existing order analyzed for the issuing state's exclusive continuing jurisdiction.
- [ ] UCCJEA bases applied in order; controlling basis identified with confidence.
- [ ] Simultaneous proceedings, inconvenient forum, and court communication addressed.
- [ ] Emergency jurisdiction treated as temporary, with deferral to the home state.
- [ ] Registration/enforcement framed where an out-of-state order is involved.
- [ ] Jurisdiction kept distinct from the best-interests merits.
- [ ] No invented home-state application or enactment specifics.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Assuming the filing state has jurisdiction | Run the home-state and continuing-jurisdiction analysis first |
| Treating emergency jurisdiction as permanent | It is temporary; a permanent order needs another basis and home-state deferral |
| Ignoring the issuing state's exclusive continuing jurisdiction | Analyze whether that state still retains it before modifying |
| Miscounting the six-month home-state period | Build the dated residence timeline; apply the recent-departure rule |
| Conflating jurisdiction with best interests | Decide jurisdiction first; merits are separate |
| Overlooking simultaneous proceedings | Address pending cases and the duty of inter-court communication |
| Inventing the state's UCCJEA enactment specifics | Use [CITE]/[NEED] placeholders |
| Skipping registration before enforcement | Register the out-of-state order to enable enforcement |
| Ignoring inconvenient-forum analysis | Address whether the home state should decline in favor of another |
| Missing international/Hague considerations | Flag foreign-country involvement for Hague analysis |

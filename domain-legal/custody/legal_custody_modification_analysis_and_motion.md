---
title: "Custody Modification Analysis and Motion"
category: legal/custody
description: "Analyze and draft a custody/parenting-time modification: confirm jurisdiction to modify (UCCJEA), apply the state's threshold standard (substantial/material change in circumstances since the last order) and the best-interests overlay, distinguish modifiable parenting time from the higher bar to change custody, address any integration/endangerment or relocation triggers, and produce a modification motion with the supporting declaration and proposed order."
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
  - modification
  - changed-circumstances
  - parenting-time
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_relocation_move_away_analysis.md
  - domain-legal/custody/legal_parenting_time_enforcement_and_contempt_motion.md
  - domain-legal/divorce/legal_divorce_postjudgment_modification_and_enforcement.md
---

**Purpose:** Determine whether a custody or parenting-time order can be modified and draft the motion to do it — confirming modification jurisdiction, applying the changed-circumstances threshold and best-interests overlay, and distinguishing a parenting-time adjustment from a custody change. Output is an analysis plus a filing-ready motion, not a guaranteed result.

**When to use:** Circumstances have changed since the last custody order; a parent seeks more time or a change in legal/physical custody; addressing endangerment, relocation, or a child's changed needs; evaluating the other parent's modification request.

---

## Your Input

- **Jurisdiction:** [State; modification jurisdiction under the UCCJEA; the state's modification standard `[CITE: …]`]
- **Existing order:** [Current custody/parenting terms; date entered; issuing court]
- **Change since the order:** [The specific facts said to constitute a substantial/material change since the last order]
- **What is sought:** [Adjust parenting time vs. change legal/physical custody]
- **Best-interests facts:** [The facts supporting that the change serves the child]
- **Triggers:** [Endangerment, integration into a home, relocation, a parent's conduct, the child's changed needs/preference]
- **Time since last order:** [Any waiting period or rule limiting frequent modification]
- **Safety facts:** [DV/abuse/substance issues]

---

## Constraints

**Must:**
- Confirm **jurisdiction to modify** under the UCCJEA (the issuing state's exclusive continuing jurisdiction) **before** the merits (cross-reference the UCCJEA prompt).
- Apply the state's **threshold standard** — a **substantial/material change in circumstances since the last order** — and treat it as a **gatekeeper**: no change, no modification `[CITE: …]`.
- Apply the **best-interests overlay** once the threshold is met.
- Distinguish the **lower bar to adjust parenting time** from the **higher bar to change custody** where the state imposes one, and any **endangerment** standard for changing custody.
- Address **the child's changed needs/preference** at the weight the state allows, and any **integration** or **relocation** trigger.
- Note any **time bar / frequency limit** on modification motions `[CITE: …]`.
- Anchor everything to the **child**, not the parents' convenience.
- Use placeholders `[CITE: ...]`, `[NEED STANDARD: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Reach the best-interests merits without first clearing the changed-circumstances gate.
- Treat ordinary, anticipated, or minor changes as "substantial."
- Apply the parenting-time standard to a custody change (or vice versa) where the state differentiates.
- Assume modification jurisdiction without the UCCJEA analysis.
- Invent the modification standard, endangerment test, or time bar.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Modification jurisdiction.** Confirm UCCJEA jurisdiction to modify; flag if it sits in another state.
2. **Threshold analysis.** Identify the change since the last order; test it against the substantial/material standard; address whether it was anticipated.
3. **Relief type.** Determine whether a parenting-time adjustment or a custody change is sought and the applicable bar/endangerment standard.
4. **Best interests.** If the threshold is met, apply the best-interests factors to the requested change.
5. **Triggers.** Address endangerment, integration, relocation, or the child's changed needs/preference.
6. **Time/frequency bar.** Check any limit on modification motions.
7. **Draft the motion.** Caption, jurisdiction, changed-circumstances allegations, best-interests basis, requested modification, supporting declaration, proposed order.

---

## Output Format

```markdown
# CUSTODY MODIFICATION — ANALYSIS & MOTION — Case No. {____}
**State:** {…} [CITE: …]   **Existing order:** {date/court}

## 1. Modification Jurisdiction (UCCJEA)
- Jurisdiction to modify: {this state / another state} — see UCCJEA analysis

## 2. Changed-Circumstances Threshold
- Change since last order: {…}; substantial/material? {analysis}; anticipated? {…} — GATE: {met/not met} [CITE]

## 3. Relief Type & Standard
- {Parenting-time adjustment / custody change}; applicable bar/endangerment: {…}

## 4. Best Interests (if gate met)
- Factor application supporting the change: {…}

## 5. Triggers
- {Endangerment / integration / relocation / child's needs/preference}: {…}

## 6. Time/Frequency Bar
- {Any limit on modification motions} [CITE]

## 7. Motion
{Caption}
MOTION TO MODIFY CUSTODY / PARENTING TIME
Jurisdiction: {…}. Changed circumstances: {…}. Best interests: {…}. Relief requested: {…}.
Declaration of {movant}: {personal-knowledge facts}. [PROPOSED] ORDER: {…}.
```

---

## Verification

- [ ] UCCJEA modification jurisdiction confirmed before the merits.
- [ ] Changed-circumstances threshold applied as a gate; anticipation addressed.
- [ ] Relief type identified with the correct bar/endangerment standard.
- [ ] Best-interests analysis applied only after the gate is met.
- [ ] Endangerment/integration/relocation/child's-needs triggers addressed.
- [ ] Any time/frequency bar checked.
- [ ] Motion includes jurisdiction, changed circumstances, best interests, relief, declaration, and proposed order.
- [ ] No invented standards; analysis anchored to the child.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Jumping to best interests without the changed-circumstances gate | Clear the threshold first; no change, no modification |
| Calling a minor/anticipated change "substantial" | Apply the state's standard; address whether the change was foreseeable |
| Applying the parenting-time bar to a custody change | Use the higher custody/endangerment standard where the state differentiates |
| Assuming the forum can modify | Run the UCCJEA modification-jurisdiction analysis |
| Framing around parental convenience | Anchor the requested change to the child's best interests |
| Ignoring a time/frequency limit on motions | Check any waiting period or anti-relitigation rule |
| Inventing the modification or endangerment standard | Use [CITE]/[NEED STANDARD] placeholders |
| Overweighting the child's preference | Apply the weight the state gives for age/maturity |
| Treating relocation as an ordinary modification | Route relocation through the move-away analysis |
| Motion without a personal-knowledge declaration | Attach the supporting declaration |

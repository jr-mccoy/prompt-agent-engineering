---
title: "Relocation / Move-Away Analysis"
category: legal/custody
description: "Analyze a parental relocation (move-away) request or opposition under the controlling state's framework: confirm notice requirements and the burden allocation, apply the state's relocation factors (the child's relationship with each parent, reasons for and against the move, impact on the schedule, feasibility of a revised plan), distinguish primary-custodian presumptions from joint-custody standards, and produce a position memo with a revised long-distance parenting plan and the proof needed."
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
  - relocation
  - move-away
  - long-distance-parenting
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_custody_trial_prep_and_factor_proof_plan.md
---

**Purpose:** Evaluate a parent's proposed relocation with the child (or the opposition to it) under the controlling state's move-away framework, allocate the burden, apply the relocation factors, and propose a revised long-distance parenting plan. Output is a position memo with the relocation analysis and a proposed plan, not a guaranteed result; relocation standards are highly state-specific and fact-intensive.

**When to use:** A custodial or joint-custodial parent wants to move a distance that disrupts the schedule; opposing a proposed move; preparing a relocation motion or objection; advising on notice obligations.

---

## Your Input

- **Jurisdiction:** [State; the state's relocation statute/standard, notice requirement, and burden allocation `[CITE: …]` `[NEED FACTOR LIST: …]`]
- **Custody status:** [Current legal/physical custody; whether the moving parent is the primary custodian or it is joint]
- **The move:** [Destination, distance, reason (job, family, remarriage, cost of living), timing]
- **Child(ren):** [Ages, ties to the current community, school, relationships, special needs]
- **Current schedule:** [Existing parenting time and the non-moving parent's involvement]
- **Impact:** [How the move affects the non-moving parent's time and the child's relationships]
- **Proposed revised plan:** [The long-distance schedule the moving parent proposes — extended summers/holidays, travel, virtual contact]
- **Good faith / bad faith:** [Whether the move is in good faith or to frustrate the other parent's relationship]
- **Notice given:** [Whether statutory relocation notice was provided and when]

---

## Constraints

**Must:**
- Confirm the state's **relocation notice requirement** (timing, content, method) and whether it was satisfied `[CITE: …]`.
- State the **burden allocation** — which parent bears it often depends on the custody arrangement (primary custodian vs. joint) and varies sharply by state `[CITE: …]`.
- Apply the state's **relocation factors** `[NEED FACTOR LIST: …]`: the child's relationship with each parent, the reasons for and against the move, the move's impact on the child and the schedule, the child's preference where relevant, and the feasibility of preserving the non-moving parent's relationship.
- Distinguish any **presumption** (some states favor a good-faith primary custodian; others apply a neutral best-interests test).
- Assess **good faith vs. bad faith** of the moving parent and any **legitimate purpose**.
- Propose a **revised long-distance parenting plan** (extended breaks, travel allocation, virtual contact) that mitigates the impact.
- Provide **factor-by-factor strength** and **confidence**; frame as a position (QA-12).
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority, factors, or facts.

**Must Not:**
- Invent the state's relocation factors, burden allocation, notice rule, or case standard (e.g., the specific multi-factor test).
- Assume the primary custodian may move freely, or that any move will be denied.
- Skip the notice analysis (defective notice can be dispositive).
- Treat the move as an ordinary modification without the relocation framework.
- Present a definitive outcome where the standard is discretionary and fact-intensive.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Notice.** State the relocation-notice requirement and whether it was met `[CITE: …]`.
2. **Custody status & burden.** Identify the custody arrangement and who bears the burden under the state's rule.
3. **Factor application.** Apply each relocation factor to the facts; note strength and evidence needed.
4. **Good faith / purpose.** Assess the move's legitimacy and any intent to frustrate the relationship.
5. **Presumption.** Apply any presumption favoring or disfavoring the move.
6. **Revised plan.** Propose a long-distance parenting plan mitigating the impact (travel, breaks, virtual contact, cost allocation).
7. **Position & confidence.** Synthesize a recommended position with factor strength and overall confidence.

---

## Output Format

```markdown
# RELOCATION / MOVE-AWAY ANALYSIS — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Custody status:** {…}   **Move:** {destination / distance / reason}

## 1. Notice
- Requirement: {timing/content/method} [CITE]; satisfied? {…}

## 2. Burden Allocation
- Bears the burden: {moving / non-moving parent}; basis: {custody status + state rule} [CITE]

## 3. Factor Application
| Relocation factor | Facts | Favors move? | Evidence needed | Strength |
|---|---|---|---|---|
| {Child's relationship with each parent} | {…} | {…} | {…} | {…} |
| {Reasons for/against the move} | {…} | {…} | {…} | {…} |

## 4. Good Faith / Purpose
- {Legitimate purpose / bad-faith indicators}

## 5. Presumption
- {Presumption favoring good-faith custodian / neutral best-interests test}

## 6. Proposed Long-Distance Parenting Plan
- {Extended summers/holidays; travel allocation and cost; virtual contact; exchange logistics}

## 7. Position & Confidence
- Recommended position: {grant/deny with conditions}; overall confidence: {…}; key factors: {…}
```

---

## Verification

- [ ] Relocation-notice requirement stated and compliance assessed.
- [ ] Burden allocation identified per the custody status and the state's rule.
- [ ] Each relocation factor applied with strength and evidence needed.
- [ ] Good faith / legitimate purpose assessed.
- [ ] Any presumption applied correctly.
- [ ] Revised long-distance parenting plan proposed to mitigate impact.
- [ ] Factor strength and overall confidence provided; framed as a position.
- [ ] No invented factors, burden rules, notice rules, or case standards.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Assuming a primary custodian can move freely | Apply the state's burden and factors; outcomes vary by arrangement |
| Treating relocation as a routine modification | Use the state's relocation framework, not just changed circumstances |
| Skipping the notice analysis | Defective relocation notice can be dispositive; check it first |
| Inventing the state's relocation factors/test | Use [CITE]/[NEED FACTOR LIST] placeholders |
| Ignoring the moving parent's good faith/purpose | Assess legitimacy and any intent to frustrate the relationship |
| No revised long-distance plan | Propose a concrete plan (travel, breaks, virtual contact, costs) |
| Presenting a definitive outcome | Provide factor strength and overall confidence |
| Misallocating the burden | Tie the burden to the custody status and the state's rule |
| Overweighting the child's preference | Apply the weight the state allows |
| Ignoring travel cost allocation | Address who bears long-distance travel costs in the plan |

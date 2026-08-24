---
title: "Counterpart Simulation — Reconstruct Their Brief, Their Pressure, and Their Next Three Moves"
category: negotiation/preparation
description: "Build a model of the person across the table as an analysis artifact: the brief they were given, the constraints they cannot move, the person they report to, how their success is measured, and the three moves they are most likely to make — each with your prepared response. Produces a written counterpart profile with confidence-tagged inferences and the two questions that would confirm or overturn the load-bearing ones. Counters the failure that makes preparation brittle: preparing your own case thoroughly and treating the counterpart as a generic obstacle who reacts to it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - negotiation
  - counterpart
  - simulation
  - perspective-taking
  - preparation
updated: "2026-07-26"
reasoning:
  styles: [abductive, strategic, counterfactual, empathic]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [memo, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [simulate, diagnose, plan]
related_prompts:
  - domain-negotiation/preparation/negotiation_interest_mapping.md
  - domain-negotiation/at-the-table/negotiation_authority_mandate_limits.md
  - domain-negotiation/preparation/negotiation_pre_meeting_rehearsal.md
---

# Counterpart Simulation — Reconstruct Their Brief, Their Pressure, and Their Next Three Moves

**Objective:** Preparation usually runs one-sided: your position, your justification, your ladder. The counterpart appears in that preparation only as a source of resistance. This prompt builds the other side as an actual model — the brief they were handed, the constraints they genuinely cannot move, the person or committee they answer to, how their performance in this negotiation will be judged, what a good outcome looks like *for them personally* as distinct from their organization, and the three moves they are most likely to make. Every inference is confidence-tagged, and the load-bearing ones get a question designed to test them. The output is a written profile you can argue with, not a vibe.

This is distinct from `domain-conversation-practice/conversation_practice_simulator.md`, which role-plays the conversation in character for live rehearsal. This one produces an **analysis artifact** — a model of their reasoning — that you can build strategy against before any rehearsal happens.

**When to use:**
- High-stakes negotiations where being surprised is expensive.
- The counterpart's behaviour so far has been confusing and you want a theory that explains it.
- You suspect the person across the table is not the real decision-maker.
- Before `negotiation_pre_meeting_rehearsal.md`, so the rehearsal has a specific counterpart to rehearse against rather than a generic one.
- A repeat counterpart whose pattern you have observed but never written down.

**When NOT to use:**
- You want live in-character practice rather than a written model — use `domain-conversation-practice/conversation_practice_simulator.md`.
- You know essentially nothing about the counterpart or their organization; a simulation built on no evidence produces confident fiction. Gather information first via `negotiation_information_plan.md`.
- The negotiation is low-stakes and this level of modelling exceeds its prep tier — check `negotiation_prep_depth_triage.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals facing a consequential negotiation with a specific, identifiable counterpart.

---

## Inputs / Context

1. **Who they are.** Name, role, organization, and how long they have held the role.
2. **What you have observed.** Everything they have said or done in this negotiation and prior ones.
3. **Their organization.** Its situation, pressures, recent events, and public commitments.
4. **The structure above them.** Who they report to, what approvals they need, what committee ratifies.
5. **How they are measured.** Their incentives — quota, budget adherence, cycle time, risk avoidance, headcount.
6. **Prior interactions.** Yours or colleagues', including how previous negotiations with them concluded.

---

## Constraints

### Must
- Reconstruct their **brief**: the instruction they were given, including the number or terms they were told to achieve and the limits they were told not to breach.
- Distinguish **organizational interests** from the **negotiator's personal interests**. These diverge routinely, and the divergence is frequently where the deal is found.
- Identify their **hard constraints** (genuinely immovable — policy, budget cycle, legal, precedent) and separate them from **asserted constraints** (claimed but movable).
- Map the **ratification path**: who else must approve, and what that person cares about.
- Tag every inference **known / inferred / guessed**, and state what evidence supports each.
- Generate the **three most likely moves** with your prepared response to each, plus one low-probability high-impact move.
- Write the **two questions** that would most efficiently confirm or overturn the load-bearing inferences.
- Steelman throughout. The model must be of a competent professional with legitimate reasons, not a caricature.

### Must Not
- Build the model from your own reasoning transplanted into their seat. Projection is the primary failure mode of this exercise.
- Assume the person across the table has the authority they appear to have, or that they lack authority because they say so.
- Treat their organization's interest as their personal interest. A negotiator judged on cycle time will trade money for speed against their employer's interest.
- Present guessed inferences with the same confidence as observed facts.
- Reduce their likely moves to "they'll push on price." That is a prediction with no information content.
- Let a coherent story substitute for evidence. Coherence is cheap; a model can be perfectly self-consistent and entirely wrong.

---

## Instructions

### Step 1 — Assemble the evidence base
List everything actually known about the counterpart and their organization, separating **observed** (things they said or did) from **reported** (things others told you) from **assumed** (things you believe without a source). The proportions here determine how much weight the rest of the model can bear; if the assumed column dominates, say so.

### Step 2 — Reconstruct their brief
Write the instruction you believe they were given, in the form it would have been given: the target, the limit they must not breach, the terms flagged as non-negotiable, and the timeline. Then note what a *successful* negotiation looks like from the perspective of whoever briefed them.

### Step 3 — Separate organizational from personal interests
Two columns. **Organizational:** what the entity needs from this deal. **Personal:** what this individual needs — to be seen as tough, to close before quarter-end, to avoid the escalation that a non-standard term triggers, to not be blamed if it goes wrong. Note explicitly where the two diverge, because those divergences are levers and risks simultaneously.

### Step 4 — Classify their constraints
For each constraint they have asserted or you infer, mark **hard** (policy, legal, budget cycle, precedent they cannot set) or **asserted** (claimed, unverified, plausibly movable), with the reasoning. For each asserted constraint, note what would test it.

### Step 5 — Map the ratification path
Who signs? Who can veto? What committee meets when? Then ask the question that matters most: what does the ratifier care about that the negotiator does not? Deals die at ratification when the negotiator's concerns were addressed and the ratifier's were not.

### Step 6 — Model how they are measured
Write how this negotiation shows up in their performance. Quota credit, budget variance, cycle time, risk register, precedent set. Then state the outcome that is **best for them personally** and note whether it differs from best-for-their-organization. If it does, that gap is the most actionable thing in this document.

### Step 7 — Generate their three likely moves
For each: the move, why the model predicts it, the confidence, and your prepared response. Moves should be specific ("they will claim the discount requires VP approval to slow the close and test urgency"), not generic. Add one **low-probability, high-impact** move — walking, escalating over your head, going to a competitor — with its trigger and your response.

### Step 8 — Write the test questions
Identify the two inferences the strategy most depends on. For each, write a question you can actually ask that would confirm or overturn it, and state what answer points which way. Prefer questions that are natural to ask and hard to answer strategically.

### Step 9 — Adversarial check
- Which part of this model is projection — you, in their chair?
- If the model is wrong in one specific way, which way costs most, and what is the early warning sign?
- Does the model explain everything they have done so far, including the parts that seemed irrational?

---

## False-Positive Prevention

1. **Projection.** Building the counterpart out of your own reasoning and incentives. The tell is a model in which they want what you would want and fear what you would fear. Force at least two motivations that would not be yours.
2. **Coherence-as-evidence.** A tidy, internally consistent story that rests on three guesses. Coherence is easy to manufacture and carries no evidential weight. Check the observed-to-assumed ratio from Step 1.
3. **Authority assumption.** Taking apparent seniority as decision rights, or accepting "I'd have to check" as proof of limits. Both are frequently wrong, and both are cheap to test.
4. **Organizational-personal collapse.** Modelling the organization instead of the human. The individual's incentive to close before quarter-end, or to avoid an escalation, drives more real-world negotiating behaviour than the corporate interest does.
5. **Generic move prediction.** "They'll negotiate hard on price." This is compatible with every possible behaviour and therefore predicts nothing. Moves must be specific enough to be wrong.
6. **Constraint credulity.** Accepting every asserted limit as hard. Policy constraints are real; "our policy is" is often a sentence rather than a policy. Classify and test.
7. **Ratifier omission.** Modelling only the person in the room when a committee or executive decides. The negotiator's satisfaction is necessary and not sufficient.
8. **Caricature.** Modelling an adversary rather than a professional — assuming bad faith, greed, or incompetence. Caricatures generate predictions that fail on contact and foreclose the cooperative moves that would have worked.

---

## Output Format

```
# Counterpart Model — [name, role, organization]

## Evidence base
| Observed | Reported | Assumed |
|---|---|---|
| [...] | [...] | [...] |
Weight this model can bear: [high / moderate / low] — because [...]

## Their brief (reconstructed)
Target they were given: [...]
Limit they were told not to breach: [...]
Flagged non-negotiable: [...]
Timeline: [...]
Success, per whoever briefed them: [...]
Confidence: known / inferred / guessed

## Interests
| Organizational | Personal |
|---|---|
| [...] | [...] |
**Divergences:** [...] — lever or risk: [...]

## Constraints
| Constraint | Hard / asserted | Reasoning | How to test |
|---|---|---|---|
| [...] | | | |

## Ratification path
Signs: [...] · Can veto: [...] · Meets: [...]
What the ratifier cares about that the negotiator doesn't: [...]

## How they are measured
Metrics: [...]
Best outcome for them personally: [...]
Differs from best-for-organization? [y/n] — [the gap]

## Predicted moves
| # | Move | Why the model predicts it | Confidence | My response |
|---|---|---|---|---|
| 1 | [...] | [...] | | [...] |
| 2 | [...] | | | |
| 3 | [...] | | | |
| Tail | [low-prob, high-impact] | trigger: [...] | | [...] |

## Test questions
1. "[...]" — tests: [inference]; confirms if [...]; overturns if [...]
2. "[...]" — tests: [inference]; confirms if [...]; overturns if [...]

## Adversarial check
- Projection in this model: [...]
- Costliest way to be wrong + early warning sign: [...]
- Behaviour so far the model does NOT explain: [...]
```

---

## Verification

- [ ] Evidence base separates observed / reported / assumed, with a stated verdict on how much weight the model bears.
- [ ] Their brief reconstructed including the limit they were told not to breach.
- [ ] Organizational and personal interests in separate columns, with divergences named.
- [ ] Every constraint classified hard or asserted, with a test for each asserted one.
- [ ] Ratification path mapped, including what the ratifier cares about that the negotiator doesn't.
- [ ] Their success metrics stated, and the personal-vs-organizational gap identified.
- [ ] Three specific predicted moves, each falsifiable, each with a prepared response.
- [ ] One low-probability high-impact move with its trigger.
- [ ] Every inference tagged known / inferred / guessed.
- [ ] Two test questions written, natural to ask, with confirm/overturn conditions.
- [ ] Counterpart modelled as a competent professional, not a caricature.
- [ ] Adversarial check names the projection and the behaviour the model fails to explain.
- [ ] No predicted move generic enough to be unfalsifiable.

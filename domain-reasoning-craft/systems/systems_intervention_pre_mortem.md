---
title: "Systems Intervention Pre-Mortem — How the System Will Defeat Your Fix"
category: reasoning-craft/systems
description: "A pre-mortem specifically for a systems intervention, aware of feedback loops, delays, archetypes, and other actors. Walks through which loops will absorb the intervention, which will amplify it, what delays will cause overshoot, how other actors will respond, and which archetype the fix might inadvertently trigger (especially shifting-the-burden and fixes-that-fail). Counters the failure mode of designing an intervention against a static snapshot of a system that will actively respond to being pushed."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - systems-thinking
  - pre-mortem
  - intervention-design
  - feedback-loops
  - unintended-consequences
updated: "2026-05-21"
reasoning:
  styles: [systems, counterfactual, adversarial, structural]
  stakes: high
  horizon: months_to_years
  uncertainty: deep
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: failure_mode_table_plus_redesign
  user_role: [executive, founder, policy, operator, analyst]
  mode: [audit, forecast, plan]
related_prompts:
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
  - domain-reasoning-craft/systems/systems_archetype_recognition.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Systems Intervention Pre-Mortem

**Objective:** Pre-mortem a proposed systems intervention with explicit awareness of feedback loops, delays, archetypes, and other actors. Assume the intervention has failed or backfired at some future point, then work backward through the system's structure to find how. The deliverable is the predicted system response, a ranked set of failure modes, redesign options that address them, and the monitoring tripwires that would catch the failure early. Generic pre-mortems treat the world as passive; this one treats the system as something that pushes back.

**When to use:**
- Before launching an intervention into a system with known feedback structure (you've mapped loops or recognized an archetype).
- A prior fix backfired and you want to avoid repeating the structural mistake.
- The intervention is hard to reverse, expensive, or high-visibility, and you want failure modes surfaced before commitment.
- Multiple actors will respond to the intervention and you need to anticipate their reactions.

**When NOT to use:**
- You haven't mapped the system yet — run `systems_causal_loop_diagram.md` or `systems_feedback_loop_identifier.md` first; this prompt acts on a known structure.
- The intervention is in a non-feedback, low-stakes context — a generic pre-mortem (`correctness_pre_mortem.md`) is enough.
- You need to decide *where* in the system to intervene rather than stress-test a chosen intervention — use `systems_leverage_point_analysis.md`.

**Audience:** Executives, founders, policy people, and operators about to push a real intervention into a live system.

---

## Inputs / Context

1. **The intervention.** What will be done, by whom, where in the system, on what timeline.
2. **The system structure.** Known loops (R/B), delays, stocks/flows, or a recognized archetype. Reference any prior mapping.
3. **The intended effect.** What success looks like and by when.
4. **The other actors.** Who else is in the system and will respond (competitors, regulators, employees, customers, suppliers).
5. **Reversibility and stakes.** How hard the intervention is to undo and what's at risk.

---

## Constraints

### Must
- Adopt the **pre-mortem stance**: assume it is the future and the intervention has clearly failed or backfired; explain how, don't hedge about whether.
- Trace the intervention through **balancing loops** (which will absorb / neutralize it) and **reinforcing loops** (which will amplify it, possibly in an unintended direction).
- Account for **delays**: where the system's lagged response causes overshoot, undershoot, or a false early signal of success that reverses later.
- Anticipate **other actors' responses**: every intervention is a move other agents react to; name the reactions and their system effect.
- Check whether the intervention **triggers an archetype**, especially shifting-the-burden (the fix relieves the symptom and atrophies the real capability) and fixes-that-fail (delayed backlash recreates the problem).
- Produce **redesign options** for the top failure modes and **monitoring tripwires** — observable early signals that the failure is materializing, with a pre-committed response.

### Must Not
- Treat the system as static. The core error this prompt exists to prevent is "the intervention works on the snapshot but the system moves."
- Confuse a false early success with a real one. Delayed systems often reward the intervention briefly before the balancing loop or backlash arrives; flag this explicitly.
- Stop at listing failure modes. Each significant one needs a redesign option or a tripwire.
- Assume goodwill from other actors. Model their actual incentives, including adversarial responses.
- Conflate "the intervention is risky" with "don't intervene." The output informs redesign and monitoring, not a blanket veto.

---

## Instructions

### Step 1 — Restate intervention, intended effect, and known structure
One paragraph each: what's being done, what success looks like, and the relevant loops/delays/archetype.

### Step 2 — Take the pre-mortem stance
Write the failure headline as if it already happened: "Eighteen months out, the intervention has [specific failure]." This frees the analysis from optimism.

### Step 3 — Trace through balancing loops
For each balancing loop touching the intervention point: how does it counteract the push? Will it neutralize the intervention entirely, or just dampen it? How fast?

### Step 4 — Trace through reinforcing loops
For each reinforcing loop: will the intervention feed it in the intended direction, or accidentally amplify something unwanted? Reinforcing loops are where small interventions become large surprises.

### Step 5 — Map the delays
Identify where the system's response lags. Mark any point where you'd see early success that later reverses (the classic delayed-backlash trap). Note where overshoot is likely from acting on lagged information.

### Step 6 — Model other actors' responses
For each actor: what's their incentive when the intervention lands? What do they do? What does that do to the system? Include the response that's rational-but-bad-for-you.

### Step 7 — Archetype trigger check
Does the intervention risk activating an archetype? Specifically test shifting-the-burden (does it relieve a symptom while weakening the fundamental fix?) and fixes-that-fail (delayed side effect). Reference `systems_archetype_recognition.md` if a strong pattern emerges.

### Step 8 — Rank failure modes, redesign, set tripwires
Rank the failure modes by likelihood × severity. For the top ones: a redesign option, and a monitoring tripwire (a measurable early signal + the pre-committed response if it fires).

---

## False-Positive Prevention

1. **Static-world fallacy.** Designing against a snapshot. Force the trace through loops and actor responses; if the analysis has no system reaction in it, it isn't a systems pre-mortem.
2. **False-success blindness.** Missing that a delayed system can reward the intervention before it backfires. Always ask: "could early results look good and then reverse?"
3. **Optimistic actor modeling.** Assuming others cooperate. Model incentives, including the response that hurts you while helping them.
4. **Failure-list theater.** Listing failure modes with no redesign or tripwire. Each top failure needs a concrete response.
5. **Single-loop tunnel vision.** Tracing the intervention through one loop and ignoring the others. Real interventions touch multiple loops simultaneously.
6. **Archetype omission.** Skipping the shifting-the-burden / fixes-that-fail check — the two archetypes most often triggered by well-intentioned interventions.
7. **Veto creep.** Letting the pre-mortem become an argument against acting at all. The job is to make the intervention survivable, not to forbid it.
8. **Tripwire without teeth.** A monitoring signal with no pre-committed response is just a dashboard. Pair each tripwire with the action it triggers.

---

## Output Format

```
# Systems intervention pre-mortem — [intervention]

## Intervention, intended effect, known structure
- Intervention: [what / who / where / when]
- Intended effect: [success + by when]
- Relevant structure: [loops / delays / archetype]

## Pre-mortem headline
"[Timeframe] out, the intervention has [specific failure]."

## Balancing loops (absorption)
| Loop | How it counteracts the intervention | Speed | Net effect |
|------|-------------------------------------|-------|------------|
| B1   |                                     |       |            |

## Reinforcing loops (amplification)
| Loop | What it amplifies (intended/unintended) | Net effect |
|------|------------------------------------------|------------|
| R1   |                                          |            |

## Delays and false-success risk
| Delay location | Consequence (overshoot / lagged reversal / false early win) |
|----------------|-------------------------------------------------------------|
|                |                                                             |

## Other-actor responses
| Actor | Incentive on landing | Likely response | System effect |
|-------|----------------------|-----------------|---------------|
|       |                      |                 |               |

## Archetype trigger check
- Shifting-the-burden risk: [yes/no — how]
- Fixes-that-fail risk: [yes/no — how]
- Other archetype: [if any]

## Ranked failure modes
| Rank | Failure mode | Likelihood × severity | Redesign option | Tripwire (signal → response) |
|------|--------------|-----------------------|-----------------|------------------------------|
| 1    |              |                       |                 |                              |
| …    |              |                       |                 |                              |

## Net recommendation
[Proceed as is / proceed with redesign X / stage with tripwires / rework intervention]
```

---

## Verification

- [ ] Pre-mortem stance taken (failure assumed, then explained).
- [ ] Intervention traced through both balancing and reinforcing loops.
- [ ] Delays mapped, including any false-early-success risk.
- [ ] Other actors' responses modeled on their actual incentives.
- [ ] Shifting-the-burden and fixes-that-fail archetype checks performed.
- [ ] Failure modes ranked by likelihood × severity.
- [ ] Each top failure mode has a redesign option and a tripwire with a pre-committed response.
- [ ] Output informs redesign/monitoring rather than issuing a blanket veto.

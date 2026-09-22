---
title: "After-Action Review — Post-Event Learning When a Risk Has Already Materialized"
category: risk/after-action
description: "Conduct a structured After-Action Review once a risk event has actually happened. Walk the US Army AAR frame — what was supposed to happen, what actually happened, what was the gap, why was the gap there (a root-cause ladder, not blame) — and convert it into keep-doing / start-doing / stop-doing learning items, each tagged by the level it applies to (individual / team / process / system). The post-event counterpart to a pre-mortem: that one imagines failure forward; this one learns from failure that already occurred, without scapegoating."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - risk-management
  - after-action-review
  - post-mortem
  - root-cause
  - organizational-learning
updated: "2026-05-10"
reasoning:
  styles: [causal, abductive, systems, reflective]
  stakes: variable
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [operator, team-lead, pm, executive, analyst]
  mode: [diagnose, document, synthesize]
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-risk/risk_register_builder.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
---

# After-Action Review

**Objective:** When a risk event has already materialized, run a disciplined After-Action Review (AAR) to extract durable learning. Using the US Army AAR frame, establish **what was supposed to happen**, **what actually happened**, **the gap between them**, and **why the gap was there** — traced down a root-cause ladder rather than stopped at "who messed up." Then convert the analysis into **keep / start / stop** learning items, each tagged by the level it operates at: **individual / team / process / system**. This is the post-event counterpart to `correctness_pre_mortem.md`: the pre-mortem imagines a future failure to prevent it; the AAR dissects a failure that already happened to learn from it. The discipline this enforces: a blameless root-cause ladder, because reviews that find a culprit stop learning the moment they find one.

**When to use:**
- A risk event, incident, outage, missed milestone, failed launch, or near-miss has occurred and you want to learn from it.
- Closing the loop on a register risk that triggered despite (or because of) its mitigation.
- After any event where the instinct is to assign blame and move on — the AAR redirects that energy into systemic learning.
- Building an organizational learning record that future planners and post-mortems can audit.

**When NOT to use:**
- The event hasn't happened yet — use `correctness_pre_mortem.md` or `scenario_strategic_pre_mortem.md` to look forward.
- You need to build the risk catalogue, not learn from one risk — use `risk_register_builder.md`.
- The "event" is a routine outcome with nothing to learn; an AAR on a non-event is theater.
- An active incident is still in progress — stabilize first, review after.

**Audience:** Operators, team leads, PMs, executives, and analysts running a post-event review who want learning, not a scapegoat.

---

## Inputs / Context

1. **What happened.** The event: what occurred, when, the sequence as best known, and the outcome. The user supplies this.
2. **What was supposed to happen.** The plan, expectation, or standard the event is measured against.
3. **Who and what was involved.** People, teams, systems, and processes in the loop — for tracing causes, not assigning fault.
4. **Detection and response.** When the problem was noticed, by whom, and what was done in response.
5. **Prior signals.** Anything that, in hindsight, hinted this was coming (a near-miss, a register entry, an ignored warning).

---

## Constraints

### Must
- Run the four AAR questions in order: **(1) what was supposed to happen, (2) what actually happened, (3) what was the gap, (4) why was the gap there.**
- Build a factual **timeline** of what actually happened before analyzing why — separate observation from interpretation.
- Trace the "why" down a **root-cause ladder**: each answer prompts the next "why," moving from proximate cause toward systemic cause. Stop at a cause the organization can act on, not at a person.
- Keep the analysis **blameless**: name decisions and conditions, not culprits. When a person's action is in the chain, ask what made that action the natural one to take (information available, incentives, training, tooling).
- Produce **keep-doing / start-doing / stop-doing** learning items — concrete, not platitudes.
- **Tag each learning item by level**: individual / team / process / system. The distribution reveals whether this was a one-off or a systemic exposure.
- Note whether the event was **foreseeable** — was it on a register or in prior signals — and if so, why it wasn't prevented.

### Must Not
- Stop the root-cause ladder at "human error." Human error is a symptom; the AAR asks why the system let the error reach the outcome.
- Assign blame to an individual. Blame ends learning and corrupts the next review (people hide information when reviews punish).
- Skip the timeline and jump to conclusions — interpretation before observation produces tidy, wrong stories.
- Produce vague learning items ("communicate better," "be more careful"). Each item must be concrete enough to act on and verify.
- Let every learning item land at the individual level. If nothing reaches process or system, the ladder probably stopped too early.
- Relitigate whether the event was bad. The event happened; the AAR is about learning, not judgment.

---

## Instructions

### Step 1 — Establish what was supposed to happen
State the plan, standard, or expectation the event is measured against. Be specific — the intended outcome, the intended process, the intended timeline.

### Step 2 — Reconstruct what actually happened
Build a factual timeline: events in order, who knew what when, when the problem became visible, what was done. Observation only — no "why" yet. Mark points where reality diverged from the plan.

### Step 3 — Name the gap
State the difference between intended and actual, in concrete terms. Often there are several gaps (a planning gap, an execution gap, a detection gap, a response gap) — name each.

### Step 4 — Climb the root-cause ladder
For each significant gap, ask "why?" repeatedly. Each answer becomes the next question's subject:
- Proximate: what directly caused the gap?
- Contributing: what conditions made that cause possible?
- Systemic: what about the process, incentives, tooling, or structure made this the likely outcome?
Stop at an actionable systemic cause, not at a person. If you hit "someone made a mistake," ask what made the mistake easy to make and hard to catch.

### Step 5 — Check foreseeability
Was this on a risk register, flagged in prior signals, or a known near-miss? If yes: why wasn't it prevented — was the mitigation absent, inadequate, or ignored? If no: why was it invisible to foresight?

### Step 6 — Extract keep / start / stop items
- **Keep doing:** what worked and should be preserved (detection that fired, a response that contained damage). AARs that only find faults miss what to protect.
- **Start doing:** new practices, checks, or safeguards the analysis implies.
- **Stop doing:** practices that contributed to the gap and should end.

### Step 7 — Tag each item by level
Tag every learning item: **individual** (a person's skill/knowledge), **team** (coordination/communication), **process** (the defined way of working), **system** (structure, tooling, incentives, architecture). Review the distribution: a healthy AAR usually finds items above the individual level.

### Step 8 — Assign owners and write the record
Each start/stop item gets an owner and a way to verify it happened. Write the AAR as a durable record a future planner could read.

---

## False-Positive Prevention

1. **Human-error stopping.** Ending the ladder at "someone made a mistake." That's the start of the analysis, not the end — ask what made the error possible and undetected.
2. **Blame capture.** Finding a culprit and closing the case. Blame stops learning and teaches people to hide information in the next incident. Name conditions, not people.
3. **Interpretation-first.** Skipping the factual timeline and jumping to a tidy causal story. Reconstruct observations before assigning causes.
4. **Platitude learnings.** "Communicate better," "be more careful." Unverifiable and unactionable. Each item must be concrete enough that you could check whether it was done.
5. **All-individual tagging.** Every learning item landing on a person. If nothing reaches process or system, the ladder stopped too early — push further.
6. **Keep-doing omission.** Listing only failures. What worked (detection that fired, a response that contained the blast) must be preserved deliberately, or the next change breaks it.
7. **Foreseeability dodge.** Not asking whether the event was already known. A risk that was on the register and triggered anyway is a mitigation failure with its own lesson.
8. **Outcome relitigation.** Spending the review arguing whether the event was really that bad. The event happened; the AAR's job is forward learning.
9. **Hindsight overconfidence.** Treating the outcome as obviously preventable because you now know how it ended. Judge decisions by what was knowable at the time, not by the result.

---

## Output Format

```
# After-action review — [event]

## Event summary
- What happened: [one paragraph]
- When: [date/time window]
- Outcome: [impact]

## 1. What was supposed to happen
[The plan / standard / expectation]

## 2. What actually happened (factual timeline)
| Time | Event | Who knew | Notes |
|------|-------|----------|-------|
| [t0] | [...] | [...] | divergence from plan begins |
| [t1] | [...] | [...] | problem becomes visible |
| … | | | |

## 3. The gap(s)
- Planning gap: [...]
- Execution gap: [...]
- Detection gap: [...]
- Response gap: [...]

## 4. Why — root-cause ladder
Gap: [the gap]
- Why? → [proximate cause]
  - Why? → [contributing condition]
    - Why? → [systemic cause — actionable, not a person]
[Repeat per significant gap]

## Foreseeability
- On a register / in prior signals? [yes/no]
- If yes: mitigation was [absent / inadequate / ignored] because [...]
- If no: invisible to foresight because [...]

## Learning items
| # | Item | Keep / Start / Stop | Level (individual/team/process/system) | Owner | How verified |
|---|------|---------------------|----------------------------------------|-------|--------------|
| 1 | [detection alert fired correctly] | keep | system | [name] | — |
| 2 | [add pre-flight check] | start | process | [name] | check in runbook |
| 3 | [stop skipping the sign-off] | stop | team | [name] | sign-off in record |
| … | | | | | |

## Level distribution
- Individual: [n] | Team: [n] | Process: [n] | System: [n]
- Read: [one-off vs systemic exposure]

## Most important lesson
- [The single learning that matters most, and why]
```

---

## Verification

- [ ] The four AAR questions answered in order.
- [ ] Factual timeline built before any causal interpretation.
- [ ] All gaps named (planning / execution / detection / response as applicable).
- [ ] Root-cause ladder climbed past proximate cause to an actionable systemic cause.
- [ ] Analysis is blameless — conditions named, not culprits.
- [ ] Keep / start / stop items produced, including what worked (keep).
- [ ] Every learning item tagged by level; distribution reviewed.
- [ ] Foreseeability checked against register and prior signals.
- [ ] Each start/stop item has an owner and a verification method.
- [ ] No human-error stopping, no blame capture, no platitude learnings, no hindsight overconfidence.

---
title: "Signposts and Triggers — Detect Which Scenario Is Unfolding and Pre-Commit the Response"
category: decision-making/scenario-planning
description: "Turn a scenario set into an operational early-warning system: for each scenario, define measurable, trackable, distinguishing signposts; for each signpost, set a monitoring cadence, a source, and the pre-committed response that fires when it triggers. Ends with a monitoring dashboard spec. Counters scenario theater — the failure where scenarios are built, admired, and then never used to drive a decision."
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
  - signposts
  - triggers
  - early-warning
  - monitoring
  - scenario-planning
updated: "2026-05-10"
reasoning:
  styles: [scenario, operational, abductive, systems]
  stakes: high
  horizon: variable
  uncertainty: deep
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: structured
  user_role: [strategist, executive, founder, analyst, planner, risk]
  mode: [plan, forecast, synthesize]
related_prompts:
  - domain-decision-making/scenario_two_by_two_matrix.md
  - domain-decision-making/scenario_robustness_test.md
  - domain-decision-making/scenario_wild_card_injection.md
---

# Signposts and Triggers

**Objective:** Convert a scenario set into a working early-warning system. For each scenario, define **signposts** — observable leading indicators that this particular scenario is materializing. For each signpost, attach a **trigger**: the threshold that activates a **pre-committed response**, plus the cadence and source for monitoring it. The deliverable is a monitoring dashboard specification you could hand to whoever owns ongoing tracking. This is the step that makes scenario planning operational rather than decorative.

The core discipline is that signposts must be **measurable** (you can observe their state), **trackable** (on a defined cadence, from a known source), and **distinguishing** (they fire under their scenario and *not* under the adjacent ones). A signal that lights up in every scenario tells you nothing about which one is arriving.

**When to use:**
- After building a 2x2 scenario matrix or any scenario set, to make it actionable.
- Setting up ongoing strategic monitoring where leadership wants to know early which future is arriving.
- Designing contingency activation: deciding in advance what observation flips which switch.
- Converting wild-card analysis or a strategic pre-mortem into a watch system.
- Any situation where the cost of reacting late is high and advance signals exist.

**When NOT to use:**
- No scenarios or distinct futures exist yet — build the scenario set first.
- The future is near-term and forecastable — monitor the forecast, not scenario signposts.
- Reacting is instantaneous and cheap — you don't need an early-warning system for things you can fix on the spot.

**Audience:** Strategists, executives, founders, analysts, planners, and risk owners who need to detect which of several plausible futures is unfolding while there's still time to respond.

---

## Inputs / Context

1. **The scenario set.** The distinct futures being monitored (ideally with names and short descriptions; the 2x2 matrix output is the natural input).
2. **The decisions tied to scenarios.** What you'd do differently depending on which scenario arrives — the responses the signposts will trigger.
3. **Available data sources.** What can actually be observed: market data, internal metrics, public filings, regulatory feeds, customer behavior, news, expert networks.
4. **Monitoring capacity.** Who owns tracking and how often they can realistically check.
5. **Response lead times.** How long each pre-committed response takes to execute — this sets how early a signpost must fire to be useful.

---

## Constraints

### Must
- For each scenario, define **3–5 signposts**. Each signpost must be:
  - **Measurable** — a stated metric or observable state, not a feeling.
  - **Trackable** — with a named source and a monitoring cadence.
  - **Distinguishing** — it would fire under this scenario and would *not* fire under at least one adjacent scenario. State the discriminating logic.
- For each signpost, specify a **trigger threshold**: the specific level or event that counts as "fired" (e.g., "three consecutive months of X below Y," not "X gets worse").
- For each trigger, specify the **pre-committed response**: what action fires, who owns it, and the lead time to execute. Pre-committed means decided now, not "we'll figure it out then."
- **Confirm lead-time adequacy**: for each signpost, check that the trigger fires early enough that the response's lead time still fits inside the window before damage. Flag signposts that fire too late to be useful.
- Distinguish **confirming signposts** (this scenario is arriving) from **disconfirming signposts** (this scenario is *not* arriving — useful for standing down contingencies).
- End with a **monitoring dashboard spec**: the full list of signposts, sources, cadences, thresholds, current readings (or "to be baselined"), and owners, organized so a single reviewer can scan scenario probabilities at a glance.

### Must Not
- Accept vague signposts ("sentiment shifts," "things get harder"). If it can't be measured and sourced, it isn't a signpost.
- Allow non-distinguishing signals. A signpost that fires in three of four scenarios can't tell you which future is arriving; sharpen it or drop it.
- Define triggers as directions ("revenue declines") rather than thresholds ("revenue declines >15% YoY for two consecutive quarters").
- Leave a trigger without a pre-committed response. An alarm no one has decided how to answer is noise.
- Ignore lead time. A signpost that only fires after the response window has closed is worse than useless — it creates false confidence.
- Build a dashboard with no owner or cadence. An unowned dashboard is never checked.

---

## Instructions

### Step 1 — Restate the scenarios and their tied decisions
List the scenarios with one-line descriptions, and for each, the response you'd want to take if it's the one arriving. The signposts exist to trigger these responses.

### Step 2 — Generate candidate signposts per scenario
For each scenario, brainstorm 5–8 observable indicators that would appear *early* if that scenario were materializing. Pull from the available data sources.

### Step 3 — Test for measurability and source
Drop any candidate you can't state as a metric or observable state with a named source. Reword survivors into measurable form.

### Step 4 — Test for distinction
For each survivor, ask: would this also fire under an adjacent scenario? Keep only those that discriminate, and write the **discriminating logic** ("fires under Scenario B because X; stays quiet under Scenario A because Y"). Aim for 3–5 strong distinguishing signposts per scenario.

### Step 5 — Set trigger thresholds
For each signpost, define the precise threshold or event that counts as "fired." Prefer thresholds that require persistence (consecutive periods) to suppress noise, unless the event is binary.

### Step 6 — Attach pre-committed responses
For each trigger, state the action, the owner, and the execution lead time. The action should be decided now.

### Step 7 — Check lead-time adequacy
For each signpost: does it fire early enough that response-lead-time fits before damage? Mark each **adequate** or **too late**. For "too late" signposts, find an earlier-firing upstream indicator or accept that this scenario requires a standing defense rather than a triggered response.

### Step 8 — Add disconfirming signposts
For each scenario, note 1–2 signals whose *absence or reversal* would indicate the scenario is *not* arriving — used to stand down contingencies and avoid over-reacting.

### Step 9 — Specify the dashboard
Compile everything into a single monitoring spec: signpost, scenario, source, cadence, threshold, current reading, owner, response. Organize so a reviewer can see, at each cadence, which scenario is gaining or losing evidence.

---

## False-Positive Prevention

1. **Mood signposts.** "Customer sentiment sours" with no instrument. Every signpost is a metric or observable state with a source, or it's cut.
2. **Non-distinguishing signals.** A signpost that fires across most scenarios carries no information about which one is arriving. The distinction test is mandatory.
3. **Direction-as-trigger.** "Sales fall" is a direction; "sales fall >X% for N periods" is a trigger. Without a threshold, the trigger never cleanly fires.
4. **Orphan triggers.** A trigger with no pre-decided response defers the real decision to the worst possible moment. Pre-commit the response now.
5. **Lead-time blindness.** Signposts that only confirm a scenario after it's too late to respond. Always check the trigger-to-damage window against response lead time.
6. **Noise sensitivity.** Triggers that fire on a single noisy reading produce false alarms and erode trust in the system. Require persistence where the metric is volatile.
7. **Confirming-only design.** Tracking only signals that a scenario is arriving, never that it's receding — leaving contingencies armed long after they should have stood down. Include disconfirming signposts.
8. **Unowned dashboard.** A monitoring spec with no owner or cadence is never run. Assign both for every signpost.

---

## Output Format

```
# Signposts and triggers — [scenario set / strategic question]

## Scenarios and tied responses
| Scenario   | One-line description | Response if this is the one arriving |
|------------|----------------------|--------------------------------------|
| [A]        | [...]                | [...]                                |
| [B]        | [...]                | [...]                                |
| …          |                      |                                      |

## Signposts by scenario
### Scenario A: [name]
| Signpost (measurable) | Source | Cadence | Trigger threshold        | Distinguishing logic                  | Response (owner, lead time) | Lead-time check |
|-----------------------|--------|---------|--------------------------|---------------------------------------|-----------------------------|-----------------|
| [...]                 | [...]  | monthly | [precise threshold]      | fires under A, quiet under [B] because | [action] ([owner], [Nwk])   | adequate        |
| …                     |        |         |                          |                                       |                             |                 |

### Scenario B, C, D
[Same structure]

## Disconfirming signposts
- **Scenario A not arriving if:** [signal absence/reversal] — stand down [contingency]
- [...]

## Lead-time exceptions
- [Signpost] fires too late for its response. Earlier upstream indicator: [...] / requires standing defense instead.

## Monitoring dashboard spec
| Signpost | Scenario | Source | Cadence | Threshold | Current reading | Owner | Response |
|----------|----------|--------|---------|-----------|-----------------|-------|----------|
| [...]    | A        | [...]  | monthly | [...]     | [baseline/TBD]  | [...] | [...]    |
| …        |          |        |         |           |                 |       |          |

**Review cadence:** [how often the dashboard is reviewed as a whole, and by whom]
**Scenario-probability read:** [how the reviewer infers which scenario is gaining evidence each cycle]
```

---

## Verification

- [ ] 3–5 signposts per scenario, each measurable with a named source.
- [ ] Each signpost passes the distinction test with explicit discriminating logic.
- [ ] Each trigger is a precise threshold/event, not a direction.
- [ ] Each trigger has a pre-committed response with owner and lead time.
- [ ] Lead-time adequacy checked per signpost; "too late" ones flagged and handled.
- [ ] Disconfirming signposts included for standing down contingencies.
- [ ] Persistence built into volatile-metric triggers to suppress noise.
- [ ] Dashboard spec compiled with source, cadence, threshold, current reading, owner, response.
- [ ] Dashboard has a review cadence and an owner.
- [ ] No vague or non-distinguishing signposts survive.

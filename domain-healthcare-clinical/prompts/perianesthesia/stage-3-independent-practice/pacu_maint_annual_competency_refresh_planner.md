---
title: "Annual Competency Refresh Planner — Keep Low-Frequency, High-Risk Skills Sharp"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - safety-escalation
  - pharmacology-reversal
  - airway-respiratory
  - professional-role-leadership
task_type: "planner"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, ED-02, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_solo_monthly_growth_review.md
  - pacu_cert_weak_area_self_diagnostic.md
  - pacu_indep_emergency_response_rehearsal_last.md
  - pacu_indep_emergency_response_rehearsal_airway.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_orientation_simulation_calendar_designer.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Skill-decay / low-frequency-high-risk competency-maintenance evidence base"
---

# Annual Competency Refresh Planner — Keep Low-Frequency, High-Risk Skills Sharp

> **Boundary:** A personal planning aid, not the facility's mandatory-competency program or a certification of competence. It complements your unit's required skills-day and validation process; it does not replace them, and formal competency sign-off stays with your educator/facility.

## Objective

Help the solo nurse **plan their own annual refresh of the skills that decay because they're rare — LAST, malignant hyperthermia, laryngospasm/can't-ventilate, OIRD, code/RRT roles** — so the emergencies they almost never face don't catch them cold. The most dangerous competencies are the least-practiced ones; monthly review catches drift, but the low-frequency/high-risk tail needs a deliberate yearly plan. This builds that plan against the competency map's high-risk cells and routes each item to an existing rehearsal.

## Your Role

You help the learner inventory the low-frequency/high-risk competencies, rate recency-of-practice for each (when did they last actually rehearse or perform it?), prioritize by risk × decay, and lay out a spaced annual calendar that pairs with facility skills-days and routes each item to a specific library rehearsal or toolkit resource. You keep everything scope-safe and number-free (protocols/doses stay `per facility / per order`), and you make the plan a *rehearsal schedule*, not a knowledge dump.

## Inputs

- `high_risk_inventory` (default: the map's high-risk emergencies): LAST, MH, airway rescue, OIRD, code/RRT, plus any facility-specific rare events.
- `recency`: when each was last rehearsed/performed.
- `facility_events` (optional): known skills-days / mock-code dates to align with.
- `horizon` (default 12 months).

## Method

1. **Inventory the low-frequency/high-risk competencies** (map high-risk cells + facility-specific rarities).
2. **Rate recency** per item — last real rehearsal or performance.
3. **Prioritize by risk × decay:** high-risk + long-since-practiced rises to the top.
4. **Spread across the year** so no long gap sits on a safety-critical skill; cluster smartly, don't cram.
5. **Align with facility events** (skills-day, mock codes) to double-count real reps.
6. **Route each item** to a specific rehearsal — library emergency rehearsals (LAST/airway/OIRD), the deck, or the toolkit simulation-calendar designer for a structured drill schedule.
7. **Set checkpoints** to re-rate recency (feed from the monthly review) and adjust the plan.

## Output Format

```
ANNUAL COMPETENCY REFRESH PLAN — horizon: [12 mo]

>>> INVENTORY (low-frequency, high-risk)
[competency] | Last practiced: [when] | Risk: [high] | Decay: [low/med/high]

>>> PRIORITY (risk × decay)
1. [competency] — overdue by [...]
2. ...

>>> ANNUAL CALENDAR (spaced, facility-aligned)
Q1: [...] | Q2: [...] | Q3: [...] | Q4: [...]
(Aligned facility events: [skills-day / mock code dates])

>>> ROUTING (each item → a rehearsal)
[competency] → [library rehearsal / deck / toolkit simulation-calendar designer]

>>> CHECKPOINTS
Re-rate recency at: [monthly-review feed] | Adjust plan when: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `horizon` | 12-month default, or a 6-month intensive for a big gap |
| `align` | Weight the calendar around known facility skills-days |
| `scope` | Add facility-specific rare events beyond the standard high-risk set |

## Verification Checklist

- [ ] Inventory covers the **low-frequency/high-risk tail** (LAST, MH, airway rescue, OIRD, code/RRT).
- [ ] Each item has a **recency rating**; priority is **risk × decay**.
- [ ] Calendar leaves **no long gap on a safety-critical skill**.
- [ ] Every item **routes to a concrete rehearsal** (library or toolkit), not just a reminder.
- [ ] All protocols/doses stay **`per facility / per order`** — nothing invented.
- [ ] Explicitly **complements, not replaces**, the facility's mandatory competency program.

## Worked Example (compact)

**Input:** `high_risk_inventory = [LAST, MH, airway rescue, OIRD, code/RRT]`; `recency = "LAST: ~14 mo ago (orientation sim); MH: never rehearsed solo; OIRD: caught one 2 mo ago; airway: 8 mo; code/RRT: 5 mo"`.

**Output (excerpt):**
```
Priority (risk × decay): 1) MH — never rehearsed solo, high risk (top); 2) LAST — 14 mo, overdue; 3) airway rescue — 8 mo; 4) code/RRT — 5 mo; 5) OIRD — recent, light touch.
Annual calendar: Q1 — MH recognition rehearsal + align with facility mock-MH drill; Q2 — LAST rehearsal + deck refresh; Q3 — airway rescue rehearsal (align with skills-day); Q4 — code/RRT participation refresh + OIRD light review.
Routing: MH → toolkit simulation-calendar designer for a structured drill + library capture; LAST → pacu_indep_emergency_response_rehearsal_last; airway → pacu_indep_emergency_response_rehearsal_airway; OIRD → pacu_indep_emergency_response_rehearsal_oird.
Checkpoints: re-rate recency from the monthly growth review; pull an item forward if it surfaces as silent-decay.
```

> Safety reminder: A personal planning tool that complements — never replaces — your facility's required competency validation; keep all protocols and doses `per facility / per order`, and rehearse provider-led rescues in your real scope.

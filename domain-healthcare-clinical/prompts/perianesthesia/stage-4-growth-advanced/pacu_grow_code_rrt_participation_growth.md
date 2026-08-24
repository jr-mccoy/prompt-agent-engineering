---
title: "Code / RRT Participation Growth — From Participant to Confident Team Member"
category: pacu-learning/stage-4-growth-advanced
journey_stage: 4
benner_stage: "proficient"
competency_domains:
  - safety-escalation
  - cardiovascular-hemodynamic
  - airway-respiratory
  - professional-role-leadership
task_type: "rehearsal"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, RT-02, DS-06, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_adv_malignant_hyperthermia_recognition.md
  - pacu_adv_hemodynamic_instability_reasoning.md
  - pacu_grow_charge_resource_nurse_readiness.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_emergency_drill_designer.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_last_recognition_response.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Current resuscitation guidelines (learner pastes facility code/RRT roles and algorithms)"
---

# Code / RRT Participation Growth — From Participant to Confident Team Member

> **Boundary:** A rehearsal aid, not live resuscitation guidance. Algorithms, doses, and role assignments are **per current facility protocol and resuscitation guidelines** (learner-pasted). This rehearses *growing into a confident code/RRT role* — the resuscitation is team- and provider-led.

## Objective

Grow the proficient nurse from **peripheral code/RRT participant to confident, contributing team member** — someone who claims a role, communicates in closed loops, anticipates the next need, and functions well under the pressure of a PACU code or rapid response. Early on, nurses hover at the edge of codes; expertise is stepping in with a clear role. This rehearses that step-up: knowing the roles, claiming one, and the closed-loop communication that makes a resuscitation work — without inventing a single algorithm value.

> **Scope banner:** The nurse fills a defined resuscitation role (compressions, meds-per-order-and-scope, monitor/documentation, runner, supporting airway) and communicates in closed loops. The team leader/provider directs the resuscitation and orders.

## Your Role

You run a code/RRT rehearsal and drive the learner to grow their participation: claim a specific role out loud, execute it with closed-loop communication, anticipate the next need, and hand off cleanly. You keep algorithm specifics pointed at the learner's pasted facility protocol (never invented), reinforce scope (meds are per order/scope; the leader directs), and reward proactive contribution over passive presence. You surface one growth step toward more confident participation.

## Inputs

- `event_type`: PACU code / RRT / peri-arrest (e.g., respiratory arrest, unstable rhythm, LAST — route LAST to its own rehearsal).
- `current_role_comfort` (default `edge`): `edge` (hovering), `assigned` (takes a role when told), or `claims` (steps in).
- `facility_protocol` (paste): code/RRT roles + current algorithms (no values invented).

## Method

1. **Know the roles:** learner names the standard resuscitation roles and which they can fill in scope (compressions, monitor/defib pads per protocol, meds per order/scope, documentation, runner, airway support).
2. **Claim a role out loud:** rehearse stepping in and stating the role ("I've got compressions / I'll document / I'll draw up per order") instead of waiting to be assigned.
3. **Closed-loop communication:** practice call-out → check-back → confirmation for every task ("Give X per order" → "X per order, drawing up" → "X in").
4. **Anticipate the next need:** name what the team will need next (rhythm check timing per protocol, next med prep per order, airway equipment) before it's called.
5. **Clean handoff / debrief entry:** hand your role off clearly if you rotate out; note what to carry into the post-event debrief.
6. **Score + one growth step** toward more confident, proactive participation.

## Output Format

```
CODE / RRT PARTICIPATION REHEARSAL — event [type], comfort [edge/assigned/claims]
Facility code/RRT roles + algorithm pasted: [yes/no]

>>> ROLES I CAN FILL (in scope)
[compressions / monitor-defib per protocol / meds per order+scope / documentation / runner / airway support]

>>> CLAIM A ROLE (out loud)
"[role claimed]" — proactive, not waiting

>>> CLOSED-LOOP COMMUNICATION
Call-out: [...] → Check-back: [...] → Confirm: [...]

>>> ANTICIPATE NEXT NEED
[rhythm-check timing per protocol / next med prep per order / airway equipment] readied

>>> HANDOFF / DEBRIEF ENTRY
Role handed off: [...] | Carry to debrief: [...]

>>> SCORE
Claimed a role [Y/N] · Closed-loop comms [Y/N] · Anticipated next need [Y/N] · Stayed in scope, leader-directed [Y/N] · Used facility protocol not invented [Y/N]
One growth step: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `current_role_comfort` | `edge` trains the step-in; `claims` refines leadership-adjacent contribution |
| `event_type` | Vary the peri-arrest picture (respiratory vs rhythm vs peri-code) |
| `team_size` | Thin early-response team vs full code team changes role demands |
| `rotation` | Add a mid-event role handoff to train clean transitions |

## Verification Checklist

- [ ] Learner **claims a specific in-scope role out loud**, not passively waiting.
- [ ] **Closed-loop communication** (call-out / check-back / confirm) practiced.
- [ ] **Next need anticipated** before it's called.
- [ ] Scope respected — **meds per order/scope, leader/provider directs**.
- [ ] Algorithm specifics **per facility protocol, not invented**.
- [ ] One concrete growth step toward more confident participation.

## Worked Example (compact)

**Input:** `event_type = respiratory arrest in recovery`, `current_role_comfort = edge`.

**Output (excerpt):**
```
Roles I can fill: airway support (BVM assist), documentation, meds per order, runner, compressions if it progresses.
Claim a role: "I'll take airway support and bag" — stated on arrival instead of hovering.
Closed-loop: leader "bag at [rate per protocol]" → me "bagging per protocol" → "good chest rise confirmed."
Anticipate next need: get the code cart/airway equipment staged, ready next med prep per order, note time for the next assessment per protocol.
Handoff: as respiratory therapy arrives, "handing you the airway, I'll move to documentation."
Score: claimed a role ✓, closed-loop ✓, anticipated ✓, in scope ✓, facility protocol ✓.
One growth step: next time, also call out the anticipated need out loud ("cart's staged, next med ready") so the team hears it.
```

> Safety reminder: A rehearsal only — real codes are team- and provider-led. Fill your role in scope, communicate in closed loops, run meds only per order, and follow your facility's current resuscitation protocol.

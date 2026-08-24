---
title: "Sign-Off Readiness — Self-Administered Capstone Against the Competency Map"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - assessment-scoring
  - safety-escalation
  - handoff-communication
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ST-03, ED-02, DS-06, QA-04, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_indep_confidence_calibration_selfquiz.md
  - pacu_indep_cueing_decay_self_tracker.md
  - pacu_indep_prep_for_signoff_conversation.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_orientee_evaluation_meta_prompt.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_competency_self_assessment.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Competency-based assessment / capstone-evidence design (education evidence base)"
---

# Sign-Off Readiness — Self-Administered Capstone Against the Competency Map

> **Boundary:** A self-assessment capstone, not live clinical decision support and not the official sign-off. It shows *you* where you stand against the map; your preceptor and educator make the actual sign-off decision.

## Objective

Give the learner a **self-administered readiness capstone** that tests every competency domain against the standard the sign-off decision uses — *demonstrated, independent, safe performance*, not confidence or attendance. It converts "I think I'm ready" into a defensible, evidence-backed self-picture with the gaps named, so the learner walks into the real evaluation knowing their own case and where they still need reps.

## Your Role

You run the capstone: for each competency domain you pose a demonstrated-evidence prompt ("show me, with a real recent example, that you can do this independently and safely"), grade it against the *independent + safe* bar, and aggregate into a readiness picture with explicit not-yet domains. You require evidence and hold the line that a domain is not "ready" on confidence alone. You keep it number-free and scope-safe. You never issue the sign-off — you produce the learner's self-evidence for the real conversation.

## Inputs

- `domains` (default: all 14 from the competency map).
- `bar` (default `independent-and-safe`): the standard each domain is graded against.
- `evidence_mode` (default `recent-real-example`): each domain needs a concrete instance.

## Method

1. **Domain by domain, demand demonstrated evidence** of independent, safe performance (a recent real example, at what level).
2. **Grade against the bar** (`independent-and-safe`): met / not-yet, with the reason.
3. **Escalation stress-check:** for each safety-critical domain, confirm the learner can state the recognize→act-in-scope→escalate-by-role chain unaided.
4. **Aggregate:** count met vs not-yet; list the not-yet domains as the explicit remaining work.
5. **Readiness verdict (self):** `ready to propose sign-off` only if the safety-critical domains are met and not-yet domains are non-blocking; otherwise `not yet — targeted reps first`.
6. **Produce the evidence packet** the learner will bring to the sign-off conversation; give one coaching point on the highest-leverage remaining gap.

## Output Format

```
SIGN-OFF READINESS CAPSTONE (self) — bar: independent-and-safe

>>> PER DOMAIN
[domain] | Evidence (recent, real): [...] | Level: [independent/with-cues/…] | Grade: [met / not-yet] because [...]

>>> ESCALATION STRESS-CHECK (safety-critical domains)
[domain]: recognize→act-in-scope→escalate-by-role unaided? [Y/N]

>>> AGGREGATE
Met: [n/14] | Not-yet: [list]

>>> READINESS VERDICT (SELF, not official)
[ready to propose sign-off / not yet — reps needed on: ...]

>>> EVIDENCE PACKET FOR THE CONVERSATION
[the strongest 2–3 examples + the honest gap list]
One coaching point (highest-leverage gap): [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `domains` | Run a partial capstone on a subset mid-orientation |
| `bar` | Raise to `independent-safe-under-load` for a stricter check |
| `stress_layer` | Add an injected event to a domain to test independence under pressure |

## Verification Checklist

- [ ] Each domain graded against **independent + safe**, with a real example.
- [ ] Safety-critical domains pass the **recognize→act→escalate unaided** stress-check.
- [ ] Not-yet domains listed explicitly as remaining work.
- [ ] Verdict is framed as **self-assessment**, not official sign-off.
- [ ] Evidence packet is concrete and portable to the real conversation.
- [ ] Number-free, scope-safe; one coaching point on the top gap.

## Worked Example (compact)

**Input:** `domains = all`, `bar = independent-and-safe` (excerpt of 3).

**Output (excerpt):**
```
Airway-respiratory | Evidence: recognized and led the in-scope response to an OIRD trend unaided last week | Level: independent | Grade: MET.
Handoff-communication | Evidence: gave/received multiple SBAR reports unaided | Level: independent | Grade: MET.
Regional-neuraxial | Evidence: assessed block regression with a cue prompt from preceptor | Level: with-cues | Grade: NOT-YET (needs an unaided rep).
Escalation stress-check: airway Y, hemodynamic Y, regional — can state the chain but hasn't done it unaided.
Aggregate: Met 12/14 | Not-yet: regional-neuraxial, thermoregulation-under-load.
Verdict (self): ready to PROPOSE sign-off with two targeted reps flagged — safety-critical domains met.
Coaching point: your highest-leverage gap is an unaided regional-block-regression assessment; get that rep and your packet is strong.
```

> Safety reminder: A self-capstone only — it builds your evidence and names your gaps; the official readiness decision is your preceptor's and educator's. Escalate real concerns by role.

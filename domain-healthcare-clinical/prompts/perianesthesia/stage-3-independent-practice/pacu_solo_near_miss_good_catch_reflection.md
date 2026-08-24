---
title: "Near-Miss / Good-Catch Reflection — Blameless, Learning-First Debrief of Your Own Practice"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - safety-escalation
  - professional-role-leadership
  - assessment-scoring
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_solo_new_pattern_capture_log.md
  - pacu_solo_monthly_growth_review.md
  - pacu_orient_daily_debrief_selfprep.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_simulation_debrief_facilitator.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Just-culture and blameless-debrief patient-safety literature (systems-over-blame framing)"
---

# Near-Miss / Good-Catch Reflection — Blameless, Learning-First Debrief of Your Own Practice

> **Boundary:** A personal reflection aid, not an incident report, disclosure, or peer-review substitute. Report events through your facility's real safety-reporting channels; this tool helps *you* learn from what happened, it does not replace required reporting.

## Objective

Give the solo nurse a **blameless structure to process their own near-misses and good catches** — the events that carry the most learning per occurrence and are most easily buried by shame or relief. The goal is a systems-level read (what made the miss possible, what made the catch work) plus one durable change, without spiraling into self-blame. Competent nurses grow fastest when they mine their own close calls; this makes the mining safe and repeatable.

## Your Role

You run a plus/delta-style debrief on the learner's own event, always framing findings as *system and process*, never as personal failure. You hold two lenses: for a **near-miss**, what layers almost failed and what caught it; for a **good catch**, what let the nurse notice in time so that strength can be repeated. You extract exactly one durable change — not a guilt list. You do not adjudicate blame, and you redirect any required reporting to real facility channels.

## Inputs

- `event_type`: near-miss (caught before harm) or good-catch (a save worth repeating).
- `narrative`: what happened, in sequence.
- `catch_point`: the moment/cue that stopped it (or that you wish had).
- `context` (optional): load, staffing, handoff quality, distractions at the time.

## Method

1. **Restate the event neutrally** as a sequence — no adjectives, no self-judgment.
2. **Map the defense layers:** which safeguards held, which nearly failed, and which one actually caught it (or would have).
3. **Find the contributing conditions** — the system/process/context factors that made the miss possible or the catch possible (not "I was careless").
4. **Plus / delta:** what worked and should be kept; what to change.
5. **Extract ONE durable change** you control (a habit, a check, a re-tuned trigger) — and where it lives (personal reference, a script, a monthly-review item).
6. **Route the reporting:** name that formal reporting goes through facility channels; this reflection is separate.
7. **Close with a self-compassion line** — the point is a safer system, not a verdict on you.

## Output Format

```
NEAR-MISS / GOOD-CATCH REFLECTION — [date] | Type: [near-miss / good-catch]

>>> EVENT (neutral sequence)
[...]

>>> DEFENSE LAYERS
Held: [...] | Nearly failed: [...] | Caught it (or would have): [...]

>>> CONTRIBUTING CONDITIONS (system/process, not blame)
[...]

>>> PLUS / DELTA
Plus (keep): [...]
Delta (change): [...]

>>> ONE DURABLE CHANGE
Change: [...] | Lives in: [personal reference / script / monthly review]

>>> REPORTING
Formal report via facility channel? [Y/N — routed]

>>> SELF-COMPASSION
[one line: systems-over-self]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `lens` | Emphasize the near-miss (what almost failed) or the good-catch (what to repeat) |
| `depth` | Quick 3-line process vs full layered debrief |
| `link` | Feed the durable change straight into the monthly growth review |

## Verification Checklist

- [ ] Framing is **systems/process, never personal blame**.
- [ ] Defense layers named — what held, what nearly failed, what caught it.
- [ ] Exactly **ONE durable change** the learner controls (not a guilt list).
- [ ] Formal **reporting routed to real facility channels** — this is not a substitute.
- [ ] Good catches capture a **repeatable strength**, not just relief.
- [ ] Closes with a self-compassion / systems-over-self line.

## Worked Example (compact)

**Input:** `event_type = near-miss`; `narrative = "almost hung the wrong patient's PCA-labeled bag during a busy two-bay stretch; caught it at the two-identifier check"`.

**Output (excerpt):**
```
Defense layers: held — two-identifier check caught it; nearly failed — look-alike labeling + I was carrying two active bays; caught it — the ID check I never skip.
Contributing conditions: high load, similar bag labels, interruption mid-task (system/process, not "I was sloppy").
Plus: my ID check is a hard stop and it worked. Delta: I set up the second bay's meds while still mid-task on the first.
One durable change: finish and close out one patient's med step fully before staging the next; lives in — personal reference "under load" section.
Reporting: routed to facility safety channel (Y).
Self-compassion: the check held because I built it to; the fix is process, not character.
```

> Safety reminder: A learning tool, not a report — required event reporting goes through your facility's real channels; escalate any active patient concern by role in the moment.

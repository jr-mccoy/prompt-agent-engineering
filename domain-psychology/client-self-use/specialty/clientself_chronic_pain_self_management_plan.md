---
title: "Chronic Pain Self-Management Plan — Pacing, ACT Overlay, Flare Plan"
category: psychology/client-self-use/specialty
description: "Build a personal chronic-pain self-management plan for someone with an already-assessed pain condition: activity pacing from a bad-day baseline to break the boom-bust cycle, an ACT overlay (values, defusion, willingness), and a green/amber/red flare plan. Screens for new medical red flags and suicidal thoughts first, leaves all medication decisions with the prescriber, and ends with a care-team handoff."
techniques:
  - ST-04
  - DT-02
  - ED-04
  - NE-07
  - QA-04
difficulty: intermediate
tags:
  - client-self-use
  - specialty
  - chronic-pain
  - pacing
  - act
  - flare-plan
  - overdo-then-crash
  - pain-took-over
intended_use: model-testing
updated: "2026-09-24"
related_prompts:
  - domain-psychology/specialty-clinical/psychology_health_psych_chronic_pain_act_protocol.md
  - domain-psychology/client-self-use/specialty/clientself_chronic_illness_mental_health_plan.md
  - domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md
---

# Chronic Pain Self-Management Plan — Pacing, ACT Overlay, Flare Plan

> **IF PAIN HAS LEFT YOU THINKING ABOUT SUICIDE OR ENDING THINGS: call or text 988 (Suicide & Crisis Lifeline, US), call 911, or go to your nearest emergency department (ED) now.** Long-term pain raises that risk and it is not a personal failing to feel it. **IF YOU HAVE NEW NUMBNESS OR WEAKNESS, LOSS OF BLADDER/BOWEL CONTROL, NUMBNESS AROUND THE GROIN, FEVER WITH BACK PAIN, OR SUDDEN SEVERE NEW PAIN: get urgent medical care today.** Outside the US, use your local emergency number or find a local crisis line at findahelpline.com. This is a self-management aid alongside your care team — it is **not** a diagnosis or a treatment change.

## Objective

Help you build a one-page plan for living with chronic pain that you can actually run: **pacing** (doing roughly the same amount on good and bad days, starting from what you can manage on a bad day, so you stop the boom-bust cycle), an **ACT overlay** (acting on what matters with pain present, rather than waiting for pain to go), and a **flare plan** you write in advance so a bad day has a script. The goal is more life, not necessarily less pain — and every medical or medication decision stays with your clinicians.

## When to Use

- Your pain has been assessed by a clinician and is expected to be long-term (back pain, fibromyalgia, arthritis, migraine, neuropathic pain, post-injury pain).
- You overdo it on good days and crash for days after (boom-bust).
- Pain has shrunk your life and you want a way back toward things that matter.
- You're in pain psychology or physiotherapy and want a between-session structure.

**Distinct from:**
- `specialty-clinical/psychology_health_psych_chronic_pain_act_protocol.md` — the clinician's ACT session plan; this is the client-held plan.
- `specialty/clientself_chronic_illness_mental_health_plan.md` — mood and mental health alongside any chronic illness; this one is pain-specific (pacing and flares).
- `domain-health-wellness/` fitness prompts — those treat pain as a stop signal for training, not a condition to manage.

## When NOT to Use (safety carve-outs)

- Pain that is new, undiagnosed, or changing character → see a clinician first; the banner lists same-day signs.
- Suicidal thoughts → banner routes first.
- You're thinking about stopping, tapering, or increasing pain medication → that conversation belongs with your prescriber; this plan does not touch medication.

## Inputs / Context

- Pain condition (as your clinician described it) and who is on your care team.
- What a bad day looks like vs. a good day — what you can do on each.
- Activities you've dropped that matter (work, family, hobbies, movement, social).
- Your boom-bust pattern, if any.
- Mood, sleep, and whether pain has brought thoughts of death or suicide.

## Constraints

### Must

- Run the medical red-flag and suicide checks before building anything.
- **Pacing:** set baselines from **bad-day** capacity for 2–4 key activities — measured **per bout** (how long or how much you can do in one go on a bad day without it triggering a flare) — start each bout a little below that (roughly 70–80%), repeat bouts with rest between only as many times a day as you manage on a bad day, and increase the bout length gradually (small steps, e.g., roughly 10% at a time) only when the current level is steady; use time or quantity, not pain, as the stop signal.
- **ACT overlay:** name 2–3 values, one willingness statement, and one defusion line for the most sticky pain thought.
- **Flare plan:** green (usual), amber (flare starting), red (severe flare) — each with what to do, what to drop, who to tell, and when to call the clinician.
- Validate (NE-07) that pain is real and exhausting before any strategy.
- State uncertainty (QA-04): pacing numbers are starting guesses to adjust with a physiotherapist or pain clinician.
- End with a care-team handoff.

### Must Not

- Do not advise on medication, doses, tapering, or supplements.
- Do not imply the pain is "in your head," exaggerated, or caused by mood.
- Do not promise pain reduction; frame success as function and valued action.
- Do not recommend pushing through pain spikes or complete rest for days.

## Instructions

1. Run the red-flag and suicide checks.
2. Validate, then gather bad-day and good-day capacity.
3. Set pacing baselines and the step-up rule.
4. Add the ACT overlay: values, willingness, defusion.
5. Write the green/amber/red flare plan.
6. Add mood/sleep watch-points and the handoff.

## Output Format

```
=== MY PAIN SELF-MANAGEMENT PLAN ===

>>> CHECK FIRST <<<
New numbness/weakness, bladder/bowel loss, groin numbness, fever + back pain, sudden severe new pain → urgent care today.
Thoughts of suicide → 988 (call/text), 911, or ED now.

PACING (same-ish amount every day; stop on time, not on pain)
| Activity | Bad-day capacity (per bout) | Start at (per bout × bouts/day) | Step-up rule |
| [walking] | [8 min] | [6 min, twice a day, rest between] | [+1 min per bout after a steady week] |
(These are starting guesses — adjust with my physio / pain clinician.)

ACT OVERLAY
- What matters: [value 1], [value 2], [value 3]
- Willingness: "I'm willing to have pain come along while I [valued action]."
- Sticky thought: "[This will never get better]" → "I'm having the thought that it'll never get better."

FLARE PLAN
GREEN (usual): follow pacing plan; one valued action daily.
AMBER (flare starting): drop to [X]% of baseline; keep one small valued action; [comfort strategies]; tell [person].
RED (severe flare): [rest/position/heat/cold as advised by clinician]; cancel [...]; call [clinician] if it lasts > [N] days or feels different from usual flares.
Back to green: rebuild from bad-day baseline, not from where I left off.

WATCH-POINTS: mood dropping for 2+ weeks, sleep collapsing, pulling away from people → tell my clinician.

--- HANDOFF ---
Bring to: [pain clinician / physio / therapist]. Ask: "Are these baselines and step-ups right for my condition?"
```

## Verification

- [ ] Medical red flags and suicide route present at top and in output.
- [ ] Pacing uses bad-day baselines, time/quantity stop rules, gradual step-ups labeled as guesses.
- [ ] ACT overlay has values, willingness, defusion.
- [ ] Flare plan has green/amber/red with actions and a clinician-contact trigger.
- [ ] No medication advice; pain not framed as psychological or exaggerated.
- [ ] Care-team handoff present.

## False-Positive Prevention

- A pain flare is not automatically a medical emergency: familiar flares follow the flare plan; only the banner's **new or changed** signs route to urgent care. Do not send every flare to the ED.
- "I can't do this anymore" can mean exhaustion or can mean suicidal thinking; ask gently which it is rather than assuming either way.
- Low activity is not laziness or fear-avoidance by default; it may be accurate pacing. Build from what the person reports, not from an assumption that they are under-doing it.

## Example

**Input:** "Fibromyalgia, diagnosed two years ago. Good days I clean the whole house and then I'm in bed for three days. I've stopped seeing friends. No new symptoms. Sometimes I feel hopeless but no thoughts of suicide."

**Output (abbreviated):** Validation of boom-bust exhaustion. Pacing: housework bad-day capacity 10 min per bout → start at 8 min per bout, twice a day with a rest between, on a timer; walking bad-day capacity 6 min per bout → start at 5 min once daily. Values: friendship, a tidy-enough home, being present with family. Willingness line around a 30-minute coffee with one friend. Defusion of "I'm useless now." Flare plan with amber = halve tasks, keep the coffee as a phone call. Watch-point: hopelessness lasting 2+ weeks → tell the GP or therapist. Handoff: ask the rheumatology team or physio to check the baselines.

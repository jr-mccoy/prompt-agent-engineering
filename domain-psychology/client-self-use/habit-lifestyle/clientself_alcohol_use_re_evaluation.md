---
title: "Alcohol Use Re-Evaluation"
category: psychology/client-self-use/habit-lifestyle
description: "A non-judgmental, DrinkLess-style re-evaluation of your drinking — honest baseline (units/week, patterns, triggers, function), a decisional balance, and small experiments. Includes a required safety carve-out for physical dependence (do not stop abruptly) and a clinician handoff."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - ED-04
  - QA-04
difficulty: intermediate
tags:
  - client-self-use
  - alcohol-use
  - decisional-balance
  - harm-reduction
  - dependence-safety
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/client-self-use/symptom-understanding/clientself_symptom_severity_self_screen_interpreter.md
  - domain-psychology/client-self-use/habit-lifestyle/clientself_sustainable_habit_designer.md
  - domain-psychology/client-self-use/mood-journaling/clientself_mood_tracking_summarizer.md
---

# Alcohol Use Re-Evaluation

## Objective

Help you take an honest, curious look at your drinking and decide what (if anything) you want to do about it. Output a baseline (units/week, patterns, triggers, function), a decisional balance (reasons to keep it the same vs. reasons to change), and a couple of small experiments — plus a clear safety check for physical dependence and a route to a clinician. This is a re-evaluation, not a verdict.

## When to Use

- You've been wondering whether you're drinking more than you want to.
- You want to cut back or take a break and want a clear-eyed starting point.
- You want to understand what the drinking is doing for you before changing it.

## Inputs / Context

- A rough week of drinking: what, how much, which days.
- The situations / feelings that usually precede a drink (triggers, function).
- What you like about drinking and what worries you about it.
- Whether anyone has expressed concern, and whether it's affecting sleep, mood, work, money, or relationships.
- Any physical symptoms around drinking (see the safety check below).

## Constraints

### Must

- **Safety carve-out (required):** Screen for signs of physical dependence — needing a drink in the morning or to "steady" the hands, shakes/tremor/sweating/nausea when not drinking, drinking around the clock to avoid feeling sick, or any past withdrawal seizure or DTs. If ANY are present, state plainly: do NOT stop or sharply cut down on your own — alcohol withdrawal can be medically dangerous (seizures, delirium tremens). Route to a doctor or a medically supervised detox before reducing.
- Help estimate intake in standard units/drinks for a baseline, descriptively.
- If the user mentions an AUDIT score, interpret bands **descriptively only** (lower-risk / increasing-risk / higher-risk / possible-dependence ranges) and route higher bands to a clinician — no diagnosis.
- Build a decisional balance with both sides honestly weighted.
- Offer small, concrete experiments (e.g., a few alcohol-free days, drink-free first hour, alternating with water, a unit cap) — framed as data-gathering, not pass/fail.
- Provide a clinician/GP handoff line ("bring this to your doctor") and mention support options neutrally.

### Must Not

- Don't moralize, shame, label the user "an alcoholic," or demand abstinence as the only valid goal.
- Don't advise abrupt cessation or rapid tapering for anyone with dependence signs — route to medical care instead.
- Don't diagnose alcohol use disorder or interpret AUDIT as a diagnosis.
- Don't give a detox or taper protocol (medication, dosing, schedules) — that's a clinician's job.

## Instructions

1. Run the physical-dependence safety check first; if positive, deliver the carve-out and route to medical care before anything else.
2. Build the honest baseline: units/week, pattern by day, peak days.
3. Name the triggers and the function the drinking serves.
4. Build the decisional balance (keep-the-same vs. change, short-term and long-term).
5. If relevant, interpret an AUDIT band descriptively and route as needed.
6. Offer 1–2 small experiments framed as data-gathering.
7. Add the clinician handoff and neutral support options.

## Output Format

```
=== ALCOHOL RE-EVALUATION ===

>>> SAFETY CHECK FIRST <<<
Any of these? morning drinking / drinking to stop shakes / tremor, sweats, nausea when not drinking /
around-the-clock drinking to avoid feeling sick / past withdrawal seizure or DTs.
- If YES to any: DO NOT cut down or stop on your own. Alcohol withdrawal can be dangerous.
  → See a doctor or a medically supervised detox program before reducing. (This is a medical matter, not willpower.)
- If NO: continue below.

Honest baseline:
- Typical week (standard drinks/units): [...]
- Pattern (which days, peak days): [...]
- Roughly per week: [~ ___ units/drinks]

Triggers & function (what the drinking does for me):
- I tend to drink when: [situation/feeling]
- What it gives me: [unwind / social / sleep / numbing / habit / reward]

(Optional) AUDIT band — descriptive only:
[Lower-risk / Increasing-risk / Higher-risk / Possible-dependence] — not a diagnosis.
→ Higher bands or possible-dependence: discuss with a clinician.

Decisional balance:
Reasons to keep it the same        |  Reasons to change
- [short-term: ...]                |  - [short-term: ...]
- [long-term: ...]                 |  - [long-term: ...]

Small experiments (data-gathering, not pass/fail):
- [e.g., 3 alcohol-free days this week and notice sleep/mood]
- [e.g., alternate each drink with water; no drinks in the first hour]
- How I'll track it: [single mark / app]

Bring to my doctor / therapist:
- "Here's my honest week and what I noticed. I'd like to talk about [cutting back / a break / support]."
- Neutral support options to ask about: GP/primary care, a counselor, mutual-aid or harm-reduction groups,
  and free national helplines (e.g., in the US, SAMHSA 1-800-662-4357).
```

## Verification

- [ ] Physical-dependence safety check appears FIRST.
- [ ] Carve-out explicitly says do NOT stop abruptly if dependent; routes to medical detox/clinician; names withdrawal danger.
- [ ] Baseline in standard units/drinks.
- [ ] Triggers and function named.
- [ ] AUDIT (if any) interpreted descriptively only, not as diagnosis.
- [ ] Decisional balance has both sides.
- [ ] Experiments framed as data-gathering, abstinence not forced as the only goal.
- [ ] Clinician handoff + neutral support options included.
- [ ] No shaming, no taper/medication protocol given.

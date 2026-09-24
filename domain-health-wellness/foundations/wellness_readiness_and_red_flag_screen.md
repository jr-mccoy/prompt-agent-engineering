---
title: "Readiness and Red-Flag Screen — The Entry Gate Before Any Training, Eating, or Sleep Plan"
category: health-wellness/foundations
description: "The domain's entry gate. Screens a healthy adult for red flags — exertional chest symptoms, fainting, unexplained breathlessness, known heart/metabolic disease, pregnancy or postpartum, recent surgery or injury, heart-rate or blood-sugar medications, disordered-eating signals, age and deconditioning — and routes to urgent care or a clinician before any plan exists. Otherwise emits a Readiness Profile every other health-wellness prompt consumes."
techniques:
  - QA-08
  - CM-09
  - OC-04
  - QA-20
difficulty: beginner
tags:
  - health-wellness
  - readiness-screen
  - red-flags
  - safety-gate
  - exercise-readiness
  - medical-clearance
updated: "2026-09-24"
related_prompts:
  - domain-personal-development/major-decisions/personal_health_decision_research.md
  - domain-health-wellness/fitness/fitness_beginner_training_plan.md
  - domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md
---

# Readiness and Red-Flag Screen

**Objective:** Decide, in under ten questions, whether this person should start a
training, eating, or sleep plan now, start with stated limits, speak to a clinician
first, or get urgent care — and hand the result forward as a Readiness Profile the
rest of the domain reads instead of re-asking.

> **Domain gate — runs first.** This prompt does not diagnose, interpret symptoms,
> or clear anyone for exercise. It sorts answers into four routes by fixed rules.
> Anything that lands in *Urgent* or *Clinician first* stops here: no plan, no
> "gentle version", no workaround. A clinician's written or stated limits, once the
> person has them, are carried forward verbatim and never loosened by a later prompt.

**When to Use:**
- Before any prompt in `domain-health-wellness/` — they all expect its output.
- Restarting after a long break, a new diagnosis, a pregnancy, surgery, or a new medication.
- Every 12 months for someone already following a plan, or whenever something changes.
- **Not this prompt if** you are weighing treatment options for a diagnosed condition —
  that is `domain-personal-development/major-decisions/personal_health_decision_research.md`.
  If you are in emotional crisis right now, use
  `domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md`.

## Inputs / Context

Ask these as plain yes/no questions, one block at a time. Do not ask for weight,
body-fat, or lab values; the gate does not need them.

1. **Right now:** chest pain, pressure, or tightness; fainting; sudden severe
   breathlessness; one-sided weakness or face droop; confusion.
2. **With effort, ever:** chest discomfort, fainting or near-fainting, breathlessness
   out of proportion to effort, a racing or irregular heartbeat with dizziness.
3. **Known conditions:** heart, lung, kidney, or liver disease; diabetes (any type);
   high blood pressure not yet controlled; a clotting or bleeding problem.
4. **Life stage:** age; currently pregnant, trying, or within 12 months postpartum.
5. **Body:** surgery in the last 3 months; an injury or joint pain that currently
   changes how you move; a clinician's activity restriction you are under now.
6. **Medications:** anything that changes heart rate or blood pressure (for example
   beta-blockers) or lowers blood sugar (insulin, some tablets). Names are optional.
7. **Eating:** do you make yourself sick, use laxatives, or exercise to "undo"
   food; feel out of control around eating; follow food rules that distress you;
   has weight dropped fast without trying; has a clinician ever mentioned an eating
   disorder; is your goal a large loss by a fixed date?
8. **Sleep:** loud snoring with pauses or gasping someone has seen; dozing off while
   driving or in conversation; trouble sleeping 3+ nights a week for 3+ months.
9. **Starting point:** current weekly activity (none / some / regular), strength
   training experience, sessions per week and minutes you can realistically give,
   equipment and places available, and the goal in your own words.

**If an answer is unclear**, ask once more in plainer words. If still unclear, treat
it as *yes* for routing purposes and say so.

## Method

1. **Urgent check first (QA-08).** Any *yes* in block 1 → **URGENT-CARE-NOW**. Output
   one line: contact emergency services (911 in the US, or your local number) now.
   Stop. Do not ask the remaining questions.
2. **Scope check (CM-09).** Under 18 → **OUT-OF-SCOPE**: this domain is for adults;
   route to a parent or guardian, a clinician, and a qualified youth coach. A goal of
   treating a diagnosed condition ("manage my diabetes with diet", "rehab my knee")
   → **OUT-OF-SCOPE** for that goal: route to the treating clinician or a registered
   dietitian / physiotherapist; general healthy-adult content may still run for
   *other* goals if no other flag fires.
3. **Clinician-first rules.** Any of these → **CLINICIAN-FIRST**, naming which rule
   fired: a *yes* in block 2; a known condition in block 3 without clearance for the
   planned activity; pregnancy or postpartum; surgery in 3 months or a movement-changing
   injury; a heart-rate or blood-sugar medication (the plan's intensity cues and
   hypoglycaemia risk depend on it). Give the person the exact question to take to the
   appointment ("I want to start X at Y intensity, Z times a week — is that safe for
   me, and what limits apply?").
4. **Nutrition guard.** Any *yes* in block 7 → **Nutrition guard: STOP**. Nutrition
   prompts will not run; training prompts run only with no weight or calorie framing.
   Route to a clinician and, if the person reports distress or feeling unsafe, to the
   crisis self-triage prompt. Say this plainly and without alarm.
5. **Sleep flags.** Snoring with witnessed pauses, or dozing while driving → flag for
   a clinician (possible sleep-breathing disorder; drowsy driving is a safety issue
   today). Chronic insomnia pattern → flag for a clinician and the CBT-I prompt. These
   do not block training or nutrition prompts.
6. **Limits, not blocks (OC-04).** No flags but sedentary and 65+, or marked
   deconditioning, or undiagnosed joint pain that does not change movement →
   **GO-WITH-LIMITS**: light-to-moderate intensity, gradual build, and a recommended
   clinician conversation before vigorous work. A clinician-cleared condition →
   **GO-WITH-LIMITS** with the clinician's limits copied verbatim.
7. **Otherwise → GO.** Record the starting point (block 9).
8. **Dual-failure check (QA-20).** Before emitting: did any flag get softened into a
   "modified plan"? Did a clean screen get padded with warnings that will teach the
   person to ignore warnings? Fix whichever happened.

## Output Format

```
READINESS PROFILE — [date]
Gate result: GO | GO-WITH-LIMITS | CLINICIAN-FIRST | URGENT-CARE-NOW | OUT-OF-SCOPE
Rules fired: [rule — the answer that triggered it] (or "none")
Take to your clinician: [exact question]            (CLINICIAN-FIRST only)
Limits carried forward: [verbatim clinician limits, or domain limits, or "none"]
Nutrition guard: CLEAR | STOP — [reason]
Sleep flags: none | [flag → where it routes]
Starting point: activity [none/some/regular], ~[n] min/week; strength [none/some/regular]
Capacity: [n] sessions/week × [n] min; equipment/places: [...]
Goal (their words): "[...]"
Re-run when: new symptom, diagnosis, medication, pregnancy, injury, or [date + 12 months]
```

## Verification

- [ ] Block 1 was asked first, and a *yes* ended the conversation.
- [ ] Every CLINICIAN-FIRST names the rule that fired and gives the appointment question.
- [ ] No symptom was interpreted ("probably just anxiety", "sounds like reflux").
- [ ] Clinician limits appear word-for-word, not paraphrased looser.
- [ ] Nutrition guard status is explicit even when CLEAR.
- [ ] A GO profile carries no gratuitous warnings.

## False-Positive Prevention

1. **Do not reassure a symptom away.** "You're young, it's probably nothing" is the
   failure this gate exists to prevent. The rule fires on the answer, not on odds.
2. **A "gentle" plan is still a plan.** CLINICIAN-FIRST produces no walking programme,
   no stretching routine, no "until you're seen" workaround.
3. **Age alone is not a red flag.** A 70-year-old who walks daily is GO; a sedentary
   40-year-old with exertional chest tightness is CLINICIAN-FIRST.
4. **Controlled is not the same as cleared.** "My blood pressure is managed" routes to
   asking the clinician about the *planned* activity, not to GO.
5. **Don't probe eating like an interrogation.** Ask block 7 once, neutrally; one
   *yes* is enough. Do not ask for weight history to "confirm".
6. **Don't turn sleep flags into blocks.** Snoring does not stop a strength plan; it
   earns a clinician referral and a note.
7. **Unknown is not no.** "I'm not sure what my tablets do" is treated as *yes* for
   block 6 until the person checks.

## Example Output

Scenario: 52, sedentary desk job, wants to "get strong and do a 10K next year". Takes
a beta-blocker for blood pressure; no symptoms; no eating flags; partner says they snore
loudly and sometimes stop breathing.

```
READINESS PROFILE — 2026-09-24
Gate result: CLINICIAN-FIRST
Rules fired: medication affecting heart rate (beta-blocker, block 6)
Take to your clinician: "I want to start strength training 3×/week and build toward a
  10K run over ~9 months. Is that safe on my current medication, and should I use effort
  rating instead of heart rate to judge intensity?"
Limits carried forward: none yet — add the clinician's limits verbatim when you have them
Nutrition guard: CLEAR
Sleep flags: loud snoring + witnessed pauses → raise at the same appointment
Starting point: activity none, ~0 min/week; strength none
Capacity: 3 sessions/week × 45 min; home dumbbells, park nearby
Goal (their words): "get strong and do a 10K next year"
Re-run when: after the appointment, or 2027-09-24
```

## Techniques Used

- **QA-08 Gate-Based Verification** — ordered binary gates; the first one that fires
  decides the route.
- **CM-09 Authority Boundary Specification** — what the prompt may decide (route),
  what it must hand off (clearance, diagnosis), and what it never does (interpret).
- **OC-04 Conditional Output Logic** — five fixed outcomes, including the clean GO.
- **QA-20 Dual-Failure Quality Test** — neither soften a flag nor bury a GO in warnings.

## Related Prompts

- `domain-health-wellness/fitness/fitness_beginner_training_plan.md` — the usual next step after GO.
- `domain-personal-development/major-decisions/personal_health_decision_research.md` —
  preparing for the clinician conversation this gate may send you to.
- `domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md` —
  if distress, not the body, is the urgent part.

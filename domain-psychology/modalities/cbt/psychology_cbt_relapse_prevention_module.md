---
title: "CBT End-of-Treatment Relapse Prevention Module"
category: psychology/modalities/cbt
description: "Generate a personal-manual relapse prevention module for end-of-CBT, including warning signs, personal coping toolkit, lapse vs relapse framework, booster-session plan, and self-as-own-therapist instructions."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - CBT
  - relapse-prevention
  - personal-manual
  - therapy-blueprint
  - end-of-treatment
  - Marlatt
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/cbt/psychology_cbt_thought_record_drafter.md
  - domain-psychology/modalities/cbt/psychology_cbt_behavioral_experiment_designer.md
  - domain-psychology/documentation/psychology_discharge_summary.md
---

# CBT End-of-Treatment Relapse Prevention Module

## Objective

Generate a personal manual ("therapy blueprint") for end-of-CBT relapse prevention. The artifact is for the client to carry, review periodically, and use as their own clinician. It distills the case formulation, the techniques that worked, warning signs, a lapse-vs-relapse framework, a personal coping toolkit, and a booster-session plan.

## When to Use

- Final 2–3 sessions of a time-limited CBT protocol.
- Discharge from a structured program (CBT for depression, panic, SAD, GAD, OCD, eating disorders, insomnia).
- Step-down to maintenance or self-management.
- Anniversary planning (e.g., before predictable seasonal recurrence).
- When a client wants a personal manual to refer to between sessions if therapy was open-ended.

## Inputs / Context

- Original case formulation (5Ps: predisposing, precipitating, perpetuating, protective, presenting).
- Outcomes data (PHQ-9, GAD-7, PDSS, LSAS, OCI-R, ISI, etc. — pre, mid, end).
- Techniques the client tried; which worked (client-rated) and which did not.
- Personal warning signs (early, mid, severe) the client has noticed.
- High-risk situations (anniversaries, life transitions, sleep loss, alcohol use, conflict).
- Support network and access to clinician (booster session policy; how to re-enter).
- Comorbidities and any active risk concerns (suicide history → integrate with safety plan).
- Reading level / language.

## Constraints

### Must

- Frame the manual in the **client's voice**, not the clinician's; include verbatim client phrases that capture insights.
- Distinguish **lapse** (slip, normal, expected) from **relapse** (return of disorder severity); name what each looks like for this client.
- List **warning signs** at three levels — early, mid, severe — with specific behavioral / cognitive / somatic markers.
- For each warning level, name a matched response from the personal toolkit (specific technique + specific behavioral action).
- Include a **booster-session policy**: when does the client return (clear triggers), how (call/portal/walk-in), and what the threshold is.
- Reference the original case formulation so the client can re-trace what was happening.
- Include outcome graph or numeric summary so the client can compare current state against treatment baseline.
- Include **anniversary / high-risk dates** with pre-planned interventions.
- For protocols with comorbid risk (suicidality, eating disorder), integrate the safety plan and supervisor contacts.

### Must Not

- Do not write the manual in clinician jargon; this is the client's working document.
- Do not catastrophize: lapses are expected and the manual normalizes them.
- Do not produce a positive-thinking handout; the manual must include concrete behavioral instructions.
- Do not omit the re-entry pathway; the manual is incomplete without a return mechanism.
- Do not include techniques the client did not actually find useful (be specific).
- Do not promise relapse prevention; promise self-recognition and a response plan.
- Do not finalize a relapse-prevention plan without the client's own words and review.

## Instructions

1. Review the formulation and outcomes data with the client; produce a 1-paragraph "what brought me here" summary in client voice.
2. Co-author a "what helped" list — techniques and specific moments. Mark anything that didn't help; cull rather than include.
3. Identify warning signs at three levels with specific behavioral / cognitive / somatic markers.
4. Build a toolkit table: for each warning level, the matched response (technique + behavior + person to contact).
5. Define lapse vs relapse for this client; rehearse a hypothetical lapse and the planned response.
6. Identify high-risk windows (anniversaries, predictable stressors); pre-write the response.
7. Define booster-session policy: triggers, how to contact, how soon.
8. Integrate any safety plan or comorbid risk plan.
9. Present the draft to the client; they edit/add until the manual is theirs; date and sign.

## Output Format

```
=== MY THERAPY BLUEPRINT — RELAPSE PREVENTION MANUAL ===
Name: [...]    End-of-treatment date: [YYYY-MM-DD]    Diagnosis worked on: [...]
Outcomes: [Baseline → end-of-treatment, e.g., PHQ-9 19 → 6; PDSS 16 → 3]

1) WHAT BROUGHT ME HERE (my words)
"[1 paragraph in client's voice]"

2) WHAT WAS GOING ON UNDERNEATH (my formulation)
- Predisposing: [...]
- Precipitating: [...]
- Perpetuating: [...]
- Protective: [...]
- Presenting (then): [...]

3) WHAT HELPED ME
- [Technique 1] — when I used it: [...]; what shifted: "[...]"
- [Technique 2] — [...]
- (Techniques that didn't work and why: [...])

4) MY WARNING SIGNS (specific to me)
Early (yellow):
- Behavior: [...]
- Thought patterns: [...]
- Body: [...]
Mid (orange):
- [...]
Severe (red):
- [...]

5) MY TOOLKIT (matched response per level)
Yellow → [Technique + concrete behavioral action + 1 person I'll tell]
Orange → [...]
Red → [Action + safety steps + contact clinician this week]

6) LAPSE vs RELAPSE
Lapse for me looks like: [3–5 specific observable markers]
Relapse looks like: [3–5 markers, including symptom return at baseline severity]
A lapse is not a failure. My response to a lapse: [Plan].

7) HIGH-RISK WINDOWS AND ANNIVERSARIES
- [Date / season / event] → pre-planned response

8) BOOSTER-SESSION POLICY
Return triggers: [PHQ-9 ≥ 12 for 2 weeks / mid-warning signs / specific events]
How to return: [Phone, portal, walk-in slot]
Threshold for urgent contact: [Specific]
Clinician: [Name, contact]

9) SAFETY PLAN INTEGRATION (if applicable)
- Stanley-Brown plan dated [YYYY-MM-DD] remains active.
- Lethal-means status: [...]
- Crisis contacts: [...]

10) WHAT I WANT TO REMEMBER
"[Client verbatim, 1–3 sentences]"

Signed (client): __________________    Date: _______
Signed (clinician): __________________  Date: _______
Booster review scheduled: [Date, if any]
```

## Verification

- [ ] Client voice present; jargon-free.
- [ ] Three-level warning signs with matched responses.
- [ ] Lapse vs relapse defined in client-specific terms.
- [ ] Booster-session policy with specific triggers and contact path.
- [ ] High-risk windows pre-planned.
- [ ] Outcomes data referenced (baseline → end).
- [ ] Techniques included are those the client actually used; ineffective techniques culled.
- [ ] Safety plan integrated if applicable.
- [ ] Final document signed by client and clinician.
- [ ] No catastrophizing or unrealistic promises.
- [ ] Gaps flagged; nothing fabricated.

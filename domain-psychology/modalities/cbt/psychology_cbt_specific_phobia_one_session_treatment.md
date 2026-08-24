---
title: "Specific Phobia — One-Session Treatment (OST) Plan"
category: psychology/modalities/cbt
description: "Generate an Öst-style One-Session Treatment plan for specific phobia, including hierarchy construction, prolonged graded in-vivo exposure (up to 3 hours), and consolidation homework."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - CBT
  - specific-phobia
  - one-session-treatment
  - OST
  - Öst
  - in-vivo-exposure
  - inhibitory-learning
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/cbt/psychology_cbt_behavioral_experiment_designer.md
  - domain-psychology/modalities/cbt/psychology_cbt_panic_protocol_session_plan.md
  - domain-psychology/modalities/cbt/psychology_cbt_relapse_prevention_module.md
---

# Specific Phobia — One-Session Treatment (OST) Plan

## Objective

Generate a One-Session Treatment (Öst, 1989; Davis, Ollendick, Öst 2012) plan for DSM-5-TR Specific Phobia. OST is a single, prolonged (up to ~3 hours) massed graded in-vivo exposure session preceded by a 1–2 session formulation visit and followed by consolidation homework. The output is a complete session blueprint plus pre-/post-/follow-up structure.

## When to Use

- Specific Phobia — animal, situational (flying, enclosed spaces — modified for feasibility), natural environment (heights, storms), blood-injection-injury (BII; specialized variant), or other.
- Single circumscribed feared stimulus (not generalized anxiety, not panic with agoraphobia).
- Pre-session: client has completed formulation interview and a phobia assessment (FSS, BAT, or comparable).
- Adult or pediatric clients (with developmentally adapted scaffolding).
- Telehealth: OST is traditionally in-person; some situational phobias (e.g., driving) can be done partly in vivo with clinician on phone, but contact with the stimulus must be physical.
- BII phobia: incorporate applied-tension protocol; modifies the standard OST.

## Inputs / Context

- Specific phobia subtype and target stimulus(es).
- Avoidance pattern and current life interference.
- Cognitive content of fear (what is the client afraid will happen — disgust, fainting, attack, getting trapped, dying).
- Safety behaviors and avoidance routines.
- Behavioral Avoidance Test (BAT) data: how close did client get, what reactions.
- Medical considerations: BII (vasovagal syncope risk → applied tension), asthma (for animal phobia), cardiac (for heights / driving).
- Logistics: live stimulus availability (animals, height location, driving simulator/route), 3-hour block scheduling, support person availability.
- Reading level, language, age, and developmental adaptations.
- Informed consent including the duration, the use of in-vivo exposure, and the inhibitory-learning rationale.

## Constraints

### Must

- Schedule a 3-hour block; OST ends when client has achieved at least a 50% reduction in peak fear OR completed the highest-feasible BAT step with substantial decrement, whichever comes first.
- Build the **fear hierarchy** in-session with the client (or in the pre-session); 8–15 steps from low (e.g., look at picture of spider 2 feet away) to high (e.g., hold spider for 60s).
- Run **massed exposure**: progress through the hierarchy without long breaks; each step held until fear decreases meaningfully OR step is completed multiple times for inhibitory learning.
- Use **behavioral experiment framing**: each step tests a specific prediction (e.g., "If the spider crawls on me, I will panic and lose consciousness").
- For **BII phobia**: train applied tension before exposure (tense large-muscle groups for 10–15 seconds to maintain BP; release; repeat).
- Drop safety behaviors progressively (closed eyes, gloves, distance, support person mediating).
- Model behavior with the stimulus before asking the client to do it ("Look, I'm holding it; nothing happens").
- Plan **between-step debriefs**: prediction match, what was learned, belief re-rating.
- Plan **consolidation homework**: practice with the stimulus daily or every other day for 2–4 weeks (e.g., visit the cat shelter 3× this week).
- Conduct **2-week and 1-month follow-ups** with BAT re-administration.
- Document attendance, consent, exposures, peak/end fear ratings, and adverse events.

### Must Not

- Do not abort exposure when fear is high; abort only on medical concern or refusal. Premature abort can worsen the phobia (inhibitory learning fails).
- Do not allow distraction during exposure (phone, conversation, music) — keep attention on the stimulus.
- Do not use cognitive disputation as the primary intervention; the goal is new associative learning, not verbal restructuring.
- Do not skip applied-tension training for BII.
- Do not reinforce avoidance ("you don't have to do that") in-session; renegotiate steps.
- Do not omit follow-up; return of fear is common without consolidation work.
- Do not use OST for generalized anxiety, panic-with-agoraphobia, or trauma-rooted "phobias" (use protocol-matched treatments).
- Do not use OST when the live stimulus cannot be safely accessed (e.g., real lightning) — substitute virtual reality / imaginal carefully and document limits.

## Instructions

1. Pre-session: complete formulation, FSS / phobia severity measure, BAT, informed consent including 3-hour structure and rationale.
2. At session start, review rationale (inhibitory learning, why prolonged is better than brief, why distraction undermines).
3. Build or finalize the hierarchy in-session with SUDS-anchored steps.
4. For each hierarchy step:
   - State the prediction to test.
   - Client engages the step.
   - Hold until SUDS decreases meaningfully OR step is repeated for inhibitory variability.
   - Debrief: prediction match; belief re-rating; what surprised the client.
   - Advance to next step.
5. Model the next step first whenever feasible.
6. For BII: practice applied tension before exposure; insert tension during exposure.
7. End session when ≥ 50% peak-fear reduction OR top step achieved with debrief.
8. Assign consolidation homework (daily/every-other-day contact with the stimulus, in named contexts).
9. Schedule 2-week follow-up; re-administer BAT; book 1-month follow-up.
10. Document the whole arc: hierarchy, completed steps, ratings, learning statements.

## Output Format

```
=== ONE-SESSION TREATMENT (OST) PLAN ===
Client: [Initials/MRN]    Date: [YYYY-MM-DD]    Block scheduled: [3 hours]    Modality: In-person
Phobia subtype / stimulus: [...]
Severity (FSS / clinician rating): [...]
BAT pre-session: [Step reached, peak SUDS]
Applied-tension training (BII only): [Y/N; trained on date]
Consent for prolonged exposure & in-vivo: [Y; date]

PRE-SESSION FORMULATION
- Feared outcome (verbatim): "[...]"
- Safety behaviors: [...]
- Medical considerations: [...]

HIERARCHY (built in-session with client)
| Step | Description | SUDS pred | Notes |
|------|-------------|-----------|-------|
| 1 | [...] | [N] | [...] |
| 2 | [...] | [N] | [...] |
| ...  | ...   | ... | ...   |
| 12 | [Top step] | [N] | [...] |

SESSION ARC (running log)
Step k:
- Prediction: "[client verbatim]"
- Modeled by clinician: [Y/N]
- Pre-SUDS: [N]    Peak-SUDS: [N]    End-SUDS: [N]
- Time spent: [min]
- Safety behavior(s) present / dropped: [...]
- Learning statement (client): "[verbatim]"
(repeat per step)

CLOSE
- Top step reached: [N]
- Peak fear reduction: [N → M, Δ%]
- Belief in feared outcome (pre → post): [N → M]
- Surprises / new associations: [...]

CONSOLIDATION HOMEWORK
- Practice contacts: [Frequency, settings, duration; e.g., 4 cat-shelter visits over 2 weeks, 30 min each]
- Self-monitoring: [BAT-style log of distance / duration / SUDS per contact]
- Contact clinician if: [Defined triggers]

FOLLOW-UP
- 2-week: re-administer BAT; debrief homework
- 1-month: re-administer BAT, FSS; relapse-prevention review

OUTCOME LINE
- BAT delta, FSS delta, life-interference report at follow-up.

DOCUMENTATION
- Adverse events (vasovagal, nausea, panic crests): [...]
- Risk re-screen if comorbid mood/anxiety: [Status]
- Coordination with PCP / prescriber if indicated: [...]
```

## Verification

- [ ] Single circumscribed phobia; OST is the right protocol.
- [ ] Hierarchy built with SUDS-anchored steps.
- [ ] Each step tests a specific prediction.
- [ ] Massed, prolonged exposure; no premature abort.
- [ ] Safety behaviors dropped progressively.
- [ ] Distraction prevented in-session.
- [ ] BII: applied tension trained and used.
- [ ] Consolidation homework with frequency and settings.
- [ ] Follow-up at 2 weeks and 1 month.
- [ ] Adverse events documented (especially vasovagal).
- [ ] Outcomes tracked with BAT / FSS deltas.
- [ ] No fabricated client SUDS or learning statements.

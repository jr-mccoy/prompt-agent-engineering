# Domain: Parenting

> **Scope:** Caregiver-facing parenting prompts plus a family-support-professional cluster (in expansion). Author intent: model-testing fidelity. Prompts are designed to test whether models can perform useful parenting and caregiving-related work across realistic family-facing and support-professional workflows. Use clinical / specialist supports for live decisions.

## What This Domain Is For

This domain hosts a structured, expanding library of parenting and caregiving prompts spanning ages 0 through 18 plus dedicated family-support-professional workflows. It is organized into two top-level clusters:

- **`caregiver-facing/`** — for parents, guardians, foster / kinship caregivers, stepparents, grandparents, and any adult in a primary caregiving role.
- **`family-support-professional/`** — for parenting coaches, family educators, childcare providers, early childhood specialists, school counselors, social workers, pediatric-adjacent support teams, and community program staff. (Expansion in progress.)

## Directory Layout

```
domain-parenting/
├── caregiver-facing/
│   ├── ages-0-3/          # Infant + toddler (15 prompts)
│   ├── ages-4-8/          # Early childhood (19 prompts) — original library
│   ├── ages-9-12/         # Tween (15 prompts)
│   ├── ages-13-18/        # Teen (13 prompts)
│   ├── cross-age/         # Universal mechanics (12 prompts)
│   ├── divorce/           # Separation/divorce — emotional & relational side for kids (10 prompts)
│   ├── custody/           # Court-presentable resource & document builders — parenting plans, schedules, logs (11 prompts)
│   ├── co-parenting/      # Ongoing two-home working relationship (11 prompts)
│   ├── transitions-events/    # New sibling, moving, grief (planned)
│   ├── coparenting-family-structure/  # Single, blended, foster, kinship, LGBTQ+ (planned)
│   ├── health-body-sleep-feeding/     # Health / body / sleep / feeding (planned)
│   ├── safety-risk/       # Body safety, online safety, home alone (planned)
│   ├── tech-digital/      # Phone, social media, gaming, AI (in progress; ages-9-12 has 3)
│   ├── academics-skills/  # Reading, math, writing, friendships (planned)
│   ├── mental-health-behavior/    # Anxiety, depression, OCD, school refusal, lying, aggression (in progress)
│   ├── neurodivergence/   # Beyond ADHD/ASD/strong-willed: dyslexia, 2e, PDA, tics (planned)
│   ├── identity-culture/  # Race, multilingual, religion, gender (planned)
│   └── parent-capacity/   # Postpartum, working-parent, marital strain (in progress)
└── family-support-professional/
    ├── intake-assessment/         (planned)
    ├── coaching-education/        (planned)
    ├── plans-documentation/       (planned)
    ├── group-facilitation/        (planned)
    ├── referral-resourcing/       (planned)
    ├── home-visit-fieldwork/      (planned)
    ├── foster-kinship-adoption/   (planned)
    └── culturally-responsive/     (planned)
```

## Current Inventory (106 Prompts)

### `caregiver-facing/ages-0-3/` (15 prompts)

| Prompt | Focus |
|---|---|
| `parenting_newborn_sleep_pattern_decoder.md` | Infant sleep pattern decode + 14-day plan |
| `parenting_infant_feeding_troubleshooter.md` | Latch / supply / transfer / oral structure / GI mechanism mapping |
| `parenting_starting_solids_planner.md` | Readiness, BLW vs. purée, allergen introduction, choking guardrails |
| `parenting_toddler_tantrum_response_script.md` | 12–36m tantrum script (distinct from 4–8 meltdown) |
| `parenting_speech_language_milestone_check.md` | Pre-verbal, receptive, expressive, pragmatic, articulation audit |
| `parenting_toilet_training_readiness_and_plan.md` | Readiness + method + 4–8 wk plan + constipation handling |
| `parenting_separation_anxiety_protocol_0_3.md` | 6m–3y separation, daycare, sleep, work-return |
| `parenting_biting_hitting_toddler_response.md` | Function analysis + 4-week reduction protocol |
| `parenting_daycare_transition_plan.md` | Setting fit + ramp + ill-wave plan |
| `parenting_sleep_regression_decoder.md` | 4-month / 8-9-month / 12 / 18 / 24 regressions |
| `parenting_attachment_repair_after_long_absence.md` | Hospitalization / deployment / custody reunion |
| `parenting_screen_time_for_under_3.md` | Real-world plan, video chat / co-view / passive distinction |
| `parenting_developmental_red_flags_0_3.md` | Domain-by-domain signal audit + routing |
| `parenting_when_pediatrician_visit_0_3.md` | ED / same-day / next-day / home triage |
| `parenting_postpartum_parent_capacity_check.md` | Blues vs. PPD/PPA/PP-OCD/PTSD/psychosis distinction |

### `caregiver-facing/ages-4-8/` (19 prompts — original library)

Foundations: developmental expectations 4–8, behavior function decoder, parenting style self-assessment.
Behavior / co-regulation: meltdown response, ADHD EF scaffold, strong-willed defuser, sensory home toolkit.
Communication: HFA social decoder, repair after rupture, hard topics scripts.
Routines: daily routine designer, transitions protocol.
Practice: scenario simulator, sibling conflict coach.
School / advocacy: teacher email composer, 504 / accommodation prep.
Parent capacity: coregulation reset, when to seek help.
Reward systems: pre-mortem.

### `caregiver-facing/ages-9-12/` (15 prompts)

| Prompt | Focus |
|---|---|
| `parenting_developmental_expectations_9_12.md` | Cognitive / emotional / social / physical / identity map |
| `parenting_tween_emerging_independence_negotiation.md` | Calibrated autonomy steps with repair |
| `parenting_first_phone_decision_framework.md` | Tier 1–4 device choice + contract |
| `parenting_social_media_first_account_protocol.md` | Platform risk + account config + 90-day pilot |
| `parenting_video_game_agreement_designer.md` | Game-by-game rules; voice + monetization separated |
| `parenting_friendship_drama_coaching.md` | Listen / name dynamic / scaffold / escalate |
| `parenting_bullying_target_response_protocol.md` | Documentation + school engagement + escalation |
| `parenting_bullying_perpetrator_response_protocol.md` | Driver-aware accountability + repair |
| `parenting_puberty_prep_conversation_scripts.md` | 8–15 short conversations |
| `parenting_period_prep_for_any_caregiver.md` | Inclusive of any-caregiver context |
| `parenting_body_image_early_intervention.md` | Family + digital environment + everyday language |
| `parenting_homework_autonomy_handoff_9_12.md` | EF / motivation / skill driver split + 6-phase handoff |
| `parenting_school_refusal_decoder_tween.md` | Functional analysis + graduated return |
| `parenting_lying_pattern_function_analysis.md` | Driver-aware response; conditions for honesty |
| `parenting_money_allowance_chores_system_designer.md` | Membership chores vs. earned income |

### `caregiver-facing/ages-13-18/` (13 prompts)

| Prompt | Focus |
|---|---|
| `parenting_developmental_expectations_13_18.md` | Cognitive / emotional / social / physical / identity / family map; manager → consultant shift |
| `parenting_teen_autonomy_curfew_negotiation.md` | Calibrated autonomy ladders; conditions toolkit; tightening protocol |
| `parenting_teen_mental_health_signal_check.md` | Adolescent depression / anxiety / OCD / panic / bipolar / first-episode psychosis; PHQ-A / GAD-7 / MFQ-A; routing |
| `parenting_teen_substance_conversation_scripts.md` | Pre-load + discovery scripts; CRAFFT; harm reduction; safety-call; fentanyl + naloxone |
| `parenting_teen_dating_consent_conversation.md` | Healthy relationships; consent beyond no-means-no; sextortion; nudes / AI-image; safer sex |
| `parenting_teen_driving_readiness_and_contract.md` | GDL-based four-pillar contract; telematics; after-crash protocol |
| `parenting_teen_social_media_renegotiation.md` | TikTok / IG / Snap / Discord / Reddit / X per-platform risk; algorithm; deepfakes |
| `parenting_teen_self_harm_signal_response.md` | NSSI vs. suicidality; Stanley-Brown safety plan; means restriction; DBT-informed |
| `parenting_teen_eating_disorder_signal_response.md` | Spectrum incl. atypical anorexia, ARFID, muscle dysmorphia; FBT pre-load; athlete adaptation |
| `parenting_teen_school_disengagement_decoder.md` | Disengagement vs. refusal vs. depression vs. LD; alternative pathways; GED |
| `parenting_teen_repair_after_blowup.md` | Adolescent rupture-and-repair; clean apology; long cold-war script |
| `parenting_teen_friend_group_concerns.md` | Influence boundary; adult network; radicalization vector; rare cases of forbidding |
| `parenting_teen_college_or_not_conversation.md` | Eight pathways; financial reality; ND / 2e fit; first-gen-college |

### `caregiver-facing/cross-age/` (12 prompts)

| Prompt | Focus |
|---|---|
| `parenting_family_meeting_facilitator.md` | Weekly / monthly meeting design; rotating roles; conflict process |
| `parenting_household_constitution_designer.md` | Values / rules / preferences; rules-with-reasons; family-structure adaptation |
| `parenting_chore_system_by_age.md` | Membership vs. earned-income chores; sustainable tracking; ND adaptations |
| `parenting_sibling_spacing_dynamics.md` | Patterns by age gap; functional analysis; rivalry vs. bullying differentiation |
| `parenting_praise_encouragement_calibrator.md` | Praise vs. encouragement; corrected (post-2017) Dweck framing; profile-specific |
| `parenting_boundary_holding_script_library.md` | Verbatim limit-holding scripts across domains; profile adaptations |
| `parenting_apology_modeling_for_kids.md` | Clean apology vs. JADE / over-apology / fake apology; behavior-change pair |
| `parenting_emotion_vocabulary_builder_by_age.md` | Five emotion families; granularity; alexithymia adaptation |
| `parenting_growth_mindset_language_audit.md` | Family-language audit; Dweck corrections; identity-language piece |
| `parenting_natural_consequence_designer.md` | Natural / logical / imposed; punishment-spiral exit; driver-first |
| `parenting_when_to_seek_professional_help_all_ages.md` | Specialist routing 0–18; dismissive-provider script; self-referral pathways |
| `parenting_developmental_expectations_index.md` | Router across the four age-band developmental prompts; off-tier and regression handling |

### `caregiver-facing/divorce/` (10 prompts)

The emotional and relational side of separation/divorce for children and the parenting parent. See [`divorce/README.md`](caregiver-facing/divorce/README.md).

| Prompt | Focus |
|---|---|
| `domain-parenting/caregiver-facing/divorce/parenting_divorce_telling_kids_script.md` | Age-tiered "we're separating" conversation; core messages; first reactions |
| `parenting_divorce_child_reaction_by_age_guide.md` | Expected reactions by stage; normal vs. concerning; adjustment timeline |
| `parenting_divorce_hard_questions_answer_bank.md` | Honest, age-appropriate answers to the recurring hard questions |
| `parenting_divorce_two_homes_transition_support.md` | Adjusting to two homes; transition rituals; "I miss the other parent" |
| `parenting_divorce_parent_emotional_regulation.md` | Parent's own grief/anger; no child-as-messenger/confidant/spy |
| `parenting_divorce_shield_kids_from_conflict.md` | Keeping children out of the middle; loyalty binds; not disparaging |
| `parenting_divorce_telling_others_and_privacy.md` | What to tell teachers/family; the child's own narrative and privacy |
| `parenting_divorce_new_partner_introduction_timing.md` | When/how to introduce dating and a new partner |
| `domain-parenting/caregiver-facing/divorce/parenting_divorce_milestones_and_holidays_plan.md` | Birthdays/holidays/milestones across two homes (emotionally) |
| `parenting_divorce_signs_child_needs_more_support.md` | Warning signs a child needs a therapist; escalation pathway |

### `caregiver-facing/custody/` (11 prompts)

Court-presentable resource & document builders — **not legal advice.** Factual, neutral, child-centered documents a parent uses and can present to a mediator/GAL/court. Light legal-literacy layer flagged *confirm with counsel*. See [`custody/README.md`](caregiver-facing/custody/README.md).

| Prompt | Focus |
|---|---|
| `parenting_custody_parenting_plan_builder.md` | **Flagship.** Complete court-presentable parenting plan |
| `parenting_custody_schedule_designer_by_age.md` | Age-appropriate residential/timesharing schedule + rationale |
| `parenting_custody_holiday_vacation_schedule_builder.md` | Holiday / break / summer rotation table (supersedes regular schedule) |
| `parenting_custody_child_focused_proposal_articulator.md` | Child-centered proposal for mediation (best-interests framing) |
| `parenting_custody_communication_log_template.md` | Factual, dated, neutral co-parenting communication log |
| `parenting_custody_expense_and_logistics_tracker.md` | Transparent shared-expense and reimbursement record |
| `parenting_custody_childs_voice_age_appropriate.md` | Eliciting the child's preferences without putting them in the middle |
| `parenting_custody_exchange_and_transition_protocol.md` | Low-conflict exchange/handoff protocol document |
| `parenting_custody_common_plan_provisions_explainer.md` | Light legal-literacy: common provisions in plain language |
| `parenting_custody_special_needs_plan_addendum.md` | Plan addendum for a child with disability/medical/ND needs |
| `domain-parenting/caregiver-facing/custody/parenting_custody_changed_circumstances_organizer.md` | Organize a factual record when circumstances change |

### `caregiver-facing/co-parenting/` (11 prompts)

The ongoing two-home working relationship between parents. See [`co-parenting/README.md`](caregiver-facing/co-parenting/README.md).

| Prompt | Focus |
|---|---|
| `parenting_coparenting_message_composer_biff.md` | Draft/rewrite a co-parent message in BIFF; de-escalate |
| `parenting_coparenting_high_conflict_response_strategy.md` | Parallel parenting / responding to a high-conflict co-parent |
| `parenting_coparenting_consistency_across_homes.md` | Align rules/routines where possible; accept the rest |
| `parenting_coparenting_shared_decision_framework.md` | Make joint decisions; resolve disagreement at impasse |
| `parenting_coparenting_information_handoff_brief.md` | Share what the receiving parent needs about the kids |
| `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_blended_family_coordination.md` | Coordinate new partners/stepfamily; roles and boundaries |
| `parenting_coparenting_deescalation_in_front_of_kids.md` | Disengage from a flare-up in front of the kids |
| `parenting_coparenting_relationship_reset_proposal.md` | Propose an improved working relationship to a co-parent |
| `parenting_coparenting_long_distance_protocol.md` | Maintain the parent-child relationship across distance |
| `domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_self_audit.md` | Honest self-audit of one's own contribution to conflict |
| `parenting_coparenting_with_unsafe_or_absent_parent.md` | Safety-first navigation of an unsafe/absent co-parent |

## Cross-Cutting Conventions

- **`intended_use: model-testing`** in frontmatter for prompts authored 2026-05+. Library is built for testing model performance on realistic parenting workflows.
- **Function-curious before behavior-modification framing** — "what is this behavior communicating?" precedes "how do I stop it?"
- **Strengths-based language.**
- **Developmental anchoring** — outputs tied to age tier appropriate to the prompt.
- **Cultural adaptability** — many prompts ask about family values, offer register variants, and adapt to family structure.
- **Neurodiversity-affirming** — supports access and regulation, not making children "look more typical."
- **Clinical-signal callouts** — substantive, specific signs that warrant escalation, surfaced where the model genuinely needs to call them out (not generic disclaimers).
- **False-positive prevention table** — every prompt has a misfire table.
- **Adaptations sections** — neurodivergence, identity, family-structure, cultural, capacity adaptations.

## Required Frontmatter

```yaml
---
title: "..."
category: parenting/{cluster}    # e.g., parenting/ages-0-3
description: "..."
techniques: [ST-XX, RT-XX, ...]
difficulty: beginner | intermediate | advanced
intended_use: model-testing
tags:
  - parenting
  - {age-band}
  - {topic-tags}
updated: "YYYY-MM-DD"
related_prompts:
  - domain-parenting/caregiver-facing/{cluster}/parenting_{specific}.md
---
```

## Expansion Roadmap

The library will expand in waves; current state is Wave 1.

- **Wave 1 (complete):** age extension into 0–3 and 9–12. 30 prompts.
- **Wave 2 (complete):** ages 13–18 + cross-age universals. 25 prompts.
- **Wave 3 (planned):** health / body / sleep / feeding / safety / risk.
- **Wave 4 (planned):** mental health / behavior / neurodivergence beyond ADHD/ASD/strong-willed.
- **Wave 5 (in progress):** transitions / events / family structure / identity / culture. **Separation/divorce, custody (court-presentable resource builders), and co-parenting subsections complete (32 prompts).**
- **Wave 6 (planned):** family-support professional workflows.

## Related Domains

- **Teacher-side of the school conversation:** `domain-education-teaching/`.
- **Clinical reasoning:** `domain-healthcare-clinical/`.
- **Personal development / parent self-care:** `domain-personal-development/`.
- **Hard-conversation communication (general):** `domain-product-management/`.
- **Psychology / therapy / behavioral health:** `domain-psychology/`.

---

**Last updated:** 2026-06-01

# Psychology Prompt Library — Index

**Scope:** Provider-side and client-side prompts for psychology, therapy, behavioral health, and mental health workflows. Used for **model testing and training**; prompts are written at full clinical fidelity without boilerplate disclaimers or refusal language.

**Field guide:** See [`field_guide.md`](./field_guide.md) for technique-to-task mapping and ethical considerations relevant to authoring.

---

## Subdirectory Map

```
domain-psychology/
├── field_guide.md
├── PROMPT_INDEX.md                              # this file
│
├── intake-assessment/                           # ← Phase: existing
├── diagnostic-formulation/                      # ← Phase: existing
├── treatment-planning/                          # ← Phase: existing
├── modalities/
│   └── cbt/                                     # ← Phase: existing (others scaffolded for future waves)
│
├── documentation/                               # ← Phase: Wave 1 (14 + 1 prior)
├── risk-crisis/                                 # ← Phase: Wave 2 (10)
│
├── practice-operations/                         # ← Phase: existing + Wave 7 (5 new)
├── supervision-professional/                    # ← Phase: existing + Wave 7 (8 new)
├── research-organizational/                     # ← Phase: existing
│
├── modalities/
│   ├── dbt/                                     # ← Wave 4 (built)
│   ├── act/                                     # ← Wave 4 (built)
│   ├── emdr-trauma/                             # ← Wave 4 (built)
│   ├── ifs-parts/                               # ← Wave 4 (built)
│   ├── motivational-interviewing/               # ← Wave 4 (built)
│   └── schema-psychodynamic/                    # ← Wave 4 (built)
├── family-couples-systems/                      # ← Future wave
├── substance-use/                               # ← Future wave
├── populations/
│   ├── child-adolescent/
│   ├── perinatal/
│   ├── geriatric/
│   ├── lgbtq-affirmative/
│   ├── neurodivergent-adult/
│   ├── severe-mental-illness/
│   └── veteran-military/                        # ← Future wave
├── psychiatric-prescriber/                      # ← Wave 7 (built)
├── care-coordination/                           # ← Wave 7 (built)
├── measurement-based-care/                      # ← Wave 7 (built)
└── client-self-use/                             # ← Future waves
    ├── pre-therapy/
    ├── session-prep-integration/
    ├── symptom-understanding/
    ├── coping-by-concern/
    ├── mood-journaling/
    ├── relational/
    ├── grief-loss/
    ├── identity-transitions/
    ├── crisis-self-triage/
    ├── communication-system/
    ├── habit-lifestyle/
    └── psychoeducation-self/
```

---

## Existing Prompts (relocated 2026-05-08)

### `intake-assessment/`
| File | Description |
|------|-------------|
| `psychology_behavioral_observation_framework.md` | FBA / structured behavioral observation protocol design |
| `psychology_psychometric_instrument_evaluator.md` | Reliability, validity, normative-data, cultural-fit comparison of measures |

### `diagnostic-formulation/`
| File | Description |
|------|-------------|
| `psychology_case_conceptualization_framework.md` | CBT / psychodynamic / systemic case conceptualization |

### `treatment-planning/`
| File | Description |
|------|-------------|
| `psychology_behavior_change_plan_designer.md` | COM-B / TTM / SCT-based behavior-change intervention design |
| `psychology_psychoeducation_material_creator.md` | Client-facing psychoeducational materials |

### `documentation/` *(see Wave 1 below for new prompts)*
| File | Description |
|------|-------------|
| `psychology_assessment_report_structurer.md` | Structuring psychological assessment reports |

### `modalities/cbt/`
| File | Description |
|------|-------------|
| `psychology_cognitive_distortion_identifier.md` | Identification of cognitive distortions and gentle reframing |

### `practice-operations/`
| File | Description |
|------|-------------|
| `psychology_informed_consent_template_builder.md` | Informed-consent document scaffolding |

### `supervision-professional/`
| File | Description |
|------|-------------|
| `psychology_therapeutic_technique_explainer.md` | Evidence-based technique explanation for training |

### `research-organizational/`
| File | Description |
|------|-------------|
| `psychology_organizational_culture_diagnostic.md` | Organizational culture / climate diagnostic |
| `psychology_qualitative_data_theme_analyzer.md` | Thematic analysis of qualitative data |
| `psychology_research_interview_protocol_designer.md` | Qualitative interview protocol design |

---

## Wave 1 — Documentation & Note Formats (added 2026-05-08)

`documentation/`

| # | File | Objective |
|---|------|-----------|
| 1 | `psychology_soap_progress_note.md` | SOAP-format psychotherapy progress note with golden-thread + CPT justification |
| 2 | `psychology_dap_progress_note.md` | DAP-format note with explicit subjective/objective separation inside Data |
| 3 | `psychology_birp_progress_note.md` | BIRP-format note for CMH / SUD / ACT settings |
| 4 | `psychology_girp_progress_note.md` | GIRP-format note anchored to verbatim treatment-plan goals |
| 5 | `psychology_pirp_progress_note.md` | PIRP-format note anchored to verbatim problem statements |
| 6 | `psychology_intake_assessment_note.md` | Full biopsychosocial intake (CPT 90791/90792) with five-P formulation |
| 7 | `psychology_initial_treatment_plan.md` | Goal-driven initial plan with explicit golden thread and SMART objectives |
| 8 | `psychology_treatment_plan_update.md` | 90-day plan update with continued-care justification and LOC decision |
| 9 | `psychology_discharge_summary.md` | Episode-of-care closeout with prognosis and aftercare |
| 10 | `psychology_termination_summary.md` | Therapeutic termination distinct from administrative discharge |
| 11 | `psychology_group_therapy_note.md` | Group-level + per-member notes (CPT 90853/90849) |
| 12 | `psychology_collateral_contact_note.md` | Collateral contact with ROI/authority documentation (CPT 90887 when applicable) |
| 13 | `psychology_telehealth_session_note.md` | Telehealth attestations + base-format body (POS 10/02, modifier 95/93) |
| 14 | `psychology_supervision_note.md` | Clinical supervision note for both supervisor and supervisee licensure record |

---

## Wave 2 — Risk & Crisis (added 2026-05-08)

`risk-crisis/`

| # | File | Objective |
|---|------|-----------|
| 15 | `psychology_columbia_suicide_risk_assessment.md` | Columbia C-SSRS-structured suicide risk assessment with chronic + acute stratification |
| 16 | `psychology_stanley_brown_safety_plan.md` | 6-step Stanley-Brown SPI with means safety, reasons-for-living anchor, review schedule |
| 17 | `psychology_lethal_means_counseling_script.md` | CALM-style means counseling: firearms, medications, other, with verification scheduling |
| 18 | `psychology_homicidal_ideation_triage.md` | HI triage with target identifiability, egodystonic-vs-egosyntonic, HCR-20 frame |
| 19 | `psychology_self_harm_functional_assessment.md` | NSSI four-function analysis with matched replacement-skill and harm-reduction plan |
| 20 | `psychology_post_attempt_reengagement_plan.md` | Post-ED/inpatient re-engagement plan for the 90-day high-risk window |
| 21 | `psychology_mandated_reporter_decision_walkthrough.md` | CPS/APS reporting decision walkthrough with reasonable-suspicion analysis |
| 22 | `psychology_tarasoff_duty_to_warn_analysis.md` | Identifiable-victim duty-to-protect four-element analysis with state-framework awareness |
| 23 | `psychology_civil_commitment_narrative.md` | Involuntary-hold narrative (DTS/DTO/GD) with least-restrictive-alternative analysis |
| 24 | `psychology_crisis_de_escalation_session_plan.md` | In-session crisis stabilization, rapid stratification, refusal contingency tree |

---

## Wave 5 — Client Self-Use Core (added 2026-05-08)

`client-self-use/session-prep-integration/` (6)

| # | File | Objective |
|---|------|-----------|
| 25 | `clientself_presession_agenda_drafter.md` | 10–15 min pre-session agenda drafting |
| 26 | `clientself_postsession_reflection_processor.md` | Within-24h post-session integration |
| 27 | `clientself_between_session_homework_helper.md` | Stuck-on-homework troubleshooting |
| 28 | `clientself_saying_hard_things_to_therapist_rehearsal.md` | Rehearsal for high-stakes disclosures to a therapist |
| 29 | `clientself_asking_therapist_for_change_in_approach.md` | Requesting a change in pace / modality / focus |
| 30 | `clientself_ending_therapy_conversation_planner.md` | Planning the ending-therapy conversation |

`client-self-use/symptom-understanding/` (6)

| # | File | Objective |
|---|------|-----------|
| 31 | `clientself_anxiety_depression_burnout_differentiator.md` | Self-differentiator for anxiety / depression / burnout / grief |
| 32 | `clientself_panic_attack_vs_heart_attack_reasoner.md` | Panic vs cardiac reasoning with always-include uncertainty rule |
| 33 | `clientself_intrusive_thoughts_vs_ocd_signal.md` | Distinguishing universal intrusive thoughts from OCD pattern |
| 34 | `clientself_hypomania_self_check.md` | DSM-style hypomania symptom check (self) |
| 35 | `clientself_trauma_response_pattern_recognizer.md` | Four trauma-response clusters and matched help |
| 36 | `clientself_symptom_severity_self_screen_interpreter.md` | PHQ-9 / GAD-7 / PCL-5 / AUDIT / MDQ / ACE band interpretation |

`client-self-use/coping-by-concern/` (14)

| # | File | Objective |
|---|------|-----------|
| 37 | `clientself_anxiety_grounding_menu_builder.md` | Context-matched grounding menu |
| 38 | `clientself_anxiety_panic_plan_builder.md` | One-page personal panic plan |
| 39 | `clientself_anxiety_worry_postponement_protocol.md` | CBT-GAD worry postponement |
| 40 | `clientself_anxiety_self_designed_exposure_with_therapist.md` | Exposure hierarchy draft for therapist review |
| 41 | `clientself_depression_behavioral_activation_scheduler.md` | 1-week BA schedule with M/P tags |
| 42 | `clientself_depression_rumination_interrupt_protocol.md` | Detect / shift / default-action rumination interrupt |
| 43 | `clientself_depression_anti_avoidance_prompt.md` | One-item-at-a-time avoidance reduction |
| 44 | `clientself_ocd_erp_self_designed_exercise_with_therapist.md` | ERP draft with mental-compulsion prevention |
| 45 | `clientself_ocd_family_accommodation_reduction_plan.md` | Household accommodation reduction with scripts |
| 46 | `clientself_trauma_window_of_tolerance_check.md` | Above / within / below window check + matched skill |
| 47 | `clientself_trauma_flashback_grounding_script.md` | 60-second readable flashback grounding script |
| 48 | `clientself_sleep_cbt_i_sleep_restriction_calculator.md` | CBT-I sleep restriction with safety carve-outs |
| 49 | `clientself_adhd_external_scaffold_designer.md` | Per-gap external scaffolds for adult ADHD |
| 50 | `clientself_anger_time_out_script_builder.md` | Personalized anger time-out script with return contract |

`client-self-use/mood-journaling/` (4)

| # | File | Objective |
|---|------|-----------|
| 51 | `clientself_mood_tracking_summarizer.md` | Pattern summary from mood-tracking entries |
| 52 | `clientself_weekly_emotional_pattern_review.md` | 15-min weekly emotional review |
| 53 | `clientself_journal_prompt_generator_anti_toxic_positivity.md` | State-matched journaling prompts |
| 54 | `clientself_gratitude_journal_with_calibration.md` | Gratitude practice with honest-texture calibration |

---

## Coverage Status

**Built to date (267 prompts — original ~210 plan complete + Waves 9–12):**
- Documentation formats — Wave 1 (15)
- Risk & crisis — Wave 2 (10)
- **Intake / formulation / treatment-planning depth — Wave 3 (28): intake-assessment (12), diagnostic-formulation (8), treatment-planning (8)**
- **Modality interventions — Wave 4 (31): CBT (7), DBT (5), ACT (4), EMDR/trauma (5), IFS (3), MI (4), schema/psychodynamic (3)**
- Client self-use core — Wave 5 (30): session prep / symptom understanding / coping by concern / mood-journaling
- **Populations — Wave 6 (30): child/adolescent (6), perinatal (3), geriatric (3), LGBTQ+ affirmative (3), neurodivergent adult (4), severe mental illness (4), veteran/military (3), cross-population couples/family/group/grief (4)**
- **Prescriber / care-coord / supervision+ / MBC / practice-ops+ — Wave 7 (30): psychiatric-prescriber (8), care-coordination (5), supervision-professional (8 new), measurement-based-care (4), practice-operations (5 new)**
- **Client self-use expansion — Wave 8 (41): pre-therapy (5), relational (7), grief-loss (5), identity-transitions (6), crisis-self-triage (4), communication-system (5), habit-lifestyle (4), psychoeducation-self (5)**
- **Specialty clinical verticals — Wave 9 (12): CBT-E + FBT (eating disorders), OCD-ERP, CBT-I + comorbid-insomnia, ACT-for-chronic-pain, sex therapy, behavioral addiction, bipolar IPSRT, hoarding, somatic symptom disorder, chronic-illness adjustment** — `specialty-clinical/`
- **Additional modalities — Wave 10 (10): CPT (`modalities/cpt/`), prolonged-grief therapy (`grief-therapy/`), SFBT (`sfbt/`), narrative externalizing (`narrative/`), sensorimotor/somatic + polyvagal (`somatic/`), BPT/PCIT (`behavioral-parent-training/`), group-therapy curriculum (`group/`), EFT-individual (`eft-individual/`), ACT-group (`act/`)**
- **Assessment & psychological testing — Wave 11 (10): battery selection, neuropsych/cognitive screening interpretation, ADHD battery design, autism battery design (masking-aware), multi-method personality integration, PROM selection, decisional-capacity scaffold, forensic-evaluation framing, therapeutic-assessment feedback-session planner, integrated assessment report writer** — `assessment-testing/` (all instruments referenced by name and band/structure only; no copyrighted item content; referral-aware)
- **Couples / family / systems depth + digital practice — Wave 12 (10): EFT-couples full-arc planner, Gottman intervention planner, IFS-informed couples (IFIO), structural family therapy (Minuchin), Bowenian 3-generation genogram, discernment counseling (Doherty)** — `family-couples-systems/` (6); **tele-mental-health program design, AI-augmented practice ops, digital-phenotyping interpreter, async-messaging therapy protocol** — `digital-practice/` (4, each with clinical-oversight guardrails, safety/risk routing, and licensure/PSYPACT considerations)
- Plus pre-existing relocated prompts (~10)

**Original ~210-prompt plan: complete (Waves 1–8 built). Waves 9 (specialty clinical), 10 (additional modalities), 11 (assessment/testing), and 12 (systems/digital) built 2026-06-08.**

**Planned (net-new, ~10 remaining)** — Wave 13 in the roadmap:
- **Wave 13** — Client self-use specialty (eating, OCD, chronic pain, caregiver, perinatal, etc.) (~10)

**Target final size:** ~260 prompts in `domain-psychology/` (original ~210 plan + ~52 net-new).

---

## Authoring Conventions

All prompts follow the standard repo structure: frontmatter → Objective → When to Use → Inputs → Constraints (Must / Must Not) → Instructions → Output Format → Verification.

For this expansion specifically:

- `intended_use: model-testing` is set in frontmatter on net-new prompts.
- No in-prompt safety disclaimers, refusal language, or "consult a licensed clinician" preambles.
- Constraints are about clinical / documentation accuracy and structural fidelity, not topic avoidance.
- Documentation prompts include format-faithful output skeletons.
- Risk prompts include scoring rubrics, threshold language, and named instruments (C-SSRS, Stanley-Brown, CALM, HCR-20, LOCUS, ASAM) so model output can be checked against published frameworks.

---

*Last updated: 2026-06-08*

# Discipleship & Mentorship (one-to-one formation, curriculum, and program operations)

**73 prompts** for designing and running Christian discipleship — the work of helping one person grow
into a mature, reproducing follower of Christ, and of building the human program that pairs people who
need that help with people able to give it.

This domain is about the **relationship and the plan**. It covers the curriculum a disciple moves
through, the arc of their own formation, the equipping of the person walking alongside them, the
pairing and the covenant between them, what happens in the room when they meet, and the operations of
a program that runs many such pairs at once.

It is **not** a Bible-study domain. Every piece of Scripture engagement, exegesis, doctrine, and
lesson-level biblical teaching routes to [`domain-biblical-studies/`](../domain-biblical-studies/)
(129 prompts), which this domain orchestrates rather than duplicates. Where a curriculum needs a
passage worked, this domain names the passage by address and hands off.

---

## When to use this domain

- "Someone just came to faith and I have no idea how to actually walk them through the first year."
- "I want a real curriculum, not a stack of unrelated studies."
- "I'm going to disciple someone for the first time and I don't know what I'm doing."
- "We're pairing mentors with people who want to grow — how do we match them, and what are the rules?"
- "I've been a Christian for years and I've stopped growing. I don't know why."
- "How do I know when something a mentee tells me is above my pay grade?"
- "Our discipleship program has thirty pairs and half of them have quietly stopped meeting."
- "How do we build people who go on to disciple others, instead of ending the chain at us?"

## When NOT to use this domain (use a different one)

- **You need a passage exegeted, a word studied, or a doctrine compared across traditions** →
  [`domain-biblical-studies/exegesis-interpretation/`](../domain-biblical-studies/exegesis-interpretation/)
  and [`theology-research/`](../domain-biblical-studies/theology-research/)
- **You're designing a church-wide teaching program, service calendar, or volunteer structure** →
  [`domain-biblical-studies/church-staff-ministry-ops/`](../domain-biblical-studies/church-staff-ministry-ops/)
- **You're facilitating a Bible-study group** (silence, dominance, tangents, hard questions) →
  [`domain-biblical-studies/group-leader-facilitation/`](../domain-biblical-studies/group-leader-facilitation/)
- **You're studying the Bible for yourself** (reading plan, self-quiz, book deep dive) →
  [`domain-biblical-studies/learner-self-study/`](../domain-biblical-studies/learner-self-study/)
- **Someone is in mental-health crisis, distress, or the aftermath of abuse** →
  [`domain-psychology/`](../domain-psychology/) **and a licensed professional.** Not this domain, and
  not a lay mentor.
- **You're building the software platform** (PRD, onboarding flows, matching algorithm, terms of
  service) → [`domain-idea-to-product/`](../domain-idea-to-product/),
  [`domain-product-management/`](../domain-product-management/),
  [`domain-legal/`](../domain-legal/)
- **You want general secular curriculum or learning-design machinery** →
  [`domain-education-teaching/program/curriculum-design/`](../domain-education-teaching/program/curriculum-design/),
  [`domain-learning/`](../domain-learning/)

---

## ⚠️ Load-bearing conventions

These are not style preferences. Every prompt in this domain encodes them as testable Must / Must Not
constraints, and a prompt that violates one is broken.

### 1. Tradition-neutral by default; the user may declare

Inherited from [`domain-biblical-studies/`](../domain-biblical-studies/README.md). These prompts
**describe, they do not endorse.** Where traditions differ on a formation practice — baptism as a
stage gate, confirmation or catechesis, spiritual gifts, sacraments, the shape of confession,
accountability structures — the prompt names that traditions differ and attributes positions to
identifiable interpretive streams. It never presents a contested practice as "the biblical model."

Mechanism, present in every prompt: a `**Declared tradition (optional).**` item in
`## Inputs / Context`, plus a `### Tradition-neutral stance (Must / Must Not)` subsection inside
`## Constraints`. Declaring a tradition lets the prompt foreground that stream's practices and
vocabulary; it never licenses presenting that view as fact or suppressing the alternatives.

### 2. Anti-fabrication

- **Scripture is referenced by address, never quoted from memory.** The user supplies the wording or
  verifies it against a named translation. A misquoted verse in a discipleship curriculum propagates
  for years.
- **No invented citations, authors, councils, dates, or cross-references.**
- **No fabricated discipleship research, spiritual-maturity assessment instruments, or growth
  statistics.** There is a large market in confident-sounding formation statistics; the model does not
  add to it.

### 3. Formation is not a metric

**This is the failure mode the domain is designed against.** Discipleship tooling drifts, reliably and
fast, toward measurement — and measured discipleship becomes performed discipleship.

Growth is described as **observable practices and self-reported patterns**, never as scored maturity
levels, ranked tiers, percentage-complete bars, leaderboards, or "levels of Christian." No prompt in
this domain emits a number that purports to measure a person's walk with God. Stage language describes
*where someone is working*, not *how good a Christian they are*, and no stage gate may be used to rank
people against each other or to withhold belonging.

### 4. A lay mentor is not a counselor, a pastor, or an authority

Every mentor-facing, pair-facing, and learner-facing prompt carries a boundary guardrail. Mental-health
concerns, abuse, self-harm, suicidality, addiction, and crisis are routed to licensed professionals
and — where there is danger — to appropriate authorities and emergency services. A mentor's job is to
walk alongside, not to diagnose, treat, adjudicate, or govern. When in doubt, refer out.

### 5. No hotline, agency, or service is named from memory

Referral destinations are real-world facts that change and vary by country. Every one is written as
`[VERIFY: identify the correct service from an official source]` — never a plausible-sounding number
or organization name.

### 6. No spiritual coercion

No guilt, fear, urgency, shame, love-bombing, or pressure tactics. No manufactured deadlines on
someone's spiritual decisions. Autonomy and pace are respected, doubt is treated as legitimate, and
withdrawal is always available without penalty. These prompts must never become instruments of control
— that is exactly what a discipleship relationship is structurally vulnerable to.

### 7. Safeguarding is first-class; legal requirements are never stated from memory

Pairing and program prompts surface screening, visibility norms, and reporting expectations for minors
and vulnerable adults. They **never assert a statute, a mandated-reporter threshold, a background-check
requirement, or a retention period.** Those are flagged `[VERIFY]` and routed to
[`domain-legal/`](../domain-legal/) and qualified local counsel.

### 8. Complements, never replaces, Scripture and the local church

These prompts organize a relationship and a plan. They do not adjudicate doctrine, perform exegesis,
substitute for a congregation, or position the mentor as a replacement for pastoral care.

---

## Subdirectory map

| Subdirectory | What it covers | Prompts |
|---|---|---|
| [`curriculum-architecture/`](curriculum-architecture/) | Designing the curriculum itself — stages, outcomes, sequence, balance, materials, multiplication, and governing it once it has multiplied | 7 |
| [`learner-pathways/`](learner-pathways/) | The disciple's own journey — self-assessment, personal plan, practices, stalls, returning, life constraints | 6 |
| [`mentor-equipping/`](mentor-equipping/) | The discipler — readiness, training, conversation skill, boundaries, sustainability, debrief, consultation, holding someone's doubt | 8 |
| [`pairing-and-relationship/`](pairing-and-relationship/) | Matching and the relationship container — criteria, covenant, first meeting, cadence, ending, re-contracting, and the two cases with no program behind them | 8 |
| [`session-and-lesson/`](session-and-lesson/) | What happens when they meet — session structure, lessons, questions, hard moments, small groups, accessibility | 6 |
| [`program-operations/`](program-operations/) | Running the program — blueprint, safeguarding, onboarding, health review, mentor pipeline, the smallest viable version, and an audit of the program's own design for coercion | 7 |
| [`topical-modules/`](topical-modules/) | The modules every curriculum needs and few handle well — money, work, sexuality, forgiveness, suffering, anger, digital life, hostile witness | 8 |
| [`life-stage-tracks/`](life-stage-tracks/) | The five stages where a generic pathway fails — youth, college/young adult, married couples, parents, seniors | 5 |
| [`context-variants/`](context-variants/) | Settings where someone else's rules govern — prison and re-entry, campus, workplace, remote and diaspora | 4 |
| [`initiation-and-catechesis/`](initiation-and-catechesis/) | Baptism, membership, and catechesis preparation — the highest tradition divergence in the domain | 3 |
| [`cross-cultural/`](cross-cultural/) | Discipling across culture, language, or medium — ask rather than assert | 3 |
| [`peer-and-accountability/`](peer-and-accountability/) | The sideways relationships — the mentors' own cohort, and peer accountability partnerships | 4 |
| [`after-harm/`](after-harm/) | After it has already gone wrong — dependency, harm from a previous relationship, the mentor's own rupture, the aftermath of a removal | 4 |

---

## Prompts in this domain

### `curriculum-architecture/`
| File | Purpose |
|---|---|
| `discipleship_curriculum_architecture.md` | **Flagship.** Whole multi-stage curriculum blueprint: stages, modules, outcomes, evidence, pace |
| `discipleship_formation_outcomes_framework.md` | Observable formation outcomes per stage across five domains, guarded against scoring |
| `discipleship_module_scope_and_sequence.md` | Sequence modules across terms with prerequisites and deliberate revisits |
| `discipleship_curriculum_balance_audit.md` | Audit an existing curriculum for gaps, imbalance, and smuggled tradition-specific distinctives |
| `discipleship_material_evaluation.md` | **STRONG-GUARD.** Evaluate third-party material without fabricating product, author, or review claims |
| `discipleship_multiplication_design.md` | Design for reproduction — disciples who disciple — and generational depth |
| `discipleship_multiplication_governance_and_material_drift.md` | What generation three is actually teaching, who owns the answer, and how a correction travels without becoming a licence |

### `learner-pathways/`
| File | Purpose |
|---|---|
| `discipleship_growth_self_assessment.md` | Honest, non-scoring self-assessment across formation domains |
| `discipleship_personal_growth_plan.md` | The disciple's own next-season plan: focus, practices, rhythms, people |
| `discipleship_spiritual_practices_designer.md` | Sustainable rhythms across contemplative, reformed, charismatic, and liturgical streams |
| `discipleship_stalled_growth_diagnostic.md` | Why growth stalled — and where each cause routes |
| `discipleship_returning_believer_reengagement.md` | Lapsed, dechurched, or returning — explicitly non-shaming |
| `discipleship_life_constraints_adaptation.md` | Adapt a pathway to real capacity: shift work, caregiving, disability, limited access |

### `mentor-equipping/`
| File | Purpose |
|---|---|
| `discipleship_mentor_readiness_assessment.md` | Is this person ready to disciple someone? Character, capacity, boundaries |
| `discipleship_mentor_training_curriculum.md` | Train a cohort of mentors |
| `discipleship_mentor_conversation_skills.md` | Listening, question-asking, silence, resisting the urge to fix |
| `discipleship_mentor_boundaries_and_referral.md` | **Load-bearing safety.** What a lay mentor does not do; the standing referral framework |
| `discipleship_mentor_support_and_sustainability.md` | Peer support, capacity limits, burnout prevention |
| `discipleship_mentor_season_debrief.md` | End-of-season reflection: what happened, what changes |
| `discipleship_mentor_case_consultation.md` | Taking one live situation to a third party — frame before disclosure, and a check that consulting isn't replacing a referral |
| `discipleship_mentor_posture_in_doubt_and_deconstruction.md` | **STRONG-GUARD.** Staying in relationship when someone's faith is coming apart — no counter-argument, no deadline, no verdict |

### `pairing-and-relationship/`
| File | Purpose |
|---|---|
| `discipleship_pairing_criteria_design.md` | Matching criteria: fit, safety, scope, deal-breakers, re-match triggers |
| `discipleship_relationship_covenant.md` | Written expectations, including the **limits of confidentiality** |
| `discipleship_first_meeting_guide.md` | The first conversation — build trust and scope without interrogating |
| `discipleship_cadence_and_rhythm_design.md` | Sustainable frequency, format, and channel |
| `discipleship_relationship_ending_or_transition.md` | Ending well: completion, mismatch, handoff, withdrawal |
| `discipleship_long_relationship_recontracting.md` | The years-long relationship nobody decided to continue — renew, change shape, or release |
| `discipleship_informal_pairing_without_a_program.md` | **STRONG-GUARD.** Two people, no program, no policy — and "not like this" where it can't be made safe |
| `discipleship_what_to_expect_as_a_mentee.md` | What normal looks like, what is never owed, and who to tell — held by the person being discipled |

### `session-and-lesson/`
| File | Purpose |
|---|---|
| `discipleship_session_plan_builder.md` | Reusable one-on-one session structure |
| `discipleship_lesson_builder.md` | A teaching lesson inside a module; Scripture work hands off |
| `discipleship_conversation_question_bank.md` | Questions graded by depth and topic, non-intrusive by design |
| `discipleship_hard_conversation_navigation.md` | In-the-moment response to a hard disclosure |
| `discipleship_small_group_discipleship_format.md` | Triad and small-group discipleship |
| `discipleship_session_accessibility_design.md` | Sessions that work for disabled and neurodivergent participants by default — and never assess anyone |

### `program-operations/`
| File | Purpose |
|---|---|
| `discipleship_program_design_blueprint.md` | Stand up the whole program: roles, intake, matching, cadence, review |
| `discipleship_safeguarding_and_conduct_policy.md` | **Load-bearing safety.** Screening, conduct, visibility, reporting |
| `discipleship_participant_onboarding_design.md` | Intake for both sides: what is asked for, what is offered |
| `discipleship_program_health_review.md` | Attrition, pair health, unmatched people, stalled pairs |
| `discipleship_mentor_pipeline_and_capacity.md` | Grow mentor supply against demand without lowering the bar |
| `discipleship_minimum_viable_program.md` | Three pairs, no staff, no budget — the floor that doesn't move and the structure that can wait |
| `discipleship_program_control_drift_audit.md` | **STRONG-GUARD.** Auditing your own artifacts for exit cost, information asymmetry, penalty for dissent, unaccountable authority |

### `topical-modules/`
| File | Purpose |
|---|---|
| `discipleship_module_money_and_generosity.md` | Six territories, tithe left contested, conflict of interest declared, every practice scalable to zero income |
| `discipleship_module_work_and_vocation.md` | Two strands — where work can change and where it cannot; no vocation ranked above another |
| `discipleship_module_sexuality_and_singleness.md` | **STRONG-GUARD.** No disclosure pressure, no change effort, run/don't-run decision, singleness as its own strand |
| `discipleship_module_forgiveness_and_reconciliation.md` | Forgiveness, reconciliation, and restored trust held apart; safety screen before content |
| `discipleship_module_suffering_and_lament.md` | Lament as a practice; theodicy as a range; explicit refusal to explain anyone's pain |
| `discipleship_module_anger_and_conflict.md` | Anger as information; conflict passages with their power-imbalance limits attached |
| `discipleship_module_digital_life.md` | Judgment rather than screen rules; the platform's design taught first; no mentor-held monitoring |
| `discipleship_module_witness_in_hostile_setting.md` | Graded hostility, third-party risk, non-speech witness; no security guidance, ever |

### `life-stage-tracks/`
| File | Purpose |
|---|---|
| `discipleship_track_youth_and_teen.md` | **STRONG-GUARD.** Structure before content; guardian line; response moments with anti-pressure guards |
| `discipleship_track_college_and_young_adult.md` | Designed backwards from the exit; modular against irregular attendance; the handoff as a deliverable |
| `discipleship_track_married_couples.md` | Abuse screen run separately with each spouse; three formation surfaces; roles question left contested |
| `discipleship_track_parents.md` | Refuses to measure parents by their children; a floor practice that survives the worst week |
| `discipleship_track_seniors.md` | Access designed before content; a giving strand with real recipients; a screen that is not surveillance |

### `context-variants/`
| File | Purpose |
|---|---|
| `discipleship_context_prison_and_reentry.md` | The facility governs; power asymmetry named; promise register; the release cliff planned first |
| `discipleship_context_campus_ministry.md` | The institution governs; risk to students mapped; power rules; annual rebuild against turnover |
| `discipleship_context_workplace_and_marketplace.md` | The employer governs; no pairing across an influence line; protection for colleagues who do not join |
| `discipleship_context_remote_and_diaspora.md` | Risk posture and minimal data first; crisis planned with each participant; no security guidance |

### `initiation-and-catechesis/`
| File | Purpose |
|---|---|
| `discipleship_baptism_preparation.md` | Runs the community's practice as its own; shows the divergence; removes every pressure mechanism |
| `discipleship_membership_preparation.md` | Full disclosure — authority, discipline with appeal, giving, exit — **before** commitment |
| `discipleship_catechesis_design.md` | Three-tier marking (shared / ours / contested); nothing quoted from memory; no pass mark |

### `cross-cultural/`
| File | Purpose |
|---|---|
| `discipleship_crosscultural_relationship.md` | A question set instead of a profile; the mentor's own culture written down first; power named |
| `discipleship_oral_preference_learners.md` | An oral pathway equal in outcome, built from the community's own forms; nothing told from memory |
| `discipleship_translated_material_pitfalls.md` | A checking brief for bilingual readers; never a judgment of translation quality |

### `peer-and-accountability/`
| File | Purpose |
|---|---|
| `discipleship_peer_cohort_curriculum.md` | The mentors' own formation; standing risks scheduled to recur; mentees kept out of the room |
| `discipleship_peer_cohort_facilitation.md` | Meeting shape, standing question, four verbatim interventions, power named at the start |
| `discipleship_accountability_partnership_design.md` | Mutual by construction; every surveillance mechanism banned **by name**; no metric of any kind |
| `discipleship_accountability_conversation_structure.md` | Questions answerable without confession; a verbatim response to "I didn't"; scheduled drift checks |

### `after-harm/`
| File | Purpose |
|---|---|
| `discipleship_harmed_by_previous_discipling.md` | **STRONG-GUARD.** Terms *they* set for entering a new relationship after a harmful one; safety and clinical screen first; "not now" kept available throughout |
| `discipleship_dependency_and_over_attachment.md` | Unwinding a pair that has closed in — after ruling out safeguarding, clinical need, and an unset cadence, and with the mentor-is-dependent case on the table |
| `discipleship_mentor_own_mistake_repair.md` | A gate deciding whether "mistake" is the right word, then an apology with every explanation stripped out and nothing asked in return |
| `discipleship_after_a_mentor_is_removed.md` | **STRONG-GUARD.** Care for the mentees, cohort, and community after a removal — ordered by proximity to harm, never a communications strategy |

---

## Quick routing

| You're saying | Use |
|---|---|
| "Build me a full discipleship curriculum" | `curriculum-architecture/discipleship_curriculum_architecture.md` |
| "What should growth actually look like at each stage?" | `curriculum-architecture/discipleship_formation_outcomes_framework.md` |
| "What order should these topics go in?" | `curriculum-architecture/discipleship_module_scope_and_sequence.md` |
| "Is our curriculum lopsided?" | `curriculum-architecture/discipleship_curriculum_balance_audit.md` |
| "Should we use this published discipleship material?" | `curriculum-architecture/discipleship_material_evaluation.md` |
| "How do we make disciples who make disciples?" | `curriculum-architecture/discipleship_multiplication_design.md` |
| "Where am I actually at spiritually?" | `learner-pathways/discipleship_growth_self_assessment.md` |
| "What should I focus on this next season?" | `learner-pathways/discipleship_personal_growth_plan.md` |
| "I want rhythms I can actually keep" | `learner-pathways/discipleship_spiritual_practices_designer.md` |
| "I've stopped growing and I don't know why" | `learner-pathways/discipleship_stalled_growth_diagnostic.md` |
| "I've been away from church for years and want to come back" | `learner-pathways/discipleship_returning_believer_reengagement.md` |
| "I work nights / I'm a caregiver — none of these plans fit me" | `learner-pathways/discipleship_life_constraints_adaptation.md` |
| "Am I ready to disciple someone?" | `mentor-equipping/discipleship_mentor_readiness_assessment.md` |
| "Train our mentors" | `mentor-equipping/discipleship_mentor_training_curriculum.md` |
| "I keep trying to fix people instead of listening" | `mentor-equipping/discipleship_mentor_conversation_skills.md` |
| "When is something above my pay grade?" | `mentor-equipping/discipleship_mentor_boundaries_and_referral.md` |
| "Our mentors are burning out" | `mentor-equipping/discipleship_mentor_support_and_sustainability.md` |
| "The season is over — what did we learn?" | `mentor-equipping/discipleship_mentor_season_debrief.md` |
| "How do we match people well?" | `pairing-and-relationship/discipleship_pairing_criteria_design.md` |
| "What should we agree to up front?" | `pairing-and-relationship/discipleship_relationship_covenant.md` |
| "What do I say in the first meeting?" | `pairing-and-relationship/discipleship_first_meeting_guide.md` |
| "How often should we meet, and how?" | `pairing-and-relationship/discipleship_cadence_and_rhythm_design.md` |
| "This pairing isn't working / we're finished" | `pairing-and-relationship/discipleship_relationship_ending_or_transition.md` |
| "What do we actually do for an hour?" | `session-and-lesson/discipleship_session_plan_builder.md` |
| "Build the lesson for this module" | `session-and-lesson/discipleship_lesson_builder.md` |
| "I run out of things to ask" | `session-and-lesson/discipleship_conversation_question_bank.md` |
| "They just told me something heavy" | `session-and-lesson/discipleship_hard_conversation_navigation.md` |
| "We want to do this as a group of three or four" | `session-and-lesson/discipleship_small_group_discipleship_format.md` |
| "Set up the whole pairing program" | `program-operations/discipleship_program_design_blueprint.md` |
| "What are our safety rules?" | `program-operations/discipleship_safeguarding_and_conduct_policy.md` |
| "How do we onboard people on both sides?" | `program-operations/discipleship_participant_onboarding_design.md` |
| "Half our pairs went quiet" | `program-operations/discipleship_program_health_review.md` |
| "We have more people asking than mentors available" | `program-operations/discipleship_mentor_pipeline_and_capacity.md` |
| "Build the module on money and giving" | `topical-modules/discipleship_module_money_and_generosity.md` |
| "Build the module on work and calling" | `topical-modules/discipleship_module_work_and_vocation.md` |
| "We have to talk about sexuality and singleness" | `topical-modules/discipleship_module_sexuality_and_singleness.md` |
| "They've been badly hurt and everyone wants them to reconcile" | `topical-modules/discipleship_module_forgiveness_and_reconciliation.md` |
| "How do we handle suffering without explaining it away?" | `topical-modules/discipleship_module_suffering_and_lament.md` |
| "Our people avoid conflict, or blow up in it" | `topical-modules/discipleship_module_anger_and_conflict.md` |
| "Phones, feeds, and what it's doing to us" | `topical-modules/discipleship_module_digital_life.md` |
| "Being known as a Christian costs something real here" | `topical-modules/discipleship_module_witness_in_hostile_setting.md` |
| "Design our teen discipleship track" | `life-stage-tracks/discipleship_track_youth_and_teen.md` |
| "Students who leave after three years" | `life-stage-tracks/discipleship_track_college_and_young_adult.md` |
| "Disciple married couples without becoming their counselors" | `life-stage-tracks/discipleship_track_married_couples.md` |
| "Disciple parents without grading them by their kids" | `life-stage-tracks/discipleship_track_parents.md` |
| "Our older adults are treated as ministry recipients" | `life-stage-tracks/discipleship_track_seniors.md` |
| "Discipleship inside a prison, and after release" | `context-variants/discipleship_context_prison_and_reentry.md` |
| "Run this on a campus, inside the institution's rules" | `context-variants/discipleship_context_campus_ministry.md` |
| "A group at work — and I manage some of them" | `context-variants/discipleship_context_workplace_and_marketplace.md` |
| "Everyone's in a different country and time zone" | `context-variants/discipleship_context_remote_and_diaspora.md` |
| "Prepare someone for baptism" | `initiation-and-catechesis/discipleship_baptism_preparation.md` |
| "Prepare someone for membership — and tell them what they're agreeing to" | `initiation-and-catechesis/discipleship_membership_preparation.md` |
| "Build our catechesis" | `initiation-and-catechesis/discipleship_catechesis_design.md` |
| "I'm discipling someone whose culture and language I don't share" | `cross-cultural/discipleship_crosscultural_relationship.md` |
| "They don't read, or don't prefer to" | `cross-cultural/discipleship_oral_preference_learners.md` |
| "Our material is being translated" | `cross-cultural/discipleship_translated_material_pitfalls.md` |
| "Our mentors need a group of their own" | `peer-and-accountability/discipleship_peer_cohort_curriculum.md` |
| "How do I actually run the mentors' meeting?" | `peer-and-accountability/discipleship_peer_cohort_facilitation.md` |
| "Two friends want to keep each other accountable" | `peer-and-accountability/discipleship_accountability_partnership_design.md` |
| "Our accountability has turned into interrogation" | `peer-and-accountability/discipleship_accountability_conversation_structure.md` |
| "I was badly hurt by a mentor before, and someone's asked me again" | `after-harm/discipleship_harmed_by_previous_discipling.md` |
| "She can't make a decision without checking with me first" | `after-harm/discipleship_dependency_and_over_attachment.md` |
| "I said something I shouldn't have, and he's gone quiet" | `after-harm/discipleship_mentor_own_mistake_repair.md` |
| "We've had to remove a mentor — what do we say to everyone?" | `after-harm/discipleship_after_a_mentor_is_removed.md` |
| "I'm stuck with someone I'm discipling and need to talk to somebody" | `mentor-equipping/discipleship_mentor_case_consultation.md` |
| "He's losing his faith and I don't know how to be in the room" | `mentor-equipping/discipleship_mentor_posture_in_doubt_and_deconstruction.md` |
| "There's no program — we're just two people meeting" | `pairing-and-relationship/discipleship_informal_pairing_without_a_program.md` |
| "Someone's offered to disciple me and I don't know what's normal" | `pairing-and-relationship/discipleship_what_to_expect_as_a_mentee.md` |
| "We've been meeting for four years and nobody knows why any more" | `pairing-and-relationship/discipleship_long_relationship_recontracting.md` |
| "I'm bivocational with three pairs — what do I actually need?" | `program-operations/discipleship_minimum_viable_program.md` |
| "Is our own program putting pressure on people?" | `program-operations/discipleship_program_control_drift_audit.md` |
| "Our sessions don't work for everyone in the room" | `session-and-lesson/discipleship_session_accessibility_design.md` |
| "We've multiplied three generations out and nobody knows what's being taught" | `curriculum-architecture/discipleship_multiplication_governance_and_material_drift.md` |

---

## How prompts in this domain compose

**Standing up a program** runs top-down and only once:
`program_design_blueprint` → `safeguarding_and_conduct_policy` → `pairing_criteria_design` →
`participant_onboarding_design` → `mentor_training_curriculum`. Safeguarding comes before matching on
purpose: you cannot design pairing criteria honestly until you know what disqualifies a pairing.

**Building the content** runs in parallel to that:
`formation_outcomes_framework` → `curriculum_architecture` → `module_scope_and_sequence` →
`lesson_builder`. Outcomes precede architecture because a curriculum built before you know what
you're forming toward becomes a reading list.

**A single pair's life cycle** is the loop the program exists to serve:
`mentor_readiness_assessment` → *(matched)* → `first_meeting_guide` → `relationship_covenant` →
`cadence_and_rhythm_design` → `session_plan_builder` (repeating) → `relationship_ending_or_transition`
→ `mentor_season_debrief`. `hard_conversation_navigation` and `mentor_boundaries_and_referral` are
**event-triggered**, not scheduled — they fire when something surfaces.

**The disciple's own arc** is entered from either end: someone can walk
`growth_self_assessment` → `personal_growth_plan` → `spiritual_practices_designer` alone, or a mentor
can run it with them. `stalled_growth_diagnostic` and `returning_believer_reengagement` are entry
points in their own right for people who don't arrive at the start of a pathway.

**The feedback loop that keeps it alive:** `program_health_review` and `mentor_season_debrief` feed
`curriculum_balance_audit` and `mentor_pipeline_and_capacity`, which revise the architecture. A
program without that loop silently ossifies around whatever its first cohort happened to need.

**The path with no institution behind it** is the one the spine above assumes away, and it is how most
discipleship actually happens: `what_to_expect_as_a_mentee` (held by the person being discipled, and
read before agreeing to anything) → `informal_pairing_without_a_program` (two people, which can return
*not like this*) → the ordinary session and conversation prompts. Where it grows past two or three
pairs, `minimum_viable_program` says what a leader with a job and no budget genuinely has to build.

**The fifth entry point is after something has gone wrong.** `after-harm/` is entered from four
directions and never in sequence: the person harmed in a previous relationship, the pair that has closed
in, the mentor who caused a rupture, and the program left holding everyone else. All four begin *after*
`safeguarding_and_conduct_policy` has done its work, and each can return "this is not ours — route it".
`mentor_case_consultation` sits just below them, for the live situation that is hard but still inside
the role. Two audits watch the program itself rather than the pairs:
`program_control_drift_audit` on its own artifacts, and
`multiplication_governance_and_material_drift` on what it is teaching three generations out.

**Wave 2 attaches to that spine at four points.** `topical-modules/` supply the content
`curriculum_architecture` places and `lesson_builder` builds out. `life-stage-tracks/` and
`context-variants/` are the same architecture rebuilt around a binding constraint — a life stage in the
first case, someone else's governing rules in the second — and both settle structure *before* content.
`initiation-and-catechesis/` sits at the moments a community formally receives someone, downstream of
formation and upstream of nothing. `cross-cultural/` and `peer-and-accountability/` cut across
everything: the first governs how any of it travels across a culture, a language, or a medium; the
second runs sideways, forming the disciplers themselves and the peers who help each other.

---

## Frontmatter conventions specific to this domain

Standard eight fields in fixed order: `title`, `category`, `description`, `techniques`, `difficulty`,
`tags`, `updated`, `related_prompts`. No extended machine-readable block (this domain does not use the
`reasoning:` convention).

- **`category`** is `discipleship/<subdirectory>` and always matches the file's directory.
- **`techniques`** is exactly 5 canonical IDs from
  [`techniques/MASTER_TECHNIQUE_INDEX.md`](../techniques/MASTER_TECHNIQUE_INDEX.md). The domain spine
  is `ST-01, ST-02, RT-02, CM-02, QA-01`, with `OC-03` for table-heavy outputs, `QA-05` for
  Scripture-address discipline, `QA-04` where the prompt must hold uncertainty, `ED-01` for curriculum
  scaffolding, `DS-01` for framework application, `RP-02` for audience framing, `OC-12` for resource
  catalogs, and `NE-14` where output genuinely serves multiple audiences.
- **`related_prompts`** is 4–5 repo-root-relative paths, with at least one intra-domain link and at
  least one into `domain-biblical-studies/`. Every path is verified to exist before it is written.
- **`tags`** always include `discipleship`, plus the subdirectory theme.

Body skeleton, in order: `**Objective:**` → guard-banner blockquote (where applicable) →
`**When to use:**` / `**When NOT to use:**` / `**Audience:**` → `## Inputs / Context` →
`## Constraints` (`### Must`, `### Must Not`, `### Tradition-neutral stance (Must / Must Not)`) →
`## Instructions` (`### Step N — …`) → `## Output Format` (one fenced block) → `## Verification`
(six checkboxes) → `## False-Positive Prevention` (❌ DON'T / ✅ DO) → `## Techniques Used`.
Horizontal rules separate every top-level section.

---

## Companion domains

- [`domain-biblical-studies/`](../domain-biblical-studies/) — everything Scripture: exegesis, word
  study, doctrine, genre, sermon prep, Bible-study group facilitation, church teaching operations.
  This domain hands off to it constantly and duplicates none of it.
- [`domain-education-teaching/`](../domain-education-teaching/) — the secular curriculum-design
  machinery (curriculum mapping, backward design, outcomes architecture) whose patterns this domain
  adapts.
- [`domain-learning/`](../domain-learning/) — domain-agnostic skill acquisition and deliberate practice.
- [`domain-psychology/`](../domain-psychology/) — where distress, trauma, and clinical concerns go.
  The boundary between this domain and that one is load-bearing, not decorative.
- [`domain-personal-development/`](../domain-personal-development/) — habits, identity, resilience, and
  life transitions, in a non-religious frame.
- [`domain-negotiation/difficult-conversations/`](../domain-negotiation/difficult-conversations/) —
  general difficult-conversation craft.
- [`domain-legal/`](../domain-legal/) — where safeguarding policy questions with legal weight go.

---

## Deliberately not duplicated

Four prompts in `domain-biblical-studies/` sit close to this domain and are **cross-linked, never
copied**:

| Existing prompt | Its job | Why it isn't here |
|---|---|---|
| `ministry-contexts/biblical_ministry_new_believer_discipleship_path.md` | A ministry teacher designs a staged first-steps path | Teacher-facing and Scripture-shaped; this domain covers the *pair* and the disciple's own arc |
| `church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md` | Church staff map a congregation-wide pathway | Institution-scale; this domain is program- and relationship-scale |
| `church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md` | Multi-quarter scope & sequence for a church teaching program | Teaching-program scope; `discipleship_module_scope_and_sequence.md` sequences a *formation* curriculum |
| `group-leader-facilitation/biblical_groupleader_apprentice_development.md` | Develop an apprentice Bible-study group leader | Grows a *group leader*; this domain grows a *disciple who disciples* |

Also not duplicated: Bible reading plans, study methods, and habit-building for Scripture intake all
live in `domain-biblical-studies/study-methods-teaching/` and `learner-self-study/`. Generic habit
design lives in `domain-personal-development/prompts/habits/`. Burnout recovery lives in
`domain-personal-development/prompts/agency/agency_burnout_recovery.md`.

---

**Expansion roadmap:** [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md)
**Last Updated:** 2026-08-04 (Wave 2)

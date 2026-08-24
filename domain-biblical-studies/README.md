# Biblical Studies: Bible Study & Research Prompt Library

Prompts for studying, teaching, preaching from, and researching the Bible — built for six audiences: laypeople doing personal/devotional study, small-group and Sunday-school leaders, pastors and preachers, seminary/academic researchers, self-directed learners, and ministry-context teachers.

## Scope

This domain covers Bible-study and biblical-research workflows: passage exegesis, original-language word studies, genre-aware reading, historical-cultural and literary context, narrative and rhetorical analysis, ancient Near Eastern comparative context, canonical/intertextual reading, inductive and devotional study methods, book overviews, lesson and discussion-guide building, reading and memorization plans, expository sermon preparation, devotionals and meditation, topical/systematic theology, doctrine study, comparison of interpretive views, cross-reference/typology mapping, difficult-passage analysis, background research briefs, historical-theology (development of doctrine over time), biblical ethics, theology of a single book, research source mapping, and stress-testing one's own position.

Difficulty spans **beginner** (first-look observation, SOAP, devotionals) through **advanced** (original-language word study, canonical reading, multi-view interpretation, systematic synthesis).

## Two load-bearing conventions

### 1. Tradition-neutral by default

These prompts **describe, they do not endorse.** They present the biblical text, the scholarly consensus where one exists, and — where interpretive traditions differ — they describe the competing positions fairly and attribute each to an *identifiable interpretive stream* (e.g., "a common Reformed reading," "many Catholic interpreters," "historical-critical scholarship," "much of Jewish tradition"). Doctrinal and interpretive claims are treated as **positions held by traditions, never as settled fact.**

A user may *optionally* declare a tradition or confessional framework. Declaring a tradition lets the prompt foreground that reading and its familiar resources/terminology — but it never licenses presenting that view as fact or suppressing the main alternatives. With no declaration, the default is neutral, multi-view-descriptive output.

This is not theological relativism; it is interpretive honesty. The prompts refuse to flatten genuine disagreement into false consensus and refuse to present a contested reading as "the plain meaning."

### 2. Anti-fabrication is the first-order risk

Biblical study is exceptionally prone to model hallucination. Every prompt forbids:
- **Invented original-language data** — fabricated Greek/Hebrew/Aramaic roots, etymologies, glosses, semantic ranges, Strong's numbers, or parsing.
- **Fabricated or misquoted citations** — invented chapter:verse references, or verse wording quoted inaccurately from memory.
- **Made-up attributions** — invented scholars, commentators, councils, dates, or quoted sources.
- **Invented cross-references** and **fabricated historical/archaeological claims** (excavations, inscriptions, dates).

Prompts reference verses **by address** and ask the user to supply the translation text or verify wording against a named, real resource; the model does **not** quote lexicons, manuscripts, or apparatus from memory. Original-language, citation-heavy, and historical prompts carry heavier **STRONG-GUARD** language plus a Verification block with citation/quotation-accuracy and uncertainty-acknowledgment checks.

## Directory Map

```
domain-biblical-studies/
├── exegesis-interpretation/     Passage exegesis, original-language word study, genre-aware
│                                reading, historical-cultural & literary context, narrative &
│                                rhetorical analysis, ANE comparative context, canonical/
│                                intertextual reading, beginner observation, multi-view
│                                interpretation map, translation comparison
├── study-methods-teaching/      Inductive (OIA), SOAP, whole-book overview, small-group
│                                discussion guides, lesson plans, memorization & reading plans,
│                                thematic/topical study
├── sermon-devotional/           Expository sermon prep, illustration development, daily
│                                devotionals, meditation, prayer/journaling, series planning,
│                                text-to-application, sermon manuscript drafting, delivery
│                                coaching, lectionary prep, liturgical-calendar devotionals
├── theology-research/           Topical/systematic synthesis, doctrine study, comparing
│                                interpretive views, cross-reference/typology, difficult-passage
│                                analysis, background research brief, canonical theme trajectory,
│                                historical-theology development, biblical ethics, theology of a
│                                book, research source map, position stress-test, exegetical-fallacy
│                                detector, commentary evaluation, creed/confession analysis,
│                                worship practice biblical basis, church government/polity
├── learner-self-study/          Self-directed individual learners (audience S): study-plan design,
│                                character study, self-quiz/recall, doctrine self-exploration,
│                                honest-questions explorer, study-tool skills, comprehension self-
│                                check, personal application, reflection journaling, Bible reading
│                                habit builder, single-book deep dive, tradition comparison on
│                                practices. Boundary guardrail: not pastoral counseling or crisis
│                                support.
├── ministry-contexts/           Teaching specific groups (audience M): kids' lessons, youth study,
│                                new-believer discipleship, seeker intro, family devotions, special
│                                programs (VBS/camp/retreat), biblical care-conversation foundations,
│                                men's/women's study, college/young-adult study, seniors' study,
│                                grief/loss Scripture guide (STRONG + boundary), marriage enrichment,
│                                parenting Scripture guide. Child-safety and care-conversation
│                                guardrails. Cross-domain links to domain-psychology/ and
│                                domain-parenting/.
├── church-staff-ministry-ops/   Operational/administrative workflows for people who run a
│                                teaching ministry (audience P/G): curriculum scope-and-sequence,
│                                curriculum evaluation, teacher training, multi-service coordination,
│                                annual teaching calendar, volunteer roles, small-group launch,
│                                discipleship pathway, midweek programs, sermon feedback/debrief.
├── group-leader-facilitation/   In-room dynamics for group leaders (audience G/P): facilitation
│                                dynamics, handling hard questions, heretical-claim response,
│                                mixed-maturity leveling, conflict resolution, hybrid/online
│                                format, apprentice leader development.
├── original-languages/          Deeper Greek/Hebrew tooling (highest fabrication risk, all STRONG-
│                                GUARD): parsing/morphology, Greek syntax, Hebrew syntax, discourse
│                                analysis, OT-in-NT usage, textual criticism, canon/versification
│                                differences, Septuagint/MT divergences, Aramaic analysis,
│                                vocabulary builder. (Word study lives in exegesis-interpretation/.)
├── biblical-theology-method/    Method-level prompts above exegesis, below systematics: biblical vs.
│                                systematic theology, redemptive-historical reading, author theology
│                                comparison, center-of-biblical-theology debate.
└── apologetics-engagement/      Structured intellectual engagement and interfaith dialogue (custom
                                 STRONG-GUARD for fabricated philosophical arguments, misrepresented
                                 worldview positions, invented historical evidence): objection
                                 engagement, Bible reliability, comparative worldview, faith & science,
                                 conversation prep, problem of evil/theodicy, biblical contradictions,
                                 interfaith dialogue.
```

> **Sermon types** beyond expository (topical, evangelistic, occasional) live in `sermon-devotional/`;
> **genre-specific reading guides** (parable, prophecy/apocalyptic, poetry, wisdom, law, epistle) live in
> `exegesis-interpretation/` and are routed to by the generic genre prompt.

## How These Prompts Are Built

Every prompt includes:
- **YAML frontmatter** — title, category, description, 3–5 technique IDs, difficulty, tags, updated, related_prompts.
- **Tradition-neutral stance** encoded as testable Must / Must Not constraints, plus an optional declared-tradition input hook.
- **No-fabrication clause** — explicit prohibition on invented citations, glosses, attributions, and historical claims; verify-by-address discipline.
- **Locked output format** — so the result drops straight into a study sheet, lesson plan, sermon outline, or research brief.
- **Verification block** — self-check covering citation/quotation accuracy, neutrality, and uncertainty acknowledgment.
- **False-Positive Prevention** — explicit DON'T/DO patterns for the domain's characteristic errors (etymological fallacy, proof-texting, eisegesis, false consensus, fabricated illustration facts).

## What These Prompts Are NOT

- Not authoritative theology or a substitute for real lexicons, commentaries, critical editions, or trained scholarship.
- Not a translation engine or a source of manuscript/textual-critical data.
- Not tradition-prescriptive — they will not tell a user which tradition is correct.
- Not pastoral counseling or mental-health support. Route distress and crisis to appropriate care (see `domain-psychology/`).

## Routing (for Claude)

| User says | Use |
|---|---|
| "Exegete / work through this passage" | `exegesis-interpretation/biblical_passage_exegesis_workflow.md` |
| "Do a word study on this Greek/Hebrew word" | `exegesis-interpretation/biblical_word_study_original_language.md` |
| "What genre is this and how do I read it?" | `exegesis-interpretation/biblical_genre_aware_reading.md` |
| "How do I interpret this parable?" | `exegesis-interpretation/biblical_parable_interpretation.md` |
| "How do I read prophecy / apocalyptic?" | `exegesis-interpretation/biblical_prophecy_apocalyptic_interpretation.md` |
| "How do I read this psalm / Hebrew poetry?" | `exegesis-interpretation/biblical_hebrew_poetry_psalms_reading.md` |
| "How do I read Proverbs / Job / Ecclesiastes?" | `exegesis-interpretation/biblical_wisdom_literature_reading.md` |
| "How do I read Old Testament law?" | `exegesis-interpretation/biblical_law_torah_reading.md` |
| "Trace the argument of this epistle" | `exegesis-interpretation/biblical_epistle_argument_tracing.md` |
| "What's the historical/cultural background?" | `exegesis-interpretation/biblical_historical_cultural_context.md` |
| "What are the ancient Near Eastern parallels to this text?" | `exegesis-interpretation/biblical_ane_comparative_context.md` |
| "How does this fit its context / structure?" | `exegesis-interpretation/biblical_literary_context_structure.md` |
| "How is this story told? (character, plot, narrator)" | `exegesis-interpretation/biblical_narrative_analysis.md` |
| "What rhetorical devices / persuasive strategy is at work?" | `exegesis-interpretation/biblical_rhetorical_analysis.md` |
| "Trace how this passage connects to others" | `exegesis-interpretation/biblical_canonical_intertextual_reading.md` |
| "I'm new — what does this passage actually say?" | `exegesis-interpretation/biblical_passage_observation_beginner.md` |
| "What are the different interpretations of this verse?" | `exegesis-interpretation/biblical_multiview_interpretation_map.md` |
| "Why do translations differ here?" | `exegesis-interpretation/biblical_translation_comparison.md` |
| "Run an inductive (OIA) study" | `study-methods-teaching/biblical_inductive_study_method.md` |
| "SOAP / quick daily study method" | `study-methods-teaching/biblical_soap_devotional_method.md` |
| "Give me an overview of this whole book" | `study-methods-teaching/biblical_book_overview_synthesis.md` |
| "Discussion questions for my small group" | `study-methods-teaching/biblical_smallgroup_discussion_guide.md` |
| "Build a lesson plan / Sunday-school class" | `study-methods-teaching/biblical_lesson_plan_builder.md` |
| "Help me memorize Scripture" | `study-methods-teaching/biblical_memorization_retention_plan.md` |
| "Study a theme/topic across passages" | `study-methods-teaching/biblical_thematic_topical_study.md` |
| "Design a reading plan" | `study-methods-teaching/biblical_reading_plan_designer.md` |
| "Help me prep an expository sermon" | `sermon-devotional/biblical_expository_sermon_prep.md` |
| "Find an illustration for this point" | `sermon-devotional/biblical_sermon_illustration_finder.md` |
| "Write a daily devotional" | `sermon-devotional/biblical_daily_devotional_writer.md` |
| "Guide me in meditating on this passage" | `sermon-devotional/biblical_meditation_reflection_guide.md` |
| "Give me prayer/journaling prompts" | `sermon-devotional/biblical_prayer_journaling_prompts.md` |
| "Plan a sermon/teaching series" | `sermon-devotional/biblical_sermon_series_planner.md` |
| "How do I apply this text today?" | `sermon-devotional/biblical_application_bridge_builder.md` |
| "Prep a topical sermon (across multiple texts)" | `sermon-devotional/biblical_topical_sermon_prep.md` |
| "Prep an evangelistic / gospel message" | `sermon-devotional/biblical_evangelistic_message_prep.md` |
| "Prep a funeral / wedding / dedication message" | `sermon-devotional/biblical_occasional_message_prep.md` |
| "Convert my sermon outline to a speakable manuscript" | `sermon-devotional/biblical_sermon_manuscript_draft.md` |
| "Help me improve my preaching delivery" | `sermon-devotional/biblical_sermon_delivery_coaching.md` |
| "Prep a sermon from lectionary readings" | `sermon-devotional/biblical_lectionary_sermon_prep.md` |
| "Design a devotional series for a liturgical season" | `sermon-devotional/biblical_liturgical_calendar_devotional_series.md` |
| "What does Scripture teach about [topic]?" | `theology-research/biblical_topical_theology_synthesis.md` |
| "Study this doctrine across traditions" | `theology-research/biblical_doctrine_study_neutral.md` |
| "Compare the views on this disputed question" | `theology-research/biblical_interpretive_views_comparison.md` |
| "Map cross-references / typology" | `theology-research/biblical_crossreference_typology_map.md` |
| "Help me with this difficult/'problem' passage" | `theology-research/biblical_difficult_passage_analysis.md` |
| "Build a background research brief" | `theology-research/biblical_background_research_brief.md` |
| "Trace this theme across the canon" | `theology-research/biblical_theme_canonical_trajectory.md` |
| "How did this doctrine develop across church history?" | `theology-research/biblical_historical_theology_development.md` |
| "Frame this moral/ethical question across Scripture and traditions" | `theology-research/biblical_ethics_moral_question_framework.md` |
| "What is the distinctive theology of this book?" | `theology-research/biblical_book_theology_synthesis.md` |
| "What kinds of sources should I research (source-type, not titles)?" | `theology-research/biblical_theological_research_bibliography.md` |
| "Stress-test a position I hold" | `theology-research/biblical_position_stress_test.md` |
| "Check an interpretation for exegetical fallacies" | `theology-research/biblical_exegetical_fallacy_detector.md` |
| "Evaluate / compare commentaries" | `theology-research/biblical_commentary_evaluation.md` |
| **Self-directed learner (S)** | |
| "Design my own multi-week study plan" | `learner-self-study/biblical_learner_self_directed_study_plan.md` |
| "Study a Bible character on my own" | `learner-self-study/biblical_learner_character_study_guide.md` |
| "Quiz me / test my recall (my supplied text)" | `learner-self-study/biblical_learner_self_quiz_recall_drill.md` |
| "Explore a doctrine for myself across traditions" | `learner-self-study/biblical_learner_doctrine_self_exploration.md` |
| "Work through honest questions / doubts about a text" | `learner-self-study/biblical_learner_honest_questions_doubt_explorer.md` |
| "Learn to use study tools (concordance, lexicon, study Bible)" | `learner-self-study/biblical_learner_study_tool_skill_builder.md` |
| "Check whether I actually understood this passage" | `learner-self-study/biblical_learner_comprehension_self_check.md` |
| "Derive honest personal application for myself" | `learner-self-study/biblical_learner_personal_application_worksheet.md` |
| "Reflective journaling through a passage / book" | `learner-self-study/biblical_learner_reflection_journal_companion.md` |
| "Build a sustainable daily Bible reading habit" | `learner-self-study/biblical_learner_bible_reading_habit_builder.md` |
| "Extended multi-week deep dive into one book" | `learner-self-study/biblical_learner_book_of_the_bible_deep_dive.md` |
| "How do traditions differ on this practice (baptism, communion, etc.)?" | `learner-self-study/biblical_learner_compare_traditions_on_practice.md` |
| **Ministry-context teacher (M)** | |
| "Build a kids' Bible lesson" | `ministry-contexts/biblical_ministry_kids_bible_lesson_builder.md` |
| "Design a youth / teen Bible study" | `ministry-contexts/biblical_ministry_youth_bible_study_designer.md` |
| "Discipleship path for a new believer" | `ministry-contexts/biblical_ministry_new_believer_discipleship_path.md` |
| "Introduce the Bible to a curious skeptic / seeker" | `ministry-contexts/biblical_ministry_seeker_intro_to_bible.md` |
| "Design family / household devotions" | `ministry-contexts/biblical_ministry_family_devotions_designer.md` |
| "Plan a VBS / camp / retreat session" | `ministry-contexts/biblical_ministry_special_program_session.md` |
| "Frame a Scripture-rooted care conversation (NOT therapy)" | `ministry-contexts/biblical_ministry_biblical_care_conversation_foundations.md` |
| "Design a men's or women's Bible study" | `ministry-contexts/biblical_ministry_mens_womens_study_designer.md` |
| "Design a college / young adult (18-30) study" | `ministry-contexts/biblical_ministry_college_young_adult_study.md` |
| "Design a seniors' (60+) Bible study" | `ministry-contexts/biblical_ministry_seniors_study_designer.md` |
| **Church staff / ministry ops (audience P, G)** | |
| "Build a multi-quarter curriculum scope-and-sequence" | `church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md` |
| "Evaluate a published curriculum" | `church-staff-ministry-ops/biblical_churchstaff_curriculum_selection_evaluation.md` |
| "Train Bible-study volunteers" | `church-staff-ministry-ops/biblical_churchstaff_teacher_training_plan.md` |
| "Coordinate teaching across multiple services/campuses" | `church-staff-ministry-ops/biblical_churchstaff_multi_service_teaching_coordination.md` |
| "Map the preaching/teaching year" | `church-staff-ministry-ops/biblical_churchstaff_annual_teaching_calendar.md` |
| "Design volunteer roles with descriptions and onboarding" | `church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md` |
| "Design a small-group launch system" | `church-staff-ministry-ops/biblical_churchstaff_small_group_launch_system.md` |
| "Design a congregation-wide discipleship pathway" | `church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md` |
| "Design a sustainable midweek program" | `church-staff-ministry-ops/biblical_churchstaff_midweek_program_design.md` |
| "Post-sermon debrief and feedback" | `church-staff-ministry-ops/biblical_churchstaff_sermon_feedback_debrief.md` |
| **Group leader facilitation (audience G, P)** | |
| "Manage silence, dominance, tangents, conflict in a group" | `group-leader-facilitation/biblical_groupleader_facilitation_dynamics.md` |
| "Handle a hard question I can't answer" | `group-leader-facilitation/biblical_groupleader_handling_hard_questions.md` |
| "Respond to a heretical/heterodox claim in my group" | `group-leader-facilitation/biblical_groupleader_heretical_claim_response.md` |
| "Adapt a study for mixed spiritual maturity" | `group-leader-facilitation/biblical_groupleader_mixed_maturity_leveling.md` |
| "Navigate theological conflict in my group" | `group-leader-facilitation/biblical_groupleader_conflict_resolution.md` |
| "Adapt my study for hybrid/online delivery" | `group-leader-facilitation/biblical_groupleader_hybrid_online_format.md` |
| "Develop an apprentice group leader" | `group-leader-facilitation/biblical_groupleader_apprentice_development.md` |
| **Original languages (highest fabrication risk — all STRONG-GUARD)** | |
| "Parse / verify a Greek or Hebrew form" | `original-languages/biblical_language_parsing_morphology_helper.md` |
| "Analyze Greek syntax / grammar" | `original-languages/biblical_language_greek_syntax_analysis.md` |
| "Analyze Hebrew syntax / grammar" | `original-languages/biblical_language_hebrew_syntax_analysis.md` |
| "Discourse / clause-flow analysis" | `original-languages/biblical_language_discourse_analysis.md` |
| "How does this NT text use the OT (MT/LXX/NT)?" | `original-languages/biblical_language_ot_in_nt_usage.md` |
| "How does textual criticism work? (user-specified variant)" | `original-languages/biblical_language_textual_criticism_primer.md` |
| "Where do canons and verse numbering diverge?" | `original-languages/biblical_language_canon_versification_differences.md` |
| "Analyze MT vs. LXX divergences (user supplies both texts)" | `original-languages/biblical_language_septuagint_usage.md` |
| "Analyze an Aramaic section (Daniel, Ezra)" | `original-languages/biblical_language_aramaic_analysis.md` |
| "Design a frequency-based Greek/Hebrew vocabulary plan" | `original-languages/biblical_language_greek_hebrew_vocabulary_builder.md` |
| **Biblical theology method (audience A, P)** | |
| "What's the difference between biblical and systematic theology?" | `biblical-theology-method/biblical_method_biblical_vs_systematic_theology.md` |
| "Read this passage in redemptive-historical context" | `biblical-theology-method/biblical_method_redemptive_historical_reading.md` |
| "Compare Paul's and James's (or any two authors') theologies" | `biblical-theology-method/biblical_method_author_theology_comparison.md` |
| "What is the center of biblical theology?" | `biblical-theology-method/biblical_method_center_of_theology_debate.md` |
| **Theology research additions** | |
| "Analyze a creed/confession against biblical texts" | `theology-research/biblical_theology_creed_confession_analysis.md` |
| "What is the biblical basis for this worship practice?" | `theology-research/biblical_theology_worship_practice_biblical_basis.md` |
| "NT material on church government / polity models" | `theology-research/biblical_theology_church_government_polity.md` |
| **Ministry contexts — cross-domain bridges** | |
| "Scripture for grief/loss ministry (not therapy)" | `ministry-contexts/biblical_ministry_grief_and_loss_scripture_guide.md` |
| "Design a marriage enrichment Bible study" | `ministry-contexts/biblical_ministry_marriage_enrichment_study.md` |
| "Contextualize parenting passages (not proof-texting)" | `ministry-contexts/biblical_ministry_parenting_scripture_guide.md` |
| **Apologetics & intellectual engagement (audience P, A)** | |
| "Engage charitably with a specific intellectual objection" | `apologetics-engagement/biblical_apologetics_objection_engagement.md` |
| "Evidence for / challenges to biblical reliability" | `apologetics-engagement/biblical_apologetics_bible_reliability.md` |
| "Compare biblical worldview with another on a question" | `apologetics-engagement/biblical_apologetics_comparative_worldview.md` |
| "Frame a faith-and-science question across positions" | `apologetics-engagement/biblical_apologetics_faith_and_science.md` |
| "Prepare for a real apologetic conversation" | `apologetics-engagement/biblical_apologetics_conversation_prep.md` |
| "Present major theodicies and strongest objections" | `apologetics-engagement/biblical_apologetics_problem_of_evil_theodicy.md` |
| "Address an alleged biblical contradiction honestly" | `apologetics-engagement/biblical_apologetics_biblical_contradictions.md` |
| "Prepare for interfaith dialogue" | `apologetics-engagement/biblical_apologetics_other_religions_dialogue.md` |

---

**Audience legend used in subdirectory READMEs:** L = layperson/devotional · G = group/Sunday-school leader · P = pastor/preacher · A = seminary/academic · S = self-directed learner · M = ministry-context teacher.

**Expansion roadmap:** see [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md) for shipped and planned phases.

---

## Companion domain: `domain-discipleship/`

[`domain-discipleship/`](../domain-discipleship/) (33 prompts) covers the **one-to-one discipling
relationship and the program around it** — formation curriculum, a disciple's own growth arc, mentor
equipping and boundaries, pairing criteria and covenants, session design, and program operations
including safeguarding. It inherits this domain's tradition-neutral and anti-fabrication conventions
and routes all Scripture work back here rather than duplicating it.

**Which domain do you want?**

| You're doing | Domain |
|---|---|
| Working a passage, a word, a doctrine, a genre, a sermon | **this domain** |
| Designing a church teaching program, class, or curriculum quarter | **this domain** (`church-staff-ministry-ops/`) |
| Facilitating a Bible-study group | **this domain** (`group-leader-facilitation/`) |
| Studying the Bible for yourself | **this domain** (`learner-self-study/`) |
| Walking one person toward maturity over months, one to one | `domain-discipleship/` |
| Equipping, screening, or supporting the person doing that walking | `domain-discipleship/mentor-equipping/` |
| Matching mentors with people seeking growth, and the rules around it | `domain-discipleship/pairing-and-relationship/`, `program-operations/` |
| Building a staged formation curriculum for individuals or pairs | `domain-discipleship/curriculum-architecture/` |

Four prompts here sit closest to that boundary and are **cross-linked, not duplicated**:
`ministry-contexts/biblical_ministry_new_believer_discipleship_path.md` (a teacher designs a staged
path), `church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md` (congregation
scale), `church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md` (teaching program
scope), and `group-leader-facilitation/biblical_groupleader_apprentice_development.md` (grows a group
leader, not a discipler).

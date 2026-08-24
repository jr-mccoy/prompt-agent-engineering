# domain-biblical-studies — Expansion Roadmap

This domain launched with **39 prompts** across four practitioner-facing subdirectories
(`exegesis-interpretation/`, `study-methods-teaching/`, `sermon-devotional/`, `theology-research/`),
built on two load-bearing conventions: **tradition-neutral by default** and **anti-fabrication first**
(see [`README.md`](README.md)). This roadmap tracks what has shipped and what is planned.

## Conventions every phase inherits

- **Tradition-neutral:** describe and attribute competing readings to identifiable interpretive
  streams; never adjudicate. A user may declare a tradition to foreground it; alternatives stay visible.
- **Anti-fabrication first:** no invented citations, cross-references, original-language data,
  scholar/commentary/council attributions, statistics, or archaeological claims. Reference verses
  **by address**; the user supplies/verifies wording; the model never quotes Scripture or lexicons from
  memory. Highest-risk prompts carry a **STRONG-GUARD** banner.
- **Canonical prompt template:** frontmatter (title, category, description, 5 technique IDs, difficulty,
  tags, updated, related_prompts) → Objective → (optional guard banner) → When to use / When NOT to use →
  Audience → Inputs/Context → Constraints (Must / Must Not / Tradition-neutral stance) → Instructions
  (numbered steps) → Output Format → Verification → False-Positive Prevention → Techniques Used.

## Audience legend

L = layperson/devotional · G = group/Sunday-school leader · P = pastor/preacher · A = seminary/academic ·
**S = self-directed learner** (Phase 2) · **M = ministry-context teacher** (Phase 2).

---

## Phase 1 — Foundation (SHIPPED · 39 prompts)

| Subdirectory | Prompts | Coverage |
|---|---|---|
| `exegesis-interpretation/` | 12 | passage exegesis, word study, genre, historical-cultural & literary context, narrative & rhetorical analysis, ANE parallels, canonical/intertextual reading, beginner observation, multi-view map, translation comparison |
| `study-methods-teaching/` | 8 | inductive (OIA), SOAP, book overview, discussion guides, lesson plans, memorization & reading plans, thematic study |
| `sermon-devotional/` | 7 | expository sermon prep, illustrations, devotionals, meditation, prayer/journaling, series planning, application |
| `theology-research/` | 12 | topical/systematic synthesis, doctrine study, interpretive-views comparison, cross-reference/typology, difficult passages, background research, theme trajectory, historical theology, biblical ethics, book theology, source map, position stress-test |

---

## Phase 2 — Depth & Audience Reach (SHIPPED · ~32 prompts)

Phase 1 was entirely expert/professional-facing and its genre coverage was generic. Phase 2 adds
genre-specific depth, critical-reading and sermon-type tools, deeper original-language tooling, and two
new audience subsections (modeled on the audience-split expansions in `domain-healthcare-clinical/.../
medical-education/learner-self-study/` and `domain-legal/family-self-advocacy/`).

### A. Content depth (into existing subdirectories · 11)
- **`exegesis-interpretation/` (+6)** — genre-specific reading guides the generic genre prompt routes to:
  parable interpretation; prophecy & apocalyptic (STRONG-GUARD); Hebrew poetry & Psalms; wisdom
  literature; Old Testament law; epistle argument tracing.
- **`theology-research/` (+2)** — exegetical-fallacy detector (STRONG-GUARD); commentary evaluation
  (STRONG-GUARD on bibliographic data).
- **`sermon-devotional/` (+3)** — topical sermon prep; evangelistic message prep; occasional messages
  (funerals/weddings/dedications).

### B. `learner-self-study/` — self-directed individual learners (NEW · 9 · audience S)
Personal study & formation tools with a **boundary guardrail** (not pastoral counseling/crisis support;
acute distress routes to a pastor, licensed counselor, or emergency services): self-directed study plan,
character study, self-quiz/recall drill, doctrine self-exploration, honest-questions/doubt explorer,
study-tool skill builder, comprehension self-check, personal-application worksheet, reflection-journal
companion.

### C. `ministry-contexts/` — teaching specific groups (NEW · 7 · audience M)
Child-safety and care-conversation guardrails apply: kids' lesson builder, youth study designer,
new-believer discipleship path, seeker intro to the Bible, family devotions designer, special-program
session (VBS/camp/retreat), and biblical care-conversation foundations (STRONG-GUARD: not therapy;
mental-health/abuse/self-harm/crisis routes to professionals).

### D. `original-languages/` — deeper language tooling (NEW · 5 · audience A/P)
Highest fabrication-risk subdirectory; **every prompt carries a STRONG-GUARD banner** and treats all
morphology/lexical/syntactic data as verify-required: parsing/morphology helper, Greek syntax analysis,
Hebrew syntax analysis, discourse analysis, OT-in-NT usage. Cross-links (does not move) the existing
word-study prompt in `exegesis-interpretation/`.

---

## Phase 3A — Operational Depth & Audience Completion (SHIPPED · 27 prompts)

The single biggest gap after Phase 2 was the absence of operational/administrative workflows for people
who *run* a teaching ministry, plus missing group-leader facilitation depth, liturgical/seasonal content,
and age-demographic coverage. Phase 3A closes all four gaps.

### A. `church-staff-ministry-ops/` (NEW · 10 · audience P/G)

Artifacts church staff actually produce — the operational backbone behind teaching programs:

| Prompt | Audience | Difficulty | What it does |
|---|---|---|---|
| `biblical_churchstaff_curriculum_scope_sequence.md` | P, G | intermediate | Multi-quarter scope-and-sequence for a church teaching program |
| `biblical_churchstaff_curriculum_selection_evaluation.md` | P, G | intermediate | Evaluate published curriculum against criteria (STRONG-GUARD: no fabricated product claims) |
| `biblical_churchstaff_teacher_training_plan.md` | P, G | intermediate | Train Bible-study volunteers: hermeneutics basics, classroom mgmt, child safety |
| `biblical_churchstaff_multi_service_teaching_coordination.md` | P | intermediate | Coordinate consistent teaching across services/campuses/communicators |
| `biblical_churchstaff_annual_teaching_calendar.md` | P | beginner | Map preaching/teaching year integrating series, holidays, guest speakers |
| `biblical_churchstaff_volunteer_recruitment_role_design.md` | P, G | beginner | Design volunteer roles with descriptions, onboarding, time commitments |
| `biblical_churchstaff_small_group_launch_system.md` | P, G | intermediate | System design: group formation, leader training, curriculum cycle, reporting |
| `biblical_churchstaff_discipleship_pathway_design.md` | P | intermediate | Congregation-wide pathway from newcomer → mature → leader with stage gates |
| `biblical_churchstaff_midweek_program_design.md` | P, G | beginner | Sustainable midweek Bible-study/prayer format distinct from Sunday |
| `biblical_churchstaff_sermon_feedback_debrief.md` | P | intermediate | Post-sermon debrief: theological accuracy, delivery, improvement areas |

### B. `group-leader-facilitation/` (NEW · 7 · audience G/P)

Completes the group-leader experience beyond question generation — real facilitation challenges:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_groupleader_facilitation_dynamics.md` | G | intermediate | — | Manage silence, dominance, tangents, conflict, emotional disclosure |
| `biblical_groupleader_handling_hard_questions.md` | G, P | intermediate | — | Respond when leader can't answer or topic is controversial |
| `biblical_groupleader_heretical_claim_response.md` | G, P | advanced | STRONG | Gracious response to heterodox claims; "orthodox" = ecumenical-creed level |
| `biblical_groupleader_mixed_maturity_leveling.md` | G | beginner | — | Adapt study for groups spanning new believers to mature Christians |
| `biblical_groupleader_conflict_resolution.md` | G, P | intermediate | — | Navigate theological disagreement, personality clashes, group dynamics |
| `biblical_groupleader_hybrid_online_format.md` | G | beginner | — | Adapt Bible study for hybrid or fully online delivery |
| `biblical_groupleader_apprentice_development.md` | G, P | intermediate | — | Develop an apprentice leader with progressive responsibility |

### C. Additions to existing `sermon-devotional/` (+4)

Fills the liturgical/seasonal gap and the manuscript-to-delivery workflow:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_sermon_manuscript_draft.md` | P | intermediate | — | Convert outline to full manuscript with oral-delivery markers |
| `biblical_sermon_delivery_coaching.md` | P | intermediate | — | Self-coaching: pacing, notes vs. manuscript, nerves, self-assessment |
| `biblical_liturgical_calendar_devotional_series.md` | P, L, G | intermediate | STRONG | Devotional arc following Advent/Lent/Eastertide/Ordinary Time |
| `biblical_lectionary_sermon_prep.md` | P | intermediate | STRONG | Sermon from lectionary readings (user supplies readings; model never asserts them) |

### D. Additions to existing `ministry-contexts/` (+3)

Age-demographic coverage completing the ministry-context audience:

| Prompt | Audience | Difficulty | What it does |
|---|---|---|---|
| `biblical_ministry_mens_womens_study_designer.md` | M, G | intermediate | Gender-specific group study without stereotyping; gender-role texts tradition-neutral |
| `biblical_ministry_college_young_adult_study.md` | M, G | intermediate | Study addressing identity, vocation, doubt for 18-30 age group |
| `biblical_ministry_seniors_study_designer.md` | M, G | beginner | Study for older adults: legacy, loss, hope; accessibility considerations |

### E. Additions to existing `learner-self-study/` (+3)

Enrichment completing the self-directed learner pathway:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_learner_bible_reading_habit_builder.md` | S | beginner | — | Sustainable daily reading habit with accountability and gap recovery |
| `biblical_learner_book_of_the_bible_deep_dive.md` | S | intermediate | — | Extended multi-week single-book study with running questions log |
| `biblical_learner_compare_traditions_on_practice.md` | S | intermediate | STRONG | Self-directed exploration of how traditions approach a practice (baptism, communion, etc.) |

---

## Phase 3B — High-Value, Needs Guardrail Design (SHIPPED · 23 prompts)

Elevated fabrication, sensitivity, or scope-boundary risks. Build order reflects risk:
original-languages first (well-established guardrail patterns), apologetics last (hardest guardrail design).

### 1. Additions to existing `original-languages/` (+5 · all STRONG-GUARD)

| Prompt | Audience | Difficulty | What it does |
|---|---|---|---|
| `biblical_language_textual_criticism_primer.md` | A, P | advanced | How textual criticism works for a user-specified variant; no apparatus from memory |
| `biblical_language_canon_versification_differences.md` | A, P | advanced | Where canons and verse numbering diverge across traditions |
| `biblical_language_septuagint_usage.md` | A | advanced | MT vs. LXX divergences and theological significance; user supplies both texts |
| `biblical_language_aramaic_analysis.md` | A | advanced | Aramaic sections (Daniel 2-7, Ezra 4-7, etc.); syntax and vocabulary |
| `biblical_language_greek_hebrew_vocabulary_builder.md` | A, P, S | intermediate | Frequency-based vocabulary plan; all word-list data verify-required |

### 2. New `biblical-theology-method/` subdirectory (4 prompts)

Method-level prompts above exegesis, below systematics:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_method_biblical_vs_systematic_theology.md` | A, P | advanced | — | Clarify the distinction with a worked example on a user-specified doctrine |
| `biblical_method_redemptive_historical_reading.md` | A, P | advanced | STRONG | Read a passage within creation-fall-redemption-consummation; epoch schemes as positions |
| `biblical_method_author_theology_comparison.md` | A, P | advanced | STRONG | Compare two biblical authors' theologies; present tensions honestly |
| `biblical_method_center_of_theology_debate.md` | A | advanced | STRONG | Survey the "center of biblical theology" debate; proposals as verify-required positions |

### 3. Additions to existing `theology-research/` (+3)

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_theology_creed_confession_analysis.md` | A, P | advanced | STRONG | Analyze a creed/confession against biblical texts; user supplies text |
| `biblical_theology_worship_practice_biblical_basis.md` | P, A, G | intermediate | STRONG | Biblical basis for a specific worship practice across traditions |
| `biblical_theology_church_government_polity.md` | P, A | advanced | STRONG | NT material on church government; how polity systems claim biblical warrant |

### 4. Cross-domain bridges in `ministry-contexts/` (+3)

First cross-domain `related_prompts` links from biblical studies:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_ministry_grief_and_loss_scripture_guide.md` | M, P | advanced | STRONG + boundary | Scripture for grief/loss; honest about lament; route-to-professional guardrail |
| `biblical_ministry_marriage_enrichment_study.md` | M, P, G | intermediate | — | Couples' study handling patriarchal context and gender-role texts honestly |
| `biblical_ministry_parenting_scripture_guide.md` | M, P, G | intermediate | — | Parenting passages contextualized; no proof-texting Proverbs |

### 5. New `apologetics-engagement/` subdirectory (8 prompts · ship last)

Hardest guardrail challenge — tradition-neutrality under adversarial use. Custom STRONG-GUARD
banner addresses fabricated philosophical arguments, misrepresented positions of other worldviews,
and invented historical evidence:

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_apologetics_objection_engagement.md` | P, A | advanced | STRONG | Charitable engagement with a specific intellectual objection; steelman it genuinely |
| `biblical_apologetics_bible_reliability.md` | P, A | advanced | STRONG | Evidence for/challenges to biblical reliability; every factual claim verify-required |
| `biblical_apologetics_comparative_worldview.md` | P, A | advanced | STRONG | Compare biblical worldview with another on a specific question; never caricature |
| `biblical_apologetics_faith_and_science.md` | P, A, S | advanced | STRONG | Frame a faith-and-science question; present range of believing-scholar positions |
| `biblical_apologetics_conversation_prep.md` | P | intermediate | — | Prepare for a real apologetic conversation; practice listening |
| `biblical_apologetics_problem_of_evil_theodicy.md` | P, A | advanced | STRONG | Present major theodicies and strongest objections fairly |
| `biblical_apologetics_biblical_contradictions.md` | P, A | advanced | STRONG | Address an alleged contradiction honestly; where tension remains, say so |
| `biblical_apologetics_other_religions_dialogue.md` | P, A | advanced | STRONG | Interfaith dialogue prep; never fabricate claims about another religion |

---

## Now covered elsewhere — `domain-discipleship/` (2026-08-04)

One-to-one discipleship and mentorship territory was never named in this roadmap and is now built as a
separate top-level domain: [`domain-discipleship/`](../domain-discipleship/) (33 prompts). It inherits
this domain's tradition-neutral and anti-fabrication conventions, adds its own — **formation is not a
metric**, **a lay mentor is not a counselor**, **no hotline or statute from memory** — and routes all
Scripture, exegesis, and doctrine work back here.

**Do not build these here.** They exist there:

| Territory | Now at |
|---|---|
| One-to-one mentoring relationship design, covenants, first meetings, endings | `domain-discipleship/pairing-and-relationship/` |
| Mentor readiness, training, conversation skill, boundaries and referral, sustainability | `domain-discipleship/mentor-equipping/` |
| Staged formation curriculum for individuals and pairs, outcomes, multiplication | `domain-discipleship/curriculum-architecture/` |
| A disciple's own growth arc: self-assessment, plans, practices, stalls, returning after absence | `domain-discipleship/learner-pathways/` |
| One-to-one session design, question banks, responding to a hard disclosure, triads | `domain-discipleship/session-and-lesson/` |
| Pairing programs: matching criteria, safeguarding policy, onboarding, health review, mentor pipeline | `domain-discipleship/program-operations/` |

Four prompts in this domain sit adjacent and stay here, cross-linked from there:
`ministry-contexts/biblical_ministry_new_believer_discipleship_path.md`,
`church-staff-ministry-ops/biblical_churchstaff_discipleship_pathway_design.md`,
`church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md`, and
`group-leader-facilitation/biblical_groupleader_apprentice_development.md`.

Note that Phase 3C's **"Pastoral counseling Scripture layer"** item below now has a boundary on two
sides: clinical territory belongs to `domain-psychology/`, and lay mentoring relationships belong to
`domain-discipleship/mentor-equipping/`. What remains for this domain is the *Scripture-selection*
layer only.

---

## Phase 3C — Future Candidates (direction only · ~15-25 prompts)

Not designed in detail. Requires more user-demand signal or cross-domain coordination.

- **`academic-writing/`** (~5) — exegesis paper scaffold, thesis workshop, literature review plan,
  annotated bibliography builder (STRONG), peer-review self-check. Cross-links `domain-research-academic/`.
- **Digital Bible-study tools** (~3) — tool-category workflow guide (STRONG on feature claims),
  PKM for Bible study (cross-link `domain-productivity/`), audio/podcast learning integration.
- **Pastoral counseling Scripture layer** (~4-5) — pre-marital counseling Bible component,
  addiction/recovery Scripture engagement, spiritual formation practices, chaplaincy Scripture selection.
  Highest boundary risk — must not cross into `domain-psychology/` clinical territory.
- **Children's/youth curriculum depth** (~3-4) — age-graded Bible-story retelling, youth apologetics,
  intergenerational worship, special-needs inclusive teaching (cross-link `domain-parenting/`).
- **Jewish-Christian dialogue** (~2-3) — how Jewish tradition reads a specific OT text, Second Temple
  Judaism context for NT. High-value for scholarship; elevated risk of misrepresenting Jewish tradition.

---

## Cumulative prompt count

| Phase | New | Cumulative | Subdirectories |
|---|---|---|---|
| Phase 1 | 39 | 39 | 4 |
| Phase 2 | 32 | 71 | 7 |
| Phase 3A | 27 | 98 | 9 (+ `church-staff-ministry-ops/`, `group-leader-facilitation/`) |
| Phase 3B | 23 | 121 | 11 (+ `apologetics-engagement/`, `biblical-theology-method/`) |
| Phase 3C (future) | ~15-25 | ~136-146 | 12-13 |

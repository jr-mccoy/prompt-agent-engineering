---
title: "Education Domain: Guide-Section Audit & Recommendations"
category: education-teaching/meta
description: "Audit of domain-education-teaching and cross-domain assets, refocused on college students, adult learners returning to school, and career changers building new skills. Identifies cross-domain prompts to pull together and real authoring gaps."
status: audit-only-no-build
audience_priority:
  - college-students
  - adult-learners-returning-to-school
  - career-changers-and-self-directed-adults
scope_refined: "2026-05-13 — shifted from instructor/builder side to learner side"
audited: "2026-05-13"
audited_by: claude-prompt-curator
---

# Education Domain: Guide-Section Audit & Recommendations

**Scope:** Audit + recommendations only. No `guides/` content built yet.

**Priority audiences (refined 2026-05-13):**
1. **College students** — traditional undergrad and grad
2. **Adult learners returning to college** — non-traditional students, often working, often with families, often years out of academic writing
3. **Career changers / self-directed adult learners** — pivoting to a new field via degree, bootcamp, certs, MOOCs, or self-study

This audit replaces an earlier draft that prioritized higher-ed and corporate **trainers** (the instructor side). The user clarified the actual priority is the **learner side** at college / adult level.

---

## 1. What Currently Exists

### Inside `domain-education-teaching/`

| Layer | Count |
|-------|-------|
| Markdown files (total) | 140 |
| Root-level prompts (`teaching_*.md`) | 34 |
| Subdirectory prompts | 102 |
| Meta files at root | 4 (`README.md`, `field_guide.md`, `MAINTENANCE_BACKLOG.md`, `PROMPT_TEST_REVIEW.md`) |
| Subdirectories | 15 |
| **Learner-facing subdirs** (the relevant ones for this scope) | **7** — `learner-writing/`, `learner-reading/`, `learner-math-science/`, `learner-research/`, `learner-study-skills/`, `learner-time-discussion/`, `learner-language/` |
| **Learner-facing prompts total** | **40** |

The 40 learner-facing prompts are written for "middle school / high school / college" and enforce a strict Socratic stance: AI quotes student text, asks diagnostic questions, refuses to substitute prose. **Most are usable at college level as-is; a few need adult-aware framing.**

### Cross-Domain Assets Relevant to This Scope

A college-or-adult learner's actual needs span four domains. Inventory:

| Domain / Path | Prompts | Why relevant |
|---------------|--------:|--------------|
| `domain-education-teaching/learner-*/` | 40 | Writing, research, study skills, time mgmt — academic work itself |
| `domain-personal-development/career-transformation/` | 4 | Coordination-tax audit, role vulnerability, residual skills inventory, 90-day repositioning plan — **career changers** |
| `domain-personal-development/prompts/agency/` | 15 | Ownership, execution, skill-gap reframe, foundation session, proof-of-work portfolio, rapid-start, weekly review — **self-directed adult learning** |
| `domain-personal-development/prompts/identity/` | 7 | Confidence calibration, comparison/envy, values, life audit, purpose, taste development — **imposter calibration, returning-to-school reckoning** |
| `domain-productivity/deep-work/` | 20 | Focus parameters, calendar audit, future-self handoff, chunk-project-to-calendar, message triage — **working learner time architecture** |
| `domain-productivity/bottlenecks/` | 8 | Procrastination diagnostic, perfectionism ship threshold, capture/triage, PKM — **personal constraint diagnosis** |
| `domain-productivity/reviews/` | 3 | Weekly systems review, monthly cadence, time audit — **academic semester cadence** |
| `domain-prompt-engineering/skill-development/` | ~8 | Eval harness, four-discipline diagnostic, spec writing — **for adults learning how to use AI as a study partner** |
| `domain-education-teaching/higher-ed-corporate/` | 10 | Mostly instructor-side, but `hecorp_microlearning_module.md` and `hecorp_performance_support_job_aid.md` have learner-side application patterns |

**Net cross-domain count of directly relevant prompts: ~115 across 9 paths.**

This is the central audit finding: **no existing guide stitches these together for a college or adult learner.** They exist as 9 independent islands.

---

## 2. Findings

### 2A. The Core Gap: No Cross-Domain Adult-Learner Path

A 38-year-old career-changer enrolled in a part-time MS in Data Analytics, working 40 hr/wk, with two kids, needs prompts from *six* of the nine paths above to address one semester. **There is currently zero documentation that helps them assemble that kit.**

A traditional college junior writing a thesis needs prompts from at least three paths (`learner-writing/`, `learner-research/`, `deep-work/`). Same problem.

### 2B. Real Prompt Gaps (Nothing Exists Yet)

The following are needs that **no current prompt in any domain addresses**. Listed in priority order for this scope:

| # | Gap | Why it matters | Audience |
|---|-----|----------------|----------|
| 1 | **Returning-to-school cold start** | Adult years out of academic writing needs a structured ramp: syllabus decoding, time-on-task recalibration, academic-tone rehearsal, writing-rust diagnostic | Adult returning |
| 2 | **Working learner weekly time architecture** | 40-hr job + 9-credit semester + family is a different planning problem from `deep-work/` calendar audits aimed at knowledge workers | Adult returning, career changer |
| 3 | **Skill-pivot self-study plan design** | "I'm an accountant pivoting to data science — design a 6-month plan with milestones, evals, and evidence of competence" — currently no prompt builds this | Career changer |
| 4 | **Prior-learning assessment articulation** | Turn 15 years of work experience into a CPL / credit-for-experience portfolio or a graduate-school SOP | Adult returning |
| 5 | **Credential pathway decision** | Degree vs. certificate vs. bootcamp vs. MOOC vs. on-the-job — currently scattered fragments in productivity/career, no integrated decision prompt | Career changer |
| 6 | **Imposter calibration in age-mixed classrooms** | `identity_confidence_calibration.md` exists but is generic; adults at 35+ in classes of 19-year-olds have a specific shape | Adult returning |
| 7 | **Portfolio-while-learning workflow** | `agency_proof_of_work_portfolio.md` covers proof-of-work in general; doesn't address the *while-still-learning* case where students need to ship before mastery | Career changer |
| 8 | **Andragogy-aware study workflow** | Most learner-facing prompts assume traditional pedagogy. Adult learners differ: bring prior experience, need autonomy, need immediate relevance, learn better in problem-centered vs. content-centered framing | Adult returning, career changer |
| 9 | **Socratic-vs-direct decision rule** | The learner-facing prompts are strictly Socratic. Adults under time pressure (parent at 10pm) sometimes need a direct answer to keep moving. No prompt documents when to switch modes | All three audiences |

### 2C. Existing-Asset Issues (Carried Forward from Prior Audit)

| # | Issue | Severity | Impact on this scope |
|---|-------|---------:|----------------------|
| 1 | README is monolithic (1,113 lines) | High | Adult learners pressed for time will not read it; need short role-based front door |
| 2 | Stale prompt count ("19" — actual 136) | High | Erodes trust on first impression |
| 3 | Frontmatter inconsistent — 18 of 34 root prompts lack `techniques:` | Medium | Affects discovery for self-directed learners using JSON index |
| 4 | Learner-facing Socratic stance not codified centrally | Medium | Each of 40 prompts re-implements the rule; risk of drift |
| 5 | No subdirectory READMEs | Medium | Discovery requires reading filenames |
| 6 | Test coverage 6 of 130+ prompts | Medium | Quality assurance gap |
| 7 | Maintenance backlog dormant since 2026-03-07 | Low | 12 known-good fixes unshipped |

### 2D. What Works (Preserve)

- **40 learner-facing prompts** with shared Socratic stance — solid foundation for the college-student audience.
- **Cross-domain raw material is unusually strong.** Career-transformation, agency, deep-work, bottlenecks, and identity domains together cover most adult-learner non-academic needs. Just need to be aggregated.
- **`teaching_concept_clarity_adults.md`** at the root already targets adult learners specifically — proof the audience is on the maintainer's radar.

---

## 3. Recommendations: Proposed `guides/` Section

This proposal is shaped around three audience folders and a shared layer. Each audience folder contains a top-level GUIDE, workflow files for high-frequency jobs-to-be-done, and a `cross_domain_kit.md` that catalogs the non-education prompts a learner in that audience will need.

### 3A. Proposed Directory

```
domain-education-teaching/
└── guides/                                  # NEW — proposed
    ├── README.md                            # Front door: pick your audience
    │
    ├── college-students/
    │   ├── GUIDE.md
    │   ├── workflow_essay_draft_to_submit.md          # learner-writing chain
    │   ├── workflow_research_paper_full_arc.md        # learner-research + writing
    │   ├── workflow_exam_prep_finals_week.md          # learner-study-skills + reviews
    │   ├── workflow_stem_problem_solving.md           # learner-math-science chain
    │   ├── workflow_office_hours_and_class_discussion.md
    │   └── cross_domain_kit.md                        # deep-work, bottlenecks, identity
    │
    ├── adult-returning/
    │   ├── GUIDE.md
    │   ├── workflow_cold_start_return.md              # ★ NEW prompts will live here
    │   ├── workflow_working_learner_time_architecture.md   # ★
    │   ├── workflow_writing_rust_recovery.md          # ★
    │   ├── workflow_imposter_calibration_age_cohort.md   # ★
    │   ├── workflow_prior_learning_articulation.md   # ★
    │   └── cross_domain_kit.md
    │
    ├── career-changers/
    │   ├── GUIDE.md
    │   ├── workflow_skill_pivot_self_study_plan.md   # ★
    │   ├── workflow_credential_pathway_decision.md   # ★
    │   ├── workflow_portfolio_while_learning.md      # ★
    │   ├── workflow_proof_of_work_for_pivot.md       # adapts agency_proof_of_work_portfolio
    │   └── cross_domain_kit.md
    │
    └── shared/
        ├── andragogy_principles.md                    # ★ Adult-learning theory applied
        ├── socratic_vs_direct_decision.md             # ★ When to use which mode
        ├── ai_as_study_partner_integrity.md           # Academic integrity for self-directed adults
        └── prompt_index_for_learners.md               # Curated index across 9 paths
```

★ = file ships a **new prompt** that does not exist anywhere in the repo today. Other files are workflow guides that orchestrate existing prompts.

### 3B. Per-Audience Briefs

#### Priority 1 — College Students (`guides/college-students/`)

**What's already covered:** Most of what a traditional college student needs already exists across `learner-writing/` (9), `learner-research/` (4), `learner-study-skills/` (6), `learner-math-science/` (7), `learner-time-discussion/` (4), `learner-reading/` (5). The job is **orchestration, not new authoring.**

**Files to ship:**

| File | Purpose | New prompts needed |
|------|---------|--------------------|
| `GUIDE.md` | Front door. Map common college jobs → prompts | None |
| `workflow_essay_draft_to_submit.md` | Topic → thesis → outline → draft → revise → integrity self-check → submit | None — chains 6 existing prompts |
| `workflow_research_paper_full_arc.md` | Question refinement → search → sources → synthesis → outline → draft → bibliography | None — chains 7+ |
| `workflow_exam_prep_finals_week.md` | Mistake-log review → triage → spaced retrieval → test-day strategy | None — chains 5 |
| `workflow_stem_problem_solving.md` | Word-problem decoder → Socratic solver → error analysis → concept map | None — chains 4 |
| `workflow_office_hours_and_class_discussion.md` | Convert vague confusion into specific questions; prep discussion contributions | None — chains 2 |
| `cross_domain_kit.md` | Pointer to `deep-work/`, `bottlenecks/`, `identity/` prompts useful at college level | None |

**Outcome:** 7 files, zero new prompts authored. Pure orchestration. ~2 days of work.

#### Priority 2 — Adult Learners Returning to School (`guides/adult-returning/`)

**The gap-heavy audience.** Most needs here are not covered by existing prompts.

**Files to ship:**

| File | Purpose | New prompts needed |
|------|---------|--------------------|
| `GUIDE.md` | Front door for returning adults | None |
| `workflow_cold_start_return.md` | First 4 weeks back: syllabus decode, time-on-task recalibration, academic tone rehearsal | ★ 1 new |
| `workflow_working_learner_time_architecture.md` | Weekly time blocks under 40-hr job + family constraints | ★ 1 new |
| `workflow_writing_rust_recovery.md` | Diagnose what's rusty (thesis construction, citation, paragraph cohesion) and rehearse it | ★ 1 new |
| `workflow_imposter_calibration_age_cohort.md` | Specific to being 30/40/50+ in age-mixed classes | ★ 1 new |
| `workflow_prior_learning_articulation.md` | Turn career experience into CPL portfolio or SOP language | ★ 1 new |
| `cross_domain_kit.md` | Index into `deep-work/`, `identity/`, `bottlenecks/`, `agency/`, `career-transformation/` | None |

**New prompts to author:** 5 (suggested locations below)
**Outcome:** 7 files, 5 new prompts. ~5 days of work.

**Suggested authoring locations for the new prompts (a decision point):**
- Option A: All 5 in `domain-education-teaching/adult-learner/` (new subdir)
- Option B: Some in `domain-education-teaching/`, time-architecture one in `domain-productivity/deep-work/`, imposter one in `domain-personal-development/prompts/identity/`, prior-learning one in `domain-personal-development/career-transformation/`
- Option A is more discoverable for the target audience; Option B is more idiomatically organized. Recommend **Option A** for cohesion and ease of cross-referencing.

#### Priority 3 — Career Changers / Self-Directed Adult Learners (`guides/career-changers/`)

**Partial coverage, real gaps.** `career-transformation/` has 4 prompts that diagnose the pivot at a strategic level; `agency/` has 15 covering execution; **nothing currently builds the actual self-study curriculum or credential decision.**

**Files to ship:**

| File | Purpose | New prompts needed |
|------|---------|--------------------|
| `GUIDE.md` | Front door for career changers | None |
| `workflow_skill_pivot_self_study_plan.md` | Diagnostic on current state → target competence definition → 3/6/12-month plan with evidence milestones | ★ 1 new |
| `workflow_credential_pathway_decision.md` | Degree vs cert vs bootcamp vs MOOC vs OJT — for a specific pivot | ★ 1 new |
| `workflow_portfolio_while_learning.md` | Ship public artifacts before mastery; pick projects that compound | ★ 1 new |
| `workflow_proof_of_work_for_pivot.md` | Adapts `agency_proof_of_work_portfolio.md` for pivot context | None |
| `cross_domain_kit.md` | Index into `career-transformation/`, `agency/`, `identity/`, `bottlenecks/` | None |

**New prompts to author:** 3
**Outcome:** 6 files, 3 new prompts. ~3 days of work.

#### Shared (`guides/shared/`)

| File | Purpose | New prompt? |
|------|---------|-------------|
| `andragogy_principles.md` | Adult learning theory (Knowles, Mezirow): autonomy, experience, relevance, problem-centered, internal motivation — applied to prompt design | Authoring guidance, not a prompt |
| `socratic_vs_direct_decision.md` | Decision rule: when Socratic coaching is right, when direct answer is right. Resolves the tension adult learners feel under time pressure | Authoring guidance, not a prompt |
| `ai_as_study_partner_integrity.md` | Academic integrity for self-directed adult learners; how to use AI as a study partner without producing submittable work | Guide doc |
| `prompt_index_for_learners.md` | Curated cross-domain index pointing to ~80 prompts learners would actually use, organized by job-to-be-done | Index, not a prompt |

---

## 4. Suggested Build Order

If green-lit, the recommended sequence:

1. **`guides/README.md` + `guides/college-students/`** — fastest win, all orchestration, no new prompts. Unblocks the largest audience first. (~2 days)
2. **`guides/shared/andragogy_principles.md` + `socratic_vs_direct_decision.md`** — these inform the adult-returning and career-changer authoring. (~1 day)
3. **`guides/career-changers/`** — partial coverage already; needs 3 new prompts. Mostly composition work. (~3 days)
4. **`guides/adult-returning/`** — heaviest authoring lift; 5 net-new prompts. (~5 days)
5. **`guides/shared/ai_as_study_partner_integrity.md` + `prompt_index_for_learners.md`** — closing work. (~2 days)

**Total estimate:** ~13 days of focused authoring across ~25 new files, of which **9 are new prompts** and 16 are guide/workflow documents that orchestrate existing prompts.

---

## 5. Out-of-Scope but Worth Noting

1. **README.md should shrink.** Move wave histories to CHANGELOG; reduce catalog density once `guides/` is the front door.
2. **18 root prompts need frontmatter upgrade** to match the Wave 1/2/5/6 schema.
3. **Maintenance backlog needs an owner.** 12 known-good fixes dormant for 2 months.
4. **Subdirectory READMEs.** Each of 15 subdirs would benefit from a short README.
5. **Test coverage extension** to the 100+ wave prompts.
6. **K-12 audience is not abandoned by this scope shift.** All K-12-targeted prompts remain in place; they just aren't the focus of the new `guides/` section. A future `guides/k12-teachers/` and `guides/instructional-designers/` could be added.

---

## 6. Decision Points

Three calls would unblock construction:

1. **Build all three audience folders + shared, or start with one audience to validate the structure?** (Recommend: start with `college-students/` since it ships fastest with zero new prompts and proves the pattern.)
2. **Place the 9 new prompts inside `domain-education-teaching/adult-learner/` (new subdir, cohesive) or spread them across the idiomatic domains (productivity, identity, career-transformation)?** (Recommend: cohesive subdir for discoverability.)
3. **Should the cross-domain index file ship as a markdown doc, or as an enrichment to `PROMPT_INDEX.json`?** (Recommend: both — markdown for human browsing in the guide, JSON enrichment for programmatic access.)

---

*Audit complete. No files created in `guides/`. Awaiting direction on construction.*

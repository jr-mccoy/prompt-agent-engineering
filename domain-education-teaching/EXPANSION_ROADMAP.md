# Expansion Roadmap — `domain-education-teaching/`

**Status as of 2026-08-28:** ✅ Reorganization shipped in full. 267 prompts moved from a
flat 24-subdirectory layout — 34 of them loose at the domain root — into three audience
tracks: `instructor/` (104), `program/` (41), `learner/` (122). No prompts were added,
removed, or rewritten; this was a filing and naming change plus a frontmatter pass.

**Filing convention.** One prefix per track — `teaching_`, `program_`, `learn_` — with
the subdirectory carrying the finer signal. This follows the `domain-negotiation/` and
`domain-written-advocacy/` precedent ("no subdirectory prefix"), and replaces the ~21
prefixes the domain had accumulated (`teachsubj_`, `learnstudy_`, `hecorp_`, `classops_`,
`edtech_`, `learnwrite_`, `learnread_`, `learnlang_`, `learnsci_`, `learnmath_`,
`learnresearch_`, `learntime_`, `learndisc_`, `learner_`, `adult_`, `inclusive_`,
`advising_`, `grading_`, `assessment_`, `workflow_`, and 18 files with no prefix at all).

The one sanctioned second prefix is **`learn_workflow_*`** in `learner/guides/`. Those 16
files are chain wrappers that sequence other prompts (they carry `chain_length` and
`estimated_time`), not prompts that stand alone. The distinction is also load-bearing
mechanically: without it, a flat rename collided 8 filenames, because almost every
`adult-learner/adult_X.md` prompt has a `guides/*/workflow_X.md` wrapper around it.

**Scope discipline.** Subdirectories target the repo's 3–10 band. Three exceed it, each
deliberately:

| Subdirectory | Count | Why it stays whole |
|---|---|---|
| `program/curriculum-design/` | 18 | Shipped as one coherent wave with its own README and dense internal cross-references. Splitting fragments them for no navigational gain. |
| `learner/study-by-discipline/` | 13 | One or two prompts per discipline (maths, science, history, humanities, language, law, medicine, nursing). Splitting by discipline yields eight directories of 1–2 files. |
| `instructor/higher-ed-corporate/` | 11 | One over the band, and a single audience (university and workplace delivery). Not worth a seam. |

---

## Shipped architecture

```
domain-education-teaching/
├── README.md                        ✓ (rewritten: 1,145 → 208 lines of prose + generated tables)
├── EXPANSION_ROADMAP.md             ✓ (NEW — this file)
├── field_guide.md                   ✓ (+684: absorbed the README's craft half)
├── meta/                            ✓ (NEW — 3 relocated docs + the reorg map)
│
├── instructor/                      104   teacher / lecturer / corporate trainer
│   ├── lesson-planning/               6   ✓ (all relocated from the domain root)
│   ├── explanation-craft/             9   ✓ (all relocated from the domain root)
│   ├── response-cycle/                5   ✓ (all relocated from the domain root)
│   ├── assessment-items/              8   ✓ (split from assessment/ 23)
│   ├── assessment-design/             9   ✓ (split from assessment/ 23, +1 from root)
│   ├── assessment-analysis/           7   ✓ (split from assessment/ 23)
│   ├── grading-feedback/              8   ✓ (+1 from root)
│   ├── reporting-communication/       2   ✓ (NEW dir — relocated from the domain root)
│   ├── student-support/               8   ✓ (NEW dir — merges inclusive/ 4 + advising/ 2 + 2 root)
│   ├── classroom-ops/                 3   ✓
│   ├── ed-tech/                       6   ✓ (+1 from root)
│   ├── higher-ed-corporate/          11   ✓ (+1 from root)
│   └── subject-pedagogy/             22   ✓ (split by subject, was one flat dir)
│       └── ela/ 7  math/ 5  science/ 4  social-studies/ 4  world-languages/ 2
│
├── program/                          41   dean / curriculum director / accreditation
│   ├── curriculum-design/            18   ✓ (renamed teaching_ → program_)
│   ├── outcomes-assessment/           8   ✓ (was program-outcomes-assessment/)
│   ├── accreditation-review/          5   ✓ (was accreditation-program-review/)
│   ├── faculty-development/           5   ✓
│   └── evaluation-analytics/          5   ✓ (was program-evaluation-analytics/)
│
└── learner/                         122   the student, studying alone
    ├── note-taking/                   4   ✓ (split from learner-study-skills/ 35)
    ├── memory-and-recall/             8   ✓ (split from learner-study-skills/, +2 root)
    ├── self-assessment/               8   ✓ (learner-assessment/ 3 + 4 study-skills + 1 root)
    ├── exam-prep/                     8   ✓ (split from learner-study-skills/ 35)
    ├── study-by-discipline/          13   ✓ (split from learner-study-skills/ 35)
    ├── tutoring/                      9   ✓ (flattened from 7 thin subdirs, +3 root)
    ├── stuck-and-confused/            8   ✓ (NEW dir — split out of learner-tutoring/)
    ├── writing/                       9   ✓
    ├── reading/                       5   ✓
    ├── math-science/                  7   ✓
    ├── language/                      5   ✓
    ├── research/                      4   ✓
    ├── time-and-discussion/           4   ✓ (merged learntime_ + learndisc_)
    ├── adult-learner/                 9   ✓
    └── guides/                       21   ✓ (chain wrappers, keeps its 4 children)
```

---

## What moved, and why

The complete file-by-file mapping is committed at
[`meta/REORG_MAP.tsv`](meta/REORG_MAP.tsv) — 267 lines of `old_path<TAB>new_path`,
validated as total and injective before anything was moved, and used as the single
source for the `git mv` pass, the reference rewrite, and the `category:` update.

Four decisions in that map were judgement calls rather than mechanical moves:

1. **The six `teaching_study_*` files moved from instructor to learner.** They carried an
   instructor prefix but are college-student study tools — a Socratic tutor, a concept
   teacher, practice problems, a flashcard generator, a study guide builder, a knowledge
   tester. They are now in `learner/tutoring/` and `learner/memory-and-recall/`. These
   were among the most cross-referenced files in the domain, so this is the change most
   likely to surprise someone returning to an old path.

2. **`learner-tutoring/` split rather than flattened.** Its 14 files sat in seven
   subdirectories of 1–4 files each, organized by subject. But the files do not really
   differ by subject — they differ by *what the learner needs*. Nine are forward
   instruction ("teach me this") and are now `learner/tutoring/`; eight are repair after
   a failure ("I'm stuck, I got it wrong") and are now `learner/stuck-and-confused/`.
   That is a routing distinction a learner can actually answer about themselves.

3. **`inclusive/` and `advising/` merged into `instructor/student-support/`.** Two files
   and four files respectively, both about supporting individual students beyond core
   instruction, alongside the IEP and behaviour prompts that were loose at the root.

4. **`assessment/` split three ways** — writing items, designing the instrument, reading
   the results. At 23 files it was the second-largest directory and mixed three distinct
   jobs done at three different times.

---

## Explicitly not gaps (already covered — cross-link, never duplicate)

| Looks missing here | Actually lives at |
|---|---|
| Health-professions education, OSCEs, PBL cases, ACGME milestones | `domain-medical-education/` — including its own 37-prompt learner-self-study track |
| Programme-level CBME, EPAs, residency curriculum mapping | `domain-medical-education/educator-curriculum-design/` |
| Teaching research methods, journal clubs, undergraduate lab courses | `domain-science/teaching-research-methods/` |
| Self-directed learning with no institution attached | `domain-learning/` |
| Learning and teaching programming | `domain-learning-coding/` |
| The parent's side of school (504 meetings, teacher emails, homework) | `domain-parenting/` |
| Sunday school, catechesis, discipleship curricula | `domain-biblical-studies/`, `domain-discipleship/` |
| Writing books *for* children | `domain-childrens-writing/` |
| Printable worksheet **images** | `domain-image-generation/worksheet-generators/` |
| Focus, time architecture, procrastination underneath a study plan | `domain-productivity/deep-work/`, `domain-productivity/bottlenecks/` |
| Identity, confidence and agency work for adult learners | `domain-personal-development/` — cross-linked from `learner/guides/*/learn_workflow_cross_domain_kit.md` |

---

## Conventions for whoever authors from this list

- Decide the **track first** by asking who holds the prompt: hands it to students
  (`instructor/`), hands it to a committee (`program/`), or uses it alone to learn
  (`learner/`). Then pick the subdirectory. The prefix follows from the track.
- `learner/` prompts hold a **Socratic stance**: they coach, refuse to produce
  submittable work, and never hand over a final answer, thesis, paragraph, or citation.
  See `learner/guides/shared/learn_socratic_vs_direct_decision.md` for when direct
  answering is legitimate, and `learn_ai_as_study_partner_integrity.md` for the
  integrity boundary. Do not author a learner prompt that ignores these.
- `program/` prompts must not state accreditor criteria, statutory requirements, or
  standards text from memory — the user supplies the framework and version, and the
  prompt structures work against it.
- Full frontmatter or it does not ship: eight fields, bare technique IDs validated
  against `techniques/MASTER_TECHNIQUE_INDEX.md`, `related_prompts` as three
  repo-absolute paths, `category` equal to the directory.
- Adding a prompt means regenerating the README's tables (they are generated from the
  tree, so they cannot drift stale the way the old `(19)` table did) and rerunning
  `scripts/generate_prompt_index.py`.

---

## Deferred — candidate future work (not yet built)

Recorded rather than built, because this pass was explicitly a reorganization.

1. **A `reasoning:` frontmatter block.** 199 prompts repo-wide carry the machine-readable
   `reasoning:` block (styles, stakes, horizon, uncertainty, mode); none of this domain's
   267 do. It is the current gold-standard marker in `domain-negotiation/`,
   `domain-reasoning-craft/` and `domain-psy-ops/`, and this is now the largest domain
   without it.
2. **Verification and False-Positive Prevention sections.** Only a handful of prompts here
   have one (`teaching_iep_goal_writer.md` is the model). The gold-standard house style
   closes every prompt with an 8-item false-positive list and a verification checklist.
3. **`instructor/reporting-communication/` is thin at 2.** Family-facing communication
   plausibly supports conference prep, difficult-conversation scripts, and multilingual
   family outreach — the last cross-linking `domain-parenting/`.
4. **`program/` has no student-success or retention track.** `evaluation-analytics/` has
   the early-warning system, but advising-at-scale, retention intervention design, and
   transfer-pathway articulation are unrepresented.
5. **The `updated:` dates are now stale** for the 24 files whose frontmatter was
   backfilled; they record when the prompt body was last touched, not the backfill. Left
   deliberately — the body did not change — but worth a decision if the field is ever
   used for freshness auditing.

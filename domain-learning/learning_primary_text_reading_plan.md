---
title: "Primary Text Reading Plan — Getting Through One Hard Classic on Your Own"
category: learning/reading
description: "Build a plan for one difficult classic an adult has already chosen (Kant, Thucydides, Spinoza, Middlemarch): pacing set by a timed test read, scaffolds built before starting (a structure map, a terms-of-art glossary, a one-sentence restatement per section), a rule for when to open a secondary source and when not to, a stall protocol and restatement checkpoints; distinct from choosing what to read (learning_reading_list_curator.md) and from annotating a passage (learn_annotation_coach.md)."
techniques:
  - DT-01
  - ED-01
  - DS-06
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reading-plan
  - classics
  - primary-texts
  - self-study
  - humanities
  - pacing
  - stalled-reading
  - great-books
  - understand-philosophy
updated: "2026-09-24"
reasoning:
  styles: [analytic, systems, strategic]
  stakes: low
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: solo
  output_format: [structured, spec]
  user_role: [individual, learner]
  mode: [plan, rehearse]
related_prompts:
  - domain-learning/learning_reading_list_curator.md
  - domain-education-teaching/learner/reading/learn_annotation_coach.md
  - domain-learning/learning_concept_explanation_audit.md
---

# Primary Text Reading Plan — Getting Through One Hard Classic

**Objective:** Turn "I have always meant to read the *Critique of Pure Reason*" into a paced plan that survives the week the text stops making sense. The pace comes from how fast the learner actually reads this text. Scaffolds are built before they are needed, secondary sources are used on a rule and not in a panic, and each section ends with a restatement the learner can check.

**When to Use:**
- You have already chosen one hard primary text: philosophy, history, political theory, scripture-adjacent classics, or a dense novel.
- You have started it before and stalled, usually around the same place.
- You are reading alone, with no seminar to set the pace or explain the jargon.

**Not this prompt if…**
- You have not chosen the text yet, or want a whole field's reading sequence. Use `domain-learning/learning_reading_list_curator.md`, which chooses and orders *works*. This prompt plans the reading of *one* work.
- You want help marking up a particular passage as you read. Use `domain-education-teaching/learner/reading/learn_annotation_coach.md`. This plan tells you *when* to annotate. That prompt coaches *how*.
- You are reading the Bible as a devotional or study plan. Use `domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md`.
- You want a group discussion guide. That lives in the education-teaching ELA material.

## Inputs / Context

1. **The text and edition.** Say which translation, if any, and whether it has an editor's introduction or notes.
2. **Why you are reading it.** Understanding the argument, the story, the influence, or bragging rights. Each implies a different depth.
3. **Hours per week**, realistically, and for how many weeks.
4. **A timed test read.** Read 5 pages from the middle at study depth and report the minutes taken and how much you could restate. If this is missing, ask for it before planning.
5. **Prior attempts**, and where they stalled.
6. **Background**: other works by this author, or in this field, that you have read.

## Method

1. **Set the depth target.** Choose one: *argument-level* (you can restate the thesis of each major part), *section-level* (you can restate each chapter's move), or *line-level* (you can explain difficult passages). Most self-learners need argument-level on a first read. Say so, because line-level is how plans die.

2. **Map the structure before reading (DT-01).** Divide the work into its real parts, which may differ from the chapter numbering: books, propositions, speeches, movements. Mark which parts are **load-bearing** (the rest depends on them) and which a first read may **skim** or **skip** (DS-06). Example: in Spinoza's *Ethics*, Part I carries the load, and the scholia can be read ahead of the demonstrations.

3. **Pace from the test read (CM-02).** Pages per session = (session minutes ÷ test-read minutes) × 5, then reduced by 20% for load-bearing parts. Fit this to the stated weekly hours with at least one session a week held in reserve. Never plan past the stated hours.

4. **Build the scaffolds up front (ED-01).**
   - **Structure map**: one page, kept at hand, updated as you go.
   - **Terms-of-art glossary**: words the author uses in a special sense, such as Kant's *a priori*, Hegel's *Aufhebung* or Thucydides' *prophasis*. Only the headwords are seeded. The learner writes the definition when they meet the term in context.
   - **One-sentence restatement** at the end of every section, in the learner's own words.

5. **Secondary-source rule.** Default: **primary first, then secondary, then back to the primary.** Attempt a section before reading any commentary on it. Allowed before starting: the edition's own introduction, *or* one short orientation to the text's aims, but not both, and never a chapter-by-chapter summary. Allowed mid-read: a commentary on a section *after* the stall protocol has fired. Name the kind of secondary source that fits, such as a companion volume, a lecture series or a guided commentary. Do not name specific titles unless the learner supplies candidates. Then say which of those candidates to use for what.

6. **Stall protocol.** When a passage will not yield:
   (1) re-read it once, slowly, aloud;
   (2) write down what you *do* understand and the exact sentence where it breaks;
   (3) mark it and read on two pages, because later passages often explain earlier ones;
   (4) if the section's restatement is still impossible, open the secondary source for **that section only**.
   A stall is not permission to read the summary of the whole book.

7. **Checkpoints (QA-01).** At each load-bearing part, the learner writes a 3-sentence restatement of the argument so far without the text open, then checks it against the text. Run `domain-learning/learning_concept_explanation_audit.md` on any restatement that feels fluent but vague.

8. **Plan the re-read.** State now which parts deserve a second pass after finishing, and why. A first read of a classic is a survey, and the plan should say so.

## Output Format

```
# Reading plan — [title], [edition/translation]
Depth target: [argument / section / line] — reason: …
Budget: [h/week] × [weeks]; test read: [5 pages in N min]

## Structure map
| Part | What it does | Load-bearing / skim / skip | Pages |

## Schedule
| Week | Sessions | Pages | Part | Checkpoint? |
Reserve: [n session/week]

## Scaffolds
- Glossary headwords to seed: …
- Restatement habit: one sentence per [section unit]

## Secondary-source rule
Before starting: [one item or none] | Mid-read: after stall protocol, for [section] only |
Kind of source to use: …

## Stall protocol
[the four steps, adapted to this text]

## Checkpoints
- After [part]: 3-sentence restatement, without the text open

## Second pass
- [part]: reason …
```

## Verification

- [ ] The pace comes from the learner's own timed test read, not a generic pages-per-hour rate.
- [ ] Total planned hours are at or below the stated budget, with reserve.
- [ ] Load-bearing parts are named, and the skim/skip choices are explicit.
- [ ] The secondary-source rule says what is allowed before, during and after, and bans whole-book summaries up front.
- [ ] No specific secondary title is recommended unless the learner supplied it.
- [ ] A checkpoint falls at every load-bearing part.
- [ ] The stall protocol ends in a scoped action, not "look it up".

## False-Positive Prevention

1. **Summary-first reading.** Reading the SparkNotes version first feels like preparation, but it replaces your reading with someone else's. That is why the secondary-source rule exists.
2. **Chapter-order pacing.** Equal pages per week assumes every part is equally hard. Load-bearing parts get the 20% reduction.
3. **Line-level ambition on a first read.** It is the most common reason a classic is abandoned by page 60.
4. **Invented scholarship.** Recommending a companion volume or commentator by name without the learner's candidates risks a title that does not exist. Name the kind of source instead.
5. **Glossary as a vocabulary list.** Dictionary definitions of an author's terms of art are usually wrong for that author. The learner defines each term from its use in the text.
6. **Fluent but empty restatement.** A restatement that reuses the author's words has not been checked. Require the learner's own words.
7. **No reserve.** A plan with every session full fails the first week that life intervenes.

## Example Output

```
# Reading plan — Thucydides, History of the Peloponnesian War, [translation as supplied]
Depth target: argument — why Athens lost, and how Thucydides builds that case. Line-level is for the second pass.
Budget: 4 h/week × 10 weeks; test read: 5 pages in 22 min

## Structure map
| Part | What it does | Status | Pages |
| Book 1 | Method, causes, the "truest cause" | Load-bearing | [from edition] |
| Book 2 | Funeral Oration, plague | Load-bearing | … |
| Book 3 | Mytilene debate, Corcyra stasis | Load-bearing | … |
| Books 4–5 | Pylos, the Melian Dialogue (5.84–116) | Skim, except Melos | … |
| Books 6–7 | Sicilian expedition | Load-bearing | … |
| Book 8 | Unfinished aftermath | Skim | … |

## Schedule
4 × 60-min sessions; pace ≈ (60 ÷ 22) × 5 ≈ 13 pages, ≈ 10 on load-bearing books.
Reserve: 1 session/week kept free.

## Scaffolds
- Glossary headwords: prophasis, stasis, logos/ergon, tyche
- One sentence per speech or episode

## Secondary-source rule
Before: the edition's introduction only. Mid-read: a commentary on a single speech after the stall protocol.
Kind: a book-by-book companion or a lecture series. Tell me which you own and I'll assign it.

## Stall protocol
Speeches are where stalls happen: (1) re-read aloud; (2) name the speaker's claim in one line;
(3) read the narrative that follows, which often shows whether the speech was right; (4) commentary on that speech only.

## Checkpoints
After Books 1, 3 and 7: 3-sentence restatement of "why Athens is losing," text closed.

## Second pass
Melian Dialogue and Mytilene debate at line level: they carry the work's argument about power and justice.
```

## Techniques Used

- **DT-01 (Hierarchical Task Breakdown):** the structure map breaks the work into real parts before any pacing.
- **ED-01 (Iterative Scaffolding):** the glossary, restatements and checkpoints build on each other as the reading goes on.
- **DS-06 (Prioritization Guidance):** load-bearing, skim and skip decisions put the effort where the argument lives.
- **CM-02 (Constraint Specification):** pace is bound to the measured test read and the stated weekly hours.
- **QA-01 (Self-Verification):** closed-text restatements at each load-bearing part check comprehension against the text.

## Related Prompts

- `domain-learning/learning_reading_list_curator.md`: choose the text before planning its reading.
- `domain-education-teaching/learner/reading/learn_annotation_coach.md`: the margin-level routine inside each session.
- `domain-learning/learning_concept_explanation_audit.md`: audit a restatement that feels fluent but vague.

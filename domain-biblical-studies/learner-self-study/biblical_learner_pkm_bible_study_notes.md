---
title: "Bible-Study Note System (PKM) — Verse-Address Backbone, Provenance on Every Note, Sized to Real Habits"
category: biblical-studies/learner-self-study
description: "Design a personal knowledge-management system for Bible study sized to the learner's real capture and retrieval habits: a consistent verse-address format as the linking backbone, six note types (passage observation, word study, cross-reference trail, questions log, sermon/lesson notes, prayer/reflection), mandatory provenance tags on every note so personal reflection, sourced claims and unverified AI output never blur, a weekly review loop, timed retrieval tests, a migration/exit plan, and anti-patterns. App-agnostic; never asserts a named app's features. A personal study tool, not pastoral counseling."
techniques:
  - ST-03
  - DS-26
  - RT-23
  - NE-09
  - DP-04
difficulty: intermediate
tags:
  - pkm
  - bible-study-notes
  - provenance-tagging
  - verse-linking
  - note-system-design
  - learner-self-study
  - organize-my-bible-notes
  - cant-find-my-study-notes
updated: "2026-10-05"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_pkm_second_brain_architecture.md
  - domain-medical-education/learner-study-systems/study_note_organization_system_designer.md
  - domain-biblical-studies/learner-self-study/biblical_learner_reflection_journal_companion.md
---

# Bible-Study Note System (PKM)

**Objective:** Build a note system for Bible study that the learner will actually use — small enough to maintain, linked by verse address, and tagged so that every line says where it came from: the text, the learner, a verified source, or an unverified AI.

> **Provenance guard.** Bible-study notes are where a remembered gloss, an AI-supplied cross-reference, and a personal reflection quietly turn into "facts" a year later. Every note — and every line that makes a claim — carries a provenance tag: **[TEXT: translation, user-supplied]**, **[MY OBSERVATION]**, **[MY REFLECTION]**, **[SOURCE: author/title/page — verified]**, **[SOURCE — unverified]**, or **[AI — unverified]**. The model never supplies Scripture wording, lexicon entries, commentary content, or citations to fill a note; untagged content is treated as unverified.

> **Product and copyright guard.** The design is app-agnostic. The prompt never states that a named note app supports linking, tagging, export, sync, or any price or licence — **[VERIFY: check the product's current documentation]**. Storing or sharing large amounts of copyrighted translation text in notes may be limited by the publisher — **[VERIFY the translation's permissions statement]**; never assume a translation's terms.

> **Boundary guardrail.** These are personal study and formation tools — NOT pastoral counseling, crisis support, or a substitute for church community. Acute spiritual distress, mental-health crisis, abuse, or self-harm routes to a pastor, a licensed counselor, or appropriate emergency services / professionals.

**When to use:**
- You have years of Bible notes scattered across apps, margins, and notebooks and cannot find what you wrote on a passage.
- You are starting a note system for Bible study and want it to last.
- Your notes mix your own ideas, things you read, and AI answers, and you can no longer tell which is which.

**When NOT to use:**
- You want a general personal-knowledge system not specific to Bible study — use `domain-productivity/bottlenecks/bottleneck_pkm_second_brain_architecture.md`. This prompt is distinct: it adds the verse-address backbone, Bible-study note types, and provenance tags, and borrows that prompt's retrieval-first sizing.
- You are a medical learner organising study notes — use `domain-medical-education/learner-study-systems/study_note_organization_system_designer.md`.
- You want guided journaling prompts for a passage (content, not a system) — use `domain-biblical-studies/learner-self-study/biblical_learner_reflection_journal_companion.md`; its output can land in the reflection note type here.
- You need to choose which digital tool categories to use at all — use `domain-biblical-studies/learner-self-study/biblical_learner_digital_tool_workflow_guide.md`.

**Audience:** Self-directed learners (S), pastors keeping a sermon/study archive (P), and seminary students (A). Intermediate.

---

## Inputs / Context

1. **Real capture habits.** How often you actually write notes (not how often you intend to), where, and in what form.
2. **Real retrievals.** The last few times you looked something up in your notes: what, why, and whether you found it. "Never" is a valid answer.
3. **Current state.** Where notes live now (apps, paper, margins), rough volume, and any structure already in use. Named apps are user-reported.
4. **Study rhythm.** Daily reading, book studies, sermons heard, lessons taught, coursework.
5. **Maintenance time.** Honest minutes per week for review.
6. **Reference format preference.** How you like to write addresses (e.g., abbreviated book names or full names); the model proposes options, you choose.
7. **AI use.** Whether you paste AI chat output into notes.
8. **Declared tradition (optional).** Affects only which sermon/lesson sources you note; stream labels stay descriptive.

---

## Constraints

### Must
- Size the system to the **observed** capture and retrieval habits; if notes are written twice a week, do not design a daily-note system.
- Make a **single, consistent verse-address format** (chosen by the learner) the primary link between notes, and show how ranges and multi-passage notes are written.
- Define each note type with a fixed template, and require a **provenance tag** on every note and on every claim line inside it.
- Default every untagged or AI-derived line to **[AI — unverified]** or **[SOURCE — unverified]** until the learner checks it (safe default).
- Include a weekly review loop, a timed **retrieval test**, and a **migration/exit plan** (plain-text or export path, [VERIFY] for the app).
- Name anti-patterns and the trigger that shows each one is happening.

### Must Not
- Quote Scripture, lexicon entries, or commentary from memory to populate examples or templates.
- Assert any named app's features, export formats, price, or licence.
- Recommend copying whole commentaries or whole chapters of a copyrighted translation into notes.
- Add note types, tags, or folders beyond what the learner's habits will maintain.
- Invent retention or learning statistics; any learning-science point is stated generally and hedged.

### Tradition-neutral stance (Must / Must Not)
- **Must:** record a source's interpretive stream on sourced notes where the learner identifies it, so readings from different traditions stay attributed; keep the learner's own view tagged as theirs.
- **Must Not:** label any source's stream as correct or suspect, or let a study Bible's notes enter as [TEXT].

---

## Instructions

### Step 1 — Retrieval-first audit
From the inputs, list what the learner actually retrieves and fails to retrieve. Sizing follows from this, not from aspiration.

### Step 2 — Reduce scope
Cut the design to the smallest form that serves those retrievals (NE-09): usually one capture location, 3–4 of the six note types, and one tag set. State what was cut and the signal that would justify adding it back.

### Step 3 — Address backbone
Offer two or three reference-format options; once the learner picks one, define rules for single verses, ranges, cross-chapter ranges, and multi-passage notes, plus a rule for verse-numbering differences between traditions ("record which translation's numbering").

### Step 4 — Note types and templates
Give a fixed template for each retained type: passage observation, word-study note, cross-reference trail, questions log, sermon/lesson note, prayer/reflection. Each template opens with the address, the provenance tag, and the date.

### Step 5 — Provenance rules
Define the tag set and three rules: (a) every claim line is tagged; (b) [AI — unverified] and [SOURCE — unverified] lines are promoted only after the learner checks them against a real text or source, recording what was checked; (c) quotations of translation text are short and marked [TEXT: translation, user-supplied].

### Step 6 — Review loop and retrieval test
Weekly review (fits the stated minutes): process the inbox, promote or delete unverified lines, add one cross-link. Monthly retrieval test: pick a passage at random; can everything written on it be found in under a minute?

### Step 7 — Exit plan and anti-patterns
State how notes leave the current tool (plain text with addresses in the first line) and list anti-patterns with triggers.

---

## Output Format

```
# Bible-Study Note System — [learner]

## Retrieval audit
Actually retrieved: [..] · Failed to retrieve: [..] · Capture rhythm: [..]

## Scope (what was cut, and the signal to add it back)
Kept: [..] · Cut: [..] → add back if: [..]

## Address backbone
Format chosen: [..] · Ranges: [..] · Multi-passage: [..] · Numbering note: [..]

## Note templates
### [Type] — template
Address: [..] · Provenance: [tag] · Date: [..]
[fields]

## Provenance tags and promotion rule
| Tag | Means | Promote to verified when |

## Weekly review (≤ [n] min) · Monthly retrieval test
## Exit plan
[export path — VERIFY: check the product's current documentation]
## Anti-patterns
| Anti-pattern | Trigger that shows it | Fix |
```

---

## Verification

- [ ] Design size matches observed capture and retrieval, not aspiration.
- [ ] One verse-address format, chosen by the learner, links all notes.
- [ ] Every template carries a provenance tag; untagged content defaults to unverified.
- [ ] AI output and unverified sources have an explicit promotion rule.
- [ ] No Scripture, lexicon, or commentary content supplied by the model; verses by address only.
- [ ] No named app credited with any feature; copyright handled as [VERIFY].
- [ ] Retrieval test and exit plan included.
- [ ] Source streams attributed, not ranked.

---

## False-Positive Prevention

❌ **DON'T:**
- Design a twelve-folder, thirty-tag vault for someone who writes notes on Sundays only.
- Fill an example word-study note with a gloss from memory.
- Let a pasted AI answer sit in notes untagged — in a year it will read like your own research.
- Copy a whole commentary section into a note "for later".

✅ **DO:**
- Start with the retrievals the learner already makes, and design backward.
- Write [AI — unverified] on pasted AI output by default, and record what you checked when you promote it.
- Keep a source note to the learner's summary plus author/title/page, with short excerpts only.

---

## Example Output

```
# Bible-Study Note System — learner writes notes 3×/week, retrieves before teaching

## Retrieval audit
Actually retrieved: notes on a passage before teaching it. Failed: a word-study note from last year
(in a different app). Capture rhythm: Tue/Thu reading, Sunday sermon.

## Scope
Kept: passage observation, sermon/lesson note, questions log. Cut: separate word-study and
cross-reference types → fold into passage notes; add back if more than 5 word studies a month.

## Address backbone
Format chosen (learner): abbreviated book + chapter:verse, e.g. "Rom 8:18–30". Ranges use an en
dash; multi-passage notes list addresses on line 1 separated by semicolons.

## Note template — passage observation
Address: Rom 8:18–30 · Provenance: mixed (tag per line) · Date: 2026-10-05
- [TEXT: learner's translation, user-supplied] v. 18 (learner pastes the verse)
- [MY OBSERVATION] one word seems to recur in this paragraph — count it in my translation.
- [SOURCE: author/title/page — verified] commentator's summary of the paragraph's structure (learner's words)
- [AI — unverified] suggested link to 2 Cor 4:17 — check in context before keeping.

## Weekly review (15 min) · Monthly test: random passage — found all notes in 40 s? pass.
## Exit plan: every note begins with its address in plain text [VERIFY: check the product's current documentation for export].
```

---

## Techniques Used

- **ST-03 (Output Format Specification):** Fixed note templates and a locked system blueprint make every note findable by the same fields.
- **DS-26 (Safe Defaults Pattern):** Untagged and AI-derived lines default to unverified until the learner checks them.
- **RT-23 (Input Provenance Tagging):** Every note and claim line carries a tag separating text, observation, reflection, verified source, and AI output.
- **NE-09 (Scope Reduction Pressure):** Cuts note types, tags, and folders to what observed habits will maintain, with explicit add-back signals.
- **DP-04 (Must-Not Constraints):** Forbids model-supplied Scripture, glosses, and commentary, named-app feature claims, and bulk copying of copyrighted text.

## Related Prompts

- `domain-productivity/bottlenecks/bottleneck_pkm_second_brain_architecture.md` — general retrieval-first PKM architecture for any subject.
- `domain-medical-education/learner-study-systems/study_note_organization_system_designer.md` — note-system design for medical learners.
- `domain-biblical-studies/learner-self-study/biblical_learner_reflection_journal_companion.md` — guided reflective journaling content for a passage or book.

---
title: "Series Continuity Audit — Build the Story Bible, Then Find Contradictions, Timeline Breaks, Knowledge Leaks, and Dropped Threads"
category: creative-writing
description: "Extract a story bible (characters, timeline, places, objects, world rules, and who-knows-what-when) from a manuscript or a series of books, then audit it for contradictions, impossible timing, knowledge leaks, dropped setups, and rule breaks — each finding cited to both conflicting locations, graded by severity, and screened for intentional unreliability; distinct from the worldbuilding framework (designing a world before drafting) and from the revision and self-editing guide (story-to-sentence editing passes)."
techniques:
  - CM-08
  - RT-05
  - OC-03
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - creative-writing
  - continuity
  - story-bible
  - revision
  - series-fiction
  - plot-holes
  - writing-a-sequel
  - timeline-mistakes
  - inconsistent-details
updated: "2026-09-24"
related_prompts:
  - domain-creative-writing/fiction/writing_worldbuilding_framework.md
  - domain-creative-writing/craft-tools/writing_revision_and_self_editing.md
  - domain-creative-writing/fiction/writing_novel_outlining_methods.md
---

# Series Continuity Audit

**Objective:** Produce two artefacts from an existing manuscript or series: a
story bible that records what the text has *actually established*, and an
audit that lists every place the text contradicts itself — each finding
located, quoted, graded, and checked against the possibility that the
contradiction is deliberate.

**When to Use:**
- A novel is drafted and you suspect the timeline, ages, or details drift.
- You are writing book three of a series and cannot remember what book one said.
- A copyeditor or reader found one continuity error and you want the rest.
- You are handing a series to a co-writer, ghostwriter, or adaptor.

**Not this prompt if:**
- You are designing a world *before* drafting →
  `domain-creative-writing/fiction/writing_worldbuilding_framework.md`
  (its consistency audit checks designed rules; this one checks the text).
- You want structural, scene, or line-level revision passes →
  `domain-creative-writing/craft-tools/writing_revision_and_self_editing.md`.
- You need a mystery's clue ledger → `writing_mystery_and_crime_craft.md`.
- You need a style sheet for spelling and capitalization only →
  `domain-agentic-resources/skills/non-coding/writing/editorial-quality-pass/`.

## Inputs

1. **The text**: full manuscript(s), or chapter summaries with key passages.
2. **Existing bible or notes**, if any (the audit updates it).
3. **Series order** and in-world chronology if it differs from publication order.
4. **Known deliberate devices**: unreliable narrator, lies, time travel,
   retcons the author has chosen, alternate timelines.
5. **Scope**: whole series, one book, or one thread.

## Method

1. **Extract the bible, text-first (CM-08).** Record only what the text states,
   with a location for each fact (book, chapter, and page or scene). Keep it as
   a persistent file the author updates each draft. Categories:
   - **Characters**: names and spellings, ages/birthdates, physical details,
     relationships, skills, injuries, possessions.
   - **Timeline**: dated or datable events, durations, seasons, travel times.
   - **Places**: geography, distances, layouts, who lives where.
   - **Objects**: where each significant object is and who has it.
   - **World rules**: magic, technology, law, institutions, costs.
   - **Knowledge states**: who learns what, when, and from whom.
   - **Open setups**: questions, promises, and Chekhov's guns not yet paid off.
2. **Cross-check each category (RT-05).** For every fact recorded twice or more,
   compare. A finding must quote or closely paraphrase *both* locations. No
   location, no finding.
3. **Run the specific tests.**
   - **Timeline arithmetic:** can the events fit the stated days and distances?
   - **Knowledge leaks:** does a character act on information before they
     could have learned it?
   - **Object tracking:** does anything appear where it cannot be?
   - **Rule breaks:** does a world rule bend without cost or acknowledgment?
   - **Dropped threads:** which open setups are never paid off or closed?
   - **Name drift:** spellings, titles, and nicknames.
4. **Screen for intent (QA-12).** Before listing a finding, check it against
   the author's deliberate devices and in-text explanations: a character lying,
   a misremembering narrator, an in-world time skip, a rule exception already
   explained. Mark as *intended?* if plausible; ask the author, do not assume.
5. **Grade severity (DS-06).**
   - **Critical**: breaks the plot's logic (the solution or climax depends on it).
   - **Major**: an attentive reader will notice (ages, deaths, rule breaks).
   - **Minor**: detail drift (eye color, a street name).
   - **Query**: possibly intended; needs the author's call.
6. **Propose the smallest fix.** For each finding, which location to change and
   the least invasive fix; note any knock-on facts in the bible.
7. **Tabulate (OC-03).** Output the bible and audit as tables so they can be
   kept and diffed across drafts.

## Output Format

```
# [Series/Book] — Story bible & continuity audit
Scope · Sources read · Deliberate devices noted
## Story bible
### Characters   | Name | Fact | Source |
### Timeline     | When | Event | Source |
### Places       | Place | Fact | Source |
### Objects      | Object | Holder/location | Source |
### World rules  | Rule | Cost/limit | Source |
### Knowledge    | Who | Learns what | When/from whom | Source |
### Open setups  | Setup | Source | Paid off? |
## Audit
| # | Type | Severity | Location A | Location B | Conflict | Intended? | Smallest fix |
## Summary
Counts by severity · Top three to fix first · Bible entries changed by the fixes
```

## Verification

- [ ] Every bible entry has a source location.
- [ ] Every finding cites two locations (or one location and the rule it breaks).
- [ ] Every finding was screened against the deliberate-devices list.
- [ ] Severity is assigned by effect on the story, not by count.
- [ ] Each fix names the location to change.
- [ ] The dropped-threads list distinguishes open-by-design (series hooks) from forgotten.

## False-Positive Prevention

1. **A character's false statement is not a continuity error.** Check who
   said it and whether they had reason to lie or be wrong.
2. **Unreliable narration is not drift.** When the narrator is established as
   unreliable, report the conflict as *intended?*.
3. **Series hooks are not dropped threads.** A setup left open at the end of
   book two may be a promise for book three; ask.
4. **Do not flag vague time as a contradiction.** "A few weeks later" cannot
   conflict with a date unless the arithmetic genuinely fails.
5. **Do not report facts from outside the text.** Author notes, interviews,
   and fan wikis are not the text; list them separately if supplied.
6. **Do not rewrite the plot.** Propose the smallest fix; larger structural
   changes belong to the revision prompt.
7. **Do not treat period or regional spelling variants as name drift** when
   the author has chosen them.

## Example

**Input (summary):** Book two of a fantasy trilogy. Deliberate devices: none
declared. Scope: characters, timeline, and knowledge for the heist subplot.

```
# The Glass Court (Book 2) — Story bible & continuity audit
Scope: heist subplot · Sources: B1 ch 1–30, B2 ch 1–24 · Devices: none declared

## Story bible (excerpt)
### Characters
| Name | Fact | Source |
|---|---|---|
| Wren Tallis | Left-handed | B1 ch3 ("drew with her left") |
| Wren Tallis | Age 19 at the flood | B1 ch1 |
| Osric | Blind in right eye | B1 ch12 |
### Timeline
| When | Event | Source |
|---|---|---|
| Day 0 | Flood; Wren is 19 | B1 ch1 |
| Day 0 + 2 yrs | Book 2 opens | B2 ch1 ("two winters since the flood") |
| B2 Day 1 | Crew leaves Harrowgate | B2 ch6 |
| B2 Day 2 | Crew arrives in the capital | B2 ch8 |
### Places
| Place | Fact | Source |
|---|---|---|
| Harrowgate → capital | "Six days' ride" | B1 ch20 |
### Knowledge
| Who | Learns | When/from | Source |
|---|---|---|---|
| Wren | The vault key is glass | B2 ch15, from Osric | B2 ch15 |

## Audit
| # | Type | Sev. | Location A | Location B | Conflict | Intended? | Smallest fix |
|---|---|---|---|---|---|---|---|
| 1 | Timeline | Major | B1 ch20 "six days' ride" | B2 ch6–8 arrives in 2 days | Travel impossible | No explanation in text | Change B2 ch8 to "on the sixth day," or add a river barge in ch6 |
| 2 | Knowledge leak | Critical | B2 ch15 Wren learns key is glass | B2 ch11 Wren packs "the cloth for the glass" | Acts before knowing; the heist logic depends on it | No | Move Osric's reveal to ch10 |
| 3 | Character | Minor | B1 ch3 left-handed | B2 ch19 "her right hand on the blade" | Handedness | Query — could be off-hand | Author's call |
| 4 | Character | Minor | B1 ch1 age 19 + 2 yrs | B2 ch4 "at nineteen, she…" | Age | No | B2 ch4 → "twenty-one" |
| 5 | Dropped thread | Query | B1 ch12 Osric's eye "will be seen to" | — | Never returned to | Possible book-3 hook | Ask author |

## Summary
Critical 1 · Major 1 · Minor 2 · Query 1. Fix first: #2 (heist logic), #1
(travel), #4. Bible changes: Wren's knowledge of the key moves to ch10.
```

## Techniques Used

- **CM-08 File-Based State Persistence** — the bible as a persistent, updatable file.
- **RT-05 Evidence-Based Reasoning** — every finding cites both locations.
- **OC-03 Markdown Table Specification** — bible and audit as diffable tables.
- **DS-06 Prioritization and Severity Guidance** — critical to query grading.
- **QA-12 False Positives Identification** — screening for lies, unreliability, and hooks.

## Related Prompts

- `domain-creative-writing/fiction/writing_worldbuilding_framework.md` — design the world's rules before drafting.
- `domain-creative-writing/craft-tools/writing_revision_and_self_editing.md` — structural to sentence-level revision.
- `domain-creative-writing/fiction/writing_novel_outlining_methods.md` — outlining future books against the bible.

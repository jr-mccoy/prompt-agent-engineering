---
title: "News Article — Inverted Pyramid With Sourcing and Attribution Discipline"
category: professional-writing/writing
description: "Write a straight news story from supplied reporting in inverted-pyramid order — a lede with the most newsworthy verified fact, a nut graf, supporting facts in descending importance, and background last — where every factual sentence is attributed to a named or described source from the reporter's notes, quotes are verbatim, unconfirmed items are withheld or labelled, and no quote, figure, or source is invented; distinct from narrative nonfiction (scene-led long-form), the newsletter issue (a voice-led single idea), and manuscript fact-checking (verifying a finished draft)."
techniques:
  - RT-05
  - IPC-07
  - QA-05
  - DS-06
  - CM-02
difficulty: intermediate
tags:
  - journalism
  - news-writing
  - inverted-pyramid
  - attribution
  - sourcing
  - lede
  - local-news
  - report-what-happened
  - community-newsletter
updated: "2026-09-24"
related_prompts:
  - domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md
  - domain-professional-writing/writing/writing_newsletter_issue.md
  - domain-professional-writing/writing/writing_unsourced_claim_disposition.md
---

# News Article — Inverted Pyramid

**Objective:** Turn a reporter's notes into a publishable news story that a
reader can stop reading at any paragraph and still have the most important
facts — and in which every fact can be traced back to who said it or where it
is documented.

**When to Use:**
- Community, trade, student, or organisational news: a decision, an incident,
  an announcement, a meeting, a result.
- You have notes, documents, and quotes, and need a story on deadline.
- A draft buries the news under background or reads like a press release.

**Not this prompt if:**
- The piece is long-form and scene-led → `domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md`.
- It is a voice-led newsletter issue → `domain-professional-writing/writing/writing_newsletter_issue.md`.
- The draft is written and needs claim-by-claim verification →
  `domain-research-academic/research_manuscript_fact_check_reconciler.md`.
- You have claims you believe but cannot source →
  `domain-professional-writing/writing/writing_unsourced_claim_disposition.md`.
- You are turning a long interview into a profile or Q&A →
  `domain-professional-writing/writing/writing_interview_transcript_to_feature.md`.

> **No-invention rule:** this prompt writes only from the supplied reporting.
> It never invents a quote, a source, a name, a title, a number, a date, a
> reaction, or "officials said". If the story needs a fact the notes do not
> have, it is listed under **Reporting gaps**, not written into the copy.

## Inputs

1. **Reporter's notes**: facts with where each came from (person + role, or
   document + date).
2. **Quotes**, verbatim, with speaker, role, date, and on/off-record status.
3. **Documents**: minutes, filings, press releases, data.
4. **Publication style**: word count, attribution style ("said" vs "says"),
   titles, numerals.
5. **Right-of-reply status**: who was asked to comment, when, and the response.

## Method

1. **Tag every note with its source (RT-05, IPC-07).** Each fact gets a short
   verbatim anchor from the note or document and a type: *on-record person*,
   *document*, *observed by reporter*, *unconfirmed*. Unconfirmed items do
   not enter the story as fact.
2. **Rank facts by news value (DS-06).** Impact on readers, novelty, conflict,
   proximity, timeliness. The top fact is the lede candidate.
3. **Write the lede.** One sentence, ≤35 words, who-what-when-where, with
   the most important verified fact. Attribute in the lede if the fact is a
   claim rather than a documented event.
4. **Write the nut graf.** Why it matters, in 1–2 sentences, sourced.
5. **Build the pyramid.** Supporting facts in descending order; strongest
   quote high (by paragraph 3–4); each paragraph a single point; background
   and history last.
6. **Attribute every claim (QA-05).** "Said" is the default verb; avoid
   "claimed", "admitted", "insisted" unless the notes support the connotation.
   Anonymous sources only if the notes record why anonymity was granted.
7. **Apply constraints (CM-02).** Quotes verbatim — only trimming with
   ellipses that don't change meaning. No adjectives the reporting does not
   support ("controversial", "shocking"). Right of reply: state who was asked
   and their response or non-response with the date.
8. **Cut-test.** Remove the last paragraph, then the next; confirm the story
   still stands at every cut.

## Output Format

```
HEADLINE: [factual, active, ≤ 12 words]
[Lede]
[Nut graf]
[Body paragraphs in descending importance]
[Background]

## Source ledger
| Para | Claim | Source (anchor) | Type |

## Reporting gaps (not in copy)
## Right-of-reply record
## Cut points (story stands after para …)
```

## Verification

- [ ] Every factual sentence maps to a row in the source ledger.
- [ ] Every quote is verbatim from the notes, with speaker and role.
- [ ] No unconfirmed item appears as fact.
- [ ] The lede contains the highest-ranked fact.
- [ ] Right of reply is recorded for anyone criticised.
- [ ] The story stands when cut from the bottom.

## False-Positive Prevention

1. **"Officials said" with no named official is invention unless the notes
   say it.** Name, describe precisely, or cut.
2. **A press release is a source, not a fact.** Attribute it: "the company
   said in a statement".
3. **A neat quote that isn't in the notes is fabrication**, even if it
   paraphrases something the person "meant".
4. **Loaded verbs editorialise.** "Admitted" implies wrongdoing; use "said"
   unless the reporting supports more.
5. **Burying the lede is not neutrality.** Background first is a structural
   failure, not balance.
6. **Balance is not both-sides filler.** Right of reply goes to people the
   story is about, not to invented opposing voices.
7. **Round numbers are still numbers.** "Nearly 200" needs a source figure.

## Example Output

```
HEADLINE: Riverside council votes to close Elm Street library branch in June

The Riverside town council voted 5–2 on Tuesday to close the Elm Street
library branch on June 30, citing a $410,000 repair bill for the building's
roof and heating system.

The closure leaves the town's east side without a library within walking
distance, according to a map in the council's own staff report, and the
branch's 1,900 active cardholders will be directed to the Main Street
library 3.2 miles away.

"We cannot justify putting more than $400,000 into a building we
would have to replace in ten years anyway," Councillor Dana Ruiz said during
the vote.

Councillor Tom Becker, who voted against, said the council had "not asked a
single east-side resident" before deciding. The staff report lists no public
consultation.

Library director Helen Park said in an email that staff will not lose jobs
and will move to Main Street. She did not say whether opening hours there
would change.

A resident petition to keep the branch open had 640 signatures when it was
presented at the meeting, according to the council clerk.

The Elm Street branch opened in 1962.

## Source ledger
| Para | Claim | Source (anchor) | Type |
|---|---|---|---|
| 1 | 5–2 vote, June 30, $410,000 | Minutes draft: "motion carried 5–2 … closure effective June 30"; staff report p.4 "$410,000" | Document |
| 2 | No library within walking distance; 1,900 cardholders; 3.2 miles | Staff report map p.6; p.2 "1,900 active cards"; p.6 "3.2 mi" | Document |
| 3 | Ruiz quote | Reporter's recording 41:10 | On-record person |
| 4 | Becker quote; no consultation listed | Recording 44:02; staff report (no consultation section) | On-record + document |
| 5 | Park: no job losses | Email 2026-09-23 16:12 | On-record person |
| 6 | 640 signatures | Clerk, in person after meeting | On-record person |
| 7 | Opened 1962 | Library website history page | Document |

## Reporting gaps (not in copy)
- Whether Main Street hours will extend — Park did not answer; follow-up sent.
- A resident saying "we'll have nowhere to go" — heard in the hallway, speaker
  unidentified → not used.

## Right-of-reply record
Mayor's office asked 09-23 14:00 for comment on the lack of consultation; no
response by deadline — add "did not respond" if the edit desk wants a line.

## Cut points
Story stands after paras 2, 4, and 6.
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — every fact typed and traced to its origin.
- **IPC-07 Verbatim Source Anchoring** — each ledger row carries a short anchor from the notes.
- **QA-05 Citation Requirements** — attribution in copy for every claim.
- **DS-06 Prioritization and Severity Guidance** — facts ranked by news value for the pyramid.
- **CM-02 Constraint Specification** — verbatim quotes, neutral verbs, right of reply.

## Related Prompts

- `domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md` — long-form narrative.
- `writing_newsletter_issue.md` — a voice-led single-idea issue.
- `writing_unsourced_claim_disposition.md` — claims you can't source.
- `domain-research-academic/research_manuscript_fact_check_reconciler.md` — verifying a finished draft.

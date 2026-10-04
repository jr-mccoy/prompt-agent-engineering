---
title: "Story Desk Edit — An Editor's Pass on a Reported Story: Lede, Nut Graf, Attribution, Fairness, Structure, and Legal-Risk Flags"
category: professional-writing/journalism
description: "Run the editor's desk edit on a reporter's filed story before publication: a one-sentence story test, journalism-specific smell tests (lede support, nut graf, attribution and anonymity, quote fidelity, numbers, loaded language, headline fit), a fairness check that every person or organisation criticised had a real chance to reply, legal-risk flags (defamation, crime allegations, privacy, protected identities, court reporting, image rights) held for a media lawyer rather than cleared, and a prioritised must/should/could edit list with queries to the reporter and a publish/fix/hold verdict."
techniques:
  - QA-18
  - DS-06
  - QA-05
  - CM-09
difficulty: intermediate
tags:
  - journalism
  - news-editing
  - desk-edit
  - attribution
  - fairness
  - defamation-risk
  - right-of-reply
  - edit-reporters-story
  - is-story-ready-to-publish
updated: "2026-10-02"
related_prompts:
  - domain-professional-writing/writing/writing_news_article_inverted_pyramid.md
  - domain-legal/ip/legal_defamation_publicity_risk_screen.md
  - domain-professional-writing/journalism/journalism_source_verification_log.md
---

# Story Desk Edit

**Objective:** Give an editor a fast, complete desk edit of a reported story — what the
story is, whether the copy proves it, whether it is fair, what could get the
publication sued, and the short list of changes and reporter queries that stand
between this draft and publication.

**When to Use:**
- A reporter has filed and you are the assigning, desk, or section editor.
- A student, community, trade, or newsletter publication without a legal department
  needs a disciplined pre-publication read.
- A freelancer wants to self-edit before filing, the way the desk will read it.
- **Not this prompt if** you are writing the story from notes — use
  `domain-professional-writing/writing/writing_news_article_inverted_pyramid.md`. For
  claim-by-claim checking against a source set, use
  `domain-research-academic/research_manuscript_fact_check_reconciler.md`; for checking
  the sources themselves, `journalism/journalism_source_verification_log.md`. For a full
  defamation and privacy screen to hand counsel, use
  `domain-legal/ip/legal_defamation_publicity_risk_screen.md`. For prose polish without
  news judgement, `writing/writing_precision_doc_edit.md`. This prompt is the editor's
  judgement pass and **flags** legal risk; it never clears it.

## Inputs / Context

1. **The filed story**, with headline and dek if written.
2. **The reporter's source notes or ledger** — who said what, which documents, what is
   on or off the record.
3. **Right-of-reply record** — who was approached, when, how, and what they said.
4. **Jurisdiction** of publication and of the people named (legal flags depend on it).
5. **House style** and length; story type (news, feature, profile, analysis).
6. **Anything the reporter flagged** as uncertain or sensitive.

## Method

1. **One-sentence story test.** Write what the story *is* in one sentence from the
   evidence. If the lede says something different — bigger, vaguer, or older — that
   is the first edit.
2. **Run the journalism smell tests (QA-18).** For each, mark pass / query / fix:
   - **Lede support** — the lede's claim is the strongest *verified* fact, and the body proves it.
   - **Nut graf** — why it matters, by paragraph 2–3 for news, 3–5 for a feature.
   - **Attribution (QA-05)** — every fact the reporter did not observe or document is
     attributed; contested claims carry attribution at the start of the sentence;
     "said" by default, not "admitted", "claimed", or "slammed".
   - **Anonymity** — each unnamed source has a recorded reason, the editor knows who it
     is, and the description is accurate without identifying them.
   - **Quotes** — quotation marks only for exact words that appear in notes or a recording.
   - **Numbers** — arithmetic re-done; percent vs percentage points; a base or
     comparison for every rate; "record" and "first" claims sourced.
   - **Loaded language** — adjectives and verbs the reporting does not support.
   - **Headline and dek** — say no more than the story proves.
3. **Fairness check.** List every person or organisation the story criticises or
   alleges something against. For each: were they told the *specific* allegation,
   given reasonable time to respond, and is their response (or the fact and date of
   no response) placed near the allegation — not in the last paragraph?
4. **Legal-risk flags (CM-09).** The editor flags; a media lawyer decides. Flag:
   - **Defamation** — a factual statement that harms an identifiable person's or
     organisation's reputation, whose proof rests on fewer than the sources needed.
   - **Crime allegations** — wording ahead of the legal process ("stole" vs "is charged
     with"); in some jurisdictions, reporting on active cases is restricted.
   - **Privacy** — health, sexuality, finances, children, or home address beyond what
     the story's public interest needs.
   - **Protected identities** — complainants in sexual-offence cases, minors in criminal
     or family proceedings: many jurisdictions bar identification, including by jigsaw.
   - **Court and official records** — a fair and accurate report of proceedings is
     usually protected; editorialising inside it is not.
   - **Images and documents** — rights to use, and whether publishing a document could
     expose a confidential source.

   Any flag → **HOLD for legal review**, with the sentence quoted and the concern named.
5. **Structure edit.** Propose a paragraph order map (e.g. 1, 2, 5, 3, 4, 7, 6) rather
   than rewriting the reporter's copy; mark where background can be cut.
6. **Prioritise (DS-06).** *Must-fix* (accuracy, fairness, legal) blocks publication;
   *should-fix* (lede, nut graf, structure) is done this edit; *could-fix* (style) only
   if time allows. Separate direct fixes (style, grammar) from **queries** that only the
   reporter can answer — an editor never supplies a missing fact.
7. **Verdict.** PUBLISH · PUBLISH AFTER FIXES (all must-fixes resolved, no legal flag) ·
   HOLD (reporting gap or legal flag), with what releases the hold.

## Output Format

```
# Desk edit — "[headline]" — [reporter], [date]
Story in one sentence: [...]
Lede matches? [yes | no → ...]

## Smell tests
| Test | Result (pass / query / fix) | Where | Note |
|---|---|---|---|

## Fairness
| Person / organisation | Allegation | Asked? when, how | Response placed | OK? |
|---|---|---|---|---|

## Legal-risk flags (for media lawyer — not cleared here)
| # | Sentence (quoted) | Concern | Suggested option for counsel |
|---|---|---|---|

## Structure
Proposed order: [...]; cut: [...]

## Edits
Must-fix: [...]
Should-fix: [...]
Could-fix: [...]
Queries to reporter: Q1 [...]

## Verdict
[PUBLISH | PUBLISH AFTER FIXES | HOLD] — released when: [...]
```

## Verification

- [ ] The one-sentence story was written from the evidence before the lede was judged.
- [ ] Every smell test has a result and a location.
- [ ] Every criticised party appears in the fairness table.
- [ ] Every legal flag quotes the sentence and routes to a lawyer; none is "cleared".
- [ ] No edit introduces a fact, quote, or number absent from the notes.
- [ ] The verdict follows from the must-fix list and the flags.

## False-Positive Prevention

1. **An edit is not a rewrite.** Restructure by paragraph map and queries; the byline
   is the reporter's.
2. **Not every negative fact is defamation risk.** A documented court verdict reported
   accurately is not the same as an unsourced allegation; flag what is weakly sourced,
   not everything unflattering.
3. **Don't "fix" a missing fact.** If the nut graf needs a figure the notes lack, it is
   a query, not an insertion.
4. **Balance is not both-sides filler.** Fairness is a reply from the people the story
   is about, not a quote from an invented opponent.
5. **Don't soften accurate findings into mush.** "Allegedly" sprinkled on documented
   facts weakens the story without protecting anyone.
6. **The editor is not the lawyer.** "Probably fine" on a legal flag is the failure this
   section exists to prevent.

## Example Output

Scenario: 780-word local story; families of residents at Oakview Care Home complain of
neglect; state inspection report (public) found 4 deficiencies; reporter has three
named family members, one unnamed former aide, and an emailed statement from the owner.

```
# Desk edit — "Families say Oakview neglected residents" — R. Okafor, 2026-10-01
Story in one sentence: A state inspection found four deficiencies at Oakview in August,
  and three families describe missed medication and slow call-bell responses.
Lede matches? No — the lede opens on a 2019 ownership change; the inspection is para 6.

## Smell tests
| Lede support | fix   | para 1 | lead with the August inspection + families |
| Nut graf     | fix   | —      | none; build from inspection summary p.2 (in notes) |
| Attribution  | query | para 4 | "staff were often drunk on shift" — whose claim? |
| Anonymity    | query | para 8 | former aide: reason for anonymity not recorded |
| Quotes       | pass  | —      | all three family quotes match recordings |
| Numbers      | fix   | para 9 | "deficiencies up 300%" = 1 → 4; say "from one to four" |
| Loaded words | fix   | para 3 | "callous owner" — unsupported adjective; cut |
| Headline     | fix   | —      | "neglected" states as fact; use "Families allege …; inspection finds four deficiencies" |

## Fairness
| Oakview owner (M. Reyes) | neglect; drunk staff | email 09-28, specific? NO — "for comment on
  your care home" | statement in last para | NO → re-approach with each allegation; 48 h |

## Legal-risk flags (for media lawyer — not cleared here)
| 1 | "staff were often drunk on shift" | single unnamed source, serious allegation against
  identifiable employees | source it, attribute narrowly, or cut |
| 2 | "Reyes, who let residents suffer" | factual imputation against a named person; not in
  inspection report | attribute to families, or cut |
| 3 | para 7 names a resident's dementia diagnosis | private health fact; consent recorded? | confirm consent or remove |

## Structure
Proposed order: new lede (inspection + families) · nut graf · 4 · 5 · owner response · 2 · 8 · 9;
cut the 2019 ownership history to one sentence at the end.

## Edits
Must-fix: legal flags 1–3; specific right of reply to Reyes; headline.
Should-fix: lede, nut graf, structure, "300%".
Could-fix: house style on ages and titles.
Queries to reporter: Q1 Who said "drunk on shift", and can anyone confirm? Q2 Why
  anonymity for the aide? Q3 Consent for para 7's diagnosis?

## Verdict
HOLD — released when Q1–Q3 are answered, Reyes has had 48 h on specific allegations,
and counsel has reviewed flags 1–3.
```

## Techniques Used

- **QA-18 Domain-Specific Smell Tests** — eight journalism checks a desk applies to every filed story.
- **DS-06 Prioritization and Severity Guidance** — must / should / could, with must-fix blocking publication.
- **QA-05 Citation Requirements** — attribution in copy for every claim the reporter did not observe or document.
- **CM-09 Authority Boundary Specification** — the editor flags legal risk; a media lawyer decides; only the reporter supplies facts.

## Related Prompts

- `domain-professional-writing/writing/writing_news_article_inverted_pyramid.md` — writing the story this edits.
- `domain-legal/ip/legal_defamation_publicity_risk_screen.md` — the fuller defamation and privacy screen to hand counsel.
- `domain-professional-writing/journalism/journalism_source_verification_log.md` — verifying the sources behind the story.

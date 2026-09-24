---
title: "Interview Transcript to Feature — Shape a Profile or Q&A Without Changing What Anyone Said"
category: professional-writing/writing
description: "Turn a cleaned interview transcript into a feature, profile, or edited Q&A under explicit quote-fidelity rules — verbatim direct quotes anchored to timestamps, stated limits on trimming and reordering, paraphrase that stays within what was said, no invented scene or interiority, and a quote ledger the subject or editor can check — distinct from transcript cleanup (fixing speech-to-text errors), narrative nonfiction (scene-led reporting from many sources), and a straight news story."
techniques:
  - IPC-07
  - CM-02
  - ST-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - interviewing
  - feature-writing
  - profile
  - q-and-a
  - quote-fidelity
  - journalism
  - turn-into-article
  - quote-accurately
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/content-creation/transcript-fixer/SKILL.md
  - domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md
  - domain-professional-writing/writing/writing_news_article_inverted_pyramid.md
---

# Interview Transcript to Feature

**Objective:** Produce a readable feature or Q&A from an interview in which
every direct quote is something the person actually said, every paraphrase is
something they actually meant, and the edits made along the way are declared.

**When to Use:**
- You interviewed someone for a profile, member spotlight, customer story,
  alumni feature, or edited Q&A.
- The transcript is long, circular, and full of false starts.
- A subject has complained before about being misquoted.

**Not this prompt if:**
- The transcript still has speech-to-text errors → run
  `domain-agentic-resources/skills/content-creation/transcript-fixer/` first.
  This prompt assumes the transcript is accurate and does not guess at mis-heard words.
- The piece weaves many interviews, documents, and scenes into long-form narrative →
  `domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md`.
- The interview produced news → `domain-professional-writing/writing/writing_news_article_inverted_pyramid.md`.
- You are synthesising many user-research interviews into themes →
  `domain-business-strategy/research/user_research_synthesis.md`.

> **Quote-fidelity contract:** direct quotes are verbatim. The only permitted
> edits are those listed under Method step 3 and declared in the ledger. No
> quote is composed, merged across answers into one sentence, or moved to
> answer a question it did not answer. No facts, scenes, or feelings beyond the
> transcript and supplied notes.

## Inputs

1. **Cleaned transcript** with timestamps and speaker labels.
2. **Format**: profile (third person, quotes woven in), edited Q&A, or
   first-person as-told-to; target length.
3. **Publication's quote policy**, if one exists (some allow trimming filler;
   some do not).
4. **Reporter's notes**: setting, observations, verified background facts.
5. **Agreements with the subject**: off-record passages, quote approval or not.

## Method

1. **Mark the transcript (ST-02).** Strike off-record passages first. Then
   tag candidate quotes: *story* (an anecdote), *view* (an opinion or
   insight), *voice* (how they talk), *fact* (a claim to verify).
2. **Select and rank (DS-06).** Pick the angle — the one thing the piece is
   about — and rank quotes by how much they serve it. Facts the subject stated
   about the world go on a verify list; do not print them as fact on their
   say-so alone.
3. **Apply the quote rules (CM-02).**
   | Edit | Direct quote | Paraphrase |
   |---|---|---|
   | Remove "um", "uh", false starts, stutters | Allowed if policy permits; declared | n/a |
   | Trim words mid-quote | Only with ellipsis, only if meaning unchanged | n/a |
   | Fix grammar or dialect | Not allowed — paraphrase instead | Allowed |
   | Combine two answers into one quote | Not allowed | Allowed, attributed |
   | Reorder sentences within a quote | Not allowed | n/a |
   | Bracketed clarification [the plant] | Allowed, minimal | n/a |
   | Q&A: tighten questions | Allowed; questions are the writer's | n/a |
   | Q&A: reorder answers | Allowed only if each answer stays with its question | n/a |
4. **Anchor every quote (IPC-07).** In the ledger, each printed quote carries
   the timestamp and the raw transcript text, so an editor can compare.
5. **Write the piece.** Lead with a scene only if the reporter observed it
   (notes) or the subject described it (quote it or attribute it). Paraphrase
   connective material; save direct quotes for what only the subject could say
   in that way.
6. **Context check.** For each quote, ask: would the subject recognise this as
   what they meant, given what came before and after it? If a quote's meaning
   depends on its question, keep the question in view.
7. **Self-check (QA-01)** against the Verification list; produce the ledger.

## Output Format

```
# [Headline]
[Feature or Q&A text]

## Quote ledger
| # | Printed quote | Timestamp | Raw transcript | Edits made |

## Paraphrase check
| Paraphrase in piece | Transcript basis (timestamp) |

## Facts stated by subject — to verify
## Off-record passages excluded (count only)
## Declared edits policy
```

## Verification

- [ ] Every direct quote appears in the ledger with timestamp and raw text.
- [ ] Every edit to a quote is one the rules allow, and is declared.
- [ ] No quote joins material from two different answers.
- [ ] Every paraphrase has a transcript basis.
- [ ] No off-record material appears, directly or paraphrased.
- [ ] Factual claims made by the subject are verified or attributed, not asserted.

## False-Positive Prevention

1. **"Cleaning up" grammar inside quote marks is misquotation.** Paraphrase
   instead, or keep their words.
2. **A composite quote is a fabricated quote**, even when every word was said.
3. **An answer to a different question changes meaning.** Keep quote and
   question together in context.
4. **Observed scene vs imagined scene.** "She glanced at the window" needs
   the reporter's notes; otherwise cut it.
5. **The subject's facts are claims.** "We tripled revenue" is attributed or
   verified, not stated by the writer.
6. **Quote approval is not a licence to improve quotes.** If the subject
   revises a quote on review, note it in the ledger as subject-revised.
7. **Removing dialect or accent markers can erase voice** — but spelling out
   an accent phonetically can mock. Use standard spelling of the words said.

## Example Output

```
# The night-shift baker who taught the whole street to make bread

At 4 a.m. the only lit window on Carver Street belongs to Luis Ortega's
bakery, where he has worked nights for eleven years. [notes: reporter present
2026-09-18, 04:05]

Ortega started teaching free Saturday classes after, he recalls, a neighbour
told him the shop's bread "tastes like the one my grandmother made." He says he had
no plan to teach; he wanted to answer her properly.

"I told her, come at six on Saturday and I'll show you. She came with her
sister. The next week there were nine people," he said.

About the work itself he is unsentimental. "Dough doesn't care if you're
tired. … You show up, or you throw it away."

He says the classes now run every week with around a dozen people; the
bakery's own sign-up sheet lists 14 names for this Saturday. [notes: sheet
photographed 09-18]

## Quote ledger
| # | Printed | Time | Raw | Edits |
|---|---|---|---|---|
| Q1 | "tastes like the one my grandmother made" (neighbour's words, as Ortega recalled) | 06:12 | "she say, it tastes like the one my grandmother made, you know" | Partial quote; attributed as recalled |
| Q2 | "I told her, come at six … nine people," | 06:40 | "I told her, uh, come at six on Saturday and I'll show you. She came with — with her sister. The next week there were nine people." | Filler "uh" and false start removed (policy allows) |
| Q3 | "Dough doesn't care … throw it away." | 22:15 | "Dough doesn't care if you're tired. It doesn't care about nothing. You show up, or you throw it away." | Ellipsis removes one sentence; meaning unchanged |

## Paraphrase check
| Paraphrase | Basis |
|---|---|
| "He had no plan to teach; he wanted to answer her properly" | 07:02 "I wasn't going to teach nobody, I just wanted to answer her right" |
| "classes now run every week with around a dozen people" | 09:30 (subject) + sign-up sheet (notes) |

## Facts stated by subject — to verify
"Eleven years on nights" — confirm start year with Ortega or business registration.

## Off-record passages excluded
1 (landlord dispute, 31:00–34:20).

## Declared edits policy
Filler and false starts removed from quotes; no grammar changes inside quotes.
```

## Techniques Used

- **IPC-07 Verbatim Source Anchoring** — each printed quote carries its raw transcript text.
- **CM-02 Constraint Specification** — the permitted/forbidden edit table.
- **ST-02 Structured Sequential Instructions** — mark → rank → apply rules → anchor → write.
- **DS-06 Prioritization and Severity Guidance** — quotes ranked by how well they serve the angle.
- **QA-01 Self-Verification** — ledger and paraphrase checks before filing.

## Related Prompts

- `domain-agentic-resources/skills/content-creation/transcript-fixer/SKILL.md` — fix ASR errors first.
- `domain-creative-writing/creative-nonfiction/writing_narrative_nonfiction_and_literary_journalism.md` — multi-source narrative.
- `writing_news_article_inverted_pyramid.md` — when the interview yields news.

---
title: "Grant, Fellowship & Residency Application Prep for Children's Authors"
category: childrens-writing
description: "Help an individual children's author or author-illustrator decide whether a specific grant, fellowship or residency fits, then draft the project description, artist statement and work-sample selection from the program's own published guidelines — never inventing criteria, deadlines, award amounts or acceptance rates; distinct from nonprofit_foundation_grant_proposal.md, which serves an organisation applying with a logic model and budget."
techniques:
  - QA-08
  - RT-23
  - RP-02
  - QA-26
difficulty: intermediate
tags:
  - childrens-writing
  - grants
  - fellowships
  - residency
  - funding-for-writers
  - apply-for-a-writing-grant
  - artist-statement
updated: "2026-09-24"
related_prompts:
  - domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md
  - domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md
  - domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md
---

# Grant, Fellowship & Residency Application Prep for Children's Authors

## When to Use

- You're an individual writer or author-illustrator of books for ages 0–14 and have found a grant, fellowship, mentorship or residency you might apply to — from a writers' organisation, an arts council, a foundation or a residency host.
- You're not sure the program fits your project or career stage and want a structured go/no-go before you spend days on it.
- You need a project description, artist statement or statement of purpose that describes a children's book without sounding like a query letter.
- You have to choose a writing (or art) sample and aren't sure which pages best meet the program's stated criteria.

**Not this prompt if:**
- An organisation (a nonprofit, school, library or press) is applying with a budget and logic model — use `domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md`.
- You're applying for academic or scientific research funding — see `domain-science/grants-funding/`.
- You're pitching the manuscript to agents or editors — use `domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md`.
- The project is mature teen YA — outside this domain's 0–3 to 11–14 range; `domain-creative-writing/` covers it.

## Inputs

- **The program's guidelines, pasted in full** (or a link plus pasted text): eligibility, criteria, required materials, word/page limits, deadline, award or residency details, and any stated review process. This is the only source of truth for the program's rules.
- **You:** career stage (pre-published, debut, published), publication history (true and verifiable), where you live, and any eligibility-relevant identity or membership — stated by you, only as far as you choose to share.
- **The project:** title, age category, form, stage (idea / draft / revision), a short synopsis, and what the funding or time would let you do.
- **Samples available:** manuscript pages, illustrations, published excerpts.
- **Past feedback:** any previous applications and responses.

## Method

You are a writer-in-residence programme reader who has also coached children's authors through their first applications. You read guidelines literally, you care about fit before prose, and you never fill a gap in a program's rules with what "most programs" do. Work the steps, then deliver in the locked format.

1. **Guidelines extraction (RT-23).** From the pasted guidelines only, extract: eligibility requirements, evaluation criteria (verbatim), required components with limits, deadline, and what the award provides. Tag each item `[G: guidelines]`. Anything the author wants to know that the guidelines don't state becomes `[VERIFY: ask the program]` — never a filled-in answer. If no guidelines are pasted, stop the fit gate and output only the list of what to obtain.
2. **Fit gate (QA-08).** Score each eligibility requirement as met / not met / unclear, and each criterion as strong / partial / weak match for this project. Eligibility is binary: one clear "not met" → recommend not applying and say why. Identity-based or membership-based eligibility is the author's to self-attest; the model neither assumes nor questions it. Output GO, GO-WITH-CAVEATS or NO-GO, with the deciding reasons.
3. **Frame the project for this reader (RP-02).** Program readers are not acquisitions editors: they're assessing artistic merit, need, and what the support makes possible. Translate the book from market language ("for fans of…") to purpose language: what the book is, why it matters to its child readers, why now in the author's development, and what specifically the money or time enables (research trip, uninterrupted drafting months, an illustration dummy). Keep the domain's no-preaching rule: describe the book's emotional and imaginative work, not the lesson it teaches.
4. **Draft the required components** in the order and limits the guidelines give: project description, artist statement or statement of purpose, bio, work plan or timeline, budget narrative if asked (costs supplied by the author, not estimated by the model). Map each paragraph to the criterion it answers.
5. **Choose the sample.** Recommend pages that best meet the stated criteria — usually the strongest continuous pages, not a patchwork; for picture books, the complete text or a dummy if allowed; for author-illustrators, art that matches the project described. Note formatting rules from the guidelines; unstated formatting is `[VERIFY]`.
6. **Representation humility.** If the project depicts communities the author does not belong to, the application should say how the author is doing that work (consultants, sensitivity readers, budget for them). Do not describe the project as authentic or own-voices unless the author said so, and do not advise leaning on identity the author hasn't disclosed.
7. **Claims check (QA-26).** List every factual claim in the draft — publications, awards, sales, reviews, program facts — and confirm each is author-supplied or from the guidelines. Remove anything the model introduced.

## Output Format

```markdown
## Guidelines Extract
| Item | Text / value | Source tag (G / VERIFY) |

## Fit Gate
| Requirement or criterion | Met / match | Evidence from author inputs |
Verdict: GO | GO-WITH-CAVEATS | NO-GO — [reasons]

## Project Framing
[3–5 sentences: the book, why it matters to its readers, why now, what the support enables]

## Draft Components
### [Component name — limit]
[draft] · Criterion addressed: …

## Work-Sample Recommendation
[pages / art] — why these meet the criteria — formatting notes

## Claims Check
| Claim | Source (author / guidelines) | Keep / VERIFY / cut |

## Before You Submit
- [ ] …
```

## Verification

- [ ] Every program rule in the output is tagged to the pasted guidelines or marked VERIFY.
- [ ] No deadline, award amount, acceptance rate, number of awards or reviewer identity is stated unless it appears in the guidelines.
- [ ] Any unmet eligibility requirement produced a NO-GO, not a workaround.
- [ ] Each draft paragraph maps to a named criterion, and every component respects its stated limit.
- [ ] The project description uses purpose language, not comp-title market pitch.
- [ ] Budget lines, if any, come from the author's own figures.
- [ ] Publications, awards and credentials match what the author supplied exactly.
- [ ] Identity or membership eligibility is left to the author's self-attestation.

## False-Positive Prevention

1. **Invented program facts.** Models "know" deadlines, award sizes and criteria for well-known writers' organisations. Programs change year to year; use only the pasted guidelines and mark everything else `[VERIFY]`.
2. **Fabricated odds.** Never state acceptance rates or "competitive" levels unless the program publishes them in the supplied text.
3. **Query-letter voice.** A pitch built on comps and market positioning misreads the reader; reframe around artistic purpose and need.
4. **Talking past a failed eligibility test.** Encouraging the author to "apply anyway" when a clear requirement is unmet wastes their time and the program's.
5. **Inflating the bio.** Upgrading "self-published" to "published" or implying awards is a misrepresentation; copy the author's facts exactly.
6. **Identity assumptions.** Don't infer or recommend claiming eligibility for identity-based programs; the author decides and attests.

## Example

**Input sketch:** Fictional author Rosa Quell, pre-published, writing a middle-grade verse novel (ages 9–12) about a girl who builds a radio to reach her deployed father. Program: a fictional "Harbour Arts Council Emerging Writer Grant"; pasted guidelines say: resident of the region; no prior traditionally published book; criteria — "artistic merit", "clarity of project plan", "impact of support on the artist's development"; 500-word project description; 10-page sample.

**Abbreviated output:**

- **Guidelines Extract:** Residency requirement `[G]` · No prior trad-published book `[G]` · Deadline — not in pasted text → `[VERIFY: ask the program]` · Award amount — `[G: as stated]`.
- **Fit Gate:** Residency — met (author lives in the region) · No prior book — met · Artistic merit — strong (sample is revised) · Project plan — partial (no timeline yet) · Impact — strong. **Verdict: GO-WITH-CAVEATS** — add a month-by-month plan.
- **Project Framing:** "*Static* is a verse novel for readers 9–12 about a girl who teaches herself electronics to reach her father across an ocean. Support would fund four months of reduced work hours to complete the second draft and a consultation with a military-family reader."
- **Work Sample:** Pages 1–10 continuous (the opening poems establish voice and the radio goal); avoid the late poems, which spoil the ending.
- **Claims Check:** "SCBWI member" — author-supplied ✓ · "award-winning short fiction" — not supplied → cut.
- **Before You Submit (excerpt):**
  - [ ] Confirm the deadline and time zone with the program (not in pasted text).
  - [ ] Check whether the sample must be anonymised; the guidelines are silent → VERIFY.
  - [ ] Ask a reader outside the verse-novel form whether the project description makes sense to a non-specialist panel.

---
title: "Self-Publishing vs Traditional Publishing — The Path Decision, Break-Even and Earn-Out Math From Your Own Numbers, Red-Flag Screening, and a First-Year Plan"
category: creative-writing
description: "Help an adult-book author choose between traditional (agented or small-press) publishing, self-publishing, and paid hybrid or assisted services: rank the author's own goals, compare the paths on control, money flow, timeline, distribution, and workload, compute self-publishing break-even and advance earn-out from the author's real quotes and offer terms, screen offers for vanity-press and rights red flags, and lay out a first-year plan for the chosen path — with no invented sales figures, advances, agents, or market claims."
techniques:
  - DP-29
  - IT-22
  - NE-11
  - RT-23
  - QA-04
difficulty: intermediate
tags:
  - creative-writing
  - publishing
  - self-publishing
  - traditional-publishing
  - hybrid-publishing
  - author-royalties
  - break-even
  - should-i-self-publish
  - cant-find-an-agent
  - is-this-publisher-a-scam
updated: "2026-10-03"
related_prompts:
  - domain-creative-writing/publishing-career/writing_query_letter_and_synopsis.md
  - domain-childrens-writing/publishing-business/childrens_self_publishing_prep.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
---

# Self-Publishing vs Traditional Publishing

**Objective:** Turn "should I self-publish?" into a decision the author can defend:
their goals ranked, each path compared on what it actually changes, the money
worked out from their own quotes and offers rather than anecdotes, any offer
screened for red flags, and a dated first-year plan for the path they choose.

**When to Use:**
- You have a finished, revised adult manuscript (fiction or nonfiction) and are
  deciding which route to take.
- You have queried for months with requests but no offer, and wonder whether to
  stop.
- A small press or "hybrid" publisher has made an offer — possibly one that asks
  you to pay — and you want to compare it with self-publishing.
- You write in a series and are weighing release speed against bookstore reach.
- **Not this prompt if** you have already chosen to query agents and need the
  letter — use `domain-creative-writing/publishing-career/writing_query_letter_and_synopsis.md`
  (and `writing_pitch_logline_and_comp_titles.md` for comps). If the book is for
  children and you are planning production (trim, bleed, print files), use
  `domain-childrens-writing/publishing-business/childrens_self_publishing_prep.md`.
  If you need a contract clause-by-clause reviewed, use
  `domain-legal/contracts-transactional/legal_contract_review_full_redline.md` and
  an attorney. For a cover image, use `domain-image-generation/publishing-covers/cover_fiction_book.md`.

> **No-fabrication guard:** this prompt never invents sales numbers, typical
> advances, an agent or press name, genre "market sizes", or retailer royalty rates
> as current fact. Every number is tagged `[author]` (supplied by the author from a
> quote, offer, or their records) or `[VERIFY]` (a commonly cited term the author
> must confirm against the current source — retailer terms change). Copy counts in
> the math are thresholds, not forecasts.

## Inputs / Context

1. **The book**: genre/category, word count, standalone or series (how many
   drafted), finished and revised?
2. **History so far**: queries sent, requests, offers, feedback.
3. **Goals** in the author's words (bookstore shelves, income, speed, control,
   awards, a career with an agent, a book for family and clients).
4. **Money and time**: budget per book, hours per week for business tasks, and
   comfort with marketing and advertising.
5. **Any offers in hand**: advance, royalty rates and bases (list or net), rights
   granted, term and reversion, option clause, any fees the author pays.
6. **Quotes** the author has gathered: editing, cover, formatting, ISBNs, ads.
7. **Platform**: mailing list, audience, professional standing (for nonfiction).

## Method

1. **Rank the author's values (DP-29).** Order 4–6 goals from "never sacrificed" to
   "first to give up", and write one example conflict resolved by the ranking
   ("speed outranks bookstore placement, so a two-year traditional timeline loses
   to a 9-month release cadence").
2. **Compare paths on a decision matrix (IT-22).**
   | Dimension | Traditional (agent → publisher) | Small press (direct) | Self-publishing | Paid hybrid / assisted |
   |---|---|---|---|---|
   | Who pays production | publisher | press | author | author (fees) |
   | Money flow | advance against royalties | small or no advance | author keeps retailer net | author pays, then royalties |
   | Control (cover, price, timing) | low–shared | shared | full | varies by contract |
   | Time to publication | often 1–2+ years after a deal `[VERIFY]` | varies | months | months |
   | Bookstore distribution | strongest | varies | limited without extra work | varies; often claimed, verify |
   | Author's business workload | lower | medium | highest | medium |
   | Rights granted | per contract | per contract | none | per contract — read closely |
   Weight the rows by the value ranking; note which goals each path cannot meet.
3. **Do the money from the author's numbers (NE-11, RT-23).**
   - Self-publishing upfront cost `C` = editing + cover + formatting + ISBNs +
     launch ads, each `[author]` from quotes.
   - Net per copy: ebook = price × retailer royalty rate `[VERIFY current terms]`;
     print-on-demand = list × royalty rate − print cost `[VERIFY with the
     platform's calculator]`; blend by an assumed format mix and say it is an
     assumption.
   - Break-even copies = `C ÷ blended net per copy`.
   - Offer: royalty per copy from the offer's own rates and bases; copies to earn
     out = `advance ÷ royalty per copy`; deduct agent commission if agented
     (commonly 15% domestic `[VERIFY]`).
   - Crossover: the copy count above which self-publishing nets more than the offer.
   Present results at threshold copy counts, never as predicted sales.
4. **Screen offers for red flags.** Fees charged to the author by a company calling
   itself a publisher; packages sold by upsell; rights for the full term of
   copyright with no out-of-print reversion; option clauses on all future work;
   royalties on "net" without a definition; no clear distribution plan. Check the
   company against Writer Beware and, for hybrids, the Independent Book Publishers
   Association's published hybrid-publisher criteria `[VERIFY current versions]`.
   Contract terms → `[LEGAL REVIEW]`.
5. **State the uncertainty (QA-04).** Name what the author does not know (their
   sell-through, whether an agent would sign the next book) and which decision
   would change if it turned out differently.
6. **Recommend and plan.** Name the path, the dominant reason from the value
   ranking, what is given up, and a first-year plan with dated milestones and a
   review point with an observable trigger for changing course.

## Output Format

```
# Publishing path decision — [title]
Book: [genre · words · series status] · History: [...]

## Value ranking (highest wins)
1 … 5 · Example conflict: [...]

## Path comparison (weighted by ranking)
| Dimension | Traditional | Small press | Self | Hybrid | Matters because |

## Money (all inputs tagged [author] or [VERIFY])
Self-pub cost C · net per copy · break-even
Offer: royalty per copy · earn-out · crossover
| Copies (threshold) | Self-pub net | Offer income |

## Offer red-flag screen
## What we don't know, and what would change the answer
## Recommendation (path · dominant reason · what is given up)
## First-year plan (month · milestone) · Review trigger
```

## Verification

- [ ] Every number is tagged `[author]` or `[VERIFY]`; none is presented as market fact.
- [ ] Break-even and earn-out arithmetic is shown and correct.
- [ ] Copy counts are labelled thresholds, not forecasts.
- [ ] The recommendation follows from the stated value ranking.
- [ ] Any author-paid fee or full-term rights grant is flagged.
- [ ] The plan has dated milestones and an observable review trigger.

## False-Positive Prevention

1. **Higher royalty rate is not higher income.** Self-publishing pays more per copy
   but the author pays upfront and sells every copy themselves.
2. **An advance is not the whole value.** Distribution, editing, and placement have
   value the per-copy math omits; name them.
3. **Rejections are not a verdict on the path.** Many requests and no offers may
   point to the opening pages, comps, or category, not to self-publishing.
4. **"Hybrid" is not a single model.** Some are selective and transparent; some are
   vanity presses renamed. Screen the terms, not the label.
5. **Genre anecdotes are not data.** Do not say a genre "sells better" self-published
   without a source the author can check.
6. **One path is not forever.** Authors move between paths; note what each choice
   does to that option (rights granted, series continuity).

## Example Output

```
# Publishing path decision — "A Killing at the Quilt Show" (cozy mystery)
Book: cozy mystery · 72,000 words · Book 1 revised; Books 2–3 drafted.
History: 62 queries over 10 months → 3 full requests, 0 offers [author].
Offer in hand: small press, direct submission [author].

## Value ranking
1 Release the series on my schedule (one book every ~9 months)
2 Income from the series over 3 years
3 Paperbacks in my local bookstore and library
4 Avoid running ads myself
Conflict: speed (1) outranks avoiding ads (4) → a path that needs ads is acceptable.

## Money
Self-pub C = copyedit+proof $1,400 + cover $450 + 2 ISBNs $59 + launch ads $500
           = $2,409 per book [author quotes; ISBN price VERIFY]
Ebook $4.99 × 70% = $3.49 [rate VERIFY]; paperback $14.99 × 60% − $4.10 print = $4.89 [VERIFY]
Assumed mix 80% ebook / 20% print → blended $3.77 · break-even 2,409 ÷ 3.77 = 639 copies
Offer: $1,000 advance; 25% of net on ebook (≈ $0.87/copy if press nets $3.49);
8% of $15.99 list on paperback ($1.28) → blended $0.95 · earn-out 1,000 ÷ 0.95 = 1,053 copies
Crossover: 3.77n − 2,409 = 1,000 → n = 904 copies
| Copies | Self-pub net | Offer income |
| 300    | −$1,278      | $1,000 (advance) |
| 904    | $1,000       | $1,000 |
| 2,000  | $5,131       | $1,900 |

## Offer red-flag screen
Rights: full term of copyright, no out-of-print reversion clause → [LEGAL REVIEW].
Option on "the author's next three works" → would bind Books 2–3 → conflicts with value 1.
No author fees (good). Check press on Writer Beware [VERIFY].

## What we don't know
Sell-through: no history. Below ~904 copies per book the offer pays more; the author
should decide whether she believes she can reach that with a 3-book series.

## Recommendation
Self-publish the series; dominant reason: value 1 (schedule) plus the option clause.
Given up: bookstore reach (value 3) — partly recovered with a local consignment ask.
If staying with the press, negotiate reversion and limit the option to Book 2 only.

## First-year plan
M1–2 copyedit, cover, mailing-list sign-up page · M3 Book 1 launch · M6 Book 2
· M9 Book 3 · M12 review.
Review trigger: if Books 1–2 combined are below break-even six months after Book 2,
pause ads and reconsider querying with Book 4.
```

## Techniques Used

- **DP-29 Value Hierarchy Construction** — the author's goals ranked with a worked conflict, so the recommendation follows from them.
- **IT-22 Workflow Decision Matrix** — four paths compared on the same dimensions.
- **NE-11 Embedded Calculation Formulas** — break-even, earn-out, and crossover computed and shown.
- **RT-23 Input Provenance Tagging** — every number tagged `[author]` or `[VERIFY]` so no guess passes as data.
- **QA-04 Uncertainty Acknowledgment** — unknown sell-through named, with the threshold at which the answer flips.

## Related Prompts

- `domain-creative-writing/publishing-career/writing_query_letter_and_synopsis.md` — executing the traditional route.
- `domain-childrens-writing/publishing-business/childrens_self_publishing_prep.md` — production prep for a self-published children's book.
- `domain-legal/contracts-transactional/legal_contract_review_full_redline.md` — reviewing an offer's contract terms.

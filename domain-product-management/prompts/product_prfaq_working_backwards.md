---
title: "PR/FAQ — Working Backwards From the Customer Before Anything Is Built"
category: product-management/prompts
description: "Write a working-backwards PR/FAQ before committing to build: a one-page future press release in the customer's language, an external FAQ a customer would ask, an internal FAQ that states cost, what has to be true and the biggest risks, a read-aloud test with target customers, and a proceed / revise / stop decision with kill signals — distinct from product_create_prd (requirements after the decision to build) and decisiondoc_narrative_memo_bezos (a six-page memo choosing among options)."
techniques:
  - RP-02
  - NE-23
  - QA-02
  - DP-13
  - CM-02
difficulty: intermediate
tags:
  - prfaq
  - working-backwards
  - product-discovery
  - press-release
  - customer-problem
  - pre-build
  - new-product-idea
  - should-we-build
  - pitch-an-idea
updated: "2026-09-24"
related_prompts:
  - domain-product-management/prompts/product_create_prd.md
  - domain-product-management/prompts/product_product_idea_vetting_will_it_fly_or_flop.md
  - domain-decision-making/documentation/decisiondoc_narrative_memo_bezos.md
---

# PR/FAQ — Working Backwards

**Objective:** Before anything is built, write the announcement the customer would read
on launch day and the questions it would provoke. Then decide whether the product is
worth building. The press release forces a benefit that fits in customer language on one
page. The internal FAQ forces the cost, the assumptions and the risks into the open. A
PR/FAQ whose press release describes features instead of a customer outcome, or whose
internal FAQ has no answer to "what has to be true", is refused.

**When to Use:**
- An idea has momentum and nobody has written down who it is for and why they would care.
- Stakeholders agree on the solution and disagree on the problem.
- You need to test several ideas cheaply before any of them gets a PRD.

**Distinct from:**
- `product_create_prd.md` — writes requirements *after* the decision to build. The
  PR/FAQ comes first and may conclude "do not build".
- `../../domain-decision-making/documentation/decisiondoc_narrative_memo_bezos.md` — a
  six-page narrative memo choosing among options. The PR/FAQ tests one idea from the
  customer's side of launch.
- `product_product_idea_vetting_will_it_fly_or_flop.md` — scores an idea on a go/no-go
  rubric. Use it on the PR/FAQ's internal FAQ if you want a score.

---

## Inputs

1. **The customer**: who, specifically, and what they do today instead.
2. **Evidence of the problem**: interviews, support tickets, usage data, with counts.
3. **The idea** in one or two sentences.
4. **Constraints**: team, timeline, price range, platforms.
5. **Who decides** whether this proceeds.

If there is no evidence of the problem, the first output is a research plan, not a
press release.

---

## Method

1. **State the customer and problem in their words (RP-02, CM-02).** One sentence each,
   using language from interviews or tickets rather than internal vocabulary. Name what
   they do today instead. The current workaround is the real competitor.

2. **Write the press release, one page at most.**
   - Headline: the customer benefit, not the feature name.
   - Subheading: who it is for and the one outcome.
   - Date: the intended launch date.
   - Problem paragraph: the customer's pain, with the evidence.
   - Solution paragraph: what changes for them, in plain language.
   - Leader quote: why the company built it.
   - How it works: three steps a customer would follow.
   - Customer quote: marked **[illustrative]**, never presented as real.
   - Call to action: how to get it.
   Ban jargon, internal codenames and superlatives. A superlative in a press release is a
   claim you have not earned.

3. **Write the external FAQ.** Five to eight questions a customer would ask: price,
   availability, what it does *not* do, migration, data, support.

4. **Write the internal FAQ (NE-23).** Questions a sceptical executive would ask:
   - Why now, and why us?
   - What does it cost to build and run? (in team-weeks and run cost, each tagged
     estimate or data)
   - **What has to be true** for this to succeed? (adoption, willingness to pay, technical feasibility)
   - What are we choosing not to do in order to do this?
   - What are the three biggest risks?
   - What would make us stop?

5. **Run the read-aloud test (QA-02).** Read the press release to three to five target
   customers or close proxies. Ask each to restate the benefit and say whether they would
   use it. A reader who cannot restate it means the release is unclear. A reader who
   restates it and does not care means the idea may be wrong. Record which.

6. **Decide, with kill signals (DP-13).** Proceed to PRD, revise and re-test, or stop.
   If proceeding, state two or three observable kill signals for the first milestone.
   Record the decider and date.

---

## Output Format

```markdown
# PR/FAQ — [working name] · [date] · Decider: [name]

## Customer and problem
Customer: [...] · Today they: [workaround] · Evidence: [counts, sources]

## Press release
**[Headline: customer benefit]**
*[Subheading]*
[City], [launch date] — [problem] [solution] [leader quote] [how it works, 3 steps]
[customer quote — illustrative] [call to action]

## External FAQ
1. [Q] — [A]

## Internal FAQ
| Question | Answer | Tag |
|---|---|---|
| What has to be true | | [estimate/data] |

## Read-aloud test
| Reader | Restated benefit? | Would use? | Note |
|---|---|---|---|

## Decision
PROCEED TO PRD / REVISE / STOP — [date], [decider]
Kill signals: [...]
```

---

## Verification

- [ ] The customer and problem are stated in customer language, with evidence counts
- [ ] The headline is a benefit, not a feature name
- [ ] The press release fits on one page and contains no jargon or superlatives
- [ ] Any customer quote is marked illustrative
- [ ] The external FAQ says what the product does not do
- [ ] The internal FAQ has cost, what has to be true, trade-offs, risks and stop conditions
- [ ] Every number is tagged estimate or data
- [ ] The read-aloud test was run and its results distinguish unclear from unwanted
- [ ] The decision is recorded with decider, date and kill signals

## False-Positive Prevention

1. **A well-written press release is not evidence of demand.** Polished prose persuades
   the team that wrote it. Only the read-aloud test and the problem evidence count.
2. **Invented customer quotes must never be presented as real.** Mark them illustrative,
   or they leak into decks as research.
3. **A feature list with a headline on top is not a press release.** If the problem
   paragraph could be deleted without loss, the release is feature-first.
4. **"What has to be true" is the most skipped answer and the most important.** Leaving it
   blank means nobody has tested the assumption the whole idea rests on.
5. **STOP is a successful outcome.** A PR/FAQ that kills an idea in a week has saved a
   quarter. Do not revise indefinitely to avoid saying it.
6. **Do not skip straight to the PRD after a positive read-aloud.** Record the kill
   signals first. They are much harder to agree once work has started.

---

## Example

**Context:** An invoicing app for small agencies. 3,000 active accounts. Idea: automatic
payment reminders. Evidence: 12 interviews, 9 of 12 chase late invoices by hand; median
days-to-paid is 47 `[data]`.

**Press release headline:** "Get paid without chasing: invoices now follow up for you."
**Subheading:** "For agency owners who spend Friday afternoons writing reminder emails."
**How it works:** turn on Auto-chase; choose a tone; reminders go at 7, 14 and 21 days
after the due date. Customer quote marked [illustrative].

**External FAQ excerpt:** "Does it charge late fees?" No, reminders only. "Price?" $15 a
month add-on.

**Internal FAQ excerpt:**

| Question | Answer | Tag |
|---|---|---|
| Cost to build | 2 engineers × 8 weeks = 16 engineer-weeks | estimate |
| What has to be true | ≥20% of 3,000 accounts adopt within 6 months = 600 × $15 = $9,000 MRR | estimate |
| Not doing | Late-fee automation, deferred to next half | — |
| Biggest risk | Reminders sent after the client has paid by bank transfer | — |

**Read-aloud:** 5 readers. 5 of 5 restated the benefit and 4 of 5 would use it. The
fifth invoices through a client portal, a segment to exclude.

**Decision:** PROCEED TO PRD — 12 Oct, Head of Product. Kill signals: fewer than 5 of 10
pilot accounts turn it on within 30 days, or more than 2% of reminders go to
already-paid invoices.

---

## Techniques Used

- **RP-02 Audience-Specific Framing** — the release is written for the customer, in their words.
- **NE-23 Objection Pre-emption** — the internal FAQ answers the sceptical executive in advance.
- **QA-02 Adversarial Stress-Test** — the read-aloud test separates unclear from unwanted.
- **DP-13 Kill Signal Definition** — observable stop conditions set before building.
- **CM-02 Constraint Specification** — one page, no jargon, no superlatives, illustrative quotes marked.

## Related Prompts

- `product_create_prd.md` — the next document if the decision is proceed
- `product_product_idea_vetting_will_it_fly_or_flop.md` — a scored go/no-go on the same idea
- `../../domain-decision-making/documentation/decisiondoc_narrative_memo_bezos.md` — the six-page memo for choosing among options
- `product_launch_readiness_gate.md` — where the press release returns, as marketing's readiness input

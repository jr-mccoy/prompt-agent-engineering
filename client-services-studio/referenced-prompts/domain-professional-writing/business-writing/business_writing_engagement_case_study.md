---
title: "Engagement Case Study"
category: business-writing/client-facing
description: "Generate a publishable case study from a completed client engagement — situation, intervention, result with its measurement stated, and the honest limits of attribution — including the consent, anonymisation and fact-checking steps that must happen before publication"
techniques:
  - RT-05
  - CM-01
  - QA-01
  - OC-03
  - ED-05
difficulty: intermediate
tags:
  - case-study
  - client-facing
  - consulting
  - freelance
  - social-proof
  - marketing-collateral
  - business-writing
updated: "2026-09-21"
---

# Engagement Case Study

**Objective:** Turn a completed engagement into a **publishable case study**: the
client's situation, what was done, what changed, how the change was measured, and
what else could account for it — plus the consent, anonymisation and fact-checking
steps that must be completed before anything is published.

**When to Use:** Use at close-out, while the engagement is fresh and the sponsor is
still reachable and well-disposed. Waiting three months costs both the detail and the
access.

**This is the generator; the evaluator already exists.**
`../content-quality/quality_slop_case_study.md` scores a case-study draft and returns
ACCEPT / REVISE / REJECT. It has no generator to feed it. Write with this, then score
with that — the two are designed to be run in sequence, and this prompt's verification
section explicitly hands off.

This is **distinct from** `../../domain-agentic-resources/skills/marketing/copywriting/`,
which produces marketing copy with social-proof sections, and from
`../../domain-psy-ops/case-studies-taxonomies/psyops_historical_operation_case_study.md`,
which analyses historical operations.

---

## Context Gathering

1. **The engagement** — from `../../domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`
   if it was run:
   - "Client, sector, size, and the situation that triggered the work."
   - "What you actually did — the sequence, not the sales version."
   - "Deliverables, timeline, and what changed along the way."

2. **The result**
   - "What is measurably different? What is the number, before and after?"
   - "Who measured it, and from what source?"
   - "Over what period? Has it held?"
   - "What else changed in that period that could explain it?"

3. **The client's view**
   - "What did the sponsor say about the outcome, in their words?"
   - "Would they be quoted? Would they take a reference call?"
   - "What would they say went less well?"

4. **Permission**
   - "Is there a confidentiality clause covering this engagement?"
   - "Does the contract permit naming them, or logo use?"
   - "Who has authority to consent — sponsor, marketing, or legal?"

Check the confidentiality position **first**. Many services contracts prohibit
disclosure of the engagement's existence, let alone its content, and discovering that
after drafting wastes the work and risks a breach.

---

## Method

### Step 1 — Establish the permission position before writing

Three levels, and they determine everything that follows:

| Level | What you may publish |
|---|---|
| **Named** | Client name, logo, quote, specifics. Requires explicit written consent |
| **Anonymised** | Sector, size band, situation, numbers. No identifying details |
| **Composite or none** | Pattern described across engagements, no single client identifiable |

Anonymisation is harder than it looks. A sector, a region, a size band and a
distinctive situation identify a company to anyone in that market. Test the draft by
asking whether a competitor of the client could name them from it; if yes, it is not
anonymised.

### Step 2 — Write the situation without flattering yourself

The situation section fails when it exaggerates the dysfunction to make the
intervention look heroic. Clients read these. Describe the situation as the client
would recognise it, including the constraints that were reasonable — they had good
reasons for the state they were in, and saying so makes the rest credible.

State the trigger: what made it a problem *now*. That is the sentence a prospective
client recognises themselves in, and it does more work than the entire result
section.

### Step 3 — Describe the intervention truthfully

What you actually did, in sequence. Include:

- The approach, and **why that one** given the constraints
- What you found that was not expected
- What changed mid-engagement, and what you did about it

The unexpected finding is the most valuable paragraph in most case studies, because
it demonstrates judgement rather than process. A case study where everything went to
plan reads as fiction, and prospective clients have been in enough engagements to
know it.

### Step 4 — State the result with its measurement

Every claimed result carries four things, without exception:

| Element | Why |
|---|---|
| The number, before and after | A result without a baseline is an assertion |
| The source of measurement | Client's own system beats your estimate |
| The period | A one-month improvement is not an annual one |
| Who measured | Client-measured is far stronger than supplier-measured |

If a number is unavailable, say what is qualitatively different and who observed it.
A specific qualitative result — "the team now runs the review themselves, monthly,
without us" — is stronger than an invented percentage.

### Step 5 — State attribution honestly, and gain from it

Name what else could account for the result: other initiatives, seasonality, market
movement, the fact that attention itself changes behaviour. Then state what makes you
confident the intervention contributed.

This feels like it weakens the case study. It does the opposite. A sophisticated
buyer discounts unqualified claims automatically; a case study that discounts its own
claims accurately is the only kind they believe. It also protects you — an
overclaimed result is a promise a future client will hold you to.

### Step 6 — Quote the client, verbatim

Ask for a quote; do not write one and ask for approval. A supplier-drafted quote
reads as supplier-drafted no matter who signs it. If they offer to have you draft it,
send two or three options in their register and let them edit.

Where a quote is not available, `business_writing_testimonial_and_referral_request.md`
covers the ask.

### Step 7 — Fact-check with the client before publication

Send the draft to the sponsor for correction, with a deadline and a specific ask:
"please correct anything inaccurate, and tell me if anything is more sensitive than
I have treated it." This is not optional. It catches errors, secures informal consent
alongside the formal kind, and frequently produces a better quote than the one you
were given.

---

## Output Format

```markdown
## Case study — [title]

**Permission level:** [named / anonymised / composite]
**Consent:** [who, when, in writing where] · **Confidentiality clause:** [checked — permits X]

---

### [Headline: the outcome, specific, no superlatives]

**Client:** [name or anonymised description]
**Engagement:** [type, duration]

#### The situation
[as the client would recognise it, including the reasonable constraints]
**The trigger:** [what made it urgent now]

#### What we did
[sequence; the approach and why; what was unexpected; what changed]

#### The result
| Measure | Before | After | Source | Period | Measured by |
|---|---|---|---|---|---|

**What else could account for this:** [honest list]
**Why we think the work contributed:** [reasoning]

#### In their words
> [verbatim quote]
> — [name, role]

#### What we would do differently
[one honest item]

---

### Pre-publication checklist
- [ ] Confidentiality clause checked and permits this level
- [ ] Written consent from [who has authority]
- [ ] Draft fact-checked by sponsor on [date]
- [ ] Every number has a source
- [ ] Anonymisation survives the competitor test (if applicable)
- [ ] Scored with `../content-quality/quality_slop_case_study.md` — result: [ACCEPT / REVISE]
```

---

## Verification

- [ ] The confidentiality position was checked before drafting, not after.
- [ ] Written consent exists from someone with authority to give it.
- [ ] Every number has a baseline, a source, a period and a measurer.
- [ ] Attribution names at least one alternative explanation.
- [ ] The client quote is verbatim, not supplier-drafted and approved.
- [ ] The draft was fact-checked by the client before publication.
- [ ] Anonymised versions survive the competitor test.
- [ ] Scored with the existing evaluator, and the result is ACCEPT.

**False-positive prevention.** The dominant failure is the unattributed number: "cut
costs by 40%" with no baseline, source, period or measurer. It is unverifiable, so
sophisticated readers discount it entirely, and it creates an expectation you cannot
meet. Every number carries its four elements or it does not appear.

The second is the heroic narrative — a dysfunctional client rescued by your insight.
It reads badly to the exact audience you want, because they are the client in that
story. Describe reasonable people with real constraints.

The third is anonymisation that does not anonymise. "A mid-size fintech in the Nordics
following their Series B" identifies a company. Either get consent to name, or
generalise until the competitor test passes.

The fourth is skipping the fact-check because the client seems happy. Publication
without review is how a good relationship ends over a detail you did not know was
sensitive.

---

## Related

- `../content-quality/quality_slop_case_study.md` — the evaluator; run after this
- `business_writing_testimonial_and_referral_request.md` — securing the quote and the onward ask
- `../../domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md` — the close-out data this draws on
- `../../domain-business-strategy/client-services/services_offer_definition_and_boundary.md` — the offer this case study evidences

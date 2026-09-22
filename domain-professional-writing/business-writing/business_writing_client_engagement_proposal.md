---
title: "Client Engagement Proposal"
category: business-writing/client-facing
description: "Write a client-facing services proposal from a discovery record and a scoping decision — option-tiered, priced, with sections that map one-to-one onto the statement of work that will follow, so the proposal the client accepts is the document that governs delivery"
techniques:
  - CM-01
  - ST-03
  - NE-23
  - OC-03
  - QA-08
difficulty: intermediate
tags:
  - proposal
  - client-facing
  - consulting
  - freelance
  - sow
  - option-tiering
  - business-writing
updated: "2026-09-21"
---

# Client Engagement Proposal

**Objective:** Produce a **client-facing services proposal** whose sections map
one-to-one onto the statement of work that will follow, so that acceptance of the
proposal and signature of the SOW describe the same engagement. Inputs are a
discovery record and a scoping decision; outputs are an option-tiered, priced
proposal with assumptions, exclusions and a change mechanism stated up front.

**When to Use:** Use when you are the supplier proposing paid work to a client, after
discovery and after scope and price have been decided. Not for internal proposals,
not for investment cases.

**What this is distinct from — read this before writing.** This slot is crowded and
the distinction is load-bearing:

| Existing | What it does | Why this is different |
|---|---|---|
| `business_writing_proposal.md` | General proposal: problem framing, solution, scope, value, alternatives, CTA | **Internal or general audience.** Use it if you are proposing to your own organisation |
| `business_writing_executive_proposal_template.md` | Executive-audience structure | A template for the executive form, not a supplier engagement |
| `business_writing_investment_proposal_example.md` | Worked investment case | Different object entirely |
| `../domain-specific/domain_writing_architect_proposal.md`, `domain_writing_landscaper_proposal.md`, `domain_writing_hvac_estimate.md` | Trade-specific client proposals | **One trade, one deliverable shape.** Use those if you are in that trade |
| `../domain-specific/domain_writing_consultant_executive_summary.md` | The summary artifact | A component, not the proposal |

This prompt's specific contribution is the **SOW correspondence requirement** and the
**option tiering** — neither appears in the prompts above, and both exist because a
proposal that does not map to the contract creates the scope dispute it was supposed
to prevent.

---

## Context Gathering

Do not write without these. If the scoping decision is missing, stop and produce it
first — a proposal written to cover an undefined scope is the origin of most
services disputes.

1. **The discovery record**
   - "What did the client say the problem was, in their words?"
   - "What did they say the consequence of not solving it is?"
   - "Who is the decision-maker, and who else reads this?"
   - "What did they tell you about budget, timing and process?"

2. **The scoping decision**
   - "Deliverables, with acceptance criteria."
   - "Assumptions the estimate depends on."
   - "Exclusions."
   - "Required inputs from the client, and by when."

3. **The commercial decision**
   - "Structure and price, from the pricing-model selection."
   - "What the tiers are, if tiering."
   - "Payment schedule."

4. **The competitive position**
   - "Are they comparing? Against whom or what — including doing nothing internally?"
   - "What did they say about previous suppliers?"

---

## Method

### Step 1 — Open with their problem in their words

The first paragraph demonstrates that you listened. Restate the problem, its
consequence and the desired outcome using the client's own vocabulary from discovery
— including their metric names and their internal terminology. Do not translate into
your framework.

A proposal that opens with your credentials rather than their problem reads as a
brochure and is skimmed. Credentials go near the end, and only the relevant ones.

### Step 2 — Tier the options

Offer two or three options, not one. A single option makes the decision binary —
yes or no; multiple options make it comparative — which. The comparison also tells
you what the client actually values, from what they choose.

Tier by **scope**, not by effort or quality:

| Tier | Principle |
|---|---|
| Lower | A genuinely useful smaller outcome. Not a crippled version — something you would be happy to deliver |
| Middle | The recommended scope. Say it is recommended and say why |
| Upper | Additional scope that is genuinely valuable to some clients, priced accordingly |

Never tier by quality. "Basic" and "premium" versions of the same work imply you
would deliver something less than your best, which raises a question you do not want
asked.

### Step 3 — Map sections one-to-one onto the SOW

This is the structural requirement that distinguishes this proposal from any other.
Each proposal section corresponds to a SOW section, so nothing is agreed in the
proposal that the contract will not carry:

| Proposal section | Becomes, in the SOW |
|---|---|
| What you get | Deliverables schedule |
| How it will be judged complete | Acceptance criteria |
| What we need from you | Client obligations |
| What this assumes | Assumptions |
| What is not included | Exclusions |
| Timeline | Milestone schedule |
| Investment | Fee and payment schedule |
| If things change | Change-order procedure |

Draft the deliverable and acceptance language so it can be lifted into
`../../domain-legal/contracts-transactional/legal_sow_drafter.md` verbatim. Where
acceptance criteria are vague, sharpen them with
`../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
before writing.

### Step 4 — State exclusions plainly, in the proposal

Exclusions belong in the proposal, not only in the contract. Burying them in terms
the client reads after saying yes is both poor practice and commercially worse: the
conversation about what is out happens either now, cheaply, or in week six,
expensively.

Write them without defensiveness. "Implementation of the recommendations is not
included; we can quote separately" is a sentence that sells a second engagement.

### Step 5 — Pre-empt the two or three real objections

From discovery, name the objections that will actually be raised — usually price,
timeline, internal capacity, or a previous supplier's failure — and address each in
the proposal body rather than waiting for the meeting. An objection answered before
it is voiced reads as competence; the same answer given defensively in a meeting
reads as a concession.

Do not invent objections to look thorough. Two real ones beat six generic ones.

### Step 6 — Make the next step small and dated

Close with one concrete action, a name, and a date. "Let us know if you would like to
proceed" is not a next step. "If this looks right, I will send the SOW for signature
and we can start on the 14th; I have held that week" is.

### Step 7 — Keep it short

Length correlates negatively with acceptance. Two to four pages for most engagements.
Everything that is reference material — methodology, credentials, case studies — goes
in an appendix the decision-maker need not read.

---

## Output Format

```markdown
# [Engagement name]
### Prepared for [client] · [date] · Valid until [date]

## The problem as we understand it
[their words, their metrics, the consequence]

## What success looks like
[the changed state, measurable where possible]

## Options
### Option A — [name] · [price]
**What you get** · **Judged complete when** · **Timeline**
### Option B — [name] · [price] — *recommended, because [reason]*
### Option C — [name] · [price]

## What we need from you
| Input | Owner | By when | If late |
|---|---|---|---|

## What this assumes
- ...

## What is not included
- [exclusion] — [available separately / not offered]

## Timeline
| Milestone | Date | Judged complete when |
|---|---|---|

## Investment and payment
| Payment | Amount | Trigger |
|---|---|---|

## If things change
[change-order trigger and procedure, in one short paragraph]

## Why us
[short — only what is relevant to this problem]

## Next step
[one action, a name, a date]

---
### Appendix
[method, credentials, references]
```

---

## Verification

- [ ] The opening paragraph uses the client's words from discovery, not your framing.
- [ ] Two or three options, tiered by scope and not by quality.
- [ ] The recommended option is marked and the reason given.
- [ ] Every section maps to a SOW section; deliverable and acceptance language is
      liftable verbatim.
- [ ] Exclusions appear in the proposal body, not only in attached terms.
- [ ] Each acceptance criterion is objectively testable.
- [ ] Client obligations have dates and a stated consequence for lateness.
- [ ] Two or three real objections are addressed.
- [ ] The next step names an action, a person and a date.
- [ ] Body is under four pages.

**False-positive prevention.** The characteristic failure is a proposal that reads
beautifully and cannot be converted into a contract, because its scope language is
persuasive rather than precise. Test every deliverable line by asking: could a
stranger holding only this sentence tell whether it had been delivered? "Strategic
review of the data platform" fails. "A written assessment of the seven named
pipelines against the six criteria in Appendix A, with a prioritised remediation
sequence" passes.

The second failure is quality-tiered options, which invite the client to ask what the
cheap version leaves out and whether the expensive one is padding. Tier by scope.

The third is the proposal that omits exclusions to avoid seeming negative. Every
exclusion omitted here becomes a conversation in delivery, at a worse moment and with
less goodwill available.

Run the draft through `../content-quality/quality_slop_client_deliverable.md` before
sending.

---

## Related

- `business_writing_proposal.md` — the general/internal proposal
- `../content-quality/quality_slop_client_deliverable.md` — the quality gate
- `../../domain-legal/contracts-transactional/legal_sow_drafter.md` — the SOW this maps to
- `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` — testable acceptance criteria
- `../../domain-business-strategy/client-services/services_pricing_model_selector.md` — the structure being proposed
- `../../domain-negotiation/preparation/negotiation_opening_offer_design.md` — where the numbers came from

---
title: "Services Offer Definition and Boundary"
category: client-services/offer
description: "Turn a vague 'I help people with X' into a named services offer with a stated outcome, a fixed set of deliverables, an explicit exclusion list, and the boundary conditions under which you will not take the work — the document every later pricing, scoping and proposal step reads from"
techniques:
  - CM-03
  - CM-02
  - NE-09
  - QA-08
  - OC-03
difficulty: intermediate
tags:
  - consulting
  - freelance
  - services
  - offer-design
  - scope-boundary
  - positioning
  - solo-operator
updated: "2026-09-21"
---

# Services Offer Definition and Boundary

**Objective:** Convert an unbounded description of what you do into a **named offer**
with one stated outcome, a closed list of deliverables, an explicit exclusion list,
and the boundary conditions that make you decline. The output is a reusable offer
record that every downstream step — qualification, scoping, pricing, proposal, change
control — reads from, so those steps stop re-litigating what the offer is.

**When to Use:** Use this first, before any client conversation, and revisit it
whenever you have taken work that felt wrong. The symptom this fixes is a practice
where every engagement is bespoke, every proposal starts from a blank page, and scope
arguments happen mid-delivery because nothing ever said what was out.

This is **distinct from** `startup/copy/startup_value_proposition.md` and
`go-to-market/marketing_competitive_differentiation.md`, which position a *product*
to a market. This defines a *service* you personally deliver, and its central output
is the exclusion list — the part a product positioning document never has.

---

## Context Gathering

Ask for these before writing anything. Do not infer them.

1. **The work itself**
   - "Describe the last three pieces of paid work you did. What did the client
     actually receive?"
   - "Which of those would you happily do again? Which drained you?"
   - "What did you do in each that you were not paid for?"

2. **The outcome**
   - "When this goes well, what is measurably different for the client afterward?"
   - "How long after you finish does that difference show up?"
   - "Who inside the client organization notices?"

3. **The edges**
   - "What have clients asked you for that you should have said no to?"
   - "What work do you technically *can* do but do not want to be known for?"
   - "What do you need from the client for this to work at all?"

If the answer to the outcome questions is a description of activity ("I do a code
audit") rather than a change of state ("their deploy failures drop and they know
why"), stop and press again. An offer built on activity cannot be priced on value
and cannot be scoped to a finish line.

---

## Method

### Step 1 — Name the outcome, not the activity

Write one sentence in this shape:

> For **[specific client type]** who **[specific trigger situation]**, this engagement
> produces **[changed state]** within **[time window]**.

Reject any sentence where the changed state is a document. A document is a
deliverable, not an outcome. "A written architecture review" is activity; "the team
can name their three highest-risk components and has a sequenced plan for each" is an
outcome that happens to arrive as a document.

### Step 2 — Close the deliverable list

List every artifact the client receives. Then apply the closure test:

- Each deliverable names a **format** and an **acceptance condition**.
- The list ends with "and nothing else."
- Any deliverable that cannot be produced without an input you have not secured moves
  to the assumptions list, not the deliverable list.

### Step 3 — Write the exclusion list

This is the step people skip and the reason scope arguments happen. For each
deliverable, ask "what will a reasonable client assume is included that is not?" and
write it down as an explicit exclusion. Work through at minimum:

| Axis | The assumption to pre-empt |
|---|---|
| Implementation | Do you *do* the fix, or *specify* it? |
| Rounds | How many revision cycles before it becomes new work? |
| Access | Whose systems, whose credentials, whose meetings? |
| Stakeholders | How many interviews, how many review meetings? |
| Downstream | Do you support the thing after handover? For how long? |
| Adjacent scope | The obvious next question the work raises — is answering it in? |
| Tooling | Do you leave behind something they run, and who maintains it? |

### Step 4 — State the boundary conditions

Write the conditions under which you decline or stop. Three kinds:

- **Entry conditions** — what must be true for you to start (a named decision-maker,
  access granted, a defined problem, budget confirmed).
- **Continuation conditions** — what must remain true (responsiveness within N days,
  access maintained, scope stable).
- **Hard exclusions** — work you will not take at any price, and why. Be specific
  enough that the rule decides for you when you are tired and the money is good.

### Step 5 — Name what this offer is not

List the two or three adjacent things clients will confuse this with, and say who to
go to instead. This is a commercial asset, not a disclaimer: referring out cleanly is
the cheapest referral source you have.

---

## Output Format

```markdown
## Offer: [name]

**Outcome statement**
For [client type] who [trigger], this produces [changed state] within [window].

**Deliverables** (closed list)
| # | Deliverable | Format | Accepted when |
|---|---|---|---|

**Explicitly excluded**
- [exclusion] — available as a separate engagement / not offered

**Entry conditions** (all must hold before start)
- [ ] ...

**Continuation conditions** (engagement pauses if breached)
- ...

**Hard exclusions** (declined at any price)
- [work] — because [reason]

**Commonly confused with**
- [adjacent offer] → refer to [who]

**Inputs required from client**
| Input | Needed by | If absent |
|---|---|---|
```

---

## Verification

Before accepting the output, check each:

- [ ] The outcome statement survives the "so what?" test twice in a row.
- [ ] No deliverable is a verb phrase without an artifact.
- [ ] The exclusion list is not empty and contains at least one thing you have
      actually been asked for and regretted saying yes to.
- [ ] Every entry condition is observable — you can tell whether it holds without
      asking the client's opinion.
- [ ] Reading only the deliverable and exclusion lists, someone else could tell a
      prospect what they are buying.

**False-positive prevention.** The common failure is an exclusion list that excludes
only absurdities ("we do not provide legal advice") while leaving the genuinely
contested territory unnamed. If no item on the exclusion list would ever cause a
client to say "oh — I assumed that was included," the list is decorative. Force at
least three exclusions drawn from real past friction.

The second failure is boundary conditions written as aspirations ("client should be
responsive"). A boundary condition that cannot be breached observably is not a
boundary condition. Rewrite it with a number.

---

## Related

- `services_ideal_client_and_disqualifiers.md` — who this offer is for, and who to turn away
- `services_pricing_model_selector.md` — how this offer should be charged for
- `services_productized_offer_designer.md` — tightening this into a fixed-price package
- `../../domain-legal/contracts-transactional/legal_sow_drafter.md` — the contractual form of the deliverable and exclusion lists

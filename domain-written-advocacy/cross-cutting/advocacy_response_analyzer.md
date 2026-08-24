---
title: "Response Analyzer — Work Out What They Actually Committed To"
category: advocacy
description: "Help a person read an organization's written reply and separate what it actually commits to from what it only appears to say — which asks were answered, which were dodged, what is conditional, what is a final response, and what the next move is. Does NOT interpret the reply as a legal position, tell the user whether the organization's stance is lawful or their obligations are met, predict outcomes, assess claim strength, or read in commitments the text does not contain. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - complaint
  - escalation
  - documentation
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md
  - domain-written-advocacy/cross-cutting/advocacy_request_letter_architect.md
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
---

**Purpose:** Help you read a reply from a company, agency, insurer, or institution and work out **what it actually commits to**. Corporate replies routinely sound responsive while committing to nothing: they acknowledge without agreeing, restate policy without applying it, answer a question you did not ask, or promise a review with no date. This maps your original asks against the reply, marks each one answered, partly answered, dodged, or refused, and identifies what to do next.

**When to use:** You sent a request or complaint, a written reply arrived, and you are not sure whether you got what you asked for, whether it is a refusal, or whether it is their final word.

**When NOT to use:** No reply arrived → `advocacy_followup_and_deadline_tracker.md`. You want to know whether their position is lawful or whether they have met a legal obligation → that is legal analysis; route to an attorney or legal aid. The reply is a legal document — a claim, a notice of proceedings, a settlement offer, or anything from a law firm → stop and route to an attorney.

---

## Boundary & Routing Block

Use a different pathway if:
- **The reply is from a law firm, or is a claim, court document, notice of proceedings, or settlement offer** → do not analyze or answer it here. Route to an attorney or **legal aid** promptly; replying without advice can affect your position.
- **The reply asks you to sign, waive, release, or accept anything in exchange for a resolution** → have an attorney or legal aid read it before you sign. A release can end rights you did not know you had.
- **The reply states a deadline for you to respond or appeal** → treat the timing as urgent and route the deadline question to an attorney or legal aid; do not assume a stated deadline is accurate or that it is the only one.
- **The reply contains a threat, or the matter has a safety dimension** → route per `domain-legal/personal-self-advocacy/`, and do not respond directly if the other party is an abuser or subject to a protective order.

This prompt is educational support for reading your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **maps your own asks against the text of the reply you received**. It is **not legal advice, legal strategy, an interpretation of your legal rights, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you whether the organization's position is lawful, whether it has met any legal obligation, or whether a stated policy is enforceable; interpret the reply as a legal position or admission; tell you whether a deadline it states is valid; predict what the organization will do next or how a dispute would resolve; assess how strong your position is; cite a statute or regulation as authority; or read a commitment into the text that the words do not contain. Consumer, insurance, and contract rules **vary by state and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Map ask by ask.** Take your original request apart into its individual asks and check the reply against each one. A reply that answers one of three asks is two-thirds unanswered, however warm its tone.
2. **Acknowledgement is not agreement.** "We understand your frustration," "your feedback is important," and "we have logged your concerns" commit to nothing. Mark them as acknowledgement and move on.
3. **A policy statement is not a decision on your case.** "Our policy is that refunds are issued within 14 days of approval" does not say whether yours was approved. Look for the sentence that applies the policy to you; if there is none, that is the gap.
4. **Commitments need a verb, an owner, and a date.** "We will refund $X to your card by [date]" is a commitment. "We will look into this" is not. Extract only the ones that have all three, and note what is missing from the rest.
5. **Conditions change everything.** "We can process this once you provide Y" is a conditional commitment — record the condition, because meeting it is now your next action and the clock restarts from it.
6. **Identify whether this is a final response.** Many escalation routes and external bodies care whether the organization has given its final word. If the reply says so, note it; if it is ambiguous, the next letter can ask directly.
7. **You read and decide; the professional assesses.** What the words say is something you can establish. Whether their position is lawful, and what you could do about it, is for an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **What you originally asked for:** [each ask, listed separately]
- **The reply, in full:** [paste verbatim — do not summarize]
- **Date received and channel:** [YYYY-MM-DD, email / letter / portal]
- **Who it is from:** [name, role, department if stated]
- **Does it say it is a final response?:** [yes / no / unclear]
- **Does it state a deadline for you?:** [what and when — flag *verify with an attorney*]
- **Does it ask you to sign, accept, or waive anything?:** [if yes → Boundary & Routing Block]
- **Prior contacts on this matter:** [dates and outcomes]
- **Any legal, deadline, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and the reply in full; work only from its actual text.
- Decompose the user's original request into individual asks before analysis.
- Classify each ask as answered, partly answered, dodged, refused, or conditional, quoting the sentence relied on.
- Quote verbatim when attributing a position to the organization; never paraphrase into a stronger or weaker claim.
- Extract only commitments that name an action, an owner, and a date; list the rest as non-commitments with what is missing.
- Record any condition placed on the user and what meeting it requires.
- Identify whether the reply is a final response, or flag it as unclear.
- Route any signature, waiver, release, deadline, or law-firm correspondence to an attorney before the user acts.

**Must Not:**
- State whether the organization's position is lawful, correct, or compliant with any obligation.
- Interpret any sentence as a legal admission, waiver, or binding legal position.
- Tell the user whether a deadline stated in the reply is valid or the only one that applies.
- Predict what the organization will do next, or how a dispute would resolve.
- Assess how strong the user's position is.
- Cite or invent a statute, regulation, or contract term as authority.
- Read a commitment into wording that does not contain one, or soften a refusal into a maybe.
- Characterize the organization or its staff, or attribute motive to the reply's wording.
- Draft a legal threat as the recommended next move.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for law-firm correspondence, a claim or court document, a signature or waiver request, a stated deadline, or a safety dimension → route per the Boundary & Routing Block before any analysis. Restate the jurisdiction and the boundary: this reads the text; legality is for an attorney.

### Stage 2 — Decompose the Original Request
List the user's original asks separately and precisely, in the words they used. This list is the checklist the reply is scored against, so it must reflect what was actually asked rather than what the user hoped to convey.

### Stage 3 — Map the Reply Against Each Ask
For each ask, find the sentence in the reply that addresses it and quote it verbatim. Classify: **answered** (a clear response with a decision), **partly answered** (addressed but incomplete), **dodged** (acknowledged without response), **refused** (declined, with or without a reason), or **conditional** (contingent on the user doing something). Where no sentence addresses the ask at all, record it as unaddressed.

### Stage 4 — Separate Commitments From Language That Sounds Like One
Extract every statement with an action, an owner, and a date into a commitment table. Put everything that sounds responsive but lacks one of the three into a second table, naming what is missing. Record conditions placed on the user with what meeting them requires.

### Stage 5 — Establish Status and What Is Outstanding
Determine whether the reply is a final response, states a deadline, or requests a signature. Summarize what remains outstanding: unaddressed asks, missing dates on vague commitments, and conditions to meet. Do not assess whether the outcome is fair or lawful.

### Stage 6 — Set the Next Move and Close
Recommend one next action from: meet the stated condition; ask the specific unanswered questions in writing; request an explicit final response; escalate a rung; or route to an attorney or legal aid. Keep the original ask unchanged. Draft the short follow-up if one is the right move. Route legal questions onward.

---

## Output Format

```markdown
MY OWN ANALYSIS OF THEIR REPLY — NOT A LEGAL FILING
Reply received [YYYY-MM-DD] via [channel] from [name / department].
This is my own reading of what the reply says. It does NOT state whether their position is
lawful or compliant, treat anything as a legal admission, validate any deadline they state,
or predict what they will do. Legal questions are for an attorney.

## What I originally asked for
1. [ask one, in my own original words]
2. [ask two]
3. [ask three]

## How the reply addresses each ask
| # | My ask | Status | The sentence they rely on (verbatim) |
|---|---|---|---|
| 1 | [ask one] | Answered | "[exact quote]" |
| 2 | [ask two] | Dodged | "[exact quote — acknowledgement only]" |
| 3 | [ask three] | Conditional | "[exact quote — requires me to provide X]" |
| — | [ask four] | Unaddressed | No sentence in the reply addresses this |

## Commitments (action + owner + date — all three present)
| What they committed to | Who | By when | How I will verify |
|---|---|---|---|
| [refund $X to card ending NNNN] | [dept] | [YYYY-MM-DD] | [check statement on that date] |

## Sounds like a commitment but is not
| Their wording | What is missing |
|---|---|
| "We will look into this and be in touch" | No action specified, no date |
| "Our policy is refunds issue within 14 days of approval" | Policy statement — does not say my case is approved |
| "We understand your frustration" | Acknowledgement only — no response to any ask |

## Conditions placed on me
| Condition | What meeting it requires | My deadline (if stated) |
|---|---|---|
| [provide proof of purchase] | [locate and send receipt] | [YYYY-MM-DD — *verify any legal deadline with an attorney*] |

## Status
- Final response? [Yes — they state it / No / Unclear — I can ask directly]
- Deadline stated for me? [what and when — *verify with an attorney; do not assume it is the only one*]
- Asks me to sign, accept, or waive anything? [No / **Yes → route to an attorney before signing**]

## Still outstanding
- [unaddressed ask #4]
- [vague commitment needing a date]
- [condition to meet]

## My next move
[One of: meet the condition; ask the unanswered questions in writing; request an explicit
final response; escalate one rung; route to an attorney or legal aid.]

### Follow-up message (my own words, if that is the move)
> Re: [subject] — account [#]. Further to your reply of [date]:
>
> Thank you for your response. Two of my three requests remain unaddressed:
> - [ask two] — your reply acknowledges this but does not respond to it.
> - [ask four] — your reply does not mention this.
>
> [If a vague commitment:] You say you will [X]. Please confirm the date by which this
> will be completed.
>
> [If clarifying status:] Please confirm whether this is your final response on this matter.
>
> My request is unchanged: [the original ask].
>
> Please respond in writing by [date].
> [Your name], [account #], [YYYY-MM-DD]

---
Note to self: this is my own reading, not legal advice. Whether their position is lawful,
whether any deadline they state is accurate or complete, and what I could do about it are for
an attorney or legal aid. I will not sign, accept, or waive anything without advice.
*Verify for your jurisdiction — consumer and contract rules vary by state and country.*
```

---

## Verification

- [ ] Jurisdiction captured, full reply supplied, and legal questions routed *verify with an attorney*?
- [ ] Law-firm correspondence, claim, waiver, or signature request screened and routed before analysis?
- [ ] Original request decomposed into individual asks in the user's own words?
- [ ] Every ask classified, with the sentence relied on quoted verbatim?
- [ ] Unaddressed asks recorded as unaddressed rather than inferred as answered?
- [ ] Commitments include action, owner, and date; near-commitments listed with what is missing?
- [ ] Conditions on the user recorded with what meeting them requires?
- [ ] Final-response status identified or flagged unclear?
- [ ] No statement that their position is lawful, correct, or compliant?
- [ ] Nothing treated as a legal admission, waiver, or binding position?
- [ ] No validation of any deadline they state; timing routed to an attorney?
- [ ] No outcome prediction, strength assessment, or motive attribution?
- [ ] Next move keeps the original ask unchanged?
- [ ] Deadline, waiver, legal, or safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Their refusal is unlawful — they can't do that" | Record the refusal and its wording; lawfulness is for an attorney |
| "By apologizing they've admitted fault" | An apology is not an admission; quote it and classify it as acknowledgement |
| "'We'll look into it' means a refund is coming" | List it as a non-commitment: no action specified, no date |
| "You have 14 days as they state, so act by then" | Note the stated deadline; *verify with an attorney whether it is accurate or the only one* |
| "They'll cave if you push once more" | Make no prediction about what the organization will do |
| Summarize their position in stronger words than they used | Quote verbatim; never paraphrase into a stronger or weaker claim |
| Treat a policy statement as a decision on this case | Mark it a policy statement and note that no sentence applies it to the user |
| Advise signing the settlement to close it out | Route any signature, waiver, or release to an attorney before signing |
| Raise the ask because the reply was dismissive | Keep the original ask unchanged; a shifting ask weakens the record |
| Analyze a letter from their law firm | Stop, use the Boundary & Routing Block, route to an attorney |

---

## Adaptations

**By reply type:**
- **Template or bot reply with a ticket number:** Often addresses nothing. Record the ticket number, mark all asks unaddressed, and ask for a human response referencing the ticket.
- **Partial approval:** Separate the approved portion from the outstanding one and confirm the approved part in writing with its date; keep the remainder live rather than letting it close.
- **Refusal with a stated reason:** Record the reason verbatim — it is the thing an escalation or external body will examine, and its wording matters more than its tone.
- **Refusal with no reason:** Ask for the reason in writing and for confirmation of whether it is a final response; both are ordinary requests.

**By situation/profile:**
- **Reply changed the subject:** Restate the original asks numerically and ask for a numbered response; it is harder to dodge a numbered list twice.
- **Reply promises a callback:** Ask for the outcome in writing instead, or send a same-day confirmation after the call — see `advocacy_channel_and_record_strategy.md`.
- **Several replies from different departments:** Map them all against the same ask list; inconsistencies between departments are themselves a fact for escalation.
- **Legal, waiver, or safety dimension:** Boundary & Routing Block first; do not reply before routing.

---

## Related Prompts

- `advocacy_escalation_ladder_designer.md` — when the reply is a refusal or a final response.
- `advocacy_followup_and_deadline_tracker.md` — when a commitment has a date and you need to track it.
- `advocacy_request_letter_architect.md` — the original request this reply responds to.
- `advocacy_correspondence_log_builder.md` — log the reply and its commitments into the running record.

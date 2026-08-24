---
title: "Authority and Mandate Limits — Set Yours, Probe Theirs, Survive Ratification"
category: negotiation/at-the-table
description: "Establish what you can agree to before you walk in, determine what the counterpart can actually agree to, and design the deal so it survives whoever must approve it. Covers probing authority without insulting anyone, responding to a late 'I'll have to check with my boss,' deciding whether to claim limited authority yourself, and pre-empting the ratification renegotiation where an approver reopens settled terms. Counters the failure that voids more agreements than any tactic: negotiating to a signature with someone who was never able to give one."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - negotiation
  - authority
  - mandate
  - ratification
  - decision-maker
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, adversarial, systems]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [structured, dialog]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [diagnose, plan, rehearse]
related_prompts:
  - domain-negotiation/preparation/negotiation_counterpart_simulation.md
  - domain-negotiation/at-the-table/negotiation_impasse_breaker.md
  - domain-negotiation/multi-party/negotiation_multi_party_alignment.md
---

# Authority and Mandate Limits — Set Yours, Probe Theirs, Survive Ratification

**Objective:** More agreements are voided by authority problems than by any coercive tactic. The counterpart cannot actually approve what they just agreed to; a committee reopens terms you thought settled; you commit to something outside your own mandate and have to walk it back, spending credibility you needed later. This prompt handles all three. It fixes **your** mandate in writing before the conversation — what you can agree to, what needs approval, and what you will never commit to live. It probes **theirs** without the insult that "do you actually have authority?" carries. It designs for **ratification**, so terms survive the approver who was not in the room and who cares about different things. And it distinguishes the genuine mandate limit from the tactical one, since "I'll have to check with my boss" is both a real constraint and one of the oldest concession-extraction devices in the field.

**When to use:**
- Before any negotiation where either side may need approval from someone not present.
- The counterpart has just said they need to check with someone, and you need to decide how to respond.
- A previous deal was reopened at approval and you want to prevent a repeat.
- You are negotiating on behalf of an organization and need your own limits fixed before pressure applies.

**When NOT to use:**
- Both parties are the final decision-makers and no approval exists — though verify this rather than assume it.
- The problem is coalition structure across three or more parties — use `multi-party/negotiation_multi_party_alignment.md`.
- You need a full model of the counterpart's incentives, not just their authority — `preparation/negotiation_counterpart_simulation.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals negotiating where approval sits with someone other than the people talking.

---

## Inputs / Context

1. **The negotiation.** What is being negotiated and how close it is to conclusion.
2. **Your own authority.** What you can commit to, and what requires sign-off from whom.
3. **What you know of their structure.** Their role, seniority, and any approval process you are aware of.
4. **Signals observed.** Anything they have said about approvals, or any pattern of concessions reversing.
5. **The deal's approval-sensitive terms.** Which terms are most likely to trigger review — non-standard clauses, unusual pricing, precedent-setting provisions.
6. **Timeline.** Whether approval cycles fit the deadline.

---

## Constraints

### Must
- Fix **your own mandate in writing** before the conversation: full authority, needs-approval, and never-commit-live categories.
- Probe their authority **early and without insult**, using process questions rather than challenges to their standing.
- Map the **full approval chain** — not only who signs but who can veto, and what each cares about.
- Identify the **approval-sensitive terms** in advance and address the approver's concerns inside the deal rather than after it.
- Distinguish a **genuine mandate limit** from the tactical use of one, and respond differently to each.
- Design the **ratification defence**: what stops an approver reopening settled terms.
- Decide deliberately whether to **claim limited authority yourself**, and note the cost — it slows the deal and invites the same treatment.

### Must Not
- Ask "do you have the authority to agree to this?" It reads as a challenge to their standing, produces a defensive yes, and forecloses the honest answer.
- Assume seniority equals authority. Senior people frequently need approval for non-standard terms; junior ones sometimes hold delegated sign-off within a band.
- Accept a claimed limit as final without asking what would change it. "I'd need approval" and "that's not possible" are different sentences.
- Make your best offer before knowing whether the person can accept it. Concessions given to a non-decider are spent twice.
- Concede again at ratification without requiring something in return. Paying twice for the same agreement establishes the pattern permanently.
- Claim limited authority you do not have as a routine device. It works, and it is also how you lose the ability to close in the room.

---

## Instructions

### Step 1 — Fix your own mandate
Write three lists before anything else. **Full authority:** terms you can agree to and sign. **Needs approval:** terms requiring sign-off, with whose and how long it takes. **Never commit live:** terms you will not agree to in the room regardless of pressure, typically anything precedent-setting, anything outside policy, and anything you have not modelled. Then write the sentence you will use when you hit the boundary: "That's outside what I can commit to today — I can get you an answer by [when]."

### Step 2 — Probe their authority through process, not challenge
Ask questions about the *process*, which are natural and non-threatening, rather than about their *standing*, which is neither:
- "What does the approval path look like on your side once we agree?"
- "Who else will want to look at this before it's signed?"
- "Has your team done a deal on these terms before, or would this be a first?"
- "What's the timeline from handshake to signature for you?"

The last is the most informative and the least confrontational. An answer of "a few weeks and it goes to committee" tells you everything the direct question would have, without the defensiveness.

### Step 3 — Map the approval chain
Write who signs, who can veto, when the relevant body meets, and — most importantly — what the approver cares about that the negotiator does not. Approvers characteristically weigh precedent, risk, and consistency, where negotiators weigh price and closing. Deals die at ratification when the negotiator's concerns were fully addressed and the approver's were never raised.

### Step 4 — Identify approval-sensitive terms
Flag the terms most likely to trigger review: non-standard clauses, pricing outside the usual band, liability or indemnity changes, anything that sets a precedent, unusual term lengths. For each, decide whether to (a) pre-empt by building in what the approver will want, (b) trade it away early for something you value more, or (c) surface it explicitly and route it to the approver before the rest of the deal is settled.

### Step 5 — Classify a claimed limit when it appears
When they say they need approval, classify it:

| Signal | Reading |
|---|---|
| Raised early, with a specific process and named approver | Genuine |
| Raised late, after agreement, on the final term | Tactical |
| Approver's concerns are specific and consistent | Genuine |
| Approver appears only to require more from you | Tactical |
| Concessions reverse after breaks | Tactical |

For genuine limits, work with the constraint — ask what would need to be true for approval, and help them build the case. For tactical ones, use the Step 6 response.

### Step 6 — Respond to the late authority reveal
When "I need to check with my boss" appears after agreement and functions as a concession extraction, the response has three parts. **Freeze the agreed terms:** "Let's treat what we've agreed as settled and take just the open item to your approver." **Require reciprocity:** if the approver wants a change, that reopens the package, not just one term — "if the pricing moves, I'd need to revisit the term length as well." **Attach a condition:** make your last concession explicitly contingent on approval as-is ("this number is available on these terms; if terms change, the number changes"). Together these remove the profit from ratification renegotiation.

### Step 7 — Decide on claiming limited authority yourself
Claiming a limit you do have is honest and useful — it buys deliberation time and lets you decline without confrontation. Claiming one you do not have is a tactic with real costs: it slows every future deal with this counterpart, invites them to mirror it, and forfeits the ability to close in the room, which is sometimes worth more than the concession it extracts. Decide deliberately and note the cost.

### Step 8 — Build the ratification defence
Write what protects the deal at approval: a written summary of agreed terms circulated immediately, the justification the negotiator can carry to their approver, pre-emptive answers to the approver's likely objections, and an explicit statement that the package is integral. Where possible, get the approver's concerns surfaced *before* the deal is closed rather than after.

### Step 9 — Adversarial check
- If they cannot approve this, what have you already conceded that you cannot recover?
- Are you treating a genuine constraint as a tactic because it is inconvenient?
- What does the approver care about that has not been addressed anywhere in the deal?

---

## False-Positive Prevention

1. **The direct authority question.** "Are you able to approve this?" challenges their standing, produces a defensive and often inaccurate yes, and closes off the process questions that would have revealed the truth painlessly.
2. **Seniority-as-authority.** Assuming a senior title means sign-off. Non-standard terms escape most delegated authority regardless of level, and the terms you care about are usually the non-standard ones.
3. **Best offer to a non-decider.** Making your strongest offer before establishing who decides. The concession becomes the new baseline, and the actual decision-maker starts from there.
4. **Claimed-limit acceptance.** Treating "I'd need approval" as the end of the line. Ask what would need to be true for approval — frequently the constraint is a specific concern that can be addressed inside the deal.
5. **Paying twice.** Conceding again at ratification to save the deal. It closes this one and guarantees that every future negotiation with this counterpart has a ratification stage with a price attached.
6. **Approver omission.** Optimizing the deal for the person in the room. The negotiator's satisfaction is necessary and not sufficient; the approver weighs precedent and risk, which the negotiator may never have mentioned.
7. **Routine false-limit claiming.** Using "I'll have to check" as a standard device. It works, and it also trains the counterpart to hold their own final concession back, converting every deal into a two-stage process.
8. **Tactical over-diagnosis.** Reading a genuine approval requirement as manipulation. Most organizations really do have approval chains; treating a real constraint as a tactic insults a counterpart who is trying to help you.

---

## Output Format

```
# Authority Map — [negotiation]

## My mandate
| Full authority | Needs approval (whose / how long) | Never commit live |
|---|---|---|
| [...] | [...] | [...] |
Boundary sentence: "[...]"

## Their authority — probe results
| Process question asked | Answer | What it reveals |
|---|---|---|
| "What's the approval path?" | [...] | [...] |
| "Timeline from handshake to signature?" | [...] | [...] |

## Approval chain
Signs: [...] · Can veto: [...] · Meets: [...]
What the approver cares about that the negotiator doesn't: [...]

## Approval-sensitive terms
| Term | Why it triggers review | Strategy: pre-empt / trade away / surface early |
|---|---|---|
| [...] | [...] | [...] |

## Claimed-limit classification
Claim: "[...]" · Raised: [early / late] · On: [which term]
Verdict: genuine / tactical — because [...]

## Response
[If genuine:] What would need to be true for approval: [...] · How I help build the case: [...]
[If tactical:] Freeze script: "[...]" · Reciprocity script: "[...]" · Conditional concession: "[...]"

## My own limited-authority claim
Claiming a limit? [y/n] · Real or tactical? [...] · Cost accepted: [...]

## Ratification defence
- Written summary circulated: [when, to whom]
- Justification the negotiator carries to the approver: "[...]"
- Pre-empted approver objections: [...]
- Package stated as integral: [y/n]

## Adversarial check
- Already conceded and unrecoverable if they can't approve: [...]
- Genuine constraint I may be treating as a tactic: [...]
- Approver concern not addressed anywhere in the deal: [...]
```

---

## Verification

- [ ] Own mandate fixed in three categories before the conversation, with a boundary sentence.
- [ ] Their authority probed via process questions, never via a direct challenge to standing.
- [ ] Approval chain mapped including veto holders and meeting cadence.
- [ ] What the approver cares about that the negotiator doesn't is named explicitly.
- [ ] Approval-sensitive terms flagged with a strategy for each.
- [ ] Any claimed limit classified genuine or tactical with reasoning.
- [ ] Tactical-limit response includes freeze, reciprocity, and conditional-concession scripts.
- [ ] Decision on claiming your own limited authority made deliberately, with the cost noted.
- [ ] Ratification defence written, including the justification the negotiator carries upward.
- [ ] Adversarial check identifies unrecoverable concessions and unaddressed approver concerns.
- [ ] No best offer made before authority was established.
- [ ] No second concession at ratification without a required return.

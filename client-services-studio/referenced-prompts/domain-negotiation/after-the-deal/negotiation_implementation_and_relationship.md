---
title: "Implementation and Relationship — The Deal Is Signed and Nothing Has Happened"
category: negotiation/after-the-deal
description: "Convert signed terms into executed obligations. Extracts every commitment from the agreement with an owner and a date on each side, identifies the terms most likely to quietly lapse, sets early-warning signals for drift, and designs the relationship maintenance that makes the next negotiation cheaper. Includes the first-breach response ladder — the reaction to the first small failure sets the standard for the whole term. Counters the failure that wastes good negotiating: treating signature as the finish line when it is the point at which the obligations start."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negotiation
  - implementation
  - relationship
  - obligations
  - drift
updated: "2026-07-26"
reasoning:
  styles: [systems, analytic, strategic, empathic]
  stakes: variable
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, hr, lawyer, pm]
  mode: [plan, monitor, document]
related_prompts:
  - domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md
  - domain-negotiation/after-the-deal/negotiation_renegotiate_existing_agreement.md
  - domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md
---

# Implementation and Relationship — The Deal Is Signed and Nothing Has Happened

**Objective:** A negotiated term is a promise about future behaviour, and promises decay. The people who negotiated move on; the people who must execute were not in the room and do not know why a term exists; obligations without an owner become nobody's; and the terms hardest won are frequently the ones most likely to lapse, because they were concessions the other side never wanted to give. This prompt converts the agreement into an execution artifact: every commitment extracted with an owner and a date on **both** sides, the at-risk terms flagged, early-warning signals set for drift, and a response ladder for the first small breach — because how the first minor failure is handled sets the standard for the remainder of the term. It also treats the relationship as an asset with maintenance requirements, since the cheapest negotiation available is the renewal with a counterpart who trusts you.

This is the phase the domain otherwise ignores. It runs after `at-the-table/negotiation_closing_and_final_concession.md` and feeds `negotiation_renegotiate_existing_agreement.md` when terms need to change.

**When to use:**
- A deal has closed and you want it to actually deliver what was agreed.
- A previous agreement quietly failed to produce what was negotiated.
- You have inherited an agreement you did not negotiate and need to know what it requires.
- The first small breach has occurred and you are deciding how to respond.

**When NOT to use:**
- Terms need to change rather than be executed — `negotiation_renegotiate_existing_agreement.md`.
- You are assessing how the negotiation went — `negotiation_post_negotiation_debrief.md`.
- The agreement has failed and the question is exit — that is a legal question; route to `domain-legal/`.

**Audience:** Executives, founders, salespeople, people leaders, project leads, and individuals responsible for what a signed agreement actually produces.

---

## Inputs / Context

1. **The agreement.** Full terms as signed.
2. **What was said but not written.** Understandings, assurances, and context that shaped the deal.
3. **Who executes.** The people on each side who will do the work, and whether they were in the negotiation.
4. **Term length and key dates.** Renewal, review, milestone, and notice dates.
5. **The relationship state.** How the negotiation ended and how each side feels about it.
6. **Precedent.** Whether this agreement sets a template for others.

---

## Constraints

### Must
- Extract **every commitment with an owner and a date**, on both sides. An obligation without a named owner is not an obligation.
- Identify the **at-risk terms** — those most likely to lapse — and explain why each is at risk.
- Transfer the **rationale** to the executors. People who do not know why a term exists deprioritize it, reasonably.
- Set **early-warning signals** for drift, defined so they can be noticed before the breach rather than after.
- Design the **first-breach response**, recognizing it establishes the standard for the term.
- Capture **what was agreed but not written**, and decide whether each item needs documenting.
- Diarize the **decision dates** — notice periods, renewal windows, review points — with enough lead time to act rather than react.

### Must Not
- Assume the written agreement captures the deal. Assurances given in the room shape expectations and are the most common source of implementation disputes.
- Leave your own obligations unowned while tracking only theirs. Your breaches license theirs and forfeit standing.
- Escalate the first minor breach to a formal remedy without a proportionate step first — it converts a working relationship into an adversarial one over something small.
- Ignore a first minor breach either. Unaddressed, it becomes the operating standard, and the next one is larger.
- Treat the relationship as concluded at signature. The counterpart's cooperation during the term is discretionary in ways no contract can compel.
- Let the renewal or notice date arrive without preparation — that is how leverage is forfeited by calendar.

---

## Instructions

### Step 1 — Extract the commitment register
Go through the agreement clause by clause and pull every obligation into a register: what, who owns it (a named person, not a team), by when, and how it will be evidenced. Do both sides. Terms that produce no register entry are either not obligations or are unenforceable in practice, and both cases are worth knowing.

### Step 2 — Flag the at-risk terms
Mark the terms most likely to lapse, and say why. The reliable predictors:

| At-risk pattern | Why |
|---|---|
| Hard-won concessions | They never wanted to give it; enthusiasm for executing it is low |
| Terms with no owner on their side | Nobody's job |
| Obligations far in the future | No proximate trigger, and staff turn over |
| Anything requiring proactive action | Passive terms self-execute; active ones need someone to act |
| Terms the executors weren't consulted on | Perceived as imposed, deprioritized quietly |

### Step 3 — Transfer the rationale to the executors
The people delivering this were mostly not in the room. Write a short brief for them: what was agreed, what matters most and why, which terms were hard-won and must not be casually traded away in day-to-day dealings, and who to tell if something is drifting. Executors who understand why a term exists protect it; executors who see an arbitrary constraint route around it — and they are right to, given what they know.

### Step 4 — Set early-warning signals
For each at-risk term, define the signal that indicates drift **before** it becomes a breach: a missed interim date, a response-time change, a personnel change on their side, a quality trend, a meeting that stops happening. Assign who watches each and how often. The purpose is to intervene while it is still a conversation rather than a claim.

### Step 5 — Design the first-breach ladder
The first small failure is the most consequential moment of the term, because the response sets the standard. The ladder, in order:

1. **Notice informally, immediately** — name it once, lightly, without accusation: "the reporting didn't come through last week — did something change?"
2. **Confirm in writing** if it recurs, still without escalation, so a record exists.
3. **Raise formally** with reference to the term, if it continues.
4. **Invoke remedy** only after the first three have run.

The failure modes are symmetric and both common: skipping straight to step 3 or 4 over something minor, which converts a working relationship into an adversarial one; and never leaving step 0, which quietly establishes the breach as the new baseline.

### Step 6 — Capture what was said but not written
List the assurances, understandings, and context that shaped the deal but are not in the document — how a discretionary term would be exercised, what a vague clause was understood to mean, what the counterpart said about their intentions. For each, decide: document it in a follow-up note, raise it now, or accept the risk consciously. Silent reliance on an unwritten understanding is the most common route to a genuine dispute, because both parties are sincere.

### Step 7 — Diarize the decision dates and maintain the relationship
Put every notice period, renewal window, review point, and milestone in a calendar with lead time — a renewal that auto-extends because nobody diarized the notice date is leverage lost to a calendar. Then plan relationship maintenance: a regular check-in that is not about a problem, early notice when *you* will miss something, and visible delivery of your own obligations. Each of these makes the renewal negotiation cheaper, and the counterpart's discretionary cooperation is worth more during the term than most of the terms are.

### Step 8 — Record the precedent
Note what this agreement establishes for the next one: terms that become the baseline, concessions that will be expected again, and anything you would not want repeated. Written terms persist across renewals with far more force than anyone anticipates at signature.

### Step 9 — Adversarial check
- Which of your own obligations is least likely to be met, and what happens when they raise it?
- If the person who negotiated this leaves tomorrow, what is lost that is not written down?
- What are you relying on that exists only as something someone said?

---

## False-Positive Prevention

1. **Signature-as-completion.** Treating the close as the end. The obligations begin at signature, and the value negotiated is realized only if they are executed.
2. **Unowned obligations.** A register listing teams rather than named people. "Operations will provide monthly reporting" is not owned; a person with a name and a date is.
3. **One-sided tracking.** Monitoring their obligations while leaving yours unmanaged. Your breaches license theirs, forfeit your standing to raise anything, and are usually noticed first by them.
4. **Rationale loss.** Handing terms to executors without the reasons. A constraint with no visible purpose is routed around by competent people acting reasonably on what they know.
5. **First-breach over-escalation.** Going formal over a minor first failure. It converts a working relationship into an adversarial one over something that a single light comment would have fixed.
6. **First-breach under-response.** Letting the first small failure pass to preserve goodwill. It becomes the operating standard, the next failure is larger, and raising it later is harder because you accepted the first.
7. **Unwritten reliance.** Depending on an assurance given in the room. Both parties usually remember it sincerely and differently, which is what makes these disputes intractable.
8. **Calendar forfeiture.** Missing a notice or renewal window. Leverage that took a negotiation to build is lost to an unentered date, and the auto-renewal is on their terms.

---

## Output Format

```
# Implementation Plan — [agreement]

## Commitment register
| # | Obligation | Side | Owner (named) | Due | Evidence | At risk? |
|---|---|---|---|---|---|---|
| 1 | [...] | mine/theirs | [...] | [...] | [...] | y/n |

## At-risk terms
| Term | Why at risk | Mitigation |
|---|---|---|
| [...] | [hard-won / no owner / distant / proactive / executors not consulted] | [...] |

## Executor brief
What was agreed: [...]
What matters most and why: [...]
Hard-won terms not to trade away informally: [...]
Tell [name] if: [...]

## Early-warning signals
| Term | Signal of drift | Who watches | How often |
|---|---|---|---|
| [...] | [...] | [...] | [...] |

## First-breach ladder
1. Informal notice: "[...]"
2. Written confirmation if repeated: [...]
3. Formal raise referencing the term: [...]
4. Remedy: [only after 1–3]
Current position on ladder: [...]

## Said but not written
| Understanding | Source | Decision: document / raise now / accept risk |
|---|---|---|
| [...] | [...] | [...] |

## Diarized dates
| Date | What | Lead time set | Owner |
|---|---|---|---|
| [...] | notice / renewal / review / milestone | [...] | [...] |

## Relationship maintenance
Regular non-problem check-in: [cadence]
Commitment: early notice when I will miss something — [confirmed]
My visible deliverables: [...]

## Precedent set
Becomes baseline for next time: [...]
Would not want repeated: [...]

## Adversarial check
- My obligation least likely to be met, and their response: [...]
- If the negotiator leaves tomorrow, what is lost: [...]
- What I'm relying on that only exists as something someone said: [...]
```

---

## Verification

- [ ] Every obligation in the register has a named owner and a date, on both sides.
- [ ] At-risk terms flagged with the specific reason each is at risk.
- [ ] Executor brief written, transferring rationale and naming hard-won terms.
- [ ] Early-warning signals defined so drift is visible before breach, with a watcher assigned.
- [ ] First-breach ladder specified with an informal first step and formal remedy last.
- [ ] Unwritten understandings captured with an explicit decision on each.
- [ ] All notice, renewal, and review dates diarized with lead time.
- [ ] Relationship maintenance planned, including early notice of your own misses.
- [ ] Precedent recorded for the next negotiation.
- [ ] Adversarial check identifies your own weakest obligation and the knowledge lost if the negotiator leaves.
- [ ] Your own obligations tracked, not only theirs.
- [ ] No obligation owned by a team rather than a person.

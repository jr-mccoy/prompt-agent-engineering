---
title: "Renewal Risk and Save Plan — One B2B Contract, Its Real Decider, the Deciding Reason, and a Save Sequence with a Floor"
category: sales-customer/customer-success
description: "For one named B2B account with a renewal inside roughly 180 days, map the contract mechanics and the people who decide the renewal now, separate the stated risk from the deciding reason with evidence, and build a dated save sequence that remediates value before it concedes price — with a concession floor, a downsell path and a let-go rule — distinct from the churn-prevention skill's self-serve cancel flows, save offers and dunning."
techniques:
  - RT-05
  - DS-06
  - CM-02
  - DP-13
difficulty: advanced
tags:
  - customer-success
  - renewal
  - churn-risk
  - retention
  - account-management
  - b2b
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/customer-success/cs_quarterly_business_review_prep.md
  - domain-business-strategy/go-to-market/workflow_cs_account_health.md
  - domain-agentic-resources/skills/marketing/churn-prevention/SKILL.md
---

# Renewal Risk and Save Plan

**Objective:** Decide how at-risk one contract renewal really is, why, and what
sequence of moves — in what order, by when, with what limit on concessions — gives
it the best chance, including the honest option of a smaller renewal or none.

**When to Use:**
- A renewal is 30–180 days out and something has changed: a sponsor left, usage
  fell, a competitor is in, a budget review was announced.
- The customer has asked for a "renewal conversation" early, or gone quiet.
- Leadership wants a save plan and a number, and the account team has only a mood.
- **Not this prompt if** the churn is self-serve — cancel-flow design, exit
  surveys, pause and downgrade offers, failed-payment dunning — which belongs to
  `domain-agentic-resources/skills/marketing/churn-prevention/`. For the general
  health diagnosis across usage, support and relationship signals, run
  `domain-business-strategy/go-to-market/workflow_cs_account_health.md` first; this
  prompt takes its output and plans the renewal event. The bargaining itself
  belongs to `domain-negotiation/after-the-deal/negotiation_renegotiate_existing_agreement.md`.

## Inputs / Context

1. **Contract mechanics:** renewal date, term, auto-renew, notice period, price
   and any uplift clause, termination rights. From the contract — not memory.
2. **Health data:** usage trend, outcomes against their goals, support history.
3. **People:** who signed originally, who holds budget now, sponsor status,
   procurement involvement.
4. **Signals:** what the customer has said about renewal, with who and when;
   competitor mentions; budget events.
5. **Commercial room:** approved discount authority, list price, cost to serve,
   and any precedent across the customer base.

## Method

1. **Fix the calendar from the contract.** The real deadline is the notice date,
   not the renewal date. Count weeks from today to notice.

2. **Map the renewal decider.** Who decides *this* renewal — often not who bought
   it. Mark each person: supporter, neutral, detractor, unknown, and whether you
   have direct access.

3. **Separate the stated risk from the deciding reason (RT-05).** The customer
   says "budget"; the evidence may say "the sponsor left and no one owns the
   outcome." For each candidate reason cite the signal, who, and when. Rank
   candidates by evidence, and name the one that, if fixed, most changes the
   decision.

4. **Rate the risk.** Probability band (Low <20% / Medium 20–50% / High >50% of
   non-renewal or material downsell) with a confidence note. Rate ARR at risk
   separately: full, partial, or expansion lost.

5. **Sequence the save (DS-06).** In this order, each with owner and date:
   1. **Access** — get to the decider; exec-to-exec if needed.
   2. **Value remediation** — fix the deciding reason: re-onboarding, a new
      sponsor, an adoption push, a support recovery.
   3. **Proof** — outcomes against their goals, sourced.
   4. **Commercial** — only now: term, scope, price structure.
   Skipping to step 4 trains the account to threaten non-renewal every year.

6. **Constrain the concessions (CM-02).**
   - **Must:** every concession buys something (term, reference, scope, timing).
   - **Must not:** exceed approved authority; concede before the deciding reason
     is addressed; offer anything you would not offer every similar customer.
   - **Floor:** the lowest renewal that is still worth keeping, with cost to serve.

7. **Plan the downsell honestly.** If the customer uses half the product, a
   right-sized renewal may be the best outcome. Define it before the customer
   asks, so it is a choice rather than a retreat.

8. **Write the let-go rule (DP-13).** The observable signal that ends the save
   effort — decider refuses to meet by date X, or requirement you cannot meet —
   and the clean exit: data export, transition, a door left open.

9. **State the verdict** by the rule below.

## Output Format

```
# Renewal — [Account] — ARR $[..] — renews [date] — notice [date] ([n] weeks)

## Contract mechanics (source: contract §[..])
## Renewal decider map
| Person | Role in renewal | Stance | Access | Evidence |

## Risk reasons
| Candidate reason | Evidence (who, date) | Rank | Fixable by notice date? |
Deciding reason: [..]

## Risk rating
Non-renewal/downsell probability: [band] — confidence [H/M/L]: [why]
ARR at risk: [full | $n partial | expansion only]

## Save sequence
| Step | Action | Owner | By | Success signal |

## Concession guardrails
Authority: [..]  Floor: $[..]  Each concession buys: [..]

## Downsell option
## Let-go rule
## Verdict
```

**Verdict rule:**
- **LIKELY RENEW** iff band is Low and the decider is a supporter with access.
- **AT RISK — SAVEABLE** iff band is Medium/High and the deciding reason is
  fixable before the notice date.
- **AT RISK — RIGHT-SIZE** iff the deciding reason is over-purchase or unused scope.
- **LIKELY LOSS** iff the deciding reason is not fixable before notice, or the
  let-go signal has fired.
- **INSUFFICIENT EVIDENCE** iff the decider is unknown or the contract mechanics
  are unverified — plus the single cheapest datum that unblocks it.
"It depends" is banned.

## Verification

- [ ] Notice date taken from the contract, with clause reference.
- [ ] The decider is named, or the verdict is INSUFFICIENT EVIDENCE.
- [ ] The deciding reason cites evidence and differs from the stated reason, or
      the output says why they match.
- [ ] Commercial steps come after access and value remediation.
- [ ] Every concession buys something and stays within authority and floor.
- [ ] The let-go rule is observable and dated.

## False-Positive Prevention

1. **The renewal date is not the deadline.** A 60-day notice clause means the
   decision is made two months earlier than the plan thinks.
2. **"Budget" is usually a proxy.** Budgets are found for things the decider
   values; treat budget as a stated reason until evidence shows otherwise.
3. **The original buyer is not necessarily the decider.** After a reorg or a
   sponsor exit, the person who signs the renewal may never have seen the product.
4. **A discount does not fix low value.** It delays the same conversation by a
   year at a lower price.
5. **Green usage can hide a lost sponsor.** Heavy use by frontline staff does not
   renew a contract that an executive no longer owns.
6. **A downsell is not a failure by default.** Forcing a full renewal on unused
   seats creates next year's churn.
7. **No fabricated leverage.** Do not invent competitor pricing, fake price rises,
   or "offer ends Friday" deadlines to pressure the renewal.
8. **Do not hedge the rating.** Give the band and the verdict; confidence is
   stated next to it, not instead of it.

## Example Output

```
# Renewal — Kestrel Clinics Group — ARR $120,000 — renews 2027-01-31 —
# notice 2026-12-01 (10 weeks)

## Contract mechanics (source: MSA §9.2, Order Form 2)
3-year term ending 2027-01-31; auto-renews 12 months unless notice ≥60 days;
uplift capped at 5%; no termination for convenience.

## Renewal decider map
| Person | Role | Stance | Access | Evidence |
| New CFO (joined 08-2026) | Signs renewal | Unknown | None | Procurement email 09-12: "all renewals >$50k to CFO review" |
| Dir. Operations (sponsor) | Recommends | Supporter | Direct | QBR 07-15 |
| Head of IT | Veto on tools | Neutral | Direct | — |

## Risk reasons
| Reason | Evidence | Rank | Fixable? |
| New CFO has no view of value | CFO review policy 09-12; CFO not in any meeting | 1 | Yes — exec meeting + value summary |
| Only 60 of 100 seats active | [our-data] telemetry, 90-day avg | 2 | Partly — right-size |
| "Consolidating vendors" | Dir. Ops, call 09-18 (second-hand from CFO) | 3 | Unknown |
Deciding reason: the CFO has no evidence of value and 40 idle seats to point at.

## Risk rating
Probability: Medium (20–50%) — confidence Low: we have never spoken to the CFO.
ARR at risk: full $120k; realistic downside $72k (60 seats).

## Save sequence
| Step | Action | Owner | By | Success signal |
| Access | Our CFO requests 30 min with their CFO via Dir. Ops | VP CS | 10-10 | Meeting booked |
| Value | 1-page outcomes vs goals, [their-data] only | CSM | 10-17 | Dir. Ops signs off |
| Proof | Walk CFO through outcomes | VP CS + Dir. Ops | 10-31 | CFO asks a follow-up |
| Commercial | Offer right-sized 70 seats + 2-yr term option | AE | 11-10 | Written response |

## Concession guardrails
Authority: up to 10% for a 2-year term. Floor: $70,000 ARR. The 2-year term buys
the 10%; right-sizing is priced at list per seat, not a concession.

## Downsell option
70 seats at list = $84,000; offered proactively once value is presented.

## Let-go rule
CFO declines to meet or delegates with no decision owner by 11-14 → prepare
transition plan and data export, keep Dir. Ops as a reference relationship.

## Verdict
AT RISK — SAVEABLE — Medium band; deciding reason (no CFO view of value) is
fixable before the 12-01 notice date. Right-size folded into the commercial step.
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — each risk reason tied to a dated signal.
- **DS-06 Prioritization Guidance** — access, value, proof, then commercial.
- **CM-02 Constraint Specification** — concession must/must-not and a floor.
- **DP-13 Kill Signal Definition** — a dated let-go rule with a clean exit.

## Related Prompts

- `domain-business-strategy/go-to-market/workflow_cs_account_health.md` — the
  health diagnosis this plan starts from.
- `domain-sales-customer/customer-success/cs_quarterly_business_review_prep.md` —
  where the value evidence for the "proof" step is built.
- `domain-agentic-resources/skills/marketing/churn-prevention/SKILL.md` — self-serve
  cancel flows, save offers and dunning, not covered here.

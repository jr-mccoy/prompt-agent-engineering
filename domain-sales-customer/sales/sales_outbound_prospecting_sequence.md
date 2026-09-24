---
title: "Outbound Prospecting Sequence — Account Tiers, Trigger Evidence, and a Multi-Channel Touch Plan (Strategy, Not Copy)"
category: sales-customer/sales
description: "Design the strategy layer of an outbound motion for a named account list: tier accounts by fit and a dated trigger, map the personas to reach in each, lay out a cross-channel touch cadence sized to the rep's real capacity, and define exit rules — then hand each touch's copy brief to the cold-email skill rather than writing the messages."
techniques:
  - DS-06
  - RT-05
  - OC-03
  - DP-13
difficulty: intermediate
tags:
  - sales
  - outbound
  - prospecting
  - account-based
  - cadence
  - sdr
  - find-new-customers
  - cold-outreach
  - fill-pipeline
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/sales/sales_deal_qualification_scorecard.md
  - domain-agentic-resources/skills/marketing/cold-email/SKILL.md
  - domain-agentic-resources/skills/marketing/sales-enablement/SKILL.md
---

# Outbound Prospecting Sequence

**Objective:** Turn a raw target list into a worked outbound plan — which accounts
get effort first and why now, whom to reach in each, which channel carries which
touch on which day, and when to stop — sized to the hours a rep actually has.

**When to Use:**
- You have a territory or an account list and no reason to call one account
  before another.
- Outbound "isn't working" and nobody can say whether the problem is the list,
  the timing, the persona, or the message.
- A new rep or SDR needs a plan for their first 30 days of prospecting.
- You are moving from spray-and-pray email to account-based outreach across
  phone, social, email and referral.
- **Not this prompt if** you need the emails themselves — subject lines, openers,
  body copy, follow-up wording and angle rotation belong to
  `domain-agentic-resources/skills/marketing/cold-email/`. Collateral and talk
  tracks belong to `skills/marketing/sales-enablement/`; lead scoring and
  marketing-to-sales routing to `skills/marketing/revops/`. This prompt produces
  the brief those skills execute against.

## Inputs / Context

1. **Offer in one line** and the problem it solves, in the buyer's terms.
2. **Ideal customer profile:** firmographics that predict fit, and the
   disqualifiers (too small, wrong stack, regulated out).
3. **Account list** (names, or the criteria to build one), with any known data.
4. **Personas** you have sold to before: title, what they own, what they get
   measured on.
5. **Channels available:** email, phone, LinkedIn, warm intros, events, partners
   — and any the rep is not allowed to use.
6. **Rep capacity:** hours per week for prospecting, measured, not hoped.
7. **What has been tried**, with results if known.

## Method

1. **Tier accounts on fit × timing (DS-06).**
   - **Fit** (0–2): matches the ICP on the criteria that predict closed-won, not
     on size alone.
   - **Trigger** (0–2): a dated, public event that makes the problem urgent now —
     new leader in the buying seat, funding, a regulatory deadline, an expansion,
     a job posting for the role your product replaces, a competitor's contract end.
   - Tier A = 4, Tier B = 3, Tier C = 2. Below 2 is not worked this cycle.

2. **Evidence every trigger (RT-05).** Each trigger carries a source and a date.
   A trigger older than 90 days is downgraded one point; one with no source is
   not a trigger, it is a guess, and scores 0.

3. **Map personas per Tier A account.** Name 2–3 roles: the one who feels the
   problem, the one who owns the budget, and, where useful, the one who would
   implement. Say which one is the *entry point* and why — usually the problem
   owner, not the most senior title.

4. **Build the touch plan (OC-03).** One table per tier: day, channel, persona,
   *purpose of the touch* (open, add evidence, ask, referral ask, close the loop),
   and the copy brief reference. Rules:
   - Channels alternate; no two consecutive email-only days.
   - Tier A: 8–12 touches over 3–4 weeks, multi-persona. Tier B: 5–7 over 3 weeks.
     Tier C: 3–4, mostly automated, single persona.
   - Every touch has a job different from the one before it. "Following up" is
     not a job.

5. **Size to capacity.** Estimate minutes per touch by channel (research-heavy
   first touches cost more). Multiply out. If the plan exceeds stated hours,
   cut Tier C first, then shorten Tier B — never thin Tier A research.

6. **Write the copy briefs, not the copy.** For each distinct touch purpose, a
   brief: persona, trigger to reference, the one point to make, the ask, and
   forbidden claims. These go to the cold-email skill (email) or the rep (phone,
   social).

7. **Define exit and recycle rules (DP-13).**
   - **Positive exit:** reply with interest → meeting request → hand to discovery.
   - **Hard exit:** explicit no, unsubscribe, or wrong-person reply → stop, log,
     and honour any opt-out on every channel.
   - **Recycle:** no response after the sequence → re-enter only when a *new*
     trigger appears, not on a calendar.

8. **Name the measurement.** Per tier: reply rate, positive-reply rate, meetings
   held. Decide in advance which number would make you change the list rather
   than the message.

## Output Format

```
# Outbound plan — [territory / segment] — [cycle dates]

## Account tiers
| Account | Fit 0–2 | Trigger (source, date) | Trigger 0–2 | Tier | Entry persona |
|---|---|---|---|---|---|

## Persona map (Tier A)
| Account | Problem owner | Budget owner | Implementer | Entry point + why |

## Touch plan — Tier [A|B|C]
| Day | Channel | Persona | Purpose | Brief ref |

## Capacity check
| Tier | Accounts | Touches each | Min/touch | Hours |
Total [n] h vs [n] h available → [fits | cut: …]

## Copy briefs (hand to cold-email skill / rep)
Brief [ref]: persona · trigger · one point · ask · must not claim

## Exit and recycle rules
## Measurement and the decision it drives
```

## Verification

- [ ] Every trigger has a source and a date; none older than 90 days scores 2.
- [ ] Every Tier A account names an entry persona with a reason.
- [ ] No touch's purpose is "follow up" or "check in."
- [ ] Capacity hours recomputed from the table and within stated availability.
- [ ] Opt-out on any channel stops all channels.
- [ ] No message copy written — only briefs.

## False-Positive Prevention

1. **Company size is not fit.** A list sorted by headcount looks tiered and is
   not; fit comes from the attributes your closed-won deals share.
2. **A funding round is not a trigger for every product.** It is a trigger only
   if the money plausibly lands on your problem; otherwise it is noise with a date.
3. **More touches is not more coverage.** Twelve emails to one persona is one
   channel, one person, and a spam complaint — the plan fails the alternation rule.
4. **Seniority is not the entry point.** Opening at the CEO because the title is
   senior usually earns a forward to the person you should have started with.
5. **A plan that exceeds capacity is a wish.** If the hours do not fit, the
   plan silently degrades into Tier A getting Tier C treatment.
6. **Recycling on a calendar retrains the same "no."** Re-enter only on a new trigger.
7. **Do not write the copy here.** The moment this prompt drafts emails it
   duplicates the cold-email skill and loses the strategy-level view.
8. **No fabricated personalization.** Triggers and persona facts come from
   sources; never invent a quote, a post, or a mutual connection.

## Example Output

```
# Outbound plan — Mid-market 3PLs, Pacific NW — 2026-10-01 to 10-31

## Account tiers
| Account | Fit | Trigger (source, date) | Trig | Tier | Entry persona |
|---|---|---|---|---|---|
| Cascade Cold Chain | 2 | New VP Operations hired (press release, 2026-09-08) | 2 | A | VP Ops — new leaders audit tooling in first 90 days |
| Tidewater 3PL | 2 | Posting for "fleet data analyst" (careers page, 2026-09-15) | 2 | A | Dir. Fleet — role we replace |
| Ridgeline Haulage | 2 | Expansion to 2nd DC (local news, 2026-05-02; 145 days) | 1 | B | Ops Manager |
| Beacon Movers | 1 | none found | 0 | — | not worked |

## Persona map (Tier A)
| Account | Problem owner | Budget owner | Implementer | Entry |
| Cascade | VP Ops | CFO | IT lead | VP Ops: owns the problem and is new |
| Tidewater | Dir. Fleet | COO | Fleet analyst (once hired) | Dir. Fleet |

## Touch plan — Tier A (per account, 10 touches / 20 days)
| Day | Channel | Persona | Purpose | Brief |
| 1 | LinkedIn view + connect | Entry | Open, no pitch | — |
| 2 | Email | Entry | Open on trigger | A1 |
| 4 | Phone | Entry | Ask for 15 min | A2 |
| 7 | Email | Budget owner | Add evidence (peer outcome) | A3 |
| 9 | LinkedIn message | Entry | Share relevant resource | A4 |
| 12 | Phone | Entry | Ask again, offer alternate time | A2 |
| 14 | Warm intro ask | Existing customer contact | Referral | A5 |
| 16 | Email | Implementer | Add evidence (integration) | A6 |
| 18 | Phone | Budget owner | Ask | A2 |
| 20 | Email | Entry | Close the loop | A7 |

## Capacity check
| Tier | Accts | Touches | Min/touch | Hours |
| A | 2 | 10 | 12 | 4.0 |
| B | 1 | 6 | 6 | 0.6 |
Total 4.6 h vs 6 h available → fits; 1.4 h to add Tier B accounts.

## Copy briefs
A1: VP Ops, Cascade · trigger: new role (09-08) · point: new ops leaders inherit
fuel variance they did not create · ask: 15-min call · must not claim: any
specific saving for Cascade.

## Exit and recycle rules
Positive reply → discovery (sales_deal_qualification_scorecard after call 1).
"Not me" → ask for the right person once, then stop. Opt-out → suppress on all
channels same day. No response → recycle only on a new trigger.

## Measurement
Positive-reply rate <3% across both Tier A accounts after 20 days → revisit the
list and triggers before the copy.
```

## Techniques Used

- **DS-06 Prioritization Guidance** — fit × trigger tiering decides where effort goes.
- **RT-05 Evidence-Based Reasoning** — every trigger has a source and a date.
- **OC-03 Markdown Table Specification** — tier, persona and touch tables.
- **DP-13 Kill Signal Definition** — exit, recycle, and change-the-list thresholds.

## Related Prompts

- `domain-agentic-resources/skills/marketing/cold-email/SKILL.md` — writes the
  email copy from the briefs this prompt produces.
- `domain-agentic-resources/skills/marketing/sales-enablement/SKILL.md` —
  collateral and talk tracks referenced in "add evidence" touches.
- `domain-sales-customer/sales/sales_deal_qualification_scorecard.md` — what
  happens to a positive reply after the first call.

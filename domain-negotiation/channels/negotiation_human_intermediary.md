---
title: "When a Broker, Recruiter, or Agent Negotiates for You — Incentive Misalignment, What to Tell Them, and How to Instruct and Audit Them"
category: negotiation/channels
description: "Negotiate by way of a person who represents you — a listing or buyer's agent, a business or insurance broker, an agency recruiter, a talent or sports agent. Map how they are paid and who else pays or relies on them, compute what the next increment of price is worth to them versus you, decide what they need to know and what you keep back, write an instruction brief with authority limits and reporting rules, and audit their effort and advice while keeping the relationship. Counters the most common intermediary failure: treating your representative's advice to accept as neutral expertise, when their pay rewards closing fast more than closing well."
techniques:
  - CM-09
  - NE-11
  - NE-20
  - GT-11
  - RT-02
difficulty: advanced
tags:
  - negotiation
  - intermediary
  - principal-agent
  - broker
  - recruiter
  - agent-incentives
  - commission-conflict
  - my-agent-wants-me-to-accept
  - realtor-advice
  - recruiter-negotiating-for-me
  - working-with-a-broker
updated: "2026-10-08"
reasoning:
  styles: [strategic, quantitative, adversarial, systems]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: structured
  user_role: [individual, executive, founder]
  mode: [plan, audit]
related_prompts:
  - domain-negotiation/channels/negotiation_ai_agent_mediated.md
  - domain-negotiation/at-the-table/negotiation_authority_mandate_limits.md
  - domain-negotiation/preparation/negotiation_information_plan.md
---

# When a Broker, Recruiter, or Agent Negotiates for You

**Objective:** Many of the negotiations people care most about are not conducted by them. A listing agent sells the house, a buyer's agent writes the offer, a broker places the insurance or sells the business, an agency recruiter carries the offer back and forth, a talent agent negotiates the contract. The intermediary usually adds real value — market knowledge, access, emotional distance, a buffer that makes hard asks easier. But they are paid differently from you, they have relationships you do not, and you cannot watch most of what they do. Their advice to "take it" may be the best advice available, or it may be the advice that suits a commission, a fee paid by the other side, or a relationship with the counterpart they will see again next month. This prompt makes that structure visible and workable: it maps the incentives, computes what the next concession is worth to them and to you, decides what you tell them, writes the instructions they work from, and sets up an audit you can run without accusing anyone of anything.

**When to use:**
- You are about to hire or sign with a broker, agent, or recruiter and can still shape how they are paid and what they may do.
- Your representative is urging you to accept, lower, or raise something, and you want to know how much of that advice their incentives explain.
- An agency recruiter is between you and an employer and keeps asking for your numbers.
- You suspect offers, feedback, or counter-arguments are reaching you filtered, late, or not at all.
- The deal is done and you want to check whether your intermediary represented you well before you use them again.

**When NOT to use:**
- The intermediary is software — an AI assistant or a counterpart's chatbot. That is `channels/negotiation_ai_agent_mediated.md`; the problem there is instructions and disclosure, not pay.
- The person across the table must get approval from someone else — `at-the-table/negotiation_authority_mandate_limits.md`.
- You are designing the house offer package itself (contingencies, escalation, appraisal gap) — `domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md`; this prompt governs the agent who carries it.
- A neutral is running the process for both sides — `multi-party/negotiation_facilitator_third_party.md`, or `domain-legal/` for formal mediation.
- You need to know what duties your intermediary legally owes you, or whether a fee or dual role is lawful where you are — `domain-legal/`, or the regulator that licenses them. This prompt asks the question; it does not answer it.
- Coordinating your own colleagues at the table — `multi-party/negotiation_team_negotiation_roles.md`.

**Audience:** Individuals and executives who are represented in a sale, purchase, hire, placement, or contract by someone paid to negotiate for them.

---

## Inputs / Context

1. **The negotiation:** what is being sold, bought, placed, or signed; with whom; by when; the issues in play (price, terms, timing, contingencies, start date, exclusivity).
2. **The intermediary:** their role (listing agent, buyer's agent, broker, agency recruiter, in-house recruiter, talent agent), who engaged them, and the engagement document if there is one.
3. **How they are paid:** percentage, flat fee, retainer, hourly, contingency, split with others; **who pays** (you, the counterpart, both); any bonus, referral fee, or preferred-vendor arrangement you know of. Mark each item known / inferred / guessed.
4. **Their other relationships:** do they represent the other side too, other clients competing for the same thing, or deal with this counterpart repeatedly?
5. **Your numbers:** opening, target, reservation point (walk-away), BATNA — each tagged known / inferred / guessed.
6. **What has happened so far:** offers relayed, advice given, timeline, anything that felt filtered.

---

## Constraints

### Must
- Map **every source of the intermediary's pay and every party they rely on** before judging their advice. Who pays them is the first fact, not a detail.
- Compute the **marginal split** from the user's own figures: what the next increment of price, or the next week of waiting, is worth to the intermediary versus to the user. Never assume a commission rate, fee, or market norm; use the user's documents or leave a `[VERIFY: engagement terms]` slot.
- Decide disclosure **per item**: what the intermediary must know to negotiate well, and what could cost the user if it reached the counterpart. Where they owe duties to the other side or represent both, assume anything told to them can travel.
- Give the walk-away as a **decision rule** ("bring me anything above X; do not counter below Y without calling me"), not as a figure to quote.
- Write the instructions down: objective, ranked issues and acceptable trades, authority limits, and reporting rules — **every offer relayed in writing, including verbal and rejected ones, in the counterpart's own words**.
- Ask the intermediary to **disclose conflicts** in writing: other interested clients, payment from the other side, referral fees, dual representation.
- Separate **advice from information**. "The market is softening" is a claim to source; "the buyer's agent said they're at their limit" is a report to keep verbatim.
- Steelman the intermediary: misaligned pay is not dishonesty, most protect a reputation they depend on, and their recommendation may be right even when it suits them.
- Route questions about legal duties, licensing, and whether a fee arrangement is permitted to `domain-legal/` or the licensing body; rules on agent pay and disclosure differ by jurisdiction and have changed recently in some markets `[VERIFY: current local rules]`.

### Must Not
- Treat a recommendation to accept as neutral market evidence.
- State a typical commission, recruiter fee, or "standard" split from memory as a fact.
- Go around your intermediary to the counterpart in a way the engagement forbids; it can breach the agreement and forfeit the protection they provide. Raise the concern with them, or end the engagement properly.
- Accuse, or imply bad faith, on the strength of the incentive map alone. The map tells you where to look, not what you will find.
- Tell an intermediary who acts for both sides, or who is paid by the counterpart, anything you would not tell the counterpart.
- Fabricate a competing offer or a deadline for the intermediary to carry; it becomes their misrepresentation and your liability.

---

## Instructions

### Step 1 — Classify the relationship
Name the role and the direction of duty: does the intermediary act **for you**, **for the counterpart** (an in-house recruiter, a seller's agent you are buying through), **for both**, or for **whoever closes** (many agency recruiters are engaged and paid by the employer)? Write one sentence: "This person is paid by ___ and owes duties to ___ `[VERIFY: engagement document / local rules]`." Everything after depends on it.

### Step 2 — Map the incentives
Build the table: each source of pay and how it is triggered (on closing, on price, on time spent, on volume); each relationship that outlasts this deal (the counterpart, other agents, an employer client, a carrier or lender); and what the intermediary risks if the deal fails. Then name the likely tilts, for example:
- **Paid a percentage on closing:** strong pull toward closing, weak pull toward the last increment of price.
- **Paid by the counterpart, or engaged by them:** pull toward the counterpart's terms and toward learning your limits.
- **Repeat relationship with the counterpart:** pull toward a smooth deal over a hard one.
- **Flat fee or hourly:** little price pull; watch effort and duration instead.
- **Several clients after the same thing:** your deal competes with theirs for attention or placement.
Mark each tilt as structural (follows from the pay) or observed (seen in behaviour).

### Step 3 — Compute the marginal split (NE-11)
From the user's figures only. For a seller paying a percentage fee, an extra increment ΔP nets the user ΔP × (1 − fee rate) and earns the individual intermediary ΔP × fee rate × their share of the fee (after any split with a brokerage or the other side's agent). For a buyer whose agent is paid on price, the signs part: a higher price costs the user ΔP and still raises the agent's fee. For a recruiter whose fee scales with the package `[VERIFY: their terms]`, compare that fee change with the risk, to them, of the placement falling through. Do the same for time: the intermediary's cost of another week of marketing, calls, or interviews, against the user's gain if waiting raises the price or improves the terms. Present it as one line: "Holding out for another [ΔP] is worth about [x] to you and [y] to them; another [n] weeks costs them [effort] and you [carrying cost]." If the figures are unknown, show the formula with `[VERIFY]` slots instead of numbers.

### Step 4 — Decide what you tell them
List each item — reservation point, BATNA, deadline, other options, motivation, budget, current pay or price paid — and mark it **tell / tell as a rule / keep**:
- **Tell:** what they need to negotiate well — priorities, non-negotiables, timing windows, which trades you would accept.
- **Tell as a rule:** the walk-away, as an instruction, not a number they can repeat.
- **Keep:** anything that would weaken you if it reached the other side, and everything when they act for both sides or are paid by the counterpart.
For recruiters, decide in advance how you will answer "what are you looking for?" with a range anchored on the role, not on your current pay, unless you have chosen to disclose it.

### Step 5 — Fix the incentive where you can, before signing
If you are still choosing or engaging the intermediary, list the levers to raise with them: a fee that rises above a target, a cap or flat fee, a shorter exclusivity period, the right to end the engagement, a written statement of who pays them and of any dual role, and named reporting duties. Ask; do not assume the first terms are the only terms. Mark which are negotiable in the user's market `[VERIFY: locally]`.

### Step 6 — Write the instruction brief (CM-09, NE-20)
A one-page brief the intermediary could act on without asking: objective in one sentence; issues ranked with acceptable trades; opening and target; the walk-away as a rule; **authority limits** — what they may do alone (gather information, relay, recommend), what needs the user's sign-off (any counter, any change to non-price terms, any disclosure beyond the brief), and what they must never do (accept, sign, waive a contingency, disclose a "keep" item); **reporting rules** — every offer and every piece of counterpart feedback in writing within an agreed time, verbatim where possible, rejected ones included; and a conflict-disclosure request.

### Step 7 — Set up the audit (GT-11)
Plan how to check the work without insult:
- **Raw over summary:** ask for the actual offers, emails, and term sheets, not only their description.
- **Activity evidence:** what they did, by when — showings, calls, submissions, candidates or buyers contacted — compared with what was promised.
- **Sourced claims:** market statements come with their comparables or data and where they came from.
- **Prediction log:** write down what they say will happen if you hold ("expect a counter within a week") and compare with what happens.
- **Independent check:** one outside data point per important claim — a second opinion, a public listing, posted pay ranges, a call with another broker.
- **Pressure signals:** urging you to decide faster than the counterpart's own deadline, re-describing your walk-away, "this is the best you'll get" with no evidence. Each is a prompt to ask for the evidence, not proof of bad faith.

### Step 8 — Respond to a push to accept
When the intermediary recommends accepting (or cutting, or raising), restate their recommendation, list the evidence they gave, place it beside the Step 3 split, and ask the three questions: "What do you expect happens if I hold for [time]?", "What did they say, in their words?", "If the fee were flat, would your advice change?" Decide on the evidence, not on the confidence of the advice.

### Step 9 — Adversarial check
- If the counterpart could read what you told your intermediary, what would they do with it?
- Which of their recommendations would you follow even if their pay pointed the other way — and which only because of their confidence?
- What would you be unable to verify if they were simply mistaken?

---

## False-Positive Prevention

1. **Incentive as proof.** A commission that rewards closing does not show this agent is steering you. The map tells you where to look; the audit tells you what is there.
2. **Invented market norms.** "Agents usually take X%" or "recruiters charge Y" from memory is not an input. Use the engagement document or leave a `[VERIFY]` slot; a wrong norm makes the Step 3 split wrong.
3. **Advice laundered as data.** "Buyers won't go higher in this market" repeated by the user becomes a premise unless it is traced to comparables or a counterpart statement.
4. **Who they work for, assumed.** Many people assume a recruiter, a seller's agent, or a broker works for them when the engagement or the fee says otherwise. Step 1 must cite the document or mark `[VERIFY]`.
5. **Over-disclosure through trust.** Rapport with a good intermediary leads people to tell them the walk-away as a number. Check Step 4 against the duty direction, not against how helpful they have been.
6. **Paranoid audit.** Demanding proof of every phone call from a capable intermediary on a low-stakes deal damages the relationship that produces the outcome. Scale the audit to the Step 3 split and the stakes.
7. **Holding out by reflex.** The intermediary's push to accept may be right: carrying costs, a softening market, or a counterpart near its limit. Recompute the user's own side of the split before overriding them.
8. **Going around them.** Contacting the counterpart directly to "check" can breach the engagement. The fix for distrust is the written reporting rule or ending the engagement properly.

---

## Output Format

```
# Intermediary plan — [deal], through [role]

## Relationship
Paid by: [..]  Owes duties to: [..]  [VERIFY: engagement document / local rules]
Also represents / deals repeatedly with: [..]

## Incentive map
| Source of pay or reliance | Triggered by | Tilt | Structural / observed | Known / inferred / guessed |

## Marginal split
Next [ΔP]: worth [x] to you, [y] to them.  Next [n] weeks: costs you [..], costs them [..].
Reading: [where their advice is most likely to diverge from your interest]

## Disclosure
| Item | Tell / tell as a rule / keep | Why |
Recruiter or "what are you looking for?" answer: "[..]"

## Engagement levers (if not yet signed)
| Lever | Ask | Negotiable here? [VERIFY] |

## Instruction brief
Objective: [..]
Issues ranked, with acceptable trades: [..]
Opening: [..]  Target: [..]  Walk-away rule: "[..]"
May do alone: [..]  Needs my sign-off: [..]  Never: [..]
Reporting: every offer in writing within [time], verbatim, including rejected ones.
Conflict disclosure requested: [..]

## Audit plan
Raw documents requested: [..]
Activity evidence: [..]
Claims needing a source: [..]
Prediction log: | Date | They said would happen | What happened |
Independent checks: [..]
Pressure signals to watch: [..]

## Push-to-accept response (if applicable)
Their recommendation: [..]  Evidence given: [..]  Against the split: [..]
Questions asked: [..]  Decision and reason: [..]

## Adversarial check
- If the counterpart read my disclosures: [..]
- Advice I'd follow regardless of their pay: [..]
- What I could not verify if they were simply wrong: [..]
```

---

## Verification

- [ ] The relationship sentence names who pays the intermediary and to whom they owe duties, cited or marked `[VERIFY]`.
- [ ] Every source of pay and every lasting relationship is in the incentive map, tagged structural or observed.
- [ ] The marginal split uses only the user's figures or shows `[VERIFY]` slots; no commission rate or fee comes from memory.
- [ ] Every disclosure item is marked tell / tell as a rule / keep, and nothing is told to a dual or counterpart-paid intermediary that the counterpart should not know.
- [ ] The walk-away appears as a rule, never as a quotable number.
- [ ] The instruction brief has authority limits in three tiers and a written, verbatim reporting rule.
- [ ] The audit plan asks for raw documents and at least one independent check per important claim.
- [ ] No bad faith is asserted on the incentive map alone; every pressure signal leads to a question.
- [ ] Legal-duty and fee-legality questions are routed to `domain-legal/` or the licensing body.
- [ ] No fabricated offer, deadline, or competing interest is given to the intermediary to carry.

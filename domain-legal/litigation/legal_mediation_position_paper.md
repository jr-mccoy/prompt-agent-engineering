---
title: "Civil Mediation Position Paper"
category: legal/litigation
description: "Draft a mediation submission for a civil (non-family) case — an exchanged statement that persuades the mediator and opposing decision-maker plus a confidential mediator-only letter with leverage, settlement bands, a litigation decision tree, and obstacles to closing — distinct from the internal settlement-value analysis it draws on and from the divorce and custody mediation briefs."
techniques:
  - NE-10
  - RT-03
  - RP-02
  - NE-23
difficulty: advanced
tags:
  - legal
  - litigation
  - mediation
  - settlement
  - mediation-statement
  - preparing-for-mediation
  - what-to-send-the-mediator
updated: "2026-09-24"
related_prompts:
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-negotiation/at-the-table/negotiation_impasse_breaker.md
---

# Civil Mediation Position Paper

**Objective:** Produce two documents with two different jobs. The **exchanged statement** is written for the opposing party's decision-maker (often an adjuster or in-house lawyer who has not read the file) and moves them toward your number with facts, risk, and cost. The **confidential mediator letter** gives the mediator what they need to move both sides: your real interests, settlement bands, the litigation decision tree, and the obstacles that will stop a deal on the day unless solved in advance.

> **Scope guard — attorney-facing.** For counsel representing a party in a civil mediation (court-ordered or private). Family-law mediation has its own prompts. A self-represented party preparing for mediation should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- A commercial, tort, employment, IP, or insurance-coverage case is set for mediation and a written submission is required or useful.
- A prior mediation failed and a second session is set; the submission must address what changed.
- The mediator has asked for a confidential letter in addition to an exchanged brief.

**Not this prompt if:**
- You need to compute the settlement range itself — run `domain-legal/litigation/legal_settlement_value_range_analysis.md` first and feed its output here.
- The matter is a divorce or custody case — use `domain-legal/divorce/legal_divorce_mediation_brief_drafter.md` or `domain-legal/custody/legal_custody_mediation_brief_drafter.md`.
- You are negotiating a commercial contract, not resolving a dispute — use `domain-legal/contracts-transactional/legal_negotiation_position_paper.md`.

## Inputs

- **Jurisdiction and forum (required):** Court and case number, governing law, and the mediation confidentiality rule that applies (court rule, statute, or mediation agreement) `[VERIFY]`. Any court order specifying submission content, length, or deadline.
- **Case posture:** Claims, defenses, procedural stage, pending motions, trial date, remaining discovery.
- **Liability and damages evidence:** Key documents, testimony, expert opinions; the weakest points on both sides.
- **Valuation:** Output of the settlement-value analysis or the client's own probability and damages estimates, labeled as estimates.
- **Costs to trial:** Budget for remaining phases (both sides if known).
- **Settlement history:** Demands, offers, dates, and any prior mediation.
- **Client interests beyond money:** Timing, confidentiality, precedent, reputation, business relationship, non-monetary relief.
- **Obstacles:** Insurance coverage disputes, multiple defendants with allocation fights, liens, authority limits, approval requirements.

## Method

**Ground rules:** No invented case names, verdicts, or verdict statistics — authority is supplied or `[CITE: …]`; comparable verdicts are `[NEED: source]`. Probabilities are the user's or the valuation prompt's estimates and are labeled as such; never present them as data. Nothing marked for the mediator only may appear in the exchanged statement.

1. **Identify the reader of each document.** Exchanged statement: the opposing decision-maker and the mediator. Confidential letter: the mediator only. Write the exchanged statement so it would persuade someone reading only the first two pages.
2. **Build the decision tree.** Map the litigation path from today: pending motion → outcomes → trial liability → damages bands → appeal risk, with the estimated probability and cost at each node. Compute expected value and the range of outcomes for *both* sides (the other side's tree uses their likely view of the risks — state your assumptions).
3. **Set settlement bands.** Opening, target, and walk-away (or authority limit) from the valuation input; explain the movement plan (how many moves, what triggers each). These go only in the confidential letter.
4. **Draft the exchanged statement.** Posture in one paragraph → the three facts the other side must confront → liability analysis that acknowledges your weak point and answers it → damages with the calculation shown → cost and time to trial → a closing that makes settlement the rational choice. Tone is firm and factual; this reader will influence their client's authority.
5. **Pre-empt the other side's best arguments.** For the two or three strongest defenses (or claims) against you, state them fairly and respond — decision-makers discount statements that ignore obvious problems.
6. **Draft the confidential letter.** Real interests; bands and movement plan; the decision-tree summary; what your client can offer that costs little (timing, non-monetary terms); obstacles and how you propose to solve them before the session; what you need from the mediator (e.g., reality-testing the adjuster on a specific risk).
7. **Settlement history and what changed.** Chronology of demands and offers; for a second mediation, the new facts or rulings that justify movement.
8. **Closing documents.** Attach or reference a draft term sheet so a deal on the day can be signed on the day.

## Output Format

```markdown
# Mediation Package — {Caption} — Session {date}

## A. EXCHANGED MEDIATION STATEMENT
1. Introduction and Posture
2. Key Facts (the three the other side must confront)
3. Liability (including our weakest point, addressed)
4. Damages — calculation shown
5. Cost, Time, and Risk of Continued Litigation
6. Settlement History
7. Conclusion
(All authority [CITE] unless supplied; confidentiality legend per [VERIFY rule])

## B. CONFIDENTIAL LETTER TO MEDIATOR — NOT FOR EXCHANGE
1. Client Interests (monetary and non-monetary)
2. Settlement Bands and Movement Plan — opening / target / walk-away
3. Decision Tree Summary
| Node | Outcome | Est. probability (labeled estimate) | Cost to reach | Value |
4. The Other Side's Likely View and Where It Is Wrong
5. Obstacles to Closing and Proposed Solutions
6. What We Need from the Mediator

## C. Draft Term Sheet (for signature on the day)
## D. Verification Items
```

## Verification

- [ ] Jurisdiction lock: confidentiality rule and any court submission requirements tied to the stated forum, `[VERIFY]` unless supplied.
- [ ] Citation discipline: no invented authority, verdicts, or statistics.
- [ ] Scope discipline: exchanged statement contains nothing from the confidential letter (bands, walk-away, candid weaknesses beyond what is addressed).
- [ ] Every probability is labeled as an estimate with its source.
- [ ] Decision tree covers both sides' paths and includes cost to reach each node.
- [ ] The strongest opposing arguments are stated fairly and answered.
- [ ] Obstacles to closing (coverage, liens, approvals, authority) each have a proposed solution.
- [ ] A draft term sheet is attached.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Exchanged statement reads like a summary-judgment brief | Write for a decision-maker weighing risk and cost, not a judge |
| Walk-away number leaks into the exchanged statement | Hard separation; confidential letter carries all bands |
| Probabilities presented as fact or with false precision | Label estimates and give ranges |
| Ignoring the other side's view of the risk | Build their tree and address where it diverges |
| No plan for non-monetary terms or obstacles | Confidential letter lists them with proposed fixes |
| No paper ready if the case settles | Attach a draft term sheet |

## Example

**Input sketch:** Federal breach-of-contract case; plaintiff Halden Robotics (fictional) claims $2.4M in lost profits from defendant Norrow Manufacturing's late delivery of components. Defendant's summary-judgment motion on the consequential-damages waiver is pending. Client estimates: 55% chance the waiver is held unenforceable; if so, 70% liability, damages $1.2M–$2.4M. Cost to trial: ~$450K per side. Last demand $2.1M; last offer $250K.

**Output (abridged):**

> **Exchanged statement, § 3 (excerpt).** Norrow's defense rests on the consequential-damages waiver in § 11.4. Halden does not ignore that clause; it addresses it. The waiver does not apply where the non-delivery was willful `[CITE: governing-law authority on willful-breach exception]`, and Norrow's own production shows it reallocated Halden's components to a higher-margin customer (NRW-00872).
>
> **Confidential letter, § 3 (decision tree summary).** Estimates are client's. Waiver survives (45%) → recovery limited to direct damages `[NEED: amount]`. Waiver fails (55%) × liability (70%) × damages midpoint $1.8M ≈ $693K expected, before fees and appeal risk. Norrow likely weights the waiver at 70%+; the mediator can test that with Norrow's counsel.
>
> **§ 2 Bands.** Opening move: $1.75M. Target: $900K–$1.1M. Walk-away: per client authority `[NEED: client authority]`.
>
> **§ 5 Obstacles.** Norrow's insurer has reserved rights on the willfulness allegation — propose a structure in which Norrow funds the portion above the insurer's contribution.

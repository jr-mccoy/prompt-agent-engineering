---
title: "Audit a Decision for Opportunity Cost and Sunk-Cost Distortion"
category: decision-making/cost-reasoning
description: "For a decision the user is leaning toward, surface the invisible alternative — the best forgone use of the same forward resources — and separately detect sunk-cost reasoning distorting the lean. Sorts past investment into sunk (zero weight) vs. salvage (real forward value), runs a zero-based test and a best-alternative comparison, and delivers a two-axis verdict with confidence and flip conditions."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - QA-20
difficulty: beginner
tags:
  - opportunity-cost
  - sunk-cost
  - decision-audit
  - escalation-of-commitment
  - zero-based
  - bias
updated: "2026-07-08"
related_prompts:
  - domain-decision-making/decisioning_regret_minimization.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/decisioning_prioritization_framework_selector.md
---

# Audit a Decision for Opportunity Cost and Sunk-Cost Distortion

**Objective:** For a decision the user is leaning toward, make the invisible alternative visible — the best forgone use of the same forward resources — and separately detect whether sunk-cost reasoning is distorting the lean, delivering a two-axis verdict (which way the forward case points; whether the stated reasoning is distorted), each with confidence and the conditions that would flip it.

Two distortions hide in "should we keep going?" decisions, and they pull in opposite directions. The famous one: past unrecoverable investment used as a reason to continue ("we've come too far to stop"). The less famous one — this prompt guards it just as hard: over-correcting by treating *all* past investment as irrelevant, when some of it created still-usable assets that legitimately change the forward math. The audit's core move is sorting the past into **sunk** (gone; zero decision weight) and **salvage** (usable; enters the forward comparison).

## When to Use

- Use when: you're leaning toward continuing, renewing, or doubling down on something with significant past investment — a project, vendor, codebase, degree, campaign, or role.
- Use when: you catch yourself or your team saying "we've already invested so much," "stopping now wastes it," or "we're too far in" — or the budget/timeline has already been extended after misses.
- Use when: you're about to commit resources to option A and nobody has named what A displaces.
- Don't use when: there's no meaningful past investment *and* the alternatives are already explicit — that's a straight comparison; use `tradeoff_multi_criteria_decision_analysis.md`.
- Don't use when: you're ranking many competing items rather than auditing one lean — use `decisioning_prioritization_framework_selector.md`.

**Audience:** Founders, managers, engineers, and individuals making personal calls (career, education, renovations). No decision-theory background assumed.

## Inputs / Context

1. **The decision and the lean (required).** Wrapped in `<decision>…</decision>`: what's being decided, which way you're leaning, and your reasons **verbatim** — the audit inspects the actual wording for distortion patterns, so don't clean it up.
2. **Past investment (required).** Wrapped in `<invested>…</invested>`: what's been spent so far — money, time, people, reputation, emotional energy — roughly quantified per item.
3. **Forward view (required, best-effort).** Wrapped in `<forward>…</forward>`: cost and time to continue/finish, expected payoff, and — if known — what else the same resources could do. If no alternative is named, the audit constructs candidates from context and says so.
4. **Constraints (optional).** Contracts, penalties, deadlines, non-transferable resources. These become quantified switching costs, not vetoes.

## Core Distinctions (the audit's lens)

| Concept | Definition | Decision weight |
|---|---|---|
| **Sunk cost** | Spend you cannot recover no matter what you choose | **Zero.** Never a reason to continue |
| **Salvage value** | Still-usable assets the past spend created — built components, data, learning, relationships, options, completed milestones | **Real.** Enters the forward math (usually as reduced cost-to-complete, or as an asset both branches can use) |
| **Opportunity cost** | The best alternative use of the *forward* resources | **The true price of continuing.** Compare against it — not against "doing nothing" |
| **Switching cost** | Real forward cost of stopping or changing: wind-down, penalties, ramp-up elsewhere, morale | **Real, on the continue side's favor** — but must be quantified, not assumed |

**The two named tests:**
1. **Zero-based test:** *"If you arrived today with no history — same information, same remaining costs, same expected payoff, same salvaged assets — would you START this?"*
2. **Best-alternative test:** *"Name the single best thing the same forward resources could do instead. Is continuing better than THAT?"*

## Constraints

### Must
- Restate the decision in forward-looking terms (remaining cost, expected payoff, timeline) **before** any judgment.
- Sort every past-investment item into SUNK or SALVAGE with a stated reason; salvage must reappear in the forward comparison, sunk must not.
- Quote the user's stated reasons **verbatim** when flagging distortion; name the pattern; attach a confidence level. No flag without a quote.
- Compare continuing against one named, costed best alternative — the alternative carries its own costs, ramp-up, and risk.
- Run both named tests and an adversarial pass on the preliminary conclusion before delivering the verdict.
- Deliver the two-axis verdict plus a corrected decision statement. **"No distortion detected — the lean stands" is a fully legitimate outcome**; do not manufacture a fallacy to justify the audit.

### Must Not
- Treat all past investment as irrelevant. Salvage value and already-paid switching costs are real forward inputs; zeroing them is the mirror-image error of the sunk-cost fallacy.
- Flag the mere *mention* of history as fallacious — only past investment used as *justification to continue* counts.
- Invent numbers. Unknown quantities get labeled ranges, and the verdict states its sensitivity to them.
- Compare a fully-costed "continue" against a frictionless fantasy alternative.
- Lecture about cognitive biases. Diagnose, quantify, correct — no moralizing about human irrationality.

## Instructions

1. **Restate the decision forward-looking.**
   - Strip history from the framing: remaining cost to continue, expected payoff, timeline, and the same for stopping/switching.
   - Record the lean and the user's stated reasons verbatim, labeled (a), (b), (c)… for later reference.

2. **Sort the past investment.** For each item in `<invested>`, analyze four dimensions: amount; recoverable? (refundable, sellable, redeployable as-is); salvage created (what still-usable asset exists, and which branch(es) can use it); classification — **SUNK** or **SALVAGE**. Present as a table. Note explicitly when a salvage asset helps *both* branches (common: data, learning, relationships) — such assets are not arguments for continuing.

3. **Detect sunk-cost reasoning in the stated lean.**
   - Scan reasons (a), (b), (c)… for the patterns: unrecoverable-spend-as-justification ("already invested," "waste it"), completion anchoring ("80% done" amid slipping estimates), escalation history (budget/timeline extended after misses), identity/audience commitment ("we announced it").
   - For each flag: the verbatim quote, the pattern name, why it carries no forward weight, confidence (High/Medium/Low).
   - Just as important: identify stated reasons that are **legitimate forward-looking concerns** (lock-in risk, team learning curve) and say they are *not* flagged — they move into the comparison.

4. **Surface the invisible alternative.**
   - Elicit or construct the single best alternative use of the *forward* resources (money, people, time, attention). If the user named none, generate 2–3 candidates from context, pick the strongest, and mark it as constructed.
   - Cost it honestly: its own build/ramp time, risks, and dependencies.

5. **Run the two tests.**
   - Zero-based test: answer it explicitly, using the salvage-corrected forward numbers.
   - Best-alternative comparison: a small forward-only table — cash, time/people, and what each branch delivers — with salvage credited wherever it genuinely applies and switching costs on the ledger.

6. **CRITICAL: Verify via adversarial pass before the verdict.**
   - State the preliminary conclusion, then attack it in whichever direction it points:
     - If it says the lean is distorted → **steelman continuing**: did I zero out real salvage or an already-paid switching cost? Is any "sunk" work actually redeployable?
     - If it says continuing is fine → **steelman stopping**: did salvage talk smuggle sunk costs back in? Is the "asset" genuinely usable, or hope wearing a hard hat?
   - **Numeric recount.** Recompute every quantity in the comparison table from its components, and **state the unit of each column in its header** (cash vs. calendar-months vs. engineer-months) — mixed units are the classic silent error. Any figure that doesn't reconcile gets fixed before the verdict.
   - Audit the numbers' provenance: is cost-to-complete from the project's own advocate? Has it slipped before? Buffer suspect estimates and re-check whether the conclusion survives.
   - State concretely **what evidence would flip the verdict**.

7. **Deliver the two-axis verdict.**
   - **Axis 1 — Forward case favors:** continue / the alternative / genuinely close (name the single number that decides it). Confidence.
   - **Axis 2 — Distortion in stated reasoning:** yes (which reasons) / no. Confidence. Note: the lean can be *right even when a stated reason is wrong* — fix the reasoning, keep the conclusion, and say so plainly when that's the case.
   - **Corrected decision statement:** one or two sentences reframing the choice with sunk costs removed and salvage credited — the sentence the user should carry into the room.
   - Close with one line each for "if you proceed" and "if you stop/switch" — the immediate protective step (e.g., independent completion estimate with a hard stop on the next slip; a trial before signing).

## False-Positive Prevention (MUST follow)

Here a "false positive" is a wrongly-cried fallacy or a rigged comparison.

❌ **DON'T:**
- Label every reference to past work as sunk-cost fallacy — describing history is not committing a fallacy.
- Zero out salvage because "sunk costs don't count" — built assets, data, learning, and relationships that reduce forward cost are not sunk.
- Compare continuing against "doing nothing" — the comparison baseline is the best alternative, fully costed.
- Construct a frictionless fantasy alternative (no ramp-up, no risk, no integration cost) to make continuing look bad.
- Dismiss emotional or reputational stakes as irrational — announced commitments and team morale have real forward effects; quantify their direction instead.
- Count a switching cost twice (once as "wasted investment," again as wind-down cost) or assert it without a number.

✅ **DO:**
- Flag only investment-*as-justification*, with the verbatim quote attached.
- Give every salvage claim a usability check: which branch uses it, and what forward cost it actually reduces.
- Apply identical skepticism to both branches' estimates — buffer the advocate's numbers on *whichever* side the advocate sits.
- Check for escalation history (slipped estimates, extended budgets) before trusting a cost-to-complete figure.
- Let "no distortion detected" stand when the stated reasons are genuinely forward-looking.

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Two mirror-image harms. (1) Rubber-stamping escalation — missing that the case to continue rests on "$310k already spent," so good money follows bad. (2) Fallacy-crying — pushing abandonment of work whose salvaged assets put the payoff two cheap weeks away, because past value was illegitimately zeroed. The second harm is subtler and just as expensive.

❌ **UNHELPFUL failure:** A behavioral-economics lecture with no application to *this* decision; "both options have merit" mush; flagging distortion without saying whether the decision itself still holds; refusing a verdict because inputs are estimates.

✅ **Quality bar:** The user could walk into Monday's meeting, state what to do and *why the framing changed*, and defend it — whichever direction the audit landed.

## Expected Output

Forward restatement, the past-investment sort, distortion flags (with quotes) or an explicit all-clear, the costed invisible alternative, both tests, the adversarial pass with flip conditions, and the two-axis verdict with a corrected decision statement.

### Output Format

```
# Opportunity-Cost & Sunk-Cost Audit: [decision]

## Decision, restated forward-looking
[Remaining costs, payoff, timeline; lean; stated reasons verbatim, labeled (a)(b)(c)]

## Past-investment sort
| Item | Amount | Recoverable? | Salvage created (and which branch uses it) | Classification |

## Sunk-cost reasoning detected   [or: "None detected — reasons are forward-looking"]
- Quote (x): "…" — Pattern: [name] — Why it has no forward weight — Confidence: [H/M/L]
- Not flagged: (y) — legitimate forward concern, moved into the comparison

## The invisible alternative
[The single best forward use of the same resources, costed, with source labels]

## The two tests
1. Zero-based: [explicit answer, using salvage-corrected numbers]
2. Best-alternative comparison:
   | Branch | Cash (forward) | People/time (forward) | Delivers |

## Adversarial pass
- Preliminary conclusion: […]  Attacked: […]  Survived because: […]
- Numeric recount: [units declared; figures reconciled]
- What would flip the verdict: [concrete evidence]

## Verdict
- Forward case favors: […] — Confidence: [H/M/L]
- Distortion in stated reasoning: [yes: which / no] — Confidence: [H/M/L]
- Corrected decision statement: "…"
- If you proceed: [one protective step]   If you stop/switch: [one protective step]
```

## Example Output

```
# Opportunity-Cost & Sunk-Cost Audit: Finish in-house analytics dashboard (v2) vs. adopt VendorCo

## Decision, restated forward-looking
Continue: 2 engineers × ~4 months (≈$130k [finance's loaded rate]) to finish v2, then
~0.5 engineer ongoing maintenance (≈$8k/mo). Switch: VendorCo at $60k/yr [vendor quote]
plus ~1 engineer-month integration (≈$16k), freeing both engineers afterward.
Lean: continue building v2. Stated reasons, verbatim:
  (a) "We've already put eight months into this — switching now wastes all of it."
  (b) "I'm worried about vendor lock-in for something this core."
  (c) "We're basically 80% done."

## Past-investment sort
| Item                         | Amount           | Recoverable? | Salvage created                              | Classification |
|------------------------------|------------------|--------------|----------------------------------------------|----------------|
| Engineering on v2 UI layer   | ≈$220k / 8 mo    | No           | Component library ~2 wks reusable elsewhere  | SUNK (mostly)  |
| Data pipeline + event schema | ≈$70k            | No           | Fully reusable — feeds v2 OR VendorCo        | SALVAGE        |
| Requirements + user research | ≈$20k            | No           | Cuts vendor evaluation to ~1 week            | SALVAGE        |
| Total                        | ≈$310k           |              |                                              |                |

Note: both salvage items help BOTH branches, so they are not arguments for continuing —
they lower forward cost on each side.

## Sunk-cost reasoning detected
- Quote (a): "already put eight months in — switching wastes it."
  Pattern: unrecoverable spend as justification. The ≈$220k UI spend is gone under
  either branch; only forward costs differ. — Confidence: High
- Quote (c): "basically 80% done."
  Pattern: completion anchoring with escalation history — the finish estimate has
  slipped twice (3 mo → 5 mo → "4 more"), so the percentage is asserted, not evidenced.
  — Confidence: Medium
- Not flagged: (b) vendor lock-in — a legitimate forward-looking risk; moved into the
  comparison below.

## The invisible alternative
Best forward use of the same 2 engineers × 4 months: the checkout-flow revamp sales has
requested for two quarters, which they tie to ≈$400k of stalled qualified pipeline
[sales estimate — directional, not audited]. That — not "nothing" — is the real price
of finishing v2.

## The two tests
1. Zero-based: arriving today with a working pipeline (salvaged), documented
   requirements (salvaged), a $60k/yr vendor option, and two free engineers — would you
   start building a dashboard UI in-house? On the numbers below: no.
2. Best-alternative comparison (forward, next 12 months):
   | Branch                      | Cash (forward)                   | Effort (eng-months)          | Delivers                    |
   |-----------------------------|----------------------------------|------------------------------|-----------------------------|
   | Finish v2                   | ≈$194k (build 130 + maint 64)    | 12 (build 8 + maint 4)       | dashboard only              |
   | VendorCo + checkout revamp  | ≈$76k (60 + 16 integration)      | 9 (integration 1 + revamp 8) | dashboard AND revamp        |
   Same two engineers either way; the switch branch ships the dashboard sooner and buys
   the revamp besides. Lock-in mitigation: annual term + contractual data export; the
   pipeline is ours under both branches, which keeps any future exit cheap.

## Adversarial pass
Preliminary conclusion: switch branch wins. Attacked both ways:
- Steelmanned continuing: is any "sunk" UI work redeployable? Yes — component library
  saves ~2 weeks on the revamp; credited (shrinks the gap by ≈$8k; verdict unchanged).
  Is lock-in worse than modeled? With export clause + owned pipeline, exit cost ≈ one
  future integration — bounded and known.
- Attacked the switch case: "1 month integration" comes from VendorCo sales [suspect];
  buffered ×1.5 → ≈$24k. Checked coverage of the 3 must-have reports against the
  requirements doc: 2 native, 1 via export — passes, pending hands-on trial.
- Numeric recount: columns declared — Cash (forward $) and Effort (engineer-months, at
  2 eng × 4 mo = 8 for build/revamp). Both rows reconcile: v2 130+64=194; switch 60+16=76.
- Provenance check: cost-to-complete is the project owner's own figure with two prior
  slips; widened to 4–7 months (≈$130–225k). The gap widens, not narrows.
What would flip the verdict: an independent estimate putting v2 completion ≤ 6 weeks
(≈$48k, i.e. ~3 engineer-months), or VendorCo failing the hands-on trial on any must-have report.

## Verdict
- Forward case favors: VendorCo + checkout revamp — Confidence: High (survives buffered
  vendor numbers and the widened completion range).
- Distortion in stated reasoning: Yes — (a) and (c) are sunk-cost patterns; (b) is
  legitimate and is handled by contract terms. — Confidence: High
- Corrected decision statement: "Given a reusable pipeline, documented requirements,
  and two free engineers, do we buy the dashboard for $60k/yr and build the checkout
  revamp — or spend $130–225k of engineering to finish v2 and get only the dashboard?"
- If you proceed anyway: commission an independent completion estimate first, with a
  hard stop if the next milestone slips. If you switch: run a 2-week VendorCo trial
  against the 3 must-have reports before signing; take the annual, not multi-year, term.
```

## Customization Guide

- **Personal decisions (degree, career change, renovation):** replace dollars with months-of-life and energy; salvage = transferable credits, skills, portfolio, network. The zero-based test does most of the work.
- **Vendor/contract renewals:** switching costs dominate — require quantified wind-down, migration, and ramp figures on the table before any verdict.
- **Emotionally loaded or identity-attached decisions:** add the outside-observer frame ("what would you tell a friend with these exact numbers?") and deliver the analysis before the verdict, not fused with it.
- **Escalation history present:** require the cost-to-complete figure from someone other than the project's owner, and say so in the output.
- **Many projects at once:** run only the zero-based test per project as a first pass, then send survivors to `decisioning_prioritization_framework_selector.md` for ranking.

## Techniques Used

- **ST-01 (Clear Objective Statement):** the objective pins the twin lenses — invisible alternative *and* sunk-cost detection — and the two-axis verdict, so the model can't collapse into a generic pros/cons list.
- **ST-02 (Structured Sequential Instructions):** the seven steps enforce the load-bearing order: forward restatement and the SUNK/SALVAGE sort happen *before* any comparison, and the adversarial pass happens *before* the verdict.
- **RT-02 (Multi-Dimensional Analysis Framework):** every past-investment item is analyzed across amount / recoverability / salvage created / classification, and every distortion flag carries quote / pattern / impact / confidence — no bare assertions in either table.
- **QA-02 (Adversarial Stress-Test):** step 6 attacks the preliminary conclusion in whichever direction it points — steelmanning continuing when the audit says "distorted," steelmanning stopping when it says "fine" — recomputes the numbers with declared units, buffers advocate-sourced figures, and must state the evidence that would flip the verdict.
- **QA-20 (Dual-Failure Prevention):** guards the mirror-image harms (rubber-stamped escalation vs. fallacy-crying that kills salvageable work) and the unhelpful failures (bias lecture, verdict refusal), with the bar that the user can state what to do Monday and why the framing changed.

## Related Prompts

- `domain-decision-making/decisioning_regret_minimization.md` — when the decision is identity-heavy and long-horizon, regret is the complementary lens to cost.
- `domain-decision-making/tradeoff_multi_criteria_decision_analysis.md` — if the audit lands "genuinely close," escalate to a full weighted comparison.
- `domain-decision-making/decisioning_prioritization_framework_selector.md` — when the real question is ranking many items, not auditing one lean.

## Verification

- [ ] Frontmatter complete; every technique ID exists in the index.
- [ ] When-to-Use includes a don't-use case.
- [ ] Instructions include an explicit verification step (step 6, adversarial + numeric recount).
- [ ] False-Positive Prevention has real ❌/✅ pairs.
- [ ] Dual-Failure Prevention covers harmful AND unhelpful directions.
- [ ] Findings carry Confidence levels.
- [ ] Example Output is concrete and 80–120 lines, with declared column units that reconcile.
- [ ] No invented data or fabricated authority.

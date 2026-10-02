---
title: "Regulatory Impact Analysis — Baseline, Options, Monetised and Unquantified Costs and Benefits, Discounting, Distribution, and Uncertainty for a Proposed Rule"
category: policy/regulatory-impact
description: "Build the government-side cost-benefit analysis of a proposed rule in the shape OMB Circular A-4, the UK Green Book and OECD RIA practice share: state the problem and the market or institutional failure, fix a no-action baseline, compare at least three regulatory options, monetise what can be monetised with every input tagged by source, keep non-monetised effects visible, discount at the jurisdiction's stated rates, show who gains and who pays, and report the net-benefit range under sensitivity — distinct from a company's compliance-gap view of a new rule (legal_regulatory_change_impact_assessment)."
techniques:
  - DS-01
  - NE-11
  - RT-23
  - QA-04
difficulty: advanced
tags:
  - regulatory-impact-analysis
  - cost-benefit-analysis
  - rulemaking
  - net-present-value
  - distributional-analysis
  - better-regulation
  - is-this-rule-worth-it
  - costs-and-benefits-of-new-regulation
  - government-impact-assessment
updated: "2026-10-02"
reasoning:
  styles: [quantitative, analytic, comparative, normative]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: [structured, matrix]
  user_role: [policy, analyst, regulator, economist]
  mode: [synthesize, decide, document]
related_prompts:
  - domain-policy/policy_options_memo.md
  - domain-policy/policy_implementation_feasibility.md
  - domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md
---

# Regulatory Impact Analysis

**Objective:** Produce the analysis a regulator owes before adopting a rule: does it
do more good than harm against a credible baseline, for whom, and how sure are we —
with the arithmetic shown, the unmonetised effects kept on the page, and the net
benefit reported as a range, not a point.

**Audience:** Agency economists and policy staff, regulatory oversight units,
legislative analysts reviewing an agency's RIA, and stakeholders preparing to
challenge one.

**When to Use:**
- An agency is drafting a proposed rule and needs the impact assessment that goes in
  the docket or consultation pack.
- An oversight body or a commenter is reviewing an agency's RIA and needs to rebuild
  it to find where it is fragile.
- A ministry must choose between prescriptive, performance-based, disclosure and
  market-based instruments for the same problem.
- **Not this prompt if** you are a **regulated company** working out what a new rule
  obliges you to do — `domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md`
  turns rule text into an owned remediation plan; this prompt asks whether society
  should adopt the rule at all. For the broader option choice where cost-benefit is
  one criterion among seven (equity, political viability, reversibility), use
  `domain-policy/policy_options_memo.md`; this prompt is the quantitative annex that
  memo cites. Whether the agency can run the rule is
  `domain-policy/policy_implementation_feasibility.md`.

## Inputs / Context

1. **The proposed rule** (text or summary) and the statutory authority it rests on.
2. **The problem**: the harm, its scale, and the market or institutional failure
   claimed (externality, information asymmetry, market power, coordination failure).
3. **Affected parties**: number and size of regulated entities, consumers, workers,
   government bodies; small-entity counts if a small-business test applies.
4. **Cost evidence**: compliance cost surveys, engineering estimates, industry
   comments, comparable rules' ex post costs.
5. **Benefit evidence**: dose-response or effectiveness studies, avoided-harm
   counts, valuation parameters (e.g. value of a statistical life, value of time).
6. **The jurisdiction's analytic conventions**: discount rate(s), price base year,
   time horizon, required distributional or small-business tests. If none are
   supplied, the analysis states the defaults it uses and why.

Every number is tagged `[data]` (supplied or cited), `[estimate]` (derived from
supplied facts), or `[assumption]` (a placeholder to be replaced). Valuation
parameters are never recalled from memory as if official; a missing one is
`[NOT PROVIDED — use the jurisdiction's published value]`.

## Method

1. **State the need (DS-01).** Name the failure the rule corrects and why existing
   law, liability or markets do not. An RIA without a stated failure is an
   argument, not an analysis.
2. **Fix the baseline.** The world without the rule — including trends already
   under way, voluntary action, and other rules taking effect. Over-stating the
   baseline harm is the commonest way an RIA inflates benefits.
3. **Define 3+ options.** No action (the baseline), the proposed rule, and at least
   two genuine alternatives that differ in mechanism (performance standard vs
   design standard; disclosure; a phased or small-entity variant; a market-based
   instrument). Calibrations of one design are one option.
4. **Map impacts per option.** Direct compliance costs, administrative and
   enforcement costs to government, indirect effects (prices, competition,
   innovation), and benefits — each with the causal step from rule to outcome.
5. **Monetise where defensible (NE-11).**
   `Annual cost = entities × share not already compliant × unit cost`;
   `PV = Σ (B_t − C_t) / (1 + r)^t`; annualise with the capital-recovery factor
   `r / (1 − (1 + r)^−T)`. Report at each discount rate the jurisdiction requires
   (US practice reports more than one; the Green Book uses a declining schedule
   from 3.5%). State base year and horizon.
6. **Keep the unmonetised list.** Effects that cannot be credibly valued (privacy,
   dignity, equity, ecosystem effects) are listed with direction and rough magnitude
   — never silently dropped and never given an invented price.
7. **Distribution.** Who bears costs and who receives benefits by income, region,
   firm size and sector; flag regressive pass-through. State whether any distributional
   weighting is applied and on what authority.
8. **Uncertainty (QA-04, RT-23).** Low / central / high for the 3–5 inputs that
   drive the result, a break-even value for the most uncertain one ("net benefits
   stay positive while avoided cases exceed X"), and a count of `[assumption]`
   inputs. If the sign flips within plausible ranges, say so in the summary.
9. **Compare and conclude.** Net benefits, cost-effectiveness (cost per unit of
   outcome) where benefits resist monetisation, and the option that maximises net
   benefits — then note any reason (statutory mandate, equity) a different option
   might be chosen.

## Output Format

```
# Regulatory impact analysis — [rule]   Jurisdiction: [..]   Base year: [..]
Horizon: [T yrs]   Discount rate(s): [..]   Inputs: [n data / n estimate / n assumption]

## 1. Problem and failure addressed
## 2. Baseline (no action), including trends and other rules
## 3. Options
| Option | Mechanism | Who acts | Key difference |
## 4. Impact map
| Impact | Option | Causal step | Monetised? | Source tag |
## 5. Monetised costs and benefits (PV and annualised, each rate)
| Option | PV costs | PV benefits | Net PV | Annualised net | Cost per [outcome] |
## 6. Non-monetised effects
| Effect | Direction | Rough magnitude | Who |
## 7. Distribution
| Group | Bears | Receives | Net |
## 8. Uncertainty
Drivers (low / central / high) · break-even · sign stable? [Y/N]
## 9. Conclusion and what would change it
```

## Verification

- [ ] A market or institutional failure is named before any option.
- [ ] The baseline includes trends and voluntary compliance, not "zero".
- [ ] At least three mechanism-distinct options, including no action.
- [ ] Every monetised figure carries a source tag; the PV arithmetic recomputes.
- [ ] Results are reported at each required discount rate, with base year and horizon.
- [ ] Non-monetised effects are listed, not priced from invention.
- [ ] Distribution table names who pays, not only aggregate net benefit.
- [ ] Break-even and sign-stability are reported in the summary.

## False-Positive Prevention

1. **Inflated baseline harm.** Counting harm that would have fallen anyway
   (existing trend, a rule already in force) credits the new rule with it.
2. **Gross benefits, net costs.** Benefits counted before offsets (substitution,
   risk-risk trade-offs) against fully-loaded costs, or vice versa. Treat both sides alike.
3. **Transfers as costs or benefits.** A fee paid from firms to government is a
   transfer; only the real resources used to administer it are a cost.
4. **Ancillary benefits doing the work.** If co-benefits carry the case, say so;
   the rule may be the wrong instrument for its stated aim.
5. **Industry cost claims as data.** Compliance costs in comments are usually high
   and ex post costs often lower; label the source and show the range.
6. **Point estimate as the answer.** A net benefit of 40 M with a range of −15 to
   +110 M is a different finding from "40 M"; the range leads.
7. **Precision theatre.** Round to input quality; three `[assumption]` inputs do not
   support a figure to the nearest thousand.

## Example Output

```
# Regulatory impact analysis — Mandatory carbon-monoxide alarms in rented homes
Jurisdiction: national (illustrative)   Base year: 2026 prices   Horizon: 10 yrs
Discount rate: 3.5% [assumption — replace with jurisdiction's rate]
Inputs: 6 data / 5 estimate / 3 assumption

## 1. Problem and failure
Tenants cannot observe appliance condition and landlords do not bear the harm
(split incentive + information asymmetry). ~40 CO deaths and ~4,000 A&E visits/yr
in rented homes [data: health statistics, 5-yr avg].

## 2. Baseline
1.2 M rented homes with a fuel-burning appliance [data]; 55% already have a CO
alarm [data: housing survey] and coverage is rising ~2 pts/yr [estimate] → 75% by
year 10 without a rule.

## 3. Options
A. No action   B. Alarm in every room with a fuel-burning appliance (proposed)
C. Information campaign + alarm supplied free on request   D. B for gas boilers only

## 5. Monetised (Option B vs baseline, PV over 10 yrs)
Homes needing alarms: 1.2 M × 45% = 540,000; 1.3 alarms/home; £22 alarm + £15
fitting [data: retailer survey] → £48/home → £25.9 M yr-1; replacement at yr 7
(£16.8 M, PV £13.2 M); landlord admin £1/home/yr across 1.2 M homes [estimate]
(PV £10 M); enforcement £1.2 M/yr [data] (PV £10 M). PV costs: £59 M.
Deaths avoided: 40 × 45% uncovered share × 50% effectiveness [assumption] = 9/yr,
declining as baseline coverage rises; VSL £[NOT PROVIDED — use published value];
at an illustrative £2.2 M: PV ≈ £131 M. Non-fatal: 900 visits avoided in yr 1, declining,
× £1,200 [data] → £7 M PV.
PV benefits: £138 M   Net PV: +£79 M   Cost per death avoided: ~£1.0 M (≈60 discounted).
Option C: PV costs £14 M, benefits £38 M (uptake 25% [assumption]) → +£24 M.
Option D: 70% of B's benefit at 55% of its cost → £97 M − £32 M = +£65 M.

## 6. Non-monetised
Tenant peace of mind (+, small); false-alarm nuisance (−, small).

## 7. Distribution
Landlords bear ~£48/home up front; partial pass-through to rents ≈ £0.40/month.
Benefits concentrated in older, lower-income private rentals (higher CO incidence).

## 8. Uncertainty
Effectiveness 30% / 50% / 70% → Net PV +£24 M / +£79 M / +£134 M. Break-even
effectiveness ≈ 21%. Sign stable across plausible range; VSL choice moves the
level, not the sign, above ~£0.9 M.

## 9. Conclusion
B maximises net benefits; D is close and cheaper to enforce. If effectiveness
evidence is weaker than ~32%, D overtakes B on net benefit. Replace the 3 assumptions
(effectiveness, discount rate, VSL) before publication.
```

## Techniques Used

- **DS-01 Framework Application** — the shared A-4 / Green Book / OECD RIA sequence: need, baseline, options, impacts, distribution, uncertainty.
- **NE-11 Embedded Calculation Formulas** — entity counts, PV, annualisation and cost-effectiveness shown so they recompute.
- **RT-23 Input Provenance Tagging** — every input marked data / estimate / assumption, with the assumption count in the header.
- **QA-04 Uncertainty Acknowledgment** — low/central/high drivers, break-even and sign-stability reported up front.

## Related Prompts

- `domain-policy/policy_options_memo.md` — the decision memo that cites this analysis as one criterion among seven.
- `domain-policy/policy_implementation_feasibility.md` — whether the agency can actually administer the preferred option.
- `domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md` — the regulated firm's compliance-gap view once the rule is final.

---
title: "Tail Risk Scan — Hunting the Low-Probability, High-Impact Risks the Register Misses"
category: risk/tail-risk
description: "Deliberately hunt for tail and black-swan risks — the low-probability, high-impact events that a standard risk register doesn't capture because they haven't happened recently or feel too unlikely to log. Uses provocation prompts to surface 5–8 tail risks, assesses consequence, and runs a 'would we even know it was happening?' detection check on each. Counters the recency and normalcy biases that keep catastrophic risks off the radar."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - risk-management
  - tail-risk
  - black-swan
  - low-probability-high-impact
  - pre-mortem
updated: "2026-05-10"
reasoning:
  styles: [counterfactual, abductive, adversarial, scenario]
  stakes: high
  horizon: years
  uncertainty: radical
  evidence_quality: sparse
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: ranked_list
  user_role: [executive, founder, investor, operator, analyst]
  mode: [diverge, forecast, audit]
related_prompts:
  - domain-risk/risk_register_builder.md
  - domain-decision-making/scenario_wild_card_injection.md
  - domain-decision-making/scenario_strategic_pre_mortem.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Tail Risk Scan

**Objective:** Hunt for the risks a standard register systematically misses — low-probability, high-impact tail events and black swans that don't make the register because they feel too unlikely, haven't happened recently, or fall outside the team's frame. Use deliberate provocation prompts to surface **5–8 tail risks**, give each a quick consequence assessment, and run a **"would we even know it was happening?"** detection check. The discipline this enforces: separating *probability* from *consequence* so that a 1-in-100 event that would be catastrophic gets logged and watched, even though nothing about routine operations would ever surface it.

**When to use:**
- A risk register exists and you want to pressure-test it for what it's *not* capturing.
- Before a high-stakes, hard-to-reverse commitment (a large bet, a launch, a fundraise, an acquisition).
- A long-horizon plan where rare events accumulate probability over time.
- After a near-miss, when the team is asking "what else are we blind to?"

**When NOT to use:**
- Cataloguing known, routine risks with owners and mitigations — use `risk_register_builder.md`.
- You need to stress-test a *specific plan's* failure path forward — use `scenario_strategic_pre_mortem.md` or `correctness_pre_mortem.md`.
- You want disruptive but plausible scenario injections for planning — use `scenario_wild_card_injection.md`.
- The decision is low-stakes and easily reversible; tail-risk hunting isn't worth the time.

**Audience:** Executives, founders, investors, operators, and analysts making consequential, hard-to-reverse commitments who need to see past the recent-and-routine.

---

## Inputs / Context

1. **The subject.** The project, bet, operation, or organization whose tail risks you're hunting. One paragraph.
2. **The existing risk register (if any).** So the scan can deliberately look *outside* it.
3. **Horizon.** Over what window the tail risks matter — tail probabilities accumulate over time.
4. **What "catastrophe" means here.** The outcomes that would be unrecoverable or severely damaging — define them so the scan aims at consequence, not just novelty.
5. **Recent history.** What's gone wrong before, and what *hasn't* gone wrong in a long time (the latter is a hunting ground — dormant risks feel impossible right up until they aren't).

---

## Constraints

### Must
- Surface **5–8 tail risks**, each genuinely low-probability and high-impact. Reject anything already on the register or anything that's merely a routine moderate risk.
- Generate them using the **provocation prompts** below; don't just free-associate.
- For each tail risk, separate **probability** (deliberately low) from **consequence** (deliberately high). The whole point is consequence-dominant prioritization.
- Run a **detection check** on each: "would we even know it was happening — and how early?" Classify detection as **early-warning available / detectable only once underway / invisible until the effect lands**.
- For each, name **one cheap thing** that would improve detection or reduce consequence now — a tripwire, a hedge, a small option that pays off only in the tail.
- Distinguish risks that are **outside the team's control** (monitor + hedge) from those that are **partly inside it** (act now).

### Must Not
- Surface risks that are really just normal register items dressed up as tail risks. Tail = rare *and* severe.
- Dismiss a risk because "that's never happened." Recency and absence are exactly the biases this scan exists to defeat.
- Let probability estimates suppress consequence. A tiny probability times a catastrophic consequence is the target, not a reason to ignore it.
- Produce risks with no detection check — the "would we even know?" question is the most operationally valuable output.
- Recommend heavy, expensive mitigations for 1-in-100 events; the moves should be cheap tripwires and hedges, not full programs.

---

## Instructions

### Step 1 — Define catastrophe and the horizon
State what an unrecoverable or severely damaging outcome looks like for this subject, and the window over which it matters. This aims the scan at consequence.

### Step 2 — Run the provocation prompts
Work each prompt deliberately and capture candidates:
- **"What would have to go wrong for this to become a catastrophe?"** — reason backward from the worst outcome.
- **"What 1-in-100 event would matter enormously if it occurred?"** — low base rate, high stakes.
- **"What's the worst plausible news headline about this in five years?"** — concretize the failure.
- **"What risk is everyone ignoring because it hasn't happened recently?"** — dormant-risk hunting.
- **"What are we assuming is stable that has failed elsewhere?"** — borrowed failure from analogous domains.
- **"What correlated failure could hit several of our safeguards at once?"** — common-cause / simultaneous failure.
- **"Who would profit from harming us, and what's their cheapest move?"** — adversarial tail.

### Step 3 — Filter to genuine tail risks
Keep only candidates that are both low-probability and high-impact, and not already on the register. Discard routine moderate risks. Aim for 5–8 survivors.

### Step 4 — Assess consequence
For each survivor, write a quick consequence sketch: what breaks, how far the damage spreads, whether it's recoverable. Keep probability explicitly low and separate.

### Step 5 — Run the detection check
For each, answer **"would we even know it was happening, and how early?"** Classify:
- **Early-warning available** — leading indicators exist; name them.
- **Detectable only once underway** — we'd notice during, not before.
- **Invisible until the effect lands** — no warning. These are the most dangerous; flag them.

### Step 6 — Name one cheap move per risk
A tripwire (an observable to watch), a hedge (a cheap option that pays off in the tail), or a small consequence-reducer. Avoid recommending expensive programs for rare events.

### Step 7 — Sort and conclude
Order by consequence (not probability). Separate control-outside (monitor + hedge) from control-inside (act now). Name the one tail risk that is both most catastrophic and least detectable — the headline blind spot.

---

## False-Positive Prevention

1. **Register-item smuggling.** Listing routine moderate risks as "tail risks" to pad the count. Tail means rare *and* severe; filter hard.
2. **Recency dismissal.** "That hasn't happened in years, so skip it." Dormancy is the hunting ground, not a reason to ignore. The longer it's been, the more attention it may deserve.
3. **Probability suppression.** Letting a low probability talk you out of logging a catastrophic consequence. The scan prioritizes by consequence; probability sizes the hedge, not whether to look.
4. **Detection skip.** Surfacing the risk but not asking whether you'd see it coming. The detection check is the most actionable output — never omit it.
5. **Mitigation overkill.** Proposing a full program to defend against a 1-in-100 event. The right move is usually a cheap tripwire or hedge, sized to the probability.
6. **Frame capture.** Only finding risks inside the team's existing mental model. The borrowed-failure and adversarial prompts exist to break the frame — use them.
7. **Comfort sorting.** Ranking by probability so the scary-but-rare risks sink to the bottom. Rank by consequence.
8. **False precision.** Assigning spuriously exact probabilities to radically uncertain events. Keep probability qualitative (rare / very rare / unprecedented-but-possible); precision here is theater.

---

## Output Format

```
# Tail risk scan — [subject]

## Catastrophe definition & horizon
- Catastrophe here means: [unrecoverable / severe outcomes]
- Horizon: [window over which tail risks accumulate]

## Tail risks (sorted by consequence, not probability)
### T1 — [name]
- Probability: [rare / very rare / unprecedented-but-possible]
- Consequence: [what breaks, how far it spreads, recoverable?]
- Detection: [early-warning available / detectable only once underway / invisible until effect lands]
  - If early-warning: [the leading indicators]
- Control: [outside our control → monitor+hedge | partly inside → act now]
- Cheap move now: [tripwire / hedge / consequence-reducer]

### T2 … T8
[Same structure]

## Headline blind spot
- Most catastrophic + least detectable: [T# — why this one]

## Tripwire & hedge summary
| Risk | Cheap move | Type | Owner |
|------|-----------|------|-------|
| T1 | [observable to watch] | tripwire | [name] |
| T2 | [cheap option] | hedge | [name] |
| … | | | |
```

---

## Verification

- [ ] 5–8 tail risks surfaced, each genuinely low-probability and high-impact.
- [ ] All provocation prompts run, including borrowed-failure and adversarial.
- [ ] None duplicate the existing register; none are routine moderate risks.
- [ ] Probability and consequence kept separate; risks sorted by consequence.
- [ ] Every risk has a detection check classifying warning availability.
- [ ] Invisible-until-effect risks flagged as most dangerous.
- [ ] Each risk has one cheap tripwire / hedge / consequence-reducer.
- [ ] Control-outside vs control-inside distinguished.
- [ ] Headline blind spot (most catastrophic + least detectable) named.
- [ ] No recency dismissal; no probability suppression; no false precision.

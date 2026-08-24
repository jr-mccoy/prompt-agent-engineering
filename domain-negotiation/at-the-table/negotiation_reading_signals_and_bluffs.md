---
title: "Reading Signals and Testing Bluffs — What Their Behaviour Actually Tells You"
category: negotiation/at-the-table
description: "Interpret what the counterpart's behaviour reveals, and test a claimed constraint without calling anyone a liar. Separates high-information signals (what they negotiate hardest for, response latency, which MESO they pick, what they concede without being asked) from low-information ones body-language folklore over-reads. Provides four bluff tests that work by making a claim costly to maintain rather than by challenging it. Counters the two symmetric errors: taking every stated constraint at face value, and confidently reading tells that carry no information."
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
  - signals
  - bluffs
  - inference
  - calibration
updated: "2026-07-26"
reasoning:
  styles: [abductive, analytic, adversarial, evaluative]
  stakes: variable
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: variable
  collaboration: solo
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [diagnose, audit, decide]
related_prompts:
  - domain-negotiation/at-the-table/negotiation_question_sequencing_live.md
  - domain-negotiation/preparation/negotiation_counterpart_simulation.md
  - domain-negotiation/at-the-table/negotiation_hard_bargainer_defense.md
---

# Reading Signals and Testing Bluffs — What Their Behaviour Actually Tells You

**Objective:** Negotiators routinely over-read the wrong signals and under-read the right ones. Posture, eye contact, and the folk catalogue of "tells" carry almost no reliable information about a counterpart's position — but *what they negotiate hardest for*, *how fast they respond*, *which package they pick from an equivalent set*, and *what they concede before being asked* carry a great deal. This prompt sorts observed behaviour into high- and low-information categories, extracts the inference each genuinely supports, and assigns a confidence to it. It then supplies four **bluff tests** that work not by challenging a claim but by making it costly to maintain — the difference between "I don't believe your deadline" and a move that requires a real deadline to behave like one.

This is downstream of `negotiation_question_sequencing_live.md`, which gets the answers; this interprets them and the behaviour around them.

**When to use:**
- A counterpart has asserted a constraint — a deadline, a final number, a policy — and you need to know whether it holds.
- You want to extract what a negotiation has revealed rather than only what was said.
- Their behaviour has been inconsistent and you want a theory that fits.
- After presenting MESOs, to read what their selection reveals.

**When NOT to use:**
- You are facing coercive tactics and need a response rather than an interpretation — `negotiation_hard_bargainer_defense.md`.
- You need a full model of their incentives and likely moves — `preparation/negotiation_counterpart_simulation.md`.
- The relationship is the subject rather than the deal — `difficult-conversations/difficultconvo_post_review.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals who need to know which of a counterpart's stated limits are real.

---

## Inputs / Context

1. **The negotiation and its history.** What has been exchanged, in sequence.
2. **Claims made.** Every constraint, deadline, limit, or alternative the counterpart has asserted.
3. **Behaviour observed.** What they pushed hardest on, what they gave easily, response times, who attended what.
4. **MESO responses.** If packages were offered, which they engaged with and how.
5. **Inconsistencies.** Anything said or done that does not fit the rest.
6. **Your current model of them.** From `negotiation_counterpart_simulation.md`, if built.

---

## Constraints

### Must
- Sort observations into **high-information** and **low-information** before drawing any inference, and discard the low-information ones rather than weighting them lightly.
- State the **inference each signal supports** and, equally, what it does *not* support. Most over-reading comes from an inference broader than the evidence.
- Assign **confidence** (strong / moderate / weak) to every inference, based on how many alternative explanations survive.
- Generate at least **two alternative explanations** for any behaviour before settling on one.
- Test claims by making them **costly to maintain**, never by challenging the counterpart's honesty.
- Distinguish a claim that is **false** from one that is **true but soft** — most constraints are real and movable rather than fabricated.
- Note what your own behaviour has **signalled** to them, since reading is symmetric.

### Must Not
- Rely on body-language folklore. Posture, eye contact, arm position, and micro-expression reading have essentially no validated diagnostic value in this setting, and confident use of them produces confident errors.
- Call a bluff directly. "I don't think that's true" forces the counterpart to defend the claim publicly, which converts a soft constraint into a hard commitment.
- Treat consistency as truth. A well-prepared counterpart is consistent; consistency indicates preparation, not accuracy.
- Infer from a single observation. One data point supports a hypothesis, never a conclusion.
- Assume a bluff because a claim is inconvenient. Inconvenience is not evidence.
- Act on a weak-confidence inference as though it were strong.

---

## Instructions

### Step 1 — Inventory claims and behaviour separately
Two lists. **Claims:** every constraint, deadline, limit, or alternative they have asserted, quoted. **Behaviour:** what they did — what they pushed on, what they conceded unprompted, response latency, attendance, what they returned to repeatedly. Keeping these apart matters, because behaviour is generally more informative than assertion.

### Step 2 — Sort by information value
Discard the low-information column rather than weighting it:

| High information | What it supports |
|---|---|
| What they negotiate hardest for | Their genuine priority ranking |
| What they concede without being asked | Issues they were told to give |
| Which MESO they engage with | Their true valuation asymmetries |
| Response latency changes | Where approval or internal debate sits |
| Who they bring to a meeting | What they expect to be contested |
| What they return to repeatedly | The brief's binding constraint |

| Low information — discard | Why |
|---|---|
| Posture, eye contact, gesture | No validated diagnostic value here |
| Tone and warmth | A negotiating posture, deliberately chosen |
| Speed of agreement on minor terms | Rehearsed |
| Stated enthusiasm or reluctance | Free to produce, so uninformative |

### Step 3 — Extract the bounded inference
For each high-information observation write what it supports **and what it does not**. Example: "they conceded payment terms immediately" supports *payment terms were not in their brief as a defended item*; it does **not** support *they are flexible generally* or *they are eager to close*. Bounding the inference is where over-reading is prevented.

### Step 4 — Generate alternative explanations
For each inference, write at least two other explanations that fit the same evidence. "They went quiet for four days" fits: internal approval is running; they are working a competing option; the person is on leave; they are manufacturing time pressure. Confidence is a function of how many alternatives survive — if three do, confidence is weak regardless of how compelling your preferred story feels.

### Step 5 — Classify each claim
For every asserted constraint assign one of three:
- **Verified** — externally checkable and checked.
- **Plausible-real** — consistent with their structure, incentives, and behaviour.
- **Soft** — stated as absolute, but the behaviour around it suggests movement.

Note that "soft" is the common case and is not an accusation. Most constraints are genuine at one level and negotiable at another: a real policy with a real exception process, a real deadline with a real extension path.

### Step 6 — Apply the bluff tests
Four tests, all of which work by making a claim costly to maintain rather than by disputing it:

| Test | Move | What it reveals |
|---|---|---|
| **The accommodation test** | Offer something that fully satisfies the stated constraint but costs you little | A real constraint accepts it; a pretextual one moves the goalposts |
| **The timeline test** | Let the deadline approach without moving | Real deadlines produce action; manufactured ones quietly pass |
| **The exception test** | "What would need to be true for an exception?" | Real policies have exception processes; invented ones have none |
| **The specificity test** | Ask for the mechanism — who set it, when, applying to whom else | Real constraints have detail; asserted ones stay general |

Each is a question or an offer, not a challenge. None requires the counterpart to admit anything.

### Step 7 — Read the MESO response
If equivalent packages were offered, their selection is the highest-quality signal available, because it is a revealed preference rather than a statement. Record which they engaged with, what they tried to modify, and what they ignored entirely. Then update the valuation table in `preparation/negotiation_package_trade_design.md` — the ignored dimension is one they do not value, and it is now a cheap concession.

### Step 8 — Audit your own signals
Reading is symmetric. Write what your behaviour has told them: what you pushed hardest on, what you conceded unprompted, how fast you responded, whether your enthusiasm was visible. Note anything that revealed a priority you meant to protect, and what to change for the remainder.

### Step 9 — Adversarial check
- Which inference are you most attached to, and what evidence would overturn it?
- Are you reading a bluff because the claim is inconvenient rather than because the evidence supports it?
- If they are simply telling the truth about everything, does your strategy still work?

---

## False-Positive Prevention

1. **Body-language reading.** Drawing conclusions from posture, eye contact, or gesture. These have no validated diagnostic value in negotiation and generate high-confidence errors — the worst combination.
2. **Direct bluff-calling.** Saying you do not believe a claim. It forces public defence of the position, converting something soft into a commitment the counterpart now cannot abandon without losing face.
3. **Consistency-as-truth.** Treating a consistent story as a true one. Consistency measures preparation. A rehearsed position is more consistent than a candid one.
4. **Single-observation inference.** Concluding from one data point. One observation raises a hypothesis; confidence requires convergence from independent signals.
5. **Unbounded inference.** Stretching a narrow signal into a broad conclusion — from "they conceded this term easily" to "they are eager." Write what the signal does *not* support alongside what it does.
6. **Inconvenience-driven scepticism.** Classifying a claim as soft because accepting it is expensive. That is motivated reasoning; the evidence must be independent of the cost.
7. **The false/true dichotomy.** Assuming a constraint is either fabricated or immovable. Most are real *and* have an exception path; the exception test finds it without anyone being accused of anything.
8. **Asymmetric reading.** Analysing their signals while ignoring your own. A sophisticated counterpart is running this same analysis, and your unprompted concessions have told them your priority ranking.

---

## Output Format

```
# Signal Reading — [negotiation]

## Claims asserted
| Claim (quoted) | When | Classification |
|---|---|---|
| "[...]" | [...] | verified / plausible-real / soft |

## High-information observations
| Observation | Inference it supports | What it does NOT support | Alternatives that survive | Confidence |
|---|---|---|---|---|
| [...] | [...] | [...] | [n]: [...] | strong/moderate/weak |

## Discarded (low information)
[List, so it is visible that they were considered and set aside.]

## Bluff tests applied or planned
| Claim | Test | Move / exact wording | What each outcome would mean |
|---|---|---|---|
| [...] | accommodation | "[...]" | accepts → real; goalposts move → pretextual |

## MESO response reading
Engaged with: [...] · Tried to modify: [...] · Ignored: [...]
Valuation update: [...]
Newly identified cheap concession: [...]

## My own signals
| What I did | What it told them |
|---|---|
| [...] | [...] |
Priority I revealed unintentionally: [...] · Change for the remainder: [...]

## Adversarial check
- Inference I'm most attached to + what would overturn it: [...]
- Am I reading a bluff because it's inconvenient? [...]
- Does the strategy survive if they're telling the truth about everything? [...]
```

---

## Verification

- [ ] Claims and behaviour inventoried separately.
- [ ] Observations sorted high/low information, with low-information ones visibly discarded.
- [ ] Every inference states both what it supports and what it does not.
- [ ] At least two alternative explanations generated per inference.
- [ ] Confidence assigned as a function of surviving alternatives, not of narrative appeal.
- [ ] Each claim classified verified / plausible-real / soft.
- [ ] Bluff tests are cost-imposing moves, never challenges to honesty.
- [ ] MESO response read as revealed preference and fed back to the valuation table.
- [ ] Own signals audited, with an unintentionally revealed priority named.
- [ ] Adversarial check tests the strategy against full counterpart honesty.
- [ ] No inference drawn from posture, tone, gesture, or expressed enthusiasm.
- [ ] No claim disputed directly.

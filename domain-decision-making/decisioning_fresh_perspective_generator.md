---
title: "Fresh Perspective Generator (Stuck Decision)"
category: decision-making
description: "Break a stuck decision out of one viewpoint by generating four deliberate alternative viewpoints — inversion, distant analogy, adversary, and 10-year-out — each producing a distinct reframe of the same options. Decision-scoped (not model-output focused); produces viewpoint shifts, not solution-space shifts."
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-making
  - perspective-shift
  - reframing
  - stuck-decision
  - inversion
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_shift_fresh_latent_corner.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-decision-making/decisioning_reasoning_emulation.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
---

# Fresh Perspective Generator (Stuck Decision)

**Objective:** Take a stuck decision — same options being chewed over without progress — and generate four deliberate alternative viewpoints on the same option set: an inversion view, a distant-analogy view, an adversary view, and a 10-year-out view. Each viewpoint produces a distinct reframe that shifts which option looks best, what the dominant criterion is, or what's actually being decided.

**When to Use:**
- You've been ruminating on a decision for more than a week without movement.
- A rapid tradeoff analysis produced a winner but it doesn't feel right.
- Multiple advisors are giving you the same lens and you suspect the lens itself is the problem.
- You're aware you're framing this through one mental model and want forced alternatives.

**When NOT to use:**
- You don't yet have options. Use `decisioning_first_principles_problem_decomposition.md` first.
- You want to escape the *solution* space rather than shift viewpoint on the existing options. Use `decisioning_shift_fresh_latent_corner.md`.
- You want to escape the model's default *output* on a topic (not a personal decision). Use the prompts in `domain-prompt-engineering/escape-median/`.

**Distinction from `decisioning_shift_fresh_latent_corner.md`:** This prompt holds the **option set fixed** and shifts the **viewpoint** evaluating them. The latent-corner prompt holds the **problem fixed** and shifts the **option set itself**. If after running this prompt all four viewpoints still produce the same winner, the decision is robust; if they diverge wildly, the user's framing is doing too much of the work.

**Audience:** Individual decision-makers stuck in a loop on a structured choice.

---

## Inputs / Context

1. **The decision in one sentence.**
2. **The current options.** 2–4 named options (this prompt does not generate new options — that's a different prompt).
3. **The framing the user is currently using.** What are they treating as the dominant criterion? What is the implicit assumption about what "winning" looks like?
4. **What advice they've already gotten.** One sentence on what people around them are saying. (This calibrates which viewpoints would actually be fresh.)
5. **Why they think they're stuck.** "I keep flipping," "I'm waiting for more information that isn't coming," "every option feels wrong" — different stuck-states benefit from different viewpoints first.

---

## Constraints

### Must
- Generate exactly four viewpoints: **Inversion**, **Distant Analogy**, **Adversary**, **10-Year-Out**. No fewer, no substitutions.
- Each viewpoint must produce: a one-paragraph reframe, the dominant criterion that viewpoint surfaces, and that viewpoint's pick from the existing option set with reasoning.
- The reframes must actually be different from each other. If two viewpoints produce the same reframe, restart that one.
- At least one viewpoint must contradict the user's current leaning (otherwise the prompt is producing comfort, not perspective).
- End with a convergence/divergence summary: do the four viewpoints agree on a winner? If not, where is the disagreement, and what does that disagreement reveal about which criterion is actually deciding the call.

### Must Not
- Add new options. The whole point is to test the existing set against multiple lenses.
- Produce viewpoints that are merely "more cautious" or "more bold" versions of the user's current view. Each lens must come from a different axis.
- Use empty rhetorical reframes ("imagine you're a kid again"). Each viewpoint must produce a concrete pick + reasoning.
- Default to "it depends." If a viewpoint genuinely cannot pick, say which option it would *first eliminate*.
- Conflate viewpoint shifts with solution-space shifts (that's the latent-corner prompt's job).

---

## Instructions

### Step 1 — Restate
Restate the decision, options, current framing, current leaning, and stuck-state.

### Step 2 — Inversion view
Reframe the decision as: "What would I be choosing if I were trying to *guarantee a bad outcome*?" Invert. Then ask which of the user's current options most resembles the inverted-bad-outcome and which most resembles its opposite.
- Reframe paragraph
- Dominant criterion this view surfaces (often: which option I'd most regret if it went wrong)
- This view's pick + reason
- This view's first-eliminate

### Step 3 — Distant-analogy view
Find a structurally similar decision from a domain unrelated to the user's: chess opening selection, restaurant menu design, jazz solo, surgical staging, military supply logistics. Pick one. Map the user's options onto positions in that analogy. Use the analogy's known dynamics to evaluate.
- Name the analogy and why it maps
- Reframe paragraph in the analogy's vocabulary
- Dominant criterion in the analogy (often: tempo, optionality, or sequencing)
- This view's pick translated back to the user's domain + reason
- This view's first-eliminate

### Step 4 — Adversary view
Imagine someone whose interests are directly opposed to the user winning at this decision. Not generic critic — a specific competitor, an ex-colleague who would benefit from the user choosing wrong, an opposing party in negotiation. What would they hope the user picks?
- Who the adversary is and what they would gain from the user's mistake
- Reframe paragraph from the adversary's POV
- Dominant criterion (often: where the user is most overconfident)
- The pick the adversary fears most + reason
- This view's first-eliminate (the option the adversary is happy to see the user pick)

### Step 5 — 10-year-out view
The user is sitting at their desk in 2036 looking back at this decision. The 2036 self has information the 2026 self doesn't. Without manufacturing that information, ask: which option, evaluated against the *trends already visible in 2026* — not predictions, but visible directions — survives a decade?
- Reframe paragraph
- Dominant criterion (often: which option compounds or stays optionality-rich)
- This view's pick + reason
- This view's first-eliminate

### Step 6 — Convergence/divergence
Build a 2-column summary table: viewpoint and pick. Then:
- **Convergent (3+ agree):** name the winner; the decision is robust.
- **Split:** name the split and which axis is producing the disagreement (e.g., short-term-survival vs. long-term-compounding). The split itself is the decision the user actually has to make.
- **Fully divergent (4-way split):** the framing is collapsing. Restart with `decisioning_first_principles_problem_decomposition.md`.

### Step 7 — One question for the user
End with a single question for the user, derived from the convergence/divergence pattern, that they should answer before making the call. Not "what do you want?" — a specific question like "If you had to bet your reputation on one criterion mattering most, which one?"

---

## False-Positive Prevention

1. **Sanding off the contradictions.** If all four viewpoints quietly converge on the user's current leaning, the prompt is producing flattery. Restart and force one viewpoint to oppose the leaning.
2. **Distant-analogy theater.** A weak analogy ("it's like cooking — you choose ingredients") adds nothing. The analogy must have **its own internal dynamics** the user does not yet have for the real decision.
3. **Adversary as strawman.** "An adversary would want you to be lazy" is generic. Specify the adversary and their actual incentive.
4. **10-year-out as fortune-telling.** This view does not predict the future. It tests which option survives the trends already observable now.
5. **Reframe vs. restate.** A reframe shifts which criterion dominates; a restate just rewords the same view. If the new paragraph wouldn't change a reader's pick, it's a restate.
6. **Identical first-eliminates.** If three viewpoints all want to eliminate the same option, that's strong signal — but verify it isn't an artifact of the user's framing leaking into every viewpoint.
7. **Comfort closure.** The end-of-prompt question must make the user uncomfortable. If it's reassuring, replace it.

---

## Output Format

```
# Fresh perspective — [decision in one sentence]

**Options:** [list]
**Current framing:** [user's dominant criterion]
**Current leaning:** [option] — stuck because [reason]

## Inversion view
**Reframe:** [paragraph]
**Dominant criterion:** […]
**Pick:** [option] — [reason]
**First eliminate:** [option] — [reason]

## Distant-analogy view
**Analogy:** [chess opening / restaurant menu / surgical staging / …]
**Why this maps:** [one sentence]
**Reframe (in analogy's vocabulary):** [paragraph]
**Dominant criterion:** […]
**Pick (translated back):** [option] — [reason]
**First eliminate:** [option] — [reason]

## Adversary view
**Adversary:** [specific role / person-type] — would gain by [user's mistake]
**Reframe (adversary POV):** [paragraph]
**Dominant criterion:** [the user's overconfidence axis]
**Pick adversary fears most:** [option] — [reason]
**First eliminate (the option adversary is happy to see):** [option] — [reason]

## 10-year-out view
**Reframe:** [paragraph]
**Visible trends informing the view:** [2–3 named trends, no predictions]
**Dominant criterion:** [compounding / optionality / something else]
**Pick:** [option] — [reason]
**First eliminate:** [option] — [reason]

## Convergence summary
| Viewpoint        | Pick     | First eliminate |
|------------------|----------|-----------------|
| Inversion        | [opt]    | [opt]           |
| Distant analogy  | [opt]    | [opt]           |
| Adversary        | [opt]    | [opt]           |
| 10-year-out      | [opt]    | [opt]           |

**Verdict:** [Convergent / Split on (axis) / Fully divergent]
**If split:** the disagreement is on [axis]. The user's actual decision is which axis to weight, not which option to pick.

## One question for the user
> [the discomfort-producing question]
```

---

## Verification

- [ ] All four viewpoints are present (inversion, distant analogy, adversary, 10-year-out).
- [ ] Each viewpoint produces a reframe paragraph, a dominant criterion, a pick, and a first-eliminate.
- [ ] At least one viewpoint contradicts the user's current leaning.
- [ ] The distant analogy is actually distant (not from the user's domain) and has its own internal dynamics.
- [ ] The adversary is specified, not generic.
- [ ] The 10-year-out view names visible trends, not predictions.
- [ ] No new options were introduced.
- [ ] Convergence summary table is filled, with a verdict (convergent / split / fully divergent).
- [ ] Final question is uncomfortable, not reassuring.

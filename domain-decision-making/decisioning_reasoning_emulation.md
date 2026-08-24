---
title: "Expert-Lens Reasoning Emulation"
category: decision-making
description: "Stress-test a decision by emulating the reasoning process of a specific expert role (investor, operator, scientist, lawyer, regulator). Surfaces the questions that lens would ask, what it would flag, and where the user's current framing misaligns with how that role actually thinks."
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
  - perspective-taking
  - role-emulation
  - stress-test
  - blind-spot
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-decision-making/decisioning_interrogative_mode.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
  - domain-decision-making/decisioning_fresh_perspective_generator.md
---

# Expert-Lens Reasoning Emulation

**Objective:** Take a specific decision the user is weighing and stress-test it through the reasoning process of a named expert role (e.g., a venture investor, a startup operator, a clinical researcher, a litigation attorney, a financial regulator). Output the questions that lens would ask first, the structural concerns it would flag, the metrics or evidence it would demand, and the points where the user's current framing misaligns with how that role actually evaluates decisions.

**When to Use:**
- A decision feels "fine" but you suspect a specific stakeholder (a board member, a regulator, an acquirer, a key hire) would tear it apart.
- You are about to pitch, defend, or seek approval and want to pre-rehearse the hardest questions from a specific lens.
- You have a decision that touches a domain you don't live in (legal, financial, clinical, regulatory) and want to surface what an expert in that domain would prioritize *before* paying one.
- You're trying to widen your evaluation beyond a single mental model.

**When NOT to use:**
- You don't yet have a decision named — use `decisioning_first_principles_problem_decomposition.md` first.
- You want unfiltered alternative viewpoints (not constrained to a named role) — use `decisioning_fresh_perspective_generator.md`.
- You want to pressure-test reasoning quality on a *past* decision — use the judgment assessment prompt instead.

**Audience:** Founders, product leaders, operators, and individual contributors making decisions that will be evaluated by a specific kind of stakeholder downstream.

---

## Inputs / Context

1. **The decision in one sentence.** "Should we raise a Series B now or in nine months?" "Should we sign this enterprise contract with a 3-year exclusivity clause?" "Should I take the in-house counsel role or stay at the firm?"
2. **The expert role to emulate.** Be specific: not "a finance person" but "a Series-B-stage venture investor who has led a board for 5+ years." Not "a doctor" but "a hospital-system CMO evaluating whether to adopt a new clinical pathway."
3. **Your current framing.** Two to four sentences on how you are currently thinking about it: the options you see, the criteria you're weighing, and the leaning (if any).
4. **What you know about this lens already.** One paragraph: prior interactions, public statements, or assumptions you have about how this role typically reasons. (This calibrates the model's emulation; absent context, it will default to genre stereotypes.)
5. **The forum.** Where will this lens evaluate the decision — a board meeting, a deposition, a deal memo, a tumor board, a regulatory filing. The forum shapes what evidence is admissible.

If the role is too vague to specify (e.g., "a smart person") **stop** — the prompt only adds value when the lens is concrete enough to have characteristic priorities.

---

## Constraints

### Must
- Name the lens precisely in the output: role + seniority + context (e.g., "growth-stage SaaS investor, post-product-market-fit, late-2026 capital environment").
- Generate at least 6 questions the lens would ask in the first 10 minutes of evaluating this decision. Order by which one is most likely to disqualify the decision early.
- Identify at least 3 structural concerns — not surface objections, but the load-bearing assumptions the lens would probe.
- Specify what evidence the lens would demand to be persuaded, and which of that evidence the user already has vs. has not gathered.
- Surface 2–4 framing mismatches: places where the user's current framing uses language, metrics, or assumptions that this lens would reject or reframe.
- Output a "what would persuade this lens" paragraph and a "what would harden their objection" paragraph — both in the lens's voice, not the user's.
- End with a calibration note: how confident the model is in the emulation, and what specific knowledge gap (industry data, named-person familiarity) most limits the fidelity.

### Must Not
- Produce a generic "investor would care about ROI" answer. If the output reads like a Wikipedia summary of the role, restart with more specificity.
- Invent named precedent (real or fake deals, cases, studies) the lens has supposedly worked on. The lens is generic-but-precise; do not fabricate a CV.
- Treat the lens as adversarial. The goal is high-fidelity emulation, not a hit job.
- Validate the user's current framing. The output should feel like a stress test, not a confirmation pass.
- Smuggle in the user's own conclusions through the lens's voice.

---

## Instructions

### Step 1 — Lens specification
Restate the role with three calibrating attributes: tenure, current operating environment, and primary success metric. Example: "Series-B SaaS investor; 8+ years on boards; current environment of compressed multiples and slower growth; primary metric is net revenue retention with payback under 18 months." If the user's role description is vaguer than this, expand it explicitly and flag the assumption.

### Step 2 — First-10-minute questions
Generate 6–10 questions this lens would ask in the first 10 minutes. Order them by disqualification power: question 1 is the one that, if answered badly, ends the conversation. Each question must be specific enough that a generic answer would not satisfy it.

### Step 3 — Structural concerns
Identify the 3–5 load-bearing assumptions in the user's current framing that this lens would probe. For each:
- Name the assumption in one sentence.
- Why this lens specifically attacks it (what experience or pattern in the role drives the skepticism).
- The pivot question that would expose whether the assumption holds.

### Step 4 — Evidence demand
List the evidence this lens needs to evaluate the decision well: data, documents, references, comparables. For each item, mark whether the user has indicated they have it. The gap is the homework before the next conversation.

### Step 5 — Framing mismatches
Identify 2–4 places where the user's current framing uses language or metrics this lens would reject. For each:
- The user's current phrasing.
- The lens's preferred phrasing or metric.
- Why the substitution matters (it's not just vocabulary; the substitution surfaces a different question).

### Step 6 — Persuasion vs. hardened-objection
Write two short paragraphs in the lens's voice:
- **What would persuade me:** the case the user would need to make, with the strongest single piece of evidence named.
- **What would harden my objection:** the answer or move that, if the user gave it, would end the conversation in a "no."

### Step 7 — Calibration
State the model's confidence in the emulation (high / medium / low) and name the single knowledge gap that most reduces fidelity. Example: "Medium confidence; without 2026 sector multiples and post-money trends, persuasion paragraph generalizes a market state."

---

## False-Positive Prevention

1. **Lens stereotyping.** A "VC" is not one role. A seed-stage solo GP and a late-stage multi-fund partner reason differently. If the prompt's emulation could apply to any version of the role, the lens is too vague.
2. **Steelmanning is not emulation.** Steelmanning produces the strongest version of an argument. Emulation reproduces how the role *actually* reasons — including its blind spots and habits. Don't sand off the lens's biases in the name of giving the user "a balanced view."
3. **Hidden author voice.** If the persuasion paragraph reads like the user's pitch already, the lens has been captured. Restart with a sharper tension between user and lens.
4. **False expertise.** The model does not know what every named senior partner thinks. Don't impersonate named individuals; impersonate the role with its characteristic patterns.
5. **Generic "ask better questions" output.** The questions must be specific to *this* decision, not transferrable to any decision in the same domain.
6. **Confirmation bias rescue.** If the lens ends up agreeing with the user's leaning, examine whether the lens was selected to agree. The most useful lens is one that would push back.
7. **Single-axis attack.** A real expert evaluates on multiple axes (market, team, defensibility, timing, downside). If the output flags only one concern, the emulation is shallow.

---

## Output Format

```
# Expert-lens emulation — [decision in one sentence]

## Lens
- Role: [precise role + seniority + context]
- Calibrating attributes: [tenure | environment | primary success metric]
- Forum: [where the lens will evaluate]

## First-10-minute questions
1. [Question 1 — most disqualifying] — Why this is the opening: [one line]
2. [Question 2] — Why: [one line]
3. [Question 3] — Why: [one line]
…

## Structural concerns
1. **Assumption:** [one sentence]
   - **Why this lens probes it:** [one or two sentences]
   - **Pivot question:** [the question that exposes whether the assumption holds]
2. …

## Evidence demand
| Evidence item            | User has? | Notes                              |
|--------------------------|-----------|------------------------------------|
| [e.g., NRR by cohort]    | Yes       | [where it is]                      |
| [e.g., named comparables]| No        | [what's missing and why it matters]|
| …                                                                       |

## Framing mismatches
1. **User says:** "[user's phrasing]"
   **Lens hears / would reframe as:** "[lens's phrasing]"
   **Why it matters:** [the question that the substitution surfaces]
2. …

## In the lens's voice

**What would persuade me:**
> [paragraph in the lens's voice describing the case that would win the conversation, naming the strongest required evidence]

**What would harden my objection:**
> [paragraph in the lens's voice naming the move or answer that would end the conversation as a "no"]

## Calibration
- Confidence in emulation: [high / medium / low]
- Largest fidelity gap: [single knowledge gap that most limits the emulation]
- Recommended next step: [what the user should do before re-running this prompt or before the actual conversation]
```

---

## Verification

- [ ] Lens is specified with role, seniority, environment, and primary success metric — not just a job title.
- [ ] First-10-minute questions are ordered by disqualification power.
- [ ] At least 3 structural concerns are present, each with an attack rationale and a pivot question.
- [ ] Evidence demand table lists every evidence item with a yes/no on whether the user already has it.
- [ ] Framing-mismatch section uses the user's actual phrasing, not paraphrase.
- [ ] Persuasion and hardened-objection paragraphs are written in the lens's voice, not the user's.
- [ ] Calibration note states confidence and names the single largest fidelity gap.
- [ ] No fabricated named precedents (deals, cases, studies attributed to the lens).
- [ ] Lens is not silently aligned with the user's current leaning.

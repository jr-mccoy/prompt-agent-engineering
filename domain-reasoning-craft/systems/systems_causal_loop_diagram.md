---
title: "Causal Loop Diagram — Map Reinforcing and Balancing Feedback"
category: reasoning-craft/systems
description: "Translate a problem description into a causal loop diagram with named variables, signed influence links (+/−), explicit feedback loops (R for reinforcing, B for balancing), delays, and external drivers. Surfaces feedback structure that point-thinking misses, so interventions can be designed against system behavior, not symptoms."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - systems-thinking
  - causal-loop-diagram
  - feedback-loops
  - dynamics
  - reinforcing-balancing
updated: "2026-05-10"
reasoning:
  styles: [systems, causal, structural]
  stakes: variable
  horizon: months_to_years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: variable_link_loop_table_plus_text_diagram
  user_role: [analyst, founder, executive, policy, researcher, operator]
  mode: [audit, synthesize, diagnose]
related_prompts:
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
  - domain-deep-analysis/deepthink_problem_analysis.md
---

# Causal Loop Diagram

**Objective:** Translate a problem description into a causal loop diagram (CLD): named variables, signed influence links, explicit feedback loops marked **R** (reinforcing) or **B** (balancing), delays, and external drivers (variables affecting the system but not affected by it). Output as a structured variable/link/loop table plus a text-render of the diagram. Designed for asynchronous use without diagramming tools.

**When to use:**
- The problem behaves dynamically over time and point-thinking ("X causes Y") doesn't explain why interventions backfire.
- An organization or system shows persistent oscillation, exponential growth/decay, or fixes-that-fail.
- Stakeholders disagree about cause-effect; making the loops explicit surfaces the disagreement.
- Designing an intervention and you want to predict where it will be absorbed by balancing loops or amplified by reinforcing ones.

**When NOT to use:**
- The problem is genuinely linear cause-effect with no feedback. CLDs add noise.
- You have time-series data and need quantitative simulation. CLDs are qualitative; for quantification use stock-and-flow + a simulator.
- Time pressure is acute. Building a defensible CLD takes 30–90 minutes.

**Audience:** Strategists, founders, operators, policy people, analysts working on dynamic systems where feedback is the cause of the behavior.

---

## Inputs / Context

1. **The dynamic problem.** A behavior over time that needs explaining ("Hiring grows, then collapses every 18 months"; "Lead quality keeps degrading despite ranking changes"). Include time-series description if available.
2. **Boundary.** What is inside the system you're modeling vs outside (external drivers)?
3. **Time horizon.** Over what period does the behavior unfold?
4. **Stakeholders / actors.** Whose decisions and behaviors are part of the loops?
5. **Existing interventions tried.** What's been done, what happened. Past failed interventions often diagnose the loop structure.

---

## Constraints

### Must
- Name 5–15 variables. Variables must be quantities that can change over time (use noun phrases: "lead quality", "team morale", "hiring velocity"). Avoid actions and decisions as variables.
- Each link gets a sign: `+` (variables move in the same direction) or `−` (variables move in opposite directions).
- Identify at least one closed feedback loop. Mark each loop **R** (reinforcing — net effect amplifies the behavior) or **B** (balancing — net effect dampens or reverses the behavior).
- Mark significant **delays** on every affected link: record magnitude in the Links table's Delay column and annotate `[delay: short/medium/long]` on the link in the text render.
- Distinguish internal variables (inside the system, change endogenously) from **external drivers** (affect the system, not affected by it).
- For each loop, write a one-sentence story: "When X goes up, Y goes up after delay D, which causes Z to go down…"
- End with a **dynamic explanation** of the observed behavior in terms of which loops are dominant when.

### Must Not
- Build a giant diagram with no loops. Without loops, it isn't a CLD; it's a tree.
- Confuse correlation with causation. Each link should pass a "would Y change if X were intervened on" test.
- Use actions ("hire more people") as variables. Use the quantities the actions affect ("hiring rate", "team size").
- Hand-wave delays. Either include them with magnitude, or explicitly note "delay assumed negligible."
- Skip the dynamic explanation. The diagram is a tool; the explanation is the deliverable.

---

## Instructions

### Step 1 — State the dynamic behavior
Describe the time-series pattern: growth, decay, oscillation, S-curve, overshoot-and-collapse, problem-returns-worse (the fixes-that-fail signature), winner-take-all divergence (the success-to-the-successful signature). Sketch what the curve looks like over time.

### Step 2 — Define system boundary
- What's inside (will be modeled with variables and links)?
- What's outside (external drivers, will appear as inputs to internal variables)?
- Justify the boundary: anything outside should not be plausibly affected by anything inside.

### Step 3 — Identify variables
List 5–15 variables. Each:
- Noun phrase
- Can be measured or imagined as a number that goes up or down over time
- Internal (endogenous) or external driver

### Step 4 — Draw causal links
For each pair of variables that have a direct causal influence:
- From → To
- Sign: `+` (same direction) or `−` (opposite direction)
- Delay: short / medium / long, or `none`
- Justification: one sentence

### Step 5 — Find loops
Walk the link graph for closed cycles. For each loop:
- List the variables in order
- Determine sign by counting `−` links: even number = **R** (reinforcing); odd = **B** (balancing)
- Estimate dominance: when is this loop in control of the system behavior?

### Step 6 — Loop stories
For each loop, write a one-sentence narrative: "Reinforcing loop R1: as customer count grows, word-of-mouth grows, which after a delay drives more customer count — this is what produces the early growth phase."

### Step 7 — Dominance shifts
Identify which loop dominates when. Many systems show **shifts in loop dominance** — early growth driven by R loops, then B loops (capacity limits, saturation, competition response) take over and produce S-curves or collapses.

### Step 8 — Dynamic explanation
Explain the observed behavior in terms of:
- Which loops are dominant in each phase
- Where delays cause oscillation (overshooting and correcting)
- What external drivers shift loop dominance
- Why prior interventions succeeded or failed (often: they targeted symptoms, leaving loop structure intact)

### Step 9 — Intervention candidates (optional)
For each candidate intervention, predict its effect via the loop structure:
- Which loop does it strengthen or weaken?
- Will balancing loops absorb it?
- Will reinforcing loops amplify it?
- Where does delay matter for timing?

(For full intervention design, hand off to `systems_unintended_consequence_scan.md`.)

---

## False-Positive Prevention

1. **Decision-as-variable.** "Hire more engineers" is a decision, not a variable. The variable is "engineering team size" or "hiring rate." Decisions enter as external interventions on variables.
2. **Linear-tree disguise.** A CLD with no loops is a causal chain. Either the system genuinely has no feedback (in which case CLD is the wrong tool), or you missed a loop. Look for loops involving stakeholder responses, market responses, customer behavior changes.
3. **Sign confusion.** A `+` link does not mean "good" or "increases over time". It means: when X increases, Y increases (or when X decreases, Y decreases) holding other variables constant. Re-test each sign with this definition.
4. **Loop-counting errors.** Number of `−` links determines loop type: even = R, odd = B. Recount if the loop story doesn't match the math.
5. **Missed delays.** Most fixes-that-fail behavior comes from delayed balancing loops. If your diagram has no delays, you're probably missing the dynamic that makes the system interesting.
6. **Over-reach on dominance claims.** Loop dominance shifts are hard to determine without simulation. State them as hypotheses and flag low confidence.
7. **External drivers smuggled inside.** If an "external" driver is actually affected by internal variables on a longer timescale, you've misdrawn the boundary; surface and decide whether to expand the model.
8. **Diagram theater.** A diagram without a dynamic explanation is decoration. Force the explanation step.

---

## Output Format

```
# Causal loop diagram — [system / problem]

## Dynamic behavior to explain
[Description of the time-series pattern, e.g., "S-curve growth followed by 12-month plateau and 18-month decline"]

## System boundary
- Inside (modeled): [list]
- Outside (external drivers): [list with one-line justification each]

## Variables
| # | Variable               | Type     | Notes                  |
|---|------------------------|----------|------------------------|
| 1 | [noun phrase]          | internal |                        |
| 2 | [noun phrase]          | external |                        |
| … |                        |          |                        |

## Links
| # | From → To              | Sign | Delay      | Justification           |
|---|------------------------|------|------------|-------------------------|
| 1 | A → B                  | +    | none       | [one line]              |
| 2 | B → C                  | −    | medium     | [one line]              |
| 3 | C → A                  | +    | long       | [one line]              |
| … |                        |      |            |                         |

## Loops
### Loop R1 (reinforcing)
- Variables: A → B → … → A
- Sign count: 0 negatives → R
- Story: [one sentence]
- Dominance: [when in control of behavior]

### Loop B1 (balancing)
- Variables: …
- Sign count: 1 negative → B
- Story: [one sentence]
- Dominance: [...]

(Repeat for each loop.)

## Text diagram
```
   [A] --(+)--> [B]
       ^         |
       |         (-) [delay: medium]
       |         v
   [C] <--(+)-- [B]   (Loop B1)
```

## Dynamic explanation
[2–4 paragraphs explaining the observed behavior in terms of dominance shifts, delays, and external drivers. Where prior interventions succeeded or failed and why.]

## Intervention sketch (optional)
| Candidate intervention | Affects loop | Predicted absorbed/amplified | Timing concern |
|------------------------|--------------|------------------------------|----------------|
| [name]                 | B1           | absorbed by R2 within 6mo    | yes — delay    |
```

---

## Verification

- [ ] 5–15 variables, all noun phrases (no decisions/actions).
- [ ] Internal vs external clearly labeled.
- [ ] Every link has a sign, delay marker, and justification.
- [ ] At least one closed loop, marked R or B based on sign count.
- [ ] Each loop has a one-sentence story.
- [ ] Delays are explicit (with magnitude) or noted as negligible.
- [ ] Dynamic explanation references loop dominance and delays.
- [ ] Text diagram renders the structure recognizably.
- [ ] No correlation-as-causation links.
- [ ] No diagram without dynamic explanation.

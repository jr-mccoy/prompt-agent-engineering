---
title: "How Might We — Turn a Problem Statement into Ideation-Ready Questions"
category: ideation/reframing
description: "Convert a raw problem, complaint, or research insight into a ranked set of 'How might we…' questions, each sized so it invites many answers without dictating one. Generates HMWs along eight deliberate reframing moves, tests each for too-narrow (solution baked in) and too-broad (unanswerable), and picks 2–3 to ideate against. Distinct from ideation_jobs_to_be_done_reframe.md (which replaces a solution-shaped brief with the customer's job) and ideation_inverse_problem.md (which flips the goal to its opposite); this prompt produces the question an ideation session answers."
techniques:
  - ST-01
  - DP-10
  - DD-02
  - CM-03
  - QA-01
difficulty: beginner
tags:
  - ideation
  - how-might-we
  - problem-framing
  - reframing
  - design-thinking
  - workshop-prep
updated: "2026-09-24"
reasoning:
  styles: [divergent, reframing, generative]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, founder, facilitator, strategist, individual]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_inverse_problem.md
  - domain-ideation/ideation_jobs_to_be_done_reframe.md
  - domain-ideation/ideation_forced_quantity_100_ideas.md
---

# How Might We — Turn a Problem Statement into Ideation-Ready Questions

**Objective:** Take a raw problem statement, user complaint, or research insight and produce a set of "How might we…" (HMW) questions that are each the right size to ideate against: open enough that a room could generate twenty different answers, specific enough that those answers would actually address the problem. The prompt generates HMWs along deliberate reframing moves rather than by paraphrase, tests every candidate against the two classic failure modes (a solution hidden in the question; a question so broad nobody can start), and ends by choosing the 2–3 questions worth spending an ideation session on.

The value is upstream: most weak brainstorms are weak because the question was wrong. A good HMW is the cheapest intervention in the whole divergence-convergence chain.

---

## When to Use

- You have an insight ("new users abandon at the permissions screen") and need to turn it into something a group can brainstorm on.
- A brief arrives as a solution ("add a chatbot") and you want to recover the problem underneath before ideating.
- You are preparing a workshop and need the prompt questions for each breakout.
- Ideas keep coming out the same shape and you suspect the question, not the people.

**Distinct from:**
- `domain-ideation/ideation_jobs_to_be_done_reframe.md` — replaces a solution-shaped brief with the job the customer is hiring for, then ideates per job. Use it when the *form* of the solution is the suspect assumption; use HMW when you already know the problem and need a well-sized question.
- `domain-ideation/ideation_inverse_problem.md` — inverts the goal ("how would we guarantee failure?"). HMW's "flip" move borrows the idea, but inverse-problem runs the whole sprint on the inversion.
- `domain-agentic-resources/skills/non-coding/creative/idea-divergence-convergence/SKILL.md` — runs a full diverge/converge cycle with one HMW as step one. This prompt is the deep version of that step.

**When NOT to use:**
- You have no evidence the problem exists. Framing a question sharply around an unvalidated problem only makes the wrong work more efficient; validate first.
- The decision is already framed and you need options compared — use `domain-decision-making/`.

---

## Inputs / Context

1. **The problem or insight.** One to three sentences, in the user's words. Include the evidence behind it if any exists.
2. **Who experiences it.** The person or group whose situation the HMW should improve.
3. **The desired outcome.** What would be different if this were solved.
4. **Known constraints.** Real limits (budget, regulation, platform) the answers must respect.
5. **Solutions already on the table.** So the HMWs can be checked for smuggling one of them in.

---

## Method

### Step 1 — Restate the point of view
Write one sentence in the form: *[person] needs [need] because [insight]*. If you cannot fill all three slots from the inputs, ask for the missing one rather than inventing it.

### Step 2 — Generate HMWs along eight reframing moves
Produce at least one HMW per move (10–16 total). The moves force different angles rather than rewordings:
1. **Amplify the good** — build on what already works.
2. **Remove the bad** — eliminate the pain directly.
3. **Explore the opposite** — make the negative the value.
4. **Question an assumption** — drop something the brief takes for granted.
5. **Change an adjective** — replace "fast" with "calm", "cheap" with "trusted".
6. **Borrow a resource** — use something already present in the situation.
7. **Shift the person** — reframe for a different stakeholder in the same situation.
8. **Break the point of view into pieces** — address one component of the need.

### Step 3 — Size-test every HMW
Mark each as **too narrow** (names or implies a specific solution), **too broad** (no one could start answering it Monday), or **right-sized**. For each failing HMW, write the corrected version beside it; keep both so the reasoning is visible.

### Step 4 — Check the verb and the outcome
A right-sized HMW has an action verb, a named beneficiary, and an outcome that could be observed. Rewrite any that end in abstractions ("improve the experience").

### Step 5 — Solution-smuggling check
Compare each surviving HMW against the solutions already on the table. If an HMW can only reasonably be answered by one of them, it is narrow in disguise; widen it.

### Step 6 — Pick 2–3 to ideate against
Score survivors on: coverage of the original need, number of distinct answer directions it invites (estimate by sketching three quick, different answers), and fit to constraints. Choose 2–3. Record why the runners-up lost.

### Step 7 — Hand off
Pair each chosen HMW with a suggested divergence prompt from this domain (e.g., `ideation_forced_quantity_100_ideas.md` for breadth, `ideation_crazy_eights.md` for a timed round).

---

## Output Format

```
# HMW set — [problem in five words]

## Point of view
[person] needs [need] because [insight]

## Generated HMWs
| # | Move | HMW | Size | Corrected version (if failed) |
|---|------|-----|------|-------------------------------|

## Survivors (right-sized, verb + beneficiary + observable outcome)
1. ...

## Chosen (2–3)
| HMW | Coverage | Answer directions (3 sketches) | Constraint fit | Next prompt |

## Runners-up and why they lost
- ...
```

---

## Verification

- [ ] Point-of-view sentence has all three slots filled from the inputs, none invented.
- [ ] At least one HMW per reframing move; no two HMWs are rewordings of each other.
- [ ] Every HMW labelled narrow / broad / right-sized, with corrections shown.
- [ ] No chosen HMW is answerable by only one solution already on the table.
- [ ] Each chosen HMW has three sketched answers in genuinely different directions.
- [ ] Chosen set is 2–3, each paired with a divergence prompt.

---

## False-Positive Prevention

1. **Paraphrase posing as reframing.** "How might we speed up onboarding" and "how might we make onboarding faster" are one HMW. Each move must change the angle, not the wording.
2. **The solution in a question costume.** "How might we add a progress bar to onboarding?" is a feature request. If the question names a mechanism, it is too narrow.
3. **The mission statement.** "How might we delight every user?" passes grammar and fails usefulness. If no one could start on it Monday, it is too broad.
4. **An invented insight.** Do not fabricate the "because" in the point of view. An HMW built on a guessed cause frames the session around the guess.
5. **Counting HMWs as progress.** Twenty HMWs are not twenty ideas; they are twenty candidate questions. The deliverable is the 2–3 chosen.
6. **Choosing by elegance.** The best-sounding HMW is not the best one. Choose by coverage and answer-direction count, and show the sketches.
7. **Dropping the beneficiary.** "How might we reduce churn" helps the company, not a person. Name who is better off.

---

## Example

**Input:** "Support tickets show new customers of our invoicing tool abandon setup when asked to connect their bank. Solutions floated: a video tutorial, a skip button."

**Point of view:** Sole-trader customers need to see value before trusting us with bank access because they have never heard of us and the permission screen arrives first.

**Selected generated HMWs:**
| Move | HMW | Size |
|------|-----|------|
| Remove the bad | HMW add a video explaining bank access? | Too narrow — this is the tutorial → *HMW make bank access feel safe to a first-time user?* |
| Question an assumption | HMW let customers send a real invoice before connecting a bank? | Right-sized |
| Explore the opposite | HMW make connecting the bank the moment customers feel most in control? | Right-sized |
| Shift the person | HMW help a customer's accountant set up the bank link for them? | Right-sized |
| Amplify the good | HMW improve onboarding? | Too broad → *HMW let new customers reach their first sent invoice within ten minutes?* |

**Chosen:** (1) "send a real invoice before connecting a bank" — three sketches: manual payment details, a pay-link without bank sync, a sandbox invoice to themselves; not answerable only by the skip button. (2) "make connecting the bank the moment customers feel most in control" — sketches: read-only first, revocable in one click, shown what we will never do. Hand-off: `ideation_crazy_eights.md` for both.

**Runner-up lost:** the accountant HMW — strong, but applies to a minority segment; revisit if segment data supports it.

---

## Techniques Used

- **ST-01 Clear Objective Statement** — the point-of-view sentence anchors every HMW.
- **DP-10 Reframe Generation** — the eight moves force genuine reframes rather than paraphrases.
- **DD-02 Vague-to-Concrete Translation** — too-broad HMWs are rewritten until someone could start Monday.
- **CM-03 Scope Definition** — the narrow/broad size test is an explicit scope check.
- **QA-01 Self-Verification** — solution-smuggling and three-sketch checks before choosing.

---

## Related Prompts

- `domain-ideation/ideation_inverse_problem.md` — run a whole sprint on the inverted goal.
- `domain-ideation/ideation_jobs_to_be_done_reframe.md` — when the solution form itself is the suspect assumption.
- `domain-ideation/ideation_forced_quantity_100_ideas.md` — breadth ideation against a chosen HMW.

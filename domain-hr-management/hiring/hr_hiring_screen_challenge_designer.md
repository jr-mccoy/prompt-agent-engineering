---
title: "Hiring Screen / Take-Home Challenge Designer — Role-Specific, Time-Boxed, Rubric-Scored"
category: hr-management/hiring
description: "Design a fair, role-specific hiring screen or take-home challenge: a realistic scenario, scoped deliverables, an explicit time-box, a weighted scoring rubric with level descriptors, and anti-bias safeguards. Refuses to produce unpaid production work or challenges that exceed a reasonable time-box."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - hiring
  - take-home
  - assessment
  - scoring-rubric
  - anti-bias
  - candidate-experience
updated: "2026-06-07"
related_prompts:
  - domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

# Hiring Screen / Take-Home Challenge Designer

**Objective:** Produce a role-specific hiring screen or take-home challenge that is realistic, fairly scoped, and consistently gradable — a scenario, scoped deliverables, an explicit time-box, a weighted scoring rubric with per-level descriptors, and anti-bias safeguards — while refusing to generate challenges that demand unpaid production work or exceed a reasonable time-box.

**When to Use:**
- You need a take-home, work-sample, or live exercise to assess candidates for a specific role.
- Your current screen is inconsistently graded, takes too long, or has produced biased or noisy outcomes.
- You want a defensible, rubric-based assessment that multiple interviewers can score the same way.
- You are replacing a "build us a feature" task with something fair and time-bounded.

**When NOT to use:**
- You need a full interview loop design (phone screen + onsite + references) — this covers one assessment instrument, not the whole process.
- You need a calibration/leveling session for existing employees — route to `hr_calibration_facilitator.md`.
- You are evaluating an AI system's output rather than a human candidate — route to `correctness_eval_design_prompt.md`.
- The role is regulated/licensed and the assessment must follow a statutory standard — defer to that standard; this prompt does not override it.

**Audience:** Hiring managers, recruiters, technical/functional interviewers, people-ops and talent teams designing assessments.

---

## Inputs / Context

Provide what you have; the prompt elicits the rest before producing the challenge.

1. **Role & level:** title, seniority (e.g. junior / mid / senior / staff), function.
2. **Core competencies to assess:** the 3–6 skills that actually predict success in this role.
3. **Where in the funnel** this sits (initial screen vs. final-round) and how many candidates it gates.
4. **Real day-to-day work:** what this person will actually do, so the scenario is representative.
5. **Time-box you intend** (and whether it is paid).
6. **Format:** take-home, live exercise, pair session, async write-up.
7. **Constraints:** tooling allowed, accessibility needs, legal/jurisdiction notes, panel size for review.
8. **Known failure modes** of your past screens (too long, too vague, gameable, biased).

If role, level, or the competencies to assess are missing, **ask up to 3 clarifying questions before producing the challenge** — do not guess on these.

---

## Constraints

### Must
- **Cap the time-box.** Default ceiling: **2–3 hours** of candidate effort for a take-home; **45–90 minutes** for a live exercise. State the cap explicitly and design the deliverables to fit it. If the user requests more, push back and propose a scoped-down version.
- **Assess the role's real competencies** — every scored criterion must map to a skill the job actually requires.
- **Make the scenario realistic but synthetic** — representative of the work, but using fictional/sample data, never the company's live backlog or unsolved production problems.
- **Provide a weighted scoring rubric** with named criteria, weights summing to 100%, and **per-level descriptors** (e.g. 1–4 or Below / Meets / Exceeds) so two reviewers grade alike.
- **Build in anti-bias safeguards:** calibration notes, blind-review guidance, structured (not gut-feel) scoring, and an accommodation note.
- **State what is explicitly NOT being assessed**, to prevent reviewers penalizing irrelevant style/format choices.
- **Label confidence / open assumptions** (QA-04) where the design depends on inputs the user didn't supply.

### Must Not
- **Do not produce unpaid production work.** The challenge must not ask candidates to solve the company's real, currently-open problems, build shippable features the company will use, or deliver assets of commercial value. If the request implies this, refuse and redirect to a synthetic equivalent.
- Do not exceed the time-box ceiling, or design deliverables that can't realistically be completed within the stated cap.
- Do not include criteria that proxy for protected characteristics, "culture fit" as a vibe, or pedigree (school/brand).
- Do not write rubric levels so vague they collapse to reviewer taste ("good," "strong," "impressive").
- Do not bury an implicit much-larger ask inside an innocuous-looking prompt.
- Do not assume a single "right" answer for open-ended roles — score reasoning and tradeoffs, not a fixed solution.

---

## Instructions

1. **Confirm role, level, and competencies.**
   - Restate the role and seniority, then list the **3–6 core competencies** the challenge will assess. If not supplied, infer candidates and ask.
   - For each competency, note *why it predicts on-the-job success* — this becomes the rubric's spine and the anti-bias justification.

2. **Set and defend the time-box.**
   - Choose a cap within the ceilings above based on level and funnel position. State it in candidate-facing language ("This should take about 2 hours; please don't spend more.").
   - If paid, state the rate/terms. If unpaid, ensure the scope is small enough that unpaid is defensible (a short exercise, not production work).
   - **Right-size the deliverables to fit the cap** — explicitly cut anything that won't fit.

3. **Design the scenario (realistic but synthetic).**
   - Write a brief, concrete scenario mirroring real work, using **fictional data/context**. Provide any inputs the candidate needs (sample dataset description, mock brief, stub repo) so they aren't blocked on setup.
   - State the **deliverable(s)** precisely and how they'll be submitted.
   - State **what candidates may use** (any tools, AI assistants, references) — be explicit, since ambiguity penalizes honest candidates.

4. **Build the weighted scoring rubric (DS-01).**
   - Define **3–6 scoring criteria**, each mapping to a competency, with **weights summing to 100%**.
   - For each criterion, write **per-level descriptors** at each scale point (recommend a 1–4 scale: 1 = Below bar, 2 = Approaching, 3 = Meets bar, 4 = Exceeds) — concrete, observable behaviors, not adjectives.
   - Define the **overall decision rule** (e.g. weighted score threshold to advance; any criterion at level 1 = auto-discuss).

5. **Add anti-bias safeguards.**
   - **Calibration note:** how reviewers align before scoring (score one sample together; agree on what a "3" looks like).
   - **Blind-review guidance:** strip name/identifying info where feasible; score criterion-by-criterion across candidates rather than candidate-by-candidate.
   - **Structured scoring:** each reviewer scores independently with the rubric before discussing; require written evidence per score.
   - **Accommodation note:** how candidates request adjustments (time, format) without penalty; assess the competency, not the medium.
   - **What is NOT assessed:** list irrelevant factors reviewers must ignore (formatting polish, tooling preference, accent/grammar where not job-relevant).

6. **Write the candidate-facing brief.**
   - Produce the exact text the candidate receives: scenario, deliverables, time-box, what's allowed, submission instructions, and the criteria they'll be judged on (publishing the rubric criteria improves fairness and signal).

7. **Self-check before reporting (QA-04).**
   - Confirm deliverables fit the time-box, every criterion ties to a competency, no production work is requested, and weights sum to 100%.
   - Flag assumptions made from missing inputs and assign an overall confidence level.

---

## False-Positive Prevention

1. **Disguised unpaid labor.** The most serious failure: a "challenge" that is actually the company's real open work (fix this live bug, design our actual onboarding flow, write copy we'll ship). Always check whether the deliverable has commercial value to the company; if so, synthesize it. Refuse production-work requests.
2. **Time-box creep.** "Just a small project" routinely balloons to 10+ hours. Estimate realistic completion time for each deliverable and cut scope until it fits the cap — then say the cap out loud to candidates.
3. **Rubric-as-vibes.** "Strong," "impressive," "good engineering sense" are not levels. Each scale point must describe observable behavior so two reviewers converge.
4. **Competency drift.** A criterion that doesn't map to a real job skill (e.g. grading a backend role on slide-deck aesthetics) is noise and a bias vector. Every criterion traces to a stated competency.
5. **Single-right-answer bias.** For open-ended roles, scoring against one expected solution penalizes valid alternative approaches. Score reasoning, tradeoffs, and judgment.
6. **Hidden bias proxies.** "Culture fit," pedigree, communication "polish," or tooling preference smuggle in bias. Name these in the "NOT assessed" list.
7. **Accommodation as afterthought.** Omitting an accommodation path disadvantages disabled and neurodivergent candidates. Include it by default.
8. **Ambiguous AI/tool rules.** Not stating whether AI assistants are allowed penalizes honest candidates and rewards quiet rule-breakers. State the policy explicitly.

---

## Output Format

```
# Hiring Challenge — [role], [level]

## 1. Competencies assessed
- [Competency] — predicts success because [reason]
- ... (3–6)

## 2. Format & time-box
- Format: [take-home / live / pair / async]
- Time-box: [cap] — paid? [yes/terms | no, justified by scope]
- Funnel position: [screen / final round]

## 3. Candidate-facing brief
**Scenario:** [realistic, synthetic context]
**You will deliver:** [precise deliverable(s)]
**Provided to you:** [sample data / stub / mock brief]
**You may use:** [tools, references, AI policy — explicit]
**Time guidance:** "This should take about [cap]; please don't exceed it."
**Submit by:** [method/deadline]
**You'll be evaluated on:** [published rubric criteria]

## 4. Scoring rubric (weights sum to 100%)
| Criterion (→ competency) | Weight | 1 — Below | 2 — Approaching | 3 — Meets | 4 — Exceeds |
|--------------------------|--------|-----------|-----------------|-----------|-------------|
| [...]                    | [..%]  | [...]     | [...]           | [...]     | [...]       |
**Decision rule:** [threshold to advance; auto-discuss triggers]

## 5. Anti-bias safeguards
- Calibration: [how reviewers align first]
- Blind review: [what to strip; criterion-wise scoring]
- Structured scoring: [independent, evidence-backed, then discuss]
- Accommodations: [how to request, no penalty]
- NOT assessed (reviewers must ignore): [irrelevant factors]

## 6. Assumptions & confidence
- Assumptions from missing inputs: [...]
- Overall confidence: [High | Medium | Low]
```

---

## Verification

- [ ] Role, level, and 3–6 competencies confirmed; each criterion maps to a competency.
- [ ] Time-box stated and within ceiling (≤2–3h take-home / ≤45–90min live); deliverables fit it.
- [ ] No production work / no commercially valuable deliverable / no live company problem requested.
- [ ] Scenario is realistic but synthetic, with all needed inputs provided.
- [ ] AI/tool usage policy stated explicitly.
- [ ] Weighted rubric with weights summing to 100% and concrete per-level descriptors.
- [ ] Overall decision rule defined.
- [ ] Anti-bias safeguards present: calibration, blind review, structured scoring, accommodation, NOT-assessed list.
- [ ] Open-ended roles scored on reasoning/tradeoffs, not a single fixed answer.
- [ ] Assumptions flagged and an overall confidence level assigned.

---
title: "AI Research Scientist Role-Readiness Assessment"
category: "productivity/career"
description: "Run an 8-question structured interview to assess readiness for an AI Research Scientist role, then deliver a tiered verdict, a phased roadmap, tailored resources, and a verify-first salary reality check."
techniques:
  - ST-01
  - RT-01
  - DS-01
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - career
  - ai-roles
  - role-readiness
  - research
  - publications
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-personal-development/career-transformation/career_90_day_repositioning_plan.md
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-productivity/career/career_ai_strategist.md
---

# AI Research Scientist Role-Readiness Assessment

**Objective:** Assess a candidate's readiness for an AI Research Scientist role through a one-question-at-a-time structured interview, then return a single qualification verdict, a phased development roadmap, tailored resources, a verify-first compensation reality check, and one concrete next action.

**When to use:**
- You are a PhD student, postdoc, research engineer, or applied scientist eyeing a research-scientist role at an industry lab or university.
- You want an honest read on whether your publication record and technical depth meet the bar, and what to close.
- You want a personalized 30-day / 6–12-month / 1–2-year plan, not generic advice.

**When NOT to use:**
- You want feedback on a specific paper or proposal (different task).
- You want guaranteed salary numbers or a placement promise — this gives estimates to verify.
- You are assessing a different role (use the matching sibling prompt).

**Audience:** PhD candidates, postdocs, research engineers, and applied scientists targeting research-scientist positions in industry or academia.

---

## Inputs / Context

The model gathers these *through the interview*. Be ready to discuss:

1. **Educational foundation** — degree (PhD typically expected), institution, area of focus, thesis, advisor.
2. **Research experience** — years, areas, methodology (theoretical/empirical/applied), academic vs. industry, collaborations.
3. **Publications & academic impact** — count, venues (top-tier conferences), first-author vs. co-author, citations/h-index, awards.
4. **Deep technical expertise** — advanced math (linear algebra, optimization, probability, information theory), DL theory, a specific subfield, novel algorithm design.
5. **Programming & implementation** — languages (Python, C++, Julia), frameworks (PyTorch, TensorFlow, JAX), large-scale/distributed compute, implementing papers from scratch.
6. **Research philosophy & vision** — interests and why they matter, an open problem, identifying impactful directions, balancing rigor and impact.
7. **Collaboration & communication** — conference presentations, papers/grants, mentoring, cross-disciplinary work, explaining to non-experts.
8. **Goals & context** — preferred environment (industry/university/hybrid), geographic preferences, transition timeline, long-term vision.

---

## Constraints

### Must
- Ask exactly **one** interview question at a time and wait for the answer.
- Open with a brief introduction and a "Ready to begin? (yes/no)" gate.
- After all 8 answers, assign exactly **one** of four verdict tiers.
- Tie the roadmap, resources, and next action to the candidate's *specific* answers and stated goals.
- Present any salary range, equity figure, or competitiveness statistic as an **estimate** to verify against current market data (levels.fyi, Glassdoor, BLS, public faculty salary data, recent postings for the candidate's setting/location).
- Be realistic about the extreme competitiveness of research roles and that a PhD is effectively mandatory; publication record is the primary currency.

### Must Not
- Never present salary/equity figures, application-volume claims, or competitiveness statistics as verified current fact — label them as estimates and tell the user to verify.
- Never dump all 8 questions at once or pre-answer for the candidate.
- Never inflate a verdict to be encouraging given how selective these roles are.
- Never recommend a named lab, conference deadline, workshop, or paper you are not reasonably confident exists/is current; if unsure, describe the type and tell the candidate to confirm.

---

## Instructions

1. **Set role context.** Prime the model as an AI Research Scientist career advisor and paste the interview prompt below.
2. **Run the interview.** Answer one question at a time.
3. **Receive the assessment.** After question 8, the model produces verdict, roadmap, resources, salary reality check, and next action.
4. **Verify the numbers.** Treat all compensation, equity, and competitiveness figures as estimates to confirm against live sources.

Paste this verbatim:

```
You are an experienced AI Research Scientist career advisor who evaluates candidates
for research positions at top AI labs, universities, and research-focused companies.

TASK: Assess my readiness for an AI Research Scientist role via an 8-question interview,
then give me a tiered verdict and a personalized roadmap.

INTERACTION RULES:
- First, briefly introduce the process: 8 questions, asked ONE AT A TIME; each builds
  on the last; ~5-10 minutes; answer honestly. Then ask "Ready to begin? (yes/no)".
- Ask ONE question, then STOP and wait for my answer. Do not ask the next or answer for me.
- Be realistic about extreme competitiveness: a PhD is effectively mandatory and
  publication record is the primary currency. Do not inflate your assessment.

THE 8 QUESTIONS (ask in order, one at a time):
1. Educational foundation: degree (PhD typically required), institution, area of focus,
   thesis topic, advisor if relevant.
2. Research experience: (a) years, (b) areas, (c) methodology (theoretical/empirical/
   applied), (d) academic vs. industry, (e) collaborations and team experience.
3. Publications & academic impact: (a) number of papers, (b) venues (top-tier
   conferences), (c) first-author vs. co-author, (d) citations/h-index if applicable,
   (e) any awards or recognitions.
4. Deep technical expertise: rate 1-10 (a) advanced math (linear algebra, optimization,
   probability, information theory), (b) deep-learning theory, (c) a specific subfield
   (RL, generative models, meta-learning, etc.), (d) novel algorithm design. Describe
   your deepest area.
5. Programming & implementation: (a) languages (Python, C++, Julia), (b) DL frameworks
   (PyTorch, TensorFlow, JAX), (c) large-scale compute (multi-GPU, distributed training),
   (d) can you implement papers from scratch?
6. Research philosophy & vision: (a) your interests and why they matter, (b) an open
   problem you'd like to work on, (c) how you identify impactful directions, (d) how you
   balance rigor and practical impact.
7. Collaboration & communication: (a) presenting at conferences, (b) writing papers/
   grants, (c) mentoring, (d) cross-disciplinary collaboration, (e) explaining complex
   ideas to non-experts.
8. Goals & context: (a) preferred environment (industry lab/university/hybrid),
   (b) geographic preferences, (c) transition timeline, (d) long-term vision
   (professor, industry researcher, entrepreneur).

AFTER ALL 8 ANSWERS, produce:
1. ONE verdict tier: Qualified Now (75%+) / Nearly Qualified (50-74%) /
   Significant Gaps (25-49%) / Not Currently Viable (<25%). Justify against my answers.
   Note adjacent roles (ML engineer, applied scientist, research engineer) for lower tiers.
2. Roadmap: Next 30 days / 6-12 months / 1-2 years, as checkbox actions tied to my gaps.
3. Top 5 resources matched to MY gaps (no generic lists) — e.g. subfields/key papers to
   deepen, venues to target. If unsure a named lab/deadline/workshop/paper exists or is
   current, describe the type and tell me to confirm it.
4. Salary reality check for my setting/location — clearly labeled ESTIMATES I should
   verify against levels.fyi, Glassdoor, BLS, public faculty salary data, and recent
   postings. Cover industry vs. academia tradeoffs qualitatively. Do not state
   application-volume or competitiveness numbers as fact.
5. ONE single next action to do within 7 days.

Begin now by introducing yourself and the process.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Quote a salary or equity band as what the candidate "will" earn.
- State "top labs get thousands of applications per opening" or any volume figure as established fact.
- Mark someone "Qualified Now" without the publication record the role demands.
- Recommend a specific paper, lab, or conference deadline you cannot verify is current.
- Rush to the verdict before all 8 questions are answered.

✅ **DO:**
- Frame every comp/equity/competitiveness number as an estimate to verify against named live sources.
- Anchor the verdict to concrete evidence, weighting publications and technical depth.
- Point lower-tier candidates to adjacent roles (ML engineer, applied/research scientist) as a bridge.
- Flag uncertainty about any named lab, paper, or deadline rather than asserting it.
- Hold one question at a time and wait.

---

## Output Format

```
# AI Research Scientist Readiness — [candidate summary]

## Verdict: [Qualified Now / Nearly Qualified / Significant Gaps / Not Currently Viable]
- Why this tier (evidence from answers): ...
- Target setting / application or bridge strategy (adjacent roles if lower tier): ...

## Roadmap
Next 30 days:
- [ ] ...
6-12 months:
- [ ] ...
1-2 years:
- [ ] ...

## Top 5 Resources (matched to your gaps)
1. ... (verify it currently exists / deadline is current)
...

## Salary Reality Check (ESTIMATES — verify before relying on them)
- Range for your setting/level/location (industry vs. academia): ~$X-$Y  [estimate; confirm via levels.fyi / Glassdoor / BLS / public faculty data / current postings]
- Industry vs. academia tradeoffs: ...

## Your Single Next Action (within 7 days)
- ...
```

---

## Verification

- [ ] Introduction given and "Ready to begin?" gate honored.
- [ ] All 8 questions asked one at a time, each waiting for an answer.
- [ ] Exactly one verdict tier assigned and justified from the answers.
- [ ] Roadmap, resources, and next action are specific to the candidate.
- [ ] Every salary/equity/competitiveness figure labeled an estimate with named sources to verify.
- [ ] Publication record and technical depth weighted; no unverifiable lab/paper/deadline asserted as fact.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as a readiness assessment ending in a tiered verdict and roadmap.
- **RT-01 (Role/Expertise Priming):** Casts the model as an AI Research Scientist career advisor to calibrate to the role's selectivity.
- **DS-01 (Input Specification):** Defines the eight dimensions the interview must elicit, weighting publications and technical depth.
- **QA-04 (Uncertainty Acknowledgment):** Forces salary/equity/competitiveness figures to be labeled estimates and unverifiable labs/papers/deadlines to be flagged.
- **CM-02 (Explicit Constraints):** Enforces one-question-at-a-time flow, the four-tier verdict, the selectivity calibration, and anti-fabrication rules.

---

## Related Prompts
- `domain-personal-development/career-transformation/career_90_day_repositioning_plan.md` — convert the roadmap into a concrete 90-day repositioning plan.
- `domain-personal-development/career-transformation/career_residual_skills_inventory.md` — inventory the durable research/judgment skills you bring.
- `domain-productivity/career/career_ai_strategist.md` — a sibling assessment if a strategy-facing AI path is also of interest.

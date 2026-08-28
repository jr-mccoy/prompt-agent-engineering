---
title: "AI Governance Specialist Role-Readiness Assessment"
category: personal-development/prompts/career
description: "Run an 8-question structured interview to assess readiness for an AI Governance Specialist role, then deliver a tiered verdict, a phased roadmap, tailored resources, and a verify-first salary reality check."
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
  - governance
  - risk
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-personal-development/career-transformation/career_90_day_repositioning_plan.md
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/prompts/career/career_ai_compliance.md
---

# AI Governance Specialist Role-Readiness Assessment

**Objective:** Assess a candidate's readiness for an AI Governance Specialist role through a one-question-at-a-time structured interview, then return a single qualification verdict, a phased development roadmap, tailored resources, a verify-first compensation reality check, and one concrete next action.

**When to use:**
- You have governance, risk, compliance, or policy experience and want to gauge readiness for AI governance work.
- You want to know which AI-technical or regulatory gaps to close, and on what timeline.
- You want a personalized 30-day / 3–6-month / 6–12-month plan, not generic advice.

**When NOT to use:**
- You need legal advice on a specific regulation (this is a career assessment, not legal counsel).
- You want guaranteed salary numbers or a placement promise — this gives estimates to verify.
- You are assessing a different role (use the matching sibling prompt).

**Audience:** Governance, risk, compliance, and policy professionals exploring a move into AI governance across tech, regulated industries, or consulting.

---

## Inputs / Context

The model gathers these *through the interview*. Be ready to discuss:

1. **Professional background** — current/recent role, years in governance/risk/compliance/policy.
2. **AI technical understanding** — how AI/ML systems work (training, inference, data pipelines), AI risks (bias, fairness, privacy, security, hallucinations), the development lifecycle.
3. **Regulatory knowledge** — EU AI Act, GDPR/data privacy, industry-specific AI regulations, risk frameworks (ISO, NIST AI RMF).
4. **Governance framework experience** — frameworks developed/implemented, your role, balancing risk vs. business objectives, policy/controls/audit.
5. **Risk assessment skills** — identification/assessment methodologies, documenting risks/mitigations, working with technical teams on vulnerabilities, stakeholder communication.
6. **Cross-functional collaboration** — engineering/data science, legal/compliance, executives, external auditors/regulators; navigating conflicting priorities.
7. **Documentation & communication** — policy/procedure writing, technical writing for diverse audiences, presenting to executives, training materials.
8. **Goals & context** — location, target industry, transition timeline, in-house vs. consulting.

---

## Constraints

### Must
- Ask exactly **one** interview question at a time and wait for the answer.
- Open with a brief introduction and a "Ready to begin? (yes/no)" gate.
- After all 8 answers, assign exactly **one** of four verdict tiers.
- Tie the roadmap, resources, and next action to the candidate's *specific* answers and stated goals.
- Present any salary range or market-demand figure as an **estimate** to verify against current market data (levels.fyi, Glassdoor, BLS, recent postings for the candidate's industry/location).

### Must Not
- Never present salary ranges, demand-growth percentages, or regulatory penalty figures as verified current fact — label them as estimates and tell the user to verify.
- Never give regulation-specific legal advice; describe what to learn and route specifics to qualified counsel.
- Never dump all 8 questions at once or pre-answer for the candidate.
- Never recommend a named certification, course, or organization you are not reasonably confident exists; if unsure, describe the type and tell the candidate to confirm.

---

## Instructions

1. **Set role context.** Prime the model as an AI governance career advisor and paste the interview prompt below.
2. **Run the interview.** Answer one question at a time.
3. **Receive the assessment.** After question 8, the model produces verdict, roadmap, resources, salary reality check, and next action.
4. **Verify the numbers.** Treat all compensation, demand, and penalty figures as estimates to confirm against live sources.

Paste this verbatim:

```
You are an experienced AI Governance career advisor who evaluates candidates for
governance, risk, and compliance roles in AI systems across tech companies,
consulting firms, and regulated industries.

TASK: Assess my readiness for an AI Governance Specialist role via an 8-question
interview, then give me a tiered verdict and a personalized roadmap.

INTERACTION RULES:
- First, briefly introduce the process: 8 questions, asked ONE AT A TIME; each
  builds on the last; ~5-10 minutes; answer honestly. Then ask "Ready to begin? (yes/no)".
- Ask ONE question, then STOP and wait for my answer. Do not ask the next or answer for me.
- Be realistic about the high demand but specific skill requirements; most roles are mid-to-senior.
- Do NOT give regulation-specific legal advice; point me to what to learn and to qualified counsel.

THE 8 QUESTIONS (ask in order, one at a time):
1. Professional background: current/recent role and years in governance, risk
   management, compliance, policy, or related fields.
2. AI technical understanding: rate 1-10 (a) how AI/ML systems work (training,
   inference, data pipelines), (b) AI risks (bias, fairness, privacy, security,
   hallucinations), (c) the AI development lifecycle. (No coding; conceptual fluency matters.)
3. Regulatory knowledge: familiarity with (a) EU AI Act, (b) GDPR/data-privacy laws,
   (c) industry-specific AI regulations, (d) risk frameworks (ISO, NIST AI RMF).
   Describe any direct compliance work.
4. Governance framework experience: frameworks developed/implemented — (a) for what
   systems/processes, (b) your role, (c) how you balanced risk vs. business objectives,
   (d) policy/controls/audit experience.
5. Risk assessment: (a) identification/assessment methodologies, (b) documenting
   risks & mitigations, (c) working with technical teams on vulnerabilities,
   (d) stakeholder communication about risk.
6. Cross-functional collaboration: with (a) engineering/data science, (b) legal/
   compliance, (c) executive leadership, (d) external auditors/regulators. Give an
   example of navigating conflicting priorities.
7. Documentation & communication: rate 1-10 (a) policy/procedure documentation,
   (b) technical writing for diverse audiences, (c) presenting governance topics to
   executives, (d) creating training materials. Examples if possible.
8. Goals & context: (a) location for salary calibration, (b) target industry,
   (c) transition timeline, (d) in-house vs. consulting.

AFTER ALL 8 ANSWERS, produce:
1. ONE verdict tier: Qualified Now (75%+) / Nearly Qualified (50-74%) /
   Significant Gaps (25-49%) / Not Currently Viable (<25%). Justify against my answers.
2. Roadmap: Next 30 days / 3-6 months / 6-12 months, as checkbox actions tied to my gaps.
3. Top 5 resources matched to MY gaps (no generic lists). If unsure a named cert/course/
   org exists, describe the type and tell me to confirm it.
4. Salary reality check for my industry/location — clearly labeled ESTIMATES I should
   verify against levels.fyi, Glassdoor, BLS, and recent postings. Note consulting and
   metro premiums qualitatively. Do not state regulatory penalty figures as fact.
5. ONE single next action to do within 7 days.

Begin now by introducing yourself and the process.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Call AI Governance "the hottest tech job" or cite a precise growth/penalty figure as fact.
- Quote a salary band as what the candidate "will" earn.
- Give specific legal interpretation of the EU AI Act or fine thresholds.
- Recommend a certification or body you cannot verify exists.
- Mark someone "Qualified Now" who lacks the AI-systems literacy the role requires.

✅ **DO:**
- Frame every comp, demand, and penalty number as an estimate to verify against named live sources.
- Anchor the verdict to concrete evidence from the candidate's answers.
- Tell the candidate which frameworks/regulations to study and route specifics to counsel.
- Flag uncertainty about any named resource rather than asserting it.
- Hold one question at a time and wait.

---

## Output Format

```
# AI Governance Specialist Readiness — [candidate summary]

## Verdict: [Qualified Now / Nearly Qualified / Significant Gaps / Not Currently Viable]
- Why this tier (evidence from answers): ...
- Target sectors / application or bridge strategy: ...

## Roadmap
Next 30 days:
- [ ] ...
3-6 months:
- [ ] ...
6-12 months:
- [ ] ...

## Top 5 Resources (matched to your gaps)
1. ... (verify it currently exists)
...

## Salary Reality Check (ESTIMATES — verify before relying on them)
- Range for your level/industry/location: ~$X-$Y  [estimate; confirm via levels.fyi / Glassdoor / BLS / current postings]
- Consulting / metro premiums: ...

## Your Single Next Action (within 7 days)
- ...
```

---

## Verification

- [ ] Introduction given and "Ready to begin?" gate honored.
- [ ] All 8 questions asked one at a time, each waiting for an answer.
- [ ] Exactly one verdict tier assigned and justified from the answers.
- [ ] Roadmap, resources, and next action are specific to the candidate.
- [ ] Every salary/demand/penalty figure labeled an estimate with named sources to verify.
- [ ] No legal advice given; no unverifiable named resources asserted as fact.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as a readiness assessment ending in a tiered verdict and roadmap.
- **RT-01 (Role/Expertise Priming):** Casts the model as an AI governance career advisor to calibrate to the role's specifics.
- **DS-01 (Input Specification):** Defines the eight dimensions the interview must elicit before judging.
- **QA-04 (Uncertainty Acknowledgment):** Forces salary/demand/penalty figures to be labeled estimates and unverifiable resources to be flagged.
- **CM-02 (Explicit Constraints):** Enforces one-question-at-a-time flow, the four-tier verdict, the no-legal-advice line, and anti-fabrication rules.

---

## Related Prompts
- `domain-personal-development/career-transformation/career_90_day_repositioning_plan.md` — convert the roadmap into a concrete 90-day repositioning plan.
- `domain-personal-development/career-transformation/career_residual_skills_inventory.md` — inventory the durable governance/judgment skills you bring.
- `domain-personal-development/prompts/career/career_ai_compliance.md` — the closely adjacent AI Compliance Manager assessment.

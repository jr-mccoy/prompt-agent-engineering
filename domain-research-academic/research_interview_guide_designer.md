---
title: "Interview Guide Designer — Semi-Structured Guide with Probes, Escalations, and Sensitive Transitions"
category: research-academic/qualitative
description: "Design a semi-structured interview guide for qualitative research. Produces opening / rapport block, themed core question modules with probes, escalation questions for thin answers, sensitive-topic transitions, closing questions, and a debrief structure. Includes pilot-and-iterate plan."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - qualitative-research
  - interview-guide
  - semi-structured
  - probes
  - rapport
updated: "2026-05-10"
reasoning:
  styles: [structured, qualitative, iterative]
  stakes: variable
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured_interview_guide
  user_role: [researcher, ux_researcher, journalist, ethnographer, hr]
  mode: [design, plan]
related_prompts:
  - domain-research-academic/research_qualitative_coding_scheme.md
  - domain-research-academic/research_question_formulation.md
  - domain-business-strategy/research/user_research_synthesis.md
---

# Interview Guide Designer

**Objective:** Design a semi-structured interview guide that elicits rich, comparable data across interviewees while leaving space for unexpected disclosures. Produce: opening / rapport block, 3–6 themed core question modules with probes, escalation questions for thin answers, sensitive-topic transitions, closing questions, and a post-interview debrief structure. Include a pilot-and-iterate plan.

**When to use:**
- Qualitative research interviews (academic, UX, market, journalistic).
- Internal user research where consistent comparison across N interviews matters.
- Ethnographic fieldwork.
- Sensitive-topic interviews (illness, conflict, failure, discrimination) where care in question construction is decisive.

**When NOT to use:**
- Structured surveys — use `research_survey_instrument_designer.md`.
- Casual conversation — guides over-formalize.
- One-shot expert interviews where the sequence depends entirely on what the expert raises.

**Audience:** Researchers, UX researchers, journalists, ethnographers, HR / org researchers.

---

## Inputs / Context

1. **Research question** the interviews serve.
2. **Target interviewees:** who, how recruited, expected number.
3. **Interview budget per session** (30, 60, 90 minutes).
4. **Mode:** in person, video, phone, async written.
5. **Sensitive topics involved.**
6. **Recording / consent context.**

---

## Constraints

### Must
- Open with **rapport-building** that does not require the interviewee to defend or explain anything.
- Sequence questions from **broad / safe** to **narrow / sensitive** — never lead with the hardest question.
- For each core question, include **probes** (follow-ups that deepen) and an **escalation** for thin answers.
- Use **open questions** for exploration; closed only for confirmation.
- For sensitive topics, design **transitions** that signal change in tone and offer interviewee control.
- Close with **catch-all questions** ("anything else?", "what didn't I ask that I should have?") — these often produce the highest-signal answers.
- Include a **debrief structure** for the interviewer immediately post-interview.
- Plan **pilot interviews** (2–3) before full deployment, with explicit revision criteria.

### Must Not
- Lead with the research question stated as a question to the interviewee.
- Embed assumptions in question phrasing ("how has X harmed you?" assumes harm).
- Stack double-barreled questions ("what was hard and how did you handle it?").
- Skip probes — the second-level answer is often where insight lives.
- Treat sensitive topics as ordinary — they need transitions and exit ramps.

---

## Instructions

### Step 1 — Map research question to interview themes
What 3–6 themes does the research question contain? Each becomes a question module.

### Step 2 — Opening / rapport block
- Welcome and consent confirmation
- Time check
- Brief restatement of purpose (what the interviewee will get out of it / what the research is for)
- 1–2 warm-up questions about something the interviewee can answer easily and with some autonomy ("tell me about your role" / "walk me through a typical day")

### Step 3 — Build core question modules
For each theme:
- **Anchor question** (open, broad)
- **Probes** (3–5: "tell me more about that", "what was that like", "can you give me an example", "what happened next", "what made you decide that")
- **Escalation** (if anchor returns thin answer): a more concrete reframe, often situational ("walk me through the last time that happened")
- **Pivot** to next theme

### Step 4 — Sensitive topic transitions
For modules touching sensitive material:
- Signal transition: "I want to ask about something more personal — feel free to share as much or as little as feels right"
- Provide an exit: "is this OK to discuss?"
- Soft entry: ask about the surrounding context before the central question
- Honor any avoidance: do not press past one signal of discomfort

### Step 5 — Closing questions
- Catch-all: "What didn't I ask about that I should have?"
- Forward-looking: "If you were doing this research, what would you ask?"
- Referral: "Who else should I be talking to?"
- Logistics: "Is it OK if I follow up by email?"

### Step 6 — Interviewer debrief structure
Immediately post-interview, capture:
- Overall impression
- 3 most striking quotes / moments
- Themes that emerged unexpectedly
- Body-language / tone notes (for in-person / video)
- Researcher reactions and biases noticed
- Questions to add or revise for next interview

### Step 7 — Pilot plan
- Run 2–3 pilots
- Revision criteria: questions that consistently confuse, questions that produce identical answers across interviewees (signaling priming), questions that take too long, sequence problems
- Approval to proceed to full deployment after pilot revision

### Step 8 — Time budget mapping
Map question modules to expected duration. Total should fit within session budget with 20% reserve for tangents.

---

## False-Positive Prevention

1. **Leading questions.** "How has X been a problem for you?" is leading. "Tell me about your experience with X" is open.
2. **Double-barreled.** Split into two questions if logically distinct.
3. **Probe-skip.** First answers are often surface-level; the 2nd or 3rd probe is where insight emerges.
4. **Sensitive-topic ambush.** Hard questions need transitions and exit ramps.
5. **Closing-question skip.** Catch-all closing produces the highest-signal answers in many studies.
6. **No pilot.** First-draft guides almost always need revision; deploying without piloting wastes early interviews.
7. **No debrief structure.** Memory degrades fast; structured debrief immediately post-interview captures what notes alone miss.
8. **Time-budget overrun.** Designing a 90-minute guide for a 60-minute slot.

---

## Output Format

```
# Interview guide — [research question]

## Logistics
- Mode: [...]
- Duration: [...]
- Recording: [yes/no, consent process]
- Compensation: [...]

## Opening / rapport (5 min)
- Welcome + consent confirmation
- Purpose restatement
- Warm-up: [...]

## Module 1: [theme name] (~10 min)
**Anchor:** [open question]
**Probes:**
- [...]
- [...]
- [...]
- [...]
**Escalation if thin:** [concrete reframe]
**Transition to next:** [...]

## Module 2: [theme name] (~10 min)
[Same structure]

## Module 3 [...]
[Same structure]

## Sensitive-topic module (if applicable)
**Transition in:** [signal + exit option]
**Soft entry:** [contextual question]
**Anchor:** [...]
**Probes:** [...]
**Honor avoidance:** if interviewee deflects, accept and move on.
**Transition out:** [grounding question]

## Closing (5 min)
- "What didn't I ask that I should have?"
- "If you were doing this research, what would you ask?"
- "Who else should I be talking to?"
- "OK to follow up by email?"

## Debrief (interviewer, immediately post)
- Overall impression: [...]
- 3 most striking quotes / moments: [...]
- Unexpected themes: [...]
- Body language / tone: [...]
- Researcher reactions / biases noticed: [...]
- Questions to add / revise: [...]

## Pilot plan
- N pilots: [2–3]
- Revision criteria: [confusing questions, leading effects, sequence issues, time]
- Approval to proceed: [...]

## Time budget
| Section | Planned | 
|---------|---------|
| Opening | 5       |
| Module 1| 10      |
| ...     | ...     |
| Closing | 5       |
| Reserve | 10      |
| **Total**| [matches session length] |
```

---

## Verification

- [ ] Opening builds rapport without requiring defense.
- [ ] Sequence flows safe → narrow → sensitive.
- [ ] Each anchor has 3–5 probes.
- [ ] Each module has an escalation for thin answers.
- [ ] Sensitive modules have transitions and exit ramps.
- [ ] Catch-all closing questions present.
- [ ] Debrief structure captures impressions, quotes, biases.
- [ ] Pilot plan with revision criteria.
- [ ] Time budget fits session length with reserve.
- [ ] No leading or double-barreled questions.

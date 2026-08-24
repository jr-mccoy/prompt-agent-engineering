---
title: "Customer Discovery Interview Protocol (JTBD + Mom Test)"
category: idea-to-product/validation
description: "Generate a 45-60 minute structured customer-discovery interview guide that probes past behavior (not hypothetical preferences), surfaces real demand signals, and avoids the leading questions that contaminate most founder interviews. Output: interview guide + scoring rubric for a 5-10 interview cohort."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - CM-02  # Must / Must Not Constraints
  - RT-05  # Interrogative Mode
  - DS-01  # Framework Application (JTBD + Mom Test)
  - QA-01  # Verification / Self-Check
difficulty: intermediate
tags:
  - customer-discovery
  - jobs-to-be-done
  - mom-test
  - validation
  - interview-design
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/stage-2-problem-validation/jobs_to_be_done_analysis.md
  - domain-idea-to-product/stage-2-problem-validation/value_proposition_canvas_analysis.md
  - domain-idea-to-product/stage-1-ideation/ideation_concept_legs_test.md
---

# Customer Discovery Interview Protocol (JTBD + Mom Test)

**Objective:** Produce a complete, ready-to-use customer-discovery interview guide for a specific problem hypothesis, structured to extract past-behavior evidence rather than hypothetical preferences. Output is a 45-60 minute interview script with question banks, anti-leading-question guardrails, and a post-interview scoring rubric the user can apply across 5-10 interviews.

## When to Use

- You have a problem hypothesis (validated lightly via concept-legs test) and want to test it with real prospective customers before building anything.
- You're about to do "customer interviews" but have read enough to know most founder interviews are useless because the founder pitches and asks leading questions.
- You want a repeatable instrument so you can compare results across 5-10 interviews and detect patterns vs. noise.

## Inputs

The user must provide:
1. **Problem hypothesis** (1-2 sentences): "I believe [user type] struggles with [problem] when [trigger context]."
2. **Customer segment** to interview: title, company stage, geography, any other filters.
3. **Idea exposure level**: do you want a "blind" interview (you never describe your solution) or a "two-phase" interview (problem-focused first half, solution-reaction second half)?
4. **Number of interviews planned** (5-10 recommended for pattern detection).

If any input is missing, ask. Do not invent a hypothesis.

## Constraints

**Must:**
- Generate at least 3 question banks per section so the interviewer can vary phrasing.
- Every question must probe **past behavior** ("last time you faced X, what did you actually do?") not hypothesis ("would you use a tool that...?").
- Include a "kill the pitch" rule: the interviewer must not describe the solution in phase 1.
- Provide a post-interview scoring rubric with 5-8 specific binary signals (yes/no), not vibe ratings.
- Include 2-3 explicit "anti-leading-question" examples per section showing what NOT to ask.
- End with a synthesis template for combining 5-10 interviews into a go/no-go signal.

**Must Not:**
- Include questions starting with "Would you..." or "Do you think..." (these invite lies).
- Recommend asking the user about pricing they'd pay (use willingness-to-pay proxies: what they currently spend, what they've switched away from).
- Promise the interview will yield a definitive verdict — be explicit that 5-10 interviews surface patterns, not statistical proof.
- Generate fluffy "rapport-building" questions that waste time. Get to behavior fast.

## Instructions

Produce the interview guide in this order:

### Section 1: Opening (3-5 minutes)
- Honest framing: "I'm researching how [target] handle [problem area]. I'm not selling anything. I want to learn from your experience."
- Permission to record (if applicable).
- One warmup question that anchors them in concrete context, not abstraction.

### Section 2: Context & Current State (10-15 minutes)
Question banks (3+ per topic):
- **Role & workflow:** What does a typical [week/sprint/quarter] look like for you? Walk me through the last time you did [activity].
- **Tools & spend:** What tools touch this area? Which do you actually use vs. which exist? What did your team spend on this category last year (rough)?
- **Triggers:** When does [problem area] come up? What was happening the last time it became a priority?

### Section 3: Pain Excavation (15-20 minutes) — the critical section
Question banks (3+ per topic):
- **Last-time-X probes:** Tell me about the last time you ran into [problem]. What did you do first? What did you try after that? How long did it take? What was the outcome?
- **Switching cost evidence:** Have you ever switched tools/approaches for this? What pushed you to switch? How long did the switch take?
- **Workaround inventory:** What hacks, scripts, spreadsheets, or human workarounds do you have in place because the tools don't quite work?
- **Magnitude tests:** How often does this happen? Last time it happened, how much time/money did it cost you? When was the last time this was discussed in a team meeting?
- **Hierarchy of pain:** If you ranked your top 5 problems in this area, where does this one sit? What's #1?

### Section 4 (OPTIONAL — only if "two-phase"): Solution Reaction (10-15 minutes)
- Briefly describe the concept (60 seconds max, no demo).
- Ask: "If this existed today, what's the first thing you'd want to do with it?"
- Ask: "What about it makes you skeptical?"
- Ask: "Who else on your team would need to weigh in to actually adopt this?"
- Ask: "What would you have to stop doing to use this?"

### Section 5: Demand-Signal Closing (5 minutes)
- "Who else should I talk to who deals with this?" (referral test — strong signal if they offer 2+ names)
- "Can I come back to you in 4-6 weeks with what I'm learning?" (re-engagement signal)
- If they ask "when can I try it?" — that's the strongest possible signal. Capture it.

### Anti-leading-question examples
Include 2-3 explicit examples per section showing the BAD version and the GOOD version. Example:
- BAD: "Wouldn't it be great if there was a tool that automated X?"
- GOOD: "Last time you needed to do X, walk me through what you actually did."

### Post-interview scoring rubric
For each interview, score these binary signals:
- [ ] Interviewee described a specific instance (with date or rough timeframe) where the problem cost them measurable time/money.
- [ ] Interviewee has an active workaround in place (not just a complaint).
- [ ] Interviewee has tried or paid for at least one solution attempt in this area.
- [ ] Interviewee named the budget owner / decision maker if not themselves.
- [ ] Interviewee offered at least one referral.
- [ ] Interviewee asked when they could try it (if solution was discussed).
- [ ] Interviewee's described pain ranks in their top 5 (per section 3).
- [ ] Interviewee did NOT need the problem explained back to them.

### Cohort synthesis template
After 5-10 interviews, fill in:
- **Pain ubiquity:** X of N interviewees described a recent instance of the problem.
- **Pain intensity:** X of N have an active workaround. X of N have paid for an attempted solution.
- **Segment crispness:** Are the high-scoring interviews clustered in one segment, or scattered? (Scattered = segment is wrong.)
- **Solution shape signal:** What did high-scoring interviews ask for that low-scoring ones didn't?
- **Verdict:** ≥6/N high-scoring with clustering → STRONG signal, advance to stage 3. 3-5/N → RESHAPE problem hypothesis or segment. <3/N → KILL hypothesis.

## Output Format

A complete interview guide with all sections above, ready to paste into a Google Doc and run.

## Verification

Before delivering, check:
- [ ] No question begins with "Would you," "Do you think," "Could you imagine"
- [ ] At least one "last time you..." probe in section 3
- [ ] Bad/good anti-leading examples included
- [ ] Scoring rubric has 5-8 binary items
- [ ] Synthesis template provides clear numeric thresholds for STRONG / RESHAPE / KILL

## False-Positive Prevention

- **Interviewees lie politely.** Friends, ex-colleagues, and warm intros bias positive. Insist on at least 3 cold interviews in the cohort.
- **"I would totally use that" is worthless.** Only past behavior (or money already spent) counts as signal.
- **Founder talks too much.** Track interviewer talk-time. Should be ≤25% of the call.
- **Confirmation bias in synthesis.** Have a non-interested party (peer, advisor) score 2-3 transcripts independently using the same rubric and compare.

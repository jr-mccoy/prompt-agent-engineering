---
title: "Blind Spot Analysis and Falsification"
category: non-engineering/decisioning
description: "Identify cognitive blind spots in your self-assessment and generate falsifiable experiments to test each hypothesis"
techniques:
  - QA-02
  - RT-02
  - DS-02
  - ST-02
  - OC-02
difficulty: intermediate
tags:
  - self-reflection
  - blind-spots
  - cognitive-bias
  - falsification
  - decision-making
  - personal-development
updated: "2026-01-24"
related_prompts:
  - productivity/validation/validation_adversarial_mini_check.md
  - productivity/validation/validation_am_i_being_nuts.md
---

# Blind Spot Analysis and Falsification

**Objective:** Identify plausible cognitive blind spots from self-provided context and generate falsifiable experiments to test each hypothesis.

## When to Use

- **Use when:** Making important life or career decisions and want to check your reasoning
- **Use when:** You've received feedback that surprises you and want to understand why
- **Use when:** Preparing for a difficult conversation and want to anticipate objections
- **Use when:** You notice patterns in your failures and want to understand root causes
- **Don't use when:** You need immediate action without time for reflection

## Instructions

1. **Gather Input Context**
   - Provide one of the following: bio, journal excerpt, personality assessment, or self-description
   - Include specific examples of recent decisions or situations
   - Note any feedback you've received that felt surprising or unfair

2. **Analyze for Blind Spot Patterns**
   - Look for recurring themes in failures or conflicts
   - Identify assumptions that are stated but never questioned
   - Note emotional reactions that seem disproportionate to situations
   - Find gaps between self-perception and described outcomes

3. **CRITICAL: Verify Before Reporting**
   - Each blind spot must have supporting evidence from the input
   - Distinguish between isolated incidents and patterns
   - Consider alternative explanations before concluding

4. **Generate Falsifiable Experiments**
   - Each experiment must be completable within 1 week
   - Define clear success/failure criteria
   - Ensure the experiment actually tests the blind spot hypothesis
   - **Confidence level** (High/Medium/Low) for each blind spot

5. **Prioritize by Impact**
   - Rank blind spots by how much they affect important outcomes
   - Consider which are most actionable to address

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Invent blind spots not supported by the provided context
- Pathologize normal human variation or preferences
- Project common biases without specific evidence
- Report vague personality critiques without actionable experiments
- Assume single incidents represent patterns

✅ **DO:**
- Ground each blind spot in specific evidence from the input
- Distinguish between preferences and genuine blind spots
- Propose experiments that could genuinely falsify the hypothesis
- Consider cultural and contextual factors
- Acknowledge uncertainty when evidence is limited

## Expected Output

A structured analysis with exactly 3 plausible blind spots, each with supporting evidence and a falsifiable experiment.

### Output Format

```markdown
## Blind Spot Analysis

### Context Summary
[1-2 sentence summary of the input context]

---

### Blind Spot 1: [Concise Title ≤5 words]
- **Statement:** [Core blind spot in ≤12 words]
- **Evidence:** [Specific quotes or patterns from input]
- **Confidence:** High | Medium | Low
- **Why This Matters:** [Impact on decisions/relationships]
- **Experiment:** [Specific, time-bound test]
  - **Duration:** [≤1 week]
  - **Success Criteria:** [Observable outcome if blind spot is real]
  - **Failure Criteria:** [Observable outcome if blind spot is not real]

### Blind Spot 2: [Concise Title ≤5 words]
[Same structure as above]

### Blind Spot 3: [Concise Title ≤5 words]
[Same structure as above]

---

### Priority Ranking

| Rank | Blind Spot | Impact | Ease to Test | Recommended Action |
|------|------------|--------|--------------|-------------------|
| 1 | [Name] | High/Med/Low | High/Med/Low | [First step] |
| 2 | [Name] | High/Med/Low | High/Med/Low | [First step] |
| 3 | [Name] | High/Med/Low | High/Med/Low | [First step] |

### Self-Audit Checklist
- [ ] Exactly 3 blind spots identified
- [ ] Each has specific evidence from input
- [ ] Each experiment is executable in ≤1 week
- [ ] Success/failure criteria are observable
- [ ] No blind spots invented without evidence
```

## Example Output

```markdown
## Blind Spot Analysis

### Context Summary
Engineering manager, 8 years experience, recently passed over for VP promotion. Journal entries show frustration with "politics" and belief that technical excellence should be sufficient for advancement.

---

### Blind Spot 1: Technical Merit Sufficiency
- **Statement:** Believes technical skill alone should drive career advancement
- **Evidence:** "My system handles 10x the traffic of anyone else's, but they promoted Sarah who barely codes anymore." "I don't play political games - my work speaks for itself."
- **Confidence:** High
- **Why This Matters:** VP roles require influence, coalition-building, and organizational navigation. Technical excellence is necessary but insufficient.
- **Experiment:** Shadow a VP for 3 meetings and document non-technical activities
  - **Duration:** 1 week
  - **Success Criteria:** Identify ≥3 VP activities that have nothing to do with technical work
  - **Failure Criteria:** VP role is primarily technical decisions

### Blind Spot 2: Feedback Interpretation
- **Statement:** Dismisses negative feedback as "political" rather than actionable
- **Evidence:** "The feedback about 'communication style' is just HR speak for 'we want someone more political.'" Three separate mentions of dismissing feedback.
- **Confidence:** Medium
- **Why This Matters:** Pattern of dismissing feedback prevents learning and signals low coachability to leadership.
- **Experiment:** Request specific examples for last 3 pieces of feedback received
  - **Duration:** 3 days
  - **Success Criteria:** ≥2 pieces of feedback have concrete, non-political examples
  - **Failure Criteria:** All feedback is genuinely vague or political in nature

### Blind Spot 3: Relationship Investment
- **Statement:** Underinvests in peer and skip-level relationships
- **Evidence:** "I don't have time for coffee chats when there's real work to do." No mention of non-direct-report relationships in journal.
- **Confidence:** Medium
- **Why This Matters:** Promotion decisions are made by people who don't see your daily work; relationships provide visibility and advocates.
- **Experiment:** Schedule 3 coffee chats with peers/skip-levels this week
  - **Duration:** 1 week
  - **Success Criteria:** Learn ≥2 things about organizational priorities you didn't know
  - **Failure Criteria:** Conversations yield no new information or relationship value

---

### Priority Ranking

| Rank | Blind Spot | Impact | Ease to Test | Recommended Action |
|------|------------|--------|--------------|-------------------|
| 1 | Technical Merit Sufficiency | High | High | Shadow VP for 3 meetings |
| 2 | Relationship Investment | High | Medium | Schedule 3 coffee chats |
| 3 | Feedback Interpretation | Medium | Medium | Request specific examples |

### Self-Audit Checklist
- [x] Exactly 3 blind spots identified
- [x] Each has specific evidence from input
- [x] Each experiment is executable in ≤1 week
- [x] Success/failure criteria are observable
- [x] No blind spots invented without evidence
```

## Customization Guide

- **For career decisions:** Focus on feedback patterns and promotion criteria
- **For relationship issues:** Focus on communication patterns and emotional reactions
- **For creative work:** Focus on feedback receptivity and self-editing patterns
- **For leadership development:** Focus on delegation, trust, and influence patterns

## Techniques Used

- **QA-02 (Adversarial Thinking):** Forces identification of blind spots and counterarguments
- **RT-02 (Multi-Dimensional Analysis):** Evidence, experiment, and impact for each finding
- **DS-02 (Evidence-Based Decision Making):** Requires specific evidence for each claim
- **ST-02 (Structured Sequential Instructions):** Clear step-by-step process
- **OC-02 (Format Specification):** Precise output structure with constraints

## Related Prompts

- [validation_adversarial_mini_check.md](../../domain-productivity/validation/validation_adversarial_mini_check.md) - Quick pre-decision verification
- [validation_am_i_being_nuts.md](validation_am_i_being_nuts.md) - Sanity check for emotional decisions

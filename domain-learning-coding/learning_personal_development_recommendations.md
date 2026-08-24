---
title: "Personal Development Recommendations — Evidence-Based Growth Plan from Code Contributions"
category: "learning-coding"
description: "Analyze an engineer's actual code contributions to produce an evidence-grounded development plan — strengths with citations, prioritized growth areas, and concrete actions, resources, and success metrics — for reviews, mentorship, or self-assessment."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - career-development
  - mentorship
  - skill-assessment
  - growth-plan
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_style_readability_analysis.md
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-learning-coding/learning_code_review_checklist.md
  - domain-learning-coding/learning_code_refactoring_exercises.md
---

# Personal Development Recommendations

**Objective:** Analyze an engineer's actual code contributions to produce an evidence-grounded development plan — strengths with citations, prioritized growth areas, and concrete actions, resources, and success metrics.

**When to use:**
- Preparing for a performance review or career-development conversation.
- Mentorship planning grounded in real work, not impressions.
- Self-assessment when building your own development plan.
- Identifying which skills to invest in for a target level.

**When NOT to use:**
- Evaluating someone with no available code samples (it would be speculation).
- Compensation or hiring decisions (this is developmental, not a verdict).
- Personality or behavioral assessment — this analyzes code contributions only.

**Audience:** Engineering managers, tech leads, mentors, and engineers self-assessing.

---

## Inputs / Context

The user supplies:
1. **Code contributions** — representative PRs, reviews given, bug fixes, features, docs, pasted wrapped in a named tag, e.g. `<contributions>...</contributions>`, or references.
2. **Engineer's current role/level** and (if any) the target level's expectations.
3. **Review period** and team/org needs.
4. **Perspective** (manager-written, mentor, or self-assessment) to calibrate tone.
5. **Optional:** the team's career framework.

Cite specific contributions by their identifier (e.g. "PR in `<contributions>`") as evidence.

---

## Constraints

### Must
- Base every strength and growth area on a cited, specific contribution from `<contributions>`; never assert a trait without evidence.
- Distinguish what the evidence shows from what it suggests (label inferences).
- For each growth area, give concrete actions, real resources, and observable success metrics.
- Prioritize by impact and feasibility, aligned to the role/target level.
- Keep tone developmental and specific, not generic praise/criticism.

### Must Not
- Invent PRs, incidents, coverage numbers, or behaviors not in the supplied material.
- Generalize from a single data point to a sweeping trait.
- Recommend resources that don't exist or aren't relevant.
- Conflate code-contribution evidence with claims about attitude or potential it can't support.

---

## Instructions

1. **Review contributions.** From `<contributions>`, gather evidence across code quality, problem-solving, system design, testing, debugging, and communication. Note the source for each observation.
2. **Identify patterns.** Find recurring strengths and recurring gaps across multiple contributions (not one-offs); mark single-instance observations as tentative.
3. **Map to level.** Compare observed behavior to current-role and target-level expectations.
4. **Assess per competency.** For each: an evidence-backed rating, cited examples (strength and growth), and the gap to the next level.
5. **Generate recommendations.** Prioritized growth areas, each with goal, concrete actions, real resources, and observable success metrics.
6. **Plan check-ins.** A timeline with milestones.
7. **Self-check (verification).** Is every claim backed by cited evidence? Are inferences labeled? Are metrics observable? Is the plan feasible?

---

## False-Positive Prevention

❌ **DON'T:**
- State a strength or weakness without pointing to a specific contribution.
- Extrapolate a personality trait from code (e.g. "not detail-oriented") — stick to what the code shows.
- Generalize from one PR to a consistent pattern.
- Recommend vague growth ("get better at design") without actions and metrics.
- Invent metrics like coverage percentages that weren't supplied.

✅ **DO:**
- Cite the specific contribution behind each observation.
- Label single-instance findings as tentative and team-wide patterns as patterns.
- Give each growth area concrete, resourced, measurable actions.
- Keep recommendations tied to the role/target level.
- Make success metrics observable (someone could check them).

---

## Output Format

```
# Personal Development Report
[Engineer / Role / Period / Perspective]

## Summary
- Overall assessment (evidence-based)
- Strengths to leverage (each cited)
- Priority growth areas

## Detailed Analysis (per competency)
### [Competency]: [rating]
- Evidence: [cited]
- Strength example / Growth opportunity (cited)

## Development Recommendations
### Priority N: [area]
- Goal / Actions / Resources / Success metrics

## Check-in Schedule
| Date | Focus | Milestone |

## Notes
```

---

## Example Output

```markdown
# Personal Development Report
**Engineer:** Alex Chen · **Role:** Software Engineer II · **Period:** Jul–Dec · **Perspective:** Manager

## Summary
- **Overall:** Strong fundamentals and consistent delivery; ready to grow into system design and technical communication.
- **Strengths (cited):** clean code (PR #1234), strong testing (92% on new code per supplied report), constructive reviews (review comments in `<contributions>`).
- **Priority growth:** system design, performance intuition, technical writing.

## Detailed Analysis

### Code Quality: Strong
- **Evidence:** PR #1234 — clear naming, ~20-line functions, consistent typing.
```typescript
interface UserNotificationPreferences { email: boolean; push: boolean; frequency: 'immediate'|'daily'|'weekly'; }
async function updateNotificationPreferences(userId: string, prefs: UserNotificationPreferences): Promise<void> {
  await validatePreferences(prefs);
  await userRepository.updatePreferences(userId, prefs);
}
```
- **Growth opportunity (cited):** PR #1567 implemented feature flags in 3 places — an opening to centralize. *(Single instance — tentative pattern.)*

### System Design: Developing
- **Evidence:** PR #1678 added a preferences table without indexing, timestamps, or a scaling consideration.
```sql
CREATE TABLE user_preferences ( user_id INT PRIMARY KEY, preferences JSONB );
```
- **Senior-level thinking would add:** indexing strategy at scale, `created_at`/`updated_at`, normalized vs JSONB trade-off for read/write patterns.

### Testing: Strong
- **Evidence:** AAA-structured tests in PR #1234; coverage on new code reported at 92% (from supplied report).
- **Growth opportunity:** PR #1567's feature-flag logic lacked end-to-end coverage, contributing to a production issue.

### Performance Awareness: Developing
- **Evidence:** N+1 query in PR #1345 caught in review (reactive, not proactive).
```typescript
// BEFORE (in PR #1345): per-user query
for (const user of users) user.orders = await orderRepository.findByUserId(user.id);
// AFTER (post-review): batched
const map = await orderRepository.findByUserIds(users.map(u => u.id));
users.forEach(u => u.orders = map[u.id] || []);
```

## Development Recommendations

### Priority 1: System Design
- **Goal:** reason beyond component boundaries.
- **Actions:** read "Designing Data-Intensive Applications" (ch. 1–5); write a design doc before the next feature; observe 2 architecture reviews.
- **Success metrics:** [ ] leads one medium-feature design discussion; [ ] proactively flags a scalability concern in review.

### Priority 2: Performance Intuition
- **Goal:** catch performance issues before review.
- **Actions:** profile one existing feature; add perf tests to the next 3 PRs.
- **Success metrics:** [ ] no N+1 in contributions (self-caught); [ ] fixes one existing perf issue.

### Priority 3: Technical Communication
- **Actions:** write an ADR for the next design decision; add a thorough README to the next new component.
- **Success metrics:** [ ] a decision documented and referenced by a teammate.

## Check-in Schedule
| Date | Focus | Milestone |
|------|-------|-----------|
| +2 mo | System design | Book ch. 1–5, first design doc |
| +4 mo | Performance | First proactive perf fix |
| +6 mo | Communication | ADR referenced by a teammate |

## Notes
On track toward Senior with focused system-design growth. Consider assigning ownership of a bounded component and pairing on the next architecture decision.
```

---

## Verification

- [ ] Every strength and growth area cites a specific contribution.
- [ ] Inferences are labeled; single-instance findings marked tentative.
- [ ] No invented PRs, incidents, or metrics.
- [ ] Each growth area has actions, real resources, and observable metrics.
- [ ] Recommendations align to the role/target level and are feasible.
- [ ] Tone is developmental and specific.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as an evidence-grounded development plan.
- **ST-02 (Structured Sequential Instructions):** Review → patterns → map to level → assess → recommend → check-ins → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Assesses quality, design, testing, debugging, and communication together.
- **RT-05 (Evidence-Based Reasoning):** Requires a cited contribution behind every claim.
- **QA-01 (Self-Verification):** Final pass confirms evidence-backing and observable metrics.

---

## Related Prompts

- `domain-learning-coding/learning_code_style_readability_analysis.md` — Assess code-quality evidence.
- `domain-learning-coding/learning_code_pattern_recognition.md` — Assess design/pattern usage.
- `domain-learning-coding/learning_code_review_checklist.md` — Assess review-quality evidence.
- `domain-learning-coding/learning_code_refactoring_exercises.md` — Build the practice that closes gaps.

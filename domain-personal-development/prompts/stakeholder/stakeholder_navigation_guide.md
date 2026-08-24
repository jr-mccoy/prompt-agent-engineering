---
title: "Stakeholder Navigation Guide"
category: personal-development
description: "Analyze complex stakeholder dynamics and develop strategic influence plans — maps power, incentives, and relationships to identify the best path through organizational politics"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - personal-development
  - stakeholder-management
  - organizational-politics
  - influence
  - strategic-communication
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/stakeholder/stakeholder_politics.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-personal-development/prompts/thinking/thinking_fresh_perspective_generator.md
  - domain-personal-development/prompts/agency/agency_feedback_extraction.md
---

# Stakeholder Navigation Guide

**Objective:** Analyze a complex political or organizational situation, map all stakeholders with their power, incentives, and positions, then develop 3 strategic paths forward with a recommended 72-hour action plan.

**When to Use:** Use this prompt when you're navigating tricky organizational dynamics — competing priorities between teams, a decision that requires buy-in from multiple stakeholders with conflicting interests, political situations where the "right answer" depends on who you ask, or any multi-party scenario where influence matters as much as logic.

---

## Inputs / Context

Provide the following. Wrap pasted material in the named tags so it can be referenced precisely during analysis.

```
<situation>
[Paste all relevant emails, meeting notes, background - be thorough]
</situation>
```

- **My Role:** [Your position, authority level, reporting structure]
- **Decision Needed By:** [Specific date and why]
- **Desired Outcome:** [What success looks like to you]
- **Constraints:** [What you cannot do/change]
- **Stakeholders I'm aware of:** [Names/titles of the people involved, even if incomplete]

### Refusal logic (insufficient input)

Do **not** produce a stakeholder analysis if the input is too thin to ground it. Specifically, ask for more before proceeding when:

- The `<situation>` block is empty or a single vague sentence with no named people, no decision, and no tension described.
- Fewer than 2 distinct stakeholders can be identified (a "stakeholder map" of one person is not a map — redirect to a direct-conversation or negotiation prompt instead).
- No desired outcome is stated (without a goal, "best path" is undefined).

When refusing, name exactly which of the inputs above is missing and ask one targeted question per gap. Do not invent stakeholders, positions, or facts to fill the gap.

---

## Instructions

Navigate this political situation through systematic analysis:

**Step 1: Situation Summary**
Distill the situation into:
- Core issue (2-3 sentences)
- Key tension points (3-5 bullets)
- Decision urgency level

**Step 2: Map the Current Landscape**

**Facts Everyone Agrees On:**
- List 3-5 undisputed facts
- Note their implications

**Points of Disagreement:**
- Issue 1: [What] → Sides: [Who believes what]
- Issue 2: [What] → Sides: [Who believes what]

**Step 3: Create Stakeholder Matrix**

For each key person involved:

**Stakeholder: [Name - Title]**
- **Power Level:** High/Medium/Low
- **Current Position:** What they want
- **Underlying Interests:** Why they want it
- **Influence Levers:** What motivates them
- **Relationship to You:** Ally/Neutral/Opponent
- **Key Pressure Points:** What they fear
- **Best Approach:** How to engage them

**Step 4: Develop Strategic Options**

Present exactly 3 paths forward:

**Option 1: [The Collaborative Path]**
- **Specific Actions:** 5 concrete steps
- **Timeline:** When to do what
- **Pros:** 3 main benefits
- **Cons:** 3 main risks
- **Success Probability:** X%
- **Second-Order Effects:** What happens next

[Repeat for Options 2 and 3 with different strategies]

**Step 5: Recommended Approach**

**Recommendation:** [Which option and why]

**First 72 Hours Action Plan:**
1. Hour 1-4: [Immediate action]
2. Day 1: [What to accomplish]
3. Day 2: [Next steps]
4. Day 3: [Checkpoint and adjust]

**Risk Mitigation:**
- If X happens, then Y
- Backup plan for resistance
- Exit strategy if needed

---

### False-Positive Prevention

- ❌ Do NOT assume all stakeholders act rationally — emotion and ego drive many decisions
- ❌ Do NOT recommend manipulation or deception — sustainable influence requires trust
- ❌ Do NOT oversimplify stakeholder positions — people hold contradictory views
- ❌ Do NOT ignore your own biases — your framing of the situation may reflect your position
- ❌ Do NOT treat this as a zero-sum game — look for solutions where multiple parties win
- ✅ DO distinguish between stated positions and underlying interests
- ✅ DO consider what each stakeholder fears losing, not just what they want to gain
- ✅ DO identify where interests align across opposing parties
- ✅ DO factor in organizational culture and unwritten rules
- ✅ DO plan for the possibility that your initial read of the situation is incomplete

---

## Expected Output

```markdown
# Stakeholder Analysis: [Situation Title]

## Situation Summary
[Core issue + tension points + urgency]

## Landscape Map
- Facts: ...
- Disagreements: ...

## Stakeholder Matrix
| Stakeholder | Power | Position | Interests | Approach |
|-------------|-------|----------|-----------|----------|
| [Name] | High/Med/Low | [What they want] | [Why] | [How to engage] |

## Strategic Options
### Option 1: [Name] — [Success probability]%
### Option 2: [Name] — [Success probability]%
### Option 3: [Name] — [Success probability]%

## Recommendation
[Which option + why]

## 72-Hour Action Plan
1. ...
2. ...
3. ...

## Risk Mitigation
- If [X]: [Response]
```

---

## Verification

Before delivering the analysis, confirm each of the following:

- [ ] Every stakeholder in the matrix appears in the source material — none were invented to round out the map.
- [ ] Each stakeholder has a *stated position* AND a distinct *underlying interest* (they are not the same sentence reworded).
- [ ] At least one point of cross-party interest alignment was identified before any zero-sum framing.
- [ ] Exactly 3 strategic options are presented, and they are genuinely different strategies (not three flavors of the same move).
- [ ] Each option's success probability is justified by the stakeholder map, not asserted arbitrarily.
- [ ] The 72-hour plan's first action is something the user can do alone, today, without anyone else's prior approval.
- [ ] Risk mitigation covers the most powerful opponent's most likely counter-move.
- [ ] The user's own framing bias is acknowledged where their position may color the situation read.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on producing actionable stakeholder strategy
- **ST-02** (Structured Sequential Instructions) — 5-step analysis from summary to action plan
- **RT-02** (Multi-Dimensional Analysis) — Power, interests, positions, fears, approaches
- **CM-01** (Explicit Context Framing) — Detailed situation and constraint capture
- **DS-06** (Prioritization Guidance) — 3 options ranked with probability and trade-offs
- **QA-04** (Uncertainty Acknowledgment) — Risk mitigation and backup plans

---

## Related Prompts

- [stakeholder_politics.md](../stakeholder/stakeholder_politics.md) — Deeper political/power analysis for especially complex, high-conflict situations.
- [thinking_blind_spot_mirror_see_what_im_missing.md](../thinking/thinking_blind_spot_mirror_see_what_im_missing.md) — Check what you're missing in the situation read.
- [thinking_fresh_perspective_generator.md](../thinking/thinking_fresh_perspective_generator.md) — Generate alternative viewpoints on the conflict.
- [agency_feedback_extraction.md](../agency/agency_feedback_extraction.md) — Extract useful signal from stakeholder reactions after you act.

> For interest-based bargaining mechanics (BATNA, ZOPA, concession sequencing), use `domain-negotiation/`. For drafting the actual stakeholder-facing message, use `domain-professional-communication/`. This prompt is for the *strategy*, not the negotiation tactics or the written deliverable.

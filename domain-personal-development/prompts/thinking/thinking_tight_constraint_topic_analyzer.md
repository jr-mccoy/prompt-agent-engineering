---
title: "Tight Constraint Topic Analyzer"
category: personal-development
description: "Deep analysis of any topic under strict constraints — word limits, required perspectives, mandatory frameworks, and source requirements force rigorous, focused thinking"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - personal-development
  - constrained-analysis
  - critical-thinking
  - frameworks
  - deep-analysis
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_question_generator_mode.md
  - domain-personal-development/prompts/thinking/thinking_interrogative_mode.md
  - domain-personal-development/prompts/thinking/thinking_fresh_perspective_generator.md
---

# Tight Constraint Topic Analyzer

**Objective:** Produce a deep, rigorous analysis of any topic under explicitly defined constraints — word limits, required perspectives, mandatory frameworks, source requirements, and forbidden words. The constraints force focused thinking and prevent the analysis from drifting into generalities.

**When to Use:** When you need disciplined analysis of a complex topic. When you want to force yourself (or the AI) to think from a specific perspective or through a specific framework. When you need presentation-ready analysis under strict format requirements. When unconstrained thinking has produced vague or bloated output.

---

## Inputs / Context

**Subject:** [The topic to analyze]
**Constraints:**
- **Word limit:** [N words]
- **Perspective:** [Role or viewpoint to adopt, e.g., "CFO", "first-time customer", "skeptical board member"]
- **Frameworks:** [Required analytical frameworks, e.g., "Porter's Five Forces + PESTLE"]
- **Source requirements:** [Cite at least N sources inline, or "none required"]
- **Forbidden words:** [Comma-separated list of words to avoid, forcing precision]
- **Additional constraints:** [Any other rules]

**Two inputs are required: a specific subject AND at least one real constraint.** The entire value of this prompt is disciplined thinking under constraints — without them it degrades into a generic essay. If the user supplies a subject but no constraints, ask which constraints to impose (offer the menu above) rather than inventing arbitrary ones. If constraints conflict or are impossible (e.g., three deep frameworks in 150 words, or a source requirement on a topic with no available sources), flag the conflict and ask the user to relax one before analyzing — do not silently violate a constraint to make it fit.

---

## Instructions

### Phase 1: Constraint Acknowledgment

Before analyzing, confirm understanding of all constraints. Flag any that conflict.

### Phase 2: Internal Reasoning

Reason step-by-step through the topic, applying each required framework. This reasoning may be done internally — only the structured output is delivered.

### Phase 3: Structured Output

Produce the analysis under `###` section headings:

### Analysis
[The substantive analysis, applying required frameworks, maintaining the required perspective, staying within word limits]

### Constraint Audit
- Word count ≤ [N]? ✅/❌
- Perspective maintained throughout? ✅/❌
- All frameworks applied? ✅/❌
- Source count met? ✅/❌
- Forbidden words absent? ✅/❌

---

### False-Positive Prevention

- ❌ Do NOT ignore constraints — the entire point is disciplined analysis under constraints
- ❌ Do NOT pad with filler to hit word counts — concision is a feature
- ❌ Do NOT drop the perspective mid-analysis — maintain it consistently
- ❌ Do NOT apply frameworks superficially — each framework should generate real insight
- ✅ DO flag if constraints conflict (e.g., too many frameworks for the word limit)
- ✅ DO compress supporting details rather than cutting core arguments
- ✅ DO make the constraint audit honest — mark ❌ if a constraint wasn't fully met
- ✅ DO use the perspective to generate genuinely different analysis than a neutral view would

---

## Expected Output

```markdown
# Constrained Analysis: [Subject]

**Perspective:** [Role]
**Frameworks:** [Applied]
**Word limit:** [N]

### Analysis
[Structured analysis under headings, applying frameworks, maintaining perspective]

### Constraint Audit
- Word count ≤ [N]? ✅ ([actual count])
- Perspective maintained? ✅
- Frameworks applied? ✅ ([list])
- Source count met? ✅ ([N] sources)
- Forbidden words absent? ✅
```

---

## Verification

Before delivering the analysis, confirm:

- [ ] Every declared constraint was checked and reported honestly in the Constraint Audit (a real ❌ is marked when a constraint wasn't fully met — no false ✅).
- [ ] The word count is within the limit, achieved by compressing detail rather than cutting core argument or padding with filler.
- [ ] The required perspective is maintained consistently throughout, not dropped after the opening.
- [ ] Each required framework was applied substantively and generated real insight, not name-dropped.
- [ ] The source-citation requirement is met inline (or marked ❌ if it could not be).
- [ ] No forbidden word appears anywhere in the analysis.
- [ ] The perspective produced genuinely different analysis than a neutral view would have.
- [ ] Any constraint conflict was flagged rather than silently violated.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Constrained analysis with explicit rules
- **ST-02** (Structured Sequential Instructions) — Acknowledge, reason, output, audit
- **CM-01** (Explicit Context Framing) — Topic and all constraints captured upfront
- **CM-02** (Constraint Specification) — Tight boundaries force precision
- **QA-01** (Chain-of-Verification) — Self-audit against all constraints

---

## Related Prompts

- `thinking_question_generator_mode.md` — Generate questions before constraining analysis
- `thinking_interrogative_mode.md` — Surface unknowns before deep analysis
- `thinking_fresh_perspective_generator.md` — Generate alternative perspectives to analyze from

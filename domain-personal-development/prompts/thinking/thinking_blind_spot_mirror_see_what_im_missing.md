---
title: "Personal Blind Spot Identifier"
category: personal-development
description: "Identify plausible blind spots in your thinking, assumptions, or behavior — with falsifiable experiments to test each one and concrete steps to address what you find"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - QA-02
  - QA-04
difficulty: intermediate
tags:
  - personal-development
  - blind-spots
  - self-awareness
  - assumptions
  - critical-thinking
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/thinking/thinking_fresh_perspective_generator.md
  - domain-personal-development/prompts/thinking/thinking_mindset_shift_reframe.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Personal Blind Spot Identifier

**Objective:** Identify 3-5 plausible blind spots in your thinking, assumptions, or behavior about a specific area of your life — then design a falsifiable experiment for each one so you can test whether the blind spot is real rather than just speculating about it.

**When to Use:** Use this prompt when you suspect you're missing something important — before a major decision, after receiving surprising feedback, when results don't match expectations, when you feel defensive about a topic, or when you've been stuck for a while and can't figure out why. Also useful for regular quarterly self-assessment.

**Important context:** Everyone has blind spots. They're not character flaws — they're structural features of how humans think. The most dangerous blind spots are the ones that feel like certainty. This prompt doesn't try to make you doubt everything; it targets the specific areas where your confidence may be unwarranted.

---

## Inputs / Context

Before identifying blind spots, provide context:

1. **Focus Area:**
   - "What area of your life are you examining? (career, relationship, project, habit, decision)"
   - "Why are you examining this now? What triggered it?"

2. **Self-Assessment:**
   - "What are you most confident about in this area?"
   - "What feedback have others given you that surprised you?"
   - "Where have your predictions been wrong recently?"

3. **Stakeholder Input:**
   - "Who sees you in this area? (colleagues, partner, friends, customers)"
   - "If you asked them what you're missing, what might they say?"
   - "Is there feedback you've dismissed or explained away?"

**If the inputs are too thin to ground real hypotheses — refuse to guess.** If the user gives only a one-word focus area (e.g., "my career") with no triggering event, no confidence claims, and no feedback or failed-prediction examples, do NOT manufacture generic blind spots ("you might be overconfident," "you might not delegate enough"). Ask for at least: (a) what triggered this examination, and (b) one concrete piece of surprising feedback OR one recent prediction that turned out wrong. Without at least one piece of real evidence, blind-spot "findings" are projection, not analysis.

---

## Instructions

### Phase 1: Blind Spot Discovery

Analyze the provided context to identify 3-5 plausible blind spots using these lenses:

**Lens 1: The Confidence-Competence Gap**
Where might you be more confident than your evidence warrants? Look for:
- Areas where you haven't tested your assumptions
- Skills you believe you have but rarely get objective feedback on
- Beliefs about "how things work" that come from limited experience

**Lens 2: The Feedback Filter**
What information are you systematically ignoring or discounting?
- Feedback you've received multiple times but haven't acted on
- Data points that contradict your narrative
- Perspectives from people you consider "less informed"

**Lens 3: The Comfort Zone Boundary**
What are you avoiding without realizing it?
- Tasks you keep deferring "until later"
- Conversations you haven't had
- Experiments you haven't tried because you "already know" the outcome

**Lens 4: The Identity Trap**
Where might your identity be preventing you from seeing clearly?
- "I'm the kind of person who..." beliefs that may be outdated
- Roles you play that limit your options
- Values you espouse but don't practice

### Phase 2: Blind Spot Documentation

For each identified blind spot (3-5 total):

```markdown
### Blind Spot #N: [Concise Statement — max 15 words]

**What you might be missing:** [2-3 sentences explaining the blind spot]

**Evidence it exists:**
- [Observable behavior or pattern that suggests this blind spot]
- [Feedback or data point that supports it]

**Why it's hard to see:**
- [What makes this blind spot feel like certainty instead of assumption]

**Impact if real:**
- [What this costs you — opportunities, relationships, growth, money]

**Falsifiable Experiment:**
- **What to do:** [Specific, concrete action — completable in 1 week]
- **What to measure:** [Observable outcome, not a feeling]
- **Result if blind spot is real:** [What you'd observe]
- **Result if blind spot is not real:** [What you'd observe instead]
- **Timeline:** [When to run the experiment and evaluate]
```

### Phase 3: Pattern Analysis

After documenting all blind spots:
1. **Common theme:** What connects these blind spots? Is there a root cause?
2. **Easiest to test:** Which experiment should you run first?
3. **Highest stakes:** Which blind spot, if real, would have the biggest impact?
4. **Action plan:** Sequence the experiments from easiest to hardest.

---

### False-Positive Prevention

- ❌ Do NOT project common blind spots without evidence from the user's context
- ❌ Do NOT treat all blind spots as equally important — prioritize by impact
- ❌ Do NOT pathologize normal behavior — having preferences isn't always a blind spot
- ❌ Do NOT present speculative blind spots with false certainty — these are hypotheses
- ❌ Do NOT overwhelm with 10+ blind spots — 3-5 is the right range for actionability
- ✅ DO ground blind spot hypotheses in the user's specific context and evidence
- ✅ DO design experiments that are genuinely falsifiable (can prove the blind spot wrong)
- ✅ DO acknowledge that some "blind spots" may turn out to be informed choices
- ✅ DO make experiments small enough to be non-threatening (1 week, low stakes)
- ✅ DO suggest starting with the easiest experiment to build momentum

---

## Expected Output

```markdown
# Blind Spot Analysis: [Focus Area]

## Context Summary
[2-3 sentences confirming understanding]

## Identified Blind Spots

### Blind Spot 1: [Statement]
- What you might be missing: ...
- Evidence: ...
- Experiment: [1-week test with measurable outcome]

### Blind Spot 2: [Statement]
...

### Blind Spot 3: [Statement]
...

## Pattern Analysis
- Common theme: ...
- Run first: Blind Spot [N] — [why]
- Highest impact: Blind Spot [N] — [why]

## Action Plan
Week 1: Run experiment for Blind Spot [N]
Week 2: Evaluate results + run experiment for Blind Spot [N]
Week 3: Evaluate + decide on remaining experiments
```

---

## Verification

Before delivering, confirm:

- [ ] 3–5 blind spots are presented (not 1–2, not 10+) — the actionable range.
- [ ] Each blind spot is grounded in the user's specific evidence, not a generic human tendency.
- [ ] Each blind spot has a **falsifiable** experiment: it states both what you'd observe if it's real AND what you'd observe if it's not.
- [ ] Each experiment is completable in ~1 week and measures an observable outcome, not a feeling.
- [ ] Blind spots are framed as hypotheses, not certainties (no false confidence).
- [ ] At least one item is acknowledged as possibly an informed choice rather than a true blind spot.
- [ ] The action plan sequences experiments easiest-first to build momentum.
- [ ] No normal preference or protective concern was pathologized as a blind spot.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on identifying testable blind spots
- **ST-02** (Structured Sequential Instructions) — Discovery, documentation, pattern analysis
- **RT-02** (Multi-Dimensional Analysis) — Four lenses covering different blind spot types
- **CM-01** (Explicit Context Framing) — Grounded in user's specific situation
- **QA-02** (Adversarial Testing) — Challenges user's confident assumptions
- **QA-04** (Uncertainty Acknowledgment) — Treats blind spots as hypotheses, not certainties

---

## Related Prompts

- `thinking_regret_minimization.md` — Make decisions using future-self perspective
- `thinking_fresh_perspective_generator.md` — Generate alternative viewpoints
- `thinking_mindset_shift_reframe.md` — Reframe beliefs that may be blocking you
- `../agency/agency_stuck_diagnosis.md` — Debug why you're stuck

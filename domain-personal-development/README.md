# Personal Development: Comprehensive Guide

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers goal setting, career planning, habit building, self-improvement, decision-making, and personal effectiveness.

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Goals/Planning** | "goal setting", "life planning", "quarterly review", "personal OKRs", "bucket list" |
| **Career** | "career change", "job search", "career path", "skill development", "professional growth" |
| **Habits/Productivity** | "habit building", "morning routine", "time management", "productivity system", "focus" |
| **Decision-Making** | "should I...", "life decision", "major choice", "weighing options", "trade-offs" |
| **Self-Improvement** | "self-reflection", "personal growth", "mindset", "overcome", "improve myself" |
| **Life Transitions** | "just started a new job", "after the move", "empty nest", "retirement", "laid off", "after the breakup", "who am I now" |
| **Emotional Skills** | "handle disappointment", "manage jealousy", "self-compassion", "overreacting", "process a hard moment" (everyday, non-clinical) |
| **Validation/Clarity** | "am I being reasonable", "sanity check", "perspective on", "gut check" |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **Career Transitioners** | Evaluating options, skill gaps, transition planning |
| **Goal Setters** | Structuring ambitions, tracking progress, accountability |
| **Decision Makers** | Weighing major life choices, reducing bias, gaining clarity |
| **Self-Improvers** | Building habits, changing behaviors, personal growth |
| **Professionals** | Work-life balance, effectiveness, leadership development |
| **People in Transition** | Living through a change already underway — new role, relocation, parenthood, empty nest, retirement, job loss, breakup |
| **Students/Learners** | Study strategies, skill acquisition, learning optimization |

### Out of Scope

- **Clinical mental health** - Anxiety, depression, trauma, therapy, crisis → `domain-psychology/` and licensed professional support. The `emotional-fitness/` and `life-transitions/` subfolders here are **everyday, non-clinical skill-building only**; anyone in or considering therapy, in distress, or facing a safety concern is routed to `domain-psychology/client-self-use/` and professional help. When in doubt, prefer the clinical domain.
- **Financial planning specifics** - Investment advice, tax strategies → `domain-finance/` / `domain-specialized-fields`
- **Medical decisions** - Health treatments → `domain-healthcare-clinical`
- **Academic research** - Methodology, literature → `domain-research-academic`

### Subfolder Map

`prompts/`: `agency/` · `goals/` · `habits/` · `identity/` · `resilience/` · `relationships/` · `thinking/` · `productivity/` · `solo-dev/` · `stakeholder/` · `career/` · **`life-transitions/`** (navigating a change already underway — the after/during complement to `major-decisions/`) · **`emotional-fitness/`** (everyday non-clinical emotional skills). Top-level: `career-transformation/` · `major-decisions/` (making the high-stakes choice, *before* the change). See `EXPANSION_ROADMAP.md` for the full inventory and future waves.

---

## Domain-Specific Considerations

### What Makes Personal Development Unique

Personal development prompts operate in environments where:

1. **Subjectivity is Central** - "Success" means different things to different people
2. **Context is Everything** - Generic advice is often wrong advice
3. **Emotions Are Involved** - Decisions carry psychological weight
4. **Trade-offs Are Personal** - What's "worth it" depends on individual values
5. **Motivation Matters** - Knowing what to do ≠ doing it
6. **Long-term Perspective** - Today's choice affects tomorrow's options
7. **Bias is Ubiquitous** - Confirmation bias, sunk cost, loss aversion all apply

### The Personal Development Difference

| Dimension | Generic Self-Help | Effective Personal Development |
|-----------|-------------------|-------------------------------|
| **Advice** | "Follow your passion!" | "Given your constraints, here are options..." |
| **Goals** | "Dream big!" | "What's achievable AND aligned with values?" |
| **Trade-offs** | Minimized | Explicitly surfaced and explored |
| **Context** | Ignored | Central to all recommendations |
| **Uncertainty** | Overstated confidence | Honest about unknowns |
| **Action** | Vague inspiration | Specific next steps |

### Critical Success Factors

1. **Understand Individual Context** - Values, constraints, history, relationships
2. **Surface Trade-offs Explicitly** - Every choice closes some doors
3. **Acknowledge Emotional Dimensions** - Feelings are data, not obstacles
4. **Provide Actionable Steps** - Not just what, but HOW
5. **Build in Reflection** - Self-assessment is part of the process
6. **Avoid Generic Platitudes** - Context-specific guidance only
7. **Respect Autonomy** - Support decisions, don't make them

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Generic advice** | "Just believe in yourself!" | Require specific context before advising |
| **Ignoring constraints** | "Quit your job and travel!" | Explicitly address financial/family/health realities |
| **Toxic positivity** | "Everything happens for a reason!" | Acknowledge difficulty, validate emotions |
| **False certainty** | "This will definitely work!" | Honest uncertainty about outcomes |
| **Overlooking trade-offs** | "You can have it all!" | Surface what you're giving up |
| **Unsolicited advice** | Telling instead of exploring | Ask questions before recommending |

---

## Recommended Techniques

### Core Techniques (Always Use)

| Technique | Application in Personal Development | Example |
|-----------|-----------------------------------|---------|
| **CM-01 Context Framing** | Detailed personal situation capture | Values, constraints, history, stakeholders |
| **RT-02 Multi-Dimensional** | Explore trade-offs across dimensions | Career vs. family vs. health vs. growth |
| **QA-04 Uncertainty** | Honest about unknowns | "This could go several ways..." |
| **ST-02 Sequential Steps** | Actionable implementation guidance | Week 1: X, Week 2: Y |
| **RT-04 Emotional Intelligence** | Acknowledge feelings as valid data | "It's understandable to feel torn..." |

### Situational Techniques

| Situation | Add Technique | Why |
|-----------|--------------|-----|
| Major decision | RT-03 Tree of Thoughts | Explore branching consequences |
| Career planning | DS-01 Framework | Use structured career frameworks |
| Goal setting | OC-01 Templates | Structured goal formats (SMART, etc.) |
| Habit building | QA-01 Verification | Build in progress checkpoints |
| Validation/sanity check | QA-02 Adversarial | Challenge assumptions systematically |

---

## Quality Indicators for Personal Development

### What "Good" Looks Like

**A high-quality personal development prompt output:**

1. **Reflects Individual Context**
   - Incorporates stated values, constraints, history
   - Doesn't give generic advice that could apply to anyone
   - Acknowledges unique circumstances

2. **Surfaces Trade-offs Explicitly**
   - Every option shows what's gained AND lost
   - No "have it all" false promises
   - Makes hidden costs visible

3. **Acknowledges Emotions**
   - Validates feelings as legitimate
   - Doesn't dismiss concerns as "just fear"
   - Integrates emotional reality with practical analysis

4. **Provides Actionable Steps**
   - Specific, time-bound actions
   - First step is immediately doable
   - Includes how to handle obstacles

5. **Maintains Honest Uncertainty**
   - Doesn't promise outcomes
   - Presents scenarios, not predictions
   - Includes contingency thinking

### Confidence Calibration Framework

```markdown
## Personal Development Confidence Levels

**High Confidence - Can State Directly:**
- Well-established frameworks (SMART goals, habit stacking)
- Research-backed principles (spaced repetition, implementation intentions)
- Mathematical trade-offs (time, money, opportunity cost)

**Medium Confidence - Present with Caveats:**
- Career path generalizations (typical trajectories)
- Skill development timelines (varies by individual)
- Behavioral predictions (based on common patterns)

**Low Confidence - Explore, Don't Prescribe:**
- Personal fulfillment predictions ("you'll be happy if...")
- Relationship outcomes
- Life satisfaction forecasts
- Long-term career predictions

**Never State:**
- Guarantees about life outcomes
- Claims that one path is objectively "right"
- Dismissal of valid concerns as irrational
```

### False-Positive Prevention for Personal Development

**DON'T:**

- Give generic advice without understanding context
- Promise outcomes ("This will make you successful!")
- Dismiss concerns or fears as irrational
- Assume your values match the user's values
- Recommend drastic action without understanding stakes
- Use toxic positivity instead of realistic optimism
- Ignore practical constraints (money, family, health)
- Present one perspective as the only valid view

**DO:**

- Ask clarifying questions before advising
- Present options with trade-offs, not recommendations
- Validate emotions while also examining them
- Make assumptions explicit and checkable
- Suggest small experiments before big commitments
- Acknowledge that "right" is subjective
- Include practical considerations alongside aspirational ones
- Present multiple valid perspectives

---

## Existing Prompts in This Repository

> **Note:** Personal development prompts are now located in `domain-personal-development/prompts/` for better organization.

### Exemplar Prompts (Study These)

| Prompt | Location | What It Demonstrates |
|--------|----------|---------------------|
| `solo_dev_burnout_prevention.md` | [prompts/solo-dev/](./prompts/solo-dev/) | Gold standard: full frontmatter, false-positive prevention, techniques |
| `goals_skill_breakdown_blueprint.md` | [prompts/goals/](./prompts/goals/) | Skill acquisition planning, systematic breakdown |
| `thinking_regret_minimization.md` | [prompts/thinking/](./prompts/thinking/) | Future-self consultation, multi-horizon analysis |

### All Personal Development Prompts

Prompts are organized into subdirectories by function:

**Solo Developer (`prompts/solo-dev/`)** - 5 prompts for independent developers
- `solo_dev_automation_audit.md` - Automation opportunity identification
- `solo_dev_burnout_prevention.md` - Burnout risk assessment and prevention
- `solo_dev_context_switching_reducer.md` - Context switch cost reduction
- `solo_dev_network_building.md` - Professional network building
- `solo_dev_skill_gap_assessment.md` - Technical skill gap analysis

**Goals & Planning (`prompts/goals/`)** - 4 prompts for goal setting and learning
- `goals_skill_breakdown_blueprint.md` - Skill acquisition planning
- `goals_goal_system_designer.md` - Goal framework design
- `goals_goal_setting_and_reflection_loop.md` - Goal reflection cycles
- `goals_decompose_learning_task.md` - Learning task breakdown

**Productivity & Focus (`prompts/productivity/`)** - 5 prompts for work effectiveness
- `productivity_personal_energy_audit.md` - Personal energy management
- `productivity_meeting_killer_prompt.md` - Meeting effectiveness optimization
- `productivity_zombie_meeting_detector.md` - Calendar audit and optimization
- `productivity_automation_gold_mine.md` - Workflow automation opportunities
- `productivity_open_loop_audit.md` - Mental clarity and open loop closure

**Thinking & Analysis (`prompts/thinking/`)** - 9 prompts for cognitive tools
- `thinking_mindset_shift_reframe.md` - Limiting belief reframing
- `thinking_blind_spot_mirror_see_what_im_missing.md` - Blind spot identification
- `thinking_fresh_perspective_generator.md` - Fresh perspective generation
- `thinking_interrogative_mode.md` - Interrogative exploration
- `thinking_question_generator_mode.md` - Strategic question generation
- `thinking_regret_minimization.md` - Regret minimization decision framework
- `thinking_tight_constraint_topic_analyzer.md` - Tight constraint analysis
- `thinking_memory_palace_generator.md` - Memory palace construction
- `thinking_explain_like_im_nine_converter.md` - Simplify a complex topic to plain language
- See [prompts/thinking/README.md](./prompts/thinking/README.md) for sub-groupings and composition

**Stakeholder Navigation (`prompts/stakeholder/`)** - 2 prompts for workplace dynamics
- `stakeholder_navigation_guide.md` - Stakeholder management
- `stakeholder_politics.md` - Political navigation

**Agency, Ownership & Execution (`prompts/agency/`)** - 13 prompts for self-directed work
- `agency_project_ownership_converter.md` - Convert a vague goal into an owned project with a first deliverable
- `agency_next_action_spec.md` - Force a single physical next action from a mental pile
- `agency_planning_masquerade_detector.md` - Audit activity for planning that stands in for execution
- `agency_ship_sprint_design.md` - Design a 2–10 day sprint that ships something real in public
- `agency_end_of_session_review.md` - 5–10 minute review that pre-stages the next session
- `agency_proof_of_work_portfolio.md` - Plan a 3–12 month portfolio with coherent story and cadence
- `agency_feedback_extraction.md` - Extract signal from reactions after shipping
- `agency_weekly_review.md` - 20–40 minute weekly review that compounds into a system
- `agency_stuck_diagnosis.md` - Classify "stuck" into 12 blocker types with targeted unblock moves
- `agency_skill_gap_reframe.md` - Separate claimed skill gaps from the project, bound the learning
- `agency_habit_loop_repair.md` - Repair a broken habit at a scale sized to the break
- `agency_foundation_session.md` - Run a 2–4 hour foundation session with durable context capture
- `agency_rapid_start_mode.md` - 60-second protocol from "at the desk" to "producing an artifact"
- See [prompts/agency/README.md](./prompts/agency/README.md) for composition patterns

**Career Assessments (`prompts/career/`)** - 17 AI career path assessments
- Interactive qualification assessments for AI career paths including ML Engineering, Prompt Engineering, Ethics, Product Management, Data Annotation, Computer Vision, NLP, Research, Deep Learning, Content Creation, Governance, Coaching, Strategy, Change Management, Compliance, Conversational AI/UX, and Product Adoption
- See [prompts/career/README.md](./prompts/career/README.md) for full index

**Career & Work Transformation (`career-transformation/`)** - 4 prompts for the hard work of assessing and repositioning a role under structural pressure
- `career_coordination_tax_audit.md` - Classify a real calendar week into coordination-tax categories
- `career_role_structural_vulnerability.md` - Grade a role on four independent axes (economic function, coordination-tax capture, scarce-input control, substitution slope)
- `career_residual_skills_inventory.md` - Evidence-keyed inventory of judgment, taste, and context that survive automation
- `career_90_day_repositioning_plan.md` - Weekly-checkpointed plan with stop conditions toward a surviving / adjacent role
- See [career-transformation/README.md](./career-transformation/README.md) for the recommended sequence

**Identity (`prompts/identity/`)** - 7 prompts for the third axis (not action, not cognition — identity, values, meaning, and discernment)
- `identity_values_clarification.md` - Surface revealed values from past decisions and contrast with stated values
- `identity_self_talk_audit.md` - Capture verbatim inner-critic sentences, classify by distortion, generate evidence-based counters
- `identity_comparison_envy_diagnostic.md` - Decompose envy into specific sub-items, classify each by signal-vs-noise pattern
- `identity_confidence_calibration.md` - Two-mode calibration: impostor-correction or overconfidence-audit, against evidence
- `identity_purpose_reignition.md` - Diagnose loss-of-why as depletion / completion / drift / mismatch / hidden goal
- `identity_life_audit_reckoning.md` - Multi-dimensional structured audit at a major life inflection
- `identity_taste_development.md` - 90-day deliberate taste-training loop in a specific domain
- New: `agency/agency_burnout_recovery.md` - Diagnose burnout stage and prescribe stage-appropriate recovery
- New: `agency/agency_decision_post_mortem.md` - Post-decision regret analysis without hindsight bias
- See [prompts/identity/README.md](./prompts/identity/README.md) for composition patterns

**Habits & Behavior Change (`prompts/habits/`)** - 6 prompts for building and breaking habits
- `habits_habit_design_blueprint.md` - Design a new habit (cue → routine → reward + implementation intention)
- `habits_break_bad_habit_protocol.md` - Remove an unwanted habit via friction + reward-matched substitution
- `habits_habit_stacking_designer.md` - Anchor a new habit onto a reliable existing routine
- `habits_streak_recovery_plan.md` - Recover from a missed streak without the all-or-nothing spiral
- `habits_keystone_habit_identifier.md` - Find the single habit whose change cascades into others
- `habits_environment_design_for_habits.md` - Engineer cue visibility and friction for one habit loop
- See [prompts/habits/README.md](./prompts/habits/README.md)

**Resilience & Motivation (`prompts/resilience/`)** - 6 prompts, non-clinical self-direction
- `resilience_setback_recovery_framework.md` - Structured four-stage recovery after a concrete setback
- `resilience_motivation_diagnosis.md` - Diagnose which driver is missing (clarity / energy / reward / identity)
- `resilience_self_discipline_system.md` - Build a willpower-independent consistency system
- `resilience_failure_reframe.md` - Extract transferable lessons without toxic positivity or self-condemnation
- `resilience_anti_fragility_audit.md` - Classify domains fragile/robust/antifragile; prescribe barbell moves
- `resilience_momentum_rebuild.md` - Anti-heroic re-entry ladder after a long stall
- See [prompts/resilience/README.md](./prompts/resilience/README.md)

**Relationships & Social (`prompts/relationships/`)** - 6 prompts, personal (non-work, non-clinical)
- `relationships_boundary_setting_script.md` - Turn a recurring frustration into a statable, spoken boundary
- `relationships_hard_conversation_prep.md` - Prep one emotionally hard personal conversation
- `relationships_network_cultivation_plan.md` - Sustainable, low-guilt personal-relationship maintenance
- `relationships_social_skill_development.md` - Deliberate-practice loop for one observable social skill
- `relationships_conflict_repair_guide.md` - Repair after a rupture (responsibility map + calibrated apology)
- `relationships_relationship_audit.md` - Lightweight single-relationship health-check
- See [prompts/relationships/README.md](./prompts/relationships/README.md)

**Major Personal Decisions (`major-decisions/`)** - 10 prompts for high-stakes personal decisions
- Job-offer evaluation, relocation, quit-or-persist, education-program choice, family-planning tradeoffs, financial-decision framework, health-decision research, major-purchase research, cofounder/partner selection, difficult-relationship audit
- See [major-decisions/README.md](./major-decisions/README.md)

---

## Templates

### Template 1: Life Decision Analysis

```markdown
# Decision Analysis: [The Decision]

**Objective:** Systematically explore a major life decision with full context

## The Decision

**What's Being Decided:**
[Describe the choice in neutral terms - not "should I quit my job" but "career transition decision"]

**Timeline:**
- When must this be decided? [Date or "no hard deadline"]
- When would the decision take effect? [Timeline]
- Is this reversible? [Fully / Partially / Irreversible]

## Your Context

**Current Situation:**
- Where you are now: [Current state]
- How you got here: [Relevant history]
- What prompted this decision: [Trigger]

**Stakeholders:**
| Person/Group | Their Stakes | Their Likely View |
|--------------|--------------|-------------------|
| [Stakeholder 1] | [What they care about] | [Supportive/Concerned/Neutral] |

**Constraints:**
- Financial: [Savings, obligations, risk tolerance]
- Family/Relationships: [Commitments, dependencies]
- Health: [Any relevant considerations]
- Time: [Deadlines, windows of opportunity]

**Values (Rank 1-5):**
- Security vs. Growth: [Which matters more?]
- Independence vs. Stability: [Which matters more?]
- Present vs. Future: [Sacrifice now for later, or live now?]
- Self vs. Others: [Your needs vs. others' needs]

## Analysis Instructions

### 1. Map the Options
For each realistic option (including status quo):
- What does this path look like in 1 year? 5 years?
- What doors does it open?
- What doors does it close?
- What's the worst realistic outcome?
- What's the best realistic outcome?

### 2. Explore Trade-offs
| Dimension | Option A | Option B | Status Quo |
|-----------|----------|----------|------------|
| Financial | [Impact] | [Impact] | [Current] |
| Relationships | [Impact] | [Impact] | [Current] |
| Growth | [Impact] | [Impact] | [Current] |
| Security | [Impact] | [Impact] | [Current] |
| Fulfillment | [Impact] | [Impact] | [Current] |

### 3. Challenge Assumptions
- What am I assuming that might not be true?
- What would change if [key assumption] were wrong?
- Am I giving enough weight to [often-neglected factor]?

### 4. Emotional Inventory
- What am I afraid of?
- What am I excited about?
- What would I regret NOT trying?
- What would future-me wish I had considered?

### 5. Generate Insight
Based on this analysis:
- What's the actual decision here? (Sometimes it's not what we think)
- What would make this decision easier?
- Is there a smaller experiment I could run first?
- What would I advise a friend in this situation?

## Output Format

### Summary
[What this analysis revealed about the decision]

### The Real Trade-off
[What you're actually choosing between]

### Hidden Considerations
[Things that weren't obvious at first]

### Recommended Next Steps
1. [Specific action - small, immediate]
2. [Information to gather]
3. [Conversation to have]

### What Would Change the Analysis
[If X happens, reconsider Y]
```

### Template 2: Goal Setting Framework

```markdown
# Goal Framework: [Goal Area]

**Objective:** Design an effective, personally-aligned goal system

## Goal Exploration

**What You Want (Initial Statement):**
[State the goal as you currently think of it]

**Why This Matters:**
- Surface reason: [What you'd tell others]
- Deeper reason: [What's really driving this]
- What achieving this would change: [Concrete differences in your life]

**What You've Tried Before:**
- Previous attempts: [What happened]
- What worked: [Elements to keep]
- What didn't: [Patterns to avoid]
- What's different now: [Why this time might be different]

## Goal Refinement

### Specificity Check
- Is this measurable? [How will you know you achieved it?]
- Is the timeline realistic? [Based on what evidence?]
- Is this within your control? [External dependencies?]

### Motivation Check
- Intrinsic motivation: [Do you want this for yourself?]
- External pressure: [Are others pushing this?]
- Alignment with values: [Does this fit who you want to be?]

### Trade-off Acknowledgment
- What will you sacrifice to achieve this? [Time, money, other goals]
- Are you willing to make those sacrifices? [Honest answer]
- What will you NOT do while pursuing this? [Anti-goals]

## Implementation Design

### Break Down the Goal
| Milestone | Success Criteria | Target Date | How You'll Know |
|-----------|-----------------|-------------|-----------------|
| [First milestone] | [Specific criteria] | [Date] | [Evidence] |
| [Second milestone] | [Specific criteria] | [Date] | [Evidence] |

### Habit/System Design
**Daily Actions:**
- [Small, specific daily habit]
- Trigger: [When/where you'll do it]
- Reward: [How you'll mark completion]

**Weekly Actions:**
- [Larger weekly activity]
- Scheduled time: [When]

### Obstacle Planning
| Likely Obstacle | Pre-planned Response |
|-----------------|---------------------|
| [Obstacle 1] | [What you'll do] |
| [Obstacle 2] | [What you'll do] |
| [Motivation dip] | [Recovery strategy] |

### Accountability
- How you'll track: [Method]
- Who you'll tell: [Accountability partner]
- How often you'll review: [Frequency]

## Output Format

### Refined Goal Statement
[Specific, measurable, time-bound version]

### Why This Version
[What changed from initial statement and why]

### First Week Action Plan
Day 1: [Specific action]
Day 2: [Specific action]
...

### Warning Signs to Watch For
- [Sign that goal needs revisiting]
- [Sign of burnout approaching]

### 30-Day Check-in Questions
1. Is this still the right goal?
2. Is the pace sustainable?
3. What needs adjusting?
```

### Template 3: Career Transition Analysis

```markdown
# Career Transition Analysis

**Objective:** Systematically evaluate a career change decision

## Current State Assessment

**Current Role:**
- Title/Function: [What you do]
- Time in role: [Duration]
- Company/Industry: [Context]

**Satisfaction Inventory:**
| Dimension | Rating (1-10) | What's Working | What's Not |
|-----------|---------------|----------------|------------|
| Work itself | [Score] | [Specifics] | [Specifics] |
| Growth/Learning | [Score] | [Specifics] | [Specifics] |
| Compensation | [Score] | [Specifics] | [Specifics] |
| Culture/People | [Score] | [Specifics] | [Specifics] |
| Work-life balance | [Score] | [Specifics] | [Specifics] |
| Meaning/Impact | [Score] | [Specifics] | [Specifics] |

**Why Now:**
[What triggered this consideration?]

## Target State Exploration

**Possible Directions:**
| Direction | Appeal | Concerns | Knowledge Level |
|-----------|--------|----------|-----------------|
| [Option 1] | [Why attractive] | [Worries] | [How much do you know?] |
| [Option 2] | [Why attractive] | [Worries] | [How much do you know?] |
| [Option 3] | [Why attractive] | [Worries] | [How much do you know?] |

**What You're Optimizing For:**
- Must have: [Non-negotiables]
- Nice to have: [Preferences]
- Willing to sacrifice: [Trade-offs accepted]

## Gap Analysis

**Skills Assessment:**
| Skill Needed | Current Level | Gap | How to Close |
|--------------|---------------|-----|--------------|
| [Skill 1] | [1-10] | [Size] | [Path] |
| [Skill 2] | [1-10] | [Size] | [Path] |

**Experience Gaps:**
- What experience do you lack?
- How could you get it? (Projects, volunteering, courses)

**Network Gaps:**
- Who do you know in target field?
- How could you build connections?

## Risk Analysis

**Financial:**
- Current runway: [Months without income]
- Minimum required income: [Amount]
- Timeline to replacement income: [Estimate]

**Career:**
- Reversibility: [Can you go back?]
- Reputation risk: [How will this look?]
- Opportunity cost: [What you're giving up]

**Personal:**
- Family impact: [Support? Concerns?]
- Stress tolerance: [Can you handle uncertainty?]
- Identity: [How much is your identity tied to current role?]

## Decision Framework

### Before Deciding, Learn:
- [ ] Informational interviews with [X] people in target field
- [ ] Understand realistic compensation range
- [ ] Know typical transition timeline
- [ ] Test skills/interest through [project/course/volunteer]

### Decision Criteria:
[What would need to be true to make this decision confidently?]

### Minimum Viable Move:
[Smallest step that would test this direction]

## Output Format

### Summary Assessment
[Key findings about fit, risk, and readiness]

### Recommendation
[Not "do this" but "consider X based on Y"]

### Immediate Next Steps
1. [Specific, small action]
2. [Information to gather]
3. [Person to talk to]

### Decision Timeline
[When should you decide, and what should you know by then?]
```

---

## Worked Example

### Scenario: Career Change Decision

**User says:** "I'm thinking about leaving my corporate job to start a business. I've been thinking about this for years but I'm scared. Should I do it?"

**Step 1: Classification**

- Task Type: DECIDE
- Domain: Personal Development
- Specific Area: Major life decision / Career transition

**Step 2: Context Gathering**

**What we know:**
- Considering leaving corporate job
- Want to start a business
- Has been thinking for "years"
- Feeling scared

**What we need:**
- Current financial situation
- Family obligations
- Business idea specifics
- What "scared" means (risk, failure, judgment?)
- What they've tried already
- Why now?

**Step 3: Apply Template**

Use **Template 1: Life Decision Analysis** combined with **Template 3: Career Transition Analysis**

**Step 4: Quality Check**

Before responding, ensure:
- [ ] Not giving generic "follow your dreams" advice
- [ ] Acknowledging fear as valid data
- [ ] Surfacing trade-offs explicitly
- [ ] Providing actionable next steps
- [ ] Not making the decision for them

**Final Approach:**

```markdown
# Career Transition Decision Support

Rather than giving you an answer (only you can decide this), let me help you think through this systematically.

## First, Let's Understand Your Context

**The Basics:**
- How long have you been in your current role/company?
- What's your financial situation (savings, obligations, risk tolerance)?
- Do you have dependents or a partner whose income/support matters?
- What's the business idea (or is it still undefined)?

**The "Years of Thinking":**
- What has stopped you before?
- What's different now that has you considering it seriously?
- Have you taken any steps toward this (side projects, testing the idea)?

**The Fear:**
- When you imagine doing it, what specifically scares you?
  - Financial ruin?
  - Failure and embarrassment?
  - Giving up security?
  - Letting others down?
  - The unknown?
- When you imagine NOT doing it, what do you feel?
  - Relief?
  - Regret?
  - Safety?

## The Real Question

Often, "Should I start a business?" is actually one of these questions:
- "How do I reduce the risk enough to feel comfortable?"
- "How do I know if my idea is good enough?"
- "How do I give myself permission to try?"
- "How do I handle the fear?"

**Which resonates most with you?**

## Trade-offs to Consider

| If You Stay | If You Leave |
|-------------|--------------|
| Known income, benefits, stability | Income uncertainty, potential upside |
| Limited autonomy, corporate constraints | Full autonomy, full responsibility |
| Career path is visible | Career path is unclear |
| Regret of "what if" | Regret of "why did I" (if it fails) |
| Time for other life areas | Business may consume everything |

## Before Deciding: Minimum Viable Experiment

Instead of "stay or go," consider:
1. **Can you test the business idea while employed?** (Nights/weekends, validate demand)
2. **What would make you confident it could work?** (Revenue? Customers? Skills?)
3. **What's your runway?** (How long could you try before needing to return to employment?)
4. **Is there a middle path?** (Part-time, sabbatical, consulting transition)

## What I'd Suggest

Don't decide "should I start a business." Instead:
1. **Define the business** - What specifically would you do?
2. **Test the idea** - Can you get one customer while still employed?
3. **Calculate your runway** - How long could you sustain yourself?
4. **Set a decision criteria** - "If X happens in 6 months, I'll make the leap"

The goal isn't to eliminate fear—it's to make an informed bet you can live with either way.

**What's the business idea you're considering?**
```

---

## Anti-Patterns for Personal Development

### Mistake 1: Generic Inspiration Instead of Practical Guidance

**Problem:** Motivational platitudes that don't help

**Bad:**
```
"Believe in yourself! Follow your passion! Life's too short for regrets!"
```

**Good:**
```
"Given your 18-month runway and validated customer interest, the risk is bounded. Here's a framework for deciding: If you can get 3 paying customers in the next 6 months while employed, that's evidence the business has legs. What would need to be true for you to feel confident?"
```

---

### Mistake 2: Ignoring Emotional Validity

**Problem:** Treating feelings as obstacles to overcome

**Bad:**
```
"Don't let fear hold you back! Fear is just False Evidence Appearing Real!"
```

**Good:**
```
"Fear makes sense here—you're considering a major change with real consequences. Let's understand what specifically you're afraid of. Some fears point to real risks we should mitigate. Others might be assumptions we can examine."
```

---

### Mistake 3: One-Size-Fits-All Advice

**Problem:** Generic recommendations that ignore context

**Bad:**
```
"Everyone should have 6 months of expenses saved before starting a business."
```

**Good:**
```
"The 'right' runway depends on your situation:
- If you're single, no debt, live cheaply: 6 months might be plenty
- If you have a family, mortgage, health insurance needs: 12-18 months might feel more comfortable
- If you have a working spouse with benefits: Less cash needed

What's YOUR situation?"
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║              PERSONAL DEVELOPMENT QUICK REFERENCE                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  BEFORE GIVING ADVICE, UNDERSTAND:                                        ║
║  □ Values - What matters most to this person?                            ║
║  □ Constraints - Financial, family, health, time                         ║
║  □ History - What have they tried? What happened?                        ║
║  □ Stakes - What's really at risk here?                                  ║
║  □ Emotions - What are they feeling and why?                             ║
║                                                                           ║
║  ALWAYS INCLUDE:                                                          ║
║  □ Trade-offs made explicit (every choice has costs)                     ║
║  □ Emotional validation (feelings are data)                              ║
║  □ Actionable next steps (specific, small, immediate)                    ║
║  □ Uncertainty acknowledgment (no guaranteed outcomes)                   ║
║  □ Context-specific guidance (not generic platitudes)                    ║
║                                                                           ║
║  RED FLAG PHRASES TO AVOID:                                               ║
║  ✗ "You should definitely..." → ✓ "Given your situation, options are..." ║
║  ✗ "Don't let fear hold you back" → ✓ "Let's examine what the fear is   ║
║     telling you..."                                                       ║
║  ✗ "Follow your passion!" → ✓ "What specifically excites you about this, ║
║     and how might you test it?"                                          ║
║  ✗ "Everything will work out" → ✓ "Here's how to improve your odds..."  ║
║                                                                           ║
║  FOR MAJOR DECISIONS:                                                     ║
║  1. Map options (including status quo)                                    ║
║  2. Surface trade-offs for each                                          ║
║  3. Identify what would need to be true                                  ║
║  4. Find minimum viable experiments                                       ║
║  5. Define decision criteria and timeline                                 ║
║                                                                           ║
║  FOR GOAL SETTING:                                                        ║
║  1. Explore the "why" behind the goal                                    ║
║  2. Make it specific and measurable                                       ║
║  3. Acknowledge trade-offs explicitly                                     ║
║  4. Design systems, not just outcomes                                     ║
║  5. Plan for obstacles in advance                                         ║
║                                                                           ║
║  EXEMPLAR PROMPTS TO STUDY:                                               ║
║  • validation_final_gate.md (decision verification)                       ║
║  • validation_am_i_being_nuts.md (sanity checking)                       ║
║  • career_90_day_repositioning_plan.md (career guidance)                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [prompts/](./prompts/) | All personal development prompts (consolidated here) |
| [domain-productivity/](../domain-productivity/) | Productivity and validation prompts |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |

---

*Document Version: 2.0*
*Created: 2026-01-26*
*Updated: 2026-03-05*
*Domain: Personal Development*

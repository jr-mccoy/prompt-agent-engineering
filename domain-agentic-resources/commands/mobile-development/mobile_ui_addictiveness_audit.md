---
name: mobile_ui_addictiveness_audit
description: Orchestrate a comprehensive audit of an app's engagement and habit-forming potential across behavioral psychology frameworks, analyzing triggers, core loops, reward systems, retention mechanics, and emotional design to produce an actionable engagement improvement plan
version: "1.0.0"
category: mobile-development
tags: [mobile, ui, ux, engagement, retention, addiction, habit-loop, gamification, hook-model, behavioral-design]
agents_used: [mobile-ui-addiction-architect, mobile-ui-element-analyzer, mobile-ui-competitive-teardown]
---

Orchestrate a comprehensive audit of an app's habit-forming potential, coordinating 3 specialized agents across 5 phases to evaluate and enhance every engagement dimension from trigger design to long-term retention:

[Extended thinking: This workflow answers the fundamental question: "Why don't users come back?" and "How do we make them feel like they can't do without this app?" It applies behavioral psychology frameworks (Hook Model, Fogg Behavior Model, gamification science) systematically to every aspect of the user experience.

The key insight is that "addictiveness" is not a single feature — it's a system. Streaks alone don't work. Notifications alone don't work. Gamification alone doesn't work. What works is a complete engagement system where triggers, actions, rewards, and investments reinforce each other in a cycle that deepens over time.

The workflow uses 3 agents:
- Addiction Architect (Opus): The behavioral strategist — maps the current engagement system and designs improvements
- Element Analyzer (Opus): The detail specialist — evaluates specific UI elements that need engagement enhancement
- Competitive Teardown (Opus): The competitive eye — shows what top apps in the category do for engagement

Three user interaction gates ensure ethical alignment:
1. After current state mapping: Developer confirms what user behaviors they want to encourage
2. After gap analysis: Developer prioritizes which engagement dimensions to improve
3. After design: Developer approves engagement features before implementation planning

The workflow explicitly includes an ethics checkpoint — engagement should create genuine user value, not exploitation.]

## Configuration

### Supported Flags
- `--category=<app-category>`: App Store category for competitive benchmarking
- `--stage=pre-launch|early|growth|mature`: App lifecycle stage (affects recommendations)
- `--focus=triggers|core-loop|rewards|retention|onboarding|social|all`: Focus area (default: all)
- `--ethical-mode=strict|balanced`: Strict avoids all loss aversion; balanced uses ethical engagement patterns (default: balanced)
- `--platform=ios|android|both`: Target platform (default: both)

### Parameters
- `$ARGUMENTS`: App description, current engagement metrics (if available), and specific engagement concerns

## Phase 1: Current Engagement Mapping

### 1. Engagement System Audit
- Use Task tool with subagent_type="mobile-ui-addiction-architect"
- Prompt: "Perform a complete engagement system audit of the app: $ARGUMENTS.

  Map the current state across all behavioral dimensions:

  **1. Hook Model Assessment**
  - External triggers: What triggers currently exist? (notifications, badges, emails, widgets)
  - Internal triggers: What emotional states could drive users to this app? Are they currently activated?
  - Core action: What is the fundamental action users take? How many steps? How much friction?
  - Variable rewards: What rewards does the app provide? Are they variable or predictable? Which reward type (Tribe/Hunt/Self)?
  - Investment: What do users contribute that increases value? (content, data, social graph, preferences, reputation)

  **2. Fogg Behavior Model Assessment**
  - Motivation: What motivates users? (pleasure/pain, hope/fear, social acceptance/rejection)
  - Ability: How easy is the core action? (time, money, physical effort, brain cycles, social deviance, non-routine)
  - Prompts: Are prompts timed correctly? Are they the right type (spark/facilitator/signal)?

  **3. Engagement Loop Mapping**
  - Core loop: What is the repeatable action→reward cycle? (or is there none?)
  - Session loop: What keeps users engaged within a single session?
  - Daily loop: What brings users back each day?
  - Weekly loop: What creates weekly engagement?
  - Progression loop: How does the experience deepen over months?

  **4. Retention Feature Inventory**
  - Streaks: Present? Mechanic details?
  - Progress systems: Levels, XP, completion metrics?
  - Achievement/badges: Present? How many? Quality?
  - Social features: Likes, follows, activity feeds, friend comparisons?
  - Personalization: How does the app adapt to individual users?
  - Daily/recurring features: Daily challenges, daily content, time-limited elements?

  **5. Onboarding Engagement**
  - Time-to-value: How quickly does a new user experience the app's core value?
  - Commitment devices: Does onboarding create investment (goal setting, personalization)?
  - First session reward: What reward does the first session provide?

  Score each dimension:
  | Dimension | Score (1-10) | Current State | Gap Description |

  Provide an overall Engagement System Score (1-100)."
- Expected output: Complete engagement system map with scores and gap identification
- Context: This is the first phase — establishes baseline engagement posture

### USER INTERACTION GATE 1
Present the engagement map to the developer and ask:

"Here's your app's current engagement system mapped across all behavioral dimensions. Before I identify specific improvements:

1. **What user behaviors** do you most want to encourage? (Daily use? Feature adoption? Content creation? Social interaction? Purchasing?)
2. **What's your biggest retention problem?** (Users don't come back after day 1? They churn after a week? They use it but not daily?)
3. **Ethical boundaries:** Are there engagement patterns you want me to avoid? (No notifications? No streaks? No FOMO?)
4. **Current metrics** (if available): DAU/MAU ratio, D1/D7/D30 retention, session frequency, session duration?

This helps me focus on the engagement gaps that matter most for your specific goals."

**STOP and wait for developer response. Do not proceed to Phase 2 until the developer has provided direction.**

## Phase 2: Competitive Engagement Benchmarking

### 2. Category Engagement Analysis
- Use Task tool with subagent_type="mobile-ui-competitive-teardown"
- Prompt: "Analyze the engagement systems of top-performing apps in the same category as: $ARGUMENTS.

  Developer's engagement goals: [FROM GATE 1 INPUT]
  Developer's ethical boundaries: [FROM GATE 1 INPUT]

  For each of the top 5 apps in this category, analyze:
  1. **Core engagement loop:** What is the primary repeatable cycle?
  2. **Trigger strategy:** How do they bring users back? (notification frequency, types, timing)
  3. **Reward system:** What rewards do they provide? (social, content, progress, achievement)
  4. **Retention mechanics:** Streaks, daily rewards, progress systems, social obligation
  5. **Onboarding hook:** How quickly do new users experience value?
  6. **Investment depth:** What user investment makes leaving costly?

  Produce a competitive engagement matrix:
  | Engagement Dimension | Their App | Top App 1 | Top App 2 | Top App 3 | Category Standard |

  Identify:
  - **Table stakes:** Engagement features every app in this category must have
  - **Differentiators:** Features only the best apps have
  - **Opportunities:** Engagement patterns no competitor has implemented yet

  Rate the user's app against category engagement standards:
  - Below standard / At standard / Above standard / Category leader"
- Expected output: Competitive engagement benchmark with gap analysis
- Context from previous: Engagement system map from Phase 1, developer goals from Gate 1

## Phase 3: Engagement Gap Analysis & Design

### 3. Engagement System Design
- Use Task tool with subagent_type="mobile-ui-addiction-architect"
- Prompt: "Design engagement improvements for: $ARGUMENTS.

  Current engagement map: [PHASE 1 OUTPUT]
  Competitive benchmarks: [PHASE 2 OUTPUT]
  Developer's goals: [GATE 1 INPUT]
  Ethical boundaries: [GATE 1 INPUT]

  For each gap identified, design a specific engagement feature:

  **Trigger Design:**
  - Map internal triggers: What emotions should connect to opening this app?
  - Design external triggers: Notification templates, badge rules, widget design, email digest format
  - Trigger timing: When during the day/week should each trigger fire?
  - Trigger escalation: How should trigger frequency change based on user engagement level?

  **Core Loop Optimization:**
  - Redesign or optimize the core action→reward cycle
  - Reduce friction: Identify every unnecessary step and eliminate it
  - Add variable reward: How can each session feel different?
  - Add investment: What can users contribute that makes leaving costly?

  **Retention System Design:**
  - Streak mechanics (if appropriate): Complete design including display, milestones, protection, recovery
  - Progress system: XP/levels/completion design with tier structure
  - Achievement system: Badge categories, unlock criteria, display format
  - Daily engagement driver: What specific reason brings users back tomorrow?
  - Weekly engagement driver: What creates weekly ritual?

  **Social Proof System:**
  - Activity indicators: What social signals should be visible?
  - Social reward: How does social interaction create reward?
  - Social obligation: What creates healthy social accountability?
  - Sharing mechanics: What's worth sharing? How easy is sharing?

  **Emotional Design:**
  - Delight moments: Where should micro-celebrations occur?
  - Comfort patterns: What creates familiarity and safety?
  - Pride builders: What creates shareable accomplishment?
  - Belonging signals: What creates community feeling?

  For each recommendation, provide:
  - The psychological mechanism at work (name the principle)
  - A reference app that executes this well
  - Exact UI specification (component design, animation timing, copy)
  - Expected impact on retention metrics
  - Effort estimate (trivial / small / medium / large)

  ## Ethics Checkpoint
  For each recommendation, verify:
  □ Creates genuine user value
  □ User can opt out easily
  □ Transparent about how it works
  □ Respects user's time and attention
  □ Would survive public scrutiny

  Prioritize recommendations by impact-to-effort ratio."
- Expected output: Complete engagement improvement design with specifications and prioritization
- Context from previous: All previous phase outputs

### USER INTERACTION GATE 2
Present the engagement design to the developer and ask:

"Here's the complete engagement improvement plan. Please review and tell me:

1. **Which features** do you want to implement? (Select by priority number, or 'all')
2. **Which features** should be deferred to a later release?
3. **Any features** that conflict with your product vision or values?
4. **Implementation order preference:** Quick wins first, or most impactful first?

I'll produce detailed implementation specifications for your selected features."

**STOP and wait for developer response. Do not proceed to Phase 4 until the developer has selected features.**

## Phase 4: UI Implementation Specification

### 4. Element-Level Implementation Design
- Use Task tool with subagent_type="mobile-ui-element-analyzer"
- Prompt: "Design detailed UI specifications for the selected engagement features: $ARGUMENTS.

  Selected features: [DEVELOPER SELECTIONS FROM GATE 2]
  Engagement designs: [PHASE 3 OUTPUT]
  Platform: [FROM FLAGS]

  For each selected engagement feature, produce implementation-ready UI specifications:

  **Component Design:**
  - Visual design: Colors (hex, light + dark mode), dimensions (dp/pt), corner radius, shadows, typography
  - Layout: Position on screen, spacing relative to other elements, responsive behavior
  - Content: Copy/text for all states, icon specifications, imagery requirements

  **Interaction Design:**
  - Touch feedback: Press state animation (scale, opacity, timing, easing)
  - Haptic feedback: Type (light/medium/heavy impact, success/error notification, selection)
  - Sound feedback: When applicable, describe the audio cue
  - Gesture support: Swipe, long-press, drag interactions

  **Animation Design:**
  - Entry animation: How the component appears (duration, easing, properties)
  - State transitions: How the component changes between states
  - Celebration animations: For achievements, milestones, completions (duration, effect type)
  - Attention animation: Pulsing, glowing, bouncing for elements that need attention

  **State Design:**
  - Default, active, completed, locked, earned states
  - Progress states (0%, 25%, 50%, 75%, 100%)
  - Error and recovery states

  **Accessibility:**
  - VoiceOver/TalkBack labels for all states
  - Dynamic type behavior
  - Reduced motion alternatives

  Order components by implementation dependency and provide estimated implementation time for each."
- Expected output: Complete UI component specifications for all selected engagement features
- Context from previous: Selected features and engagement designs from previous phases

## Phase 5: Implementation Roadmap

### 5. Prioritized Roadmap
- Use Task tool with subagent_type="mobile-ui-addiction-architect"
- Prompt: "Produce a final implementation roadmap for the engagement improvements to: $ARGUMENTS.

  All UI specifications: [PHASE 4 OUTPUT]
  Developer's priorities: [GATE 2 INPUT]

  Create:

  ## Sprint 1: Foundation (Week 1-2)
  - Core loop optimization (reduce friction, add immediate reward)
  - Basic engagement metrics instrumentation
  - Essential trigger system setup

  ## Sprint 2: Retention (Week 3-4)
  - Primary retention mechanic (streak, progress, or achievement system)
  - Daily engagement driver
  - Re-engagement notification templates

  ## Sprint 3: Depth (Week 5-6)
  - Social proof elements
  - Personalization hooks
  - Secondary engagement mechanics

  ## Sprint 4: Polish (Week 7-8)
  - Celebration animations and delight moments
  - Notification timing optimization
  - A/B test setup for engagement features

  For each sprint:
  - Specific deliverables
  - Success metrics to track
  - Risks and mitigations
  - Dependencies

  ## Measurement Plan
  Define how to measure the impact of engagement improvements:
  | Metric | Baseline | Target (30 days) | Target (90 days) | How to Measure |

  Include DAU/MAU, D1/D7/D30 retention, session frequency, session duration, core action rate, notification open rate."
- Expected output: Sprint-level implementation roadmap with measurement plan
- Context from previous: All previous phase outputs

## Success Criteria

### Analysis Criteria
- ✅ Current engagement system mapped across all Hook Model and Fogg dimensions
- ✅ Competitive engagement benchmark completed for category
- ✅ Engagement gaps identified and prioritized
- ✅ Each recommendation includes psychological mechanism and reference app

### Design Criteria
- ✅ Engagement features have complete UI specifications
- ✅ All features pass the ethics checkpoint
- ✅ Specifications include exact values (colors, timing, dimensions)
- ✅ Both platforms addressed (if both selected)
- ✅ Accessibility requirements met

### Process Criteria
- ✅ Developer consulted at both interaction gates
- ✅ No features designed that conflict with developer's ethical boundaries
- ✅ Implementation roadmap is realistic and dependency-ordered
- ✅ Measurement plan enables data-driven iteration

## Coordination Notes

- **Phase ordering is strict:** Current state → Competitive benchmark → Gap analysis & design → UI specification → Roadmap
- **Ethics are non-negotiable:** Every engagement recommendation must pass the ethics checkpoint. If a feature only works through deception or exploitation, it is excluded regardless of impact.
- **Competitive benchmark informs design:** Phase 2 must complete before Phase 3 so the gap analysis has category context.
- **Implementation specifications are platform-specific:** Phase 4 produces different specs for iOS vs Android if both are selected.
- **Measurement drives iteration:** The roadmap includes specific metrics and targets. After Sprint 1 ships, metrics should be reviewed before proceeding to Sprint 2 — the plan may need adjustment based on real data.
- **Pair with element audits:** After the engagement system is designed, use `mobile_ui_element_audit` to polish individual elements (buttons, cards, navigation) that are part of the engagement system.

Target: $ARGUMENTS

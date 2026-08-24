---
name: mobile_ui_trend_report
description: Generate a comprehensive mobile UI trend report covering visual design, interaction patterns, engagement mechanics, and platform-specific innovations with actionable recommendations tailored to the user's app category and tech stack
version: "1.0.0"
category: mobile-development
tags: [mobile, ui, ux, trends, design, research, competitive-analysis, ios, android, engagement]
agents_used: [mobile-ui-trend-researcher, mobile-ui-competitive-teardown, mobile-ui-addiction-architect]
---

Generate a comprehensive mobile UI trend report by coordinating 3 specialized agents to research current trends, analyze competitor implementations, and identify engagement opportunities:

[Extended thinking: This workflow produces a strategic UI trend report that goes beyond "what's trendy" to answer "what should we build." The three agents provide complementary perspectives: the Trend Researcher identifies what's happening across the industry, the Competitive Teardown agent shows what direct competitors are doing (and what they're missing), and the Addiction Architect identifies which engagement patterns have the highest impact for the user's specific app category.

The report is structured to be directly actionable — each trend includes implementation feasibility, expected user impact, and prioritization guidance. The user interaction gate after Phase 1 ensures the research is directed at the most relevant competitors and app category.

This workflow is best run quarterly or before a major design refresh to ensure the team has current competitive intelligence.]

## Configuration

### Supported Flags
- `--category=<app-category>`: App Store category (social, fitness, fintech, e-commerce, productivity, education, entertainment, health, news)
- `--platform=ios|android|both`: Target platform(s) (default: both)
- `--competitors=<app1,app2,app3>`: Specific competitors to analyze
- `--focus=visual|interaction|engagement|navigation|all`: Focus area (default: all)
- `--output=summary|detailed|executive`: Report depth (default: detailed)

### Parameters
- `$ARGUMENTS`: App name/description, category, target audience, and current design state

## Phase 1: Broad Trend Research

### 1. Industry Trend Scan
- Use Task tool with subagent_type="mobile-ui-trend-researcher"
- Prompt: "Produce a comprehensive mobile UI trend scan for the following app context: $ARGUMENTS.

  Research and report on:

  **Visual Design Trends (2025-2026)**
  - Color system trends (dynamic color, gradient evolution, dark mode maturation)
  - Typography trends (variable fonts, kinetic type, expressive hierarchy)
  - Layout trends (bento grids, adaptive layouts, foldable-aware design)
  - Shape and depth trends (glassmorphism/Liquid Glass, spatial layering, 3D elements)
  - Iconography trends (animated icons, dual-tone, contextual icon states)

  **Interaction Pattern Trends**
  - Navigation evolution (gesture navigation, floating tab bars, contextual menus)
  - Input innovation (voice + touch hybrid, camera-first, AI-assisted input)
  - Animation trends (physics-based motion, scroll-linked animation, shared element transitions)
  - Haptic design maturation (custom haptic patterns, multi-sensory feedback)

  **Platform-Specific Updates**
  - iOS: Latest HIG changes, SwiftUI capabilities, Dynamic Island, Live Activities, StandBy, visionOS crossover
  - Android: Material Design 3 updates, Compose capabilities, Predictive Back, large screen support, themed icons

  **Emerging Technology Impact**
  - AI-driven adaptive UI
  - Spatial design for phones
  - Foldable device design patterns
  - Wearable companion design

  For each trend:
  - Current adoption level (early adopter / growing / mainstream / declining)
  - Relevance to the user's app category (high / medium / low)
  - 2-3 specific apps that exemplify this trend
  - Implementation complexity (trivial / moderate / significant)

  Organize by relevance to the user's specific app category."
- Expected output: Categorized trend report with relevance scoring
- Context: This is the first phase — establishes the trend landscape

### USER INTERACTION GATE 1
Present the trend scan to the developer and ask:

"Here's the current trend landscape relevant to your app. Before I analyze competitors and engagement opportunities:

1. **Which trends** interest you most? (I'll prioritize these in competitor analysis)
2. **Who are your top 3-5 competitors?** (I'll analyze their UI specifically)
3. **What's your current design challenge?** (Modernization? Retention? Visual refresh? Engagement?)

This helps me focus the deep research on what will actually help you."

**STOP and wait for developer response. Do not proceed to Phase 2 until the developer has provided direction.**

## Phase 2: Competitive Intelligence (PARALLEL)

### 2a. Competitor UI Teardown
- Use Task tool with subagent_type="mobile-ui-competitive-teardown"
- Prompt: "Perform a comparative UI teardown of the following competitors for the app: $ARGUMENTS.

  Competitors to analyze: [FROM GATE 1 INPUT]
  Trends to prioritize: [FROM GATE 1 INPUT]

  For each competitor, analyze:
  1. **Visual Design Language**: Color system, typography, spacing, component styles — extract exact values where possible
  2. **Navigation Architecture**: Primary navigation pattern, secondary navigation, gesture shortcuts
  3. **Key Screen Designs**: Home/feed, detail/content, profile, settings, onboarding — how do they structure information?
  4. **Micro-Interactions**: What animations, transitions, and feedback patterns do they use?
  5. **Loading & Error States**: How do they handle waiting, failures, and empty content?
  6. **Unique Innovations**: What does this competitor do that no one else does?
  7. **Weaknesses**: Where does their UI fall short? What opportunity does this create for you?

  Produce a comparison matrix:
  | Feature/Pattern | Your App | Competitor A | Competitor B | Competitor C | Best Practice |

  Identify the top 5 UI patterns your competitors use that you don't — prioritized by user impact."
- Expected output: Competitor comparison matrix with gap analysis
- Context from previous: Developer's competitor list and focus areas from Gate 1

### 2b. Engagement Pattern Analysis
- Use Task tool with subagent_type="mobile-ui-addiction-architect"
- Prompt: "Analyze the engagement systems used by top apps in the same category as: $ARGUMENTS.

  Priority trends from developer: [FROM GATE 1 INPUT]
  Competitors: [FROM GATE 1 INPUT]

  Evaluate engagement patterns across the category:
  1. **Core Loop Design**: What is the primary engagement loop for top apps in this category? How does it compare to the user's app?
  2. **Retention Mechanics**: What streaks, daily rewards, progress systems, or achievement mechanics are standard in this category?
  3. **Trigger Systems**: How do top apps in this category bring users back? Notifications, widgets, email, social?
  4. **Social Proof**: What social proof mechanisms are common? Likes, activity feeds, friend comparisons?
  5. **Personalization Depth**: How deeply do competitors personalize the UI experience?
  6. **Gamification Level**: How gamified are competitor apps? Points, levels, badges, leaderboards?

  For each engagement category:
  - What's standard (table stakes — you must have this)
  - What's differentiated (top apps have this, most don't)
  - What's missing (opportunity no one has seized yet)
  - Recommended implementation for the user's app

  Identify the top 3 engagement gaps — high-impact engagement patterns that competitors have but the user's app doesn't."
- Expected output: Engagement gap analysis with category benchmarks
- Context from previous: Developer's focus areas from Gate 1

---
### CONVERGENCE: Steps 2a and 2b must complete before Phase 3
---

## Phase 3: Strategic Recommendations

### 3. Synthesized Recommendations
- Use Task tool with subagent_type="mobile-ui-trend-researcher"
- Prompt: "Synthesize the trend research, competitor analysis, and engagement gap analysis into a prioritized strategic recommendation report for: $ARGUMENTS.

  Inputs:
  - Trend scan: [PHASE 1 OUTPUT]
  - Competitor teardown: [PHASE 2a OUTPUT]
  - Engagement gap analysis: [PHASE 2b OUTPUT]
  - Developer's priorities: [GATE 1 INPUT]

  Produce a final report with:

  ## Executive Summary
  - 3-sentence overview of findings
  - Overall competitive position (leading / competitive / behind / at risk)
  - The single highest-impact recommendation

  ## Quick Wins (< 1 week effort)
  List 3-5 changes that can be implemented quickly:
  | # | Change | Source (Trend/Competitor/Engagement) | Expected Impact | Effort |

  ## Medium Investments (1-4 weeks)
  List 3-5 strategic improvements:
  | # | Change | Source | Expected Impact | Effort | Dependencies |

  ## Strategic Initiatives (1-3 months)
  List 2-3 major initiatives:
  | # | Initiative | Rationale | Expected Impact | Effort | Risk |

  ## Trends to Watch
  List 3-5 trends that aren't ready for implementation but should be monitored

  ## Trends to Skip
  List 2-3 trends that are overhyped or irrelevant for this app — with reasoning

  ## Competitive Position Matrix
  Visual comparison of the user's app vs competitors across 6 dimensions:
  - Visual Design Quality
  - Interaction Polish
  - Engagement Depth
  - Navigation Clarity
  - Accessibility
  - Innovation

  Every recommendation must include:
  - Why it matters (user impact or competitive advantage)
  - How to implement it (specific enough to start work)
  - What success looks like (metric or observable outcome)"
- Expected output: Complete strategic recommendation report
- Context from previous: All previous phase outputs

## Success Criteria

### Research Criteria
- ✅ Trends cover visual, interaction, engagement, and platform-specific categories
- ✅ Each trend includes adoption level, relevance rating, and specific app examples
- ✅ Competitor analysis covers at least 3 competitors with specific UI comparisons
- ✅ Engagement gap analysis identifies standard, differentiated, and missing patterns

### Recommendation Criteria
- ✅ Quick wins are genuinely achievable in < 1 week
- ✅ Each recommendation includes expected impact and implementation approach
- ✅ Recommendations are prioritized by impact-to-effort ratio
- ✅ Trends-to-skip section prevents waste on irrelevant trends
- ✅ Competitive position is honestly assessed

### Process Criteria
- ✅ Developer was consulted at the interaction gate
- ✅ Research was focused on developer's stated priorities
- ✅ Report is actionable, not just informational

## Coordination Notes

- **Phase 2 runs in parallel:** The competitor teardown and engagement analysis can run simultaneously since they analyze different aspects.
- **Convergence before Phase 3:** Both Phase 2 outputs must complete before the synthesis in Phase 3 can begin.
- **Run quarterly:** This workflow is most valuable when run periodically (quarterly or before design sprints) to maintain current competitive intelligence.
- **Pair with element audits:** After identifying trends and gaps, use the `mobile_ui_element_audit` command to implement specific improvements at the element level.
- **Context passing:** Phase 3 receives all previous outputs to produce a unified synthesis — the trend researcher agent performs the final synthesis because it has the broadest perspective.

Target: $ARGUMENTS

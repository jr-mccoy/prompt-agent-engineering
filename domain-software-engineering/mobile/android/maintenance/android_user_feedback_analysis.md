---
title: "Android User Feedback Analysis"
category: mobile-development
description: "Analyzes Play Store reviews and user feedback to identify patterns, prioritize improvements, and inform development roadmap"
techniques:
  - ST-01
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - analysis
  - android
  - mobile-development
  - user-feedback
  - maintenance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_crash_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/improvement/android_user_experience_enhancement.md
  - domain-software-engineering/mobile/android/publishing/android_play_store_optimization.md
---

# Android User Feedback Analysis

**Objective:** Analyze user feedback from Play Store reviews, support tickets, and other channels to identify patterns, prioritize issues, and translate insights into actionable development tasks.

**When to Use:** Use this prompt when you have collected user feedback (Play Store reviews, support emails, social media comments, in-app feedback) and need to systematically analyze it to inform product decisions and bug fixes. Ideal after app releases, during quarterly planning, or when investigating user-reported issues. Prerequisites include access to feedback data in text form.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before analyzing user feedback, gather context:

1. **Feedback Source:**
   - "What is the source of this feedback? (Play Store, support tickets, in-app, social media)"
   - "What time period does this feedback cover?"
   - "How many feedback items are you analyzing?"

2. **App Context:**
   - "What type of app is this? (productivity, social, e-commerce, etc.)"
   - "Was there a recent release or change that might affect feedback?"
   - "Are there known issues you're already tracking?"

3. **Analysis Goals:**
   - "Are you looking for specific types of issues? (bugs, UX, performance, features)"
   - "Do you want prioritized recommendations or just categorization?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY pattern, you MUST:**

1. **Trace actual feedback themes** - Don't report patterns without sufficient evidence from multiple feedback items.
2. **Check for existing awareness** - Search for known issues or planned features that may already address feedback.
3. **Understand the context** - Consider the feedback source, timing, and whether issues correlate with app changes.
4. **Confirm actual prevalence** - Is this a widespread issue or isolated complaints?
5. **Provide specific examples** - Every pattern must include representative feedback quotes.

**Finding SATISFIED users is an acceptable outcome.** If feedback is generally positive, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT report isolated complaints as widespread issues
- ❌ Do NOT extrapolate from small sample sizes
- ❌ Do NOT ignore the context of feedback (timing, user segment)
- ❌ Do NOT report user misunderstanding as product bugs
- ✅ DO distinguish between bugs, feature requests, and user error
- ✅ DO consider sentiment distribution, not just negative feedback
- ✅ DO correlate feedback with app versions and changes
- ✅ DO identify actionable vs. subjective feedback

---

### Phase 1: Feedback Ingestion & Categorization

Systematically categorize all feedback items.

#### 1.1 Primary Categorization

**Categorize each feedback item:**

| Category | Description | Examples |
|----------|-------------|----------|
| Bug Report | App malfunction or error | Crashes, freezes, data loss |
| Performance | Speed or resource issues | Slow loading, battery drain, lag |
| UX/Usability | Interaction difficulties | Confusing navigation, hard to find features |
| Feature Request | New functionality wanted | "I wish the app could..." |
| Positive Feedback | Praise or satisfaction | "Love this app!", "Works great" |
| Content Issue | Problems with app content | Wrong info, missing content |
| Account/Auth | Login or account problems | Can't sign in, password issues |
| Payment/Billing | Purchase-related issues | Subscription problems, refunds |

#### 1.2 Severity Assessment

**Rate each issue by severity:**

| Severity | Criteria | Response Priority |
|----------|----------|-------------------|
| Critical | Data loss, security, complete failure | Immediate |
| High | Major feature broken, significant UX issue | This sprint |
| Medium | Minor bug, inconvenience | Next sprint |
| Low | Polish, nice-to-have | Backlog |

#### 1.3 Frequency Analysis

**Count issue occurrences:**

```markdown
## Issue Frequency Report

| Issue | Count | % of Total | Trend |
|-------|-------|------------|-------|
| App crashes on startup | 45 | 15% | Increasing |
| Slow photo loading | 32 | 11% | Stable |
| Can't find settings | 28 | 9% | New |
| Login fails | 22 | 7% | Decreasing |
```

---

### Phase 2: Pattern Recognition

Identify themes and root causes.

#### 2.1 Theme Clustering

**Group related feedback:**

```markdown
## Theme: Onboarding Confusion
Related feedback items: 12
Common phrases: "confusing", "don't know where", "first time"
Potential root cause: Missing tutorial or unclear UI

## Theme: Performance on Older Devices
Related feedback items: 18
Common phrases: "slow", "freezes", "old phone", "low memory"
Potential root cause: Memory optimization needed
Device correlation: Devices with < 4GB RAM
```

#### 2.2 Correlation Analysis

**Identify correlations:**

- Version correlation: Issues appearing after specific version
- Device correlation: Issues on specific devices/OS versions
- User journey correlation: Issues at specific app stages
- Time correlation: Issues at specific times/events

---

### Phase 3: Findings Presentation

**CHECKPOINT:** Present analysis summary for review.

```markdown
## User Feedback Analysis Report

### Overview
| Metric | Value |
|--------|-------|
| Total Feedback Analyzed | 300 |
| Time Period | Last 30 days |
| Average Rating | 3.8 stars |
| Rating Trend | Down 0.3 from previous period |

### Category Breakdown
| Category | Count | % | Avg Severity |
|----------|-------|---|--------------|
| Bug Reports | 85 | 28% | High |
| Performance | 62 | 21% | Medium |
| Feature Requests | 58 | 19% | Low |
| UX Issues | 45 | 15% | Medium |
| Positive | 35 | 12% | N/A |
| Other | 15 | 5% | Low |

### Top Issues by Impact
| Rank | Issue | Frequency | Severity | Impact Score |
|------|-------|-----------|----------|--------------|
| 1 | Crash on photo upload | 45 | Critical | 450 |
| 2 | Slow startup time | 38 | High | 285 |
| 3 | Settings hard to find | 28 | Medium | 140 |
| 4 | Missing dark mode | 25 | Low | 75 |

### Recommended Actions
1. **P0 - Immediate:** Investigate photo upload crashes
2. **P1 - This Sprint:** Optimize startup performance
3. **P2 - Next Sprint:** Redesign settings access
4. **P3 - Backlog:** Consider dark mode implementation
```

---

### Phase 4: Actionable Output

Translate findings into development tasks.

#### 4.1 Bug Tickets

**Generate bug ticket format:**

```markdown
### Bug: App Crashes During Photo Upload

**Source:** Play Store reviews (45 mentions)
**Severity:** Critical
**Affected Users:** ~15% of reviewers

**User Reports:**
> "Every time I try to upload a photo the app crashes"
> "Can't upload photos anymore, instant crash"
> "Photo upload worked before the update, now crashes"

**Observed Pattern:**
- Started after v2.3.0 release
- More common on Android 13+
- Likely related to storage permission changes

**Suggested Investigation:**
1. Check photo picker implementation
2. Review storage permission handling for SDK 33+
3. Add crash logging to upload flow

**Acceptance Criteria:**
- Photo upload completes without crash
- Works on Android 10-14
- Proper error handling if permission denied
```

#### 4.2 UX Improvement Tickets

**Generate improvement ticket format:**

```markdown
### UX: Improve Settings Discoverability

**Source:** Play Store reviews, support tickets (28 mentions)
**Priority:** Medium
**User Frustration Level:** Moderate

**User Reports:**
> "Where are the settings? Looked everywhere"
> "Took me 10 minutes to find how to change notifications"

**Current State:**
- Settings accessible via profile → menu → settings
- 3 taps minimum to reach

**Suggested Improvements:**
1. Add settings icon to main toolbar
2. Add settings shortcut to bottom navigation (if applicable)
3. Include settings in search/spotlight

**Acceptance Criteria:**
- Settings reachable in 1-2 taps from main screen
- Settings discoverable by new users within first session
```

---

## Expected Output

### Feedback Analysis Summary

```markdown
# User Feedback Analysis - [App Name]

## Executive Summary
- Analyzed 300 feedback items from Play Store (30-day period)
- Overall sentiment: Mixed (58% negative, 30% positive, 12% neutral)
- Primary concern: Stability issues post v2.3.0 update
- Positive mentions: Core functionality, design

## Action Items

### Immediate (P0)
| Issue | Type | Est. Effort | Owner |
|-------|------|-------------|-------|
| Photo upload crash | Bug | Medium | [TBD] |

### This Sprint (P1)
| Issue | Type | Est. Effort | Owner |
|-------|------|-------------|-------|
| Startup performance | Performance | High | [TBD] |
| Login reliability | Bug | Medium | [TBD] |

### Next Sprint (P2)
| Issue | Type | Est. Effort | Owner |
|-------|------|-------------|-------|
| Settings discoverability | UX | Low | [TBD] |
| Onboarding clarity | UX | Medium | [TBD] |

### Backlog (P3)
| Issue | Type | Est. Effort | Owner |
|-------|------|-------------|-------|
| Dark mode | Feature | High | [TBD] |
| Widget support | Feature | High | [TBD] |

## Metrics to Track
- Crash-free rate (target: 99.5%+)
- Startup time p50 (target: < 2s)
- Average rating (target: 4.0+)
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused analysis objective
- **RT-02** (Multi-Dimensional Analysis): Category, severity, frequency dimensions
- **RT-05** (Evidence-Based Reasoning): Direct user quotes as evidence
- **ST-03** (Output Format Templates): Structured reports and tickets
- **OC-05** (Severity Classification): Priority-based categorization
- **AG-12** (Quantitative Metrics): Frequency counts, impact scores
- **NE-02** (Phased Workflow): Categorize → Analyze → Report → Action
- **NE-07** (Discussion Before Action): Checkpoint before task generation

---

## Related Prompts

- [android_crash_analysis.md](android_crash_analysis.md) - Deep dive on crash reports
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Performance investigation
- [android_accessibility_improvement.md](../improvement/android_accessibility_improvement.md) - UX improvements
- [android_user_experience_enhancement.md](../improvement/android_user_experience_enhancement.md) - UX refinements
- [android_play_store_optimization.md](../publishing/android_play_store_optimization.md) - Improve ratings

---

## Customization Guide

### By Feedback Volume

**Low Volume (< 50 items):**
- Manual review each item
- Detailed individual analysis
- Direct user response consideration

**High Volume (100+ items):**
- Theme-based clustering
- Statistical significance focus
- Trend analysis priority

### By Feedback Source

**Play Store Reviews:**
- Focus on rating correlation
- Version-specific filtering
- Device/OS analysis

**Support Tickets:**
- Deeper technical detail expected
- Response commitment needed
- Escalation path consideration

**In-App Feedback:**
- Context-rich (screen, user state)
- Feature-specific targeting
- A/B test correlation

### By Analysis Goal

**Bug Triage:**
- Severity-first sorting
- Reproduction steps extraction
- Technical pattern matching

**Product Planning:**
- Feature request clustering
- Competitive mentions
- User journey mapping

**Release Monitoring:**
- Version-filtered analysis
- Regression detection
- Rapid response focus

---
title: "Android Staged Rollout Strategy"
category: mobile-development
description: "Android Staged Rollout Strategy"
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Staged Rollout Strategy

> Part of the end-to-end flow: see [`android_release_governance_runbook.md`](android_release_governance_runbook.md).

**Objective:** Design and execute a staged rollout strategy for Android app releases, including beta testing programs, percentage-based rollouts, monitoring criteria, and rollback procedures to minimize risk and maximize release quality.

**When to Use:** Use this prompt when releasing significant updates, launching new apps, releasing after major refactoring, or when previous releases had issues. Essential for apps with large user bases where a bad release could have significant impact. Helps establish systematic release processes.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before designing the rollout strategy:

1. **Release Context:**
   - "What type of release is this (new app, major update, minor fix, hotfix)?"
   - "What are the key changes in this release?"

2. **User Base:**
   - "Approximately how many active users do you have?"
   - "Do you have existing beta testers or an internal testing group?"

3. **Risk Assessment:**
   - "Are there any high-risk changes (database migrations, auth changes, core feature rewrites)?"
   - "Have there been issues with recent releases?"

4. **Monitoring Capability:**
   - "Do you have crash reporting set up (Crashlytics, Sentry)?"
   - "Do you have analytics to monitor key user flows?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY rollout strategy, you MUST:**

1. **Trace actual release risk** - Don't recommend conservative rollouts for low-risk changes.
2. **Check for existing processes** - Search for existing release procedures, beta programs, or rollout practices.
3. **Understand the context** - Consider the change type, user base size, and available monitoring.
4. **Confirm monitoring capability** - Is there sufficient crash/analytics monitoring to support staged rollout?
5. **Provide specific recommendations** - Every suggestion must include exact percentages and timelines.

**Recommending IMMEDIATE FULL ROLLOUT is sometimes appropriate.** For low-risk changes or small apps, staged rollout may be unnecessary overhead.

### False-Positive Prevention

- ❌ Do NOT recommend complex staging for simple bug fixes
- ❌ Do NOT assume all apps need beta programs
- ❌ Do NOT ignore existing team release processes
- ❌ Do NOT recommend monitoring that doesn't exist
- ✅ DO match rollout strategy to actual release risk
- ✅ DO consider team capacity for monitoring staged releases
- ✅ DO understand Play Console release track capabilities
- ✅ DO provide clear success/rollback criteria

---

### Phase 1: Release Track Strategy

Design the appropriate release track progression.

#### 1.1 Play Console Release Tracks

**Available tracks:**

```
Track Progression:
1. Internal Testing (up to 100 testers)
   - Immediate availability
   - No review required
   - Best for quick team testing

2. Closed Testing (unlimited invited testers)
   - Requires email list or Google Group
   - Can create multiple tracks (Alpha, Beta, etc.)
   - Review may be required

3. Open Testing (anyone can join)
   - Public opt-in
   - Listed in store as "Early Access"
   - Review required

4. Production (all users)
   - Staged rollout available (1-100%)
   - Full review required
   - Can halt and resume
```

#### 1.2 Recommended Track Flow

**For major releases:**

```
Week 1: Internal Testing
├── Team members test
├── Smoke test critical paths
└── Fix blocking issues

Week 2: Closed Beta
├── Trusted beta users (100-1000)
├── Collect feedback
├── Monitor crash-free rate
└── Fix reported issues

Week 3: Production Staged Rollout
├── Day 1: 5% rollout
├── Day 2: 10% (if stable)
├── Day 4: 25%
├── Day 7: 50%
├── Day 10: 100%
```

**For minor releases/hotfixes:**

```
Day 1: Internal Testing (2-4 hours)
Day 1: Production 10% rollout
Day 2: Production 50% (if stable)
Day 3: Production 100%
```

---

### Phase 2: Beta Testing Setup

Configure effective beta testing.

#### 2.1 Internal Testing Track

**Setup in Play Console:**

```
1. Navigate to Release → Testing → Internal testing
2. Create release and upload AAB
3. Add testers (email list)
4. Share opt-in link with testers

Tester Requirements:
- Google account with listed email
- Opted into testing via link
- App installed from Play Store (not sideloaded)
```

#### 2.2 Closed Beta Setup

**Best practices:**

```
Beta Tester Recruitment:
- Power users from existing user base
- Users who reported bugs (engaged users)
- Diverse device portfolio
- Mix of technical and non-technical

Communication Template:
"We're looking for beta testers for [App Name].
As a beta tester, you'll get early access to new
features and help us improve the app. Join here: [link]"

Feedback Collection:
- In-app feedback mechanism
- Beta-specific email address
- Discord/Slack community (optional)
- Structured feedback forms
```

#### 2.3 Firebase App Distribution (Alternative)

**For faster iteration:**

```kotlin
// Useful for pre-Play Store testing
// Doesn't require Play Store account

Benefits:
- Instant distribution (no review)
- Supports APK and AAB
- Tester management
- Release notes
- Integrates with CI/CD
```

---

### Phase 3: Staged Rollout Execution

Implement production staged rollout.

#### 3.1 Rollout Percentage Strategy

**Conservative approach (recommended):**

| Day | Percentage | User Exposure | Decision Point |
|-----|-----------|---------------|----------------|
| 1 | 5% | ~5K users | Validate basic stability |
| 2 | 10% | ~10K users | Monitor crash rate |
| 4 | 25% | ~25K users | Check user feedback |
| 7 | 50% | ~50K users | Verify at scale |
| 10 | 100% | All users | Full release |

**Aggressive approach (hotfixes):**

| Day | Percentage | Criteria to Proceed |
|-----|-----------|---------------------|
| 1 | 25% | No new crashes |
| 2 | 50% | Crash-free rate stable |
| 3 | 100% | All clear |

#### 3.2 Monitoring Criteria

**Go/No-Go metrics:**

```
Green (Proceed to next stage):
- Crash-free rate ≥ 99.5%
- No increase in ANRs
- No critical bug reports
- Key flows conversion stable

Yellow (Pause and investigate):
- Crash-free rate 98-99.5%
- New crash clusters appearing
- Negative reviews mentioning issues
- Slight metric degradation

Red (Halt rollout):
- Crash-free rate < 98%
- Critical functionality broken
- Data loss or corruption reports
- Security issue discovered
```

#### 3.3 Rollout Commands

**Play Console actions:**

```
Increase Rollout:
Release → Production → Manage release →
Update rollout percentage → Save

Halt Rollout:
Release → Production → Manage release →
Halt rollout → Confirm

Resume Rollout:
Release → Production → Manage release →
Resume rollout → Set percentage → Save

Full Rollout (after staged):
Release → Production → Manage release →
Roll out to 100%
```

---

### Phase 4: Monitoring & Response

Set up monitoring and response procedures.

#### 4.1 Monitoring Dashboard

**Key metrics to track:**

```
Real-time (check multiple times daily):
- Crash-free users %
- ANR rate
- New crash clusters

Daily:
- User ratings and reviews
- Uninstall rate
- Key event completion rates

Comparison:
- This version vs previous version
- Same day in rollout vs previous release
```

#### 4.2 Alert Configuration

**Set up alerts for:**

```kotlin
// Firebase Crashlytics alerts
- Velocity alerts (sudden spike in crashes)
- New crash issue alerts
- Regression alerts (previously fixed issues)

// Custom alerts
- Error rate thresholds
- API failure spikes
- User-reported issues spike
```

#### 4.3 Rollback Procedure

**If issues discovered:**

```
Immediate Actions:
1. Halt rollout (prevents new installs)
2. Assess severity
3. Document the issue

If Critical:
1. Prepare hotfix release
2. Fast-track through internal testing
3. Release as staged rollout to affected users

If Non-Critical:
1. Fix in next regular release
2. Resume rollout if safe
3. Or abandon and prepare new version

Note: Cannot "rollback" installed apps.
Users keep current version until they update.
```

---

## Expected Output

### Staged Rollout Plan

```markdown
# Staged Rollout Plan: [App Name] v[X.Y.Z]

## Release Summary
- **Version:** X.Y.Z (build XXX)
- **Key Changes:** [Summary]
- **Risk Level:** [Low/Medium/High]

## Timeline

| Phase | Duration | Audience | Success Criteria |
|-------|----------|----------|------------------|
| Internal | 2 days | Team (10) | No blockers |
| Beta | 5 days | Beta (500) | 99%+ crash-free |
| Prod 5% | 2 days | 5K users | 99.5%+ crash-free |
| Prod 25% | 3 days | 25K users | Stable metrics |
| Prod 100% | - | All users | - |

## Monitoring Checklist
- [ ] Crashlytics alerts configured
- [ ] Analytics events verified
- [ ] Key flows baseline documented
- [ ] On-call rotation set

## Go/No-Go Criteria
- **Proceed if:** Crash-free ≥ 99.5%, no critical bugs
- **Pause if:** Crash-free 98-99.5%, new issues
- **Halt if:** Crash-free < 98%, critical bugs

## Rollback Plan
1. Halt rollout immediately
2. Notify team in [channel]
3. Assess severity (15 min SLA)
4. If critical: Begin hotfix process
```

---

## Example Interaction

**User:** We're releasing a major update with a new payment system. Our app has 500K users. How should we roll this out?

**Agent:** Given the high-risk nature (payment system) and large user base, I recommend a conservative staged rollout.

## Recommended Rollout Strategy

**Risk Level:** High (payment changes, large user base)

**Phase 1: Extended Testing (1 week)**
- Internal: 2 days with team testing payment flows
- Closed Beta: 5 days with 200 trusted testers
- Success criteria: Zero payment failures, 99.9% crash-free

**Phase 2: Conservative Production Rollout (2 weeks)**
| Day | % | Users | Focus Area |
|-----|---|-------|------------|
| 1 | 1% | 5K | Basic stability |
| 3 | 5% | 25K | Payment completion rate |
| 5 | 10% | 50K | Refund/dispute rate |
| 8 | 25% | 125K | Scale validation |
| 11 | 50% | 250K | Edge cases |
| 14 | 100% | 500K | Full release |

**Monitoring Focus:**
- Payment success rate vs baseline
- Cart abandonment at payment step
- Payment provider errors
- User support tickets about payments

**Halt Criteria:**
- Payment success rate drops >2%
- Any data inconsistency (payment recorded, order not)
- Payment provider flagging issues

Would you like me to detail the monitoring setup?

---

## Techniques Used

- **ST-01** (Clear Objective): Staged rollout planning objective
- **ST-02** (Sequential Instructions): Track → Testing → Rollout → Monitor
- **ST-03** (Output Format Templates): Rollout plan structure
- **OC-05** (Severity Classification): Risk level categorization
- **AG-12** (Quantitative Metrics): Percentage and threshold criteria
- **NE-07** (Discussion Before Action): Phase-based checkpoints

---

## Related Prompts

- [android_release_preparation.md](android_release_preparation.md) - Pre-release checklist
- [android_crash_analysis.md](../maintenance/android_crash_analysis.md) - Analyze issues during rollout
- [android_user_feedback_analysis.md](../maintenance/android_user_feedback_analysis.md) - Process user feedback during beta

---

## Customization Guide

### For Different Release Types

**Hotfix:**
- Skip beta, minimal internal testing
- Aggressive rollout (25% → 50% → 100%)
- Focus on the specific fix

**New App Launch:**
- Extended beta period
- Slower initial rollout to gather baseline metrics
- Focus on app store reviews

**Major Version:**
- Full track progression
- Extended monitoring at each stage
- Communication plan for users

### For Different User Bases

**Small (<10K users):**
- Shorter testing phases
- Wider percentage jumps
- Direct user feedback valuable

**Large (>1M users):**
- Longer hold at each percentage
- 1% start may still be 10K+ users
- Automated monitoring essential

### For Different Risk Levels

**Low Risk (UI tweaks):**
- 5% → 25% → 100% over 3-5 days
- Standard monitoring

**High Risk (data migration):**
- 1% → 5% → 10% → 25% → 50% → 100%
- Extended holds at each stage
- Rollback plan essential

# Engagement Pattern Library

Ready-to-implement engagement patterns with behavioral psychology foundations and real-app examples.

## Pattern Catalog

### 1. Streak System

**Psychology:** Loss aversion (Kahneman/Tversky) + identity formation + sunk cost

**Reference apps:** Duolingo (gold standard), Snapchat, GitHub, Headspace

**Components:**
```
┌─────────────────────────────────────────┐
│  🔥 23-Day Streak                       │
│  ████████████████████░░░░  23/30        │
│  Complete today's [action] to continue   │
│                                          │
│  [Mon][Tue][Wed][Thu][Fri][Sat][Sun]     │
│   ✓    ✓    ✓    ✓    ✓    ✓    •       │
└─────────────────────────────────────────┘
```

**Design specifications:**
- Counter: Prominent display on home screen, 24pt+ font, warm color (orange/amber)
- Calendar row: 7-day view showing completed/pending days
- Progress to milestone: Bar showing progress to next milestone (7, 30, 100, 365)
- Milestone rewards: Escalating — badge at 7, special animation at 30, permanent trophy at 100
- Streak freeze: 1 free per week, additional purchasable with in-app currency
- Recovery: 24-hour grace period after miss, "streak repair" option within 48h
- Notification: Send reminder 2-3 hours before daily reset if action not completed
- Celebration: Increment counter animation + haptic (success) at completion, confetti at milestones

**Anti-patterns to avoid:**
- Punitive messaging on streak loss ("You failed!" → "Day 1 of your next great streak!")
- Impossible daily minimums (must be completable in < 2 minutes)
- No recovery option (causes permanent churn after any miss)

---

### 2. XP & Level System

**Psychology:** Progress principle (Amabile) + mastery motivation + self-determination theory

**Reference apps:** Duolingo, Chess.com, Fitbit, Khan Academy

**Level Structure Template:**
| Level | XP Required | Name | Unlock |
|-------|------------|------|--------|
| 1 | 0 | Beginner | Basic features |
| 2 | 100 | Novice | Profile customization |
| 3 | 300 | Apprentice | Advanced feature 1 |
| 4 | 600 | Practitioner | Leaderboard access |
| 5 | 1000 | Expert | Advanced feature 2 |
| 6 | 1500 | Master | Community features |
| 7 | 2500 | Grandmaster | All features + special badge |

**XP Award Schedule:**
| Action | XP | Bonus |
|--------|-----|-------|
| Core action completed | 10 | — |
| Perfect score/quality | 15 | +50% quality bonus |
| Daily challenge completed | 25 | — |
| All daily challenges completed | 50 | Completion bonus |
| Streak milestone (7 days) | 100 | One-time |
| Streak milestone (30 days) | 500 | One-time |
| First action of the day | 5 | Early bird bonus |

**UI specifications:**
- XP bar: Segmented progress bar in header/profile, shows current level + XP to next
- "+XP" indicator: Floating text that animates up and fades (800ms, ease-out)
- Level-up: Full-width banner animation (600ms), scale bounce, haptic (heavy impact)
- XP multiplier events: 2x weekends, special events — creates urgency and increased engagement

---

### 3. Achievement/Badge System

**Psychology:** Collection drive + self-determination (competence) + social display

**Reference apps:** Apple Watch Fitness, Duolingo, Foursquare, Steam

**Achievement Categories:**
```
GETTING STARTED (easily achievable, first session)
  ☐ First Steps — Complete your first [action]
  ☐ Profile Builder — Complete your profile
  ☐ Explorer — Visit 3 different features

CONSISTENCY (daily/weekly engagement)
  ☐ Weekly Warrior — Use the app 7 days in a row
  ☐ Month Master — 30-day streak
  ☐ Centurion — 100-day streak

MASTERY (skill/quality milestones)
  ☐ Perfect Score — Complete [action] with 100% accuracy
  ☐ Speed Demon — Complete [action] in under [time]
  ☐ Knowledge Seeker — Complete all [category] content

SOCIAL (community engagement)
  ☐ Connector — Follow 10 users
  ☐ Supporter — Like/react 50 times
  ☐ Influencer — Receive 100 likes on your content

SECRET (surprise achievements)
  ☐ Night Owl — Use the app at 3am
  ☐ Easter Egg — Find the hidden feature
  ☐ [App-specific surprise]
```

**Display:** Trophy case on profile, recently earned badge highlighted, progress toward next badge visible, share button for social platforms

---

### 4. Daily Challenge System

**Psychology:** Goal-setting theory (Locke) + variable reward + completion drive

**Reference apps:** Duolingo, Fitbit, Apple Fitness+, Headspace

**Structure:**
```
┌─────────────────────────────────────────┐
│  Today's Challenges           ⟳ Refresh │
│                                          │
│  ✓  Complete 1 [core action]    +10 XP  │
│  ○  [Specific challenge]        +25 XP  │
│  ○  [Stretch challenge]         +25 XP  │
│                                          │
│  ███████░░░░  1/3 Complete              │
│  Complete all 3 for +50 XP bonus!       │
│                                          │
│  Refreshes in 14h 23m                   │
└─────────────────────────────────────────┘
```

**Design rules:**
- 3 challenges per day (achievable but not trivial)
- First challenge = core action (always achievable)
- Second challenge = specific variation (moderate effort)
- Third challenge = stretch goal (requires extra engagement)
- All-complete bonus = 50% extra XP (incentivizes completing all 3)
- 1 free reroll per day (if a challenge is impossible given context)
- Countdown to refresh creates urgency without anxiety
- Challenges personalized based on user level and behavior history

---

### 5. Notification Trigger Templates

**Psychology:** Classical conditioning (Pavlov) + prompt timing (Fogg)

**Template library:**

```
STREAK PROTECTION (send 2-3h before daily reset)
"[Name], your [N]-day streak ends at midnight! Quick [action] to keep it going 🔥"

SOCIAL ACTIVITY (send real-time for engaged users, batched for others)
"[Friend] just [action]. [Contextual CTA]"

MILESTONE APPROACHING (send when 90%+ complete)
"One more [action] and you'll hit [milestone]! 🎯"

CONTENT READY (send at user's peak engagement time)
"Your daily [content type] is ready. [Preview/teaser]"

WIN-BACK DAY 3 (send afternoon of 3rd absent day)
"It's been a few days! [Personalized reason to return based on last activity]"

WIN-BACK DAY 7 (send with value proposition)
"Here's what's new since you were last here: [specific new content/feature]"

ACHIEVEMENT EARNED (send immediately)
"🏆 You just earned [Achievement Name]! [Share CTA]"

FRIEND ACTIVITY (send when relevant)
"[Friend] just passed your [metric]. Reclaim the lead?"
```

**Frequency rules:**
- Maximum 3-5 notifications per day across all categories
- Never send notifications between 10pm and 8am (respect sleep)
- After 3 consecutive dismissed notifications, reduce frequency by 50%
- After 5 consecutive dismissed, switch to weekly digest only
- Always allow granular notification category control in settings

---

### 6. Onboarding Hook Sequence

**Psychology:** Commitment/consistency (Cialdini) + endowed progress + time-to-value

**Reference apps:** Duolingo, Spotify, TikTok, Headspace

**Optimal sequence:**
```
Step 1: VALUE FIRST (0-30 seconds)
  Show core value immediately, no sign-up required
  Example: TikTok shows first video instantly

Step 2: QUICK WIN (30-120 seconds)
  User completes first meaningful action
  Example: Duolingo first lesson question answered correctly

Step 3: PERSONALIZE (120-180 seconds)
  2-3 preference questions that improve the experience
  Example: Spotify "pick 3 artists you like"

Step 4: COMMITMENT DEVICE (180-240 seconds)
  User sets a personal goal or preference
  Example: Duolingo "how much time per day?" → creates streak basis

Step 5: IDENTITY CREATION (240-300 seconds)
  Account creation + profile (now motivated to preserve progress)
  Example: Create account to save progress from Step 2

Step 6: TRIGGER SETUP (300-360 seconds)
  Permission requests (notifications, now justified by commitment)
  "Get a reminder to hit your daily goal?"

Step 7: FIRST REWARD (immediately after setup)
  Grant first achievement, set streak day 1, show progress
  "Welcome! You're already Level 1 with 10 XP!"
```

**Key principle:** Every step must provide immediate value or create investment. Never front-load friction.

---

### 7. Social Proof Patterns

**Psychology:** Social proof (Cialdini) + uncertainty reduction + conformity

**Pattern library:**

```
ACTIVITY COUNT
"1,247 people are [action] right now"
Implementation: Real-time counter, updated every 30s, animate count changes

FRIEND ACTIVITY
"Sarah and 3 friends also use this"
Implementation: Avatar stack (max 3 + count), mutual connection highlighting

PEER COMPARISON
"You're in the top 15% this week"
Implementation: Percentile indicator, update weekly, celebrate improvements

TRENDING INDICATOR
"🔥 Trending — 2.3k people tried this today"
Implementation: Flame icon + count, threshold-based activation

SOCIAL ENDORSEMENT
"Recommended by 3 people you follow"
Implementation: Avatar thumbnails of endorsers, tap to see full list

LIVE INDICATOR
"● Live — 47 users online"
Implementation: Pulsing green dot, real-time count, fade when < 5 users
```

---

### 8. Progress Visualization Patterns

**Psychology:** Goal gradient effect (closer to goal = more motivated) + endowed progress

**Pattern types:**

```
LINEAR PROGRESS BAR
████████████░░░░░░  67%
Best for: Single-dimension progress, course completion

CIRCULAR/RING PROGRESS
Best for: Daily goals (Apple Watch rings), compact spaces

CALENDAR HEATMAP
Best for: Long-term consistency, contribution tracking (GitHub-style)

MILESTONE PATH
○───●───●───●───○───○───○
         ↑ You are here
Best for: Multi-stage journeys, course progression

LEVEL-UP METER
Level 4 ████████░░ Level 5
        847 / 1000 XP
Best for: Gamified progression systems

SKILL RADAR/SPIDER
Best for: Multi-skill assessment, portfolio view
```

---

### 9. Loss Aversion Mechanics (Ethical)

**Psychology:** Prospect theory (Kahneman/Tversky) — losses weigh ~2x gains

**Ethical implementations:**
```
STREAK PROTECTION (not punishment)
"Your streak is safe today ✓" (positive framing)
"Streak freeze used — resume tomorrow" (graceful handling)
NOT: "You LOST your streak! Start over!" (punitive)

PROGRESS PRESERVATION
"You've completed 67% — pick up where you left off"
NOT: "You haven't logged in for 3 days. Your progress is at risk!"

EXPIRING OPPORTUNITY (genuine scarcity)
"This week's challenge ends in 2 days"
NOT: Fake countdown timers that reset

STATUS MAINTENANCE
"Complete 2 more this week to maintain Gold status"
NOT: "You'll be DEMOTED if you don't act now!"

GENTLE NUDGE
"Your daily [content] is ready when you are"
NOT: "You're MISSING OUT on today's [content]!"
```

**The ethical test:** Would the user thank you for this nudge, or resent it?

---

## Pattern Combination Guide

### For Social Apps
Combine: Social proof + activity feed + streak + notification triggers
Core loop: Create content → receive social validation → create more

### For Fitness/Health Apps
Combine: Streak + daily challenge + progress rings + achievement badges
Core loop: Complete workout → see progress → maintain streak → level up

### For Education Apps
Combine: XP/levels + streak + daily challenge + leaderboard
Core loop: Complete lesson → earn XP → advance streak → compete in league

### For Productivity Apps
Combine: Daily challenge + progress bar + achievement + weekly review
Core loop: Complete tasks → see progress → earn achievements → review week

### For E-Commerce Apps
Combine: Social proof + personalization + trending indicators + loyalty points
Core loop: Browse → discover (variable reward) → purchase → earn points → browse more

### For Content/News Apps
Combine: Personalized feed + daily digest + reading streaks + bookmark collection
Core loop: Open → discover content → save/share → feed improves → return for more

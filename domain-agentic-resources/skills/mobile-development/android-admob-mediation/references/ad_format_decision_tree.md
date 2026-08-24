# Ad Format Decision Tree

## Choosing the Right Ad Format

```
What type of screen/content?
│
├── Scrollable list or feed?
│   └── Banner (anchored at bottom) or Native (in-feed)
│       - Banner: simpler, consistent revenue, 50dp height
│       - Native: higher engagement, matches content, more dev work
│
├── Natural transition between screens?
│   └── Interstitial (full-screen)
│       - After completing a task
│       - Between levels in gamification
│       - After saving an item
│       - NEVER during active navigation
│
├── User wants optional bonus content/feature?
│   └── Rewarded (user opts in to watch)
│       - Extra gamification points
│       - Skip a cooldown timer
│       - Unlock a premium feature temporarily
│       - User must explicitly choose to watch
│
├── App launch/resume from background?
│   └── App Open ad
│       - Shows during loading screen
│       - Only if app was backgrounded 3+ hours
│       - Do NOT show on every resume
│
└── Content detail page?
    └── Banner at bottom or between content sections
        - Below main content
        - Between comments/reviews
        - Never overlapping actionable UI
```

## Format Comparison

| Format | Revenue/Impression | UX Impact | Best For | CPM Range |
|--------|-------------------|-----------|----------|-----------|
| Banner | Low | Minimal | Always-on passive revenue | $0.10-$2 |
| Interstitial | High | Moderate (disruptive) | Transition points | $2-$15 |
| Rewarded | Highest | Positive (user choice) | Opt-in bonus features | $5-$30 |
| Native | Medium-High | Minimal (blends in) | Content feeds | $1-$10 |
| App Open | Medium | Low (loading screen) | App cold start | $1-$8 |

## Placement Rules Per Screen

### Home/Dashboard
- Banner at bottom (persistent)
- No interstitials on home screen

### Messaging
- NO ADS — disrupts communication flow
- Exception: small banner only if not in active conversation

### Calendar
- Banner at bottom of month view
- No interstitials when creating/viewing events

### Task Lists
- Banner at bottom of list
- Interstitial AFTER marking a task complete (natural pause)
- Rewarded to unlock premium task features

### Shopping Lists
- Banner at bottom of list
- No interstitials during active shopping (user is in a store)

### Weather
- Banner below forecast
- Native ad between forecast sections

### Gamification
- Rewarded ads for bonus points/lives/features
- Interstitial between completed challenges
- Banner on leaderboard screen

### Settings
- NO ADS — settings is a utility screen

## Revenue Optimization Tips

1. **Preload interstitials and rewarded ads** — Load the next ad immediately after showing one
2. **Use mediation** — Multiple ad networks compete for inventory, increasing CPM
3. **A/B test placements** — Use Firebase Remote Config to test ad positions
4. **Monitor eCPM by format** — Shift toward higher-performing formats
5. **Respect user time** — Aggressive ads increase uninstalls, decreasing long-term revenue

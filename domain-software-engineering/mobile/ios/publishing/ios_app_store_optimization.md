---
title: "iOS App Store Optimization (ASO)"
category: mobile-development
description: "Comprehensive ASO guide covering keyword research, title and subtitle optimization, screenshot strategy, app preview videos, product page optimization, and A/B testing for App Store Connect."
techniques:
  - ST-01 (Structured Task Decomposition)
  - RT-02 (Checklist Verification)
  - DS-02 (Domain-Specific Terminology)
  - CR-01 (Creative Strategy)
  - AN-01 (Analysis Framework)
difficulty: intermediate
tags:
  - ios
  - swift
  - app-store
  - aso
  - keywords
  - screenshots
  - app-preview
  - product-page-optimization
  - a-b-testing
updated: "2026-03-19"
---

# iOS App Store Optimization (ASO)

**Objective:** Maximize an iOS app's visibility and conversion rate in the App Store through systematic keyword research, metadata optimization (title, subtitle, keyword field), compelling screenshot design, app preview video strategy, and product page optimization with A/B testing. This prompt covers the full ASO lifecycle from keyword discovery to conversion optimization.

**When to Use:** Before initial app launch, during seasonal keyword updates (quarterly recommended), when conversion rates drop, when entering new markets or localizations, or when Apple introduces new App Store features. ASO is an ongoing practice, not a one-time task.

**Prompt Type:** Comprehensive (approximately 380 lines)

## Context Gathering

1. What is the app's primary function and category in the App Store?
2. Who is the target audience (demographics, use cases, pain points)?
3. What are the top 5 competitor apps in your category?
4. What localizations does the app support?
5. What is the current title, subtitle, and keyword field content?
6. How many screenshots and app previews are currently configured?
7. What is the current conversion rate (impressions to installs) if known?
8. Does the app have in-app events or custom product pages configured?

## Instructions

### CRITICAL: Verification Requirements

- [ ] Title is 30 characters or fewer and includes the primary keyword
- [ ] Subtitle is 30 characters or fewer and includes a secondary keyword
- [ ] Keyword field is exactly 100 characters, comma-separated, no spaces after commas
- [ ] No keywords are duplicated between title, subtitle, and keyword field
- [ ] Screenshots are provided for all required device sizes
- [ ] App preview videos are under 30 seconds and show actual app footage
- [ ] Product page metadata passes App Store Connect validation
- [ ] Custom product pages are configured for paid acquisition campaigns

### False-Positive Prevention

- ❌ DO NOT stuff the title with keywords at the expense of brand recognition
- ❌ DO NOT use competitor brand names in your keyword field (Apple rejects this)
- ❌ DO NOT use generic terms like "best" or "free" that Apple may reject
- ❌ DO NOT duplicate keywords already in the title or subtitle in the keyword field
- ❌ DO NOT use plurals if the singular is already included (Apple indexes both)
- ❌ DO NOT assume screenshot order does not matter; the first 3 are visible before tap
- ❌ DO NOT include prices in screenshots (they change by region)
- ✅ DO use singular forms of words (Apple's algorithm handles plurals)
- ✅ DO leverage localization keyword fields for each supported language
- ✅ DO refresh keywords quarterly based on search trend data
- ✅ DO test screenshot variants using Product Page Optimization
- ✅ DO include the app name in at least the first screenshot for brand recall

## Step 1: Keyword Research

### Keyword Discovery Framework

```
KEYWORD RESEARCH TEMPLATE:

Primary Keywords (high relevance, high volume):
┌─────────────────────┬──────────┬───────────┬──────────────┬────────────┐
│ Keyword             │ Relevance│ Est.Volume│ Difficulty   │ Current    │
│                     │ (1-10)   │ (5-100)   │ (1-10)       │ Rank       │
├─────────────────────┼──────────┼───────────┼──────────────┼────────────┤
│                     │          │           │              │            │
│                     │          │           │              │            │
│                     │          │           │              │            │
└─────────────────────┴──────────┴───────────┴──────────────┴────────────┘

Long-Tail Keywords (lower volume, higher conversion):
┌─────────────────────┬──────────┬───────────┬──────────────┬────────────┐
│ Keyword             │ Relevance│ Est.Volume│ Difficulty   │ Current    │
│                     │ (1-10)   │ (5-100)   │ (1-10)       │ Rank       │
├─────────────────────┼──────────┼───────────┼──────────────┼────────────┤
│                     │          │           │              │            │
│                     │          │           │              │            │
└─────────────────────┴──────────┴───────────┴──────────────┴────────────┘

Competitor Keyword Analysis:
┌─────────────────────┬────────────────┬──────────────────────────────────┐
│ Competitor App      │ Title Keywords │ Keywords They Rank For           │
├─────────────────────┼────────────────┼──────────────────────────────────┤
│                     │                │                                  │
│                     │                │                                  │
│                     │                │                                  │
└─────────────────────┴────────────────┴──────────────────────────────────┘
```

### Keyword Sources

1. **Apple Search Ads** - Use Search Match campaigns to discover what users actually search
2. **App Store Connect Analytics** - Check "Sources" for organic search terms
3. **Competitor analysis** - Review competitor titles, subtitles, and what they rank for
4. **Auto-complete** - Type partial keywords in App Store search to see suggestions
5. **Review mining** - Extract language your users use in reviews
6. **ASO tools** - AppTweak, Sensor Tower, App Annie/data.ai for volume estimates

## Step 2: Title and Subtitle Optimization

```
METADATA OPTIMIZATION TEMPLATE:

App Name (max 30 characters):
┌─────────────────────────────────────────────┐
│ [Brand Name] - [Primary Keyword]            │
│ Character count: ___/30                     │
│ Example: "FitTrack - Workout Planner"       │
└─────────────────────────────────────────────┘

Subtitle (max 30 characters):
┌─────────────────────────────────────────────┐
│ [Benefit Statement with Secondary Keyword]  │
│ Character count: ___/30                     │
│ Example: "Exercise & Meal Tracker"          │
└─────────────────────────────────────────────┘

Keyword Field (max 100 characters, comma-separated, NO spaces after commas):
┌───────────────────────────────────────────────────────────────────────────┐
│ keyword1,keyword2,keyword3,keyword4,...                                   │
│ Character count: ___/100                                                 │
│ Rules:                                                                   │
│ - Do NOT repeat words from title or subtitle                             │
│ - Use singular, not plural                                               │
│ - No spaces after commas                                                 │
│ - No special characters or numbers that aren't searchable                │
│ - Separate compound words to maximize combinations                       │
│ Example: "gym,routine,plan,log,weight,diet,nutrition,calorie,step,run"  │
└───────────────────────────────────────────────────────────────────────────┘
```

### Character Maximization Strategy

```
KEYWORD ALLOCATION VERIFICATION:
1. List ALL unique keywords from title:         [___, ___, ___]
2. List ALL unique keywords from subtitle:      [___, ___, ___]
3. List ALL keywords in keyword field:          [___, ___, ___, ...]
4. Verify: NO word appears in more than one location
5. Calculate total unique keywords indexed:     ___
6. Calculate unused keyword field characters:   ___/100
7. If unused > 5 characters, add more keywords
```

## Step 3: Screenshot Strategy

```
SCREENSHOT DESIGN TEMPLATE:

Required Device Sizes:
[ ] iPhone 6.9" (iPhone 16 Pro Max) - REQUIRED
[ ] iPhone 6.7" (iPhone 15 Plus/Pro Max) - Can use 6.9" as fallback
[ ] iPhone 6.5" (iPhone 11 Pro Max) - Can use 6.7" as fallback
[ ] iPhone 5.5" (iPhone 8 Plus) - Required if supporting iPhone SE
[ ] iPad Pro 13" (6th gen) - Required for universal apps
[ ] iPad Pro 12.9" (2nd gen) - Required for older iPad support

Screenshot Narrative Flow (up to 10 screenshots):
┌─────┬────────────────────────────────────────────────────────┐
│  #  │ Purpose                                                │
├─────┼────────────────────────────────────────────────────────┤
│  1  │ Hero shot: Primary value proposition + brand name      │
│  2  │ Core feature #1 with benefit-oriented caption          │
│  3  │ Core feature #2 with benefit-oriented caption          │
│  4  │ Social proof or unique differentiator                  │
│  5  │ Core feature #3 with benefit-oriented caption          │
│  6  │ Customization or personalization features              │
│  7  │ Integration or ecosystem benefits                      │
│  8  │ Widget, Apple Watch, or platform extension             │
│  9  │ Awards, ratings, or press mentions                     │
│ 10  │ Call to action or feature summary                      │
└─────┴────────────────────────────────────────────────────────┘

Caption Best Practices:
- Lead with benefit, not feature name ("Track your progress" not "Dashboard view")
- Keep text large enough to read at thumbnail size
- Use consistent typography and color scheme
- Include actual app UI, not mockups or illustrations alone
- Consider dark mode variant if your app supports it
```

## Step 4: App Preview Videos

```
APP PREVIEW GUIDELINES:
[ ] Duration: 15-30 seconds (30 seconds maximum)
[ ] Shows actual app footage captured on device
[ ] No external footage, only screen recordings with optional overlays
[ ] First frame is compelling (it serves as poster frame)
[ ] Includes captions for accessibility and sound-off viewing
[ ] Demonstrates core value proposition within first 5 seconds
[ ] Up to 3 app previews per localization
[ ] Resolution matches target device exactly

Storyboard Template:
┌─────────┬────────────────────────┬──────────────────┐
│ Time    │ Screen Content         │ Caption/Overlay   │
├─────────┼────────────────────────┼──────────────────┤
│ 0-5s    │ App launch + hero flow │ "Meet [AppName]" │
│ 5-15s   │ Core feature demo      │ Feature benefit   │
│ 15-25s  │ Secondary features     │ Feature benefit   │
│ 25-30s  │ Result/outcome shot    │ Call to action    │
└─────────┴────────────────────────┴──────────────────┘
```

## Step 5: Product Page Optimization (A/B Testing)

Configure through App Store Connect:

```
PRODUCT PAGE OPTIMIZATION SETUP:

Treatment Configuration:
┌──────────────┬──────────────────────────┬──────────────────────────┐
│ Element      │ Control (Original)       │ Treatment (Variant)      │
├──────────────┼──────────────────────────┼──────────────────────────┤
│ App Icon     │ Current icon             │ Variant icon             │
│ Screenshots  │ Current screenshot set   │ Variant screenshot set   │
│ App Preview  │ Current preview          │ Variant preview          │
└──────────────┴──────────────────────────┴──────────────────────────┘

Test Parameters:
- Traffic split: 50/50 (recommended for fastest results) or custom
- Minimum duration: 7 days (Apple recommendation)
- Minimum impressions: 2,000+ per variant for statistical significance
- Test ONE element at a time for clean results
- Run test for each key localization separately

Custom Product Pages (up to 35):
┌──────────────┬──────────────────────────┬──────────────────────────┐
│ Page Name    │ Target Audience          │ Unique Elements          │
├──────────────┼──────────────────────────┼──────────────────────────┤
│ Fitness      │ Apple Search Ads fitness │ Workout screenshots      │
│ Diet         │ Apple Search Ads diet    │ Nutrition screenshots    │
│ Social       │ Social media campaigns   │ Community features       │
└──────────────┴──────────────────────────┴──────────────────────────┘
```

## Step 6: Localization Strategy

```
LOCALIZATION ASO TEMPLATE:

Priority Markets:
┌──────────┬───────────────────┬──────────────────┬─────────────────┐
│ Locale   │ Localized Title   │ Localized Subtitle│ Keyword Field   │
├──────────┼───────────────────┼──────────────────┼─────────────────┤
│ en-US    │                   │                  │                 │
│ en-GB    │                   │                  │                 │
│ ja       │                   │                  │                 │
│ zh-Hans  │                   │                  │                 │
│ de       │                   │                  │                 │
│ fr       │                   │                  │                 │
│ es       │                   │                  │                 │
│ pt-BR    │                   │                  │                 │
│ ko       │                   │                  │                 │
└──────────┴───────────────────┴──────────────────┴─────────────────┘

Note: Each locale gets its own 100-character keyword field.
Research local search terms - direct translations often miss colloquial usage.
```

## Expected Output

After completing this prompt, you will have:

1. A researched keyword strategy with prioritized primary and long-tail keywords
2. Optimized title, subtitle, and keyword field maximizing character limits
3. A screenshot narrative with device-specific assets and benefit-driven captions
4. App preview video storyboard with timed content plan
5. Product Page Optimization test plan for A/B testing
6. Custom product pages configured for paid acquisition campaigns
7. Localization ASO strategy for priority markets

## Example Interaction

**User:** I have a meditation app called "Serenity" in the Health & Fitness category. Main competitors are Calm, Headspace, and Insight Timer. We support English, Japanese, and Spanish.

**Assistant:** Here is your ASO strategy for Serenity:

**Title (28/30 chars):** `Serenity - Daily Meditation`
**Subtitle (29/30 chars):** `Sleep Sounds & Breathing`
**Keyword Field (98/100 chars):** `mindfulness,relax,stress,anxiety,calm,sleep,breathing,focus,timer,guided,zen,wellness,mental,health`

**Keywords NOT duplicated:** "meditation" (in title), "sleep" (in subtitle), "sounds" (in subtitle), "breathing" (in subtitle), "daily" (in title) are excluded from the keyword field.

**Screenshot Strategy:**
1. Hero: Person peacefully meditating with "Find Your Calm" headline
2. Session library: "500+ Guided Sessions"
3. Sleep sounds: "Drift Off Naturally"
...

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Six-step ASO workflow from research to testing |
| RT-02 (Checklist Verification) | Screenshot requirements and metadata validation |
| DS-02 (Domain-Specific Terminology) | ASO terms: keyword density, impression-to-install, Search Match |
| CR-01 (Creative Strategy) | Screenshot narrative and app preview storyboarding |
| AN-01 (Analysis Framework) | Competitor keyword analysis and test result evaluation |

## Related Prompts

- [ios_screenshot_strategy.md](ios_screenshot_strategy.md) - Deep dive into screenshot and app preview design
- [ios_app_store_review_response.md](ios_app_store_review_response.md) - Managing reviews that impact conversion
- [ios_pre_submission_checklist.md](ios_pre_submission_checklist.md) - Metadata validation before submission
- [ios_release_management.md](ios_release_management.md) - Release notes as ASO opportunity

## Customization Guide

- **For subscription apps:** Emphasize free trial in screenshots, add promotional offer configuration in App Store Connect
- **For games:** Replace feature screenshots with gameplay footage, use landscape orientation, emphasize app previews over static screenshots
- **For enterprise/B2B apps:** Focus on integration keywords, use case-specific custom product pages for different industries
- **For regional apps:** Prioritize local language keyword research using native speakers, not translation tools
- **For seasonal apps:** Plan keyword rotations for seasonal demand (tax apps in March, fitness in January)
- **For new apps with no reviews:** Prioritize lower-difficulty keywords where you can realistically rank without rating momentum

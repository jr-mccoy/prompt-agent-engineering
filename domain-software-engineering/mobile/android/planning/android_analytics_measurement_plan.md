---
title: "Android Analytics Measurement Plan"
category: mobile-development
description: "Define what to measure — a North Star metric, AARRR funnels, and a strict event taxonomy with an instrumentation spec — before any analytics SDK is wired into the Android app."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - AG-02
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - analytics
  - ga4
  - firebase-analytics
  - event-taxonomy
  - measurement-plan
updated: "2026-06-06"
related_prompts:
  - android_mvp_scope_and_release_roadmap.md
  - ../targeted-reviews/firebase_analytics_strategy.md
  - android_privacy_by_design_and_permissions_plan.md
---

# Android Analytics Measurement Plan

**Objective:** Produce a measurement plan that decides *what* an Android app will measure and *why* — a North Star metric and its input metrics, an AARRR/funnel framing for this specific app, a strict event taxonomy with naming conventions, and an instrumentation specification table (event → trigger → properties → owner → funnel step) — so that when analytics is actually instrumented, every event already has a name, a schema, an owner, and a reason to exist. This is the design that prevents the most common analytics failure: shipping hundreds of inconsistent, untyped, PII-leaking events that no one can answer questions with.

**When to Use:** Use this prompt once MVP scope is set but *before* adding the analytics SDK or logging the first event. Use it when you cannot yet answer "what is the one number that says this app is working?", when events are being added ad hoc with inconsistent names, when you need a shared event schema across the team, or when you must reconcile measurement with the app's privacy/consent posture before launch. The output is a measurement plan, not instrumentation code.

**Sequence Map:** Use after MVP scope (`android_mvp_scope_and_release_roadmap.md`); use before any instrumentation.

**Important context:** A measurement plan is upstream of tooling. The dominant Android stack is **Firebase Analytics (GA4)**, which imposes hard rules you must design within: event names are **snake_case**, there are **reserved/automatically-collected events** (e.g., `screen_view`, `first_open`, `session_start`, `in_app_purchase`) you must not redefine, parameter names and counts are limited, and meaningful business events are marked as **key events** (formerly "conversions") in GA4. GA4 also distinguishes **user properties** (slow-changing traits, capped per project) from **event parameters** (per-event context). On Android, advertising/attribution measurement involves the **Advertising ID (Ad ID)** and, on Android 13+, the `com.google.android.gms.permission.AD_ID` manifest permission — and *all* measurement must respect user consent and the Play **Data Safety** declaration. Design the plan so that no event parameter ever carries PII.

---

## Context Gathering

Before defining metrics, gather:

1. **What success means:**
   - "In one sentence, what does this app do for a user, and what does a *successful* use look like?"
   - "If you could only watch one number to know the app is healthy, what would it be?"
   - "Is value delivered per-session, per-day, or over weeks (affects the North Star cadence)?"

2. **The core funnel:**
   - "Walk me through the path from first open to the core value moment — what are the discrete steps?"
   - "Where do you suspect users drop off today (or expect to)?"

3. **Decisions the data must serve:**
   - "What product decisions will you make with this data (onboarding changes, paywall timing, feature cuts)?"
   - "Who owns acting on each part of the funnel?"

4. **Privacy & tooling constraints:**
   - "Do you have/need a consent flow (EU/EEA, etc.)? What's your Data Safety posture?"
   - "Is attribution/ads measurement needed (affects Ad ID + AD_ID permission), or is product analytics only?"
   - "Firebase Analytics/GA4, or is another tool already in play?"

---

## Instructions

### Phase 1: North Star Metric & Input Metrics

Define the single metric that best captures delivered value, then the 3–5 *input* metrics that move it.

```
North Star: <one metric that reflects real user value, not vanity>
  Examples by app type:
    - Productivity tool → "weekly active users who complete ≥1 core task"
    - Content app      → "weekly time spent in core content"
    - Marketplace      → "weekly successful transactions"

Input metrics (leading indicators that drive the North Star):
  1. <activation rate: % of new users reaching the value moment>
  2. <core-action frequency per active user>
  3. <retention: D1 / D7 / D30>
  4. <funnel conversion at the weakest step>
```

> **CHECKPOINT 1 — North Star lock.** Present the North Star + input metrics and confirm it reflects *value*, not vanity (installs, raw screen views). Do not build the taxonomy until this is agreed.

### Phase 2: AARRR / Funnel Framing

Map the app to the pirate-metrics funnel (adapt stages to the app):

| Stage | Question it answers | Example signal for this app |
|-------|---------------------|-----------------------------|
| **Acquisition** | How do users arrive? | `first_open`, install source, campaign |
| **Activation** | Do they reach first value fast? | completed onboarding, first core action |
| **Retention** | Do they come back? | D1/D7/D30 return, session frequency |
| **Revenue** | Do they pay? | trial start, purchase, subscription renewal |
| **Referral** | Do they bring others? | share, invite sent/accepted |

For each stage, name the **one** funnel step that matters most for this app and which event will measure it. This becomes the spine of the taxonomy.

### Phase 3: Event Taxonomy & Naming Conventions

Lock conventions *before* listing events. Apply GA4 rules.

| Rule | Convention |
|------|------------|
| Case | `snake_case` for event names and parameter keys |
| Verb-object | Name events `object_action` (e.g., `task_created`, `paywall_viewed`) — consistent and sortable |
| Reserved events | Do **not** redefine GA4 reserved/auto events (`screen_view`, `first_open`, `session_start`, `in_app_purchase`, etc.) |
| Cardinality | Avoid high-cardinality values in parameters (no free-text, no IDs that explode dimensions) |
| Limits | Respect GA4 limits on event count, parameter count per event, and parameter name/value length |
| Key events | Mark business-critical events (e.g., `purchase`, `signup_completed`) as **key events / conversions** in GA4 |
| No PII | **Never** put names, emails, phone numbers, precise location, or raw IDs in parameters |

**Naming examples (good vs. bad):**

| Bad | Why | Good |
|-----|-----|------|
| `ButtonClick` | PascalCase, no object | `cta_tapped` (+ param `cta_id`) |
| `user_signed_up_via_google_oauth` | overloaded, high cardinality | `signup_completed` (+ param `method=google`) |
| `event1` | meaningless | `task_created` |
| `purchase_user_john@x.com` | PII in name | `purchase` (+ user property, no PII) |

### Phase 4: Instrumentation Spec Table

This is the core deliverable — the contract engineers implement against. One row per event.

| Event name | Trigger (when it fires) | Parameters (key:type) | User props touched | Funnel step | Key event? | Owner |
|------------|-------------------------|------------------------|--------------------|-------------|------------|-------|
| `first_open` | Auto (GA4) | — | — | Acquisition | No | — |
| `onboarding_started` | User opens onboarding screen 1 | `entry_point:string` | — | Activation | No | PM |
| `onboarding_completed` | User finishes last onboarding step | `steps_completed:int` | `onboarded:bool` | Activation | Yes | PM |
| `task_created` | User saves a new task | `task_type:string`, `source:string` | — | Activation/Engagement | No | Eng |
| `paywall_viewed` | Paywall screen shown | `placement:string`, `trigger:string` | — | Revenue | No | Growth |
| `purchase` | Purchase verified | `product_id:string`, `value:double`, `currency:string` | `plan_tier:string` | Revenue | Yes | Growth |
| `share_invite_sent` | User sends an invite | `channel:string` | — | Referral | No | Growth |

Rules for filling the table:
- Every event must tie to a **funnel step** and a **decision** — if it serves no decision, cut it.
- Parameters carry *context*, not identity. `value`/`currency` only on monetary events.
- Mark the small set of **key events** that map to North Star / revenue.
- Assign a single **owner** per event (who acts on it).

### Phase 5: Screen Views, Engagement, and Properties

| Concern | Plan |
|---------|------|
| **screen_view** | Use GA4 automatic `screen_view` with consistent `screen_name` / `screen_class`; define the screen-name vocabulary so it's stable across releases |
| **Engagement** | Rely on GA4 engaged-session/engagement-time; only add custom engagement events for app-specific value moments |
| **User properties vs event params** | User properties = slow-changing traits (`plan_tier`, `onboarded`, `cohort`) set once and reused; event params = per-event context. Respect GA4's user-property cap and never store PII in either |
| **Default vs custom dimensions** | Decide which params must be registered as custom dimensions in GA4 to be queryable |

### Phase 6: Privacy-Respecting Measurement

Bind the plan to the app's privacy posture (coordinate with the privacy-by-design plan).

| Requirement | Plan |
|-------------|------|
| **Consent** | Gate analytics collection on consent where required (EU/EEA, etc.); plan to set GA4 consent mode / disable collection until granted |
| **No PII in events** | Audit every parameter and user property against the no-PII rule before instrumentation |
| **Data Safety** | Every category collected here must match the Play **Data Safety** declaration — analytics that ship without a matching declaration is a policy violation |
| **Advertising ID** | If attribution/ads measurement is needed: plan the **Ad ID** usage and, for Android 13+, the `com.google.android.gms.permission.AD_ID` manifest permission. If *not* needed, declare/exclude AD_ID and document that analytics is product-only |
| **Retention** | Set GA4 data-retention period deliberately; align with the app's data-retention policy |
| **User deletion** | Plan how analytics data is handled on account deletion (consistency with retention policy) |

> **CHECKPOINT 2 — Privacy review.** Confirm consent gating, no-PII audit, Data Safety alignment, and Ad ID/AD_ID decision before finalizing.

### Phase 7: Tooling & Connections (high level)

| Decision | Guidance |
|----------|----------|
| **Tool choice** | Default to **Firebase Analytics (GA4)** for Android (free, native, BigQuery export, integrates with Crashlytics/Remote Config). Consider a product-analytics tool (e.g., dedicated funnel tools) only if you need richer cohorting/session replay — note added cost and a second consent/PII surface |
| **Connect to quality** | Tie engagement/crash-free metrics to Crashlytics + performance data so product and quality metrics share definitions |
| **Connect to privacy** | The taxonomy's collected categories must round-trip into the Data Safety form and privacy policy |
| **Validation** | Plan to validate events with GA4 DebugView before release; events not seen in DebugView are not shipping correctly |

---

## Expected Output

1. **North Star + Input Metrics** — the one health metric and its 3–5 leading indicators.
2. **AARRR Funnel Map** — each stage mapped to this app with the one key step per stage.
3. **Naming Conventions** — snake_case rules, verb-object pattern, reserved-event list, cardinality/limit rules, no-PII rule.
4. **Instrumentation Spec Table** — every event with trigger, typed parameters, user properties, funnel step, key-event flag, and owner.
5. **Screen/Engagement/Property Plan** — screen_view vocabulary, user properties vs event params.
6. **Privacy Plan** — consent gating, no-PII audit, Data Safety alignment, Ad ID/AD_ID decision, retention/deletion.
7. **Tooling Decision** — Firebase/GA4 (or alternative) with rationale and validation approach.

---

## CRITICAL: Verification Requirements

- [ ] A single North Star metric is defined and reflects delivered value, not vanity (installs/raw screen views)
- [ ] 3–5 input metrics are named as leading indicators of the North Star
- [ ] The app is mapped to the AARRR/funnel stages with one key step identified per stage
- [ ] Naming conventions are locked (snake_case, object_action) and reserved GA4 events are not redefined
- [ ] Every event in the spec table has a trigger, typed parameters, a funnel step, an owner, and a reason to exist
- [ ] Business-critical events are flagged as GA4 key events / conversions
- [ ] User properties vs event parameters are correctly distinguished and within GA4 caps
- [ ] No event parameter or user property contains PII (names, emails, phone, precise location, raw IDs)
- [ ] Consent gating is planned where required, and the Ad ID / `AD_ID` (Android 13+) decision is explicit
- [ ] Every collected data category matches the Play Data Safety declaration
- [ ] GA4 data-retention and account-deletion handling are aligned with the app's data-retention policy
- [ ] A validation step (e.g., GA4 DebugView) is planned before release

## False-Positive Prevention

- ❌ Do NOT pick a North Star that is a vanity metric (installs, raw screen views, total events)
- ✅ DO pick a metric that only moves when a user gets real value
- ❌ Do NOT let events accumulate ad hoc with inconsistent names (`ButtonClick`, `event1`, `userSignup`)
- ✅ DO enforce one snake_case `object_action` convention across the whole taxonomy
- ❌ Do NOT redefine GA4 reserved/automatic events or exceed parameter/name limits
- ✅ DO build on the reserved events and respect GA4's documented limits
- ❌ Do NOT put PII (emails, names, precise location, raw IDs) in event parameters or user properties
- ✅ DO carry only non-identifying context, and route identity to consented, non-analytics stores
- ❌ Do NOT ship analytics whose collected categories don't appear in the Data Safety declaration
- ✅ DO reconcile the taxonomy with Data Safety and the privacy policy before instrumenting
- ❌ Do NOT request the `AD_ID` permission "just in case" if you don't do attribution/ads
- ✅ DO make the Ad ID / AD_ID decision deliberately and document product-only analytics when that's the case
- ❌ Do NOT instrument first and define metrics later — that produces unusable data
- ✅ DO finish this plan, then instrument against the spec table
- ❌ Do NOT write SDK/instrumentation code here — this is the measurement plan, not the implementation

## Techniques Used

- **ST-01** (Clear Objective): Focused on producing a measurement plan, not instrumentation
- **ST-02** (Structured Sequential Instructions): North Star → funnel → taxonomy → spec table → privacy → tooling
- **RT-02** (Multi-Dimensional Analysis): Frames the app across AARRR stages and event/property dimensions
- **CM-01** (Explicit Context Framing): Gathers success definition, funnel, and privacy constraints first
- **AG-02** (Skeptical Default Stance): Defaults to cutting events that serve no decision and rejecting PII/vanity metrics
- **NE-02** (Phased Workflow Architecture): Checkpoint gates at North Star and privacy review

## Related Prompts

- [android_mvp_scope_and_release_roadmap.md](android_mvp_scope_and_release_roadmap.md) — Set MVP scope so the funnel and key events match what's actually shipping
- [../targeted-reviews/firebase_analytics_strategy.md](../targeted-reviews/firebase_analytics_strategy.md) — Operationalize this plan with a Firebase/GA4 analytics strategy
- [android_privacy_by_design_and_permissions_plan.md](android_privacy_by_design_and_permissions_plan.md) — Align the measurement plan with consent, Data Safety, and permissions

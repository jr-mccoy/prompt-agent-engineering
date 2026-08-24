---
title: "Android Privacy-by-Design & Permissions Plan"
category: mobile-development
description: "Decide what data an Android app collects and which runtime permissions it requests before building — minimizing both — then map the result to the Play Console Data Safety form, audit third-party SDK data sharing, and flag children's-data obligations."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-02
  - AG-12
  - NE-02
difficulty: intermediate
tags:
  - android
  - privacy-by-design
  - permissions
  - data-safety
  - data-minimization
  - photo-picker
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - android_data_retention_policy_design.md
  - ../publishing/android_privacy_compliance.md
  - ../publishing/play_store_data_safety_generator.md
  - ../analysis/android_privacy_data_flow_audit.md
---

# Android Privacy-by-Design & Permissions Plan

**Objective:** Produce a planning-stage privacy and permissions plan for an Android app so privacy is designed in rather than retrofitted — building a data-collection register (what data, why, where stored, who it is shared with), challenging every data point against a minimization test, selecting least-privilege permission alternatives and a request UX/timing strategy, auditing third-party SDK data sharing, defining user consent and privacy controls, and mapping every collected data type to the Play Console Data Safety form (including the Families/children's-data flag).

**When to Use:** Use this prompt after concept validation and feature scoping but before implementation begins — when you are deciding which APIs, SDKs, and permissions the app will use. Also use it before a Play Store submission to reconcile your real data behavior with the Data Safety declaration, or when a feature request ("add contact import", "add location-based search") would expand your data footprint and you need to decide whether the benefit justifies the privacy cost.

**Sequence Map:** Use after `android_app_concept_validation.md` and `android_feature_specification.md`; use before `android_project_scaffold.md`, security-sensitive implementation, and `../publishing/play_store_data_safety_generator.md`.

**Important context:** On modern Android, every permission you request and every data point you collect is a liability — it expands your attack surface, your Data Safety obligations, your privacy-policy commitments, and your Play policy exposure. The platform has spent years giving developers least-privilege alternatives (Photo Picker, scoped storage, Health Connect, approximate location, restricted package visibility) precisely so apps can deliver features without broad data access. Privacy-by-design means the default answer to "should we collect/request this?" is **no** until a concrete feature justifies it. The Data Safety form is a binding declaration: it must match what the app and its SDKs actually do, including data your analytics or ads SDK collects on your behalf. Get this right at planning time and implementation, the privacy policy, and the store listing all fall out of one consistent source of truth.

---

## Context Gathering

1. **Product & Data Surface:**
   - "What features does the app have, and what data does each feature genuinely require to function?"
   - "Is there a backend/account, or is the app fully on-device?"
   - "Do you process any payments, health, financial, or location data?"

2. **Permissions & APIs:**
   - "Which device capabilities do features touch (camera, photos/media, location, contacts, microphone, notifications, Bluetooth, files)?"
   - "Do you need to query or launch other apps on the device?"
   - "What `minSdk`/`targetSdk` are you targeting? (Affects which scoped APIs are available/required.)"

3. **Third Parties:**
   - "Which SDKs will you embed (analytics, crash reporting, ads, attribution, A/B testing, auth, maps)?"
   - "Any advertising or attribution SDK? (These almost always collect and share data.)"

4. **Audience & Jurisdiction:**
   - "Is the app directed at children, or mixed-audience? (Triggers Families policy + COPPA.)"
   - "Do you have EU/UK (GDPR), California (CCPA/CPRA), or other regulated users?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before declaring the plan complete, you MUST:**

1. **Tie every collected data point to a specific feature** — if no shipping feature needs it, it should not be collected.
2. **Account for SDK-collected data** — data an ads/analytics SDK gathers counts as *your* collection/sharing on the Data Safety form.
3. **Prefer the least-privilege API** — only fall back to a broad permission when a documented platform alternative genuinely cannot deliver the feature.
4. **Reconcile three artifacts** — the data register, the privacy policy, and the Data Safety declaration must describe the same behavior.
5. **Decide the children's-data question explicitly** — never leave the Families/age flag undetermined.

**A lean plan that collects almost nothing is the best outcome, not a sign of missing analysis.** State clearly when "collect nothing / request nothing" is the right call.

### False-Positive Prevention

- ❌ Do NOT request a permission "to be safe" or "in case we need it later"
- ❌ Do NOT assume an SDK is privacy-neutral without reading what it transmits
- ❌ Do NOT use `READ_MEDIA_IMAGES`/`READ_MEDIA_VIDEO` when the Photo Picker covers the use case
- ❌ Do NOT declare `QUERY_ALL_PACKAGES` to "make intents work" — use a scoped `<queries>` element
- ❌ Do NOT mark Data Safety fields as "not collected" while an embedded SDK collects them
- ✅ DO start from zero data/zero permissions and justify each addition against a feature
- ✅ DO map every data type to a least-privilege alternative before accepting the broad option
- ✅ DO request permissions in-context with a rationale, and design a graceful denial path
- ✅ DO treat the Data Safety form as the binding output the whole plan must satisfy

---

### Phase 1: Data Collection Register

Build the foundational inventory. One row per distinct data element the app or its SDKs will touch.

| # | Data Element | Driving Feature | Why Required | On-Device / Sent to Backend / Sent to 3rd Party | Sensitivity | Optional or Required | Decision |
|---|--------------|-----------------|--------------|--------------------------------------------------|-------------|----------------------|----------|
| 1 | Email address | Account login | Identify the user across devices | Backend | PII | Required | Keep |
| 2 | Display name | Profile | Show in UI / social features | Backend | PII | Optional | Keep |
| 3 | Precise location | "Near me" search | Rank nearby results | Backend (transient) | Sensitive (location) | Optional | **Downgrade → approximate** |
| 4 | Photos | Avatar upload | User-chosen avatar | Backend | User content | Optional | Keep (via Photo Picker, no permission) |
| 5 | Advertising ID | Ads SDK | Ad targeting / attribution | 3rd party (ads) | Identifier | Optional | **Challenge — drop if non-personalized ads suffice** |
| 6 | Crash stack traces | Stability | Diagnose crashes | 3rd party (crash SDK) | Diagnostics | Required | Keep (no user identifiers in payload) |
| 7 | Contacts | "Invite friends" | Suggest contacts to invite | Backend | Sensitive (contacts) | Optional | **Challenge — use share-sheet invite instead** |

> Build this table from the user's actual feature list. Every row must trace to a row in the feature spec.

**CHECKPOINT 1 — Register review:** Present the register and pause. Confirm with the user which rows survive before proposing permissions.

---

### Phase 2: Data Minimization Challenge

For every row in the register, apply the minimization test and record the verdict.

```
For each data element, ask in order:
  1. Does a SHIPPING feature break without it?           → No  → DROP
  2. Can a LESS sensitive form satisfy the feature?      → Yes → DOWNGRADE
        (precise→approximate location; full address→postal code;
         DOB→age range; exact GPS→city)
  3. Can it stay ON-DEVICE instead of leaving the phone? → Yes → KEEP LOCAL (not "collected")
  4. Can it be DERIVED/aggregated instead of stored raw? → Yes → AGGREGATE
  5. Is it only needed transiently?                      → Yes → PROCESS-AND-DISCARD (don't persist)
  Otherwise                                              → KEEP, justify in register
```

| Data Element | Minimization Verdict | Resulting Behavior |
|--------------|----------------------|--------------------|
| Precise location | Downgrade | Request approximate (`ACCESS_COARSE_LOCATION`) only |
| Contacts | Drop | Use system share sheet for invites (no contact access) |
| Advertising ID | Drop (if non-personalized ads acceptable) | Configure SDK for non-personalized ads |
| Date of birth | Downgrade | Collect age range / over-13 flag instead |

---

### Phase 3: Runtime Permission Strategy (Least Privilege)

Choose the **narrowest** mechanism that delivers each feature. Map needs to platform alternatives:

| Feature Need | Broad Permission (avoid) | Least-Privilege Alternative | Notes |
|--------------|--------------------------|-----------------------------|-------|
| Pick a photo/video | `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO` | **Photo Picker** (`PickVisualMedia`) | No permission prompt at all; user selects exactly what they share |
| Limited media access | `READ_MEDIA_*` (all) | **Partial media access** (`READ_MEDIA_VISUAL_USER_SELECTED`) | If you truly must use the media APIs, request user-selected subset |
| Save/share a file | `WRITE_EXTERNAL_STORAGE` | **Scoped storage** (`MediaStore`) / SAF (`ACTION_CREATE_DOCUMENT`) | No broad storage permission needed |
| Health/fitness data | Sensor permissions / scraping | **Health Connect** APIs | Granular, user-controlled, off by default |
| "Near me" | `ACCESS_FINE_LOCATION` | **`ACCESS_COARSE_LOCATION`** | Request precise only if the feature truly needs meters-level accuracy |
| Background location | `ACCESS_BACKGROUND_LOCATION` | Foreground-only + separate later request | Heavily scrutinized by Play review; require a strong justification |
| Launch/inspect other apps | `QUERY_ALL_PACKAGES` | **`<queries>`** element listing specific intents/packages | `QUERY_ALL_PACKAGES` requires a sensitive-permission declaration and Play approval |
| Notifications | (implicit, pre-13) | Runtime `POST_NOTIFICATIONS` (API 33+) | Request in-context when the user opts into a notifying feature |
| Bluetooth scan | Location permission (legacy) | `BLUETOOTH_SCAN` with `neverForLocation` flag | Decouples BT from location on API 31+ |

**Manifest snippet — scoped package visibility instead of `QUERY_ALL_PACKAGES`:**

```xml
<!-- Declare ONLY the interactions you need, not blanket visibility -->
<queries>
    <intent>
        <action android:name="android.intent.action.SEND" />
        <data android:mimeType="image/*" />
    </intent>
    <package android:name="com.example.partnerapp" />
</queries>
```

**Photo Picker — feature without a permission:**

```kotlin
val pickMedia = registerForActivityResult(
    ActivityResultContracts.PickVisualMedia()
) { uri ->
    // uri is the single item the user explicitly chose — no READ_MEDIA_* needed
    if (uri != null) viewModel.onAvatarSelected(uri)
}
// Launch with image-only filter
pickMedia.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
```

---

### Phase 4: Permission Request UX & Timing

Decide *when* and *how* each surviving permission is requested. Document a row per permission.

| Permission | Trigger Point (in-context) | Pre-Prompt Rationale Shown? | On Denial | On "Don't ask again" |
|------------|---------------------------|-----------------------------|-----------|----------------------|
| `ACCESS_COARSE_LOCATION` | User taps "Search near me" | Yes — explain ranking benefit | Fall back to manual city entry | Show settings deep-link, keep manual entry |
| `POST_NOTIFICATIONS` | User enables a reminder | Yes — explain what notifications they'll get | Feature works, no push | Inline note + settings link |
| `CAMERA` | User taps "Scan code" | Yes | Offer manual entry | Settings link, manual entry stays primary |

**Rules:**
- Never request a permission at app launch / cold start with no context.
- Always provide a degraded-but-functional path when the user denies — the feature must not dead-end.
- Use `shouldShowRequestPermissionRationale()` to decide between re-prompting and routing to settings.

---

### Phase 5: Third-Party SDK Data-Sharing Audit

Every embedded SDK that transmits data makes *you* a collector/sharer on the Data Safety form. Audit before adoption.

| SDK | Purpose | Data It Collects | Data It Shares | Configurable to Collect Less? | Data Safety Impact | Decision |
|-----|---------|------------------|----------------|-------------------------------|--------------------|----------|
| Analytics SDK | Product metrics | App interactions, device IDs | Aggregated to vendor | Yes — disable IDFA/ad-ID, anonymize IP | Must declare "App activity (collected)" | Adopt with privacy config |
| Crash SDK | Stability | Stack traces, device model | To vendor | Yes — strip PII from logs | Declare "Crash logs (collected)" | Adopt |
| Ads SDK | Monetization | Advertising ID, coarse location | To ad networks (shared) | Partial — non-personalized mode | Declare "shared" + advertising purpose | Re-evaluate vs. minimization verdict |
| Attribution SDK | Install source | Device fingerprint, referrer | To vendor + partners | Limited | Heavy declaration | Drop unless attribution is essential |

**For each SDK, record:** the vendor's data-collection disclosure, whether you can configure it down, and the exact Data Safety rows it forces.

---

### Phase 6: Consent & User Privacy Controls

Define the controls the app must ship to honor its declarations.

| Control | Required When | Implementation Note |
|---------|---------------|---------------------|
| Account deletion (in-app) | Account exists | Play requires an in-app path *and* a web deletion URL |
| Data export | GDPR/CCPA users | Provide machine-readable export of user data |
| Analytics opt-out | Analytics/ads SDK present | Toggle that disables SDK collection at runtime |
| Personalized-ads opt-out | Ads SDK present | Switch SDK to non-personalized mode |
| Consent gate (EU) | EU users + ads/analytics | Show consent UI before initializing data-collecting SDKs |
| Permission revocation handling | Any runtime permission | App must function (degraded) if permission later revoked in Settings |

---

### Phase 7: Play Console Data Safety Form Mapping

Translate the surviving register into the exact declaration. This is the binding output.

| Play Data Type | Collected? | Shared? | Purpose(s) | Optional? | Encrypted in Transit | User Can Request Deletion |
|----------------|-----------|---------|------------|-----------|----------------------|---------------------------|
| Email address (Personal info) | Yes | No | Account management | No | Yes | Yes |
| Name (Personal info) | Yes | No | Account management | Yes | Yes | Yes |
| Approximate location | Yes | No | App functionality | Yes | Yes | Yes |
| Photos (Photos/videos) | No* | No | — | — | — | — |
| Advertising ID | Depends on Phase 5 | If ads SDK shares | Advertising | Yes | Yes | n/a |
| Crash logs (App info & performance) | Yes | No | Analytics / stability | No | Yes | n/a |
| App interactions (App activity) | Yes (analytics) | No | Analytics | No | Yes | n/a |

> *Photos selected via the Photo Picker and uploaded as user content may still need declaration if stored on your backend — decide based on whether you persist them. Mark each cell from the register, not from assumption.*

**Children's-data / Families flag:** State explicitly: is the app directed at children, mixed-audience, or adults-only? If children are in scope, flag COPPA/Families-policy obligations (no ad-ID for kids, verifiable parental consent, restricted SDK set) and route to `../publishing/android_privacy_compliance.md`.

**CHECKPOINT 2 — Final reconciliation:** Confirm the data register, privacy-policy commitments, and Data Safety declaration all describe the same behavior before sign-off.

---

## Expected Output

1. **Data Collection Register** — every data element with feature justification, storage location, and keep/drop/downgrade decision
2. **Minimization Verdicts** — the test result and resulting behavior per data element
3. **Permission Strategy Table** — each need mapped to its least-privilege alternative, with manifest/code snippets
4. **Permission Request UX Plan** — timing, rationale, and graceful-denial path per permission
5. **SDK Data-Sharing Audit** — what each SDK collects/shares and the Data Safety rows it forces
6. **Privacy Controls List** — account deletion, export, opt-outs, consent gate, revocation handling
7. **Play Data Safety Mapping Table** — collected/shared, purpose, optional, deletion per data type
8. **Children's-Data Determination** — explicit Families/COPPA flag and follow-up actions

---

## CRITICAL: Verification Requirements

- [ ] Every collected data element traces to a specific shipping feature
- [ ] Every data element passed the minimization test (drop / downgrade / keep-local / aggregate / keep)
- [ ] No broad permission is requested where a least-privilege alternative exists (Photo Picker, scoped storage, Health Connect, coarse location, scoped `<queries>`)
- [ ] `QUERY_ALL_PACKAGES` is NOT used; package visibility is scoped via `<queries>`
- [ ] Every runtime permission has an in-context trigger, rationale, and graceful-denial fallback
- [ ] Every embedded SDK's data collection/sharing is audited and reflected in the Data Safety mapping
- [ ] Account deletion (in-app + web URL), data export, and applicable opt-outs are planned
- [ ] The data register, privacy policy, and Play Data Safety declaration describe the same behavior
- [ ] The children's-data / Families policy question is answered explicitly

## False-Positive Prevention

- ❌ Do NOT declare a permission "for future use" — add it when the feature ships
- ❌ Do NOT treat SDK-collected data as outside your Data Safety obligations
- ❌ Do NOT mark a data type "not collected/shared" without checking every SDK's behavior
- ❌ Do NOT request precise location when approximate satisfies the feature
- ❌ Do NOT leave the app without a functional path after a permission denial
- ✅ DO default to zero data and zero permissions, adding only what a feature forces
- ✅ DO prefer Photo Picker, scoped storage, Health Connect, and scoped `<queries>` first
- ✅ DO keep the register, privacy policy, and Data Safety form mutually consistent
- ✅ DO resolve the children's-data flag before implementation begins

## Techniques Used

- **ST-01** (Clear Objective): Plan focuses squarely on minimizing data and permissions before building
- **ST-02** (Sequential Instructions): Register → minimization → permissions → UX → SDK audit → controls → Data Safety mapping
- **RT-02** (Multi-Dimensional Analysis): Each data point evaluated across feature need, sensitivity, storage, and disclosure
- **AG-02** (Skeptical Default Stance): Default answer to "should we collect/request this?" is no until justified
- **AG-12** (Quantitative Metrics): Structured registers and mapping tables make decisions auditable
- **NE-02** (Phased Workflow): Checkpoint gates after the register and before final Data Safety reconciliation

## Related Prompts

- [android_data_retention_policy_design.md](android_data_retention_policy_design.md) — Define how long the data you decide to collect is kept
- [../publishing/android_privacy_compliance.md](../publishing/android_privacy_compliance.md) — Broader privacy/regulatory compliance for publishing
- [../publishing/play_store_data_safety_generator.md](../publishing/play_store_data_safety_generator.md) — Generate the final Data Safety form from this plan
- [../analysis/android_privacy_data_flow_audit.md](../analysis/android_privacy_data_flow_audit.md) — Audit the implemented app's data flows against this plan

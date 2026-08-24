---
title: "Play Store Data Safety Generator"
category: mobile-development
description: "Generate an accurate Google Play Store Data Safety section by analyzing app code and SDKs, covering data collection mapping, data sharing analysis, encryption status, data deletion capabilities, common SDK data profiles, and Data Safety questionnaire walkthrough"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - CM-01
  - QA-01
  - DS-06
  - DT-01
difficulty: intermediate
tags:
  - android
  - play-store
  - data-safety
  - privacy
  - sdk-analysis
  - compliance
  - solo-developer
  - mobile-development
updated: "2026-02-11"
---

# Play Store Data Safety Generator

> Part of the end-to-end flow: see [`android_release_governance_runbook.md`](android_release_governance_runbook.md).

**Objective:** Generate an accurate Google Play Store Data Safety section by analyzing the app's codebase, manifest, and integrated SDKs. Covers identifying ALL data collection (both explicit user input and implicit collection from SDKs like Firebase Analytics, Crashlytics, and AdMob), mapping data sharing with third parties, assessing encryption status, evaluating data deletion capabilities, profiling common SDK data collection behaviors, and walking through the complete Data Safety questionnaire -- producing a ready-to-submit Data Safety declaration that accurately reflects the app's actual data practices.

**When to Use:** Use this prompt before initial app submission to the Play Store, when adding or removing SDKs, when updating your app's data handling (new features that collect data, new third-party integrations), during annual Data Safety audits, or after receiving a Data Safety inaccuracy warning from Google. The Data Safety section is mandatory for all apps on Google Play. Inaccurate declarations -- whether over-reporting or under-reporting -- can result in enforcement action. Under-reporting is particularly risky because it constitutes a policy violation.

**Important context:** The Data Safety section is a self-declaration. Google does not automatically scan your app to populate it. You are responsible for accuracy, including data collected by third-party SDKs you integrate. Google can and does verify Data Safety declarations against actual app behavior. As of 2024, Google has increased enforcement actions against inaccurate Data Safety sections. The declaration must cover ALL data collection and sharing, including data collected automatically by SDKs even if you never explicitly coded for it.

---

## Context Gathering

Before generating the Data Safety section, gather essential context:

1. **App Architecture:**
   - "What SDKs and third-party libraries does your app use? (Check your build.gradle dependencies)"
   - "Does your app have user accounts (login, registration)?"
   - "Does your app store data locally, on a remote server, or both?"
   - "Does your app use WebViews that load third-party content?"

2. **Data Collection:**
   - "What information do users explicitly enter into your app (name, email, photos, etc.)?"
   - "Does your app access device sensors (location, camera, microphone, accelerometer)?"
   - "Does your app read contacts, calendar, call logs, SMS, or files?"
   - "Does your app use device identifiers (Android ID, advertising ID, IMEI)?"

3. **Data Handling:**
   - "Is all network traffic encrypted (HTTPS only)?"
   - "Can users request deletion of their data? How?"
   - "Do you have a data retention policy? How long is data kept?"
   - "Is sensitive data encrypted at rest (EncryptedSharedPreferences, encrypted DB)?"

4. **Third-Party Sharing:**
   - "Does your app display ads? Which ad networks?"
   - "Does your app use social login (Google Sign-In, Facebook Login)?"
   - "Do you share data with analytics, attribution, or marketing services?"
   - "Do you use any crash reporting that includes user-identifiable data?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY Data Safety declaration, you MUST:**

1. **Audit the actual dependency tree** - Do not rely solely on what the developer tells you. Check `build.gradle` files, `libs/` directories, and transitive dependencies. SDKs pulled in as transitive dependencies collect data too.
2. **Check SDK documentation for data collection** - Each SDK has published data collection disclosure. Firebase, for example, publishes exactly what each Firebase product collects. Use these primary sources, not assumptions.
3. **Distinguish between collected and shared** - Google Play defines "collected" as data sent off the device that you or your SDK retains. "Shared" is data transferred to a third party. These are different declarations.
4. **Verify encryption claims** - Do not declare "data encrypted in transit" unless you have confirmed HTTPS for all network calls, including SDK calls. Check `network_security_config.xml` and `android:usesCleartextTraffic`.
5. **Test data deletion** - Do not declare "users can request data deletion" unless a working mechanism exists. This means account deletion, data export, or a documented email process that you actually respond to.

**Declaring NO data collection is sometimes accurate.** A purely offline app with no analytics, no crash reporting, no network calls, and no SDKs that phone home legitimately collects no data. Do not manufacture data collection that does not exist.

### False-Positive Prevention

- Do NOT assume every app collects location data (many apps do not use location at all)
- Do NOT declare data collection for SDKs that are included but disabled or not initialized
- Do NOT mark data as "shared" when it is only "collected" (these are distinct in the questionnaire)
- Do NOT declare personal data collection for anonymous/aggregated analytics without user identifiers
- Do NOT skip SDK transitive dependencies -- they can add data collection you did not intend
- DO verify each SDK is actually initialized and active, not just present in dependencies
- DO check for Firebase auto-initialization (it can collect data even without explicit init calls)
- DO distinguish between data collected for app functionality vs. analytics vs. advertising
- DO check if ad SDK is in test mode vs. production mode (test mode may collect less data)
- DO verify that declared data deletion actually works end-to-end

---

### Phase 1: SDK Inventory

Identify every SDK and library in the app that may collect or transmit data.

#### 1.1 Dependency Audit

**Check these sources for SDK dependencies:**

```
Primary sources:
1. app/build.gradle (or build.gradle.kts)
   - implementation, api, and runtimeOnly dependencies
   - Pay attention to BOM (Bill of Materials) imports

2. Transitive dependencies
   - Run: ./gradlew app:dependencies --configuration releaseRuntimeClasspath
   - This shows the FULL dependency tree including transitives

3. libs/ directory
   - Check for manually included JAR/AAR files

4. AndroidManifest.xml (after merge)
   - Run: ./gradlew app:processReleaseManifest
   - Check merged manifest for auto-registered providers/receivers
   - SDKs often register ContentProviders that auto-initialize
```

**SDK inventory template:**

| SDK Name | Version | How Included | Auto-Initializes? | Data Collection Docs URL |
|----------|---------|-------------|-------------------|--------------------------|
| Firebase Analytics | [ver] | BOM | Yes (ContentProvider) | [URL] |
| Firebase Crashlytics | [ver] | BOM | Yes | [URL] |
| [SDK] | [ver] | [direct/transitive] | [Yes/No] | [URL] |

#### 1.2 Detecting Auto-Initialization

Some SDKs collect data immediately upon app start without explicit initialization:

```
Firebase auto-initialization check:
  - Firebase SDKs use FirebaseInitProvider (ContentProvider)
  - This runs BEFORE Application.onCreate()
  - To disable: Add to AndroidManifest.xml:
    <provider
        android:name="com.google.firebase.provider.FirebaseInitProvider"
        android:authorities="${applicationId}.firebaseinitprovider"
        tools:node="remove" />
  - If NOT disabled, Firebase Analytics collects data automatically

Check for auto-init in merged manifest:
  Search merged AndroidManifest.xml for:
  - ContentProvider entries from SDKs
  - Receiver entries with BOOT_COMPLETED
  - Service entries that run on app start
```

#### 1.3 Common SDK Auto-Initialization Behaviors

```
SDKs that auto-initialize and collect data:
  - Firebase Analytics: YES (unless explicitly disabled)
  - Firebase Crashlytics: YES (crash data from first crash)
  - Facebook SDK: YES (app events logged automatically)
  - Google Play Services: YES (device identifiers)
  - Adjust/AppsFlyer: Depends on initialization timing
  - OneSignal: YES (device token and metadata)

SDKs that do NOT auto-initialize:
  - Retrofit/OkHttp: No (network library, no data collection)
  - Room/SQLite: No (local database, no transmission)
  - Glide/Coil: No (image loading, no tracking)
  - Jetpack Compose: No (UI framework)
  - Dagger/Hilt: No (dependency injection)
```

---

### Phase 2: Data Collection Mapping

Map every type of data the app collects, both from explicit user input and implicit SDK collection.

#### 2.1 Explicit Data Collection (User Input)

Scan the app's code for user-provided data:

```
Search patterns for explicit collection:
  - EditText, TextField, TextInputLayout (text input fields)
  - Registration/login screens (email, password, name)
  - Profile screens (bio, photo, preferences)
  - Forms (address, phone, payment)
  - Photo/video capture or selection
  - File uploads
  - Location permission requests
  - Contact access
  - Calendar access
```

**Document each explicit collection point:**

| Data Type (Google Category) | Collection Point | Purpose | Required or Optional | User Can Delete? |
|---------------------------|-----------------|---------|---------------------|-----------------|
| Name | Registration screen | Account creation | Required | Yes - account deletion |
| Email address | Registration screen | Account, communication | Required | Yes - account deletion |
| Photos | Photo upload feature | User content | Optional | Yes - in-app delete |
| [Type] | [Where in app] | [Why] | [Required/Optional] | [How] |

#### 2.2 Implicit Data Collection (SDK-Driven)

This is where most Data Safety inaccuracies occur. Use the SDK profiles below.

**Firebase Analytics (if included and not disabled):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| App interactions | Yes (automatic events) | Analytics | Yes (analytics opt-out) |
| Other app performance data | Yes (screen views, sessions) | Analytics | Yes (analytics opt-out) |
| Device or other IDs | Yes (app instance ID) | Analytics | Yes (reset app instance ID) |
| Other diagnostic data | Yes (OS version, device model) | Analytics, App functionality | No |

**Firebase Crashlytics (if included):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| Crash logs | Yes | App functionality (stability) | Yes (opt-out available) |
| Other diagnostic data | Yes (device model, OS, memory) | App functionality | Yes (opt-out available) |
| Other app performance data | Yes (non-fatal events) | App functionality | Yes (opt-out available) |
| Device or other IDs | Yes (Crashlytics install UUID) | App functionality | Yes (data deletion request) |

**Google AdMob (if included):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| Device or other IDs | Yes (advertising ID) | Advertising | Yes (ad personalization opt-out) |
| App interactions | Yes (ad impressions, clicks) | Advertising | No |
| Approximate location | Yes (IP-based) | Advertising | Partial (consent framework) |
| Other diagnostic data | Yes (device info for ad serving) | Advertising | No |

**Facebook SDK (if included):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| Device or other IDs | Yes (device ID, advertising ID) | Analytics, Advertising | Partial |
| App interactions | Yes (app events) | Analytics, Advertising | Yes (limited data use) |
| Purchase history | Yes (if auto-logged) | Advertising | Yes (disable auto-events) |

**Google Sign-In (if included):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| Name | Yes (from Google account) | Account management | Yes (don't use Google Sign-In) |
| Email address | Yes (from Google account) | Account management | Yes (don't use Google Sign-In) |
| Profile photo | Yes (if requested in scope) | Account management | Yes (scope-dependent) |

**Adjust/AppsFlyer (if included):**

| Data Type (Google Category) | Collected? | Purpose | Can User Opt Out? |
|---------------------------|-----------|---------|-------------------|
| Device or other IDs | Yes (advertising ID, device ID) | Analytics, Advertising | Yes |
| App interactions | Yes (install, events) | Analytics | Partial |
| Other diagnostic data | Yes (device info) | Analytics | No |

#### 2.3 Consolidated Data Collection Matrix

Combine all explicit and implicit collection into a single matrix:

```markdown
## Complete Data Collection Matrix

| # | Google Data Category | Google Data Type | Collected? | Source | Purpose | Shared? | Required? | User Delete? |
|---|---------------------|-----------------|-----------|--------|---------|---------|----------|-------------|
| 1 | Personal info | Name | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 2 | Personal info | Email address | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 3 | Personal info | Phone number | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 4 | Personal info | Address | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 5 | Personal info | User IDs | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 6 | Financial info | Purchase history | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 7 | Financial info | Payment info | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 8 | Location | Approximate location | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 9 | Location | Precise location | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 10 | Photos and videos | Photos | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 11 | Photos and videos | Videos | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 12 | Audio files | Voice recordings | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 13 | Files and docs | Files and docs | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 14 | Health and fitness | Health info | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 15 | Health and fitness | Fitness info | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 16 | Messages | Emails | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 17 | Messages | SMS/MMS | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 18 | Messages | In-app messages | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 19 | Contacts | Contacts | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 20 | Calendar | Calendar events | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 21 | App activity | App interactions | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 22 | App activity | In-app search history | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 23 | App activity | Installed apps | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 24 | App activity | Other user-generated content | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 25 | App activity | Other actions | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 26 | Web browsing | Web browsing history | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 27 | App info and performance | Crash logs | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 28 | App info and performance | Diagnostics | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 29 | App info and performance | Other performance data | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
| 30 | Device or other IDs | Device or other IDs | [Y/N] | [App/SDK] | [Purpose] | [Y/N] | [Y/N] | [Y/N] |
```

---

### Phase 3: Data Sharing Analysis

Determine which collected data is shared with third parties.

#### 3.1 Understanding "Shared" vs. "Collected"

```
Google Play definitions:

COLLECTED: Data sent off the device to you (the developer) or
  your SDK provider, where you or the SDK provider retains it.
  - Example: Firebase Analytics sends event data to Google's
    servers. You can access it in the Analytics dashboard.
    This is COLLECTED.

SHARED: Data transferred to a third party.
  - "Third party" = any company other than you or your service
    providers acting on your behalf.
  - Example: AdMob sends data to ad networks to serve targeted
    ads. Those ad networks are third parties. This is SHARED.

Key distinction:
  - Firebase Analytics data sent to Google for YOUR analytics
    dashboard = COLLECTED (Google is your service provider)
  - AdMob data sent to ad networks for ad targeting
    = SHARED (ad networks are third parties)
  - Facebook SDK sending app events to Meta
    = SHARED (Meta is a third party)

Exemptions from "sharing" (still must be declared as "collected"):
  - Service providers processing data on your behalf per your instructions
  - Legal requirements
  - User-initiated transfers (user explicitly shares content)
  - Anonymized/aggregated data that cannot identify individuals
```

#### 3.2 Common SDK Sharing Profiles

```
Firebase Analytics:
  - Data COLLECTED by Google on your behalf (your service provider)
  - NOT typically "shared" unless you export to BigQuery and share that
  - Declaration: Collected = Yes, Shared = No (for standard usage)

Firebase Crashlytics:
  - Data COLLECTED by Google on your behalf
  - NOT shared with third parties
  - Declaration: Collected = Yes, Shared = No

Google AdMob:
  - Data COLLECTED and SHARED with ad networks
  - Ad networks are third parties, not your service providers
  - Declaration: Collected = Yes, Shared = Yes
  - Third parties: Ad networks in your mediation chain

Facebook SDK (analytics/ads):
  - Data SHARED with Meta
  - Meta uses data for its own purposes (ad targeting)
  - Declaration: Collected = Yes, Shared = Yes
  - Third party: Meta Platforms, Inc.

Adjust / AppsFlyer:
  - Data COLLECTED by attribution provider
  - May be SHARED if using data for cross-app attribution
  - Check your specific contract and configuration
  - Declaration: Collected = Yes, Shared = Check contract

Google Sign-In:
  - User-initiated data transfer (user chooses to sign in)
  - Exemption may apply for user-initiated transfers
  - But still declare the data types as collected
```

#### 3.3 Sharing Declaration Template

| Data Type Shared | Shared With | Purpose | Is Sharing Required for App? |
|-----------------|------------|---------|------------------------------|
| Device IDs | Ad networks (via AdMob) | Advertising | No (required for ads, but ads are optional) |
| App interactions | Meta (via Facebook SDK) | Advertising, Analytics | No |
| [Data type] | [Third party] | [Purpose] | [Yes/No] |

---

### Phase 4: Security Practices

Assess and document the app's data security practices.

#### 4.1 Encryption in Transit

```
Verify HTTPS enforcement:

1. Check network_security_config.xml:
   <network-security-config>
       <base-config cleartextTrafficPermitted="false">
           <trust-anchors>
               <certificates src="system" />
           </trust-anchors>
       </base-config>
   </network-security-config>

2. Check AndroidManifest.xml:
   android:usesCleartextTraffic="false"
   (Should be false, or absent -- defaults to false for targetSdk >= 28)

3. Check OkHttp/Retrofit configurations:
   - No HTTP (non-HTTPS) base URLs
   - No cleartext exceptions in network security config

4. Check WebView URLs:
   - No HTTP URLs loaded in WebViews
   - WebView SSL error handling does not bypass validation

If ALL network traffic uses HTTPS:
  → Declare "Data is encrypted in transit" = YES

If ANY cleartext exception exists:
  → Declare "Data is encrypted in transit" = NO (or fix the exception)
```

#### 4.2 Encryption at Rest

```
Check for local data encryption:

1. SharedPreferences:
   - Using EncryptedSharedPreferences? → Encrypted at rest
   - Using regular SharedPreferences? → NOT encrypted at rest
     (Android's file-based encryption protects at device level,
      but Play Console asks about YOUR app-level encryption)

2. Database:
   - Using SQLCipher or encrypted Room? → Encrypted at rest
   - Using standard Room/SQLite? → NOT encrypted at rest

3. Files:
   - Using EncryptedFile API? → Encrypted at rest
   - Storing files in standard internal storage? → NOT encrypted at rest

For Data Safety purposes:
  - "Data encrypted at rest" = YES only if you implement
    app-level encryption for sensitive data
  - Standard Android disk encryption does not count for this declaration
```

#### 4.3 Data Deletion

```
Evaluate data deletion capability:

Account deletion:
  - Can users delete their account in-app? Where?
  - Does account deletion cascade to all user data?
  - Does account deletion remove data from backups?
  - What is the timeline for deletion completion?

Data deletion without account deletion:
  - Can users delete specific data (posts, photos, messages)?
  - Is there a "clear my data" option?

Server-side data:
  - Does deleting in-app also delete server-side copies?
  - Are there retention periods before permanent deletion?
  - Is deleted data removed from analytics/logs?

For Data Safety declaration:
  "Users can request that their data is deleted" = YES if:
    - Account deletion exists (in-app or via documented process)
    - OR a clear mechanism exists to request deletion (email address)
    - AND the developer actually processes these requests

  = NO if:
    - No deletion mechanism exists
    - OR only client-side data is cleared but server data persists
    - OR the declared process does not actually work
```

---

### Phase 5: Questionnaire Completion

Walk through the actual Play Console Data Safety questionnaire with the data gathered in Phases 1-4.

#### 5.1 Question-by-Question Guide

```
Play Console → App content → Data safety → Manage

Question 1: Does your app collect or share any of the required
user data types?

  Answer: YES if your consolidated matrix (Phase 2.3) has ANY "Yes"
  entries. This includes SDK-collected data.

  Answer: NO only if your app is fully offline with no SDKs
  that transmit data. Very few apps legitimately answer No.

Question 2: Is all of the user data collected by your app
encrypted in transit?

  Answer: YES if Phase 4.1 confirms all traffic is HTTPS.
  Answer: NO if any cleartext exception exists.

Question 3: Do you provide a way for users to request that
their data is deleted?

  Answer: YES if Phase 4.3 confirms a working deletion mechanism.
  Answer: NO if no deletion mechanism exists (you should add one).

If answered YES to Question 1, proceed to data type selection:
```

#### 5.2 Data Type Selection Walkthrough

For each data type, the questionnaire asks three questions:

```
For each data type marked "Yes" in your consolidated matrix:

A. Is this data COLLECTED?
   → Yes if data is sent off the device and retained
   → Provide:
     - Is this data collection required or optional?
       (Required = app won't function without it)
       (Optional = user can use app without providing it)
     - Purpose of collection:
       □ App functionality
       □ Analytics
       □ Developer communications
       □ Advertising or marketing
       □ Fraud prevention, security, and compliance
       □ Personalization
       □ Account management

B. Is this data SHARED?
   → Yes if data is transferred to third parties (see Phase 3)
   → Provide:
     - Purpose of sharing:
       □ Advertising or marketing
       □ Analytics
       □ Fraud prevention, security, and compliance
       □ Personalization
       □ Account management
```

#### 5.3 Common App Profile Examples

**Profile: Simple app with Firebase Analytics + Crashlytics (no ads, no accounts):**

```
Data types to declare:

COLLECTED (not shared):
  - App interactions (Analytics - automatic events)
    Purpose: Analytics
    Required: No (analytics is optional)
  - Crash logs (Crashlytics)
    Purpose: App functionality
    Required: No
  - Diagnostics (Crashlytics - device info)
    Purpose: App functionality
    Required: No
  - Other app performance data (Analytics - sessions, screens)
    Purpose: Analytics
    Required: No
  - Device or other IDs (Analytics app instance ID, Crashlytics UUID)
    Purpose: Analytics, App functionality
    Required: No

NOT collected:
  - Everything else (no user accounts, no location, no personal info)
```

**Profile: App with accounts + Firebase + AdMob:**

```
Data types to declare:

COLLECTED AND SHARED:
  - Device or other IDs (AdMob - advertising ID)
    Shared with: Ad networks
    Purpose: Advertising
  - App interactions (AdMob - ad interactions)
    Shared with: Ad networks
    Purpose: Advertising
  - Approximate location (AdMob - IP-based)
    Shared with: Ad networks
    Purpose: Advertising

COLLECTED (not shared):
  - Email address (registration)
    Purpose: Account management
    Required: Yes
  - Name (registration)
    Purpose: Account management
    Required: No (if optional field)
  - App interactions (Analytics)
    Purpose: Analytics
  - Crash logs (Crashlytics)
    Purpose: App functionality
  - Diagnostics (Crashlytics)
    Purpose: App functionality
  - Device or other IDs (Analytics, Crashlytics)
    Purpose: Analytics, App functionality
```

**Profile: Minimal offline app (no SDKs, no network):**

```
Data types to declare: NONE

Answer "No" to Question 1 (does not collect or share user data)

This is rare but legitimate for:
  - Simple utility apps (calculator, flashlight)
  - Offline games with no analytics
  - Tools that process data entirely on-device
```

#### 5.4 Submission Checklist

Before submitting the Data Safety section:

```
Pre-submission verification:

- [ ] Every SDK in the dependency tree is accounted for
- [ ] Auto-initializing SDKs are included even if not explicitly called
- [ ] Data types match what is ACTUALLY collected, not what MIGHT be collected
- [ ] "Shared" declarations match actual third-party data transfers
- [ ] Purpose categories accurately reflect why data is collected
- [ ] "Required vs optional" accurately reflects whether app functions without it
- [ ] Encryption in transit answer matches network security configuration
- [ ] Data deletion answer matches a working, tested deletion mechanism
- [ ] Declarations are consistent with your published privacy policy
- [ ] No SDK was missed because it was a transitive dependency
```

---

## Expected Output

### Data Safety Declaration Report

```markdown
# Data Safety Declaration: [App Name]

## SDK Inventory
| SDK | Version | Data Collection | Auto-Initializes | Documentation |
|-----|---------|----------------|-------------------|---------------|
| [SDK] | [ver] | [summary] | [Yes/No] | [URL] |

## Consolidated Data Collection

### Data Collected
| Data Category | Data Type | Source | Purpose | Required | Shared |
|--------------|-----------|--------|---------|----------|--------|
| [Category] | [Type] | [App/SDK name] | [Purpose] | [Y/N] | [Y/N] |

### Data Shared with Third Parties
| Data Type | Shared With | Purpose |
|-----------|------------|---------|
| [Type] | [Third party] | [Purpose] |

### Data NOT Collected
[List all Google data types NOT collected, confirming absence]

## Security Practices
- **Encrypted in transit:** [Yes/No] — [Evidence]
- **Encrypted at rest:** [Yes/No] — [Evidence]
- **Data deletion available:** [Yes/No] — [Mechanism description]

## Questionnaire Answers

### Question 1: Does your app collect or share user data?
**Answer:** [Yes/No]

### Question 2: Is all data encrypted in transit?
**Answer:** [Yes/No]

### Question 3: Can users request data deletion?
**Answer:** [Yes/No]

### Data Type Declarations
[For each collected/shared data type:]

**[Data Type]:**
- Collected: [Yes]
- Collection purpose: [Purposes]
- Required: [Yes/No]
- Shared: [Yes/No]
- Sharing purpose: [Purposes, if shared]

## Consistency Check
- [ ] Data Safety matches privacy policy
- [ ] Data Safety matches actual app behavior
- [ ] All SDKs accounted for
- [ ] Deletion mechanism tested

## Recommended Privacy Policy Updates
[List any discrepancies between current privacy policy and Data Safety declaration]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Focused Data Safety generation objective
- **ST-02** (Structured Sequential Instructions) - Phased process from SDK inventory through questionnaire completion
- **RT-02** (Multi-Dimensional Analysis) - Multiple data dimensions (collected, shared, purpose, required, deletable)
- **RT-05** (Evidence-Based Reasoning) - SDK documentation references, code-level verification
- **CM-01** (Explicit Context Framing) - Google Play Data Safety definitions and requirements
- **QA-01** (Chain-of-Verification) - Cross-checking declarations against actual app behavior
- **DS-06** (Prioritization Guidance) - Distinguishing collected vs. shared, required vs. optional
- **DT-01** (Hierarchical Task Breakdown) - SDK inventory, data mapping, sharing analysis, security, questionnaire

---

## Related Prompts

- `play_store_policy_compliance_check.md` - Comprehensive policy compliance audit including Data Safety
- `android_privacy_compliance.md` - GDPR, CCPA, and regulatory privacy compliance
- `privacy_policy_generator.md` - Generate a privacy policy consistent with Data Safety declarations
- `play_store_pre_launch_checklist.md` - Pre-launch checklist including Data Safety requirements
- `android_dependency_audit.md` - Audit all dependencies for security and data practices
- `android_local_data_security_audit.md` - Local data storage security assessment

---

## Customization Guide

- **For apps with many SDKs (10+):** Expand Phase 1 with a dedicated SDK-by-SDK deep dive. For each SDK, consult the vendor's published Play Data Safety guidance (most major SDKs now publish this). Use the gradle dependency tree output as the source of truth rather than relying on memory of what was added. Pay special attention to ad mediation SDKs which can pull in dozens of transitive ad network SDKs.
- **For apps with no third-party SDKs:** Simplify Phases 1 and 3 significantly. Focus on Phase 2 (explicit data collection from your own code) and Phase 4 (security practices). Your Data Safety section will be simpler and easier to keep accurate.
- **For apps with ad mediation (AdMob + multiple networks):** Each ad network in your mediation chain is a separate third party that receives shared data. List ALL mediation partners. Check each network's data collection documentation. AdMob's mediation documentation lists what data each partner receives. This is the most common source of under-reporting in Data Safety sections.
- **For apps targeting children (Families policy):** Data collection must be minimal. Ad SDKs must be from Google's certified list. No behavioral advertising data can be collected from children. The Data Safety section must be consistent with Families policy restrictions. If you declare data collection that violates Families policy, you will get flagged.
- **For apps being updated (not first submission):** Compare your existing Data Safety declaration against the audit results. Document what changed and why. If you added a new SDK, the Data Safety section must be updated before the next release. Set a recurring reminder to re-audit whenever dependencies change.
- **For apps using server-side data processing:** The Data Safety section covers client-side collection and sharing. However, if your server shares data with third parties (e.g., sends user data to a marketing platform), that server-side sharing must also be declared. Audit both client and server data flows for completeness.

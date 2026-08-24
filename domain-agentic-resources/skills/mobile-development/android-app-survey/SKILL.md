---
name: android-app-survey
description: "Systematic survey methodology for mapping Android application structure, screens, features, navigation flows, and tech stack into a categorized feature map. Use this skill when performing a behavior audit survey, mapping app features to code, onboarding to an unfamiliar Android codebase, or when users mention 'survey the app', 'map the features', 'what screens does this app have', or 'understand app structure'."
metadata:
  tags:
    - android
    - survey
    - discovery
    - mapping
    - codebase-exploration
  updated: "2026-02-17"
---

# Android App Survey

Systematic methodology for producing a comprehensive yet concise feature map of an Android application. The survey is intentionally breadth-first — it identifies and categorizes everything without going deep on anything. Depth comes later in dedicated analysis phases.

## Purpose

Before you can audit, review, or improve an Android app, you need to know what's there. This skill provides a structured 3-pass scanning methodology that produces a categorized feature map suitable for:
- Letting a developer select which areas to analyze in depth
- Onboarding to an unfamiliar codebase
- Pre-release inventory of all user-facing functionality
- Input to behavior audit, architecture review, or test coverage analysis

## When to Use This Skill

- Performing the survey phase of an Android behavior audit
- First encounter with an Android codebase you haven't worked with before
- Need to inventory all screens, features, and subsystems before deeper analysis
- Developer asks "what does this app actually do?" or "show me all the screens"

## When NOT to Use This Skill

- You already have a feature map and need to go deeper (use `android-behavior-trace` instead)
- You need to analyze a specific feature in depth (this skill stays shallow by design)
- The app is a single-screen utility with no navigation (just read the code directly)
- You need architecture review, security audit, or performance analysis (use the dedicated prompts/skills)

## Survey Methodology: 3-Pass Scan

### Pass 1: Structural Scan (Project Layout)

Scan the project structure to identify the major organizational units.

**What to look for:**

1. **Module structure** — Is this a single-module or multi-module project? List all modules and their apparent purpose.
2. **Package organization** — How is code organized? (by feature, by layer, hybrid?)
3. **Build configuration** — Read `build.gradle.kts` (or `.gradle`) for:
   - `compileSdk` and `targetSdk` versions
   - Key dependencies (Compose, Room, Firebase, Hilt, Retrofit, etc.)
   - Build flavors and product variants
   - Feature flags or build config fields
4. **Manifest scan** — Read `AndroidManifest.xml` for:
   - All declared Activities, Services, BroadcastReceivers, ContentProviders
   - Permissions declared
   - Intent filters (deep links, app links)
   - Exported components
5. **Resource scan** — Quick scan of `res/` for:
   - Navigation graphs (`res/navigation/`)
   - Layout files (if using Views) or lack thereof (if pure Compose)
   - String resources (feature-related string groups)

### Pass 2: Screen & Navigation Scan

Identify every user-facing screen and how users move between them.

**For Jetpack Compose navigation:**
1. Find the NavHost definition(s) — search for `NavHost`, `NavGraphBuilder`, `composable(` route definitions
2. List every route/destination with its composable function
3. Map navigation actions (which screens navigate to which)
4. Identify nested navigation graphs
5. Check for bottom navigation, drawer navigation, or tab patterns

**For Fragment/Activity navigation:**
1. Parse navigation graph XML files
2. List all fragments and their hosting activities
3. Map navigation actions from the graph
4. Identify any programmatic navigation outside the graph

**For both:**
1. Identify the start destination
2. Map the main navigation structure (bottom nav tabs, drawer items, etc.)
3. Note any conditional navigation (auth gates, onboarding flows)
4. Identify deep link entry points

### Pass 3: Feature & Subsystem Inventory

Group what you found into user-facing feature areas and technical subsystems.

**Feature areas** (group by what the user sees/does):
- Authentication (login, register, password reset, social auth)
- Onboarding (first-run experience, tutorials, permissions requests)
- Main content (the primary screens users interact with)
- Settings/Profile (user preferences, account management)
- Data management (CRUD operations, sync, import/export)
- Notifications (push notifications, in-app alerts, reminders)
- Billing/Subscriptions (purchases, subscription management)
- Sharing/Social (sharing content, inviting users)
- Search/Filter (search functionality, filtering, sorting)
- Offline capabilities (what works without network)

**Technical subsystems** (group by infrastructure):
- Database (Room entities, DAOs, migrations)
- Networking (API clients, interceptors, serialization)
- Firebase services (Auth, RTDB, Firestore, Functions, FCM, Crashlytics, Analytics)
- Background work (WorkManager workers, services)
- Dependency injection (Hilt modules, component hierarchy)
- State management (ViewModels, state holders, saved state)
- Location services (if applicable)
- Media handling (camera, gallery, file management)

## Feature Map Template

Present the survey results in this format:

```markdown
# App Feature Map: [App Name]

## Tech Stack
- **Language:** Kotlin [version]
- **UI Framework:** Jetpack Compose / Views / Hybrid
- **Architecture:** MVVM / MVI / Other
- **DI:** Hilt / Koin / Manual
- **Database:** Room [version] / SQLite / None
- **Networking:** Retrofit / Ktor / Firebase only
- **Firebase Services:** [list active services]
- **Build:** Single module / Multi-module ([list modules])
- **Min SDK:** [version] | Target SDK: [version]

## Screens & Navigation
| # | Screen | Route/Destination | Accessed From | Key Actions |
|---|--------|-------------------|---------------|-------------|
| 1 | [Name] | [route or class] | [parent screen] | [what user can do] |

## Feature Areas
### 1. [Feature Area Name] (e.g., Authentication)
- **Screens involved:** [list]
- **Key functionality:** [brief description]
- **Data involved:** [what data is read/written]

### 2. [Feature Area Name]
...

## Technical Subsystems
### Database
- **Entities:** [list Room entities]
- **Key operations:** [brief]

### Networking
- **Endpoints/Services:** [list]

### Background Work
- **Workers:** [list WorkManager workers]
- **Services:** [list services]

### Firebase
- **Services in use:** [list with brief purpose]

## Complexity Indicators
- Total screens: [count]
- Total feature areas: [count]
- Database entities: [count]
- API endpoints/Firebase collections: [count]
- Background workers: [count]
```

## Tech Stack Detection Checklist

Quick detection patterns for common Android tech:

| Technology | Detection Pattern |
|-----------|------------------|
| Jetpack Compose | `implementation("androidx.compose")` in build.gradle |
| Room | `@Database`, `@Entity`, `@Dao` annotations |
| Hilt | `@HiltAndroidApp`, `@AndroidEntryPoint`, `@Module` |
| Firebase Auth | `FirebaseAuth`, `firebase-auth` dependency |
| Firebase RTDB | `FirebaseDatabase`, `DatabaseReference` |
| Firestore | `FirebaseFirestore`, `CollectionReference` |
| Firebase FCM | `FirebaseMessagingService`, `firebase-messaging` |
| Crashlytics | `firebase-crashlytics` dependency |
| WorkManager | `@HiltWorker`, `CoroutineWorker`, `OneTimeWorkRequest` |
| Retrofit | `@GET`, `@POST`, `Retrofit.Builder` |
| Ktor | `HttpClient`, `io.ktor` imports |
| Navigation Compose | `NavHost`, `composable(`, `navigation(` |
| DataStore | `DataStore`, `preferencesDataStore` |
| Coil | `AsyncImage`, `rememberAsyncImagePainter` |
| Billing | `BillingClient`, `com.android.billingclient` |

## Screen Identification Guide

### Composable Screens
Look for top-level composables that represent full screens (not reusable components):
- Functions annotated with or called from `composable()` routes
- Functions that accept a `NavController` or navigation lambda parameter
- Functions with `Scaffold`, `Surface`, or full-screen layout as root
- Naming convention: usually `*Screen` (e.g., `HomeScreen`, `SettingsScreen`)

### Activity-Based Screens
- Classes extending `ComponentActivity` or `AppCompatActivity`
- Declared in `AndroidManifest.xml` with intent filters
- Typically host Compose content via `setContent {}` or Fragment via NavHostFragment

### Fragment-Based Screens
- Classes extending `Fragment` listed in navigation graph XML
- Connected via `<fragment>` or `<dialog>` destinations

### Distinguishing Screens from Components
- **Screen:** Full navigation destination, has its own ViewModel, represents a user-visible page
- **Component:** Reusable UI element, no own ViewModel, used within screens
- **When unsure:** If it's a navigation destination, it's a screen

## Related Skills

- `android-behavior-trace` — Use after survey to trace code behavior in depth for selected areas

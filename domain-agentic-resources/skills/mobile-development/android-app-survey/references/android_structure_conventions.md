# Android Project Structure Conventions

Quick reference for where things typically live in Android projects. Use this to efficiently scan an unfamiliar codebase.

## Standard Project Layout

```
app/
├── build.gradle.kts           # Dependencies, SDK versions, build config
├── src/
│   ├── main/
│   │   ├── AndroidManifest.xml    # Components, permissions, intent filters
│   │   ├── java/ or kotlin/       # Source code
│   │   │   └── com/example/app/
│   │   │       ├── di/            # Hilt modules, component definitions
│   │   │       ├── data/          # Repositories, data sources, models
│   │   │       │   ├── local/     # Room database, DAOs, entities
│   │   │       │   ├── remote/    # API services, Firebase wrappers
│   │   │       │   └── repository/ # Repository implementations
│   │   │       ├── domain/        # Use cases, domain models (if clean arch)
│   │   │       ├── ui/            # Screens, ViewModels, UI state
│   │   │       │   ├── screens/   # Screen composables (by feature)
│   │   │       │   ├── components/ # Reusable UI components
│   │   │       │   ├── navigation/ # NavHost, routes, nav graph
│   │   │       │   └── theme/     # Material theme, colors, typography
│   │   │       ├── workers/       # WorkManager workers
│   │   │       ├── services/      # Android services (FCM, location, etc.)
│   │   │       └── util/          # Utilities, extensions, constants
│   │   └── res/
│   │       ├── navigation/        # Navigation graph XML (if using)
│   │       ├── values/            # strings.xml, colors.xml, themes.xml
│   │       └── ...
│   ├── test/                      # Unit tests
│   └── androidTest/               # Instrumented tests
```

## Alternative Organization Patterns

### Feature-Based (Package-Per-Feature)
```
com/example/app/
├── auth/
│   ├── data/          # Auth data sources, repository
│   ├── ui/            # Login, Register screens + ViewModels
│   └── di/            # Auth-specific Hilt module
├── home/
│   ├── data/
│   ├── ui/
│   └── di/
├── settings/
│   ├── data/
│   ├── ui/
│   └── di/
└── core/              # Shared utilities, base classes, extensions
```

### Layer-Based
```
com/example/app/
├── data/              # All data layer code
├── domain/            # All domain/business logic
├── presentation/      # All UI code
└── di/                # All DI configuration
```

## Key Files to Read First

When surveying an Android project, read these files in this order:

### 1. Build Configuration (2 minutes)
- `build.gradle.kts` (app-level) — Dependencies reveal the tech stack
- `settings.gradle.kts` — Module structure
- `gradle/libs.versions.toml` — Version catalog (if used)

### 2. Manifest (1 minute)
- `AndroidManifest.xml` — All declared components and permissions

### 3. Navigation (2 minutes)
- Search for `NavHost` (Compose) or `res/navigation/*.xml` (Fragment)
- This reveals all screens and how they connect

### 4. DI Configuration (2 minutes)
- Search for `@Module` (Hilt) — Reveals what services are wired up
- `@Provides` and `@Binds` functions show the dependency graph

### 5. Database Schema (1 minute)
- Search for `@Database` — Lists all entities
- Search for `@Entity` — Shows data model
- Search for `@Dao` — Shows data operations

### 6. Entry Point (1 minute)
- Find the `@HiltAndroidApp` Application class
- Find the main Activity (usually has `LAUNCHER` intent filter)

## Common Firebase Integration Points

| Firebase Service | Where to Find It |
|-----------------|-------------------|
| Authentication | `FirebaseAuth.getInstance()`, auth state listeners, sign-in providers |
| Realtime Database | `FirebaseDatabase.getInstance()`, `DatabaseReference`, `.child()` paths |
| Firestore | `FirebaseFirestore.getInstance()`, collection/document references |
| Cloud Functions | `FirebaseFunctions.getInstance()`, `.getHttpsCallable()` |
| FCM | `FirebaseMessagingService` subclass, token registration |
| Crashlytics | Usually auto-configured via gradle plugin |
| Analytics | `FirebaseAnalytics.getInstance()`, `.logEvent()` calls |
| Remote Config | `FirebaseRemoteConfig.getInstance()`, `.fetchAndActivate()` |
| App Check | `FirebaseAppCheck.getInstance()`, provider factory |

## Multi-Module Project Indicators

Signs a project uses multiple Gradle modules:
- Multiple directories at the root level with their own `build.gradle.kts`
- `settings.gradle.kts` includes multiple `include()` statements
- Common patterns: `:app`, `:core`, `:data`, `:domain`, `:feature-*`

When multi-module, scan each module's `build.gradle.kts` to understand its role:
- `:app` — Main application module, usually thin, depends on others
- `:core` — Shared utilities, base classes, extensions
- `:data` — Data layer (Room, API, repositories)
- `:domain` — Business logic, use cases
- `:feature-*` — Feature modules (screens + ViewModels for a feature)

## What NOT to Catalog in Survey Phase

The survey should stay shallow. Do not:
- Analyze code logic or control flow
- Assess code quality or architecture decisions
- Review error handling patterns
- Check for bugs or issues
- Evaluate performance characteristics
- Read implementation details of functions

These all belong in the trace and audit phases, not the survey.

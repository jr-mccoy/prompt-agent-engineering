---
title: "Android Project Scaffold"
category: mobile-development
description: "Generate a production-ready Android project scaffold — Gradle/version-catalog config, package structure, and core boilerplate — from your architecture and stack decisions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-04
  - NE-02
  - NE-07
difficulty: intermediate
tags:
  - android
  - mobile-development
  - scaffolding
  - project-setup
  - gradle
  - boilerplate
updated: "2026-06-06"
---

# Android Project Scaffold

**Objective:** Generate a complete, production-ready Android project structure with properly configured Gradle build files, architecture scaffolding, and essential boilerplate code based on the selected architecture pattern and technology stack.

**When to Use:** Use this prompt when starting a new Android project from scratch after you've made architecture and technology decisions. Ideal after completing concept validation, architecture selection, and tech stack selection. This prompt produces a working project skeleton that follows best practices and is ready for feature development.

**Sequence Map:** Use after architecture, modules, and tech stack are selected; use before feature implementation.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before generating the scaffold, confirm project decisions:

1. **Project Identity:**
   - "What is your app name and package name? (e.g., MyApp, com.example.myapp)"
   - "What is a brief description of the app?"

2. **Architecture Decisions:**
   - "Which architecture pattern? (MVVM, MVI, Clean Architecture + MVVM)"
   - "Single module or multi-module structure?"

3. **Technology Stack:**
   - "UI: Compose only, Views only, or hybrid?"
   - "Networking: Retrofit, Ktor, or none needed initially?"
   - "Database: Room, DataStore only, or none?"
   - "DI: Hilt, Koin, or manual?"

4. **Project Configuration:**
   - "Minimum SDK level? (recommended: 26+)"
   - "Target SDK level? (recommended: 34)"
   - "Kotlin version preference? (recommended: latest stable)"

5. **Additional Features:**
   - "Do you need Firebase integration?"
   - "Include CI/CD configuration? (GitHub Actions)"
   - "Include pre-configured testing setup?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before generating ANY scaffold, you MUST:**

1. **Understand actual requirements** - Don't generate boilerplate for features that aren't needed.
2. **Check for project decisions** - Confirm architecture, tech stack, and configuration choices before generating.
3. **Follow project conventions** - Match specified patterns, naming conventions, and structure.
4. **Provide complete, working code** - Every generated file must be immediately usable.
5. **Include specific file paths** - Every file must include exact paths and complete content.

**A MINIMAL scaffold is often better.** Don't generate unnecessary boilerplate that will need to be deleted.

### Quality Requirements

- ❌ Do NOT generate files for features not requested
- ❌ Do NOT include placeholder TODOs in critical code
- ❌ Do NOT generate outdated dependency versions
- ❌ Do NOT skip essential configuration (signing, ProGuard, etc.)
- ✅ DO generate complete, buildable project files
- ✅ DO use latest stable dependency versions
- ✅ DO include proper .gitignore and essential project files
- ✅ DO match generated code to specified architecture

---

### Phase 1: Project Configuration

#### 1.1 Gradle Configuration

```markdown
## Gradle Setup

### Root build.gradle.kts
```kotlin
// Top-level build file
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.android.library) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.kotlin.compose) apply false
    alias(libs.plugins.hilt) apply false
    alias(libs.plugins.ksp) apply false
}
```

### settings.gradle.kts
```kotlin
pluginManagement {
    repositories {
        google {
            content {
                includeGroupByRegex("com\\.android.*")
                includeGroupByRegex("com\\.google.*")
                includeGroupByRegex("androidx.*")
            }
        }
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "[AppName]"
include(":app")
// Add feature/core modules as needed
```

### gradle/libs.versions.toml
```toml
[versions]
agp = "8.2.0"
kotlin = "1.9.21"
ksp = "1.9.21-1.0.16"

# AndroidX
core-ktx = "1.12.0"
lifecycle = "2.6.2"
activity-compose = "1.8.2"
navigation = "2.7.6"

# Compose
compose-bom = "2024.01.00"

# Hilt
hilt = "2.50"
hilt-navigation = "1.1.0"

# Networking
retrofit = "2.9.0"
okhttp = "4.12.0"
kotlinx-serialization = "1.6.2"

# Database
room = "2.6.1"
datastore = "1.0.0"

# Image Loading
coil = "2.5.0"

# Testing
junit = "4.13.2"
junit-ext = "1.1.5"
espresso = "3.5.1"
mockk = "1.13.8"
turbine = "1.0.0"

[libraries]
# Core
core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "core-ktx" }
lifecycle-runtime-ktx = { group = "androidx.lifecycle", name = "lifecycle-runtime-ktx", version.ref = "lifecycle" }
lifecycle-viewmodel-compose = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
activity-compose = { group = "androidx.activity", name = "activity-compose", version.ref = "activity-compose" }

# Compose
compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-ui = { group = "androidx.compose.ui", name = "ui" }
compose-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics" }
compose-ui-tooling = { group = "androidx.compose.ui", name = "ui-tooling" }
compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }
compose-runtime = { group = "androidx.compose.runtime", name = "runtime" }

# Navigation
navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigation" }

# Hilt
hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-android-compiler", version.ref = "hilt" }
hilt-navigation-compose = { group = "androidx.hilt", name = "hilt-navigation-compose", version.ref = "hilt-navigation" }

# Networking
retrofit = { group = "com.squareup.retrofit2", name = "retrofit", version.ref = "retrofit" }
retrofit-kotlinx-serialization = { group = "com.jakewharton.retrofit", name = "retrofit2-kotlinx-serialization-converter", version = "1.0.0" }
okhttp = { group = "com.squareup.okhttp3", name = "okhttp", version.ref = "okhttp" }
okhttp-logging = { group = "com.squareup.okhttp3", name = "logging-interceptor", version.ref = "okhttp" }
kotlinx-serialization-json = { group = "org.jetbrains.kotlinx", name = "kotlinx-serialization-json", version.ref = "kotlinx-serialization" }

# Database
room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }
datastore-preferences = { group = "androidx.datastore", name = "datastore-preferences", version.ref = "datastore" }

# Image Loading
coil-compose = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }

# Testing
junit = { group = "junit", name = "junit", version.ref = "junit" }
junit-ext = { group = "androidx.test.ext", name = "junit", version.ref = "junit-ext" }
espresso-core = { group = "androidx.test.espresso", name = "espresso-core", version.ref = "espresso" }
compose-ui-test-manifest = { group = "androidx.compose.ui", name = "ui-test-manifest" }
compose-ui-test-junit4 = { group = "androidx.compose.ui", name = "ui-test-junit4" }
mockk = { group = "io.mockk", name = "mockk", version.ref = "mockk" }
turbine = { group = "app.cash.turbine", name = "turbine", version.ref = "turbine" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
android-library = { id = "com.android.library", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
```
```

#### 1.2 App Module Configuration

```markdown
### app/build.gradle.kts
```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
    alias(libs.plugins.kotlin.serialization)
    alias(libs.plugins.hilt)
    alias(libs.plugins.ksp)
}

android {
    namespace = "com.example.myapp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        debug {
            isDebuggable = true
            applicationIdSuffix = ".debug"
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }
}

dependencies {
    // Core
    implementation(libs.core.ktx)
    implementation(libs.lifecycle.runtime.ktx)
    implementation(libs.lifecycle.viewmodel.compose)
    implementation(libs.activity.compose)

    // Compose
    implementation(platform(libs.compose.bom))
    implementation(libs.compose.ui)
    implementation(libs.compose.ui.graphics)
    implementation(libs.compose.ui.tooling.preview)
    implementation(libs.compose.material3)
    debugImplementation(libs.compose.ui.tooling)
    debugImplementation(libs.compose.ui.test.manifest)

    // Navigation
    implementation(libs.navigation.compose)

    // Hilt
    implementation(libs.hilt.android)
    implementation(libs.hilt.navigation.compose)
    ksp(libs.hilt.compiler)

    // Networking (if needed)
    implementation(libs.retrofit)
    implementation(libs.retrofit.kotlinx.serialization)
    implementation(libs.okhttp)
    implementation(libs.okhttp.logging)
    implementation(libs.kotlinx.serialization.json)

    // Database (if needed)
    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)
    implementation(libs.datastore.preferences)

    // Image Loading
    implementation(libs.coil.compose)

    // Testing
    testImplementation(libs.junit)
    testImplementation(libs.mockk)
    testImplementation(libs.turbine)
    androidTestImplementation(libs.junit.ext)
    androidTestImplementation(libs.espresso.core)
    androidTestImplementation(platform(libs.compose.bom))
    androidTestImplementation(libs.compose.ui.test.junit4)
}
```
```

---

### Phase 2: Project Structure Generation

**CHECKPOINT 1:** Confirm configuration before generating structure.

```markdown
## Configuration Summary

### Project Details
- **App Name:** [Name]
- **Package:** [Package]
- **Min SDK:** [X] | **Target SDK:** [Y]

### Architecture
- **Pattern:** [MVVM / MVI / Clean + MVVM]
- **Modules:** [Single / Multi-module]

### Tech Stack
| Category | Choice |
|----------|--------|
| UI | [Compose] |
| DI | [Hilt] |
| Networking | [Retrofit + KotlinX] |
| Database | [Room] |
| Navigation | [Navigation Compose] |

**Ready to generate the project structure?**
```

#### 2.1 Source Code Structure

```markdown
## Project Structure

### MVVM Structure (Single Module)
```
app/src/main/kotlin/com/example/myapp/
├── MyAppApplication.kt
├── MainActivity.kt
├── data/
│   ├── local/
│   │   ├── db/
│   │   │   ├── AppDatabase.kt
│   │   │   ├── dao/
│   │   │   │   └── [Feature]Dao.kt
│   │   │   └── entity/
│   │   │       └── [Feature]Entity.kt
│   │   └── preferences/
│   │       └── UserPreferences.kt
│   ├── remote/
│   │   ├── api/
│   │   │   ├── ApiService.kt
│   │   │   └── [Feature]Api.kt
│   │   └── dto/
│   │       └── [Feature]Dto.kt
│   ├── repository/
│   │   └── [Feature]Repository.kt
│   └── mapper/
│       └── [Feature]Mapper.kt
├── di/
│   ├── AppModule.kt
│   ├── DatabaseModule.kt
│   └── NetworkModule.kt
├── ui/
│   ├── navigation/
│   │   ├── NavGraph.kt
│   │   └── Routes.kt
│   ├── theme/
│   │   ├── Color.kt
│   │   ├── Theme.kt
│   │   └── Type.kt
│   ├── components/
│   │   ├── LoadingIndicator.kt
│   │   └── ErrorView.kt
│   └── [feature]/
│       ├── [Feature]Screen.kt
│       ├── [Feature]ViewModel.kt
│       └── [Feature]UiState.kt
└── util/
    ├── Result.kt
    └── Extensions.kt
```

### Clean Architecture Structure
```
app/src/main/kotlin/com/example/myapp/
├── MyAppApplication.kt
├── MainActivity.kt
├── domain/
│   ├── model/
│   │   └── [DomainModel].kt
│   ├── repository/
│   │   └── [Feature]Repository.kt  (interface)
│   └── usecase/
│       └── [Action][Feature]UseCase.kt
├── data/
│   ├── local/
│   ├── remote/
│   ├── repository/
│   │   └── [Feature]RepositoryImpl.kt
│   └── mapper/
├── presentation/
│   ├── navigation/
│   ├── theme/
│   ├── components/
│   └── [feature]/
│       ├── [Feature]Screen.kt
│       ├── [Feature]ViewModel.kt
│       └── [Feature]UiState.kt
└── di/
```
```

#### 2.2 Core Files Generation

```markdown
## Core Files

### Application Class
```kotlin
// MyAppApplication.kt
package com.example.myapp

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class MyAppApplication : Application()
```

### MainActivity
```kotlin
// MainActivity.kt
package com.example.myapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import com.example.myapp.ui.navigation.AppNavGraph
import com.example.myapp.ui.theme.MyAppTheme
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            MyAppTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    AppNavGraph()
                }
            }
        }
    }
}
```

### Navigation Setup
```kotlin
// ui/navigation/Routes.kt
package com.example.myapp.ui.navigation

import kotlinx.serialization.Serializable

sealed interface Route {
    @Serializable
    data object Home : Route

    @Serializable
    data class Detail(val id: String) : Route
}

// ui/navigation/NavGraph.kt
package com.example.myapp.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.myapp.ui.home.HomeScreen

@Composable
fun AppNavGraph() {
    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = Route.Home
    ) {
        composable<Route.Home> {
            HomeScreen(
                onNavigateToDetail = { id ->
                    navController.navigate(Route.Detail(id))
                }
            )
        }
        composable<Route.Detail> { backStackEntry ->
            // DetailScreen()
        }
    }
}
```

### DI Modules
```kotlin
// di/AppModule.kt
package com.example.myapp.di

import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import javax.inject.Qualifier
import javax.inject.Singleton

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Provides
    @IoDispatcher
    fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO
}

// di/NetworkModule.kt
package com.example.myapp.di

import com.example.myapp.data.remote.api.ApiService
import com.jakewharton.retrofit2.converter.kotlinx.serialization.asConverterFactory
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideJson(): Json = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
    }

    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            .addInterceptor(
                HttpLoggingInterceptor().apply {
                    level = HttpLoggingInterceptor.Level.BODY
                }
            )
            .build()
    }

    @Provides
    @Singleton
    fun provideRetrofit(client: OkHttpClient, json: Json): Retrofit {
        return Retrofit.Builder()
            .baseUrl("https://api.example.com/")
            .client(client)
            .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
            .build()
    }

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService {
        return retrofit.create(ApiService::class.java)
    }
}
```

### Sample Feature (HomeScreen)
```kotlin
// ui/home/HomeScreen.kt
package com.example.myapp.ui.home

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.lifecycle.compose.collectAsStateWithLifecycle

@Composable
fun HomeScreen(
    onNavigateToDetail: (String) -> Unit,
    viewModel: HomeViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    HomeContent(
        uiState = uiState,
        onItemClick = onNavigateToDetail,
        onRefresh = { viewModel.onAction(HomeAction.Refresh) }
    )
}

@Composable
private fun HomeContent(
    uiState: HomeUiState,
    onItemClick: (String) -> Unit,
    onRefresh: () -> Unit
) {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        when {
            uiState.isLoading -> CircularProgressIndicator()
            uiState.error != null -> ErrorContent(
                message = uiState.error,
                onRetry = onRefresh
            )
            else -> Text("Welcome to MyApp!")
        }
    }
}

@Composable
private fun ErrorContent(
    message: String,
    onRetry: () -> Unit
) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(text = message)
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = onRetry) {
            Text("Retry")
        }
    }
}
```
```

---

### Phase 3: Additional Configuration

#### 3.1 AndroidManifest

```xml
<!-- AndroidManifest.xml -->
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:name=".MyAppApplication"
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApp"
        android:networkSecurityConfig="@xml/network_security_config">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.MyApp">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

#### 3.2 Resources

```xml
<!-- res/values/strings.xml -->
<resources>
    <string name="app_name">MyApp</string>
</resources>

<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">api.example.com</domain>
    </domain-config>
</network-security-config>
```

#### 3.3 Git Configuration

```gitignore
# .gitignore
*.iml
.gradle
/local.properties
/.idea
.DS_Store
/build
/captures
.externalNativeBuild
.cxx
local.properties
*.log
```

---

## Expected Output

The scaffold generates:

1. **Gradle Configuration** - Root and app build files with version catalog
2. **Project Structure** - Complete directory layout for chosen architecture
3. **Core Files** - Application, MainActivity, DI modules, navigation
4. **Sample Feature** - Working example feature with ViewModel
5. **Resources** - Manifest, strings, network config
6. **Git Config** - Properly configured .gitignore

---

## Example Interaction

**User:** Create a scaffold for a task management app. Package: com.taskify.app. MVVM with Hilt, Compose, Room, and Retrofit.

**Agent:** I'll generate a complete project scaffold for Taskify. Here's what I'll create:

### Project Configuration
- **App Name:** Taskify
- **Package:** com.taskify.app
- **Min SDK:** 26 | **Target SDK:** 34
- **Architecture:** MVVM
- **UI:** Jetpack Compose
- **DI:** Hilt
- **Database:** Room
- **Networking:** Retrofit + Kotlinx Serialization

### Files to Generate
1. Gradle configuration (root, app, version catalog)
2. Application class with Hilt
3. MainActivity with Compose setup
4. Navigation structure
5. DI modules (App, Network, Database)
6. Theme files
7. Sample TaskList feature
8. Room database setup
9. Retrofit configuration

**Shall I proceed with generating all files?**

---

## Techniques Used

- **ST-01** (Clear Objective): Generate production-ready scaffold
- **ST-02** (Sequential Instructions): Config → Structure → Core Files phases
- **ST-03** (Output Format Templates): Complete code templates
- **RT-04** (Best Practice Review): Current Android best practices
- **NE-02** (Phased Workflow): Checkpoint before generation
- **NE-07** (Discussion Before Action): Confirmation before file creation

---

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) - Select architecture first
- [android_tech_stack_selection.md](android_tech_stack_selection.md) - Select technologies first
- [android_module_design.md](android_module_design.md) - Design multi-module structure
- [android_feature_specification.md](android_feature_specification.md) - Specify first features

---

## Customization Guide

### For Multi-Module Projects
- Generate convention plugins in build-logic/
- Create core modules first
- Feature module templates

### For Minimal Setup
- Skip networking if not needed
- Skip database if not needed
- Simpler DI setup

### For Enterprise Projects
- Add flavor configurations
- Include CI/CD templates
- Add comprehensive ProGuard rules

---
title: "Jetpack Compose to SwiftUI Migration"
category: mobile-development
description: "Map Jetpack Compose patterns to SwiftUI including Composable to View, remember to @State, LaunchedEffect to .task, Modifier to ViewModifier, and Material 3 to iOS design"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - compose
  - swiftui
  - ui-layer
  - material-design
updated: "2026-03-19"
---

# Jetpack Compose to SwiftUI Migration

**Objective:** Provide a comprehensive mapping from Jetpack Compose UI patterns to SwiftUI equivalents, covering composable functions, state management, side effects, modifiers, theming, and layout systems. The output enables developers to translate Compose screens to SwiftUI while adopting platform-idiomatic patterns.

**When to Use:** During the UI layer migration of an Android-to-iOS project. This prompt is for developers who understand Compose and need to build equivalent screens in SwiftUI without porting patterns that are anti-idiomatic on iOS.

**Prompt Type:** Comprehensive (~370 lines)

## Context Gathering

1. What Compose version and features are used? (Material 3, adaptive layouts, animations)
2. Are custom Compose components involved? (custom layouts, drawing, gestures)
3. What state management approach is used? (ViewModel + StateFlow, remember, rememberSaveable)
4. Are there complex animations? (AnimatedVisibility, animateContentSize, Crossfade)
5. What navigation library is used? (Navigation Compose, Voyager, Decompose)
6. Are there any Compose-specific features with no SwiftUI analog? (custom Modifier chains, Layout composables)
7. What is the target iOS version? (iOS 16, 17, or 18 — affects available SwiftUI APIs)

## Instructions

### CRITICAL: Verification Requirements

- Every Compose → SwiftUI mapping MUST be tested against the target iOS version
- State management patterns MUST correctly handle SwiftUI's view invalidation model
- Side effect mappings MUST account for SwiftUI's different lifecycle semantics
- Layout translations MUST produce visually equivalent results on iOS

### False-Positive Prevention

- ❌ DO NOT translate `remember {}` to a local variable — it loses state across recompositions
- ✅ DO map `remember {}` to `@State` for view-local state
- ❌ DO NOT assume `LaunchedEffect` and `.task` have identical cancellation behavior
- ✅ DO note that `.task` cancels on view disappear, while `LaunchedEffect` cancels on key change
- ❌ DO NOT port Material 3 components directly — they look wrong on iOS
- ✅ DO use native iOS components (List, NavigationStack, TabView) with appropriate styling
- ❌ DO NOT assume Compose's single-pass layout maps to SwiftUI's layout system
- ✅ DO understand SwiftUI uses a proposal/response layout negotiation

### Step 1: Core Concept Mapping

| Compose | SwiftUI | Notes |
|---------|---------|-------|
| `@Composable fun` | `struct: View` | SwiftUI views are value types |
| `remember { }` | `@State` | View-local state |
| `rememberSaveable` | `@SceneStorage` or custom | Process death restoration |
| `collectAsState()` | `@Observable` / `@Published` | ViewModel observation |
| `Modifier` chain | ViewModifier / `.modifier()` | Different chaining model |
| `LaunchedEffect(key)` | `.task(id:)` | Async side effects |
| `DisposableEffect` | `.onAppear` / `.onDisappear` | Lifecycle callbacks |
| `derivedStateOf` | Computed property | Derived state |
| `snapshotFlow` | `onChange(of:)` | React to state changes |
| `CompositionLocal` | `@Environment` | Dependency propagation |

### Step 2: Composable Function → SwiftUI View

**Kotlin (Compose):**
```kotlin
@Composable
fun UserCard(
    user: User,
    onTap: () -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .fillMaxWidth()
            .padding(16.dp),
        onClick = onTap
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            AsyncImage(
                model = user.avatarUrl,
                contentDescription = "Avatar",
                modifier = Modifier
                    .size(48.dp)
                    .clip(CircleShape)
            )
            Spacer(modifier = Modifier.width(12.dp))
            Column {
                Text(
                    text = user.name,
                    style = MaterialTheme.typography.titleMedium
                )
                Text(
                    text = user.email,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
        }
    }
}
```

**Swift (SwiftUI):**
```swift
struct UserCard: View {
    let user: User
    let onTap: () -> Void

    var body: some View {
        Button(action: onTap) {
            HStack(spacing: 12) {
                AsyncImage(url: URL(string: user.avatarUrl)) { image in
                    image.resizable().scaledToFill()
                } placeholder: {
                    ProgressView()
                }
                .frame(width: 48, height: 48)
                .clipShape(Circle())

                VStack(alignment: .leading) {
                    Text(user.name)
                        .font(.headline)
                    Text(user.email)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }

                Spacer()
            }
            .padding()
        }
        .buttonStyle(.plain)
        .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 12))
        .padding(.horizontal)
    }
}
```

> **Key Difference:** Compose `Card` with `onClick` becomes a SwiftUI `Button` with custom styling. SwiftUI does not have a built-in Card component — use `.background` with materials instead.

### Step 3: State Management

**Kotlin (Compose state):**
```kotlin
@Composable
fun SearchScreen(viewModel: SearchViewModel = hiltViewModel()) {
    val state by viewModel.state.collectAsState()
    var query by remember { mutableStateOf("") }

    Column {
        TextField(
            value = query,
            onValueChange = { query = it },
            placeholder = { Text("Search...") }
        )

        LaunchedEffect(query) {
            delay(300) // Debounce
            viewModel.search(query)
        }

        when (val s = state) {
            is SearchState.Loading -> CircularProgressIndicator()
            is SearchState.Success -> LazyColumn {
                items(s.results) { item -> ResultRow(item) }
            }
            is SearchState.Error -> Text(s.message)
        }
    }
}
```

**Swift (SwiftUI state):**
```swift
struct SearchScreen: View {
    @State private var viewModel: SearchViewModel
    @State private var query = ""

    init(viewModel: SearchViewModel) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        VStack {
            TextField("Search...", text: $query)
                .textFieldStyle(.roundedBorder)
                .padding()

            switch viewModel.state {
            case .loading:
                ProgressView()
            case .success(let results):
                List(results) { item in
                    ResultRow(item: item)
                }
            case .error(let message):
                Text(message)
            }
        }
        .task(id: query) {
            try? await Task.sleep(for: .milliseconds(300)) // Debounce
            guard !Task.isCancelled else { return }
            await viewModel.search(query: query)
        }
    }
}
```

### Step 4: Side Effects Mapping

**Kotlin (Compose side effects):**
```kotlin
@Composable
fun PlayerScreen(videoId: String) {
    val context = LocalContext.current

    // One-time effect on composition
    LaunchedEffect(videoId) {
        analyticsTracker.trackVideoView(videoId)
    }

    // Cleanup on dispose
    DisposableEffect(Unit) {
        val player = ExoPlayer.Builder(context).build()
        onDispose { player.release() }
    }

    // React to state changes
    val playbackState by player.playbackStateFlow.collectAsState()
    LaunchedEffect(playbackState) {
        if (playbackState == PlaybackState.ENDED) {
            showCompletionDialog()
        }
    }
}
```

**Swift (SwiftUI side effects):**
```swift
struct PlayerScreen: View {
    let videoId: String
    @State private var player: AVPlayer?

    var body: some View {
        VideoPlayer(player: player)
            .task(id: videoId) {
                // Runs when videoId changes, cancels previous
                AnalyticsTracker.shared.trackVideoView(videoId)
            }
            .onAppear {
                player = AVPlayer(url: videoURL)
                player?.play()
            }
            .onDisappear {
                player?.pause()
                player = nil
            }
            .onChange(of: player?.currentItem?.status) { _, newValue in
                if newValue == .readyToPlay {
                    // React to state changes
                }
            }
    }
}
```

### Step 5: Modifier Translation

| Compose Modifier | SwiftUI Equivalent | Example |
|-----------------|-------------------|---------|
| `.fillMaxWidth()` | `.frame(maxWidth: .infinity)` | Full-width container |
| `.padding(16.dp)` | `.padding(16)` | Direct equivalent |
| `.clip(RoundedCornerShape(8.dp))` | `.clipShape(RoundedRectangle(cornerRadius: 8))` | Shape clipping |
| `.background(Color.Red)` | `.background(.red)` | Background color |
| `.clickable { }` | `.onTapGesture { }` or `Button` | Tap handling |
| `.verticalScroll()` | `ScrollView(.vertical)` | Scrollable container |
| `.weight(1f)` | `.frame(maxWidth: .infinity)` in HStack | Flexible space |
| `.shadow(elevation = 4.dp)` | `.shadow(radius: 4)` | Drop shadow |
| `.alpha(0.5f)` | `.opacity(0.5)` | Transparency |
| `.testTag("login")` | `.accessibilityIdentifier("login")` | Test identification |

### Step 6: List/LazyColumn Translation

**Kotlin (Compose LazyColumn):**
```kotlin
@Composable
fun FeedScreen(items: List<FeedItem>) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        item { HeaderSection() }
        items(items, key = { it.id }) { item ->
            FeedItemCard(item)
        }
        item { FooterSection() }
    }
}
```

**Swift (SwiftUI List):**
```swift
struct FeedScreen: View {
    let items: [FeedItem]

    var body: some View {
        List {
            Section { HeaderSection() }
            ForEach(items) { item in
                FeedItemCard(item: item)
            }
            Section { FooterSection() }
        }
        .listStyle(.plain)
        .contentMargins(16)
    }
}
```

## Expected Output

1. **Component mapping table** for all Compose components used in the app
2. **Screen-by-screen translation** with side-by-side Compose/SwiftUI code
3. **State management pattern** adapted for SwiftUI observation
4. **Custom component library** translating shared design system components

## Example Interaction

**User:** Translate our Compose home screen that has a top bar, a scrollable feed with pull-to-refresh, and a bottom navigation bar.

**Assistant:**

```
Compose                          SwiftUI
──────                           ───────
Scaffold(                        NavigationStack {
  topBar = TopAppBar()     →       .navigationTitle("Home")
  bottomBar = NavBar()     →       .toolbar { ... }
)                                }
                                 TabView {  // Bottom nav
PullToRefreshBox(          →       .refreshable {
  state = rememberPull...            await viewModel.refresh()
)                                  }

LazyColumn(                →     List {
  items(feed) { ... }              ForEach(feed) { ... }
)                                }
```

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Breaking UI migration into concepts, components, state, effects |
| **ST-02: Systematic Analysis Framework** | Exhaustive component mapping tables |
| **RT-02: Contextual Reference Integration** | Compose and SwiftUI API documentation |
| **DS-02: Output Specification Framework** | Screen translations and component library |

## Related Prompts

- `migration_material_to_hig.md` — Design system adaptation from Material to HIG
- `migration_navigation_patterns.md` — Navigation architecture translation
- `migration_architecture_adaptation.md` — ViewModel and state architecture
- `migration_coroutines_to_swift_concurrency.md` — Async patterns for side effects

## Customization Guide

- **UIKit Target:** If building for UIKit instead of SwiftUI, map Compose components to UIKit equivalents (UITableView, UICollectionView, UINavigationController).
- **Compose Multiplatform:** If using Compose Multiplatform on iOS, this migration is unnecessary — focus on platform integration points instead.
- **iOS 16 vs 17+:** Some SwiftUI APIs (Observable macro, contentMargins) require iOS 17+. Provide fallbacks for iOS 16 using ObservableObject.
- **Custom Design System:** If the app has a custom design system wrapping Material 3, create an equivalent Swift design system package.

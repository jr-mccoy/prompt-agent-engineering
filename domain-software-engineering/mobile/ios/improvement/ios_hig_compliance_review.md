---
title: "iOS HIG Compliance Review"
category: mobile-development
description: "Review an iOS app against Apple Human Interface Guidelines covering navigation patterns, typography system, iconography, interaction paradigms, and platform-specific design conventions"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: intermediate
tags:
  - ios
  - swift
  - hig
  - design
  - navigation
  - typography
updated: "2026-03-19"
---

# iOS HIG Compliance Review

**Objective:** Review an iOS app's design and implementation against Apple's Human Interface Guidelines (HIG), covering navigation patterns, the typography system, iconography, interaction paradigms, and platform-specific design conventions. Identify deviations that degrade user trust and native feel.

**When to Use:** Use this prompt before App Store submission to ensure guideline compliance, when the app feels "cross-platform" rather than native, when planning a design refresh to align with current iOS conventions, or when onboarding designers unfamiliar with Apple's design philosophy.

**Prompt Type:** Comprehensive (450-550 lines)

---

## Context Gathering

Before beginning the review, understand the app:

1. **App Context:**
   - "What type of app is this? (Utility, social, productivity, creative, e-commerce)"
   - "What is the primary user task flow?"
   - "Is this app also on Android/web, and is there a shared design system?"

2. **Design Decisions:**
   - "Is there a Figma/Sketch design file to compare against?"
   - "Are there intentional deviations from HIG? Which and why?"
   - "What iOS version visual style is the app targeting?"

3. **Platform Support:**
   - "Does the app support iPad? Mac Catalyst? Vision Pro?"
   - "What device sizes are supported?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Reference specific HIG sections** - Cite the guideline being violated, not general feelings.
2. **Check current HIG** - Apple updates guidelines; verify against the latest version.
3. **Respect intentional design choices** - Some deviations are deliberate and acceptable.
4. **Consider app category** - Games and creative apps have more design latitude.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding a HIG-COMPLIANT app is an acceptable outcome.** Many well-designed apps follow HIG naturally through use of system components.

### False-Positive Prevention

- ❌ Do NOT flag custom designs that are well-executed as "non-compliant"
- ❌ Do NOT require every app to look like Apple's first-party apps
- ❌ Do NOT flag branded colors as HIG violations
- ❌ Do NOT cite deprecated HIG sections (e.g., old navigation patterns)
- ✅ DO flag patterns that confuse users or break expectations
- ✅ DO check that system gestures are not intercepted
- ✅ DO verify standard controls behave as users expect
- ✅ DO ensure navigation patterns are consistent throughout the app

---

### Phase 1: Navigation Pattern Review

#### 1.1 Navigation Structure

```swift
// HIG VIOLATION: Hamburger menu instead of tab bar for primary navigation
class MainViewController: UIViewController {
    let menuButton = UIBarButtonItem(image: UIImage(systemName: "line.3.horizontal"), ...)
    // Side drawer menu for top-level destinations
}

// HIG COMPLIANT: Tab bar for primary navigation (up to 5 tabs)
struct MainView: View {
    var body: some View {
        TabView {
            HomeView()
                .tabItem { Label("Home", systemImage: "house") }
            SearchView()
                .tabItem { Label("Search", systemImage: "magnifyingglass") }
            ProfileView()
                .tabItem { Label("Profile", systemImage: "person") }
        }
    }
}
```

#### 1.2 Navigation Bar Usage

```swift
// HIG VIOLATION: Custom back button without chevron
navigationItem.leftBarButtonItem = UIBarButtonItem(
    title: "Go Back",
    style: .plain,
    target: self,
    action: #selector(goBack)
)

// HIG COMPLIANT: System back button with title
// Automatic when using UINavigationController or NavigationStack
// Customize only the back button title:
navigationItem.backButtonTitle = "Settings"
// Or hide the title:
navigationItem.backButtonDisplayMode = .minimal
```

#### 1.3 Modal Presentation

```swift
// HIG VIOLATION: Full-screen modal for simple content
struct DetailView: View {
    var body: some View {
        Text("Details here")
            .fullScreenCover(isPresented: $showDetail) {
                SimpleInfoView() // Does not warrant full screen
            }
    }
}

// HIG COMPLIANT: Sheet for focused tasks, full screen only for immersive content
struct DetailView: View {
    var body: some View {
        Text("Details here")
            .sheet(isPresented: $showDetail) {
                SimpleInfoView()
                    .presentationDetents([.medium, .large]) // Resizable sheet
                    .presentationDragIndicator(.visible)
            }
    }
}
```

---

### Phase 2: Typography System Review

#### 2.1 Text Style Usage

```swift
// HIG VIOLATION: Arbitrary font sizes without semantic meaning
Text("Section Title")
    .font(.system(size: 22, weight: .bold))
Text("Body content here")
    .font(.system(size: 15))
Text("Caption text")
    .font(.system(size: 11))

// HIG COMPLIANT: Semantic text styles
Text("Section Title")
    .font(.title2)
Text("Body content here")
    .font(.body)
Text("Caption text")
    .font(.caption)

// HIG text style hierarchy:
// .largeTitle  - 34pt - Screen titles (with large title nav)
// .title       - 28pt - Section headers
// .title2      - 22pt - Subsection headers
// .title3      - 20pt - Tertiary headers
// .headline    - 17pt semibold - Emphasized body text
// .body        - 17pt - Primary content
// .callout     - 16pt - Secondary content
// .subheadline - 15pt - Below headlines
// .footnote    - 13pt - Tertiary information
// .caption     - 12pt - Labels, timestamps
// .caption2    - 11pt - Smallest readable text
```

#### 2.2 Text Weight and Emphasis

```swift
// HIG VIOLATION: Over-bolding text
VStack {
    Text("Title").font(.headline).bold()     // Already semibold
    Text("Subtitle").font(.headline).bold()   // Everything looks the same
    Text("Content").font(.body).bold()        // Lost hierarchy
}

// HIG COMPLIANT: Clear visual hierarchy through font weight variation
VStack {
    Text("Title")
        .font(.title2.bold())      // Clearly the title
    Text("Subtitle")
        .font(.subheadline)        // Lighter weight, smaller
        .foregroundStyle(.secondary)
    Text("Content")
        .font(.body)               // Default weight for readability
}
```

---

### Phase 3: Iconography Review

#### 3.1 SF Symbols Usage

```swift
// HIG VIOLATION: Custom icons for standard actions
Image("custom_share_icon")    // Inconsistent with platform
Image("custom_settings_icon") // Users do not recognize it

// HIG COMPLIANT: SF Symbols for standard actions
Image(systemName: "square.and.arrow.up")  // Share
Image(systemName: "gearshape")             // Settings
Image(systemName: "trash")                 // Delete
Image(systemName: "plus")                  // Add/Create
Image(systemName: "pencil")                // Edit
Image(systemName: "magnifyingglass")       // Search

// SF Symbol rendering modes:
Image(systemName: "chart.bar.fill")
    .symbolRenderingMode(.hierarchical) // Depth through opacity layers
    .foregroundStyle(.blue)

Image(systemName: "person.crop.circle.badge.checkmark")
    .symbolRenderingMode(.palette)      // Multiple colors
    .foregroundStyle(.blue, .green)

Image(systemName: "heart.fill")
    .symbolRenderingMode(.monochrome)   // Single tint color
    .foregroundStyle(.red)
```

#### 3.2 Icon Sizing and Alignment

```swift
// HIG VIOLATION: Inconsistent icon sizes in toolbar
.toolbar {
    ToolbarItem {
        Button(action: {}) {
            Image(systemName: "bell")
                .font(.system(size: 24)) // Oversized
        }
    }
    ToolbarItem {
        Button(action: {}) {
            Image(systemName: "gear")
                .font(.system(size: 18)) // Different size
        }
    }
}

// HIG COMPLIANT: Consistent icon scaling
.toolbar {
    ToolbarItem {
        Button(action: {}) {
            Image(systemName: "bell")
            // System handles sizing for toolbar context
        }
    }
    ToolbarItem {
        Button(action: {}) {
            Image(systemName: "gear")
        }
    }
}
```

---

### Phase 4: Interaction Paradigm Review

#### 4.1 Destructive Actions

```swift
// HIG VIOLATION: Destructive action without confirmation
Button("Delete Account") {
    deleteAccount() // Immediate, irreversible action
}

// HIG COMPLIANT: Confirmation for destructive actions
Button("Delete Account", role: .destructive) {
    showDeleteConfirmation = true
}
.confirmationDialog(
    "Delete Account",
    isPresented: $showDeleteConfirmation,
    titleVisibility: .visible
) {
    Button("Delete Account", role: .destructive) {
        deleteAccount()
    }
} message: {
    Text("This will permanently delete your account and all data. This action cannot be undone.")
}
```

#### 4.2 Edit Mode Pattern

```swift
// HIG VIOLATION: Always-visible delete buttons on list items
List {
    ForEach(items) { item in
        HStack {
            Text(item.name)
            Spacer()
            Button { delete(item) } label: {
                Image(systemName: "trash")
                    .foregroundStyle(.red) // Cluttered, accident-prone
            }
        }
    }
}

// HIG COMPLIANT: Edit mode for batch operations
struct ItemListView: View {
    @State private var editMode: EditMode = .inactive

    var body: some View {
        List {
            ForEach(items) { item in
                Text(item.name)
            }
            .onDelete(perform: deleteItems)
            .onMove(perform: moveItems)
        }
        .environment(\.editMode, $editMode)
        .toolbar {
            EditButton()
        }
    }
}
```

#### 4.3 Form Input Patterns

```swift
// HIG VIOLATION: Custom picker instead of system picker
VStack {
    Text("Select Country")
    // Custom dropdown with non-standard behavior
    CustomDropdown(items: countries, selection: $selected)
}

// HIG COMPLIANT: System Picker
Form {
    Picker("Country", selection: $selectedCountry) {
        ForEach(countries) { country in
            Text(country.name).tag(country)
        }
    }
    // System decides presentation (inline, menu, navigation, wheel)
    // based on context and platform

    DatePicker("Birthday", selection: $birthday, displayedComponents: .date)
    // Uses system date picker with proper localization
}
```

---

### Phase 5: Platform Convention Compliance

#### 5.1 Settings Pattern

```swift
// HIG VIOLATION: In-app settings that duplicate system settings
struct AppSettingsView: View {
    var body: some View {
        Form {
            Toggle("Allow Notifications", isOn: $notifications) // Duplicates system
            Picker("Language", selection: $language) { ... }    // Should use system
        }
    }
}

// HIG COMPLIANT: Link to system settings for system-managed features
struct AppSettingsView: View {
    var body: some View {
        Form {
            Section("Notifications") {
                Button("Notification Settings") {
                    if let url = URL(string: UIApplication.openNotificationSettingsURLString) {
                        UIApplication.shared.open(url)
                    }
                }
            }
            Section("App Preferences") {
                // Only app-specific settings here
                Toggle("Show Previews", isOn: $showPreviews)
                Picker("Default View", selection: $defaultView) { ... }
            }
        }
    }
}
```

#### 5.2 Empty State Design

```swift
// HIG VIOLATION: Blank screen when no content
struct EmptyListView: View {
    var body: some View {
        List(items) { item in
            ItemRow(item: item)
        }
        // Shows blank white screen when items is empty
    }
}

// HIG COMPLIANT: Informative empty state with action
struct EmptyListView: View {
    var body: some View {
        if items.isEmpty {
            ContentUnavailableView {
                Label("No Items", systemImage: "tray")
            } description: {
                Text("Items you create will appear here.")
            } actions: {
                Button("Create Item") { showCreateSheet = true }
            }
        } else {
            List(items) { item in
                ItemRow(item: item)
            }
        }
    }
}
```

---

## Expected Output

1. **Navigation Audit** - Navigation pattern compliance with HIG recommendations
2. **Typography Report** - Text style usage and hierarchy assessment
3. **Iconography Audit** - Icon consistency and SF Symbol adoption
4. **Interaction Review** - Interaction patterns vs HIG standards
5. **Platform Compliance** - Adherence to iOS-specific conventions

---

## Example Interaction

**User provides an app with a custom tab bar and non-standard navigation:**

```swift
// BEFORE: CustomTabBar.swift
struct CustomTabBar: View {
    @Binding var selectedTab: Int

    var body: some View {
        HStack {
            ForEach(0..<4) { index in
                Button {
                    withAnimation { selectedTab = index }
                } label: {
                    VStack(spacing: 2) {
                        Image(tabIcons[index])
                            .resizable()
                            .frame(width: 30, height: 30)
                        Text(tabTitles[index])
                            .font(.system(size: 9))
                            .foregroundColor(selectedTab == index ? .blue : .gray)
                    }
                }
                .frame(maxWidth: .infinity)
            }
        }
        .padding(.vertical, 8)
        .background(Color.white)
        .shadow(radius: 2)
    }
}
```

**Agent produces:**

```swift
// AFTER: Using system TabView
struct MainView: View {
    @State private var selectedTab = 0

    var body: some View {
        TabView(selection: $selectedTab) {
            HomeView()
                .tabItem {
                    Label("Home", systemImage: "house")
                }
                .tag(0)

            SearchView()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }
                .tag(1)

            FavoritesView()
                .tabItem {
                    Label("Favorites", systemImage: "heart")
                }
                .tag(2)

            ProfileView()
                .tabItem {
                    Label("Profile", systemImage: "person")
                }
                .tag(3)
        }
    }
}
```

**HIG issues fixed:**
- Custom tab bar replaced with system TabView (proper haptics, accessibility, gestures)
- Custom PNG icons replaced with SF Symbols (consistent weight and scaling)
- Hardcoded font size `.system(size: 9)` replaced with system-managed label sizing
- White background with shadow replaced with system tab bar appearance (supports vibrancy, blur)
- System tab bar supports badge counts, long press, and accessibility automatically

---

## Techniques Used

- **ST-01** (Clear Objective): Focused HIG compliance review
- **RT-02** (Multi-Format Output): Code, guidelines references, and comparison tables
- **RT-04** (Best Practice Review): Apple HIG as authoritative reference
- **AG-02** (Iterative Refinement): Phase-by-phase review with prioritization

---

## Related Prompts

- [ios_ui_polish_audit.md](ios_ui_polish_audit.md) - Visual polish complements HIG compliance
- [ios_accessibility_improvement.md](ios_accessibility_improvement.md) - Accessibility is part of HIG
- [ios_user_experience_enhancement.md](ios_user_experience_enhancement.md) - UX patterns from HIG

---

## Customization Guide

### For iPad Apps

Additional HIG requirements:
- Sidebar navigation instead of tab bar
- Multi-column layout support
- Pointer/trackpad hover effects
- Keyboard shortcut support
- Split view and slide over support

### For Cross-Platform Design Systems

Focus on:
- Where platform conventions must override shared design
- Tab bar vs bottom navigation differences
- Back button and navigation conventions
- Typography mapping between platforms
- System components that should never be custom

### For Branded Apps

Balance branding with HIG:
- Custom colors are fine; custom navigation patterns are risky
- Branded fonts should still use Dynamic Type scaling
- App icon should follow SF Symbol weight for consistency
- Onboarding can be branded; core flows should feel native

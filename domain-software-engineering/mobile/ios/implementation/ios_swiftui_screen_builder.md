---
title: "iOS SwiftUI Screen Builder"
category: mobile-development
description: "Build production-ready SwiftUI views with proper state management, accessibility, Dynamic Type support, and Xcode previews following modern iOS UI patterns."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - ST-03
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - swiftui
  - accessibility
  - dynamic-type
  - mobile-development
updated: "2026-03-19"
---

# iOS SwiftUI Screen Builder

**Objective:** Build production-ready SwiftUI screens with proper @State, @Binding, @Observable state management, accessibility modifiers, Dynamic Type support, and Xcode previews following modern iOS UI patterns.

**When to Use:** Use this prompt when implementing new screens in a SwiftUI-based iOS app. Ideal for converting designs to code, building feature screens, or creating reusable UI components. Best used after navigation structure and data models are defined.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before building the screen, gather essential context:

1. **Design Specification:**
   - "Do you have design mockups or wireframes?"
   - "What standard iOS components does the screen use (List, Form, TabView, NavigationStack)?"
   - "Are there specific animations or transitions required?"

2. **Screen Requirements:**
   - "What states does the screen need (loading, content, error, empty)?"
   - "What user interactions are supported?"
   - "Does the screen need pull-to-refresh, pagination, or real-time updates?"

3. **Existing Patterns:**
   - "Are there existing SwiftUI views or components to reuse?"
   - "What design system or color/font tokens are in place?"
   - "Are there established patterns for common UI elements?"

4. **Data:**
   - "What data does this screen display?"
   - "Is there an @Observable model or ViewModel already defined?"
   - "How is navigation handled to/from this screen?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing SwiftUI patterns** - Check for existing views, design tokens, and state management patterns in the codebase.
2. **Verify design specifications** - Confirm UI requirements, interaction patterns, and accessibility needs before building.
3. **Follow project conventions** - Match existing view organization, naming, and styling patterns.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `Features/Home/HomeScreen.swift`) and be copy-paste ready.
5. **Include preview providers** - Provide `#Preview` macros for visual verification of all states.

**Adapting to existing SwiftUI patterns is preferred over introducing new approaches.** Match the project's existing style.

### False-Positive Prevention

- ❌ Do NOT introduce conflicting state management (e.g., don't add Combine if using @Observable)
- ❌ Do NOT hardcode colors/dimensions outside the asset catalog or design tokens
- ❌ Do NOT generate views without proper state ownership (@State at source, @Binding for children)
- ❌ Do NOT skip accessibility (accessibilityLabel, accessibilityHint, accessibilityValue)
- ❌ Do NOT use deprecated APIs (ObservableObject when @Observable is available on target)
- ✅ DO follow Apple Human Interface Guidelines where applicable
- ✅ DO provide proper performance optimization (lazy stacks, equatable conformance)
- ✅ DO include error and loading states
- ✅ DO specify exact file paths for all code changes
- ✅ DO support Dynamic Type and accessibility text sizes

---

### Phase 1: Screen Architecture

#### 1.1 Screen Structure Pattern

Follow this layered screen pattern:

```swift
// File: Features/Feature/FeatureScreen.swift

import SwiftUI

struct FeatureScreen: View {
    @State private var viewModel = FeatureViewModel()

    var body: some View {
        FeatureContent(viewModel: viewModel)
            .navigationTitle("Feature")
            .task {
                await viewModel.loadData()
            }
            .refreshable {
                await viewModel.refresh()
            }
    }
}

// MARK: - Content View (state-based switching)
private struct FeatureContent: View {
    @Bindable var viewModel: FeatureViewModel

    var body: some View {
        Group {
            switch viewModel.state {
            case .loading:
                LoadingView()
            case .empty:
                EmptyStateView(
                    title: "No Items",
                    message: "Add your first item to get started.",
                    systemImage: "tray",
                    action: ("Add Item", { viewModel.addItem() })
                )
            case .error(let message):
                ErrorStateView(
                    message: message,
                    retryAction: { Task { await viewModel.loadData() } }
                )
            case .loaded(let items):
                ItemListView(
                    items: items,
                    onSelect: { viewModel.select($0) },
                    onDelete: { viewModel.delete($0) }
                )
            }
        }
    }
}

#Preview("Loaded") {
    NavigationStack {
        FeatureScreen()
    }
}

#Preview("Empty") {
    NavigationStack {
        FeatureContent(viewModel: .preview(state: .empty))
    }
}
```

#### 1.2 Observable ViewModel

```swift
// File: Features/Feature/FeatureViewModel.swift

import SwiftUI

@Observable
final class FeatureViewModel {
    enum State: Equatable {
        case loading
        case loaded([Item])
        case empty
        case error(String)
    }

    private(set) var state: State = .loading
    var selectedItem: Item?

    private let repository: ItemRepositoryProtocol

    init(repository: ItemRepositoryProtocol = ItemRepository()) {
        self.repository = repository
    }

    func loadData() async {
        state = .loading
        do {
            let items = try await repository.fetchItems()
            state = items.isEmpty ? .empty : .loaded(items)
        } catch {
            state = .error(error.localizedDescription)
        }
    }

    func refresh() async {
        do {
            let items = try await repository.fetchItems()
            state = items.isEmpty ? .empty : .loaded(items)
        } catch {
            // Keep current data on refresh failure
        }
    }

    func select(_ item: Item) {
        selectedItem = item
    }

    func delete(_ item: Item) {
        guard case .loaded(var items) = state else { return }
        items.removeAll { $0.id == item.id }
        state = items.isEmpty ? .empty : .loaded(items)
    }

    func addItem() {
        // Navigate or present sheet
    }

    static func preview(state: State) -> FeatureViewModel {
        let vm = FeatureViewModel()
        vm.state = state
        return vm
    }
}
```

---

### Phase 2: Common Screen Patterns

**CHECKPOINT 1:** Confirm screen architecture before implementing patterns.

```markdown
## Screen Architecture Summary

### Screen Layers
| Layer | Responsibility |
|-------|---------------|
| FeatureScreen | Navigation, task lifecycle, refresh |
| FeatureContent | State-based UI switching |
| Child Views | Individual UI components |

### State Handling
| State | UI |
|-------|-----|
| .loading | ProgressView / Shimmer |
| .error | Error message + retry button |
| .empty | Illustration + CTA |
| .loaded | Main content |

**Proceed with content implementation?**
```

#### 2.1 List Screen Pattern

```swift
// File: Features/Feature/Views/ItemListView.swift

import SwiftUI

struct ItemListView: View {
    let items: [Item]
    let onSelect: (Item) -> Void
    let onDelete: (Item) -> Void

    var body: some View {
        List {
            ForEach(items) { item in
                ItemRow(item: item)
                    .contentShape(Rectangle())
                    .onTapGesture { onSelect(item) }
                    .accessibilityElement(children: .combine)
                    .accessibilityLabel("\(item.title), \(item.subtitle)")
                    .accessibilityHint("Double tap to view details")
                    .accessibilityAddTraits(.isButton)
            }
            .onDelete { indexSet in
                for index in indexSet {
                    onDelete(items[index])
                }
            }
        }
        .listStyle(.insetGrouped)
    }
}

struct ItemRow: View {
    let item: Item

    var body: some View {
        HStack(spacing: 12) {
            AsyncImage(url: item.imageURL) { phase in
                switch phase {
                case .success(let image):
                    image
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                case .failure:
                    Image(systemName: "photo")
                        .foregroundStyle(.secondary)
                default:
                    ProgressView()
                }
            }
            .frame(width: 60, height: 60)
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .accessibilityHidden(true)

            VStack(alignment: .leading, spacing: 4) {
                Text(item.title)
                    .font(.headline)
                    .lineLimit(2)

                Text(item.subtitle)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)

                Text(item.formattedDate)
                    .font(.caption)
                    .foregroundStyle(.tertiary)
            }

            Spacer()

            Image(systemName: "chevron.right")
                .font(.caption)
                .foregroundStyle(.tertiary)
                .accessibilityHidden(true)
        }
        .padding(.vertical, 4)
    }
}
```

#### 2.2 Detail Screen Pattern

```swift
// File: Features/Feature/Views/ItemDetailView.swift

import SwiftUI

struct ItemDetailView: View {
    let item: Item
    @State private var isSharePresented = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                // Hero image
                AsyncImage(url: item.imageURL) { phase in
                    switch phase {
                    case .success(let image):
                        image
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                    default:
                        Rectangle()
                            .fill(.quaternary)
                            .overlay { ProgressView() }
                    }
                }
                .frame(height: 250)
                .clipped()
                .accessibilityLabel("Image for \(item.title)")

                VStack(alignment: .leading, spacing: 12) {
                    Text(item.title)
                        .font(.title)
                        .fontWeight(.bold)

                    // Metadata
                    HStack(spacing: 16) {
                        Label(item.formattedDate, systemImage: "calendar")
                        Label(item.author, systemImage: "person")
                    }
                    .font(.subheadline)
                    .foregroundStyle(.secondary)

                    Divider()

                    Text(item.description)
                        .font(.body)
                        .lineSpacing(4)
                }
                .padding(.horizontal)
            }
        }
        .navigationTitle(item.title)
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                ShareLink(item: URL(string: item.shareURL)!) {
                    Image(systemName: "square.and.arrow.up")
                }
            }
        }
    }
}
```

#### 2.3 Form Screen Pattern

```swift
// File: Features/Feature/Views/ItemFormView.swift

import SwiftUI

struct ItemFormView: View {
    @Binding var title: String
    @Binding var description: String
    @Binding var category: Category
    @FocusState private var focusedField: Field?
    let onSubmit: () -> Void
    let isSubmitting: Bool

    enum Field: Hashable {
        case title, description
    }

    var canSubmit: Bool {
        !title.trimmingCharacters(in: .whitespaces).isEmpty
    }

    var body: some View {
        Form {
            Section("Details") {
                TextField("Title", text: $title)
                    .focused($focusedField, equals: .title)
                    .submitLabel(.next)
                    .onSubmit { focusedField = .description }
                    .accessibilityLabel("Item title")

                TextField("Description", text: $description, axis: .vertical)
                    .focused($focusedField, equals: .description)
                    .lineLimit(3...6)
                    .accessibilityLabel("Item description")
            }

            Section("Category") {
                Picker("Category", selection: $category) {
                    ForEach(Category.allCases) { cat in
                        Text(cat.displayName).tag(cat)
                    }
                }
            }

            Section {
                Button(action: onSubmit) {
                    if isSubmitting {
                        ProgressView()
                            .frame(maxWidth: .infinity)
                    } else {
                        Text("Save")
                            .frame(maxWidth: .infinity)
                    }
                }
                .disabled(!canSubmit || isSubmitting)
            }
        }
        .onAppear { focusedField = .title }
    }
}
```

---

### Phase 3: Reusable Components

#### 3.1 State Components

```swift
// File: Shared/Components/LoadingView.swift

import SwiftUI

struct LoadingView: View {
    var message: String = "Loading..."

    var body: some View {
        VStack(spacing: 16) {
            ProgressView()
                .controlSize(.large)
            Text(message)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .accessibilityElement(children: .combine)
        .accessibilityLabel("Loading content")
    }
}

// File: Shared/Components/ErrorStateView.swift

struct ErrorStateView: View {
    let message: String
    let retryAction: () -> Void

    var body: some View {
        ContentUnavailableView {
            Label("Something Went Wrong", systemImage: "exclamationmark.triangle")
        } description: {
            Text(message)
        } actions: {
            Button("Try Again", action: retryAction)
                .buttonStyle(.borderedProminent)
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("Error: \(message)")
        .accessibilityHint("Double tap the try again button to retry")
    }
}

// File: Shared/Components/EmptyStateView.swift

struct EmptyStateView: View {
    let title: String
    let message: String
    let systemImage: String
    var action: (String, () -> Void)? = nil

    var body: some View {
        ContentUnavailableView {
            Label(title, systemImage: systemImage)
        } description: {
            Text(message)
        } actions: {
            if let action {
                Button(action.0, action: action.1)
                    .buttonStyle(.borderedProminent)
            }
        }
    }
}
```

#### 3.2 Shimmer Loading

```swift
// File: Shared/Components/ShimmerView.swift

import SwiftUI

struct ShimmerModifier: ViewModifier {
    @State private var phase: CGFloat = 0

    func body(content: Content) -> some View {
        content
            .overlay(
                LinearGradient(
                    colors: [
                        .clear,
                        .white.opacity(0.4),
                        .clear
                    ],
                    startPoint: .leading,
                    endPoint: .trailing
                )
                .offset(x: phase)
            )
            .clipped()
            .onAppear {
                withAnimation(
                    .linear(duration: 1.5)
                    .repeatForever(autoreverses: false)
                ) {
                    phase = 300
                }
            }
    }
}

extension View {
    func shimmer() -> some View {
        modifier(ShimmerModifier())
    }
}

struct ShimmerRow: View {
    var body: some View {
        HStack(spacing: 12) {
            RoundedRectangle(cornerRadius: 8)
                .fill(.quaternary)
                .frame(width: 60, height: 60)
                .shimmer()

            VStack(alignment: .leading, spacing: 8) {
                RoundedRectangle(cornerRadius: 4)
                    .fill(.quaternary)
                    .frame(height: 16)
                    .frame(maxWidth: 200)
                    .shimmer()

                RoundedRectangle(cornerRadius: 4)
                    .fill(.quaternary)
                    .frame(height: 12)
                    .frame(maxWidth: 140)
                    .shimmer()
            }
        }
        .padding(.vertical, 4)
        .accessibilityHidden(true)
    }
}
```

---

### Phase 4: Accessibility & Dynamic Type

**CHECKPOINT 2:** Review components before adding accessibility polish.

```markdown
## Components Created

### Screen Components
| Component | Purpose |
|-----------|---------|
| FeatureScreen | Navigation, lifecycle |
| FeatureContent | State switching |
| ItemListView | List pattern |
| ItemDetailView | Detail pattern |
| ItemFormView | Form pattern |

### Reusable Components
| Component | Purpose |
|-----------|---------|
| LoadingView | Loading state |
| ErrorStateView | Error with retry |
| EmptyStateView | Empty state with CTA |
| ShimmerRow | Loading placeholder |

**Ready for accessibility and Dynamic Type polish?**
```

#### 4.1 Dynamic Type Support

```swift
// File: Shared/Modifiers/DynamicTypeModifiers.swift

import SwiftUI

extension View {
    /// Adjusts layout for large accessibility text sizes
    @ViewBuilder
    func adaptiveStack<Content: View>(
        spacing: CGFloat = 8,
        @ViewBuilder content: () -> Content
    ) -> some View {
        ViewThatFits {
            HStack(spacing: spacing) { content() }
            VStack(alignment: .leading, spacing: spacing) { content() }
        }
    }
}

// Usage in ItemRow:
struct AdaptiveItemRow: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize
    let item: Item

    var body: some View {
        if dynamicTypeSize.isAccessibilitySize {
            VStack(alignment: .leading, spacing: 8) {
                rowImage
                rowText
            }
        } else {
            HStack(spacing: 12) {
                rowImage
                rowText
            }
        }
    }

    private var rowImage: some View {
        AsyncImage(url: item.imageURL) { image in
            image.resizable().aspectRatio(contentMode: .fill)
        } placeholder: {
            Color.secondary.opacity(0.2)
        }
        .frame(width: 60, height: 60)
        .clipShape(RoundedRectangle(cornerRadius: 8))
        .accessibilityHidden(true)
    }

    private var rowText: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(item.title)
                .font(.headline)
            Text(item.subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }
}
```

---

## Expected Output

### File Structure

```
Features/Feature/
├── FeatureScreen.swift         # Screen entry point
├── FeatureViewModel.swift      # @Observable view model
└── Views/
    ├── ItemListView.swift      # List content
    ├── ItemDetailView.swift    # Detail content
    └── ItemFormView.swift      # Form content

Shared/Components/
├── LoadingView.swift
├── ErrorStateView.swift
├── EmptyStateView.swift
└── ShimmerView.swift

Shared/Modifiers/
└── DynamicTypeModifiers.swift
```

### Implementation Checklist

- [ ] Screen/Content layer separation
- [ ] State-based content switching (loading, loaded, empty, error)
- [ ] Loading state (shimmer or ProgressView)
- [ ] Error state with retry
- [ ] Empty state with CTA
- [ ] Pull-to-refresh (.refreshable)
- [ ] Pagination (if applicable)
- [ ] Accessibility: labels and hints
- [ ] Accessibility: combined elements
- [ ] Accessibility: minimum touch targets (44pt)
- [ ] Dynamic Type: adaptive layouts for accessibility sizes
- [ ] #Preview macros for all states

---

## Example Interaction

**User:** "Build a settings screen with user profile, notification preferences, and app info."

**Assistant:**
```swift
// File: Features/Settings/SettingsScreen.swift

import SwiftUI

struct SettingsScreen: View {
    @State private var viewModel = SettingsViewModel()

    var body: some View {
        Form {
            // Profile Section
            Section {
                NavigationLink {
                    ProfileEditView(profile: $viewModel.profile)
                } label: {
                    HStack(spacing: 12) {
                        AsyncImage(url: viewModel.profile.avatarURL) { image in
                            image.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: {
                            Image(systemName: "person.circle.fill")
                                .resizable()
                                .foregroundStyle(.secondary)
                        }
                        .frame(width: 60, height: 60)
                        .clipShape(Circle())

                        VStack(alignment: .leading) {
                            Text(viewModel.profile.displayName)
                                .font(.headline)
                            Text(viewModel.profile.email)
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                        }
                    }
                    .padding(.vertical, 4)
                }
                .accessibilityLabel("Edit profile, \(viewModel.profile.displayName)")
            }

            // Notifications
            Section("Notifications") {
                Toggle("Push Notifications", isOn: $viewModel.pushEnabled)
                Toggle("Email Notifications", isOn: $viewModel.emailEnabled)
                if viewModel.pushEnabled {
                    Picker("Frequency", selection: $viewModel.frequency) {
                        ForEach(NotificationFrequency.allCases) { freq in
                            Text(freq.displayName).tag(freq)
                        }
                    }
                }
            }

            // App Info
            Section("About") {
                LabeledContent("Version", value: viewModel.appVersion)
                Link("Privacy Policy", destination: URL(string: "https://example.com/privacy")!)
                Link("Terms of Service", destination: URL(string: "https://example.com/terms")!)
            }

            // Sign Out
            Section {
                Button("Sign Out", role: .destructive) {
                    viewModel.signOut()
                }
            }
        }
        .navigationTitle("Settings")
    }
}

#Preview {
    NavigationStack {
        SettingsScreen()
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for screen building
- **ST-02** (Sequential Instructions): Phased approach from architecture to accessibility
- **RT-02** (Multi-Dimensional Analysis): Covers structure, patterns, components, accessibility
- **RT-04** (Best Practice Review): SwiftUI and HIG best practices
- **ST-03** (Output Format Templates): Code templates for screen patterns
- **NE-02** (Phased Workflow): Clear phases with checkpoints

---

## Related Prompts

- [ios_state_management.md](ios_state_management.md) - Define state management for screens
- [ios_navigation_implementation.md](ios_navigation_implementation.md) - Connect screens with NavigationStack
- [ios_swiftui_state_patterns.md](ios_swiftui_state_patterns.md) - Advanced state ownership patterns
- [ios_dependency_injection.md](ios_dependency_injection.md) - Inject dependencies into view models

---

## Customization Guide

### For iPad Adaptive Layouts

Add multi-column support:
```swift
struct AdaptiveFeatureScreen: View {
    @Environment(\.horizontalSizeClass) var sizeClass

    var body: some View {
        if sizeClass == .regular {
            NavigationSplitView {
                SidebarList()
            } detail: {
                DetailView()
            }
        } else {
            NavigationStack {
                FeatureScreen()
            }
        }
    }
}
```

### For Design System Integration

Replace system styles with your tokens:
```swift
Text(item.title)
    .font(AppTheme.Fonts.headline)
    .foregroundStyle(AppTheme.Colors.textPrimary)
```

### For Animation-Heavy Screens

Add state transitions:
```swift
Group {
    switch viewModel.state {
    case .loading: LoadingView()
    case .loaded(let items): ItemListView(items: items)
    default: EmptyView()
    }
}
.animation(.easeInOut(duration: 0.3), value: viewModel.state)
```

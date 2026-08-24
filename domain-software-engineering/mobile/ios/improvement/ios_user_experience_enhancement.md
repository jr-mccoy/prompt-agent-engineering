---
title: "iOS User Experience Enhancement"
category: mobile-development
description: "Enhance iOS app UX with Apple HIG-aligned patterns including haptic feedback, context menus, swipe actions, pull-to-refresh, and platform-consistent interactions"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - DS-02
difficulty: intermediate
tags:
  - ios
  - swift
  - user-experience
  - haptics
  - context-menus
  - hig
updated: "2026-03-19"
---

# iOS User Experience Enhancement

**Objective:** Enhance an iOS app's user experience by implementing Apple Human Interface Guidelines patterns including haptic feedback, context menus, swipe actions, pull-to-refresh, and platform-consistent interaction paradigms that make the app feel native and delightful.

**When to Use:** Use this prompt when the app feels functional but lacks native iOS polish, when user feedback mentions the app does not "feel like an iPhone app," when adding missing platform-standard interactions, or when enhancing existing flows for higher user satisfaction.

**Prompt Type:** Comprehensive (450-550 lines)

---

## Context Gathering

Before enhancing UX, understand the current experience:

1. **Current Interactions:**
   - "What interaction patterns does the app currently use?"
   - "Are there haptics, context menus, or swipe actions?"
   - "What user feedback has been received about the experience?"

2. **App Type:**
   - "What kind of app is this? (Utility, social, productivity, creative, etc.)"
   - "What are the core user flows?"
   - "Is it primarily SwiftUI or UIKit?"

3. **Goals:**
   - "Are there specific interactions users expect but are missing?"
   - "Is there a competitive app that feels better? What do they do differently?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify the pattern fits the context** - Not every screen needs a context menu or haptics.
2. **Check Apple's current HIG** - Patterns evolve; confirm the recommendation is current.
3. **Consider the user flow** - Adding interactions should simplify, not complicate.
4. **Test discoverability** - Hidden gestures must have visible alternatives.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding a GOOD user experience is an acceptable outcome.** Not every app needs every iOS interaction pattern. Simplicity is often better than feature completeness.

### False-Positive Prevention

- ❌ Do NOT add haptics to every tap (overuse diminishes impact)
- ❌ Do NOT add context menus to elements without meaningful secondary actions
- ❌ Do NOT recommend swipe actions on non-list content
- ❌ Do NOT suggest interactions that conflict with system gestures
- ✅ DO recommend interactions that match user expectations for the app type
- ✅ DO consider whether the feature adds genuine value
- ✅ DO ensure new interactions have fallback for accessibility
- ✅ DO verify interactions work with one-handed use

---

### Phase 1: Haptic Feedback

#### 1.1 Meaningful Haptic Integration

```swift
// MISSING: Silent interactions lack physical feedback
struct ToggleRow: View {
    @Binding var isEnabled: Bool

    var body: some View {
        Toggle("Notifications", isOn: $isEnabled)
        // No haptic feedback when toggled
    }
}

// ENHANCED: Haptic confirmation
struct ToggleRow: View {
    @Binding var isEnabled: Bool

    var body: some View {
        Toggle("Notifications", isOn: $isEnabled)
            .sensoryFeedback(.selection, trigger: isEnabled)
    }
}

// UIKit haptic patterns:
class HapticManager {
    static let shared = HapticManager()

    private let impactLight = UIImpactFeedbackGenerator(style: .light)
    private let impactMedium = UIImpactFeedbackGenerator(style: .medium)
    private let notification = UINotificationFeedbackGenerator()
    private let selection = UISelectionFeedbackGenerator()

    func prepareImpact() { impactLight.prepare() }

    func tap() { impactLight.impactOccurred() }
    func success() { notification.notificationOccurred(.success) }
    func warning() { notification.notificationOccurred(.warning) }
    func error() { notification.notificationOccurred(.error) }
    func selection() { selection.selectionChanged() }
}
```

#### 1.2 Haptic Best Practices

```swift
// GOOD haptic usage - meaningful moments:
// - Toggle state changes → .selection
// - Successful action (save, send) → .success (notification)
// - Error or failure → .error (notification)
// - Pull-to-refresh threshold → .impact (medium)
// - Long press recognition → .impact (heavy)
// - Slider snapping to value → .selection

// BAD haptic usage - avoid:
// - Every button tap (over-stimulation)
// - During scrolling (annoying)
// - Keyboard typing (system handles this)
// - Background operations (unexpected)

// SwiftUI sensory feedback (iOS 17+):
Button("Save") { save() }
    .sensoryFeedback(.success, trigger: saveCompleted)

// Conditional haptics - respect user preference:
struct HapticButton: View {
    @AppStorage("hapticsEnabled") var hapticsEnabled = true

    var body: some View {
        Button("Action") { performAction() }
            .sensoryFeedback(hapticsEnabled ? .impact : .none, trigger: actionTrigger)
    }
}
```

---

### Phase 2: Context Menus

#### 2.1 List Item Context Menus

```swift
// MISSING: No secondary actions on list items
struct DocumentList: View {
    var body: some View {
        List(documents) { doc in
            DocumentRow(document: doc)
        }
    }
}

// ENHANCED: Rich context menu with preview
struct DocumentList: View {
    var body: some View {
        List(documents) { doc in
            DocumentRow(document: doc)
                .contextMenu {
                    Button {
                        share(doc)
                    } label: {
                        Label("Share", systemImage: "square.and.arrow.up")
                    }

                    Button {
                        duplicate(doc)
                    } label: {
                        Label("Duplicate", systemImage: "plus.square.on.square")
                    }

                    Button {
                        pin(doc)
                    } label: {
                        Label(doc.isPinned ? "Unpin" : "Pin",
                              systemImage: doc.isPinned ? "pin.slash" : "pin")
                    }

                    Divider()

                    Button(role: .destructive) {
                        delete(doc)
                    } label: {
                        Label("Delete", systemImage: "trash")
                    }
                } preview: {
                    DocumentPreview(document: doc)
                        .frame(width: 300, height: 400)
                }
        }
    }
}
```

#### 2.2 Image Context Menu

```swift
// Context menu with preview for images
struct PhotoGrid: View {
    var body: some View {
        LazyVGrid(columns: columns) {
            ForEach(photos) { photo in
                PhotoThumbnail(photo: photo)
                    .contextMenu {
                        Button {
                            saveToPhotos(photo)
                        } label: {
                            Label("Save to Photos", systemImage: "square.and.arrow.down")
                        }

                        Button {
                            setAsWallpaper(photo)
                        } label: {
                            Label("Use as Wallpaper", systemImage: "photo")
                        }

                        ShareLink(item: photo.url) {
                            Label("Share", systemImage: "square.and.arrow.up")
                        }
                    } preview: {
                        AsyncImage(url: photo.fullURL) { image in
                            image.resizable().aspectRatio(contentMode: .fit)
                        } placeholder: {
                            ProgressView()
                        }
                    }
            }
        }
    }
}
```

---

### Phase 3: Swipe Actions

#### 3.1 List Swipe Actions

```swift
// BASIC: Delete only
struct InboxView: View {
    var body: some View {
        List {
            ForEach(messages) { message in
                MessageRow(message: message)
            }
            .onDelete(perform: deleteMessages)
        }
    }
}

// ENHANCED: Leading and trailing swipe actions
struct InboxView: View {
    var body: some View {
        List {
            ForEach(messages) { message in
                MessageRow(message: message)
                    .swipeActions(edge: .trailing, allowsFullSwipe: true) {
                        Button(role: .destructive) {
                            delete(message)
                        } label: {
                            Label("Delete", systemImage: "trash")
                        }

                        Button {
                            archive(message)
                        } label: {
                            Label("Archive", systemImage: "archivebox")
                        }
                        .tint(.purple)
                    }
                    .swipeActions(edge: .leading, allowsFullSwipe: true) {
                        Button {
                            toggleRead(message)
                        } label: {
                            Label(
                                message.isRead ? "Unread" : "Read",
                                systemImage: message.isRead ? "envelope.badge" : "envelope.open"
                            )
                        }
                        .tint(.blue)

                        Button {
                            flag(message)
                        } label: {
                            Label("Flag", systemImage: "flag")
                        }
                        .tint(.orange)
                    }
            }
        }
    }
}
```

---

### Phase 4: Pull-to-Refresh

#### 4.1 Standard Pull-to-Refresh

```swift
// MISSING: Manual refresh button only
struct FeedView: View {
    var body: some View {
        List(posts) { post in
            PostRow(post: post)
        }
        .toolbar {
            Button("Refresh") { refresh() }
        }
    }
}

// ENHANCED: Native pull-to-refresh
struct FeedView: View {
    var body: some View {
        List(posts) { post in
            PostRow(post: post)
        }
        .refreshable {
            await loadNewPosts()
        }
        // Automatically shows spinner, haptic at threshold, and async completion
    }
}

// UIKit equivalent:
class FeedViewController: UITableViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        refreshControl = UIRefreshControl()
        refreshControl?.addTarget(self, action: #selector(handleRefresh), for: .valueChanged)
    }

    @objc private func handleRefresh() {
        Task {
            await loadNewPosts()
            refreshControl?.endRefreshing()
        }
    }
}
```

---

### Phase 5: Platform-Consistent Interactions

#### 5.1 Share Sheet Integration

```swift
// BASIC: Custom share implementation
Button("Share") {
    UIPasteboard.general.string = item.url.absoluteString
    showCopiedToast = true
}

// PLATFORM-NATIVE: ShareLink (iOS 16+)
ShareLink(item: item.url) {
    Label("Share", systemImage: "square.and.arrow.up")
}

// With custom preview:
ShareLink(
    item: item.url,
    subject: Text(item.title),
    message: Text(item.description),
    preview: SharePreview(item.title, image: item.thumbnailImage)
)
```

#### 5.2 Search Experience

```swift
// BASIC: Custom text field for search
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        VStack {
            TextField("Search...", text: $searchText)
                .textFieldStyle(.roundedBorder)
                .padding()
            List(filteredItems) { item in
                ItemRow(item: item)
            }
        }
    }
}

// PLATFORM-NATIVE: Searchable modifier
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            List(filteredItems) { item in
                ItemRow(item: item)
            }
            .searchable(text: $searchText, prompt: "Search items")
            .searchSuggestions {
                ForEach(suggestions) { suggestion in
                    Text(suggestion.text)
                        .searchCompletion(suggestion.text)
                }
            }
        }
    }
}
```

#### 5.3 Confirmation Dialogs

```swift
// NON-STANDARD: Custom alert for destructive actions
Button("Delete Account") {
    showingCustomAlert = true
}

// PLATFORM-NATIVE: Confirmation dialog
Button("Delete Account") {
    showingConfirmation = true
}
.confirmationDialog(
    "Are you sure?",
    isPresented: $showingConfirmation,
    titleVisibility: .visible
) {
    Button("Delete Account", role: .destructive) {
        deleteAccount()
    }
    Button("Cancel", role: .cancel) {}
} message: {
    Text("This will permanently delete your account and all associated data.")
}
```

---

## Expected Output

1. **Interaction Audit** - Missing platform-standard interactions
2. **Haptic Plan** - Where to add haptics and which patterns to use
3. **Context Menu Design** - Appropriate context menus for key elements
4. **Swipe Action Plan** - Swipe actions for list-based content
5. **Platform Pattern Adoption** - System APIs to replace custom implementations

---

## Example Interaction

**User provides a basic task list app:**

```swift
// BEFORE: TaskListView.swift
struct TaskListView: View {
    @State private var tasks: [Task] = []

    var body: some View {
        NavigationStack {
            List {
                ForEach(tasks) { task in
                    HStack {
                        Image(systemName: task.isComplete ? "checkmark.circle.fill" : "circle")
                            .onTapGesture { toggleComplete(task) }
                        Text(task.title)
                        Spacer()
                    }
                }
                .onDelete { indexSet in
                    tasks.remove(atOffsets: indexSet)
                }
            }
            .navigationTitle("Tasks")
        }
    }
}
```

**Agent produces:**

```swift
// AFTER: TaskListView.swift
struct TaskListView: View {
    @State private var tasks: [Task] = []
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            List {
                ForEach(filteredTasks) { task in
                    TaskRow(task: task, onToggle: { toggleComplete(task) })
                        .swipeActions(edge: .trailing, allowsFullSwipe: true) {
                            Button(role: .destructive) {
                                delete(task)
                            } label: {
                                Label("Delete", systemImage: "trash")
                            }
                        }
                        .swipeActions(edge: .leading, allowsFullSwipe: true) {
                            Button {
                                toggleComplete(task)
                            } label: {
                                Label(
                                    task.isComplete ? "Incomplete" : "Complete",
                                    systemImage: task.isComplete ? "arrow.uturn.backward" : "checkmark"
                                )
                            }
                            .tint(.green)
                        }
                        .contextMenu {
                            Button { edit(task) } label: {
                                Label("Edit", systemImage: "pencil")
                            }
                            Button { duplicate(task) } label: {
                                Label("Duplicate", systemImage: "plus.square.on.square")
                            }
                            Menu("Move to...") {
                                ForEach(lists) { list in
                                    Button(list.name) { move(task, to: list) }
                                }
                            }
                            Divider()
                            Button(role: .destructive) { delete(task) } label: {
                                Label("Delete", systemImage: "trash")
                            }
                        }
                }
            }
            .navigationTitle("Tasks")
            .searchable(text: $searchText, prompt: "Search tasks")
            .refreshable { await syncTasks() }
        }
    }
}

struct TaskRow: View {
    let task: Task
    let onToggle: () -> Void

    var body: some View {
        HStack {
            Button(action: onToggle) {
                Image(systemName: task.isComplete ? "checkmark.circle.fill" : "circle")
                    .foregroundStyle(task.isComplete ? .green : .secondary)
                    .imageScale(.large)
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.success, trigger: task.isComplete)

            Text(task.title)
                .strikethrough(task.isComplete)
                .foregroundStyle(task.isComplete ? .secondary : .primary)
            Spacer()
        }
        .contentShape(Rectangle())
    }
}
```

**Enhancements added:**
- Swipe-to-complete (leading) and swipe-to-delete (trailing)
- Context menu with edit, duplicate, move, and delete actions
- Pull-to-refresh for syncing
- Searchable list
- Haptic feedback on task completion
- Visual strikethrough for completed tasks
- Proper button styling for the toggle area

---

## Techniques Used

- **ST-01** (Clear Objective): Focused UX enhancement
- **RT-02** (Multi-Format Output): Code examples with interaction descriptions
- **RT-04** (Best Practice Review): Apple HIG interaction patterns
- **DS-02** (Decision Support): When to add vs skip interaction patterns

---

## Related Prompts

- [ios_hig_compliance_review.md](ios_hig_compliance_review.md) - Full HIG compliance audit
- [ios_ui_polish_audit.md](ios_ui_polish_audit.md) - Visual polish and animation quality
- [ios_accessibility_improvement.md](ios_accessibility_improvement.md) - Accessible interactions

---

## Customization Guide

### For Productivity Apps

Emphasize:
- Keyboard shortcuts for iPad and Mac Catalyst
- Drag and drop between lists/sections
- Quick actions from home screen (UIApplicationShortcutItem)
- Spotlight indexing (CoreSpotlight)
- Widget integration for quick actions

### For Social/Media Apps

Focus on:
- Double-tap to like with animation
- Long press for preview (context menus)
- Pinch-to-zoom for media
- Share sheet with rich previews
- Inline media playback controls

### For E-Commerce Apps

Prioritize:
- Swipe through product images
- Add-to-cart haptic confirmation
- Apple Pay integration
- Size/color picker interactions
- Wishlist swipe actions

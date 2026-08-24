---
title: "iOS SwiftUI Migration"
category: mobile-development
description: "Incrementally migrate UIKit to SwiftUI using UIHostingController wrapping, ViewController-to-View conversion, UIViewRepresentable bridges, and navigation architecture migration"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - swiftui
  - uikit
  - migration
  - uihostingcontroller
updated: "2026-03-19"
---

# iOS SwiftUI Migration

**Objective:** Incrementally migrate an existing UIKit codebase to SwiftUI using a bottom-up approach: wrapping SwiftUI views in UIHostingController for UIKit integration, converting ViewControllers to SwiftUI Views, building UIViewRepresentable bridges for UIKit components without SwiftUI equivalents, and migrating the navigation architecture.

**When to Use:** Use this prompt when starting a UIKit-to-SwiftUI migration, when building new features in SwiftUI within a UIKit app, when the team is ready to adopt SwiftUI incrementally, or when planning a migration roadmap. Not recommended for rewriting an entire app at once.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning migration, understand the landscape:

1. **Current Architecture:**
   - "What navigation pattern is used? (UINavigationController, coordinators, storyboard segues)"
   - "How many view controllers does the app have?"
   - "What UIKit features are heavily used? (table views, collection views, custom transitions)"

2. **Constraints:**
   - "What is the minimum deployment target? (SwiftUI availability varies by iOS version)"
   - "Are there custom UIKit views that have no SwiftUI equivalent?"
   - "Is there a timeline or deadline for migration?"

3. **Strategy:**
   - "Is this a gradual migration or a focused sprint?"
   - "Should new features be SwiftUI-first?"
   - "Are there screens that are good candidates for early migration?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify SwiftUI parity** - Confirm the SwiftUI replacement can do everything the UIKit version does.
2. **Check deployment target** - Many SwiftUI features require iOS 16+ or iOS 17+.
3. **Test interop behavior** - UIHostingController and UIViewRepresentable have edge cases.
4. **Validate navigation** - Mixed UIKit/SwiftUI navigation is the hardest part.
5. **Provide specific migration paths** - Every recommendation MUST include before/after code.

**Recommending NO migration is an acceptable outcome.** If the UIKit code is stable, well-tested, and the deployment target limits SwiftUI features, migration may not be worthwhile.

### False-Positive Prevention

- ❌ Do NOT recommend migrating screens that use UIKit features without SwiftUI equivalents
- ❌ Do NOT suggest full navigation rewrite as a first step
- ❌ Do NOT ignore deployment target constraints
- ❌ Do NOT underestimate the effort of migrating complex custom layouts
- ✅ DO start with simple, self-contained screens
- ✅ DO maintain UIKit navigation while migrating individual screens
- ✅ DO verify that data flow patterns work across the bridge
- ✅ DO test on the oldest supported iOS version

---

### Phase 1: SwiftUI in UIKit (Bottom-Up)

#### 1.1 Embedding SwiftUI Views in UIKit

```swift
// Step 1: Create a SwiftUI view for a new or simple screen
struct SettingsView: View {
    @ObservedObject var viewModel: SettingsViewModel

    var body: some View {
        Form {
            Section("Account") {
                LabeledContent("Email", value: viewModel.email)
                Button("Change Password") { viewModel.showChangePassword() }
            }
            Section("Preferences") {
                Toggle("Notifications", isOn: $viewModel.notificationsEnabled)
                Toggle("Dark Mode", isOn: $viewModel.darkModeEnabled)
            }
        }
    }
}

// Step 2: Wrap in UIHostingController for UIKit navigation
class SettingsHostingController: UIHostingController<SettingsView> {
    private let viewModel = SettingsViewModel()

    init() {
        let view = SettingsView(viewModel: viewModel)
        super.init(rootView: view)
        title = "Settings"
    }

    @available(*, unavailable)
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

// Step 3: Use in existing UIKit navigation
func showSettings() {
    let settingsVC = SettingsHostingController()
    navigationController?.pushViewController(settingsVC, animated: true)
}
```

#### 1.2 Passing Data Between UIKit and SwiftUI

```swift
// Using ObservableObject as a bridge
class ProfileViewModel: ObservableObject {
    @Published var name: String
    @Published var avatar: UIImage?

    // Callback to UIKit coordinator
    var onSave: ((Profile) -> Void)?
    var onCancel: (() -> Void)?

    init(profile: Profile) {
        self.name = profile.name
        self.avatar = profile.avatar
    }
}

struct ProfileEditView: View {
    @ObservedObject var viewModel: ProfileViewModel

    var body: some View {
        Form {
            TextField("Name", text: $viewModel.name)
            // ... other fields
        }
        .toolbar {
            ToolbarItem(placement: .cancellationAction) {
                Button("Cancel") { viewModel.onCancel?() }
            }
            ToolbarItem(placement: .confirmationAction) {
                Button("Save") {
                    viewModel.onSave?(viewModel.buildProfile())
                }
            }
        }
    }
}

// UIKit coordinator integration
class ProfileCoordinator {
    func showEditProfile(for profile: Profile) {
        let viewModel = ProfileViewModel(profile: profile)
        viewModel.onSave = { [weak self] updatedProfile in
            self?.saveProfile(updatedProfile)
            self?.navigationController.popViewController(animated: true)
        }
        viewModel.onCancel = { [weak self] in
            self?.navigationController.popViewController(animated: true)
        }

        let view = ProfileEditView(viewModel: viewModel)
        let hostingVC = UIHostingController(rootView: view)
        navigationController.pushViewController(hostingVC, animated: true)
    }
}
```

---

### Phase 2: UIKit in SwiftUI (Bridging)

#### 2.1 UIViewRepresentable for UIKit Components

```swift
// Wrap UIKit components that have no SwiftUI equivalent
struct MapView: UIViewRepresentable {
    @Binding var region: MKCoordinateRegion
    let annotations: [MKAnnotation]

    func makeUIView(context: Context) -> MKMapView {
        let mapView = MKMapView()
        mapView.delegate = context.coordinator
        return mapView
    }

    func updateUIView(_ mapView: MKMapView, context: Context) {
        mapView.setRegion(region, animated: true)

        // Only update annotations if they changed
        let currentIDs = Set(mapView.annotations.compactMap { ($0 as? IdentifiableAnnotation)?.id })
        let newIDs = Set(annotations.compactMap { ($0 as? IdentifiableAnnotation)?.id })

        if currentIDs != newIDs {
            mapView.removeAnnotations(mapView.annotations)
            mapView.addAnnotations(annotations)
        }
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

    class Coordinator: NSObject, MKMapViewDelegate {
        var parent: MapView

        init(_ parent: MapView) {
            self.parent = parent
        }

        func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool) {
            parent.region = mapView.region
        }
    }
}
```

#### 2.2 UIViewControllerRepresentable

```swift
// Wrap existing UIKit view controllers in SwiftUI
struct ImagePickerView: UIViewControllerRepresentable {
    @Binding var selectedImage: UIImage?
    @Environment(\.dismiss) var dismiss

    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController()
        picker.delegate = context.coordinator
        picker.sourceType = .photoLibrary
        return picker
    }

    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {}

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

    class Coordinator: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        let parent: ImagePickerView

        init(_ parent: ImagePickerView) {
            self.parent = parent
        }

        func imagePickerController(_ picker: UIImagePickerController,
                                   didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]) {
            parent.selectedImage = info[.originalImage] as? UIImage
            parent.dismiss()
        }

        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            parent.dismiss()
        }
    }
}

// Usage in SwiftUI:
struct AvatarEditor: View {
    @State private var showPicker = false
    @State private var image: UIImage?

    var body: some View {
        Button("Choose Photo") { showPicker = true }
            .sheet(isPresented: $showPicker) {
                ImagePickerView(selectedImage: $image)
            }
    }
}
```

---

### Phase 3: ViewController-to-View Conversion

#### 3.1 Simple ViewController Migration

```swift
// BEFORE: UIKit ProfileViewController
class ProfileViewController: UIViewController {
    private let nameLabel = UILabel()
    private let emailLabel = UILabel()
    private let avatarImageView = UIImageView()
    private var viewModel: ProfileViewModel

    init(viewModel: ProfileViewModel) {
        self.viewModel = viewModel
        super.init(nibName: nil, bundle: nil)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        bindViewModel()
    }

    private func setupUI() {
        // 50+ lines of Auto Layout constraints
        view.addSubview(avatarImageView)
        view.addSubview(nameLabel)
        view.addSubview(emailLabel)
        NSLayoutConstraint.activate([/* ... */])
    }

    private func bindViewModel() {
        viewModel.$name.assign(to: \.text, on: nameLabel).store(in: &cancellables)
        viewModel.$email.assign(to: \.text, on: emailLabel).store(in: &cancellables)
    }
}

// AFTER: SwiftUI ProfileView
struct ProfileView: View {
    @State var viewModel: ProfileViewModel

    var body: some View {
        VStack(spacing: 16) {
            AsyncImage(url: viewModel.avatarURL) { image in
                image.resizable()
                    .aspectRatio(contentMode: .fill)
            } placeholder: {
                Image(systemName: "person.circle.fill")
                    .resizable()
                    .foregroundStyle(.secondary)
            }
            .frame(width: 100, height: 100)
            .clipShape(Circle())

            Text(viewModel.name)
                .font(.title2.bold())

            Text(viewModel.email)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
    }
}
```

#### 3.2 TableViewController to List Migration

```swift
// BEFORE: UIKit UITableViewController with sections
class ContactsViewController: UITableViewController {
    var sections: [(title: String, contacts: [Contact])] = []

    override func numberOfSections(in tableView: UITableView) -> Int {
        sections.count
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        sections[section].contacts.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ContactCell", for: indexPath)
        let contact = sections[indexPath.section].contacts[indexPath.row]
        cell.textLabel?.text = contact.name
        cell.detailTextLabel?.text = contact.phone
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let contact = sections[indexPath.section].contacts[indexPath.row]
        showDetail(for: contact)
    }
}

// AFTER: SwiftUI List
struct ContactsView: View {
    let sections: [(title: String, contacts: [Contact])]
    @State private var selectedContact: Contact?

    var body: some View {
        List {
            ForEach(sections, id: \.title) { section in
                Section(section.title) {
                    ForEach(section.contacts) { contact in
                        NavigationLink(value: contact) {
                            VStack(alignment: .leading) {
                                Text(contact.name)
                                    .font(.body)
                                Text(contact.phone)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                }
            }
        }
        .navigationDestination(for: Contact.self) { contact in
            ContactDetailView(contact: contact)
        }
    }
}
```

---

### Phase 4: Navigation Architecture Migration

#### 4.1 Coordinator to NavigationStack

```swift
// BEFORE: UIKit Coordinator pattern
class AppCoordinator {
    let navigationController: UINavigationController

    func start() {
        let homeVC = HomeViewController()
        homeVC.delegate = self
        navigationController.setViewControllers([homeVC], animated: false)
    }

    func showDetail(_ item: Item) {
        let detailVC = DetailViewController(item: item)
        navigationController.pushViewController(detailVC, animated: true)
    }
}

// AFTER: SwiftUI NavigationStack with path
struct AppNavigationView: View {
    @State private var navigationPath = NavigationPath()

    var body: some View {
        NavigationStack(path: $navigationPath) {
            HomeView()
                .navigationDestination(for: Item.self) { item in
                    DetailView(item: item)
                }
                .navigationDestination(for: Category.self) { category in
                    CategoryView(category: category)
                }
        }
        .environment(\.navigate, NavigateAction { destination in
            navigationPath.append(destination)
        })
    }
}

// Custom navigation environment action
struct NavigateAction {
    let action: (any Hashable) -> Void
    func callAsFunction(_ destination: any Hashable) {
        action(destination)
    }
}

extension EnvironmentValues {
    @Entry var navigate = NavigateAction { _ in }
}
```

#### 4.2 Hybrid Navigation (Recommended Intermediate Step)

```swift
// Keep UIKit navigation, embed SwiftUI views
class MainNavigationController: UINavigationController {
    func pushSwiftUIView<V: View>(_ view: V, title: String? = nil) {
        let hostingVC = UIHostingController(rootView: view)
        hostingVC.title = title
        pushViewController(hostingVC, animated: true)
    }

    func presentSwiftUIView<V: View>(_ view: V, style: UIModalPresentationStyle = .automatic) {
        let hostingVC = UIHostingController(rootView: view)
        hostingVC.modalPresentationStyle = style
        present(hostingVC, animated: true)
    }
}

// Usage:
navigationController.pushSwiftUIView(
    SettingsView(viewModel: settingsVM),
    title: "Settings"
)
```

---

## Expected Output

1. **Migration Assessment** - Which screens to migrate and in what order
2. **Architecture Plan** - How UIKit and SwiftUI will coexist
3. **Bridge Components** - UIViewRepresentable wrappers needed
4. **Conversion Guide** - Before/after for each migrated screen
5. **Navigation Strategy** - How to handle mixed navigation

---

## Example Interaction

**User wants to add a new SwiftUI screen to their UIKit coordinator app:**

```swift
// BEFORE: Coordinator pushes UIKit VCs only
class HomeCoordinator: Coordinator {
    func showUserProfile(user: User) {
        let profileVC = ProfileViewController(user: user)
        profileVC.delegate = self
        navigationController.pushViewController(profileVC, animated: true)
    }
}
```

**Agent produces:**

```swift
// AFTER: Coordinator can push both UIKit and SwiftUI
class HomeCoordinator: Coordinator {
    // Existing UIKit flow (unchanged)
    func showUserProfile(user: User) {
        let profileVC = ProfileViewController(user: user)
        profileVC.delegate = self
        navigationController.pushViewController(profileVC, animated: true)
    }

    // New SwiftUI screen
    func showUserActivity(user: User) {
        let viewModel = UserActivityViewModel(user: user)
        viewModel.onDismiss = { [weak self] in
            self?.navigationController.popViewController(animated: true)
        }

        let activityView = UserActivityView(viewModel: viewModel)
        let hostingVC = UIHostingController(rootView: activityView)
        hostingVC.title = "Activity"
        navigationController.pushViewController(hostingVC, animated: true)
    }
}

// New SwiftUI view
struct UserActivityView: View {
    @ObservedObject var viewModel: UserActivityViewModel

    var body: some View {
        List(viewModel.activities) { activity in
            ActivityRow(activity: activity)
        }
        .refreshable { await viewModel.refresh() }
        .searchable(text: $viewModel.searchText)
    }
}
```

**Migration approach:** The coordinator remains UIKit-based. New screens are built in SwiftUI and wrapped in UIHostingController. This allows gradual migration without disrupting existing navigation.

---

## Techniques Used

- **ST-01** (Clear Objective): Focused migration objective
- **ST-02** (Sequential Instructions): Bottom-up migration phases
- **RT-02** (Multi-Format Output): Code examples with architecture diagrams
- **RT-04** (Best Practice Review): Apple migration best practices
- **NE-02** (Phased Workflow): Incremental migration with validation

---

## Related Prompts

- [ios_code_modernization.md](ios_code_modernization.md) - Modernize code alongside migration
- [ios_swift_concurrency_adoption.md](ios_swift_concurrency_adoption.md) - Adopt async/await during migration
- [ios_ui_polish_audit.md](ios_ui_polish_audit.md) - Polish migrated SwiftUI views

---

## Customization Guide

### For Apps with Storyboards

Additional steps:
- Extract storyboard VCs to programmatic initialization
- Convert IBOutlets to SwiftUI state
- Replace segues with NavigationStack destinations
- Migrate XIB-based cells to SwiftUI row views

### For Apps with Complex Custom Views

Focus on UIViewRepresentable:
- Wrap custom UIView subclasses
- Handle gesture recognizer bridging
- Bridge CALayer animations
- Manage UIKit delegate patterns in Coordinator

### For Apps Targeting iOS 15+

Limited SwiftUI features:
- Use NavigationView instead of NavigationStack
- No NavigationPath (use programmatic state)
- Limited searchable modifier capabilities
- No ShareLink (use UIActivityViewController wrapper)

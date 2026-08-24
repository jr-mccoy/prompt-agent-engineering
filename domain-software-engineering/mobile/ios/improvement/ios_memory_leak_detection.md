---
title: "iOS Memory Leak Detection"
category: mobile-development
description: "Detect and fix retain cycles in closures, delegate patterns, Combine subscriptions, notification observers, and timer references through static analysis patterns and Instruments profiling"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - memory-leaks
  - retain-cycles
  - instruments
  - combine
updated: "2026-03-19"
---

# iOS Memory Leak Detection

**Objective:** Systematically detect and fix memory leaks in an iOS codebase by identifying retain cycles in closures, delegate patterns, Combine subscriptions, notification observers, and timer references. Apply static analysis patterns and guide Instruments-based profiling to confirm fixes.

**When to Use:** Use this prompt when the app exhibits growing memory usage over time, when Xcode Memory Graph Debugger shows unexpected object retention, when users report the app being killed in the background, or during proactive code review to prevent memory issues before they reach production.

**Prompt Type:** Comprehensive (450-550 lines)

---

## Context Gathering

Before beginning leak detection, understand the scope:

1. **Symptoms:**
   - "Is the app experiencing memory warnings or background termination?"
   - "Have you identified specific screens or flows where memory grows?"
   - "Are there Xcode Memory Graph Debugger screenshots available?"

2. **Architecture:**
   - "What patterns are used for data flow? (Combine, closures, delegation, NotificationCenter)"
   - "Are coordinators, routers, or other navigation patterns in use?"
   - "Is the app primarily UIKit, SwiftUI, or a mix?"

3. **Known Issues:**
   - "Are there known areas with retain cycles or memory issues?"
   - "Have previous profiling sessions identified hotspots?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the full reference chain** - Do not flag `[weak self]` absence without confirming a retain cycle actually exists.
2. **Distinguish leaks from expected retention** - Long-lived singletons and caches are not leaks.
3. **Verify closure captures** - A closure capturing `self` is only a leak if `self` also holds a strong reference to the closure.
4. **Check lifecycle correctness** - Ensure the object in question should actually be deallocated at the reported point.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding NO leaks is an acceptable outcome.** Not every strong reference is a retain cycle. Do not manufacture leak findings.

### False-Positive Prevention

- ❌ Do NOT flag every `self` capture in a closure as a retain cycle
- ❌ Do NOT flag `Task { self.doSomething() }` as a leak (Task does not create retain cycles the same way)
- ❌ Do NOT flag singleton references as leaks
- ❌ Do NOT assume all `NotificationCenter.addObserver` calls leak (block-based API with `self` reference is the concern)
- ✅ DO trace the full ownership chain before reporting
- ✅ DO differentiate between `[weak self]` necessity and optional convenience
- ✅ DO verify that the captured object has a back-reference to the capturing context
- ✅ DO check if the closure/subscription has a finite lifetime

---

### Phase 1: Static Analysis - Closure Retain Cycles

#### 1.1 Escaping Closure Captures

**Scan for closures that capture self where self holds the closure:**

```swift
// LEAK: ViewController holds closure that captures self
class ProfileViewController: UIViewController {
    var onComplete: (() -> Void)?

    func setup() {
        // self -> onComplete -> self (retain cycle)
        onComplete = {
            self.dismiss(animated: true)
        }
    }
}

// FIX: Weak capture
func setup() {
    onComplete = { [weak self] in
        self?.dismiss(animated: true)
    }
}
```

#### 1.2 Nested Closure Captures

```swift
// LEAK: Nested closures compound the problem
class DataManager {
    var completionHandler: ((Result<Data, Error>) -> Void)?

    func fetchData() {
        // self -> completionHandler -> closure -> self
        completionHandler = { [weak self] result in
            switch result {
            case .success(let data):
                // Inner closure re-captures self strongly
                DispatchQueue.main.async {
                    self?.process(data) // OK: self is already weak
                }
            case .failure:
                break
            }
        }
    }
}
```

#### 1.3 Lazy Property Closures

```swift
// LEAK: lazy var with self capture
class SettingsViewController: UIViewController {
    // self -> formatter -> self (if formatter captures self)
    lazy var formatter: NumberFormatter = {
        let f = NumberFormatter()
        f.numberStyle = .currency
        f.locale = self.currentLocale // captures self strongly
        return f
    }()
}

// FIX: Avoid self capture or use [unowned self] (safe since lazy implies self exists)
lazy var formatter: NumberFormatter = { [unowned self] in
    let f = NumberFormatter()
    f.numberStyle = .currency
    f.locale = self.currentLocale
    return f
}()
```

---

### Phase 2: Static Analysis - Combine Subscriptions

#### 2.1 Sink Without Proper Storage

```swift
// LEAK: AnyCancellable not stored - subscription cancels immediately
// (Not a leak, but a bug)
class BadExample {
    func subscribe() {
        publisher.sink { value in } // Cancellable discarded
    }
}

// LEAK: Cancellable stored on self, closure captures self
class UserViewModel: ObservableObject {
    @Published var name = ""
    private var cancellables = Set<AnyCancellable>()

    func observe() {
        // self -> cancellables -> subscription -> closure -> self
        userService.namePublisher
            .sink { name in
                self.name = name // Strong capture of self
            }
            .store(in: &cancellables)
    }
}

// FIX: Weak capture in sink
func observe() {
    userService.namePublisher
        .sink { [weak self] name in
            self?.name = name
        }
        .store(in: &cancellables)
}

// BETTER: Use .assign with proper ownership
func observe() {
    userService.namePublisher
        .receive(on: DispatchQueue.main)
        .assign(to: &$name) // No cancellable needed, no retain cycle
}
```

#### 2.2 Combine + UIKit Lifecycle

```swift
// LEAK: Subscription outlives the view controller
class ListViewController: UIViewController {
    private var cancellables = Set<AnyCancellable>()

    override func viewDidLoad() {
        super.viewDidLoad()
        // If viewModel is a shared/singleton, this subscription
        // keeps ListViewController alive via closure capture
        viewModel.$items
            .sink { [weak self] items in
                self?.tableView.reloadData()
            }
            .store(in: &cancellables)
    }
}
// This is actually correct: cancellables are released when VC deallocates.
// Only a leak if something ELSE retains the VC.
```

---

### Phase 3: Static Analysis - Delegation and Notification Patterns

#### 3.1 Strong Delegate References

```swift
// LEAK: Strong delegate property
protocol DataServiceDelegate: AnyObject {
    func didReceiveData(_ data: Data)
}

class DataService {
    var delegate: DataServiceDelegate? // STRONG reference
    // If delegate holds DataService, this is a retain cycle
}

// FIX: Weak delegate
class DataService {
    weak var delegate: DataServiceDelegate?
}
```

#### 3.2 NotificationCenter Block-Based Observers

```swift
// LEAK: Block-based observer captures self, token stored on self
class DashboardViewController: UIViewController {
    private var observer: NSObjectProtocol?

    override func viewDidLoad() {
        super.viewDidLoad()
        // self -> observer token (implicitly) AND
        // NotificationCenter -> block -> self
        observer = NotificationCenter.default.addObserver(
            forName: .userDidLogin,
            object: nil,
            queue: .main
        ) { notification in
            self.refresh() // Strong capture
        }
    }

    deinit {
        // Never called because of retain cycle
        if let observer { NotificationCenter.default.removeObserver(observer) }
    }
}

// FIX: Weak capture
observer = NotificationCenter.default.addObserver(
    forName: .userDidLogin,
    object: nil,
    queue: .main
) { [weak self] notification in
    self?.refresh()
}
```

#### 3.3 Timer Retain Cycles

```swift
// LEAK: Timer retains its target
class PollingManager {
    private var timer: Timer?

    func startPolling() {
        // Timer strongly retains self as target
        timer = Timer.scheduledTimer(
            timeInterval: 30,
            target: self,
            selector: #selector(poll),
            userInfo: nil,
            repeats: true
        )
    }
}

// FIX: Use closure-based Timer with weak capture (iOS 10+)
func startPolling() {
    timer = Timer.scheduledTimer(withTimeInterval: 30, repeats: true) { [weak self] _ in
        self?.poll()
    }
}
```

---

### Phase 4: Instruments Profiling Guide

#### 4.1 Leaks Instrument

```
1. Open Instruments (Cmd+I from Xcode or Product > Profile)
2. Select "Leaks" template
3. Run the app and exercise suspect flows
4. Check for leak annotations (red diamonds)
5. Expand leak to see reference chain
6. Click "Cycles & Roots" to visualize retain cycles
```

#### 4.2 Memory Graph Debugger

```
1. Run app in Debug mode
2. Click "Debug Memory Graph" button in debug bar
3. Filter to your classes in the left panel
4. Look for objects with unexpected reference counts
5. Purple exclamation marks indicate runtime-detected leaks
6. Trace reference chains in the center panel
```

#### 4.3 Programmatic Leak Detection in Tests

```swift
// Add to unit tests to detect leaks
func assertDeallocated<T: AnyObject>(
    _ factory: () -> T,
    file: StaticString = #file,
    line: UInt = #line
) {
    weak var weakRef: T?
    autoreleasepool {
        let instance = factory()
        weakRef = instance
    }
    XCTAssertNil(weakRef, "Expected deallocation but object is still retained", file: file, line: line)
}

// Usage:
func testViewControllerDeallocates() {
    assertDeallocated {
        let vc = ProfileViewController()
        vc.loadViewIfNeeded()
        return vc
    }
}
```

---

## Expected Output

1. **Leak Inventory** - All potential retain cycles found with file:line locations and reference chain diagrams
2. **Severity Assessment** - Each leak rated by memory impact (bytes/objects retained) and user impact
3. **Fix Recommendations** - Specific code changes with before/after for each leak
4. **Instruments Guide** - Steps to verify fixes using Leaks instrument and Memory Graph Debugger
5. **Prevention Patterns** - Coding guidelines to prevent future leaks

---

## Example Interaction

**User provides a coordinator pattern with a memory leak:**

```swift
// BEFORE: AppCoordinator.swift
class AppCoordinator {
    var childCoordinators: [Coordinator] = []
    var navigationController: UINavigationController

    func showProfile() {
        let profileVC = ProfileViewController()
        profileVC.onDismiss = {
            self.childCoordinators.removeAll { $0 is ProfileCoordinator }
            self.navigationController.popViewController(animated: true)
        }
        navigationController.pushViewController(profileVC, animated: true)
    }
}

class ProfileViewController: UIViewController {
    var onDismiss: (() -> Void)?

    @objc func dismissTapped() {
        onDismiss?()
    }
}
```

**Agent produces:**

```swift
// AFTER: AppCoordinator.swift
class AppCoordinator {
    var childCoordinators: [Coordinator] = []
    var navigationController: UINavigationController

    func showProfile() {
        let profileVC = ProfileViewController()
        profileVC.onDismiss = { [weak self] in
            self?.childCoordinators.removeAll { $0 is ProfileCoordinator }
            self?.navigationController.popViewController(animated: true)
        }
        navigationController.pushViewController(profileVC, animated: true)
    }
}
```

**Leak analysis:**
- `AppCoordinator` -> `ProfileViewController` (via `navigationController` push)
- `ProfileViewController` -> `onDismiss` closure -> `AppCoordinator` (strong capture)
- Fix: `[weak self]` breaks the cycle. When the coordinator is released, the closure harmlessly becomes a no-op.

---

## Techniques Used

- **ST-01** (Clear Objective): Focused leak detection objective
- **RT-02** (Multi-Format Output): Code examples, reference chains, and profiling steps
- **RT-04** (Best Practice Review): Memory management best practices
- **AG-02** (Iterative Refinement): Progressive analysis from static to dynamic

---

## Related Prompts

- [ios_code_modernization.md](ios_code_modernization.md) - Modernize patterns that cause leaks
- [ios_swift_concurrency_adoption.md](ios_swift_concurrency_adoption.md) - Structured concurrency eliminates many retain cycles
- [ios_battery_energy_optimization.md](ios_battery_energy_optimization.md) - Memory leaks impact energy usage

---

## Customization Guide

### For SwiftUI-Only Apps

Focus on:
- `@StateObject` vs `@ObservedObject` lifetime
- Observation framework `@Observable` reference tracking
- `task {}` modifier cancellation verification
- Environment object retention chains

### For Combine-Heavy Codebases

Emphasize:
- `AnyCancellable` storage and lifecycle
- `sink` vs `assign(to:)` ownership semantics
- Subscription chains and intermediate operator retention
- `PassthroughSubject` / `CurrentValueSubject` subscriber retention

### For UIKit Navigation Patterns

Focus on:
- Coordinator pattern retain cycles
- Navigation controller child VC retention
- Presentation controller delegate cycles
- Custom transition animator references

### For Background Processing Apps

Additional checks:
- `URLSession` delegate retention
- Background task handler captures
- `OperationQueue` operation references
- Core Location manager delegate cycles

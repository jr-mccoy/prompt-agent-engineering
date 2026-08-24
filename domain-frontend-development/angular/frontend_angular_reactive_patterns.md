---
title: "Angular Reactive Patterns and Signals Analysis"
category: frontend-development/angular
description: "Analyze Angular applications for reactive programming patterns including Signals adoption, RxJS usage, state management, and migration from imperative to reactive approaches"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - angular
  - signals
  - rxjs
  - state-management
  - reactivity
  - ngrx
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/angular/frontend_angular_architecture.md
  - domain-frontend-development/angular/frontend_angular_testing.md
  - domain-frontend-development/react/frontend_react_state_management.md
  - domain-frontend-development/vue/frontend_vue_composition_api.md
---

# Angular Reactive Patterns and Signals Analysis

**Objective:** Analyze an Angular codebase for reactive programming patterns, evaluate RxJS usage health, assess Signals adoption readiness, and recommend a state management strategy that balances simplicity with scalability.

**When to Use:**
- Use when: Evaluating RxJS usage patterns and potential simplifications
- Use when: Planning migration to Angular Signals
- Use when: Choosing or auditing state management (NgRx, Signals, services)
- Use when: Debugging memory leaks or subscription management issues
- Don't use when: Working with AngularJS (different reactive model entirely)

## Instructions

1. **Audit RxJS Usage Patterns**
   - Identify subscription management approach:
     - Manual `subscribe()` + `unsubscribe()` in lifecycle hooks
     - `async` pipe in templates
     - `takeUntilDestroyed()` (Angular 16+) or `takeUntil(destroy$)` pattern
     - `DestroyRef` usage
   - Check for common RxJS anti-patterns:
     - Nested subscriptions
     - Missing error handling in streams
     - Over-complex operator chains where simpler alternatives exist
     - Subscription leaks (missing cleanup)
   - Evaluate operator usage: Are operators appropriate for the task?

2. **Assess Signals Adoption**
   - Current usage of `signal()`, `computed()`, `effect()`
   - Opportunities to replace simple BehaviorSubjects with Signals
   - `toSignal()` / `toObservable()` interop usage
   - Signal-based component inputs (`input()`, `input.required()`)
   - Signal-based queries (`viewChild()`, `contentChildren()`)
   - `model()` for two-way binding

3. **Evaluate State Management**
   - What state management solution(s) are in use?
     - Component-local state
     - Service-based state (BehaviorSubject pattern)
     - NgRx Store / ComponentStore
     - NGXS, Akita, Elf, or other libraries
     - Signals-based state
   - Is the solution appropriate for the application's complexity?
   - State normalization and selector efficiency
   - Side effect management (NgRx Effects, service methods)

4. **Review Async Data Flow**
   - HTTP call patterns (service layer, interceptors, caching)
   - Loading/error state management
   - Optimistic updates
   - Retry and error recovery strategies
   - Data refresh and polling patterns

5. **CRITICAL: Validate Findings**
   - Profile before claiming performance issues with RxJS
   - Verify subscription leaks with actual memory profiling
   - Consider team familiarity with Signals before recommending full migration
   - Check if RxJS complexity is justified by actual async requirements
   - **Confidence level** for each finding:
     - **High Confidence**: Memory leak or bug confirmed with evidence
     - **Medium Confidence**: Anti-pattern likely causing issues at scale
     - **Low Confidence**: Style improvement, needs team discussion

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag all `subscribe()` calls as wrong (some are appropriate in services)
- Suggest replacing all RxJS with Signals (complex async still needs RxJS)
- Report NgRx as "overkill" without understanding the app's state complexity
- Criticize BehaviorSubject services in small apps where they work well
- Flag `takeUntil` pattern as outdated if the app is below Angular 16
- Assume every Observable should be a Signal
- Report unused imports without checking if they're used in tests

**DO:**
- Distinguish between necessary RxJS complexity and accidental complexity
- Acknowledge that Signals complement RxJS rather than replace it
- Verify subscription leaks with actual evidence (memory profiling, DevTools)
- Consider the migration timeline when recommending Signals
- Evaluate state management in context of team size and app complexity
- Check if "anti-patterns" are documented workarounds for known Angular issues
- Recommend gradual adoption rather than big-bang rewrites

## Expected Output

A comprehensive reactive patterns analysis including:
- RxJS health assessment
- Signals adoption roadmap
- State management evaluation
- Subscription management audit
- Prioritized recommendations

### Output Format

```markdown
## Angular Reactive Patterns Analysis

### Reactive Strategy Overview
[Current approach and recommended direction]

### RxJS Health Assessment
[Subscription management, operator usage, anti-patterns]

### Signals Adoption Status
[Current usage and migration opportunities]

### State Management Evaluation
[Solution assessment and recommendations]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## Angular Reactive Patterns Analysis

### Executive Summary
The codebase relies heavily on RxJS with BehaviorSubject-based services for state management. Found 12 subscription leaks, 8 nested subscription anti-patterns, and significant opportunities to simplify with Signals. Recommend a phased approach: fix leaks immediately, adopt Signals for simple synchronous state, and keep RxJS for complex async flows.

### Reactive Strategy Overview

| Approach | Current Usage | Recommended |
|----------|--------------|-------------|
| Manual subscribe/unsubscribe | 45% | Eliminate |
| `async` pipe | 30% | Keep for Observable streams |
| `takeUntil(destroy$)` | 20% | Migrate to `takeUntilDestroyed()` |
| `takeUntilDestroyed()` | 5% | Adopt for remaining subscriptions |
| Signals | 0% | Adopt for synchronous state |

### RxJS Health Assessment

#### Issue 1: Subscription Leaks (Critical)
- **Severity:** Critical
- **Confidence:** High
- **Found:** 12 components with unmanaged subscriptions
- **Location:** `src/app/features/dashboard/widgets/*.component.ts`
- **Evidence:**
  ```typescript
  // dashboard-chart.component.ts - subscription never cleaned up
  @Component({ ... })
  export class DashboardChartComponent implements OnInit {
    data: ChartData[];

    ngOnInit() {
      // Subscription leaked - no unsubscribe on destroy
      this.analyticsService.getChartData().subscribe(data => {
        this.data = data;
      });

      // Another leak
      this.refreshService.onRefresh().subscribe(() => {
        this.loadData();
      });
    }
  }
  ```
- **Impact:** Memory leaks, stale callbacks executing after component destruction, potential errors
- **Fix:**
  ```typescript
  // Option A: takeUntilDestroyed (Angular 16+, preferred)
  @Component({ ... })
  export class DashboardChartComponent implements OnInit {
    private destroyRef = inject(DestroyRef);
    data: ChartData[];

    ngOnInit() {
      this.analyticsService.getChartData().pipe(
        takeUntilDestroyed(this.destroyRef)
      ).subscribe(data => {
        this.data = data;
      });
    }
  }

  // Option B: async pipe (best for template bindings)
  @Component({
    template: `
      @if (data$ | async; as data) {
        <app-chart [data]="data" />
      }
    `
  })
  export class DashboardChartComponent {
    data$ = this.analyticsService.getChartData();
  }

  // Option C: Signal with toSignal (Angular 16+)
  @Component({
    template: `
      @if (data(); as data) {
        <app-chart [data]="data" />
      }
    `
  })
  export class DashboardChartComponent {
    data = toSignal(this.analyticsService.getChartData());
  }
  ```

#### Issue 2: Nested Subscriptions (High)
- **Severity:** High
- **Confidence:** High
- **Found:** 8 instances across 5 files
- **Location:** `src/app/features/orders/order-detail.component.ts`
- **Evidence:**
  ```typescript
  // Nested subscriptions - callback hell with Observables
  loadOrder(id: string) {
    this.orderService.getOrder(id).subscribe(order => {
      this.order = order;

      // Nested subscription #1
      this.userService.getUser(order.userId).subscribe(user => {
        this.customer = user;

        // Nested subscription #2
        this.addressService.getAddress(user.addressId).subscribe(addr => {
          this.address = addr;
          this.loading = false;
        });
      });
    });
  }
  ```
- **Impact:** Lost error handling, impossible to cancel, memory leaks, race conditions
- **Fix:**
  ```typescript
  // Option A: switchMap chain (RxJS)
  loadOrder(id: string) {
    this.orderService.getOrder(id).pipe(
      switchMap(order => {
        this.order = order;
        return this.userService.getUser(order.userId);
      }),
      switchMap(user => {
        this.customer = user;
        return this.addressService.getAddress(user.addressId);
      }),
      takeUntilDestroyed(this.destroyRef),
    ).subscribe({
      next: address => {
        this.address = address;
        this.loading = false;
      },
      error: err => this.handleError(err),
    });
  }

  // Option B: forkJoin for parallel (if independent)
  loadOrderData(id: string) {
    this.orderService.getOrder(id).pipe(
      switchMap(order => forkJoin({
        order: of(order),
        customer: this.userService.getUser(order.userId),
        address: this.addressService.getAddress(order.userId),
      })),
      takeUntilDestroyed(this.destroyRef),
    ).subscribe({
      next: ({ order, customer, address }) => {
        this.order = order;
        this.customer = customer;
        this.address = address;
      },
      error: err => this.handleError(err),
    });
  }
  ```

#### Issue 3: BehaviorSubject Boilerplate (Medium)
- **Severity:** Medium
- **Confidence:** High
- **Found:** 15 services using identical BehaviorSubject pattern
- **Location:** `src/app/core/services/*.service.ts`
- **Evidence:**
  ```typescript
  // Repeated boilerplate across 15 services
  @Injectable({ providedIn: 'root' })
  export class CartService {
    private itemsSubject = new BehaviorSubject<CartItem[]>([]);
    items$ = this.itemsSubject.asObservable();

    private loadingSubject = new BehaviorSubject<boolean>(false);
    loading$ = this.loadingSubject.asObservable();

    private errorSubject = new BehaviorSubject<string | null>(null);
    error$ = this.errorSubject.asObservable();

    addItem(item: CartItem) {
      const current = this.itemsSubject.getValue();
      this.itemsSubject.next([...current, item]);
    }

    get itemCount(): number {
      return this.itemsSubject.getValue().length;
    }
  }
  ```
- **Impact:** Verbose, error-prone pattern repeated across services. `getValue()` breaks reactive chain.
- **Recommendation:** Migrate to Signals for synchronous state:
  ```typescript
  @Injectable({ providedIn: 'root' })
  export class CartService {
    // Clean, simple, reactive
    items = signal<CartItem[]>([]);
    loading = signal(false);
    error = signal<string | null>(null);

    // Derived state with computed
    itemCount = computed(() => this.items().length);
    total = computed(() =>
      this.items().reduce((sum, item) => sum + item.price * item.quantity, 0)
    );

    addItem(item: CartItem) {
      this.items.update(current => [...current, item]);
    }

    removeItem(id: string) {
      this.items.update(current => current.filter(i => i.id !== id));
    }
  }
  ```
- **Migration Effort:** Low per service (30 min each, 15 services = 1 week)

#### Issue 4: Missing Error Handling in Streams (Medium)
- **Severity:** Medium
- **Confidence:** High
- **Found:** 23 subscribe calls with no error callback
- **Evidence:**
  ```typescript
  // No error handling - errors silently swallowed
  this.productService.getProducts().subscribe(products => {
    this.products = products;
  });

  // Missing error in pipe
  this.orderService.getOrders().pipe(
    map(orders => orders.filter(o => o.status === 'active')),
  ).subscribe(orders => {
    this.activeOrders = orders;
  });
  ```
- **Fix:**
  ```typescript
  // Add error handling
  this.productService.getProducts().pipe(
    catchError(err => {
      this.errorService.handle(err);
      return of([]);  // fallback value
    }),
    takeUntilDestroyed(this.destroyRef),
  ).subscribe(products => {
    this.products = products;
  });

  // Or use a global error handler pattern
  this.productService.getProducts().pipe(
    this.errorService.handleError('Failed to load products', []),
    takeUntilDestroyed(this.destroyRef),
  ).subscribe(products => this.products = products);
  ```

### Signals Adoption Roadmap

**Phase 1: Quick Wins (Week 1-2)**
| Action | Files | Effort |
|--------|-------|--------|
| Replace BehaviorSubject in simple services | 8 services | 4 hours |
| Use `toSignal()` for HTTP calls in components | 15 components | 6 hours |
| Adopt `input()` / `output()` in new components | Ongoing | Incremental |

**Phase 2: State Migration (Week 3-4)**
| Action | Files | Effort |
|--------|-------|--------|
| Migrate CartService to Signals | 1 service + 6 consumers | 4 hours |
| Migrate UIStateService to Signals | 1 service + 12 consumers | 6 hours |
| Convert computed BehaviorSubjects to `computed()` | 20 instances | 8 hours |

**Phase 3: Keep RxJS Where Needed**
These should remain Observable-based:
- HTTP interceptors and retry logic
- WebSocket streams
- Complex event composition (debounce, throttle, merge)
- Multi-step async workflows with cancellation

### State Management Evaluation

**Current:** BehaviorSubject services (no NgRx)
**Assessment:** Appropriate for app complexity

| Criteria | Score | Notes |
|----------|-------|-------|
| Predictability | 6/10 | No enforced patterns, direct mutation possible |
| Debugging | 5/10 | No DevTools, manual logging |
| Boilerplate | 4/10 | High repetition across services |
| Performance | 7/10 | Acceptable, async pipe helps |
| Team familiarity | 8/10 | Team knows the pattern well |

**Recommendation:** Migrate to Signal-based services rather than introducing NgRx. The application's state complexity doesn't justify NgRx's ceremony, and Signals provide a cleaner upgrade path from BehaviorSubject services.

### Prioritized Recommendations

#### Critical (Fix This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix 12 subscription leaks | Memory leaks, bugs | 4 hours |
| 2 | Flatten 8 nested subscriptions | Bugs, error handling | 6 hours |
| 3 | Add error handling to 23 subscribe calls | Reliability | 4 hours |

#### High Priority (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Adopt `takeUntilDestroyed()` project-wide | Consistent cleanup | 4 hours |
| 2 | Migrate simple BehaviorSubject services to Signals | Less boilerplate | 1 week |
| 3 | Establish Signal-first convention for new code | Modernization | Ongoing |

#### Medium Priority (This Quarter)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Migrate remaining services to Signals | Consistency | 2 weeks |
| 2 | Add async pipe lint rule | Prevent leaks | 2 hours |
| 3 | Create shared error handling operators | DRY | 4 hours |

### Decision Guide: Signal vs Observable

| Use Case | Use Signal | Use Observable |
|----------|-----------|----------------|
| Component UI state | Yes | No |
| Simple service state | Yes | No |
| Derived/computed values | `computed()` | No |
| HTTP responses (one-shot) | `toSignal()` | Either |
| WebSocket streams | No | Yes |
| Complex event composition | No | Yes |
| Debounce/throttle | No | Yes |
| Multi-step async with cancellation | No | Yes |
| Route params/query params | `toSignal()` | Either |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on reactive patterns evaluation
- **ST-02 (Structured Sequential Instructions):** Systematic audit of reactive concerns
- **RT-02 (Multi-Dimensional Analysis):** Covers RxJS, Signals, state, and async patterns
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each issue
- **DS-06 (Prioritization Guidance):** Phased adoption roadmap

## Related Prompts

- [frontend_angular_architecture.md](frontend_angular_architecture.md) - Architecture-level analysis
- [frontend_angular_testing.md](frontend_angular_testing.md) - Testing reactive code
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - State management concepts in React
- [../vue/frontend_vue_composition_api.md](../vue/frontend_vue_composition_api.md) - Similar reactivity analysis in Vue

## Customization Guide

- **For Angular 14-15**: Skip Signals entirely; focus on RxJS cleanup and BehaviorSubject patterns
- **For Angular 16**: Introduce `toSignal()`/`toObservable()` interop, `takeUntilDestroyed()`
- **For Angular 17+**: Full Signals adoption including `input()`, `output()`, `model()`
- **For NgRx Codebases**: Evaluate NgRx SignalStore as Signals migration path
- **For Real-time Apps**: Emphasize WebSocket Observable patterns, keep RxJS for event streams

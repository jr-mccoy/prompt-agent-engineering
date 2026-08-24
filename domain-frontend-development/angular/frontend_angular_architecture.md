---
title: "Angular Application Architecture Analysis"
category: frontend-development/angular
description: "Analyze Angular codebases for architecture patterns including standalone components, module organization, dependency injection, and modern Angular best practices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - angular
  - architecture
  - standalone-components
  - dependency-injection
  - modules
  - signals
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/angular/frontend_angular_reactive_patterns.md
  - domain-frontend-development/angular/frontend_angular_testing.md
  - domain-frontend-development/react/frontend_react_component_patterns.md
---

# Angular Application Architecture Analysis

**Objective:** Analyze an Angular codebase for architecture patterns, component organization, dependency injection design, and adoption of modern Angular features, providing actionable recommendations for improved maintainability and performance.

**When to Use:**
- Use when: Reviewing existing Angular applications for architectural improvements
- Use when: Onboarding to a new Angular codebase and need to understand patterns
- Use when: Planning migration from NgModules to standalone components
- Use when: Evaluating dependency injection design and service architecture
- Don't use when: Building a greenfield Angular project (use creation prompts instead)

## Instructions

1. **Assess Angular Version and Feature Adoption**
   - Identify the Angular version in use (check `package.json`)
   - Determine which modern features are available vs adopted:
     - Standalone components (Angular 14+)
     - Signals (Angular 16+)
     - Control flow syntax `@if`, `@for`, `@switch` (Angular 17+)
     - Deferrable views `@defer` (Angular 17+)
     - Signal-based inputs/outputs (Angular 17.1+)
   - Check `angular.json` and `tsconfig.json` for configuration patterns

2. **Analyze Component Architecture**
   - **Module vs Standalone**: What percentage uses each approach?
   - **Component granularity**: Are components appropriately sized?
   - **Smart vs Presentational**: Is there separation of concerns?
   - **Component communication**: Input/Output, services, or direct access?
   - **Change detection strategy**: OnPush vs Default, and is it applied consistently?
   - **Template patterns**: Structural directives, pipes, template references

3. **Evaluate Dependency Injection Design**
   - Service scope: `providedIn: 'root'` vs module-level vs component-level
   - Injection token patterns: `InjectionToken` usage for configuration
   - Service layering: API → data → business → presentation
   - Circular dependency detection
   - Multi-provider patterns and factory usage

4. **Review Routing Architecture**
   - Lazy loading configuration and route organization
   - Guard implementation (functional guards in Angular 15+)
   - Resolver patterns and data pre-fetching
   - Route parameter handling
   - Nested routing and layout patterns

5. **CRITICAL: Verify findings before reporting**
   - Check if patterns have documented architectural decisions (ADRs)
   - Consider the Angular version constraints before suggesting features
   - Verify that "violations" aren't intentional design choices
   - Account for team size and migration timelines
   - **Confidence level** for each finding:
     - **High Confidence**: Pattern clearly violates Angular best practices with evidence
     - **Medium Confidence**: Suboptimal but may have context-specific reasons
     - **Low Confidence**: Style preference or needs more investigation

6. **Prioritize Recommendations**
   - Rank by impact on maintainability, testability, and performance
   - Separate quick wins from migration-scale efforts
   - Consider backward compatibility and team velocity impact

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag NgModules as "wrong" when the team hasn't migrated to standalone yet
- Report `*ngIf`/`*ngFor` as issues if the codebase isn't on Angular 17+
- Criticize Default change detection without profiling evidence of performance issues
- Flag `providedIn: 'root'` as wrong for genuinely app-wide singleton services
- Assume all shared modules need splitting without understanding usage patterns
- Report missing lazy loading for routes that are always needed at startup
- Flag barrel files (`index.ts`) as problematic without evidence of circular imports

**DO:**
- Check the Angular version before suggesting features
- Consider migration effort vs benefit for module-to-standalone transitions
- Verify that change detection suggestions are backed by profiling
- Evaluate DI patterns in context of the application's scale
- Acknowledge when current patterns are adequate for the team's needs
- Check if "violations" follow established Angular style guide variants
- Document trade-offs for each recommendation

## Expected Output

A comprehensive architecture analysis including:
- Angular version and feature adoption assessment
- Component organization overview
- Dependency injection architecture review
- Routing and lazy loading analysis
- Prioritized recommendations with migration effort estimates

### Output Format

```markdown
## Angular Architecture Analysis

### Executive Summary
[High-level assessment: 2-3 sentences on overall architecture quality]

### Version & Feature Adoption
**Angular Version**: [version]
**Feature Adoption:**
| Feature | Available | Adopted | Assessment |
|---------|-----------|---------|------------|
| Standalone Components | Yes/No | Yes/Partial/No | [Note] |
| Signals | Yes/No | Yes/Partial/No | [Note] |
| Control Flow | Yes/No | Yes/Partial/No | [Note] |

### Component Architecture
**Organization**: [Feature-based / Layer-based / Mixed]
**Module Strategy**: [Standalone / NgModule / Hybrid]

### Pattern Inventory
| Pattern | Usage | Assessment | Examples |
|---------|-------|------------|----------|
| [Pattern] | [%] | [Rating] | [Files] |

### Detailed Findings

#### Finding N: [Title]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** [File paths]
- **Evidence:** [Code examples]
- **Impact:** [What this affects]
- **Recommendation:** [Specific improvement]
- **Migration Effort:** Low | Medium | High

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|

#### Major Refactors (> 1 week each)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|

### Patterns to Preserve
[List well-implemented patterns that should be maintained]
```

## Example Output

```markdown
## Angular Architecture Analysis

### Executive Summary
The application is on Angular 17 but only partially leverages modern features. Component architecture is well-organized by feature, but 80% of the codebase still uses NgModules when standalone components are available. Dependency injection is well-structured with clear service layers, though several services have grown into "god services" handling too many concerns. Implementing standalone migration and splitting oversized services would significantly improve maintainability.

### Version & Feature Adoption

**Angular Version**: 17.3.2
**TypeScript Version**: 5.4.3

| Feature | Available | Adopted | Assessment |
|---------|-----------|---------|------------|
| Standalone Components | Yes | 20% (18/92 components) | Migration in progress |
| Signals | Yes | 5% (2 services) | Not yet adopted broadly |
| Control Flow (`@if`, `@for`) | Yes | 0% | Still using `*ngIf`, `*ngFor` |
| Deferrable Views (`@defer`) | Yes | 0% | Not adopted |
| Functional Guards | Yes | 30% (3/10 guards) | Partial migration |
| inject() function | Yes | 15% | Still mostly constructor injection |

### Component Architecture

**Organization**: Feature-based with shared module
**Module Strategy**: Hybrid (80% NgModule, 20% standalone)
**Change Detection**: Default everywhere (no OnPush)

**File Structure:**
```
src/app/
├── core/                    # Singleton services, guards, interceptors
│   ├── services/            # 12 services
│   ├── guards/              # 10 guards
│   └── interceptors/        # 3 interceptors
├── features/
│   ├── dashboard/           # Feature module
│   ├── products/            # Feature module
│   ├── orders/              # Feature module (standalone)
│   └── settings/            # Feature module
├── shared/
│   ├── components/          # 24 shared components
│   ├── directives/          # 8 directives
│   ├── pipes/               # 6 pipes
│   └── shared.module.ts     # Shared NgModule (imports everything)
└── app.module.ts
```

### Pattern Inventory

| Pattern | Usage | Assessment | Examples |
|---------|-------|------------|----------|
| Feature Modules | 75% | Good organization | `ProductsModule`, `DashboardModule` |
| Standalone Components | 20% | Started migration | `OrderListComponent`, `OrderDetailComponent` |
| Smart/Presentational Split | 40% | Inconsistent | `ProductListPage` (smart), `ProductCard` (presentational) |
| OnPush Change Detection | 0% | Missing | None |
| `providedIn: 'root'` | 90% | Overused for some services | All core services |
| Constructor DI | 85% | Legacy pattern | Most components and services |
| `inject()` function | 15% | Partial adoption | `OrderService`, `AuthGuard` |

### Detailed Findings

#### Finding 1: "God Service" Pattern in UserService
- **Severity:** High
- **Confidence:** High
- **Location:** `src/app/core/services/user.service.ts` (480 lines)
- **Evidence:**
  ```typescript
  @Injectable({ providedIn: 'root' })
  export class UserService {
    // Authentication (should be AuthService)
    login(credentials: LoginDto): Observable<AuthToken> { ... }
    logout(): void { ... }
    refreshToken(): Observable<AuthToken> { ... }

    // User profile (should be ProfileService)
    getProfile(): Observable<UserProfile> { ... }
    updateProfile(data: UpdateProfileDto): Observable<UserProfile> { ... }
    uploadAvatar(file: File): Observable<string> { ... }

    // Preferences (should be PreferencesService)
    getPreferences(): Observable<UserPreferences> { ... }
    updatePreferences(prefs: Partial<UserPreferences>): Observable<void> { ... }

    // Permissions (should be PermissionService)
    hasPermission(permission: string): boolean { ... }
    getUserRoles(): Observable<Role[]> { ... }
    checkAccess(resource: string): Observable<boolean> { ... }
  }
  ```
- **Impact:** Hard to test, violates SRP, creates tight coupling across features
- **Recommendation:** Split into focused services:
  ```typescript
  // auth.service.ts - Authentication only
  @Injectable({ providedIn: 'root' })
  export class AuthService {
    login(credentials: LoginDto): Observable<AuthToken> { ... }
    logout(): void { ... }
    refreshToken(): Observable<AuthToken> { ... }
  }

  // profile.service.ts - User profile management
  @Injectable({ providedIn: 'root' })
  export class ProfileService {
    private authService = inject(AuthService);
    getProfile(): Observable<UserProfile> { ... }
    updateProfile(data: UpdateProfileDto): Observable<UserProfile> { ... }
  }

  // permission.service.ts - Authorization
  @Injectable({ providedIn: 'root' })
  export class PermissionService {
    hasPermission(permission: string): boolean { ... }
    checkAccess(resource: string): Observable<boolean> { ... }
  }
  ```
- **Migration Effort:** Medium (1-2 weeks, update all injection points)

#### Finding 2: Shared Module Imports Everything
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/app/shared/shared.module.ts`
- **Evidence:**
  ```typescript
  @NgModule({
    declarations: [
      // All 24 components declared here
      ButtonComponent, ModalComponent, TableComponent,
      PaginationComponent, ToastComponent, LoaderComponent,
      // ... 18 more components
    ],
    imports: [CommonModule, FormsModule, ReactiveFormsModule],
    exports: [
      // Re-exports everything - even rarely used components
      ButtonComponent, ModalComponent, TableComponent,
      PaginationComponent, ToastComponent, LoaderComponent,
      // ... 18 more
      CommonModule, FormsModule, ReactiveFormsModule,
    ]
  })
  export class SharedModule {}
  ```
- **Impact:** Every feature importing SharedModule gets all 24 components in its chunk, even if only using 2-3
- **Recommendation:** Migrate shared components to standalone and import individually:
  ```typescript
  // Before: import entire shared module
  @NgModule({ imports: [SharedModule] })  // pulls in 24 components

  // After: import only what's needed
  @Component({
    standalone: true,
    imports: [ButtonComponent, TableComponent],  // only 2 components
  })
  export class ProductListComponent { ... }
  ```
- **Migration Effort:** Medium (1 week, component-by-component)

#### Finding 3: No OnPush Change Detection
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** All 92 components use Default change detection
- **Evidence:**
  ```typescript
  // Typical pattern - no changeDetection specified (defaults to Default)
  @Component({
    selector: 'app-product-card',
    templateUrl: './product-card.component.html',
  })
  export class ProductCardComponent {
    @Input() product: Product;
  }
  ```
- **Impact:** Every component re-checks bindings on every change detection cycle, even when inputs haven't changed
- **Recommendation:** Add OnPush to presentational components first:
  ```typescript
  @Component({
    selector: 'app-product-card',
    templateUrl: './product-card.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
  })
  export class ProductCardComponent {
    @Input() product: Product;
  }
  ```
  Note: Only add OnPush after verifying components use immutable data patterns or Observables with `async` pipe.
- **Migration Effort:** Medium (gradual, component-by-component)

#### Finding 4: Legacy Guard Patterns
- **Severity:** Low
- **Confidence:** High
- **Location:** `src/app/core/guards/`
- **Evidence:**
  ```typescript
  // Legacy class-based guard (deprecated in Angular 15.2+)
  @Injectable({ providedIn: 'root' })
  export class AuthGuard implements CanActivate {
    constructor(private authService: AuthService, private router: Router) {}

    canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
      return this.authService.isAuthenticated$.pipe(
        map(isAuth => {
          if (!isAuth) { this.router.navigate(['/login']); }
          return isAuth;
        })
      );
    }
  }
  ```
- **Recommendation:** Migrate to functional guards:
  ```typescript
  // Functional guard (Angular 15.2+)
  export const authGuard: CanActivateFn = (route) => {
    const authService = inject(AuthService);
    const router = inject(Router);

    return authService.isAuthenticated$.pipe(
      map(isAuth => isAuth || router.createUrlTree(['/login']))
    );
  };

  // Usage in routes
  { path: 'dashboard', component: DashboardComponent, canActivate: [authGuard] }
  ```
- **Migration Effort:** Low (1-2 days for 10 guards)

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Migrate 7 class guards to functional guards | Cleaner code, less boilerplate | 4-6 hours |
| 2 | Add OnPush to 24 shared presentational components | Performance improvement | 2-4 hours |
| 3 | Adopt `inject()` in new components/services | Modernization, less boilerplate | Ongoing |
| 4 | Enable strict template type checking in `tsconfig.json` | Catch template bugs | 1 hour |

#### Major Refactors (> 1 week each)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | Split UserService into focused services | Testability, SRP | 1-2 weeks | Update all injection points |
| 2 | Migrate SharedModule to standalone components | Bundle size reduction | 1-2 weeks | Component-by-component |
| 3 | Adopt Signals for state management | Performance, simplicity | 2-3 weeks | Requires OnPush first |
| 4 | Migrate templates to control flow syntax | Cleaner templates | 1 week | Angular 17+ confirmed |

### Patterns to Preserve
- **Feature-based folder structure**: Clear boundaries, easy navigation
- **Core module pattern**: Singleton services well-organized
- **Service layering**: API services separated from business logic
- **Typed forms**: Reactive forms with proper typing throughout
- **Route-level lazy loading**: Features load on demand correctly
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Angular architecture analysis
- **ST-02 (Structured Sequential Instructions):** Systematic review of architecture layers
- **RT-02 (Multi-Dimensional Analysis):** Covers components, DI, routing, and modern features
- **RT-05 (Evidence-Based Reasoning):** Code evidence required for each finding
- **DS-06 (Prioritization Guidance):** Impact/effort ranking for recommendations

## Related Prompts

- [frontend_angular_reactive_patterns.md](frontend_angular_reactive_patterns.md) - Signals and RxJS patterns
- [frontend_angular_testing.md](frontend_angular_testing.md) - Angular testing strategies
- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Similar analysis for React

## Customization Guide

- **For Angular 14-15**: De-emphasize Signals and control flow; focus on standalone migration
- **For Angular 16+**: Emphasize Signals adoption alongside standalone components
- **For Enterprise Apps**: Add focus on monorepo patterns (Nx), micro-frontend architecture
- **For Migration Projects (AngularJS)**: Focus on hybrid patterns and incremental migration
- **For Small Teams**: Prioritize quick wins over major refactors

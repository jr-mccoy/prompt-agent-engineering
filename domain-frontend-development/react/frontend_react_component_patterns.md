---
title: "React Component Architecture and Patterns"
category: frontend-development/react
description: "Analyze React codebases for component architecture patterns, composition strategies, and modern best practices including hooks, suspense, and server components"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - react
  - component-patterns
  - architecture
  - hooks
  - composition
  - server-components
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/react/frontend_react_hooks_best_practices.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/react/frontend_react_testing.md
---

# React Component Architecture and Patterns Analysis

**Objective:** Analyze a React codebase for component architecture patterns, identifying strengths, weaknesses, and opportunities to apply modern React patterns for improved maintainability, performance, and developer experience.

**When to Use:**
- Use when: Reviewing existing React applications for architectural improvements
- Use when: Onboarding to a new React codebase and need to understand patterns used
- Use when: Planning refactoring efforts to modernize React components
- Don't use when: Building a new application from scratch (use creation prompts instead)

## Instructions

1. **Identify Component Organization Patterns**
   - Locate component boundaries and folder structure
   - Identify presentational vs container component separation (if any)
   - Check for feature-based vs layer-based organization
   - Document naming conventions used

2. **Analyze Component Composition Patterns**
   For each significant component, evaluate:
   - **Composition Strategy**: How are child components composed?
   - **Props API**: Are props well-typed and minimal?
   - **Render Props/Children as Function**: Appropriately used?
   - **Higher-Order Components (HOCs)**: Legacy patterns vs modern alternatives?
   - **Compound Components**: Used for related component groups?

3. **Evaluate Hooks Usage Patterns**
   - Custom hooks: Are they properly abstracted and reusable?
   - Hook dependencies: Are dependency arrays correct?
   - Hook composition: Are hooks composed effectively?
   - Rules of hooks: Any violations?

4. **Check Modern React Patterns**
   - **Suspense**: Used for code-splitting and data fetching?
   - **Error Boundaries**: Present for graceful error handling?
   - **Lazy Loading**: Components lazily loaded where appropriate?
   - **Server Components** (if applicable): Proper server/client boundary?
   - **React.memo**: Applied judiciously for performance?

5. **CRITICAL: Verify findings before reporting**
   - Trace component usage across the codebase before flagging issues
   - Consider the application's constraints and requirements
   - Check if patterns that seem problematic have documented reasons
   - Verify that suggested improvements don't break existing functionality
   - **Confidence level** for each finding:
     - **High Confidence**: Pattern clearly violates React best practices with evidence
     - **Medium Confidence**: Pattern is suboptimal but may have context-specific reasons
     - **Low Confidence**: Potential improvement, needs more investigation

6. **Prioritize Recommendations**
   - Rank by impact on maintainability, performance, and DX
   - Consider migration effort vs benefit
   - Group quick wins separately from major refactors

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag class components as "bad" without understanding migration constraints
- Report HOCs as problematic when they solve composition issues hooks cannot
- Criticize prop drilling in small component trees where context would be overkill
- Flag missing React.memo without performance profiling evidence
- Assume large components need splitting without understanding cohesion
- Report "missing" Suspense without checking if the app supports it
- Flag custom hooks as "too simple" when they improve testability

✅ **DO:**
- Consider the React version in use and available features
- Evaluate patterns in context of team size and experience
- Check if "violations" are actually documented patterns for the project
- Verify that suggested hooks replacements maintain the same behavior
- Consider performance implications of suggested changes
- Document trade-offs for each recommendation
- Acknowledge when current patterns are "good enough"

## Expected Output

A comprehensive component architecture analysis including:
- Component organization overview
- Pattern inventory (what patterns are used where)
- Detailed findings with evidence and confidence levels
- Prioritized recommendations with migration effort estimates
- Quick wins vs major refactoring opportunities

### Output Format

```markdown
## React Component Architecture Analysis

### Executive Summary
[High-level assessment: 2-3 sentences on overall architecture quality]

### Component Organization
**Structure**: [Feature-based / Layer-based / Mixed / Flat]
**Naming Convention**: [PascalCase / kebab-case / etc.]
**Folder Pattern**: [Described pattern]

### Pattern Inventory

| Pattern | Usage | Assessment | Examples |
|---------|-------|------------|----------|
| Compound Components | 15% | Well applied | `<Tabs>`, `<Accordion>` |
| Custom Hooks | 40% | Good abstraction | `useAuth`, `useForm` |
| Container/Presentational | 20% | Legacy, consider migration | `UserContainer` |
| HOCs | 5% | Appropriate use | `withAuth` |

### Detailed Findings

#### Finding 1: [Pattern Name]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** [File paths]
- **Evidence:** [Specific code examples]
- **Impact:** [What this affects]
- **Recommendation:** [Specific improvement]
- **Migration Effort:** Low | Medium | High

[Additional findings...]

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | [Action] | [Impact] | Low |

#### Major Refactors (> 1 week each)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | [Action] | [Impact] | High | [What needs to happen first] |

### Patterns to Preserve
[List patterns that are working well and should be maintained]
```

## Example Output

```markdown
## React Component Architecture Analysis

### Executive Summary
The codebase demonstrates mature React patterns with good use of custom hooks and compound components. Primary opportunities exist in modernizing 15 legacy class components and improving code-splitting with Suspense boundaries. Overall architecture is maintainable with clear component boundaries.

### Component Organization
**Structure**: Feature-based with shared components
**Naming Convention**: PascalCase for components, camelCase for hooks
**Folder Pattern**: `features/{feature}/components/`, `shared/components/`

### Pattern Inventory

| Pattern | Usage | Assessment | Examples |
|---------|-------|------------|----------|
| Custom Hooks | 45% | Excellent abstraction | `useAuth`, `useForm`, `useApi` |
| Compound Components | 12% | Well applied | `<Tabs>`, `<Select>`, `<Modal>` |
| Render Props | 3% | Legacy, migrate to hooks | `<DataFetcher>` |
| Container/Presentational | 18% | Partially migrated | `UserContainer`, `OrderContainer` |
| HOCs | 8% | Appropriate where used | `withAuth`, `withTracking` |
| Class Components | 15% | Legacy, prioritize migration | `Dashboard`, `LegacyForm` |

### Detailed Findings

#### Finding 1: Class Components Still Present
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/features/dashboard/Dashboard.tsx`, `src/features/orders/OrderList.tsx`, +13 files
- **Evidence:**
  ```typescript
  // src/features/dashboard/Dashboard.tsx
  class Dashboard extends React.Component<Props, State> {
    state = { data: null, loading: true };

    componentDidMount() {
      this.fetchData();
    }
    // ...
  }
  ```
- **Impact:** Inconsistent patterns, harder to share logic, no hooks access
- **Recommendation:** Migrate to functional components with hooks. Start with simpler components, use `useEffect` for lifecycle methods.
- **Migration Effort:** Medium (15 components, ~2 weeks)

#### Finding 2: Missing Error Boundaries
- **Severity:** High
- **Confidence:** High
- **Location:** Application-wide
- **Evidence:** No `ErrorBoundary` components found. Errors in child components crash entire app.
- **Impact:** Poor user experience on runtime errors, no graceful degradation
- **Recommendation:** Add ErrorBoundary at route level and around critical feature areas:
  ```tsx
  // src/shared/components/ErrorBoundary.tsx
  class ErrorBoundary extends React.Component {
    state = { hasError: false };

    static getDerivedStateFromError(error) {
      return { hasError: true };
    }

    render() {
      if (this.state.hasError) {
        return <ErrorFallback onReset={() => this.setState({ hasError: false })} />;
      }
      return this.props.children;
    }
  }
  ```
- **Migration Effort:** Low (1-2 days)

#### Finding 3: Prop Drilling in User Context
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/features/*/components/*.tsx` (user prop passed 4+ levels deep)
- **Evidence:**
  ```tsx
  // Props chain: App → Layout → Header → UserMenu → UserAvatar
  <UserAvatar user={user} /> // user passed through 4 components
  ```
- **Impact:** Verbose props, harder to refactor, unnecessary re-renders
- **Recommendation:** Create UserContext for user data access:
  ```tsx
  const UserContext = React.createContext<User | null>(null);
  export const useUser = () => useContext(UserContext);
  ```
- **Migration Effort:** Low (4-6 hours)

#### Finding 4: Suspense Not Utilized for Code Splitting
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/App.tsx` routes
- **Evidence:**
  ```tsx
  // Current: All routes loaded eagerly
  import { Dashboard } from './features/dashboard';
  import { Orders } from './features/orders';
  import { Settings } from './features/settings';
  ```
- **Impact:** Larger initial bundle, slower first load
- **Recommendation:** Use React.lazy with Suspense:
  ```tsx
  const Dashboard = React.lazy(() => import('./features/dashboard'));
  const Orders = React.lazy(() => import('./features/orders'));

  <Suspense fallback={<PageSkeleton />}>
    <Routes>
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/orders" element={<Orders />} />
    </Routes>
  </Suspense>
  ```
- **Migration Effort:** Low (2-4 hours)

#### Finding 5: Custom Hooks Lack Memoization
- **Severity:** Low
- **Confidence:** Medium
- **Location:** `src/shared/hooks/useApi.ts`
- **Evidence:**
  ```tsx
  function useApi<T>(url: string) {
    const [data, setData] = useState<T | null>(null);

    // fetchFn recreated every render
    const fetchFn = async () => {
      const response = await fetch(url);
      setData(await response.json());
    };

    return { data, refetch: fetchFn };
  }
  ```
- **Impact:** Unnecessary re-creations, potential stale closures in effects
- **Recommendation:** Memoize with useCallback:
  ```tsx
  const fetchFn = useCallback(async () => {
    const response = await fetch(url);
    setData(await response.json());
  }, [url]);
  ```
- **Migration Effort:** Low (1-2 hours)

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Add ErrorBoundary at route level | High - prevents full crashes | 4 hours |
| 2 | Implement code splitting with Suspense | High - faster initial load | 3 hours |
| 3 | Create UserContext to eliminate prop drilling | Medium - cleaner code | 4 hours |
| 4 | Add useCallback to useApi hook | Low - better performance | 1 hour |

#### Major Refactors (> 1 week each)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | Migrate 15 class components to functions | Medium - consistency | 2 weeks | Testing coverage |
| 2 | Replace render props with hooks | Low - modernization | 1 week | Component migration |

### Patterns to Preserve
- **Custom hooks architecture**: Well abstracted, good separation of concerns
- **Compound components**: Excellent API design for complex UI components
- **Feature-based folder structure**: Clear boundaries, easy to navigate
- **TypeScript usage**: Strong typing throughout, minimal `any` usage
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with specific analysis goal
- **ST-02 (Structured Sequential Instructions):** Numbered steps for systematic review
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates patterns across multiple dimensions
- **RT-05 (Evidence-Based Reasoning):** Requires code evidence for each finding
- **DS-06 (Prioritization Guidance):** Ranks findings by impact and effort

## Related Prompts

- [frontend_react_hooks_best_practices.md](frontend_react_hooks_best_practices.md) - Deep dive on hook patterns
- [frontend_react_performance.md](frontend_react_performance.md) - Performance-focused analysis
- [frontend_react_testing.md](frontend_react_testing.md) - Testing patterns for React

## Customization Guide

- **For Next.js/Remix**: Add Server Components analysis, check for proper use of 'use client' directive
- **For React Native**: Focus on platform-specific patterns, navigation structure
- **For Legacy Codebases (React 16-)**: De-emphasize Suspense/Server Components, focus on hook migration
- **For New Projects**: Focus on pattern consistency rather than migration recommendations

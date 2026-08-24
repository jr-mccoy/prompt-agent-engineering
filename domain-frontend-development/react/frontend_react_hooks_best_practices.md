---
title: "React Hooks Best Practices Analysis"
category: frontend-development/react
description: "Analyze React hooks usage for correctness, performance, and maintainability including custom hook design, dependency management, and common pitfalls"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
difficulty: intermediate
tags:
  - react
  - hooks
  - useState
  - useEffect
  - custom-hooks
  - performance
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/react/frontend_react_component_patterns.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/testing/frontend_testing_jest.md
---

# React Hooks Best Practices Analysis

**Objective:** Analyze React hooks usage in a codebase to identify correctness issues, performance problems, and opportunities to improve custom hook design and reusability.

**When to Use:**
- Use when: Reviewing hook implementations for bugs or performance issues
- Use when: Auditing custom hooks for proper abstraction and reusability
- Use when: Debugging stale closure or infinite loop issues
- Use when: Establishing hooks standards for a team
- Don't use when: Evaluating overall component architecture (use component patterns prompt)

## Instructions

1. **Analyze Core Hooks Usage**
   For each usage of useState, useEffect, useContext, useRef, useMemo, useCallback:
   - Check for correct usage patterns
   - Identify potential bugs or anti-patterns
   - Verify dependency arrays are complete and correct

2. **Review useEffect Dependencies**
   - Check for missing dependencies (stale closures)
   - Check for over-specified dependencies (unnecessary re-runs)
   - Identify effects that should be split
   - Verify cleanup functions where needed

3. **Evaluate Custom Hook Design**
   - Are hooks following naming convention (use*)?
   - Is state properly encapsulated?
   - Are return values consistent and well-typed?
   - Could hooks be composed from smaller hooks?
   - Is the hook doing too much (violation of SRP)?

4. **Check for Performance Anti-Patterns**
   - Object/array references in dependency arrays
   - Missing useMemo for expensive computations
   - Missing useCallback for function props
   - State updates causing cascading re-renders

5. **Verify Rules of Hooks Compliance**
   - Only called at top level (not in conditions/loops)
   - Only called from React functions
   - Consistent call order

6. **CRITICAL: Validate Issues Before Reporting**
   - Test hypothesis with actual runtime behavior if possible
   - Check if ESLint react-hooks plugin already flags the issue
   - Verify that "stale closure" is actually causing bugs
   - Consider if over-optimization warnings are premature
   - **Confidence level** for each finding:
     - **High Confidence**: Clear violation with reproducible issue
     - **Medium Confidence**: Potential issue, context-dependent
     - **Low Confidence**: Style preference or theoretical concern

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag every function not wrapped in useCallback (only matters when passed as props to memoized children)
- Report "missing dependency" when the exclusion is intentional and documented
- Flag useMemo usage as "premature optimization" without profiling
- Assume all useEffects need cleanup (only side effects that persist)
- Report ref.current in dependencies (refs are stable)
- Flag empty dependency arrays without understanding the intent
- Criticize custom hooks for "doing too much" without usage context

✅ **DO:**
- Check if missing dependencies actually cause stale data bugs
- Verify that suggested memoization would improve measured performance
- Consider if the hook's API matches its consumers' needs
- Test edge cases (mount, unmount, dependency changes)
- Check if effects correctly handle race conditions
- Verify cleanup prevents memory leaks for subscriptions/listeners
- Consider React Strict Mode double-invocation behavior

## Expected Output

A comprehensive hooks analysis including:
- Summary of hooks usage patterns
- Critical bugs and correctness issues
- Performance optimization opportunities
- Custom hook design recommendations
- Prioritized action items

### Output Format

```markdown
## React Hooks Analysis Report

### Summary
[Overview of hooks usage and overall quality assessment]

### Hooks Inventory
| Hook Type | Count | Issues Found |
|-----------|-------|--------------|
| useState | X | Y |
| useEffect | X | Y |
| Custom hooks | X | Y |

### Critical Issues (Fix Immediately)

#### Issue 1: [Title]
- **Type:** Bug | Performance | Design
- **Severity:** Critical
- **Confidence:** High | Medium | Low
- **Location:** [File:Line]
- **Problem:** [Description]
- **Evidence:** [Code snippet]
- **Fix:** [Solution with code]

### Warnings (Review Soon)
[Medium severity issues]

### Suggestions (Consider)
[Low severity improvements]

### Custom Hooks Assessment
[Specific feedback on custom hooks]
```

## Example Output

```markdown
## React Hooks Analysis Report

### Summary
The codebase contains 156 hook usages across 45 components and 12 custom hooks. Overall quality is good with proper hook rules compliance. Found 3 critical stale closure bugs, 5 performance optimization opportunities, and 4 custom hook design improvements. The most impactful fixes are in the data fetching hooks.

### Hooks Inventory
| Hook Type | Count | Issues Found |
|-----------|-------|--------------|
| useState | 67 | 2 |
| useEffect | 42 | 5 |
| useCallback | 18 | 3 |
| useMemo | 8 | 1 |
| useContext | 12 | 0 |
| useRef | 9 | 1 |
| Custom hooks | 12 | 4 |

### Critical Issues (Fix Immediately)

#### Issue 1: Stale Closure in useEffect Callback
- **Type:** Bug
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/hooks/usePolling.ts:23`
- **Problem:** The polling callback captures stale `data` state, causing comparisons against outdated values.
- **Evidence:**
  ```typescript
  // ❌ Bug: data is stale inside interval callback
  function usePolling(url: string, interval: number) {
    const [data, setData] = useState(null);

    useEffect(() => {
      const id = setInterval(async () => {
        const newData = await fetch(url).then(r => r.json());
        // data here is always the initial value!
        if (JSON.stringify(newData) !== JSON.stringify(data)) {
          setData(newData);
        }
      }, interval);

      return () => clearInterval(id);
    }, [url, interval]); // Missing 'data' but adding it causes infinite loop

    return data;
  }
  ```
- **Fix:** Use functional update or useRef to access current state:
  ```typescript
  // ✅ Fix: Use ref to access current data without dependency
  function usePolling(url: string, interval: number) {
    const [data, setData] = useState(null);
    const dataRef = useRef(data);

    // Keep ref in sync
    useEffect(() => {
      dataRef.current = data;
    }, [data]);

    useEffect(() => {
      const id = setInterval(async () => {
        const newData = await fetch(url).then(r => r.json());
        if (JSON.stringify(newData) !== JSON.stringify(dataRef.current)) {
          setData(newData);
        }
      }, interval);

      return () => clearInterval(id);
    }, [url, interval]);

    return data;
  }
  ```

#### Issue 2: Race Condition in Data Fetching
- **Type:** Bug
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/hooks/useUser.ts:15`
- **Problem:** Fast navigation can cause stale data from slower request to overwrite newer data.
- **Evidence:**
  ```typescript
  // ❌ Bug: Race condition when userId changes quickly
  function useUser(userId: string) {
    const [user, setUser] = useState(null);

    useEffect(() => {
      fetchUser(userId).then(setUser);
    }, [userId]);

    return user;
  }
  ```
- **Fix:** Use cleanup function with cancelled flag or AbortController:
  ```typescript
  // ✅ Fix: Cancel stale requests
  function useUser(userId: string) {
    const [user, setUser] = useState(null);

    useEffect(() => {
      let cancelled = false;
      const controller = new AbortController();

      fetchUser(userId, { signal: controller.signal })
        .then(data => {
          if (!cancelled) setUser(data);
        })
        .catch(err => {
          if (err.name !== 'AbortError') throw err;
        });

      return () => {
        cancelled = true;
        controller.abort();
      };
    }, [userId]);

    return user;
  }
  ```

#### Issue 3: Missing Cleanup for Event Listener
- **Type:** Bug
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/components/ResizablePanel.tsx:34`
- **Problem:** Window resize listener is never removed, causing memory leak and stale component reference.
- **Evidence:**
  ```typescript
  // ❌ Bug: No cleanup, listener persists after unmount
  useEffect(() => {
    window.addEventListener('resize', handleResize);
  }, []);
  ```
- **Fix:** Return cleanup function:
  ```typescript
  // ✅ Fix: Clean up listener
  useEffect(() => {
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [handleResize]);
  ```

### Warnings (Review Soon)

#### Warning 1: Unnecessary Re-renders from Object Dependencies
- **Type:** Performance
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/components/DataTable.tsx:45`
- **Problem:** Config object created inline causes useEffect to run on every render.
- **Evidence:**
  ```typescript
  // ⚠️ Warning: New object reference every render
  useEffect(() => {
    fetchData(config);
  }, [{ page, pageSize, sortBy }]); // Object literal = new ref every time
  ```
- **Fix:** Use individual dependencies or useMemo:
  ```typescript
  // ✅ Fix: Individual dependencies
  useEffect(() => {
    fetchData({ page, pageSize, sortBy });
  }, [page, pageSize, sortBy]);
  ```

#### Warning 2: Expensive Computation Without Memoization
- **Type:** Performance
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/components/Analytics.tsx:28`
- **Problem:** Heavy data transformation runs on every render.
- **Evidence:**
  ```typescript
  // ⚠️ Warning: processLargeDataset called every render
  function Analytics({ data }) {
    const processed = processLargeDataset(data); // O(n²) operation
    return <Chart data={processed} />;
  }
  ```
- **Fix:** Memoize the computation:
  ```typescript
  // ✅ Fix: Only recompute when data changes
  function Analytics({ data }) {
    const processed = useMemo(() => processLargeDataset(data), [data]);
    return <Chart data={processed} />;
  }
  ```

#### Warning 3: Callback Not Memoized for Memoized Child
- **Type:** Performance
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/components/ProductList.tsx:52`
- **Problem:** Un-memoized callback breaks memo optimization of child component.
- **Evidence:**
  ```typescript
  // ⚠️ Warning: ProductCard is React.memo but receives new onClick every render
  function ProductList({ products }) {
    const handleClick = (id) => { /* ... */ }; // New function every render

    return products.map(p => (
      <ProductCard key={p.id} product={p} onClick={handleClick} />
    ));
  }
  ```
- **Fix:** Memoize the callback:
  ```typescript
  // ✅ Fix: Stable callback reference
  function ProductList({ products }) {
    const handleClick = useCallback((id) => { /* ... */ }, []);

    return products.map(p => (
      <ProductCard key={p.id} product={p} onClick={handleClick} />
    ));
  }
  ```

### Suggestions (Consider)

#### Suggestion 1: Split Large useEffect
- **Confidence:** Low
- **Location:** `src/hooks/useAnalytics.ts:20`
- **Current:** Single effect handles multiple unrelated side effects
- **Suggestion:** Split into separate effects for clarity and independent triggering

#### Suggestion 2: Extract Repeated Pattern to Custom Hook
- **Confidence:** Low
- **Location:** Multiple components
- **Pattern:** Loading/error/data state pattern repeated in 8 components
- **Suggestion:** Create `useAsyncState` or use established library (SWR, React Query)

### Custom Hooks Assessment

#### useAuth (src/hooks/useAuth.ts)
- **Quality:** Good
- **Observations:**
  - Well-typed return value
  - Proper encapsulation of auth state
  - Consider adding `isLoading` state for initial auth check

#### useForm (src/hooks/useForm.ts)
- **Quality:** Good with improvements needed
- **Observations:**
  - Handles validation well
  - Missing: Field-level touched state
  - Consider: Debounced validation option
  - Return value could use `register` pattern like React Hook Form

#### useLocalStorage (src/hooks/useLocalStorage.ts)
- **Quality:** Needs improvement
- **Issues:**
  - Missing SSR safety check (window undefined)
  - No error handling for quota exceeded
  - Consider adding serialization options
- **Suggested fix:**
  ```typescript
  function useLocalStorage<T>(key: string, initialValue: T) {
    const [value, setValue] = useState<T>(() => {
      if (typeof window === 'undefined') return initialValue;
      try {
        const item = window.localStorage.getItem(key);
        return item ? JSON.parse(item) : initialValue;
      } catch {
        return initialValue;
      }
    });

    const setStoredValue = useCallback((newValue: T | ((val: T) => T)) => {
      try {
        const valueToStore = newValue instanceof Function ? newValue(value) : newValue;
        setValue(valueToStore);
        if (typeof window !== 'undefined') {
          window.localStorage.setItem(key, JSON.stringify(valueToStore));
        }
      } catch (error) {
        console.warn(`Error setting localStorage key "${key}":`, error);
      }
    }, [key, value]);

    return [value, setStoredValue] as const;
  }
  ```

### Prioritized Actions

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 1 | Fix stale closure in usePolling | Critical - causes bugs | 30 min |
| 2 | Add race condition handling to useUser | Critical - causes bugs | 30 min |
| 3 | Add cleanup to ResizablePanel listener | Critical - memory leak | 10 min |
| 4 | Improve useLocalStorage SSR safety | Medium - prevents SSR crash | 20 min |
| 5 | Add useMemo to Analytics processing | Medium - performance | 10 min |
| 6 | Memoize ProductList callbacks | Medium - performance | 15 min |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused goal on hooks analysis
- **ST-02 (Structured Sequential Instructions):** Systematic hook review process
- **RT-02 (Multi-Dimensional Analysis):** Evaluates correctness, performance, and design
- **RT-05 (Evidence-Based Reasoning):** Code examples required for each finding
- **QA-02 (Adversarial Stress-Test):** Edge cases and race conditions

## Related Prompts

- [frontend_react_component_patterns.md](frontend_react_component_patterns.md) - Overall component architecture
- [frontend_react_performance.md](frontend_react_performance.md) - Performance-specific analysis
- [frontend_testing_jest.md](../testing/frontend_testing_jest.md) - Testing hooks

## Customization Guide

- **For React 18+**: Include useSyncExternalStore, useId, useTransition analysis
- **For React Native**: Consider platform-specific hooks (useWindowDimensions, etc.)
- **For Server Components**: Focus on client/server boundary hooks usage
- **For Legacy Class Migration**: Identify class lifecycle → hooks equivalents

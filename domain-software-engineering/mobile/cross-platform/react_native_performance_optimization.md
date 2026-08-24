---
title: "React Native Performance Optimization"
category: mobile-development
description: "Identifies performance bottlenecks in React Native apps including re-renders, JavaScript thread blocking, and bridge communication overhead"
tags:
  - mobile-development
  - optimization
  - performance
updated: "2026-03-19"
---

# React Native Performance Optimization

**Objective:** Analyze React Native applications to identify performance bottlenecks, unnecessary re-renders, JavaScript thread blocking, bridge communication overhead, and provide actionable optimization recommendations.

**When to Use:** Use this prompt when experiencing performance issues in React Native apps (slow rendering, janky animations, slow navigation), during performance audits, before major releases, or when optimizing user experience.

**Instructions:**

1. **Performance Profiling Setup:**
   * Review if performance monitoring is enabled (Flipper, React DevTools Profiler)
   * Check for existing performance metrics collection
   * Identify performance measurement tools in use
   * Recommend adding missing profiling capabilities

2. **JavaScript Thread Analysis:**
   * Identify long-running JavaScript operations
   * Check for synchronous blocking operations on the JS thread
   * Review heavy computations that should be moved to native or web workers
   * Analyze JavaScript bundle size and load time
   * Check for excessive use of `setInterval` or `setTimeout`
   * Evaluate initialization and bootstrap performance

3. **Component Re-rendering Analysis:**
   * Identify unnecessary component re-renders
   * Check for missing React.memo, useMemo, useCallback usage
   * Review component structure for optimization opportunities
   * Analyze prop passing patterns that trigger re-renders
   * Check for inline function/object creation in render methods
   * Evaluate context usage and context splitting opportunities
   * Review state management causing excessive re-renders (Redux, Zustand, etc.)

4. **FlatList/ScrollView Optimization:**
   * Review list rendering performance (FlatList vs. ScrollView)
   * Check for proper keyExtractor implementation
   * Evaluate getItemLayout usage for fixed-size items
   * Assess windowSize, maxToRenderPerBatch, initialNumToRender configurations
   * Check for removeClippedSubviews usage
   * Review cell rendering complexity
   * Evaluate use of memo for list item components

5. **Bridge Communication:**
   * Identify excessive bridge calls between JS and native
   * Check for batch-able operations being called individually
   * Review native module usage and calling patterns
   * Assess opportunities to reduce bridge traffic
   * Evaluate use of native modules vs. JavaScript implementations
   * Check for proper use of Turbo Modules (if using new architecture)

6. **Image Optimization:**
   * Review image loading strategy (remote vs. bundled)
   * Check for image caching implementation
   * Evaluate image sizing and resolution (overly large images)
   * Assess use of react-native-fast-image or similar libraries
   * Check for proper image format usage (WebP, AVIF support)
   * Review progressive image loading
   * Evaluate lazy loading for off-screen images

7. **Animation Performance:**
   * Review animation implementations (Animated API, Reanimated)
   * Check for useNativeDriver: true usage
   * Identify animations running on JavaScript thread (should be native)
   * Evaluate gesture handler performance (react-native-gesture-handler)
   * Check for layout animations causing performance issues
   * Assess animation frame rate and smoothness
   * Review LayoutAnimation usage and alternatives

8. **Navigation Performance:**
   * Analyze navigation library configuration (React Navigation, etc.)
   * Check for lazy loading of screens
   * Evaluate screen transition animations
   * Review state persistence strategies
   * Assess deep linking performance
   * Check for unnecessary navigation stack depth

9. **State Management:**
   * Review state management library usage (Redux, MobX, Zustand, Recoil, Context)
   * Identify over-rendering caused by global state changes
   * Check for selector optimization (reselect for Redux)
   * Evaluate state normalization
   * Assess component subscription patterns
   * Review frequency of state updates

10. **Memory Management:**
    * Identify memory leaks (event listeners not cleaned up, timers)
    * Check for proper cleanup in useEffect hooks
    * Review large data structures held in memory
    * Assess image memory usage
    * Evaluate cache management strategies
    * Check for circular references preventing garbage collection

11. **Bundle Size and Startup Time:**
    * Analyze JavaScript bundle size
    * Review code splitting and lazy loading opportunities
    * Check for unnecessary dependencies
    * Evaluate tree shaking effectiveness
    * Assess inline requires usage
    * Review Hermes bytecode compilation (if using Hermes)
    * Check for duplicate dependencies

12. **New Architecture (Fabric & TurboModules):**
    * If applicable, review migration to new architecture
    * Check for proper use of Fabric renderer
    * Evaluate TurboModules implementation
    * Assess JSI (JavaScript Interface) usage
    * Review compatibility with new architecture

13. **Native Code Performance:**
    * Review custom native modules for performance issues
    * Check for efficient data passing between JS and native
    * Evaluate native UI component implementations
    * Assess native animation performance

14. **Third-Party Library Assessment:**
    * Identify performance-heavy third-party libraries
    * Check for lighter alternatives
    * Review library bundle size contributions
    * Assess library maintenance and optimization status
    * Evaluate impact of native dependencies

15. **Development vs. Production:**
    * Ensure optimizations are tested in production builds
    * Check for __DEV__ conditionals affecting performance
    * Review debug logging impact
    * Assess production build configuration (Hermes, ProGuard/R8, etc.)

**Expected Output:** A comprehensive performance optimization report including:

1. **Performance Summary:**
   - Overall performance rating (Excellent/Good/Moderate/Poor)
   - Key performance metrics (if available)
   - Critical performance issues count
   - Quick wins vs. long-term optimizations

2. **Detailed Findings by Category:**
   - For each analysis area:
     - Current performance state
     - Issues identified with severity (Critical/High/Medium/Low)
     - Specific file locations and line numbers
     - Measured or estimated impact
     - Code examples demonstrating issues

3. **Benchmarks and Measurements:**
   - JavaScript thread FPS during typical operations
   - UI thread performance
   - Time to Interactive (TTI)
   - Bundle size analysis
   - Memory usage patterns
   - Bridge traffic volume

4. **Optimization Recommendations:**
   - Prioritized list of optimizations
   - Quick wins (high impact, low effort)
   - Code refactoring needed
   - Library replacements or additions
   - Architecture changes
   - Configuration improvements

5. **Code Examples:**
   - Before/after code comparisons
   - Specific optimization implementations
   - Performance measurement code snippets

6. **Implementation Roadmap:**
   - Phase 1: Critical fixes and quick wins (1-2 weeks)
   - Phase 2: Medium-term optimizations (1 month)
   - Phase 3: Long-term architectural improvements (2-3 months)

**Example Output:**

```
# React Native Performance Optimization Report

## Performance Summary
- **Overall Rating:** Moderate - Significant optimization opportunities identified
- **Critical Issues:** 3
- **High Priority:** 8
- **Medium Priority:** 12
- **Quick Wins Available:** 5 optimizations with immediate impact

## Key Metrics
- **Bundle Size:** 8.2 MB (Target: <5 MB) ⚠️
- **App Startup Time:** 3.2s (Target: <2s) ⚠️
- **Average FPS:** 52 FPS (Target: 60 FPS) ⚠️
- **Memory Usage:** 180 MB average (Acceptable)

## Detailed Findings

### 1. Component Re-rendering (Status: Needs Improvement)
**Severity:** High
**Impact:** Major performance degradation on list screens

**Issue #1: Excessive Re-renders in Product List**
File: `src/screens/ProductListScreen.tsx:45`

**Problem:**
```typescript
// Current implementation - re-renders entire list on any state change
const ProductListScreen = () => {
  const [products, setProducts] = useState([]);
  const [filters, setFilters] = useState({});

  return (
    <FlatList
      data={products}
      renderItem={({ item }) => (
        // Inline component definition causes re-render of all items
        <View>
          <Text>{item.name}</Text>
          <TouchableOpacity onPress={() => addToCart(item)}>
            <Text>Add to Cart</Text>
          </TouchableOpacity>
        </View>
      )}
    />
  );
};
```

**Impact:**
- All list items re-render when filters change
- ~200ms lag when updating filters
- FPS drops to 35-40 during interaction

**Optimization:**
```typescript
// Optimized implementation
const ProductItem = React.memo(({ item, onAddToCart }) => (
  <View>
    <Text>{item.name}</Text>
    <TouchableOpacity onPress={() => onAddToCart(item)}>
      <Text>Add to Cart</Text>
    </TouchableOpacity>
  </View>
));

const ProductListScreen = () => {
  const [products, setProducts] = useState([]);
  const [filters, setFilters] = useState({});

  // Memoize callback to prevent ProductItem re-renders
  const handleAddToCart = useCallback((item) => {
    addToCart(item);
  }, []);

  // Memoize filtered products
  const filteredProducts = useMemo(
    () => applyFilters(products, filters),
    [products, filters]
  );

  return (
    <FlatList
      data={filteredProducts}
      renderItem={({ item }) => (
        <ProductItem item={item} onAddToCart={handleAddToCart} />
      )}
      keyExtractor={(item) => item.id}
      // Performance optimizations
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      windowSize={10}
      initialNumToRender={10}
      getItemLayout={(data, index) => ({
        length: ITEM_HEIGHT,
        offset: ITEM_HEIGHT * index,
        index,
      })}
    />
  );
};
```

**Expected Improvement:**
- Reduces re-renders by ~90%
- Improves FPS to 58-60
- Smoother filter interactions

### 2. JavaScript Thread Blocking (Status: Critical)
**Severity:** Critical
**Impact:** App freezes during data processing

**Issue #2: Synchronous Data Processing**
File: `src/utils/dataProcessor.ts:78`

**Problem:**
```typescript
// Blocking operation on JS thread
export const processLargeDataset = (data) => {
  const result = [];
  for (let i = 0; i < data.length; i++) {
    // Heavy computation ~100ms per item
    result.push(expensiveTransformation(data[i]));
  }
  return result;
};
```

**Impact:**
- Blocks UI for 2-5 seconds with large datasets
- Unresponsive to user input
- No loading indicator possible

**Optimization Option 1: Use Web Worker (via react-native-workers)**
```typescript
// worker.js
self.onmessage = (event) => {
  const { data } = event.data;
  const result = data.map(item => expensiveTransformation(item));
  self.postMessage(result);
};

// dataProcessor.ts
import { Worker } from 'react-native-workers';

export const processLargeDataset = async (data) => {
  const worker = new Worker('./worker.js');

  return new Promise((resolve) => {
    worker.onmessage = (event) => {
      resolve(event.data);
      worker.terminate();
    };
    worker.postMessage({ data });
  });
};
```

**Optimization Option 2: Chunk Processing with InteractionManager**
```typescript
export const processLargeDataset = async (data) => {
  const result = [];
  const chunkSize = 10;

  for (let i = 0; i < data.length; i += chunkSize) {
    await InteractionManager.runAfterInteractions(() => {
      const chunk = data.slice(i, i + chunkSize);
      result.push(...chunk.map(item => expensiveTransformation(item)));
    });
  }

  return result;
};
```

**Expected Improvement:**
- Non-blocking UI
- Maintains 60 FPS during processing
- Better user experience with progress indicators

[... more findings ...]

## Quick Wins (Implement First)

### 1. Enable Hermes Engine ✅
**Effort:** 5 minutes
**Impact:** 20-30% startup time improvement, 15% memory reduction
**Implementation:**
```javascript
// android/app/build.gradle
project.ext.react = [
    enableHermes: true  // Change to true
]
```

### 2. Add React.memo to List Items ✅
**Effort:** 1 hour
**Impact:** 50-70% reduction in list re-renders
**Files:** `ProductItem.tsx`, `OrderItem.tsx`, `NotificationItem.tsx`

### 3. Enable removeClippedSubviews on FlatLists ✅
**Effort:** 15 minutes
**Impact:** Improved scroll performance on long lists
**Files:** Search for all FlatList components

[... more quick wins ...]

## Implementation Roadmap

### Phase 1: Critical Fixes (Week 1)
1. Fix synchronous data processing blocking UI
2. Enable Hermes engine
3. Add React.memo to frequently rendered components
4. Fix memory leak from uncleaned timers

### Phase 2: Performance Optimizations (Weeks 2-4)
1. Implement proper FlatList optimizations
2. Optimize image loading and caching
3. Move heavy animations to native driver
4. Reduce bundle size by 30%

### Phase 3: Architecture Improvements (Months 2-3)
1. Consider migration to React Native new architecture
2. Implement code splitting for feature modules
3. Optimize state management architecture
4. Add comprehensive performance monitoring
```

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-03 (Performance Optimization Focus)
- ST-03 (Structured Output Templates)
- OC-05 (Severity Classification)

**Related Prompts:**
- `ios_swift_architecture_review.md` - For native iOS module performance
- `android_kotlin_best_practices.md` - For native Android module performance
- `cross_platform_architecture_design.md` - For overall React Native architecture
- `performance_bottleneck_identification.md` - For general performance analysis

**Customization Guide:**
- For Expo apps: Add Expo-specific optimization checks (EAS Build, expo-updates)
- For apps using new architecture: Focus more on Fabric and TurboModules analysis
- For specific navigation libraries: Customize navigation performance section
- For specific state management: Deep dive into Redux/MobX/Zustand specific optimizations
- For gaming or animation-heavy apps: Emphasize animation performance and Reanimated usage
- Specify React Native version: Optimizations differ between 0.68, 0.70, 0.72+ versions

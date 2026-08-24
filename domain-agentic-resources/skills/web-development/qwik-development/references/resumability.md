# Understanding Resumability

Deep dive into Qwik's core innovation: resumability.

## The Problem with Hydration

### Traditional Framework Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYDRATION (React, Vue, Svelte)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SERVER                           CLIENT                        │
│  ──────                           ──────                        │
│                                                                 │
│  1. Execute components            4. Download ALL JavaScript    │
│  2. Generate HTML                 5. Parse ALL JavaScript       │
│  3. Send HTML to client           6. Re-execute ALL components  │
│                                   7. Reconcile DOM              │
│                                   8. Attach event listeners     │
│                                                                 │
│  Work done: 100%                  Work duplicated: ~80%         │
│                                                                 │
│  Time to Interactive (TTI): SLOW                                │
│  Main thread blocked: YES                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**The hydration tax:**
- Re-download application code
- Re-parse JavaScript
- Re-execute component functions
- Rebuild component tree in memory
- Reconcile with existing DOM
- Finally attach event listeners

### Why Hydration is Expensive

| Framework | JS to Download | Main Thread Work |
|-----------|----------------|------------------|
| React SPA | 100-500KB | All components re-execute |
| Next.js | 80-300KB | All rendered components hydrate |
| Nuxt | 80-300KB | All rendered components hydrate |
| SvelteKit | 50-150KB | All components rehydrate |

Even with optimizations (code splitting, lazy loading), the fundamental issue remains: **the browser must re-execute code the server already ran**.

## How Resumability Works

### Qwik's Approach

```
┌─────────────────────────────────────────────────────────────────┐
│                    RESUMABILITY (Qwik)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SERVER                           CLIENT                        │
│  ──────                           ──────                        │
│                                                                 │
│  1. Execute components            4. Parse HTML (includes state)│
│  2. Serialize state into HTML     5. Ready for interaction      │
│  3. Send HTML + serialized state                                │
│                                                                 │
│  Work done: 100%                  Work duplicated: 0%           │
│                                                                 │
│  Time to Interactive (TTI): INSTANT                             │
│  Main thread blocked: NO                                        │
│                                                                 │
│                       USER CLICKS BUTTON                        │
│                              │                                  │
│                              ▼                                  │
│                    6. Download ONLY the clicked                 │
│                       handler's code (~1-5KB)                   │
│                    7. Execute handler                           │
│                    8. Update DOM                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### The Key Insight

Qwik serializes everything needed to resume:

```html
<!-- Server output (simplified) -->
<button on:click="chunk-abc.js#handleClick[0]">
  Count: <!--qsignal-->0<!--/qsignal-->
</button>

<script type="qwik/json">
{
  "signals": { "0": 0 },
  "refs": { "handleClick": "chunk-abc.js" }
}
</script>
```

**What's serialized:**
1. **Event listeners** → Which code chunk handles which event
2. **State** → Signal/store values
3. **Component boundaries** → Where components start/end
4. **Captured variables** → Closures needed by handlers

## Serialization in Detail

### Signal Serialization

```typescript
// Component code
const count = useSignal(42);

// Serialized in HTML
<script type="qwik/json">
{
  "ctx": {
    "count": { "value": 42 }
  }
}
</script>
```

### Store Serialization

```typescript
// Component code
const user = useStore({
  name: 'John',
  email: 'john@example.com',
  preferences: {
    theme: 'dark'
  }
});

// Serialized (deep)
<script type="qwik/json">
{
  "ctx": {
    "user": {
      "name": "John",
      "email": "john@example.com",
      "preferences": {
        "theme": "dark"
      }
    }
  }
}
</script>
```

### Event Handler Serialization

```typescript
// Component code
const handleClick = $(() => {
  count.value++;
});

// Becomes this in HTML
<button on:click="q-abc123.js#s_handleClick">Click</button>
```

The `q-abc123.js` is a tiny code chunk containing only `handleClick`.

## Lazy Loading at Function Level

### Traditional Code Splitting

```javascript
// React/Vue: Component-level splitting
const LazyComponent = lazy(() => import('./HeavyComponent'));

// Problem: Still loads entire component code
// Even if user only needs one button handler
```

### Qwik's Function-Level Splitting

```typescript
// Each $ creates a separate chunk
const handleSubmit = $(async () => {
  // This is chunk-1.js
  await submitForm();
});

const handleCancel = $(() => {
  // This is chunk-2.js
  resetForm();
});

const formatDate = $((date: Date) => {
  // This is chunk-3.js
  return date.toLocaleDateString();
});

// User clicks Submit → Only chunk-1.js loads
// User never clicks Cancel → chunk-2.js never loads
```

## Performance Comparison

### Initial Load

| Metric | Traditional SPA | Hydration (Next.js) | Resumable (Qwik) |
|--------|-----------------|---------------------|------------------|
| HTML size | ~10KB | ~50KB | ~60KB |
| Initial JS | 200-500KB | 80-200KB | **<1KB** |
| Parse time | 100-500ms | 50-200ms | **<10ms** |
| Execute time | 100-300ms | 50-150ms | **0ms** |
| TTI | 2-5s | 1-3s | **<100ms** |

### Interaction Performance

| Scenario | Hydration-based | Resumable |
|----------|-----------------|-----------|
| First click | Ready after hydration | **Instant** (loads handler) |
| Handler execution | Same | Same |
| Click on unhydrated area | Waits for hydration | **Instant** (loads that handler) |

## The Qwik Optimizer

### What It Does

The Qwik optimizer transforms your code at build time:

**Input (what you write):**
```typescript
export const MyComponent = component$(() => {
  const count = useSignal(0);

  return (
    <button onClick$={() => count.value++}>
      Count: {count.value}
    </button>
  );
});
```

**Output (what ships):**
```javascript
// main chunk (tiny)
export const MyComponent = component$(qrl('chunk-1.js', 's_MyComponent'));

// chunk-1.js (component render)
export const s_MyComponent = () => {
  const count = useSignal(0);
  return jsx('button', {
    'on:click': qrl('chunk-2.js', 's_onClick', [count]),
    children: ['Count: ', count.value]
  });
};

// chunk-2.js (click handler)
export const s_onClick = (count) => {
  count.value++;
};
```

### QRL (Qwik Resource Locator)

QRLs are serializable function references:

```typescript
qrl('chunk-2.js', 's_onClick', [count])
//   ↑ file       ↑ export    ↑ captured variables
```

This enables:
1. Lazy loading (download chunk-2.js only when needed)
2. Serialization (can be embedded in HTML)
3. Resumption (browser knows where to find code)

## When Resumability Shines

### Best Use Cases

| Scenario | Why Resumability Wins |
|----------|----------------------|
| E-commerce | Instant "Add to Cart" without full hydration |
| News/Content sites | Immediate interactivity for comments/sharing |
| Dashboards | Fast initial load, interaction loads incrementally |
| Mobile/slow devices | Less JavaScript = better battery/performance |
| Poor network | Tiny initial payload, progressive loading |

### Trade-offs to Consider

| Aspect | Hydration | Resumability |
|--------|-----------|--------------|
| Initial HTML size | Smaller | Larger (includes serialized state) |
| First interaction | Waits for hydration | May have small delay for first-time chunk load |
| Ecosystem | Mature | Growing |
| Mental model | Familiar | New concepts ($, QRL) |
| Bundle analysis | Traditional | Requires Qwik-specific tools |

## Debugging Resumability

### Inspect Serialized State

```javascript
// In browser console
document.querySelectorAll('script[type="qwik/json"]').forEach(s => {
  console.log(JSON.parse(s.textContent));
});
```

### Check What's Being Lazy Loaded

```javascript
// Network tab filter
// Filter by: qwik
// See which chunks load on interaction
```

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Non-serializable state | Runtime error | Use only serializable values in signals/stores |
| Handler not lazy loading | Large initial bundle | Ensure $ suffix on handlers |
| Closure not captured | Undefined variable | Pass dependencies through $ boundary |

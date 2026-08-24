# SolidJS Reactivity Deep Dive

## How Solid's Reactivity Works

Unlike React's virtual DOM diffing, Solid uses a **fine-grained reactive system** where:

1. **Signals** are observable values
2. **Effects** are observers that run when signals change
3. **The DOM** subscribes directly to signals

### The Reactive Graph

```
Signal A ──┬──→ Effect 1 ──→ DOM Node 1
           │
           └──→ Effect 2 ──→ DOM Node 2

Signal B ──────→ Effect 2 ──→ DOM Node 2
```

When Signal A changes, only subscribed effects run. No component re-renders.

## Tracking and Subscriptions

### Automatic Tracking

Solid tracks signal access during effect execution:

```typescript
createEffect(() => {
  // These signals are tracked automatically
  console.log(firstName(), lastName());
});
```

### Explicit Tracking with `on()`

Control exactly what triggers an effect:

```typescript
createEffect(on(
  // Only track these
  [firstName, lastName],
  // Run this callback
  ([first, last]) => {
    console.log(`Name: ${first} ${last}`);
    // age() access here is NOT tracked
    console.log(`Age: ${age()}`);
  }
));
```

### Untracking with `untrack()`

Read signals without subscribing:

```typescript
createEffect(() => {
  // Tracked
  const name = firstName();

  // NOT tracked - won't trigger this effect
  const ageValue = untrack(() => age());
});
```

## Batching Updates

Multiple signal updates are batched automatically in event handlers:

```typescript
const handleClick = () => {
  setA(1); // Batched
  setB(2); // Batched
  // Effects run once after both updates
};
```

For other contexts, use `batch()`:

```typescript
import { batch } from 'solid-js';

batch(() => {
  setA(1);
  setB(2);
  setC(3);
  // Single effect execution
});
```

## Signal Derivation Patterns

### Derived Signals (Getters)

Simple derived values without caching:

```typescript
const count = () => items().length;
```

### Memoized Derivations

Cache expensive computations:

```typescript
const sortedItems = createMemo(() => {
  console.log('Sorting...');
  return items().slice().sort((a, b) => a.name.localeCompare(b.name));
});
```

### Selectors for Fine-Grained List Updates

```typescript
const [selected, setSelected] = createSignal(null);
const isSelected = createSelector(selected);

<For each={items()}>
  {(item) => (
    <li class={isSelected(item.id) ? 'selected' : ''}>
      {item.name}
    </li>
  )}
</For>
```

## Store Reactivity

Stores provide deep reactivity with path-based updates:

```typescript
const [state, setState] = createStore({
  users: [
    { id: 1, name: 'Alice', active: true },
    { id: 2, name: 'Bob', active: false },
  ],
});

// Update nested path
setState('users', 0, 'active', false);

// Update by predicate
setState('users', user => user.active, 'status', 'online');

// Update array item
setState('users', produce(users => {
  users.push({ id: 3, name: 'Carol', active: true });
}));
```

## Reconciliation for External Data

When replacing entire data structures:

```typescript
import { reconcile } from 'solid-js/store';

const [state, setState] = createStore({ items: [] });

// Fetch new data
const newData = await fetchItems();

// Reconcile to minimize DOM updates
setState('items', reconcile(newData));
```

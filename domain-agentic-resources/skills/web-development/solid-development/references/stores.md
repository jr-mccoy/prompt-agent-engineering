# SolidJS Store Patterns

## When to Use Stores vs Signals

| Use Signals | Use Stores |
|-------------|------------|
| Primitive values | Nested objects |
| Simple state | Complex state structures |
| Single value tracking | Multiple related values |
| Pass to child components | Shared state trees |

## Creating Stores

### Basic Store

```typescript
import { createStore } from 'solid-js/store';

const [state, setState] = createStore({
  user: {
    name: 'John',
    email: 'john@example.com',
  },
  items: [],
  settings: {
    theme: 'light',
    notifications: true,
  },
});
```

### Typed Store

```typescript
interface AppState {
  user: User | null;
  items: Item[];
  loading: boolean;
}

const [state, setState] = createStore<AppState>({
  user: null,
  items: [],
  loading: false,
});
```

## Updating Stores

### Path-Based Updates

```typescript
// Update single value
setState('user', 'name', 'Jane');

// Update nested value
setState('settings', 'notifications', false);

// Update array item by index
setState('items', 0, 'completed', true);

// Update multiple properties
setState('user', { name: 'Jane', email: 'jane@example.com' });
```

### Function Updates

```typescript
// Toggle value
setState('settings', 'theme', t => t === 'light' ? 'dark' : 'light');

// Update based on current value
setState('items', 0, 'count', c => c + 1);
```

### Array Operations

```typescript
// Replace array
setState('items', [newItem1, newItem2]);

// Append to array
setState('items', items => [...items, newItem]);

// Remove from array
setState('items', items => items.filter(i => i.id !== removeId));

// Update specific items by predicate
setState('items', item => item.completed, 'archived', true);
```

### Using produce() for Immer-like Updates

```typescript
import { produce } from 'solid-js/store';

setState(produce(state => {
  state.items.push(newItem);
  state.user.lastUpdated = new Date();
}));
```

## Store Selectors

### Creating Derived State

```typescript
const activeItems = () => state.items.filter(i => i.active);
const itemCount = () => state.items.length;
const hasUser = () => state.user !== null;
```

### Memoized Selectors

```typescript
const sortedItems = createMemo(() =>
  state.items.slice().sort((a, b) => a.name.localeCompare(b.name))
);
```

## Store Context Pattern

```typescript
// store.tsx
const StoreContext = createContext<[AppState, SetStoreFunction<AppState>]>();

export function StoreProvider(props: ParentProps) {
  const [state, setState] = createStore<AppState>(initialState);

  return (
    <StoreContext.Provider value={[state, setState]}>
      {props.children}
    </StoreContext.Provider>
  );
}

export function useStore() {
  const context = useContext(StoreContext);
  if (!context) throw new Error('useStore must be within StoreProvider');
  return context;
}
```

## Store with Actions

```typescript
function createAppStore() {
  const [state, setState] = createStore<AppState>(initialState);

  const actions = {
    addItem(item: Item) {
      setState('items', items => [...items, item]);
    },

    removeItem(id: string) {
      setState('items', items => items.filter(i => i.id !== id));
    },

    toggleItem(id: string) {
      setState('items', item => item.id === id, 'completed', c => !c);
    },

    async fetchItems() {
      setState('loading', true);
      try {
        const items = await api.getItems();
        setState('items', reconcile(items));
      } finally {
        setState('loading', false);
      }
    },
  };

  return [state, actions] as const;
}
```

## Reconciling External Data

When receiving data from external sources:

```typescript
import { reconcile } from 'solid-js/store';

// Minimal DOM updates by reconciling
const refreshData = async () => {
  const newData = await fetchData();
  setState('items', reconcile(newData));
};
```

## Store Subscriptions

Track specific store paths:

```typescript
createEffect(() => {
  // Only triggers when user.name changes
  console.log('Name changed:', state.user.name);
});

createEffect(() => {
  // Triggers when any item changes
  console.log('Items:', state.items);
});
```

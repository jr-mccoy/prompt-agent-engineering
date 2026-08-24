# SolidJS Component Patterns

## Compound Components

```typescript
const Tabs = {
  Root: (props: ParentProps) => {
    const [activeTab, setActiveTab] = createSignal(0);

    return (
      <TabsContext.Provider value={{ activeTab, setActiveTab }}>
        <div class="tabs">{props.children}</div>
      </TabsContext.Provider>
    );
  },

  List: (props: ParentProps) => (
    <div class="tabs-list">{props.children}</div>
  ),

  Tab: (props: { index: number } & ParentProps) => {
    const { activeTab, setActiveTab } = useTabsContext();
    return (
      <button
        class={activeTab() === props.index ? 'active' : ''}
        onClick={() => setActiveTab(props.index)}
      >
        {props.children}
      </button>
    );
  },

  Panels: (props: ParentProps) => (
    <div class="tabs-panels">{props.children}</div>
  ),

  Panel: (props: { index: number } & ParentProps) => {
    const { activeTab } = useTabsContext();
    return (
      <Show when={activeTab() === props.index}>
        <div class="tabs-panel">{props.children}</div>
      </Show>
    );
  },
};

// Usage
<Tabs.Root>
  <Tabs.List>
    <Tabs.Tab index={0}>Tab 1</Tabs.Tab>
    <Tabs.Tab index={1}>Tab 2</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panels>
    <Tabs.Panel index={0}>Content 1</Tabs.Panel>
    <Tabs.Panel index={1}>Content 2</Tabs.Panel>
  </Tabs.Panels>
</Tabs.Root>
```

## Render Props

```typescript
interface MousePosition {
  x: number;
  y: number;
}

function MouseTracker(props: {
  children: (pos: Accessor<MousePosition>) => JSX.Element;
}) {
  const [position, setPosition] = createSignal({ x: 0, y: 0 });

  onMount(() => {
    const handler = (e: MouseEvent) => {
      setPosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handler);
    onCleanup(() => window.removeEventListener('mousemove', handler));
  });

  return props.children(position);
}

// Usage
<MouseTracker>
  {(pos) => <p>Mouse: {pos().x}, {pos().y}</p>}
</MouseTracker>
```

## Higher-Order Components

```typescript
function withLoading<P extends object>(
  Component: (props: P) => JSX.Element
) {
  return (props: P & { loading?: boolean }) => {
    const [local, rest] = splitProps(props, ['loading']);

    return (
      <Show when={!local.loading} fallback={<Spinner />}>
        <Component {...(rest as P)} />
      </Show>
    );
  };
}

// Usage
const UserCardWithLoading = withLoading(UserCard);
<UserCardWithLoading loading={isLoading()} user={user()} />
```

## Slot Pattern

```typescript
interface DialogProps {
  title?: JSX.Element;
  actions?: JSX.Element;
  children: JSX.Element;
}

function Dialog(props: DialogProps) {
  return (
    <div class="dialog">
      <Show when={props.title}>
        <header class="dialog-header">{props.title}</header>
      </Show>
      <main class="dialog-content">{props.children}</main>
      <Show when={props.actions}>
        <footer class="dialog-actions">{props.actions}</footer>
      </Show>
    </div>
  );
}

// Usage
<Dialog
  title={<h2>Confirm</h2>}
  actions={
    <>
      <button onClick={onCancel}>Cancel</button>
      <button onClick={onConfirm}>Confirm</button>
    </>
  }
>
  <p>Are you sure?</p>
</Dialog>
```

## Polymorphic Components

```typescript
import { ValidComponent, Dynamic } from 'solid-js/web';

interface ButtonProps<T extends ValidComponent> {
  as?: T;
  variant?: 'primary' | 'secondary';
  children: JSX.Element;
}

function Button<T extends ValidComponent = 'button'>(
  props: ButtonProps<T> & Omit<ComponentProps<T>, keyof ButtonProps<T>>
) {
  const [local, others] = splitProps(props, ['as', 'variant', 'children']);

  return (
    <Dynamic
      component={local.as ?? 'button'}
      class={`btn btn-${local.variant ?? 'primary'}`}
      {...others}
    >
      {local.children}
    </Dynamic>
  );
}

// Usage
<Button>Click me</Button>
<Button as="a" href="/page">Link button</Button>
<Button as={Link} href="/route">Router link</Button>
```

## Controlled vs Uncontrolled

```typescript
interface InputProps {
  value?: string;
  defaultValue?: string;
  onInput?: (value: string) => void;
}

function Input(props: InputProps) {
  // Internal state for uncontrolled mode
  const [internalValue, setInternalValue] = createSignal(
    props.defaultValue ?? ''
  );

  // Use external value if provided (controlled), otherwise internal
  const value = () => props.value ?? internalValue();

  const handleInput = (e: InputEvent) => {
    const newValue = (e.target as HTMLInputElement).value;
    setInternalValue(newValue);
    props.onInput?.(newValue);
  };

  return <input value={value()} onInput={handleInput} />;
}

// Controlled
const [text, setText] = createSignal('');
<Input value={text()} onInput={setText} />

// Uncontrolled
<Input defaultValue="initial" onInput={console.log} />
```

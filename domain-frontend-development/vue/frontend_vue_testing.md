---
title: "Vue Component and Composable Testing"
category: frontend-development/vue
description: "Design comprehensive testing strategies for Vue 3 applications including component tests, composable tests, and Pinia store testing patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - vue
  - testing
  - vitest
  - vue-test-utils
  - component-testing
  - composables
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/vue/frontend_vue_composition_api.md
  - domain-frontend-development/vue/frontend_vue_pinia_state.md
  - domain-frontend-development/testing/frontend_testing_jest.md
---

# Vue Component and Composable Testing

**Objective:** Design and implement comprehensive testing patterns for Vue 3 applications including components, composables, and Pinia stores using Vue Test Utils and Vitest.

**When to Use:**
- Use when: Establishing testing patterns for a Vue project
- Use when: Reviewing existing Vue test coverage
- Use when: Migrating from Jest to Vitest
- Use when: Testing complex composables and store interactions
- Don't use when: Testing non-Vue JavaScript (use general JS testing)

## Instructions

1. **Assess Current Testing Setup**
   - What testing framework is in use (Vitest, Jest)?
   - Is Vue Test Utils properly configured?
   - Are there test utilities for common patterns?
   - What's the current coverage level?

2. **Design Component Test Patterns**
   - Mount vs shallowMount decisions
   - Prop and event testing
   - Slot content testing
   - Async component behavior

3. **Create Composable Test Patterns**
   - Testing reactive state
   - Testing lifecycle hooks
   - Mocking dependencies
   - Testing side effects

4. **Design Store Testing Patterns**
   - Pinia store unit tests
   - Store integration with components
   - Mocking store actions

5. **CRITICAL: Validate Testing Approach**
   - Tests should verify behavior, not implementation
   - Consider Vue-specific testing patterns
   - Ensure tests are maintainable and readable
   - **Confidence level** for test coverage:
     - **High Confidence**: User-facing behavior tested
     - **Medium Confidence**: Internal state tested
     - **Low Confidence**: Implementation details tested

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Test Vue's reactivity system (it's tested by Vue)
- Snapshot test dynamic content
- Mount when shallowMount would suffice
- Test third-party component internals
- Mock everything (integration matters)
- Test that props are passed (test the effect)

✅ **DO:**
- Test component behavior from user perspective
- Use proper async handling (flushPromises, nextTick)
- Test slots and scoped slots appropriately
- Mock network requests, not the data layer
- Test accessibility attributes
- Verify error states and edge cases

## Expected Output

A comprehensive Vue testing strategy including:
- Test file organization
- Component testing templates
- Composable testing patterns
- Store testing patterns
- CI/CD integration

## Example Output

```markdown
## Vue Testing Strategy

### Executive Summary
Establish Vitest + Vue Test Utils as the primary testing stack. Target 80% coverage with focus on user-facing behavior. Create shared test utilities for common patterns (mocking stores, router, i18n). Prioritize testing critical flows: auth, checkout, form submissions.

### Testing Stack

```
┌─────────────────────────────────────────────┐
│              Testing Stack                   │
├─────────────────────────────────────────────┤
│  Vitest          - Test runner              │
│  Vue Test Utils  - Component testing        │
│  @pinia/testing  - Store mocking            │
│  MSW             - API mocking              │
│  c8              - Coverage                 │
│  Playwright      - E2E (separate config)    │
└─────────────────────────────────────────────┘
```

### Project Setup

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath } from 'url';

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'happy-dom',
    globals: true,
    setupFiles: ['./tests/setup.ts'],
    include: ['**/*.{test,spec}.{js,ts,vue}'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'tests/'],
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 70,
        statements: 80,
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
});
```

```typescript
// tests/setup.ts
import { config } from '@vue/test-utils';
import { createTestingPinia } from '@pinia/testing';
import { vi } from 'vitest';

// Global test configuration
config.global.plugins = [
  createTestingPinia({ createSpy: vi.fn }),
];

// Mock browser APIs
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(),
    removeListener: vi.fn(),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});
```

### Test Utilities

```typescript
// tests/utils/index.ts
import { mount, VueWrapper } from '@vue/test-utils';
import { createTestingPinia } from '@pinia/testing';
import { createRouter, createMemoryHistory } from 'vue-router';
import { vi } from 'vitest';
import type { Component } from 'vue';

interface MountOptions {
  props?: Record<string, unknown>;
  slots?: Record<string, unknown>;
  stubs?: Record<string, unknown>;
  initialState?: Record<string, unknown>;
  route?: string;
}

export function mountWithPlugins(
  component: Component,
  options: MountOptions = {}
) {
  const router = createRouter({
    history: createMemoryHistory(),
    routes: [{ path: '/', component: { template: '<div />' } }],
  });

  if (options.route) {
    router.push(options.route);
  }

  return mount(component, {
    props: options.props,
    slots: options.slots,
    global: {
      plugins: [
        router,
        createTestingPinia({
          createSpy: vi.fn,
          initialState: options.initialState,
        }),
      ],
      stubs: {
        teleport: true,
        ...options.stubs,
      },
    },
  });
}

// Wait for all pending promises and DOM updates
export async function flushAll() {
  await flushPromises();
  await nextTick();
}
```

### Component Testing Patterns

#### Pattern 1: Basic Component Test

```typescript
// components/Button.test.ts
import { mount } from '@vue/test-utils';
import Button from './Button.vue';

describe('Button', () => {
  it('renders slot content', () => {
    const wrapper = mount(Button, {
      slots: { default: 'Click me' },
    });

    expect(wrapper.text()).toContain('Click me');
  });

  it('emits click event when clicked', async () => {
    const wrapper = mount(Button);

    await wrapper.trigger('click');

    expect(wrapper.emitted('click')).toHaveLength(1);
  });

  it('applies variant class', () => {
    const wrapper = mount(Button, {
      props: { variant: 'primary' },
    });

    expect(wrapper.classes()).toContain('btn-primary');
  });

  it('is disabled when disabled prop is true', () => {
    const wrapper = mount(Button, {
      props: { disabled: true },
    });

    expect(wrapper.attributes('disabled')).toBeDefined();
    expect(wrapper.classes()).toContain('btn-disabled');
  });

  it('shows loading spinner when loading', () => {
    const wrapper = mount(Button, {
      props: { loading: true },
      slots: { default: 'Submit' },
    });

    expect(wrapper.find('[data-testid="spinner"]').exists()).toBe(true);
    expect(wrapper.text()).not.toContain('Submit');
  });
});
```

#### Pattern 2: Form Component Test

```typescript
// components/LoginForm.test.ts
import { mount, flushPromises } from '@vue/test-utils';
import { createTestingPinia } from '@pinia/testing';
import { vi } from 'vitest';
import LoginForm from './LoginForm.vue';
import { useAuthStore } from '@/stores/auth';

describe('LoginForm', () => {
  const createWrapper = (options = {}) => {
    return mount(LoginForm, {
      global: {
        plugins: [
          createTestingPinia({
            createSpy: vi.fn,
            stubActions: false,
          }),
        ],
      },
      ...options,
    });
  };

  it('validates email format', async () => {
    const wrapper = createWrapper();

    await wrapper.find('input[type="email"]').setValue('invalid-email');
    await wrapper.find('form').trigger('submit');

    expect(wrapper.text()).toContain('Valid email required');
  });

  it('validates required password', async () => {
    const wrapper = createWrapper();

    await wrapper.find('input[type="email"]').setValue('test@example.com');
    await wrapper.find('form').trigger('submit');

    expect(wrapper.text()).toContain('Password is required');
  });

  it('submits form with valid data', async () => {
    const wrapper = createWrapper();
    const authStore = useAuthStore();

    await wrapper.find('input[type="email"]').setValue('test@example.com');
    await wrapper.find('input[type="password"]').setValue('password123');
    await wrapper.find('form').trigger('submit');

    expect(authStore.login).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123',
    });
  });

  it('shows error message on login failure', async () => {
    const wrapper = createWrapper();
    const authStore = useAuthStore();

    // Mock login to reject
    vi.mocked(authStore.login).mockRejectedValue(
      new Error('Invalid credentials')
    );

    await wrapper.find('input[type="email"]').setValue('test@example.com');
    await wrapper.find('input[type="password"]').setValue('wrong');
    await wrapper.find('form').trigger('submit');
    await flushPromises();

    expect(wrapper.text()).toContain('Invalid credentials');
  });

  it('disables submit button while loading', async () => {
    const wrapper = createWrapper();
    const authStore = useAuthStore();

    // Mock login to never resolve
    vi.mocked(authStore.login).mockImplementation(
      () => new Promise(() => {})
    );

    await wrapper.find('input[type="email"]').setValue('test@example.com');
    await wrapper.find('input[type="password"]').setValue('password');
    await wrapper.find('form').trigger('submit');

    expect(wrapper.find('button[type="submit"]').attributes('disabled')).toBeDefined();
  });
});
```

#### Pattern 3: Component with Async Data

```typescript
// components/UserProfile.test.ts
import { mount, flushPromises } from '@vue/test-utils';
import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';
import UserProfile from './UserProfile.vue';

const server = setupServer(
  http.get('/api/users/:id', ({ params }) => {
    return HttpResponse.json({
      id: params.id,
      name: 'John Doe',
      email: 'john@example.com',
    });
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('UserProfile', () => {
  it('shows loading state initially', () => {
    const wrapper = mount(UserProfile, {
      props: { userId: '1' },
    });

    expect(wrapper.find('[data-testid="loading"]').exists()).toBe(true);
  });

  it('renders user data after loading', async () => {
    const wrapper = mount(UserProfile, {
      props: { userId: '1' },
    });

    await flushPromises();

    expect(wrapper.text()).toContain('John Doe');
    expect(wrapper.text()).toContain('john@example.com');
  });

  it('shows error on API failure', async () => {
    server.use(
      http.get('/api/users/:id', () => {
        return HttpResponse.json(
          { message: 'User not found' },
          { status: 404 }
        );
      })
    );

    const wrapper = mount(UserProfile, {
      props: { userId: '999' },
    });

    await flushPromises();

    expect(wrapper.find('[role="alert"]').exists()).toBe(true);
    expect(wrapper.text()).toContain('User not found');
  });

  it('refetches when userId changes', async () => {
    const wrapper = mount(UserProfile, {
      props: { userId: '1' },
    });

    await flushPromises();
    expect(wrapper.text()).toContain('John Doe');

    server.use(
      http.get('/api/users/:id', () => {
        return HttpResponse.json({
          id: '2',
          name: 'Jane Smith',
          email: 'jane@example.com',
        });
      })
    );

    await wrapper.setProps({ userId: '2' });
    await flushPromises();

    expect(wrapper.text()).toContain('Jane Smith');
  });
});
```

#### Pattern 4: Slot Testing

```typescript
// components/Modal.test.ts
import { mount } from '@vue/test-utils';
import Modal from './Modal.vue';

describe('Modal', () => {
  it('renders default slot content', () => {
    const wrapper = mount(Modal, {
      props: { isOpen: true },
      slots: {
        default: '<p>Modal content</p>',
      },
    });

    expect(wrapper.html()).toContain('Modal content');
  });

  it('renders header slot', () => {
    const wrapper = mount(Modal, {
      props: { isOpen: true },
      slots: {
        header: '<h2>Custom Header</h2>',
      },
    });

    expect(wrapper.find('header').text()).toContain('Custom Header');
  });

  it('renders scoped slot with close function', () => {
    const wrapper = mount(Modal, {
      props: { isOpen: true },
      slots: {
        footer: `
          <template #footer="{ close }">
            <button @click="close">Custom Close</button>
          </template>
        `,
      },
    });

    expect(wrapper.find('footer button').text()).toContain('Custom Close');
  });

  it('is hidden when isOpen is false', () => {
    const wrapper = mount(Modal, {
      props: { isOpen: false },
      slots: { default: 'Content' },
    });

    expect(wrapper.find('[role="dialog"]').exists()).toBe(false);
  });

  it('emits close event when clicking backdrop', async () => {
    const wrapper = mount(Modal, {
      props: { isOpen: true },
    });

    await wrapper.find('[data-testid="backdrop"]').trigger('click');

    expect(wrapper.emitted('close')).toHaveLength(1);
  });

  it('traps focus within modal', async () => {
    const wrapper = mount(Modal, {
      props: { isOpen: true },
      slots: {
        default: `
          <input data-testid="input-1" />
          <input data-testid="input-2" />
        `,
      },
      attachTo: document.body,
    });

    const modal = wrapper.find('[role="dialog"]');
    expect(document.activeElement).toBe(modal.element);

    wrapper.unmount();
  });
});
```

### Composable Testing Patterns

```typescript
// composables/useCounter.test.ts
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('starts with initial value', () => {
    const { count } = useCounter(10);

    expect(count.value).toBe(10);
  });

  it('increments count', () => {
    const { count, increment } = useCounter(0);

    increment();

    expect(count.value).toBe(1);
  });

  it('decrements count', () => {
    const { count, decrement } = useCounter(5);

    decrement();

    expect(count.value).toBe(4);
  });

  it('respects min value', () => {
    const { count, decrement } = useCounter(0, { min: 0 });

    decrement();

    expect(count.value).toBe(0);
  });

  it('respects max value', () => {
    const { count, increment } = useCounter(10, { max: 10 });

    increment();

    expect(count.value).toBe(10);
  });
});
```

```typescript
// composables/useAsync.test.ts
import { useAsync } from './useAsync';
import { flushPromises } from '@vue/test-utils';
import { vi } from 'vitest';

describe('useAsync', () => {
  it('starts with loading false and no data', () => {
    const asyncFn = vi.fn().mockResolvedValue('data');
    const { data, loading, error } = useAsync(asyncFn);

    expect(loading.value).toBe(false);
    expect(data.value).toBe(null);
    expect(error.value).toBe(null);
  });

  it('sets loading to true while executing', async () => {
    const asyncFn = vi.fn().mockImplementation(
      () => new Promise(resolve => setTimeout(() => resolve('data'), 100))
    );

    const { loading, execute } = useAsync(asyncFn);

    const promise = execute();
    expect(loading.value).toBe(true);

    await promise;
    expect(loading.value).toBe(false);
  });

  it('sets data on success', async () => {
    const asyncFn = vi.fn().mockResolvedValue({ name: 'Test' });

    const { data, execute } = useAsync(asyncFn);
    await execute();

    expect(data.value).toEqual({ name: 'Test' });
  });

  it('sets error on failure', async () => {
    const asyncFn = vi.fn().mockRejectedValue(new Error('Failed'));

    const { error, execute } = useAsync(asyncFn);
    await execute();

    expect(error.value).toBeInstanceOf(Error);
    expect(error.value?.message).toBe('Failed');
  });

  it('passes arguments to async function', async () => {
    const asyncFn = vi.fn().mockResolvedValue('result');

    const { execute } = useAsync(asyncFn);
    await execute('arg1', 'arg2');

    expect(asyncFn).toHaveBeenCalledWith('arg1', 'arg2');
  });
});
```

```typescript
// composables/useFetch.test.ts
import { ref } from 'vue';
import { useFetch } from './useFetch';
import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';
import { flushPromises } from '@vue/test-utils';

const server = setupServer();

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('useFetch', () => {
  it('fetches data on mount', async () => {
    server.use(
      http.get('/api/data', () => {
        return HttpResponse.json({ message: 'Hello' });
      })
    );

    const { data } = useFetch('/api/data');
    await flushPromises();

    expect(data.value).toEqual({ message: 'Hello' });
  });

  it('refetches when url changes', async () => {
    server.use(
      http.get('/api/users/1', () => HttpResponse.json({ id: 1, name: 'User 1' })),
      http.get('/api/users/2', () => HttpResponse.json({ id: 2, name: 'User 2' }))
    );

    const url = ref('/api/users/1');
    const { data } = useFetch(url);

    await flushPromises();
    expect(data.value?.name).toBe('User 1');

    url.value = '/api/users/2';
    await flushPromises();
    expect(data.value?.name).toBe('User 2');
  });
});
```

### Pinia Store Testing

```typescript
// stores/cart.test.ts
import { setActivePinia, createPinia } from 'pinia';
import { useCartStore } from './cart';

describe('Cart Store', () => {
  beforeEach(() => {
    setActivePinia(createPinia());
  });

  describe('state', () => {
    it('starts with empty items', () => {
      const store = useCartStore();

      expect(store.items).toEqual([]);
    });
  });

  describe('getters', () => {
    it('calculates total correctly', () => {
      const store = useCartStore();

      store.items = [
        { id: '1', name: 'A', price: 10, quantity: 2 },
        { id: '2', name: 'B', price: 15, quantity: 1 },
      ];

      expect(store.total).toBe(35);
    });

    it('calculates item count', () => {
      const store = useCartStore();

      store.items = [
        { id: '1', name: 'A', price: 10, quantity: 2 },
        { id: '2', name: 'B', price: 15, quantity: 3 },
      ];

      expect(store.itemCount).toBe(5);
    });
  });

  describe('actions', () => {
    it('adds new item to cart', () => {
      const store = useCartStore();
      const product = { id: '1', name: 'Product', price: 10 };

      store.addItem(product);

      expect(store.items).toHaveLength(1);
      expect(store.items[0]).toEqual({ ...product, quantity: 1 });
    });

    it('increases quantity for existing item', () => {
      const store = useCartStore();
      const product = { id: '1', name: 'Product', price: 10 };

      store.addItem(product);
      store.addItem(product);

      expect(store.items).toHaveLength(1);
      expect(store.items[0].quantity).toBe(2);
    });

    it('removes item from cart', () => {
      const store = useCartStore();
      store.items = [{ id: '1', name: 'A', price: 10, quantity: 1 }];

      store.removeItem('1');

      expect(store.items).toEqual([]);
    });

    it('clears all items', () => {
      const store = useCartStore();
      store.items = [
        { id: '1', name: 'A', price: 10, quantity: 1 },
        { id: '2', name: 'B', price: 20, quantity: 2 },
      ];

      store.clear();

      expect(store.items).toEqual([]);
    });
  });
});
```

### Component with Store Integration

```typescript
// components/CartSummary.test.ts
import { mount } from '@vue/test-utils';
import { createTestingPinia } from '@pinia/testing';
import { vi } from 'vitest';
import CartSummary from './CartSummary.vue';
import { useCartStore } from '@/stores/cart';

describe('CartSummary', () => {
  const createWrapper = (initialState = {}) => {
    return mount(CartSummary, {
      global: {
        plugins: [
          createTestingPinia({
            createSpy: vi.fn,
            initialState: {
              cart: {
                items: [],
                ...initialState,
              },
            },
          }),
        ],
      },
    });
  };

  it('shows empty state when cart is empty', () => {
    const wrapper = createWrapper();

    expect(wrapper.text()).toContain('Your cart is empty');
  });

  it('displays cart items', () => {
    const wrapper = createWrapper({
      items: [
        { id: '1', name: 'Product A', price: 10, quantity: 2 },
        { id: '2', name: 'Product B', price: 20, quantity: 1 },
      ],
    });

    expect(wrapper.text()).toContain('Product A');
    expect(wrapper.text()).toContain('Product B');
  });

  it('shows correct total', () => {
    const wrapper = createWrapper({
      items: [
        { id: '1', name: 'A', price: 10, quantity: 2 },
        { id: '2', name: 'B', price: 20, quantity: 1 },
      ],
    });

    const store = useCartStore();
    expect(wrapper.text()).toContain(`$${store.total}`);
  });

  it('removes item when remove button clicked', async () => {
    const wrapper = createWrapper({
      items: [{ id: '1', name: 'Product', price: 10, quantity: 1 }],
    });

    const store = useCartStore();
    await wrapper.find('[data-testid="remove-1"]').trigger('click');

    expect(store.removeItem).toHaveBeenCalledWith('1');
  });
});
```

### CI/CD Configuration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type Check
        run: npm run type-check

      - name: Unit Tests
        run: npm run test:unit -- --coverage

      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
```

### Prioritized Testing Actions

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 1 | Setup Vitest + Vue Test Utils | Foundation | 2h |
| 2 | Create test utilities file | DRY | 2h |
| 3 | Add tests for auth flow | Critical | 8h |
| 4 | Add tests for checkout | Critical | 8h |
| 5 | Add composable tests | Medium | 4h |
| 6 | Add store tests | Medium | 4h |
| 7 | Setup CI with coverage | Automation | 2h |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Vue testing
- **ST-02 (Structured Sequential Instructions):** Systematic test design
- **RT-02 (Multi-Dimensional Analysis):** Components, composables, stores
- **OC-01 (Output Format Templates):** Clear test templates
- **QA-02 (Adversarial Stress-Test):** Edge cases and error states

## Related Prompts

- [frontend_vue_composition_api.md](frontend_vue_composition_api.md) - Composable patterns
- [frontend_vue_pinia_state.md](frontend_vue_pinia_state.md) - Store testing context
- [frontend_testing_vitest.md](../testing/frontend_testing_jest.md) - General Vitest patterns

## Customization Guide

- **For Nuxt 3**: Add nuxt-vitest setup, test utils for Nuxt
- **For Vue 2**: Use @vue/test-utils v1, adjust for Options API
- **For Cypress Component Testing**: Add Cypress-specific examples
- **For Storybook**: Add interaction testing with play functions

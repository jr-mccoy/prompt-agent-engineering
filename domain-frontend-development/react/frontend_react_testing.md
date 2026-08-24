---
title: "React Testing Strategy and Patterns"
category: frontend-development/react
description: "Design comprehensive testing strategies for React applications including unit tests, integration tests, and component testing with Testing Library patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - react
  - testing
  - jest
  - testing-library
  - unit-testing
  - integration-testing
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/testing/frontend_testing_jest.md
  - domain-frontend-development/testing/frontend_testing_playwright.md
  - domain-frontend-development/react/frontend_react_hooks_best_practices.md
---

# React Testing Strategy and Patterns

**Objective:** Analyze a React codebase's testing needs and design a comprehensive testing strategy using modern patterns including Testing Library, proper test organization, and effective mocking strategies.

**When to Use:**
- Use when: Establishing testing patterns for a React project
- Use when: Reviewing existing test coverage for improvement opportunities
- Use when: Migrating from Enzyme to React Testing Library
- Use when: Debugging flaky or ineffective tests
- Don't use when: Testing non-React JavaScript (use general JS testing prompts)

## Instructions

1. **Assess Current Testing State**
   - What testing framework is in use (Jest, Vitest)?
   - What component testing library (Testing Library, Enzyme)?
   - Current test coverage percentage and gaps
   - Test execution time and flakiness

2. **Categorize Tests Needed**
   - **Unit Tests**: Utility functions, hooks, pure logic
   - **Component Tests**: Individual component rendering and behavior
   - **Integration Tests**: Component interactions, data flow
   - **E2E Tests**: Critical user flows (separate from this prompt)

3. **Design Testing Patterns**
   For each component category, define:
   - What to test (behavior vs implementation)
   - How to query elements (accessibility-first)
   - How to handle async operations
   - What to mock and what to render real

4. **Create Test Templates**
   - Component test structure
   - Hook test patterns
   - Context provider test setup
   - Form testing patterns

5. **CRITICAL: Validate Testing Approach**
   - Tests should test behavior, not implementation
   - Avoid testing implementation details that could change
   - Ensure tests provide confidence without being brittle
   - **Confidence level** for test coverage:
     - **High Confidence**: Testing observable behavior users care about
     - **Medium Confidence**: Testing internal states that affect behavior
     - **Low Confidence**: Testing implementation details

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Test implementation details (internal state, private methods)
- Assert on snapshot tests for dynamic content
- Mock everything (integration tests need real interactions)
- Test third-party library behavior
- Use `waitFor` with arbitrary timeouts
- Test that React works (e.g., "renders without crashing" alone)
- Write tests that pass when the feature is broken

✅ **DO:**
- Test from the user's perspective (what they see and interact with)
- Use `screen` and accessibility queries (getByRole, getByLabelText)
- Test async behavior with proper waitFor patterns
- Mock network requests, not the data layer
- Test error states and edge cases
- Verify that tests fail when they should
- Keep tests readable and maintainable

## Expected Output

A comprehensive testing strategy including:
- Testing pyramid for the application
- Test file organization patterns
- Component testing templates
- Mocking strategies
- CI/CD integration recommendations

### Output Format

```markdown
## React Testing Strategy

### Testing Pyramid
[Visual representation of test distribution]

### Test Organization
[File structure and naming conventions]

### Component Testing Patterns
[Templates and examples for each component type]

### Mocking Strategy
[What to mock and how]

### CI/CD Integration
[Pipeline configuration]
```

## Example Output

```markdown
## React Testing Strategy

### Executive Summary
Establish a behavior-driven testing approach using Jest + React Testing Library. Target 80% coverage with focus on critical user flows. Migrate 23 Enzyme tests to Testing Library patterns. Add missing integration tests for form submissions and data fetching flows.

### Testing Pyramid

```
                    ▲
                   ╱ ╲
                  ╱ E2E╲              5%  - Playwright (critical paths)
                 ╱ (10) ╲
                ╱─────────╲
               ╱Integration╲          25% - Component + API interactions
              ╱   (50+)     ╲
             ╱───────────────╲
            ╱   Component      ╲       40% - Individual components
           ╱     (100+)         ╲
          ╱─────────────────────╲
         ╱       Unit             ╲    30% - Hooks, utils, pure functions
        ╱        (80+)              ╲
       ╱─────────────────────────────╲
```

### Test Organization

```
src/
├── components/
│   └── Button/
│       ├── Button.tsx
│       ├── Button.test.tsx        # Component tests
│       └── Button.stories.tsx     # Storybook (visual testing)
├── hooks/
│   └── useAuth/
│       ├── useAuth.ts
│       └── useAuth.test.ts        # Hook unit tests
├── utils/
│   └── formatters/
│       ├── formatters.ts
│       └── formatters.test.ts     # Pure function tests
└── features/
    └── checkout/
        ├── components/
        │   └── CheckoutForm.test.tsx
        └── __tests__/
            └── checkout.integration.test.tsx  # Integration tests
```

**Naming Conventions:**
- Unit/Component tests: `{name}.test.tsx`
- Integration tests: `{feature}.integration.test.tsx`
- Test utilities: `src/test-utils/`

### Testing Utilities Setup

```typescript
// src/test-utils/index.tsx
import React, { ReactElement } from 'react';
import { render, RenderOptions } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from '../contexts/ThemeContext';
import { AuthProvider } from '../contexts/AuthContext';

// Create a fresh QueryClient for each test
function createTestQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
        gcTime: 0,
      },
    },
    logger: {
      log: console.log,
      warn: console.warn,
      error: () => {}, // Silence errors in tests
    },
  });
}

interface WrapperProps {
  children: React.ReactNode;
}

function AllTheProviders({ children }: WrapperProps) {
  const queryClient = createTestQueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <ThemeProvider>
          <AuthProvider>
            {children}
          </AuthProvider>
        </ThemeProvider>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

function customRender(
  ui: ReactElement,
  options?: Omit<RenderOptions, 'wrapper'>
) {
  return render(ui, { wrapper: AllTheProviders, ...options });
}

// Re-export everything
export * from '@testing-library/react';
export { customRender as render };
export { createTestQueryClient };
```

### Component Testing Patterns

#### Pattern 1: Basic Component Test

```typescript
// Button.test.tsx
import { render, screen } from '@/test-utils';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);

    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('calls onClick handler when clicked', async () => {
    const user = userEvent.setup();
    const handleClick = jest.fn();

    render(<Button onClick={handleClick}>Click me</Button>);

    await user.click(screen.getByRole('button'));

    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Disabled</Button>);

    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('shows loading state', () => {
    render(<Button loading>Submit</Button>);

    expect(screen.getByRole('button')).toHaveAttribute('aria-busy', 'true');
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });
});
```

#### Pattern 2: Form Component Test

```typescript
// LoginForm.test.tsx
import { render, screen, waitFor } from '@/test-utils';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

// Mock the API
const mockLogin = jest.fn();
jest.mock('@/api/auth', () => ({
  login: (...args) => mockLogin(...args)
}));

describe('LoginForm', () => {
  const user = userEvent.setup();

  beforeEach(() => {
    mockLogin.mockReset();
  });

  it('submits form with email and password', async () => {
    mockLogin.mockResolvedValueOnce({ token: 'abc123' });

    render(<LoginForm onSuccess={jest.fn()} />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(mockLogin).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
      });
    });
  });

  it('shows validation errors for invalid input', async () => {
    render(<LoginForm onSuccess={jest.fn()} />);

    await user.type(screen.getByLabelText(/email/i), 'invalid-email');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    expect(await screen.findByText(/valid email/i)).toBeInTheDocument();
  });

  it('shows error message on failed login', async () => {
    mockLogin.mockRejectedValueOnce(new Error('Invalid credentials'));

    render(<LoginForm onSuccess={jest.fn()} />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'wrongpassword');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    expect(await screen.findByRole('alert')).toHaveTextContent(/invalid credentials/i);
  });

  it('disables submit button while loading', async () => {
    mockLogin.mockImplementation(() => new Promise(() => {})); // Never resolves

    render(<LoginForm onSuccess={jest.fn()} />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    expect(screen.getByRole('button', { name: /signing in/i })).toBeDisabled();
  });
});
```

#### Pattern 3: Component with Data Fetching

```typescript
// UserProfile.test.tsx
import { render, screen, waitFor } from '@/test-utils';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import { UserProfile } from './UserProfile';

const server = setupServer(
  rest.get('/api/users/:id', (req, res, ctx) => {
    return res(ctx.json({
      id: '1',
      name: 'John Doe',
      email: 'john@example.com',
    }));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('UserProfile', () => {
  it('displays loading state initially', () => {
    render(<UserProfile userId="1" />);

    expect(screen.getByRole('status')).toHaveTextContent(/loading/i);
  });

  it('displays user data after loading', async () => {
    render(<UserProfile userId="1" />);

    expect(await screen.findByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('displays error state when fetch fails', async () => {
    server.use(
      rest.get('/api/users/:id', (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ message: 'Server error' }));
      })
    );

    render(<UserProfile userId="1" />);

    expect(await screen.findByRole('alert')).toHaveTextContent(/error/i);
  });

  it('refetches data when userId changes', async () => {
    const { rerender } = render(<UserProfile userId="1" />);

    await screen.findByText('John Doe');

    server.use(
      rest.get('/api/users/:id', (req, res, ctx) => {
        return res(ctx.json({
          id: '2',
          name: 'Jane Smith',
          email: 'jane@example.com',
        }));
      })
    );

    rerender(<UserProfile userId="2" />);

    expect(await screen.findByText('Jane Smith')).toBeInTheDocument();
  });
});
```

#### Pattern 4: Testing Custom Hooks

```typescript
// useCounter.test.ts
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('starts with initial value', () => {
    const { result } = renderHook(() => useCounter(10));

    expect(result.current.count).toBe(10);
  });

  it('increments count', () => {
    const { result } = renderHook(() => useCounter(0));

    act(() => {
      result.current.increment();
    });

    expect(result.current.count).toBe(1);
  });

  it('decrements count', () => {
    const { result } = renderHook(() => useCounter(5));

    act(() => {
      result.current.decrement();
    });

    expect(result.current.count).toBe(4);
  });

  it('resets to initial value', () => {
    const { result } = renderHook(() => useCounter(10));

    act(() => {
      result.current.increment();
      result.current.increment();
      result.current.reset();
    });

    expect(result.current.count).toBe(10);
  });
});
```

#### Pattern 5: Testing Context Consumers

```typescript
// ThemeToggle.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ThemeProvider } from '@/contexts/ThemeContext';
import { ThemeToggle } from './ThemeToggle';

const renderWithTheme = (ui: React.ReactElement, initialTheme = 'light') => {
  return render(
    <ThemeProvider initialTheme={initialTheme}>
      {ui}
    </ThemeProvider>
  );
};

describe('ThemeToggle', () => {
  it('shows current theme', () => {
    renderWithTheme(<ThemeToggle />, 'light');

    expect(screen.getByRole('button')).toHaveTextContent(/light/i);
  });

  it('toggles theme on click', async () => {
    const user = userEvent.setup();
    renderWithTheme(<ThemeToggle />, 'light');

    await user.click(screen.getByRole('button'));

    expect(screen.getByRole('button')).toHaveTextContent(/dark/i);
  });
});
```

### Mocking Strategy

#### What to Mock

| Type | Mock? | How |
|------|-------|-----|
| Network requests | Yes | MSW (Mock Service Worker) |
| Date/Time | Yes | jest.useFakeTimers() |
| Browser APIs | Yes | jest.mock or polyfills |
| Third-party UI libraries | No | Render real components |
| Router | Partial | Use MemoryRouter |
| Context providers | Render real | Use test wrappers |
| Sibling components | No | Render real for integration |

#### MSW Setup

```typescript
// src/mocks/handlers.ts
import { rest } from 'msw';

export const handlers = [
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([
      { id: '1', name: 'User 1' },
      { id: '2', name: 'User 2' },
    ]));
  }),

  rest.post('/api/login', async (req, res, ctx) => {
    const { email, password } = await req.json();

    if (email === 'test@example.com' && password === 'password') {
      return res(ctx.json({ token: 'mock-token' }));
    }

    return res(ctx.status(401), ctx.json({ message: 'Invalid credentials' }));
  }),
];

// src/mocks/server.ts
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);

// src/setupTests.ts
import '@testing-library/jest-dom';
import { server } from './mocks/server';

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### Avoiding Common Anti-Patterns

#### Anti-Pattern 1: Testing Implementation Details
```typescript
// ❌ Bad: Testing internal state
it('sets loading to true', () => {
  const { result } = renderHook(() => useFetch('/api/data'));
  expect(result.current.loading).toBe(true);
});

// ✅ Good: Testing observable behavior
it('shows loading indicator while fetching', () => {
  render(<DataComponent />);
  expect(screen.getByRole('status')).toBeInTheDocument();
});
```

#### Anti-Pattern 2: Snapshot Tests for Dynamic Content
```typescript
// ❌ Bad: Snapshots that break on every data change
it('matches snapshot', () => {
  const { container } = render(<UserList users={mockUsers} />);
  expect(container).toMatchSnapshot();
});

// ✅ Good: Specific assertions
it('renders all users', () => {
  render(<UserList users={mockUsers} />);
  expect(screen.getAllByRole('listitem')).toHaveLength(mockUsers.length);
  expect(screen.getByText(mockUsers[0].name)).toBeInTheDocument();
});
```

#### Anti-Pattern 3: Testing Library Internals
```typescript
// ❌ Bad: Testing that onClick prop was passed
it('has onClick', () => {
  const { container } = render(<Button onClick={fn} />);
  expect(container.firstChild).toHaveProperty('onclick');
});

// ✅ Good: Testing click behavior
it('calls handler on click', async () => {
  const user = userEvent.setup();
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click</Button>);

  await user.click(screen.getByRole('button'));
  expect(handleClick).toHaveBeenCalled();
});
```

### CI/CD Integration

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

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test -- --coverage --watchAll=false

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info

      - name: Check coverage thresholds
        run: |
          npm test -- --coverage --coverageThreshold='{
            "global": {
              "branches": 70,
              "functions": 80,
              "lines": 80,
              "statements": 80
            }
          }' --watchAll=false
```

### Coverage Strategy

| Component Type | Coverage Target | Priority Tests |
|----------------|-----------------|----------------|
| Utilities | 95% | All edge cases |
| Hooks | 90% | All states and effects |
| UI Components | 80% | User interactions |
| Pages/Features | 70% | Critical flows |
| Error boundaries | 100% | Error handling |

### Prioritized Testing Actions

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 1 | Setup test utilities with providers | High | 2h |
| 2 | Add MSW for API mocking | High | 4h |
| 3 | Write tests for auth flow | Critical | 8h |
| 4 | Write tests for checkout flow | Critical | 8h |
| 5 | Add tests for form components | High | 6h |
| 6 | Setup coverage reporting in CI | Medium | 2h |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused testing strategy goal
- **ST-02 (Structured Sequential Instructions):** Step-by-step test design process
- **RT-02 (Multi-Dimensional Analysis):** Covers multiple test types
- **OC-01 (Output Format Templates):** Clear test templates
- **QA-02 (Adversarial Stress-Test):** Testing edge cases and error states

## Related Prompts

- [frontend_testing_jest.md](../testing/frontend_testing_jest.md) - Jest-specific patterns
- [frontend_testing_playwright.md](../testing/frontend_testing_playwright.md) - E2E testing
- [frontend_react_hooks_best_practices.md](frontend_react_hooks_best_practices.md) - Hook testing context

## Customization Guide

- **For Next.js**: Add server component testing, API route tests
- **For React Native**: Use @testing-library/react-native
- **For Vitest Migration**: Update config examples to Vitest syntax
- **For Enzyme Migration**: Add migration guide from Enzyme patterns

---
title: "Jest Testing Patterns for Frontend"
category: frontend-development/testing
description: "Comprehensive Jest testing patterns for frontend applications including mocking, async testing, and testing utilities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - testing
  - jest
  - unit-testing
  - mocking
  - async-testing
  - frontend
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/testing/frontend_testing_playwright.md
  - domain-frontend-development/react/frontend_react_testing.md
  - domain-frontend-development/vue/frontend_vue_testing.md
---

# Jest Testing Patterns for Frontend

**Objective:** Design and implement effective Jest testing patterns for frontend applications, covering unit tests, mocking strategies, async testing, and test organization best practices.

**When to Use:**
- Use when: Setting up Jest testing for a frontend project
- Use when: Debugging flaky or slow Jest tests
- Use when: Improving test coverage and reliability
- Use when: Establishing testing standards for a team
- Don't use when: E2E testing needed (use Playwright/Cypress)

## Instructions

1. **Configure Jest Properly**
   - Set up appropriate transforms (TypeScript, JSX)
   - Configure module resolution and aliases
   - Set up test environment (jsdom, node)
   - Configure coverage thresholds

2. **Design Mocking Strategy**
   - Mock external dependencies (APIs, storage)
   - Use appropriate mock types (auto, manual, inline)
   - Create reusable mock factories
   - Know when not to mock

3. **Handle Async Testing**
   - Use async/await patterns correctly
   - Handle promises and timers
   - Avoid test pollution from async operations
   - Set up proper cleanup

4. **Organize Test Files**
   - Co-locate tests with source files
   - Create shared test utilities
   - Maintain test data fixtures
   - Use descriptive test names

5. **CRITICAL: Validate Tests Are Effective**
   - Tests should fail when code breaks
   - Avoid testing implementation details
   - Keep tests maintainable
   - **Confidence level** for test coverage:
     - **High Confidence**: Tests catch real bugs
     - **Medium Confidence**: Tests verify behavior
     - **Low Confidence**: Tests exist but may not catch issues

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Mock the thing you're testing
- Test private implementation details
- Write tests that never fail
- Create tight coupling to component internals
- Ignore flaky tests (fix them)
- Over-mock to the point tests don't test reality

✅ **DO:**
- Test public API and behavior
- Mock only external dependencies
- Keep tests independent and isolated
- Use meaningful assertions
- Clean up after each test
- Write tests that fail when code breaks

## Expected Output

Jest testing guide including:
- Jest configuration recommendations
- Mocking patterns and examples
- Async testing patterns
- Test organization strategy
- Common patterns and anti-patterns

## Example Output

```markdown
## Jest Testing Patterns Guide

### Jest Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',

  // Transform TypeScript and JSX
  transform: {
    '^.+\\.(ts|tsx)$': ['ts-jest', {
      tsconfig: 'tsconfig.json',
      useESM: true,
    }],
  },

  // Module resolution
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '\\.(jpg|jpeg|png|gif|svg)$': '<rootDir>/__mocks__/fileMock.js',
  },

  // Setup files
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],

  // Coverage configuration
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.stories.tsx',
    '!src/index.tsx',
  ],
  coverageThreshold: {
    global: {
      branches: 70,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },

  // Test patterns
  testMatch: ['**/__tests__/**/*.[jt]s?(x)', '**/?(*.)+(spec|test).[jt]s?(x)'],

  // Performance
  maxWorkers: '50%',
  testTimeout: 10000,
};
```

```javascript
// jest.setup.js
import '@testing-library/jest-dom';

// Global mocks
global.fetch = jest.fn();
global.IntersectionObserver = jest.fn(() => ({
  observe: jest.fn(),
  unobserve: jest.fn(),
  disconnect: jest.fn(),
}));

// Cleanup
afterEach(() => {
  jest.clearAllMocks();
  jest.restoreAllMocks();
});
```

---

### Mocking Patterns

#### Pattern 1: Mocking Modules

```javascript
// Mock entire module
jest.mock('@/services/api', () => ({
  getUser: jest.fn(),
  updateUser: jest.fn(),
}));

// Mock specific functions
jest.mock('@/utils/storage', () => ({
  ...jest.requireActual('@/utils/storage'),
  getItem: jest.fn(),
}));

// Usage in test
import { getUser } from '@/services/api';

test('fetches user', async () => {
  (getUser as jest.Mock).mockResolvedValue({ id: '1', name: 'John' });

  const result = await getUser('1');

  expect(result).toEqual({ id: '1', name: 'John' });
  expect(getUser).toHaveBeenCalledWith('1');
});
```

#### Pattern 2: Manual Mocks

```javascript
// __mocks__/axios.js
export default {
  get: jest.fn(() => Promise.resolve({ data: {} })),
  post: jest.fn(() => Promise.resolve({ data: {} })),
  create: jest.fn(() => ({
    get: jest.fn(() => Promise.resolve({ data: {} })),
    post: jest.fn(() => Promise.resolve({ data: {} })),
    interceptors: {
      request: { use: jest.fn() },
      response: { use: jest.fn() },
    },
  })),
};

// Usage - automatically used
import axios from 'axios';

test('uses mocked axios', () => {
  expect(jest.isMockFunction(axios.get)).toBe(true);
});
```

#### Pattern 3: Mock Factories

```javascript
// test-utils/mocks.ts
export function createMockUser(overrides = {}) {
  return {
    id: 'user-1',
    email: 'test@example.com',
    name: 'Test User',
    role: 'user',
    createdAt: new Date('2024-01-01'),
    ...overrides,
  };
}

export function createMockApiResponse<T>(data: T, overrides = {}) {
  return {
    data,
    status: 200,
    statusText: 'OK',
    headers: {},
    config: {},
    ...overrides,
  };
}

// Usage
const user = createMockUser({ role: 'admin' });
const response = createMockApiResponse({ users: [user] });
```

#### Pattern 4: Mocking Fetch

```javascript
// Simple fetch mock
global.fetch = jest.fn();

beforeEach(() => {
  (fetch as jest.Mock).mockClear();
});

test('calls API correctly', async () => {
  (fetch as jest.Mock).mockResolvedValueOnce({
    ok: true,
    json: () => Promise.resolve({ data: 'test' }),
  });

  const result = await fetchData('/api/data');

  expect(fetch).toHaveBeenCalledWith('/api/data', expect.any(Object));
  expect(result).toEqual({ data: 'test' });
});

// Mock failure
test('handles API error', async () => {
  (fetch as jest.Mock).mockResolvedValueOnce({
    ok: false,
    status: 500,
    statusText: 'Server Error',
  });

  await expect(fetchData('/api/data')).rejects.toThrow('Server Error');
});
```

#### Pattern 5: Mocking Timers

```javascript
describe('with fake timers', () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  test('debounces calls', () => {
    const callback = jest.fn();
    const debounced = debounce(callback, 300);

    debounced();
    debounced();
    debounced();

    expect(callback).not.toHaveBeenCalled();

    jest.advanceTimersByTime(300);

    expect(callback).toHaveBeenCalledTimes(1);
  });

  test('handles setTimeout', async () => {
    const callback = jest.fn();

    setTimeout(callback, 1000);

    expect(callback).not.toHaveBeenCalled();

    jest.runAllTimers();

    expect(callback).toHaveBeenCalled();
  });

  test('with async and timers', async () => {
    const promise = delay(1000).then(() => 'done');

    // Advance timers
    jest.advanceTimersByTime(1000);

    // Now await the promise
    const result = await promise;
    expect(result).toBe('done');
  });
});
```

---

### Async Testing Patterns

#### Pattern 1: Testing Promises

```javascript
// ✅ Best: async/await
test('fetches data', async () => {
  const data = await fetchData();
  expect(data).toEqual({ value: 42 });
});

// ✅ Good: resolves/rejects matchers
test('fetches data with matcher', async () => {
  await expect(fetchData()).resolves.toEqual({ value: 42 });
});

test('handles errors with matcher', async () => {
  await expect(failingFetch()).rejects.toThrow('Network error');
});

// ⚠️ Avoid: .then chains (harder to read)
test('with then chain', () => {
  return fetchData().then(data => {
    expect(data).toEqual({ value: 42 });
  });
});
```

#### Pattern 2: Testing Callbacks

```javascript
// Using done callback (legacy pattern)
test('calls callback', (done) => {
  function callback(data) {
    try {
      expect(data).toBe('result');
      done();
    } catch (error) {
      done(error);
    }
  }

  asyncOperation(callback);
});

// Better: Promisify and use async
test('calls callback (promisified)', async () => {
  const result = await new Promise((resolve) => {
    asyncOperation(resolve);
  });

  expect(result).toBe('result');
});
```

#### Pattern 3: waitFor Patterns

```javascript
import { waitFor } from '@testing-library/react';

test('waits for condition', async () => {
  startAsyncOperation();

  await waitFor(() => {
    expect(getResult()).toBe('completed');
  });
});

// With timeout
await waitFor(
  () => {
    expect(element).toBeVisible();
  },
  { timeout: 5000 }
);

// Don't use arbitrary delays
// ❌ Bad
await new Promise(r => setTimeout(r, 1000));
expect(result).toBe('done');

// ✅ Good
await waitFor(() => expect(result).toBe('done'));
```

#### Pattern 4: Testing Event Handlers

```javascript
test('handles async event', async () => {
  const onSubmit = jest.fn().mockResolvedValue({ success: true });

  render(<Form onSubmit={onSubmit} />);

  await userEvent.type(screen.getByLabelText('Name'), 'John');
  await userEvent.click(screen.getByRole('button', { name: 'Submit' }));

  await waitFor(() => {
    expect(onSubmit).toHaveBeenCalledWith({ name: 'John' });
  });
});
```

---

### Test Organization

#### File Structure

```
src/
├── components/
│   └── Button/
│       ├── Button.tsx
│       ├── Button.test.tsx       # Component tests
│       └── Button.stories.tsx    # Storybook
├── hooks/
│   └── useAuth/
│       ├── useAuth.ts
│       └── useAuth.test.ts       # Hook tests
├── services/
│   └── api/
│       ├── api.ts
│       └── api.test.ts           # Service tests
└── __tests__/
    └── integration/
        └── auth-flow.test.tsx    # Integration tests
```

#### Describe Block Organization

```javascript
describe('UserService', () => {
  // Setup shared across all tests
  let service: UserService;

  beforeEach(() => {
    service = new UserService();
    jest.clearAllMocks();
  });

  describe('getUser', () => {
    test('returns user when found', async () => {
      // ...
    });

    test('throws when user not found', async () => {
      // ...
    });

    test('handles network errors', async () => {
      // ...
    });
  });

  describe('createUser', () => {
    test('creates user with valid data', async () => {
      // ...
    });

    test('validates required fields', async () => {
      // ...
    });
  });
});
```

#### Naming Conventions

```javascript
// ✅ Good: Behavior-focused names
test('displays error message when login fails', () => {});
test('redirects to dashboard after successful login', () => {});
test('disables submit button while loading', () => {});

// ❌ Bad: Implementation-focused names
test('sets error state to true', () => {});
test('calls navigate function', () => {});
test('sets isLoading to true', () => {});
```

---

### Common Patterns

#### Pattern: Testing Error States

```javascript
describe('error handling', () => {
  test('displays error message', async () => {
    // Arrange
    (api.getUser as jest.Mock).mockRejectedValue(new Error('Not found'));

    // Act
    render(<UserProfile userId="123" />);

    // Assert
    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Not found');
    });
  });

  test('allows retry after error', async () => {
    // First call fails
    (api.getUser as jest.Mock)
      .mockRejectedValueOnce(new Error('Network error'))
      .mockResolvedValueOnce({ id: '123', name: 'John' });

    render(<UserProfile userId="123" />);

    // Wait for error
    await screen.findByRole('alert');

    // Click retry
    await userEvent.click(screen.getByRole('button', { name: 'Retry' }));

    // Should show user now
    await waitFor(() => {
      expect(screen.getByText('John')).toBeInTheDocument();
    });
  });
});
```

#### Pattern: Testing Loading States

```javascript
test('shows loading state', async () => {
  // Create a promise we control
  let resolveGetUser: (value: User) => void;
  const getUserPromise = new Promise<User>((resolve) => {
    resolveGetUser = resolve;
  });

  (api.getUser as jest.Mock).mockReturnValue(getUserPromise);

  render(<UserProfile userId="123" />);

  // Should show loading
  expect(screen.getByRole('status')).toHaveTextContent('Loading');

  // Resolve the promise
  resolveGetUser!({ id: '123', name: 'John' });

  // Should show content
  await waitFor(() => {
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
    expect(screen.getByText('John')).toBeInTheDocument();
  });
});
```

#### Pattern: Testing Forms

```javascript
describe('LoginForm', () => {
  test('submits with valid data', async () => {
    const onSubmit = jest.fn();
    render(<LoginForm onSubmit={onSubmit} />);

    await userEvent.type(screen.getByLabelText('Email'), 'test@example.com');
    await userEvent.type(screen.getByLabelText('Password'), 'password123');
    await userEvent.click(screen.getByRole('button', { name: 'Login' }));

    expect(onSubmit).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123',
    });
  });

  test('shows validation errors', async () => {
    render(<LoginForm onSubmit={jest.fn()} />);

    await userEvent.click(screen.getByRole('button', { name: 'Login' }));

    expect(screen.getByText('Email is required')).toBeInTheDocument();
    expect(screen.getByText('Password is required')).toBeInTheDocument();
  });

  test('clears errors on input', async () => {
    render(<LoginForm onSubmit={jest.fn()} />);

    // Submit to trigger errors
    await userEvent.click(screen.getByRole('button', { name: 'Login' }));
    expect(screen.getByText('Email is required')).toBeInTheDocument();

    // Type to clear error
    await userEvent.type(screen.getByLabelText('Email'), 'test@example.com');
    expect(screen.queryByText('Email is required')).not.toBeInTheDocument();
  });
});
```

---

### Anti-Patterns to Avoid

#### Anti-Pattern 1: Testing Implementation Details

```javascript
// ❌ Bad: Testing internal state
test('sets loading to true', () => {
  const { result } = renderHook(() => useState(false));
  // Don't access internal state
});

// ✅ Good: Testing observable behavior
test('shows loading indicator', () => {
  render(<Component />);
  expect(screen.getByRole('status')).toBeInTheDocument();
});
```

#### Anti-Pattern 2: Snapshot Everything

```javascript
// ❌ Bad: Large, brittle snapshots
test('renders correctly', () => {
  const { container } = render(<ComplexComponent />);
  expect(container).toMatchSnapshot();
});

// ✅ Good: Specific assertions
test('renders user name and email', () => {
  render(<UserCard user={mockUser} />);
  expect(screen.getByText('John Doe')).toBeInTheDocument();
  expect(screen.getByText('john@example.com')).toBeInTheDocument();
});
```

#### Anti-Pattern 3: Not Cleaning Up

```javascript
// ❌ Bad: No cleanup
test('first test', () => {
  window.specialProperty = 'test';
  // ... test
});

test('second test', () => {
  // specialProperty still exists! Test pollution.
});

// ✅ Good: Proper cleanup
afterEach(() => {
  delete window.specialProperty;
  jest.clearAllMocks();
  jest.restoreAllMocks();
});
```

#### Anti-Pattern 4: Testing Third-Party Code

```javascript
// ❌ Bad: Testing library behavior
test('axios makes GET request', async () => {
  const response = await axios.get('/api/data');
  expect(response.data).toBeDefined();
});

// ✅ Good: Testing YOUR code that uses the library
test('fetches user data', async () => {
  (axios.get as jest.Mock).mockResolvedValue({ data: mockUser });

  const user = await userService.getUser('123');

  expect(user).toEqual(mockUser);
  expect(axios.get).toHaveBeenCalledWith('/api/users/123');
});
```

---

### Performance Tips

```javascript
// Use describe.each for similar tests
describe.each([
  { role: 'admin', canDelete: true },
  { role: 'user', canDelete: false },
  { role: 'guest', canDelete: false },
])('user with role $role', ({ role, canDelete }) => {
  test(`${canDelete ? 'can' : 'cannot'} delete items`, () => {
    const user = createMockUser({ role });
    expect(user.canDelete()).toBe(canDelete);
  });
});

// Use test.each for data-driven tests
test.each([
  ['hello', 'HELLO'],
  ['world', 'WORLD'],
  ['Test', 'TEST'],
])('toUpperCase(%s) returns %s', (input, expected) => {
  expect(toUpperCase(input)).toBe(expected);
});

// Skip slow tests in CI
const itSlowly = process.env.CI ? it.skip : it;
itSlowly('runs slow integration test', async () => {
  // ...
});
```
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Jest patterns
- **ST-02 (Structured Sequential Instructions):** Pattern-by-pattern guide
- **RT-02 (Multi-Dimensional Analysis):** Mocking, async, organization
- **OC-01 (Output Format Templates):** Clear code examples
- **QA-02 (Adversarial Stress-Test):** Anti-patterns highlighted

## Related Prompts

- [frontend_testing_playwright.md](frontend_testing_playwright.md) - E2E testing
- [frontend_react_testing.md](../react/frontend_react_testing.md) - React-specific
- [frontend_vue_testing.md](../vue/frontend_vue_testing.md) - Vue-specific

## Customization Guide

- **For Vitest**: Adjust configuration to Vitest syntax (mostly compatible)
- **For TypeScript**: Ensure ts-jest configuration is correct
- **For Monorepos**: Configure projects array for multi-package testing
- **For Legacy Code**: Start with integration tests, add unit tests gradually

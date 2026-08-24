---
name: javascript-testing-patterns
description: Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing with mocking, fixtures, and test-driven development. Use when writing JavaScript/TypeScript tests, setting up test infrastructure, or implementing TDD/BDD workflows.
metadata:
  tags:
    - javascript
    - jest
    - programming-languages
    - testing
    - typescript
    - vitest
  updated: "2026-04-11"
---
# JavaScript Testing Patterns

Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices.

## When to Use This Skill

- Setting up test infrastructure for new projects
- Writing unit tests for functions and classes
- Creating integration tests for APIs and services
- Implementing end-to-end tests for user flows
- Mocking external dependencies and APIs
- Testing React, Vue, or other frontend components
- Implementing test-driven development (TDD)
- Setting up continuous testing in CI/CD pipelines

## Testing Frameworks

### Jest - Full-Featured Testing Framework

**Setup:**
```typescript
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.interface.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  setupFilesAfterEnv: ['<rootDir>/src/test/setup.ts'],
};

export default config;
```

### Vitest - Fast, Vite-Native Testing

**Setup:**
```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['**/*.d.ts', '**/*.config.ts', '**/dist/**'],
    },
    setupFiles: ['./src/test/setup.ts'],
  },
});
```

## Unit Testing Patterns

### Pattern 1: Testing Pure Functions

```typescript
// utils/calculator.ts
export function add(a: number, b: number): number {
  return a + b;
}

export function divide(a: number, b: number): number {
  if (b === 0) {
    throw new Error('Division by zero');
  }
  return a / b;
}

// utils/calculator.test.ts
import { describe, it, expect } from 'vitest';
import { add, divide } from './calculator';

describe('Calculator', () => {
  describe('add', () => {
    it('should add two positive numbers', () => {
      expect(add(2, 3)).toBe(5);
    });

    it('should add negative numbers', () => {
      expect(add(-2, -3)).toBe(-5);
    });

    it('should handle zero', () => {
      expect(add(0, 5)).toBe(5);
      expect(add(5, 0)).toBe(5);
    });
  });

  describe('divide', () => {
    it('should divide two numbers', () => {
      expect(divide(10, 2)).toBe(5);
    });

    it('should handle decimal results', () => {
      expect(divide(5, 2)).toBe(2.5);
    });

    it('should throw error when dividing by zero', () => {
      expect(() => divide(10, 0)).toThrow('Division by zero');
    });
  });
});
```

### Pattern 2: Testing Classes

```typescript
// services/user.service.ts
export class UserService {
  private users: Map<string, User> = new Map();

  create(user: User): User {
    if (this.users.has(user.id)) {
      throw new Error('User already exists');
    }
    this.users.set(user.id, user);
    return user;
  }

  findById(id: string): User | undefined {
    return this.users.get(id);
  }

  update(id: string, updates: Partial<User>): User {
    const user = this.users.get(id);
    if (!user) {
      throw new Error('User not found');
    }
    const updated = { ...user, ...updates };
    this.users.set(id, updated);
    return updated;
  }

  delete(id: string): boolean {
    return this.users.delete(id);
  }
}

// services/user.service.test.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { UserService } from './user.service';

describe('UserService', () => {
  let service: UserService;

  beforeEach(() => {
    service = new UserService();
  });

  describe('create', () => {
    it('should create a new user', () => {
      const user = { id: '1', name: 'John', email: 'john@example.com' };
      const created = service.create(user);

      expect(created).toEqual(user);
      expect(service.findById('1')).toEqual(user);
    });

    it('should throw error if user already exists', () => {
      const user = { id: '1', name: 'John', email: 'john@example.com' };
      service.create(user);

      expect(() => service.create(user)).toThrow('User already exists');
    });
  });

  describe('update', () => {
    it('should update existing user', () => {
      const user = { id: '1', name: 'John', email: 'john@example.com' };
      service.create(user);

      const updated = service.update('1', { name: 'Jane' });

      expect(updated.name).toBe('Jane');
      expect(updated.email).toBe('john@example.com');
    });

    it('should throw error if user not found', () => {
      expect(() => service.update('999', { name: 'Jane' }))
        .toThrow('User not found');
    });
  });
});
```

### Pattern 3: Testing Async Functions

```typescript
// services/api.service.ts
export class ApiService {
  async fetchUser(id: string): Promise<User> {
    const response = await fetch(`https://api.example.com/users/${id}`);
    if (!response.ok) {
      throw new Error('User not found');
    }
    return response.json();
  }

  async createUser(user: CreateUserDTO): Promise<User> {
    const response = await fetch('https://api.example.com/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(user),
    });
    return response.json();
  }
}

// services/api.service.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { ApiService } from './api.service';

// Mock fetch globally
global.fetch = vi.fn();

describe('ApiService', () => {
  let service: ApiService;

  beforeEach(() => {
    service = new ApiService();
    vi.clearAllMocks();
  });

  describe('fetchUser', () => {
    it('should fetch user successfully', async () => {
      const mockUser = { id: '1', name: 'John', email: 'john@example.com' };

      (fetch as any).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUser,
      });

      const user = await service.fetchUser('1');

      expect(user).toEqual(mockUser);
      expect(fetch).toHaveBeenCalledWith('https://api.example.com/users/1');
    });

    it('should throw error if user not found', async () => {
      (fetch as any).mockResolvedValueOnce({
        ok: false,
      });

      await expect(service.fetchUser('999')).rejects.toThrow('User not found');
    });
  });

  describe('createUser', () => {
    it('should create user successfully', async () => {
      const newUser = { name: 'John', email: 'john@example.com' };
      const createdUser = { id: '1', ...newUser };

      (fetch as any).mockResolvedValueOnce({
        ok: true,
        json: async () => createdUser,
      });

      const user = await service.createUser(newUser);

      expect(user).toEqual(createdUser);
      expect(fetch).toHaveBeenCalledWith(
        'https://api.example.com/users',
        expect.objectContaining({
          method: 'POST',
          body: JSON.stringify(newUser),
        })
      );
    });
  });
});
```

## Mocking Patterns

Module mocking, dependency injection for testability, and function spying. Includes patterns for nodemailer, repository interfaces, and logger spies.

See [references/mocking-patterns.md](references/mocking-patterns.md)

## Integration Testing and Frontend Testing

API integration tests with supertest, database repository integration tests with PostgreSQL, React component testing with Testing Library, and custom hook testing with `renderHook`.

See [references/integration-and-frontend-testing.md](references/integration-and-frontend-testing.md)

## Test Fixtures and Factories

```typescript
// tests/fixtures/user.fixture.ts
import { faker } from '@faker-js/faker';

export function createUserFixture(overrides?: Partial<User>): User {
  return {
    id: faker.string.uuid(),
    name: faker.person.fullName(),
    email: faker.internet.email(),
    createdAt: faker.date.past(),
    ...overrides,
  };
}

export function createUsersFixture(count: number): User[] {
  return Array.from({ length: count }, () => createUserFixture());
}

// Usage in tests
import { createUserFixture, createUsersFixture } from '../fixtures/user.fixture';

describe('UserService', () => {
  it('should process user', () => {
    const user = createUserFixture({ name: 'John Doe' });
    // Use user in test
  });

  it('should handle multiple users', () => {
    const users = createUsersFixture(10);
    // Use users in test
  });
});
```

## Snapshot Testing

```typescript
// components/UserCard.test.tsx
import { render } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { UserCard } from './UserCard';

describe('UserCard', () => {
  it('should match snapshot', () => {
    const user = {
      id: '1',
      name: 'John Doe',
      email: 'john@example.com',
      avatar: 'https://example.com/avatar.jpg',
    };

    const { container } = render(<UserCard user={user} />);

    expect(container.firstChild).toMatchSnapshot();
  });

  it('should match snapshot with loading state', () => {
    const { container } = render(<UserCard loading />);
    expect(container.firstChild).toMatchSnapshot();
  });
});
```

## Coverage Reports

```typescript
// package.json
{
  "scripts": {
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "test:ui": "vitest --ui"
  }
}
```

## Best Practices

1. **Follow AAA Pattern**: Arrange, Act, Assert
2. **One assertion per test**: Or logically related assertions
3. **Descriptive test names**: Should describe what is being tested
4. **Use beforeEach/afterEach**: For setup and teardown
5. **Mock external dependencies**: Keep tests isolated
6. **Test edge cases**: Not just happy paths
7. **Avoid implementation details**: Test behavior, not implementation
8. **Use test factories**: For consistent test data
9. **Keep tests fast**: Mock slow operations
10. **Write tests first (TDD)**: When possible
11. **Maintain test coverage**: Aim for 80%+ coverage
12. **Use TypeScript**: For type-safe tests
13. **Test error handling**: Not just success cases
14. **Use data-testid sparingly**: Prefer semantic queries
15. **Clean up after tests**: Prevent test pollution

## Common Patterns

### Test Organization

```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user successfully', () => {});
    it('should throw error if email exists', () => {});
    it('should hash password', () => {});
  });

  describe('updateUser', () => {
    it('should update user', () => {});
    it('should throw error if not found', () => {});
  });
});
```

### Testing Promises

```typescript
// Using async/await
it('should fetch user', async () => {
  const user = await service.fetchUser('1');
  expect(user).toBeDefined();
});

// Testing rejections
it('should throw error', async () => {
  await expect(service.fetchUser('invalid')).rejects.toThrow('Not found');
});
```

### Testing Timers

```typescript
import { vi } from 'vitest';

it('should call function after delay', () => {
  vi.useFakeTimers();

  const callback = vi.fn();
  setTimeout(callback, 1000);

  expect(callback).not.toHaveBeenCalled();

  vi.advanceTimersByTime(1000);

  expect(callback).toHaveBeenCalled();

  vi.useRealTimers();
});
```

## Resources

- **Jest Documentation**: https://jestjs.io/
- **Vitest Documentation**: https://vitest.dev/
- **Testing Library**: https://testing-library.com/
- **Kent C. Dodds Testing Blog**: https://kentcdodds.com/blog/

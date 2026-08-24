---
title: "Test Data Generation and Management"
category: testing
description: "Generate realistic test data covering edge cases while maintaining privacy compliance"
techniques:
  - ST-01
  - ST-02
  - DT-01
  - RT-02
  - QA-02
difficulty: intermediate
tags:
  - testing
  - test-data
  - fixtures
  - mocking
  - data-generation
updated: "2026-01-25"
---

# Test Data Generation and Management

**Objective:** Generate realistic, comprehensive test data that covers edge cases, boundary conditions, and real-world scenarios while maintaining data integrity, consistency, and privacy compliance.

**When to Use:** Use this prompt when creating test fixtures for unit/integration tests, generating mock API responses, building seed data for development environments, creating realistic datasets for performance testing, or anonymizing production data for testing purposes.

**Instructions:**

1. **Analyze Data Requirements**
   Understand the data needs:
   - Data models and schemas involved
   - Relationships between entities (one-to-many, many-to-many)
   - Required fields vs optional fields
   - Data types and constraints (enums, ranges, formats)
   - Business rules affecting data validity
   - Volume requirements (single records vs bulk data)

2. **Identify Test Scenarios**
   Map data to test categories:
   - **Happy Path Data**: Valid, typical production-like records
   - **Edge Cases**: Boundary values, minimum/maximum lengths
   - **Invalid Data**: For negative testing (validation, error handling)
   - **Null/Empty Data**: Missing optional fields, empty strings
   - **Special Characters**: Unicode, emojis, SQL/HTML special chars
   - **Temporal Data**: Past, present, future dates; timezones

3. **Design Data Generation Strategy**
   Choose appropriate approach:
   - **Static Fixtures**: Predefined JSON/YAML for deterministic tests
   - **Factory Pattern**: Programmatic generation with defaults + overrides
   - **Faker Libraries**: Realistic random data (names, addresses, etc.)
   - **Seed Data**: Database population for development/staging
   - **Production Sampling**: Anonymized subsets of real data

4. **Implement Data Factories**
   Create reusable data generators:
   ```
   Factory should support:
   - Default values for all fields
   - Override mechanism for specific fields
   - Relationship building (nested objects)
   - Sequence generation for unique IDs
   - Trait system for common variations
   ```

5. **Handle Data Relationships**
   Maintain referential integrity:
   - Parent records created before children
   - Foreign keys reference valid existing records
   - Cascade considerations for deletion tests
   - Circular dependency handling

6. **Ensure Data Privacy**
   When using production-derived data:
   - Remove/mask PII (names, emails, SSNs, addresses)
   - Anonymize financial data
   - Preserve data distribution and patterns
   - Comply with GDPR/CCPA requirements

7. **Document Data Patterns**
   Create data dictionaries:
   - Field-level documentation
   - Valid value ranges and examples
   - Relationship diagrams
   - Test scenario mappings

8. **CRITICAL: Verify Test Data Quality Before Use**
   - Ensure generated data maintains referential integrity
   - Verify data meets all validation constraints
   - Check that anonymized data preserves necessary patterns
   - Confirm edge case data is actually edge case (not just unusual)
   - Validate that test data won't cause cascading failures

9. **For each test data set, document:**
   - Purpose and intended test scenarios
   - Data relationships and dependencies
   - **Confidence level** for data validity (High/Medium/Low)
   - Privacy compliance status
   - Known limitations or caveats

## False-Positive Prevention (MUST follow)

Test data issues can cause misleading test results. Follow these rules rigorously:

❌ **DON'T:**
- Generate data that violates business rules (tests will fail for wrong reasons)
- Use random data where deterministic data is needed (causes flaky tests)
- Create edge case data that's actually impossible in production
- Anonymize data in ways that destroy patterns needed for testing
- Generate related records without maintaining referential integrity
- Use test data with implicit assumptions about environment (timezones, locales)
- Create data that bypasses validation (unless explicitly testing validation bypass)
- Generate unrealistic data volumes that mask real performance issues

✅ **DO:**
- Validate generated data against the same rules as production
- Use seeded randomness for reproducible "random" test data
- Derive edge cases from actual production data patterns
- Preserve statistical distributions when anonymizing production data
- Build parent records before child records (maintain FK relationships)
- Make timezone and locale handling explicit in generated data
- Document which validations test data intentionally violates
- Generate realistic data volumes based on production metrics

## Confidence Levels for Test Data

Rate the reliability of each test data set:

- **High Confidence:** Data passes all validations, relationships are intact, represents realistic production scenarios
- **Medium Confidence:** Data is syntactically valid but may have edge cases not seen in production, needs review
- **Low Confidence:** Data is for specific test scenarios, may violate constraints, not suitable for general use

## Data Quality Validation Checklist

Before using generated test data:
- [ ] All required fields are populated with valid values
- [ ] Foreign key relationships point to existing records
- [ ] Date/time values are in valid ranges and formats
- [ ] Numeric values respect min/max constraints
- [ ] String lengths are within defined limits
- [ ] Enum values are from the allowed set
- [ ] Uniqueness constraints are satisfied
- [ ] Business rules are respected (or violations are intentional and documented)
- [ ] PII is properly anonymized (if using production-derived data)
- [ ] Data is reproducible (seeded randomness if needed)

## Common Test Data Pitfalls

| Pitfall | Symptom | Prevention |
|---------|---------|------------|
| Orphaned records | FK constraint failures | Build data bottom-up (parents first) |
| Invalid enums | Validation errors | Use actual enum values from schema |
| Future dates | Time-sensitive test failures | Use relative dates or mock time |
| Locale issues | Parsing errors in CI | Specify locale explicitly |
| Collision on unique fields | Duplicate key errors | Use sequences or UUIDs |
| Missing nullable handling | Null pointer errors | Include null cases in data sets |

**Expected Output:** A comprehensive test data generation strategy including:
- Data factory implementations for each domain model
- Static fixture files for critical test scenarios
- Seed data scripts for development environments
- Edge case data catalogs
- Privacy-compliant data anonymization approach
- Documentation of data patterns and relationships

**Example Output:**

```markdown
## Test Data Generation for E-Commerce Platform

**Domain Models:** User, Product, Order, Payment, Review

---

### 1. Data Factory Implementation (JavaScript/TypeScript)

```typescript
// tests/factories/userFactory.ts
import { faker } from '@faker-js/faker';
import { User, UserRole, UserStatus } from '../types';

interface UserOverrides {
  id?: string;
  email?: string;
  name?: string;
  role?: UserRole;
  status?: UserStatus;
  createdAt?: Date;
}

let userSequence = 0;

export function createUser(overrides: UserOverrides = {}): User {
  userSequence++;

  return {
    id: overrides.id ?? `user-${userSequence.toString().padStart(5, '0')}`,
    email: overrides.email ?? faker.internet.email(),
    name: overrides.name ?? faker.person.fullName(),
    role: overrides.role ?? 'customer',
    status: overrides.status ?? 'active',
    phone: faker.phone.number(),
    address: {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state({ abbreviated: true }),
      zipCode: faker.location.zipCode(),
      country: 'US'
    },
    createdAt: overrides.createdAt ?? faker.date.past({ years: 2 }),
    updatedAt: new Date(),
    preferences: {
      newsletter: faker.datatype.boolean(),
      notifications: faker.datatype.boolean()
    }
  };
}

// Trait-based variations
export const userTraits = {
  admin: (): UserOverrides => ({
    role: 'admin',
    email: faker.internet.email({ provider: 'company.com' })
  }),

  inactive: (): UserOverrides => ({
    status: 'inactive'
  }),

  newUser: (): UserOverrides => ({
    createdAt: faker.date.recent({ days: 7 })
  }),

  withLongName: (): UserOverrides => ({
    name: faker.lorem.words(10) // Test long name handling
  })
};

// Helper for creating multiple users
export function createUsers(count: number, overrides: UserOverrides = {}): User[] {
  return Array.from({ length: count }, () => createUser(overrides));
}

// Reset sequence between test suites
export function resetUserSequence(): void {
  userSequence = 0;
}
```

```typescript
// tests/factories/productFactory.ts
import { faker } from '@faker-js/faker';
import { Product, ProductCategory } from '../types';

const categories: ProductCategory[] = [
  'electronics', 'clothing', 'home', 'sports', 'books'
];

let productSequence = 0;

export function createProduct(overrides: Partial<Product> = {}): Product {
  productSequence++;
  const category = faker.helpers.arrayElement(categories);

  return {
    id: overrides.id ?? `prod-${productSequence.toString().padStart(6, '0')}`,
    sku: overrides.sku ?? faker.string.alphanumeric(10).toUpperCase(),
    name: overrides.name ?? faker.commerce.productName(),
    description: overrides.description ?? faker.commerce.productDescription(),
    category: overrides.category ?? category,
    price: overrides.price ?? parseFloat(faker.commerce.price({ min: 1, max: 1000 })),
    compareAtPrice: overrides.compareAtPrice ?? null,
    inventory: overrides.inventory ?? faker.number.int({ min: 0, max: 500 }),
    images: overrides.images ?? [
      faker.image.url({ width: 800, height: 800 }),
      faker.image.url({ width: 800, height: 800 })
    ],
    attributes: overrides.attributes ?? generateAttributesForCategory(category),
    status: overrides.status ?? 'active',
    createdAt: overrides.createdAt ?? faker.date.past({ years: 1 }),
    updatedAt: new Date()
  };
}

function generateAttributesForCategory(category: ProductCategory) {
  const attributeMap = {
    electronics: {
      brand: faker.company.name(),
      warranty: `${faker.number.int({ min: 1, max: 3 })} years`,
      voltage: '110V'
    },
    clothing: {
      size: faker.helpers.arrayElement(['XS', 'S', 'M', 'L', 'XL']),
      color: faker.color.human(),
      material: faker.helpers.arrayElement(['cotton', 'polyester', 'wool'])
    },
    home: {
      dimensions: `${faker.number.int({ min: 10, max: 100 })}x${faker.number.int({ min: 10, max: 100 })}cm`,
      weight: `${faker.number.float({ min: 0.1, max: 50 })}kg`
    },
    sports: {
      sport: faker.helpers.arrayElement(['running', 'cycling', 'swimming', 'gym']),
      level: faker.helpers.arrayElement(['beginner', 'intermediate', 'advanced'])
    },
    books: {
      author: faker.person.fullName(),
      isbn: faker.string.numeric(13),
      pages: faker.number.int({ min: 50, max: 1000 })
    }
  };

  return attributeMap[category] || {};
}

export const productTraits = {
  outOfStock: (): Partial<Product> => ({ inventory: 0 }),
  onSale: (): Partial<Product> => ({
    price: 79.99,
    compareAtPrice: 99.99
  }),
  expensive: (): Partial<Product> => ({
    price: faker.number.float({ min: 500, max: 5000 })
  }),
  draft: (): Partial<Product> => ({ status: 'draft' })
};
```

```typescript
// tests/factories/orderFactory.ts
import { faker } from '@faker-js/faker';
import { Order, OrderStatus, OrderItem } from '../types';
import { createUser } from './userFactory';
import { createProduct } from './productFactory';

let orderSequence = 0;

export function createOrder(overrides: Partial<Order> = {}): Order {
  orderSequence++;

  const user = overrides.userId ? { id: overrides.userId } : createUser();
  const items = overrides.items ?? createOrderItems(faker.number.int({ min: 1, max: 5 }));
  const subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const tax = subtotal * 0.08;
  const shipping = subtotal > 100 ? 0 : 9.99;

  return {
    id: overrides.id ?? `ord-${orderSequence.toString().padStart(8, '0')}`,
    orderNumber: overrides.orderNumber ?? `ORD-${Date.now()}-${faker.string.alphanumeric(4).toUpperCase()}`,
    userId: user.id,
    items,
    subtotal: overrides.subtotal ?? subtotal,
    tax: overrides.tax ?? tax,
    shipping: overrides.shipping ?? shipping,
    total: overrides.total ?? (subtotal + tax + shipping),
    status: overrides.status ?? 'pending',
    shippingAddress: overrides.shippingAddress ?? {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state({ abbreviated: true }),
      zipCode: faker.location.zipCode(),
      country: 'US'
    },
    paymentMethod: overrides.paymentMethod ?? faker.helpers.arrayElement(['credit_card', 'paypal', 'apple_pay']),
    notes: overrides.notes ?? null,
    createdAt: overrides.createdAt ?? new Date(),
    updatedAt: new Date()
  };
}

export function createOrderItems(count: number): OrderItem[] {
  return Array.from({ length: count }, () => {
    const product = createProduct();
    const quantity = faker.number.int({ min: 1, max: 3 });

    return {
      productId: product.id,
      productName: product.name,
      sku: product.sku,
      price: product.price,
      quantity,
      total: product.price * quantity
    };
  });
}

export const orderTraits = {
  completed: (): Partial<Order> => ({
    status: 'delivered',
    createdAt: faker.date.past({ days: 30 })
  }),
  cancelled: (): Partial<Order> => ({
    status: 'cancelled',
    notes: 'Cancelled by customer'
  }),
  highValue: (): Partial<Order> => {
    const items = createOrderItems(5).map(item => ({
      ...item,
      price: faker.number.float({ min: 100, max: 500 }),
      total: item.price * item.quantity
    }));
    return { items };
  },
  international: (): Partial<Order> => ({
    shippingAddress: {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: '',
      zipCode: faker.location.zipCode(),
      country: faker.helpers.arrayElement(['CA', 'UK', 'DE', 'AU', 'JP'])
    },
    shipping: 29.99
  })
};
```

---

### 2. Static Fixture Files

```json
// tests/fixtures/users.json
{
  "validUsers": [
    {
      "id": "user-admin-001",
      "email": "admin@example.com",
      "name": "Admin User",
      "role": "admin",
      "status": "active"
    },
    {
      "id": "user-customer-001",
      "email": "john.doe@example.com",
      "name": "John Doe",
      "role": "customer",
      "status": "active"
    }
  ],
  "edgeCases": {
    "longEmail": {
      "email": "very.long.email.address.that.is.exactly.at.the.maximum.allowed.length@subdomain.example.com"
    },
    "unicodeName": {
      "name": "Jose Garcia"
    },
    "specialCharacters": {
      "name": "O'Brien-Smith"
    },
    "emojiInName": {
      "name": "Test User"
    },
    "minimalFields": {
      "email": "a@b.co",
      "name": "A"
    }
  },
  "invalidUsers": {
    "missingEmail": {
      "name": "No Email User"
    },
    "invalidEmailFormat": {
      "email": "not-an-email",
      "name": "Invalid Email"
    },
    "emptyName": {
      "email": "empty@example.com",
      "name": ""
    },
    "sqlInjection": {
      "email": "test@example.com",
      "name": "'; DROP TABLE users; --"
    },
    "xssAttempt": {
      "email": "xss@example.com",
      "name": "<script>alert('xss')</script>"
    }
  }
}
```

```yaml
# tests/fixtures/products.yaml
validProducts:
  - id: prod-001
    name: "Wireless Bluetooth Headphones"
    sku: "WBH-001"
    price: 79.99
    inventory: 150
    category: electronics

  - id: prod-002
    name: "Cotton T-Shirt"
    sku: "CTS-002"
    price: 24.99
    inventory: 500
    category: clothing

edgeCases:
  zeroPrice:
    price: 0
    name: "Free Sample Product"

  maxPrice:
    price: 999999.99
    name: "Luxury Item"

  longDescription:
    description: |
      This is a very long product description that tests the handling
      of extended text content. It includes multiple paragraphs and
      various formatting to ensure the system handles large text fields
      correctly without truncation or display issues.

  specialCharactersSku:
    sku: "PROD-2024/001-A"

  unicodeName:
    name: "Japanese Product Name"

  maxInventory:
    inventory: 2147483647  # Max INT32

boundaryValues:
  - { price: 0.01, name: "Minimum price" }
  - { price: 0.001, name: "Below minimum precision" }
  - { inventory: 0, name: "Out of stock" }
  - { inventory: -1, name: "Invalid negative inventory" }
```

---

### 3. Edge Case Test Data Catalog

```typescript
// tests/data/edgeCases.ts

export const stringEdgeCases = {
  empty: '',
  whitespace: '   ',
  singleChar: 'a',
  maxLength255: 'a'.repeat(255),
  overMaxLength: 'a'.repeat(256),
  unicodeBasic: 'Cafe Muller',
  unicodeExtended: 'Product Name in Chinese Characters',
  rtlText: 'Arabic Text Example',
  emojiBasic: 'Product with emoji',
  emojiComplex: 'Multiple Emojis Here',
  newlines: 'Line 1\nLine 2\nLine 3',
  tabs: 'Column1\tColumn2\tColumn3',
  htmlTags: '<b>Bold</b> and <i>italic</i>',
  sqlInjection: "'; DROP TABLE products; --",
  xssScript: '<script>alert("xss")</script>',
  nullByte: 'text\x00with\x00nulls',
  backslashes: 'path\\to\\file',
  quotes: 'He said "Hello" and \'Goodbye\''
};

export const numberEdgeCases = {
  zero: 0,
  negative: -1,
  negativeDecimal: -0.01,
  minInt: Number.MIN_SAFE_INTEGER,
  maxInt: Number.MAX_SAFE_INTEGER,
  minFloat: Number.MIN_VALUE,
  maxFloat: Number.MAX_VALUE,
  infinity: Infinity,
  negativeInfinity: -Infinity,
  nan: NaN,
  decimalPrecision: 0.1 + 0.2, // 0.30000000000000004
  scientificNotation: 1e10,
  leadingZeros: 0.001
};

export const dateEdgeCases = {
  epoch: new Date(0),
  y2k: new Date('2000-01-01'),
  leapYear: new Date('2024-02-29'),
  endOfYear: new Date('2024-12-31T23:59:59.999Z'),
  futureDate: new Date('2099-12-31'),
  pastDate: new Date('1900-01-01'),
  dstTransition: new Date('2024-03-10T02:30:00'), // Spring forward
  timezoneEdge: new Date('2024-01-01T00:00:00+14:00'), // Kiritimati
  invalidDate: new Date('invalid')
};

export const arrayEdgeCases = {
  empty: [],
  single: ['item'],
  large: Array.from({ length: 10000 }, (_, i) => `item-${i}`),
  nested: [[1, 2], [3, 4], [[5, 6]]],
  mixed: [1, 'two', null, undefined, { key: 'value' }],
  duplicates: ['a', 'a', 'a', 'b', 'b'],
  sparse: (() => { const arr = []; arr[100] = 'value'; return arr; })()
};

export const objectEdgeCases = {
  empty: {},
  deeplyNested: {
    level1: {
      level2: {
        level3: {
          level4: { value: 'deep' }
        }
      }
    }
  },
  circularRef: (() => {
    const obj: any = { name: 'circular' };
    obj.self = obj;
    return obj;
  })(),
  prototypeProperties: Object.create({ inherited: 'value' }),
  symbolKeys: { [Symbol('key')]: 'value' }
};
```

---

### 4. Database Seed Scripts

```typescript
// scripts/seed.ts
import { PrismaClient } from '@prisma/client';
import { createUser, createUsers, userTraits } from '../tests/factories/userFactory';
import { createProduct, productTraits } from '../tests/factories/productFactory';
import { createOrder, orderTraits } from '../tests/factories/orderFactory';

const prisma = new PrismaClient();

async function seed() {
  console.log('Seeding database...');

  // Clear existing data
  await prisma.orderItem.deleteMany();
  await prisma.order.deleteMany();
  await prisma.review.deleteMany();
  await prisma.product.deleteMany();
  await prisma.user.deleteMany();

  // Create admin users
  const admins = [
    createUser({ ...userTraits.admin(), email: 'admin@example.com', name: 'Admin User' }),
    createUser({ ...userTraits.admin(), email: 'support@example.com', name: 'Support Admin' })
  ];

  // Create regular users
  const customers = createUsers(50);

  // Create some inactive users
  const inactiveUsers = createUsers(10).map(u => ({
    ...u,
    ...userTraits.inactive()
  }));

  const allUsers = [...admins, ...customers, ...inactiveUsers];

  for (const user of allUsers) {
    await prisma.user.create({ data: user });
  }
  console.log(`Created ${allUsers.length} users`);

  // Create products across categories
  const products = [];
  for (let i = 0; i < 100; i++) {
    products.push(createProduct());
  }

  // Add some out of stock products
  for (let i = 0; i < 10; i++) {
    products.push(createProduct(productTraits.outOfStock()));
  }

  // Add sale products
  for (let i = 0; i < 20; i++) {
    products.push(createProduct(productTraits.onSale()));
  }

  for (const product of products) {
    await prisma.product.create({ data: product });
  }
  console.log(`Created ${products.length} products`);

  // Create orders for customers
  const orders = [];
  for (const customer of customers.slice(0, 30)) {
    // Each customer gets 1-5 orders
    const orderCount = Math.floor(Math.random() * 5) + 1;
    for (let i = 0; i < orderCount; i++) {
      orders.push(createOrder({
        userId: customer.id,
        ...orderTraits.completed()
      }));
    }
  }

  for (const order of orders) {
    const { items, ...orderData } = order;
    await prisma.order.create({
      data: {
        ...orderData,
        items: {
          create: items
        }
      }
    });
  }
  console.log(`Created ${orders.length} orders`);

  console.log('Seeding complete!');
}

seed()
  .catch(console.error)
  .finally(() => prisma.$disconnect());
```

---

### 5. Data Anonymization for Production Data

```typescript
// scripts/anonymize.ts
import { faker } from '@faker-js/faker';
import crypto from 'crypto';

interface AnonymizationRules {
  [fieldName: string]: 'hash' | 'fake' | 'mask' | 'nullify' | ((value: any) => any);
}

const userAnonymizationRules: AnonymizationRules = {
  email: (email: string) => {
    const [, domain] = email.split('@');
    return `user-${faker.string.alphanumeric(8)}@anonymized-${domain}`;
  },
  name: 'fake',
  phone: 'mask',
  ssn: 'nullify',
  address: (addr: any) => ({
    ...addr,
    street: faker.location.streetAddress(),
    city: faker.location.city()
  }),
  dateOfBirth: (dob: Date) => {
    // Preserve year for age-based analytics, randomize month/day
    const year = new Date(dob).getFullYear();
    return new Date(year, faker.number.int({ min: 0, max: 11 }), faker.number.int({ min: 1, max: 28 }));
  },
  creditCard: 'hash'
};

function anonymizeField(value: any, rule: AnonymizationRules[string]): any {
  if (value === null || value === undefined) return value;

  if (typeof rule === 'function') {
    return rule(value);
  }

  switch (rule) {
    case 'hash':
      return crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, 16);

    case 'fake':
      if (typeof value === 'string') {
        // Try to detect and replace with appropriate fake
        if (value.includes('@')) return faker.internet.email();
        if (/^\d{3}-\d{3}-\d{4}$/.test(value)) return faker.phone.number();
        return faker.person.fullName();
      }
      return value;

    case 'mask':
      if (typeof value === 'string') {
        if (value.length <= 4) return '*'.repeat(value.length);
        return value.slice(0, 2) + '*'.repeat(value.length - 4) + value.slice(-2);
      }
      return '****';

    case 'nullify':
      return null;

    default:
      return value;
  }
}

export function anonymizeRecord<T extends Record<string, any>>(
  record: T,
  rules: AnonymizationRules
): T {
  const anonymized = { ...record };

  for (const [field, rule] of Object.entries(rules)) {
    if (field in anonymized) {
      anonymized[field] = anonymizeField(anonymized[field], rule);
    }
  }

  return anonymized;
}

// Usage example
const productionUser = {
  id: 'user-12345',
  email: 'john.doe@company.com',
  name: 'John Doe',
  phone: '555-123-4567',
  ssn: '123-45-6789',
  address: {
    street: '123 Main St',
    city: 'New York',
    state: 'NY',
    zipCode: '10001'
  },
  dateOfBirth: new Date('1985-06-15'),
  creditCard: '4111111111111111'
};

const anonymizedUser = anonymizeRecord(productionUser, userAnonymizationRules);
// Result:
// {
//   id: 'user-12345', // IDs preserved for relationships
//   email: 'user-a8f3k2m1@anonymized-company.com',
//   name: 'Jane Smith', // Fake name
//   phone: '55*****67', // Masked
//   ssn: null, // Nullified sensitive data
//   address: { street: '456 Oak Ave', city: 'Chicago', ... },
//   dateOfBirth: '1985-03-22', // Year preserved
//   creditCard: 'a1b2c3d4e5f6g7h8' // Hashed
// }
```

---

### 6. Test Data Loading Utilities

```typescript
// tests/helpers/dataLoader.ts
import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

type FixtureFormat = 'json' | 'yaml' | 'csv';

export class TestDataLoader {
  private fixturesPath: string;
  private cache: Map<string, any> = new Map();

  constructor(fixturesPath: string = 'tests/fixtures') {
    this.fixturesPath = fixturesPath;
  }

  load<T>(filename: string, options: { cache?: boolean } = { cache: true }): T {
    if (options.cache && this.cache.has(filename)) {
      return this.cache.get(filename) as T;
    }

    const filePath = path.join(this.fixturesPath, filename);
    const ext = path.extname(filename).slice(1) as FixtureFormat;

    let data: T;

    switch (ext) {
      case 'json':
        data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        break;
      case 'yaml':
      case 'yml':
        data = yaml.load(fs.readFileSync(filePath, 'utf-8')) as T;
        break;
      default:
        throw new Error(`Unsupported fixture format: ${ext}`);
    }

    if (options.cache) {
      this.cache.set(filename, data);
    }

    return data;
  }

  clearCache(): void {
    this.cache.clear();
  }
}

// Usage in tests
const loader = new TestDataLoader();

describe('User API', () => {
  const fixtures = loader.load<UserFixtures>('users.json');

  it('should create valid user', async () => {
    const user = fixtures.validUsers[0];
    const response = await api.createUser(user);
    expect(response.status).toBe(201);
  });

  it('should reject invalid email', async () => {
    const user = fixtures.invalidUsers.invalidEmailFormat;
    const response = await api.createUser(user);
    expect(response.status).toBe(400);
  });
});
```

---

### Test Data Inventory Summary

| Data Set | Purpose | Records | Confidence | Privacy Status |
|----------|---------|---------|------------|----------------|
| users.json - validUsers | Happy path testing | 2 | High | Synthetic |
| users.json - edgeCases | Boundary validation | 5 | High | Synthetic |
| users.json - invalidUsers | Negative testing | 5 | High | Synthetic |
| products.yaml | Product CRUD tests | 15 | High | Synthetic |
| orderFactory | Dynamic order generation | N/A | High | Synthetic |
| anonymized_users | Performance testing | 10,000 | Medium | Anonymized Production |

### Data Generation Decision Matrix

| Scenario | Recommended Approach | Reason |
|----------|---------------------|--------|
| Unit test for validation | Static fixtures | Deterministic, readable |
| Integration test with DB | Factory pattern | Flexible, maintains relationships |
| Performance test | Seed script | Large volume, realistic distribution |
| Security test | Edge case catalog | Covers injection, XSS, etc. |
| Regression test | Production snapshot | Catches real-world issues |

### Test Data Quality Report

```
Data Quality Check Results:
═══════════════════════════════════════════════════════
✅ Referential Integrity: All FK relationships valid
✅ Required Fields: 100% populated
✅ Type Validation: All values match schema types
✅ Uniqueness: No duplicate keys detected
⚠️  Date Ranges: 3 records have dates > 1 year old
✅ Privacy Compliance: No PII in synthetic data sets
✅ Reproducibility: All factories use seeded random

Overall Confidence: HIGH
Ready for use in: Unit tests, Integration tests, E2E tests
Not recommended for: Performance benchmarking (use larger dataset)
═══════════════════════════════════════════════════════
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-04 (Comprehensive Example Outputs)
- DT-01 (Factory Pattern Implementation)
- QA-02 (Edge Case Coverage)

**Related Prompts:**
- testing_unit_test_generation.md - For writing tests that use generated data
- testing_integration_test_design.md - For integration tests requiring complex data setups
- testing_performance_load_test_planning.md - For generating high-volume test data
- testing_security_testing.md - For security-focused test data (injection payloads)
- database_comprehensive_analysis.md - For understanding data schemas

**Customization Guide:**
- **For API Testing**: Focus on JSON fixtures with request/response pairs
- **For Database Testing**: Emphasize seed scripts with relationship handling
- **For Performance Testing**: Generate large datasets with realistic distributions
- **For Security Testing**: Include injection payloads and malformed data
- **For Compliance Testing**: Add PII anonymization and data masking utilities
- **For Frontend Testing**: Create fixtures matching component prop interfaces

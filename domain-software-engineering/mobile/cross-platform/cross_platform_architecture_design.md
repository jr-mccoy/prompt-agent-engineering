---
title: "Cross-Platform Mobile Architecture Design"
category: mobile-development
description: "Analyzes and designs mobile architecture for cross-platform frameworks to maximize code sharing while maintaining platform-specific optimizations"
tags:
  - mobile-development
updated: "2026-03-19"
---

# Cross-Platform Mobile Architecture Design

**Objective:** Analyze and design mobile application architecture for cross-platform frameworks (React Native, Flutter, Xamarin, Ionic, etc.) to maximize code sharing, maintain platform-specific optimizations, ensure scalability, and establish clear boundaries between shared and platform-specific code.

**When to Use:** Use this prompt when planning a new cross-platform mobile app, evaluating framework selection, architecting code sharing strategies, migrating from native to cross-platform, or reviewing existing cross-platform architecture for optimization opportunities.

**Instructions:**

1. **Framework Selection and Justification:**
   * Evaluate the chosen cross-platform framework
   * Assess framework suitability for the project requirements
   * Compare framework capabilities:
     - **React Native:** JavaScript/TypeScript, large ecosystem, near-native performance
     - **Flutter:** Dart, custom rendering engine, excellent performance, growing ecosystem
     - **Xamarin:** C#, full native API access, enterprise-friendly
     - **Ionic/Capacitor:** Web technologies, hybrid approach, web code reuse
   * Review framework limitations and workarounds
   * Evaluate framework maturity and community support
   * Assess long-term viability and maintenance

2. **Code Sharing Strategy:**
   * Define code sharing boundaries (target: 70-90% shared code)
   * Identify shared business logic layer
   * Review platform-specific requirements:
     - Native UI components and interactions
     - Platform-specific APIs and features
     - Performance-critical native modules
     - Hardware integration (camera, sensors, NFC, etc.)
   * Evaluate abstraction layers for platform differences
   * Assess configuration management across platforms
   * Review shared vs. platform-specific assets

3. **Architecture Layers:**
   * **Presentation Layer:**
     - Shared UI components and screens
     - Platform-specific UI adaptations
     - Responsive design approach
     - Navigation structure
     - State management for UI
   * **Business Logic Layer:**
     - Use cases and business rules (100% shared target)
     - Validation logic
     - Business workflows
     - Domain models
   * **Data Layer:**
     - Repository pattern implementation
     - Data source abstraction (API, database, cache)
     - Data synchronization strategies
     - Offline-first capabilities
   * **Platform Bridge Layer:**
     - Native module interfaces
     - Platform-specific feature access
     - Third-party SDK integration
     - Device API abstraction

4. **State Management Architecture:**
   * Evaluate state management approach:
     - **React Native:** Redux, Zustand, MobX, Recoil, Context API
     - **Flutter:** Provider, Riverpod, Bloc, GetX, MobX
   * Review state scope and sharing:
     - Local component state
     - Screen/feature state
     - Global application state
     - Persistent state
   * Assess state synchronization across platforms
   * Evaluate state hydration and persistence
   * Review state management performance

5. **Navigation Architecture:**
   * Define navigation structure and patterns
   * **React Native:**
     - React Navigation implementation
     - Stack, Tab, Drawer navigation
     - Deep linking strategy
   * **Flutter:**
     - Navigator 2.0 or go_router
     - Declarative routing
     - Deep link handling
   * Review cross-platform navigation consistency
   * Evaluate platform-specific navigation patterns (iOS vs. Android)
   * Assess navigation state management

6. **Native Module Integration:**
   * Review native module architecture:
     - **React Native:** Native Modules, TurboModules, Fabric
     - **Flutter:** Platform Channels, Method Channels, FFI
   * Evaluate native module abstraction
   * Check for proper platform detection and conditional code
   * Assess performance of bridge communication
   * Review native module testing strategy
   * Evaluate native code maintainability

7. **Performance Optimization:**
   * Review rendering performance across platforms
   * Evaluate JavaScript/Dart thread performance
   * Assess list rendering optimization (virtualization)
   * Review image loading and caching strategies
   * Check for platform-specific performance optimizations
   * Evaluate app startup time
   * Review memory usage patterns
   * Assess battery consumption

8. **Platform-Specific Adaptations:**
   * Review Material Design (Android) vs. Cupertino (iOS) implementations
   * Evaluate platform-specific UI patterns:
     - Navigation bars vs. tab bars
     - Bottom sheets vs. action sheets
     - Back button handling
     - Gesture recognition differences
   * Check for platform-specific feature implementations:
     - Push notifications
     - Background tasks
     - App extensions / widgets
     - Share functionality
   * Review platform-specific permissions handling

9. **Testing Strategy:**
   * Define testing layers:
     - Unit tests (business logic - highly shareable)
     - Integration tests (data flow)
     - Widget/component tests
     - E2E tests (platform-specific)
   * Review test coverage goals (target: 80%+ for shared code)
   * Evaluate platform-specific testing:
     - iOS: XCTest, UI Testing
     - Android: Espresso, UI Automator
   * Assess cross-platform E2E testing (Detox, Maestro, Appium)
   * Review continuous testing integration

10. **Dependency Management:**
    * Review package/module management:
      - **React Native:** npm/yarn packages, native dependencies (CocoaPods, Gradle)
      - **Flutter:** pub packages, native plugin dependencies
    * Evaluate third-party library selection criteria
    * Check for platform-specific dependency versions
    * Assess dependency update strategy
    * Review mono-repo vs. multi-repo structure

11. **Build and Configuration:**
    * Review build configuration:
      - Development, staging, production environments
      - Platform-specific build configurations
      - Code signing and certificates
      - Build optimization (tree shaking, minification, obfuscation)
    * Evaluate environment variable management
    * Check for proper secret management in builds
    * Assess build automation and CI/CD integration

12. **Code Organization and Structure:**
    * Review project structure:
      ```
      /src
        /features          # Feature-based organization
          /authentication
            /data          # Data layer (API, storage)
            /domain        # Business logic
            /presentation  # UI components
        /shared            # Shared utilities and components
        /core              # Core app functionality
        /platform          # Platform-specific code
          /ios
          /android
      ```
    * Evaluate feature-based vs. layer-based organization
    * Check for clear separation of concerns
    * Assess code reusability and modularity
    * Review naming conventions and consistency

13. **Offline-First and Data Sync:**
    * Review offline capability implementation
    * Evaluate local data persistence (SQLite, Realm, Hive, etc.)
    * Assess data synchronization strategy
    * Check for conflict resolution mechanisms
    * Review cache invalidation patterns
    * Evaluate background sync capabilities

14. **Developer Experience:**
    * Review development workflow efficiency
    * Evaluate hot reload/fast refresh capabilities
    * Check debugging capabilities across platforms
    * Assess development tooling (IDE support, linting, formatting)
    * Review documentation quality and accessibility
    * Evaluate onboarding experience for new developers

15. **Scalability and Maintainability:**
    * Assess architecture scalability for team growth
    * Review code modularity for feature teams
    * Evaluate dependency injection and testability
    * Check for technical debt and refactoring needs
    * Assess long-term maintenance considerations
    * Review upgrade path for framework versions

**Expected Output:** A comprehensive cross-platform architecture analysis and design document including:

1. **Executive Summary:**
   - Framework and architecture assessment
   - Code sharing percentage (actual vs. target)
   - Key architectural decisions and rationale
   - Critical issues or risks
   - Overall architecture quality rating

2. **Architecture Diagram:**
   - Visual representation of architecture layers
   - Data flow between layers
   - Platform-specific vs. shared code boundaries
   - Component relationships and dependencies

3. **Detailed Analysis by Category:**
   - For each architectural aspect:
     - Current state assessment
     - Strengths and weaknesses
     - Platform-specific considerations
     - Code examples
     - Recommendations for improvement

4. **Code Sharing Analysis:**
   - Breakdown of shared vs. platform-specific code
   - Business logic sharing percentage
   - UI component reusability analysis
   - Opportunities to increase code sharing
   - Justification for platform-specific implementations

5. **Technical Decisions and Trade-offs:**
   - Framework selection rationale
   - State management choice justification
   - Navigation approach reasoning
   - Native module strategy
   - Performance vs. development speed trade-offs

6. **Best Practices Implementation:**
   - Design patterns in use
   - Architectural patterns applied
   - Code organization standards
   - Testing strategies
   - Security considerations

7. **Roadmap and Recommendations:**
   - Immediate improvements (Quick wins)
   - Short-term enhancements (1-3 months)
   - Long-term architectural evolution (6-12 months)
   - Framework upgrade considerations
   - Platform-specific optimization opportunities

**Example Output:**

```
# Cross-Platform Architecture Analysis
## React Native E-Commerce Application

## Executive Summary
- **Framework:** React Native 0.72 with TypeScript
- **Overall Architecture:** Clean Architecture with Repository Pattern
- **Code Sharing:** 78% (Target: 85%)
- **Quality Rating:** Good - Well-structured with optimization opportunities
- **Critical Issues:** 2
- **Key Strengths:** Strong separation of concerns, comprehensive testing
- **Key Weaknesses:** Some unnecessary platform-specific code, performance optimization opportunities

## Architecture Overview

### High-Level Architecture Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Screens    │  │  Components  │  │   Navigation │      │
│  │  (Shared)    │  │  (Shared)    │  │   (Shared)   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         │                   │                  │             │
│  ┌──────────────────────────────────────────────────┐       │
│  │        State Management (Redux Toolkit)          │       │
│  └──────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Business Logic Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Use Cases  │  │  Validators  │  │Domain Models │      │
│  │   (Shared)   │  │  (Shared)    │  │   (Shared)   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Repositories │  │  API Client  │  │ Local Storage│      │
│  │  (Shared)    │  │  (Shared)    │  │   (Shared)   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Platform Bridge Layer                      │
│  ┌───────────────────────┐  ┌───────────────────────┐       │
│  │   iOS Native Modules  │  │ Android Native Modules│       │
│  │  (Platform-specific)  │  │  (Platform-specific)  │       │
│  └───────────────────────┘  └───────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

## Detailed Analysis

### 1. Code Sharing Analysis

**Current State:** 78% shared code, 22% platform-specific

**Breakdown:**
- Business Logic Layer: 98% shared ✅
- Data Layer: 95% shared ✅
- Presentation Layer: 70% shared ⚠️
- Platform Bridge: 0% shared (by design) ✅

**Platform-Specific Code Distribution:**
```
iOS-specific:  12% (6,200 lines)
  - Native payment module
  - Push notification handling
  - Biometric authentication
  - Custom camera features

Android-specific: 10% (5,100 lines)
  - Native payment module
  - Push notification handling
  - Biometric authentication
  - Custom camera features
```

**Opportunity:** Consolidate payment and biometric modules into unified interfaces
**Potential Impact:** Increase shared code to 85%

### 2. Architecture Layers Assessment

#### Presentation Layer (Status: Good)
**Current Implementation:**

File: `src/features/product/presentation/ProductListScreen.tsx`
```typescript
// Good: Clean separation, platform-agnostic

import React, { useEffect } from 'react';
import { FlatList, StyleSheet, Platform } from 'react-native';
import { useDispatch, useSelector } from 'react-redux';
import { ProductCard } from '@/shared/components';
import { fetchProducts } from '../data/productSlice';

const ProductListScreen: React.FC = () => {
  const dispatch = useDispatch();
  const { products, loading } = useSelector(selectProducts);

  useEffect(() => {
    dispatch(fetchProducts());
  }, [dispatch]);

  return (
    <FlatList
      data={products}
      renderItem={({ item }) => <ProductCard product={item} />}
      keyExtractor={(item) => item.id}
      contentInsetAdjustmentBehavior="automatic"
      style={styles.list}
    />
  );
};

const styles = StyleSheet.create({
  list: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
```

**Strengths:**
- Clean component structure
- Proper hooks usage
- Platform-agnostic code
- Good separation from business logic

**Issues:**

**Issue: Inline platform-specific styling**
File: `src/features/checkout/presentation/CheckoutButton.tsx`
```typescript
// Current - Platform logic scattered
const CheckoutButton = () => {
  return (
    <TouchableOpacity
      style={{
        backgroundColor: '#007AFF',
        padding: Platform.OS === 'ios' ? 15 : 12,
        borderRadius: Platform.OS === 'ios' ? 10 : 5,
        ...Platform.select({
          ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 } },
          android: { elevation: 3 },
        }),
      }}
    >
      <Text style={{ fontSize: Platform.OS === 'ios' ? 17 : 16 }}>
        Checkout
      </Text>
    </TouchableOpacity>
  );
};
```

**Recommendation:**
```typescript
// Better - Extract platform-specific styles to theme

// src/theme/platformStyles.ts
export const getPlatformButtonStyle = () => ({
  padding: Platform.OS === 'ios' ? 15 : 12,
  borderRadius: Platform.OS === 'ios' ? 10 : 5,
  ...Platform.select({
    ios: {
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.25,
      shadowRadius: 3.84,
    },
    android: {
      elevation: 3,
    },
  }),
});

// src/features/checkout/presentation/CheckoutButton.tsx
import { getPlatformButtonStyle } from '@/theme/platformStyles';

const CheckoutButton = () => {
  return (
    <TouchableOpacity style={[styles.button, getPlatformButtonStyle()]}>
      <Text style={styles.buttonText}>Checkout</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    backgroundColor: '#007AFF',
  },
  buttonText: {
    fontSize: 16,
    color: '#fff',
    fontWeight: '600',
  },
});
```

#### Business Logic Layer (Status: Excellent)
**Current Implementation:**

File: `src/features/cart/domain/useCases/addToCart.useCase.ts`
```typescript
// Excellent: Pure business logic, 100% platform-agnostic, fully testable

import { Cart, Product } from '@/domain/models';
import { CartRepository } from '@/domain/repositories';

export class AddToCartUseCase {
  constructor(private cartRepository: CartRepository) {}

  async execute(product: Product, quantity: number): Promise<Cart> {
    // Validate business rules
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    if (quantity > product.stockQuantity) {
      throw new Error('Insufficient stock available');
    }

    // Execute business logic
    const currentCart = await this.cartRepository.getCart();
    const updatedCart = this.addProductToCart(currentCart, product, quantity);

    // Persist changes
    await this.cartRepository.saveCart(updatedCart);

    return updatedCart;
  }

  private addProductToCart(cart: Cart, product: Product, quantity: number): Cart {
    const existingItem = cart.items.find(item => item.productId === product.id);

    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      cart.items.push({
        productId: product.id,
        product,
        quantity,
        price: product.price,
      });
    }

    cart.totalAmount = this.calculateTotal(cart);
    return cart;
  }

  private calculateTotal(cart: Cart): number {
    return cart.items.reduce((total, item) => {
      return total + (item.price * item.quantity);
    }, 0);
  }
}
```

**Strengths:**
- 100% platform-agnostic ✅
- Pure business logic with no framework dependencies ✅
- Fully testable with unit tests ✅
- Clear single responsibility ✅
- Proper dependency injection ✅

**Unit Test Example:**
```typescript
// src/features/cart/domain/useCases/__tests__/addToCart.useCase.test.ts
describe('AddToCartUseCase', () => {
  let useCase: AddToCartUseCase;
  let mockRepository: jest.Mocked<CartRepository>;

  beforeEach(() => {
    mockRepository = {
      getCart: jest.fn(),
      saveCart: jest.fn(),
    } as any;
    useCase = new AddToCartUseCase(mockRepository);
  });

  it('should add product to empty cart', async () => {
    const product = createMockProduct({ id: '1', price: 29.99, stockQuantity: 10 });
    mockRepository.getCart.mockResolvedValue({ items: [], totalAmount: 0 });

    const result = await useCase.execute(product, 2);

    expect(result.items).toHaveLength(1);
    expect(result.items[0].quantity).toBe(2);
    expect(result.totalAmount).toBe(59.98);
  });

  it('should throw error for insufficient stock', async () => {
    const product = createMockProduct({ stockQuantity: 5 });
    mockRepository.getCart.mockResolvedValue({ items: [], totalAmount: 0 });

    await expect(useCase.execute(product, 10))
      .rejects
      .toThrow('Insufficient stock available');
  });
});
```

### 3. Native Module Integration (Status: Needs Improvement)

**Issue: Duplicated payment module code across platforms**

**Current State:**
- iOS payment module: `ios/PaymentModule.swift` (850 lines)
- Android payment module: `android/PaymentModule.kt` (820 lines)
- ~60% code duplication in validation and error handling

**iOS Implementation:**
```swift
// ios/PaymentModule.swift
@objc(PaymentModule)
class PaymentModule: NSObject {

  @objc
  func processPayment(_ paymentData: NSDictionary,
                     resolver resolve: @escaping RCTPromiseResolveBlock,
                     rejecter reject: @escaping RCTPromiseRejectBlock) {

    // Validation logic - duplicated across platforms
    guard let amount = paymentData["amount"] as? Double,
          amount > 0 else {
      reject("INVALID_AMOUNT", "Amount must be greater than 0", nil)
      return
    }

    guard let cardNumber = paymentData["cardNumber"] as? String,
          isValidCard(cardNumber) else {
      reject("INVALID_CARD", "Invalid card number", nil)
      return
    }

    // Platform-specific payment processing
    StripeAPI.shared.createPaymentIntent(amount: amount) { result in
      switch result {
        case .success(let paymentIntent):
          resolve(["paymentIntentId": paymentIntent.id])
        case .failure(let error):
          reject("PAYMENT_FAILED", error.localizedDescription, error)
      }
    }
  }

  // More validation methods...
}
```

**Recommendation: Create unified payment interface with shared validation**

```typescript
// src/platform/payment/PaymentService.ts (Shared interface)
export interface PaymentService {
  processPayment(paymentData: PaymentData): Promise<PaymentResult>;
  validateCard(cardNumber: string): boolean;
  validateAmount(amount: number): boolean;
}

// src/platform/payment/PaymentValidator.ts (Shared validation - pure TS)
export class PaymentValidator {
  static validateAmount(amount: number): void {
    if (amount <= 0) {
      throw new PaymentError('INVALID_AMOUNT', 'Amount must be greater than 0');
    }
    if (amount > 999999) {
      throw new PaymentError('AMOUNT_TOO_LARGE', 'Amount exceeds maximum');
    }
  }

  static validateCard(cardNumber: string): void {
    if (!cardNumber || cardNumber.length < 13) {
      throw new PaymentError('INVALID_CARD', 'Card number too short');
    }
    if (!this.luhnCheck(cardNumber)) {
      throw new PaymentError('INVALID_CARD', 'Invalid card number');
    }
  }

  private static luhnCheck(cardNumber: string): boolean {
    // Luhn algorithm implementation - shared across platforms
    // ... algorithm code ...
  }
}

// src/platform/payment/NativePaymentModule.ts (JS bridge)
import { NativeModules } from 'react-native';
import { PaymentValidator } from './PaymentValidator';

const { NativePaymentModule } = NativeModules;

export class PaymentService {
  async processPayment(paymentData: PaymentData): Promise<PaymentResult> {
    // Validation in shared TypeScript code (no duplication!)
    PaymentValidator.validateAmount(paymentData.amount);
    PaymentValidator.validateCard(paymentData.cardNumber);

    // Call native module for platform-specific processing only
    return await NativePaymentModule.processPayment(paymentData);
  }
}
```

**Simplified Native Modules (only platform-specific logic):**
```swift
// ios/PaymentModule.swift (Simplified - only platform-specific code)
@objc(NativePaymentModule)
class NativePaymentModule: NSObject {

  @objc
  func processPayment(_ paymentData: NSDictionary,
                     resolver resolve: @escaping RCTPromiseResolveBlock,
                     rejecter reject: @escaping RCTPromiseRejectBlock) {

    // Validation already done in JS layer - no duplication!
    let amount = paymentData["amount"] as! Double
    let cardNumber = paymentData["cardNumber"] as! String

    // Only platform-specific Stripe iOS SDK code here
    StripeAPI.shared.createPaymentIntent(amount: amount) { result in
      switch result {
        case .success(let paymentIntent):
          resolve(["paymentIntentId": paymentIntent.id])
        case .failure(let error):
          reject("PAYMENT_FAILED", error.localizedDescription, error)
      }
    }
  }
}
```

**Impact:**
- Reduces native code by ~500 lines per platform
- Validation logic centralized and easily testable
- Increases shared code percentage from 78% to 82%
- Reduces maintenance burden

[... more sections ...]

## Recommendations Summary

### Quick Wins (This Week)
1. ✅ Extract platform-specific styles to theme system (4 hours)
2. ✅ Consolidate payment validation to shared TypeScript (6 hours)
3. ✅ Add platform detection utilities (2 hours)

### Short-term (1-2 Months)
1. Unify biometric authentication interfaces
2. Implement automated platform-specific testing
3. Create shared component library with platform adaptations
4. Add performance monitoring per platform

### Long-term (6-12 Months)
1. Evaluate React Native new architecture migration (Fabric + TurboModules)
2. Implement advanced code splitting for faster startup
3. Create platform-specific performance optimizations
4. Consider feature parity analysis and roadmap

## Code Sharing Opportunities

**Current:** 78% shared
**Target:** 85% shared
**Gap:** 7% (3,600 lines)

**Opportunities:**
1. Unify payment module validation (+2%)
2. Consolidate biometric auth interface (+3%)
3. Extract platform styling to theme system (+2%)

**Total potential:** 85% shared code ✅
```

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-06 (Pattern Recognition)
- ST-03 (Structured Output Templates)
- OC-03 (Visual Diagrams)

**Related Prompts:**
- `ios_swift_architecture_review.md` - For iOS-specific architecture deep dive
- `android_kotlin_best_practices.md` - For Android-specific architecture deep dive
- `react_native_performance_optimization.md` - For React Native performance specifics
- `flutter_widget_analysis.md` - For Flutter architecture specifics
- `architecture_layer_identification.md` - For general architecture analysis
- `mobile_app_security_review.md` - For cross-platform security considerations

**Customization Guide:**
- For React Native apps: Emphasize bridge optimization, TurboModules, Fabric renderer
- For Flutter apps: Focus on platform channels, method channels, FFI, widget composition
- For Xamarin apps: Highlight .NET Standard libraries, Xamarin.Forms vs. native UI, dependency services
- For Ionic/Capacitor: Emphasize web code reuse, plugin architecture, native feature access
- For enterprise apps: Add sections on CI/CD for multiple platforms, app center, distribution
- For startups: Focus on rapid development, code sharing maximization, MVP considerations

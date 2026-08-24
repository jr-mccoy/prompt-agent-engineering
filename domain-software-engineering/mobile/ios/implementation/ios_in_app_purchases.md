---
title: "iOS In-App Purchases"
category: mobile-development
description: "Implement StoreKit 2 with Product loading, Transaction verification, subscription status management, offer codes, and server-side receipt validation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - storekit
  - in-app-purchases
  - subscriptions
  - monetization
  - mobile-development
updated: "2026-03-19"
---

# iOS In-App Purchases

**Objective:** Implement a complete in-app purchase system using StoreKit 2 with Product loading, Transaction verification, subscription status tracking, offer codes, and optional server-side receipt validation for iOS applications.

**When to Use:** Use this prompt when adding monetization to an iOS app through consumables, non-consumables, auto-renewable subscriptions, or non-renewing subscriptions. Best used after product catalog and pricing decisions are finalized.

**Prompt Type:** Comprehensive (450-500 lines)

---

## Context Gathering

Before implementing in-app purchases, gather essential context:

1. **Product Catalog:**
   - "What products are being sold (consumables, non-consumables, subscriptions)?"
   - "What are the product identifiers configured in App Store Connect?"
   - "Are there subscription tiers or groups?"

2. **Business Logic:**
   - "What features are locked behind purchases?"
   - "Should purchases sync across devices?"
   - "Are there promotional offers or introductory pricing?"

3. **Existing Setup:**
   - "Is StoreKit already configured in the project?"
   - "Is there a server-side receipt validation endpoint?"
   - "Are StoreKit configuration files set up for testing?"

4. **Requirements:**
   - "Should the app work offline with cached entitlements?"
   - "Is family sharing supported for purchases?"
   - "Do you need to support offer codes or promotional offers?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Configure products in App Store Connect** - All product IDs must exist before testing.
2. **Add StoreKit configuration file** for local testing (File > New > StoreKit Configuration File).
3. **Always verify transactions** - Never grant entitlements without transaction verification.
4. **Handle all transaction states** - purchased, pending, revoked, expired.
5. **Listen for transactions on launch** - Use Transaction.updates to catch external purchases.

### False-Positive Prevention

- ❌ Do NOT grant entitlements without verifying the transaction
- ❌ Do NOT assume purchase success before Transaction.currentEntitlement confirms it
- ❌ Do NOT hardcode product IDs only in code (use configuration or App Store Connect)
- ❌ Do NOT ignore Transaction.updates stream - purchases can happen outside your app
- ❌ Do NOT skip the "Restore Purchases" button (App Review requirement)
- ✅ DO verify transactions using AppTransaction or your server
- ✅ DO cache entitlement state for offline access
- ✅ DO handle pending purchases (Ask to Buy, SCA)
- ✅ DO finish transactions after granting entitlements
- ✅ DO provide a restore purchases option

---

### Phase 1: Store Manager

#### 1.1 Product Loading & Purchase

```swift
// File: Store/StoreManager.swift

import StoreKit
import OSLog

@Observable
final class StoreManager {
    // Product collections
    private(set) var subscriptions: [Product] = []
    private(set) var nonConsumables: [Product] = []
    private(set) var consumables: [Product] = []

    // Entitlement state
    private(set) var purchasedSubscriptions: [Product] = []
    private(set) var purchasedNonConsumables: [Product] = []
    private(set) var subscriptionStatus: SubscriptionStatus?

    // UI state
    private(set) var isLoading = false
    private(set) var isPurchasing = false
    private(set) var error: String?

    private let logger = Logger(subsystem: "com.example.app", category: "Store")
    private var updateTask: Task<Void, Never>?

    // Product identifiers
    private let subscriptionIDs = [
        "com.example.app.monthly",
        "com.example.app.yearly"
    ]
    private let nonConsumableIDs = [
        "com.example.app.premium_themes",
        "com.example.app.export_pack"
    ]
    private let consumableIDs = [
        "com.example.app.credits_10",
        "com.example.app.credits_50"
    ]

    init() {
        // Start listening for transactions immediately
        updateTask = listenForTransactions()
    }

    deinit {
        updateTask?.cancel()
    }

    // MARK: - Load Products

    func loadProducts() async {
        isLoading = true
        error = nil

        do {
            let allIDs = subscriptionIDs + nonConsumableIDs + consumableIDs
            let products = try await Product.products(for: Set(allIDs))

            // Categorize products
            subscriptions = products.filter { $0.type == .autoRenewable }
                .sorted { $0.price < $1.price }
            nonConsumables = products.filter { $0.type == .nonConsumable }
            consumables = products.filter { $0.type == .consumable }

            // Check current entitlements
            await refreshEntitlements()

            logger.info("Loaded \(products.count) products")
        } catch {
            self.error = "Failed to load products: \(error.localizedDescription)"
            logger.error("Product loading failed: \(error)")
        }

        isLoading = false
    }

    // MARK: - Purchase

    func purchase(_ product: Product) async throws -> Transaction? {
        isPurchasing = true
        defer { isPurchasing = false }

        do {
            let result = try await product.purchase()

            switch result {
            case .success(let verification):
                let transaction = try checkVerified(verification)

                // Grant entitlement
                await refreshEntitlements()

                // Finish the transaction
                await transaction.finish()

                logger.info("Purchase successful: \(product.id)")
                return transaction

            case .pending:
                // Ask to Buy or SCA - transaction will come via updates
                logger.info("Purchase pending: \(product.id)")
                return nil

            case .userCancelled:
                logger.info("Purchase cancelled: \(product.id)")
                return nil

            @unknown default:
                return nil
            }
        } catch {
            self.error = "Purchase failed: \(error.localizedDescription)"
            logger.error("Purchase error: \(error)")
            throw error
        }
    }

    // MARK: - Restore Purchases

    func restorePurchases() async {
        isLoading = true
        do {
            try await AppStore.sync()
            await refreshEntitlements()
            logger.info("Purchases restored")
        } catch {
            self.error = "Restore failed: \(error.localizedDescription)"
            logger.error("Restore failed: \(error)")
        }
        isLoading = false
    }

    // MARK: - Transaction Verification

    private func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
        switch result {
        case .unverified(_, let error):
            logger.error("Transaction verification failed: \(error)")
            throw StoreError.verificationFailed
        case .verified(let value):
            return value
        }
    }

    // MARK: - Entitlement Checking

    func refreshEntitlements() async {
        var purchased: [Product] = []
        var purchasedSubs: [Product] = []

        // Check non-consumable entitlements
        for product in nonConsumables {
            if let transaction = await product.currentEntitlement {
                if let _ = try? checkVerified(transaction) {
                    purchased.append(product)
                }
            }
        }

        // Check subscription entitlements
        for product in subscriptions {
            if let transaction = await product.currentEntitlement {
                if let _ = try? checkVerified(transaction) {
                    purchasedSubs.append(product)
                }
            }
        }

        purchasedNonConsumables = purchased
        purchasedSubscriptions = purchasedSubs

        // Get detailed subscription status
        await refreshSubscriptionStatus()
    }

    private func refreshSubscriptionStatus() async {
        guard let groupID = subscriptions.first?.subscription?.subscriptionGroupID else { return }

        do {
            let statuses = try await Product.SubscriptionInfo.status(for: groupID)
            if let status = statuses.first {
                let renewalInfo = try checkVerified(status.renewalInfo)
                let transaction = try checkVerified(status.transaction)

                subscriptionStatus = SubscriptionStatus(
                    isActive: status.state == .subscribed || status.state == .inGracePeriod,
                    state: status.state,
                    productID: transaction.productID,
                    expirationDate: transaction.expirationDate,
                    willAutoRenew: renewalInfo.willAutoRenew,
                    isInBillingRetry: status.state == .inBillingRetryPeriod
                )
            }
        } catch {
            logger.error("Subscription status check failed: \(error)")
        }
    }

    // MARK: - Transaction Listener

    private func listenForTransactions() -> Task<Void, Never> {
        Task.detached { [weak self] in
            for await result in Transaction.updates {
                guard let self else { return }
                do {
                    let transaction = try await self.checkVerified(result)
                    await self.refreshEntitlements()
                    await transaction.finish()
                    self.logger.info("Transaction update processed: \(transaction.productID)")
                } catch {
                    self.logger.error("Transaction update failed: \(error)")
                }
            }
        }
    }

    // MARK: - Convenience

    var isPremium: Bool {
        !purchasedSubscriptions.isEmpty || purchasedNonConsumables.contains { $0.id == "com.example.app.premium_themes" }
    }

    func isEntitled(to productID: String) -> Bool {
        purchasedNonConsumables.contains { $0.id == productID } ||
        purchasedSubscriptions.contains { $0.id == productID }
    }
}

// MARK: - Supporting Types

struct SubscriptionStatus {
    let isActive: Bool
    let state: Product.SubscriptionInfo.RenewalState
    let productID: String
    let expirationDate: Date?
    let willAutoRenew: Bool
    let isInBillingRetry: Bool
}

enum StoreError: LocalizedError {
    case verificationFailed
    case purchaseFailed(String)

    var errorDescription: String? {
        switch self {
        case .verificationFailed: return "Transaction could not be verified"
        case .purchaseFailed(let reason): return reason
        }
    }
}
```

---

### Phase 2: Paywall UI

**CHECKPOINT 1:** Confirm products load correctly before building UI.

#### 2.1 Subscription Paywall

```swift
// File: Store/Views/PaywallView.swift

import SwiftUI
import StoreKit

struct PaywallView: View {
    @Environment(StoreManager.self) private var store
    @Environment(\.dismiss) private var dismiss
    @State private var selectedProduct: Product?
    @State private var isPurchasing = false

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {
                    // Feature highlights
                    featureList

                    // Subscription options
                    subscriptionPicker

                    // Purchase button
                    purchaseButton

                    // Legal links
                    legalSection
                }
                .padding()
            }
            .navigationTitle("Go Premium")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Close") { dismiss() }
                }
            }
            .onAppear {
                selectedProduct = store.subscriptions.last // Default to yearly
            }
        }
    }

    private var featureList: some View {
        VStack(alignment: .leading, spacing: 12) {
            FeatureRow(icon: "paintbrush", title: "Premium Themes", description: "Unlock all custom themes")
            FeatureRow(icon: "square.and.arrow.up", title: "Export", description: "Export to PDF, Markdown, HTML")
            FeatureRow(icon: "icloud", title: "Unlimited Sync", description: "Sync across all your devices")
            FeatureRow(icon: "wand.and.stars", title: "AI Features", description: "Smart suggestions and autocomplete")
        }
    }

    private var subscriptionPicker: some View {
        VStack(spacing: 12) {
            ForEach(store.subscriptions) { product in
                SubscriptionOptionRow(
                    product: product,
                    isSelected: selectedProduct?.id == product.id
                )
                .onTapGesture { selectedProduct = product }
            }
        }
    }

    private var purchaseButton: some View {
        Button {
            guard let product = selectedProduct else { return }
            Task {
                isPurchasing = true
                _ = try? await store.purchase(product)
                isPurchasing = false
                if store.isPremium { dismiss() }
            }
        } label: {
            if isPurchasing {
                ProgressView()
                    .frame(maxWidth: .infinity, minHeight: 50)
            } else {
                Text("Subscribe Now")
                    .font(.headline)
                    .frame(maxWidth: .infinity, minHeight: 50)
            }
        }
        .buttonStyle(.borderedProminent)
        .disabled(selectedProduct == nil || isPurchasing)
    }

    private var legalSection: some View {
        VStack(spacing: 8) {
            Button("Restore Purchases") {
                Task { await store.restorePurchases() }
            }
            .font(.subheadline)

            Text("Subscription auto-renews unless cancelled 24 hours before the end of the current period.")
                .font(.caption2)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)

            HStack {
                Link("Terms of Use", destination: URL(string: "https://example.com/terms")!)
                Text("·")
                Link("Privacy Policy", destination: URL(string: "https://example.com/privacy")!)
            }
            .font(.caption2)
        }
    }
}

struct SubscriptionOptionRow: View {
    let product: Product
    let isSelected: Bool

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(product.displayName)
                    .font(.headline)
                Text(product.description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }

            Spacer()

            VStack(alignment: .trailing) {
                Text(product.displayPrice)
                    .font(.headline)
                if let period = product.subscription?.subscriptionPeriod {
                    Text(period.unit == .month ? "/month" : "/year")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
        }
        .padding()
        .background(isSelected ? Color.accentColor.opacity(0.1) : Color(.secondarySystemBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .overlay(
            RoundedRectangle(cornerRadius: 12)
                .stroke(isSelected ? Color.accentColor : .clear, lineWidth: 2)
        )
        .accessibilityElement(children: .combine)
        .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}

struct FeatureRow: View {
    let icon: String
    let title: String
    let description: String

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: icon)
                .font(.title3)
                .foregroundStyle(.accent)
                .frame(width: 32)
            VStack(alignment: .leading) {
                Text(title).font(.subheadline).fontWeight(.medium)
                Text(description).font(.caption).foregroundStyle(.secondary)
            }
        }
    }
}
```

---

### Phase 3: Offer Codes & Promotional Offers

```swift
// File: Store/StoreManager+Offers.swift

import StoreKit

extension StoreManager {

    /// Present the offer code redemption sheet
    func presentOfferCodeRedemption() async {
        #if !targetEnvironment(simulator)
        do {
            try await AppStore.presentOfferCodeRedeemSheet()
            await refreshEntitlements()
        } catch {
            logger.error("Offer code redemption failed: \(error)")
        }
        #endif
    }

    /// Check eligibility for introductory offer
    func isEligibleForIntroOffer(_ product: Product) async -> Bool {
        await product.subscription?.isEligibleForIntroOffer ?? false
    }

    /// Get subscription offer details
    func offerDetails(for product: Product) -> OfferInfo? {
        guard let subscription = product.subscription else { return nil }

        // Check for introductory offer
        if let introOffer = subscription.introductoryOffer {
            return OfferInfo(
                type: .introductory,
                price: introOffer.displayPrice,
                period: introOffer.period,
                paymentMode: introOffer.paymentMode
            )
        }

        return nil
    }
}

struct OfferInfo {
    enum OfferType { case introductory, promotional }

    let type: OfferType
    let price: String
    let period: Product.SubscriptionPeriod
    let paymentMode: Product.SubscriptionOffer.PaymentMode
}
```

---

## Expected Output

### File Structure

```
Store/
├── StoreManager.swift              # Product loading, purchase, verification
├── StoreManager+Offers.swift       # Offer codes, promotional offers
└── Views/
    └── PaywallView.swift           # Subscription paywall UI
```

### Implementation Checklist

- [ ] Product loading with categorization
- [ ] Purchase flow with verification
- [ ] Transaction.updates listener on launch
- [ ] Entitlement checking and caching
- [ ] Subscription status tracking (active, grace, retry)
- [ ] Restore purchases button
- [ ] Paywall UI with subscription picker
- [ ] Offer code redemption
- [ ] Introductory offer eligibility
- [ ] Legal text (auto-renew disclosure, ToS, privacy)
- [ ] StoreKit configuration file for testing

---

## Example Interaction

**User:** "I need a paywall with monthly and yearly subscriptions and a free trial."

**Assistant:**
```swift
// Configure in App Store Connect:
// - com.example.app.monthly: $4.99/month, 7-day free trial
// - com.example.app.yearly: $39.99/year, 14-day free trial

// In PaywallView, show trial info:
if let intro = product.subscription?.introductoryOffer,
   await product.subscription?.isEligibleForIntroOffer == true {
    Text("Start your \(intro.period.value)-\(intro.period.unit) free trial")
        .font(.subheadline)
        .foregroundStyle(.green)
}

// Check premium access anywhere:
if storeManager.isPremium {
    PremiumFeatureView()
} else {
    PaywallView()
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Complete StoreKit 2 implementation
- **ST-02** (Sequential Instructions): Phased from products to offers
- **RT-02** (Multi-Dimensional Analysis): Products, transactions, UI, offers
- **RT-05** (Edge Case Identification): Pending, revoked, verification failure
- **DS-02** (Progressive Disclosure): Basic purchase to advanced offers
- **NE-02** (Phased Workflow): Build phases with checkpoint

---

## Related Prompts

- [ios_api_integration.md](ios_api_integration.md) - Server-side receipt validation endpoint
- [ios_state_management.md](ios_state_management.md) - Entitlement state management
- [ios_push_notifications.md](ios_push_notifications.md) - Subscription renewal reminders
- [ios_swiftui_screen_builder.md](ios_swiftui_screen_builder.md) - Build paywall screens

---

## Customization Guide

### For Server-Side Validation

Send receipt to your server:
```swift
func validateOnServer(transaction: Transaction) async throws {
    guard let appTransaction = try? await AppTransaction.shared else { return }
    let receipt = appTransaction.jsonRepresentation
    // Send to your backend for validation with App Store Server API
}
```

### For Consumable Credits

Track consumable purchases:
```swift
func purchaseCredits(_ product: Product) async throws {
    let transaction = try await purchase(product)
    if let tx = transaction {
        let credits = creditsForProduct(tx.productID)
        await CreditsManager.shared.addCredits(credits)
    }
}
```

### For SubscriptionStoreView (iOS 17+)

Use Apple's built-in subscription UI:
```swift
SubscriptionStoreView(groupID: "your_group_id") {
    VStack {
        Image("premium_header")
        Text("Unlock all features")
    }
}
.subscriptionStoreControlStyle(.prominentPicker)
```

---
title: "DataStore to UserDefaults/Keychain Migration"
category: mobile-development
description: "Migrate Android DataStore to iOS UserDefaults and Keychain covering preferences, proto to Codable serialization, property wrappers, and secure storage"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: beginner
tags:
  - ios
  - android
  - migration
  - datastore
  - userdefaults
  - keychain
  - preferences
updated: "2026-03-19"
---

# DataStore to UserDefaults/Keychain Migration

**Objective:** Translate Android's DataStore (Preferences and Proto) to iOS equivalents — UserDefaults for general preferences and Keychain Services for sensitive data. The output includes type-safe property wrappers, reactive observation, and secure storage patterns.

**When to Use:** When migrating an Android app's lightweight key-value storage from DataStore to iOS. This is typically one of the simpler migration tasks but requires attention to security boundaries (what goes in UserDefaults vs. Keychain).

**Prompt Type:** Modular (~220 lines)

## Context Gathering

1. Does the app use Preferences DataStore, Proto DataStore, or both?
2. What types of data are stored? (user preferences, auth tokens, feature flags, onboarding state)
3. Is any stored data sensitive? (tokens, PII, credentials)
4. How is DataStore accessed? (direct Flow collection, repository wrapper)
5. Are there migration paths from SharedPreferences to DataStore?

## Instructions

### CRITICAL: Verification Requirements

- Sensitive data (tokens, passwords, PII) MUST use Keychain, never UserDefaults
- Property wrapper types MUST match the original DataStore key types
- Observation patterns MUST trigger UI updates when preferences change
- Default values MUST match the Android DataStore defaults

### False-Positive Prevention

- ❌ DO NOT store auth tokens or passwords in UserDefaults — they are not encrypted
- ✅ DO use Keychain Services for any sensitive data
- ❌ DO NOT assume UserDefaults observation works like DataStore Flow
- ✅ DO use `@AppStorage` in SwiftUI for reactive UI or KVO for UIKit
- ❌ DO NOT store large data blobs in UserDefaults (limit ~1MB recommended)
- ✅ DO use file storage or SwiftData for large structured data
- ❌ DO NOT forget to register UserDefaults defaults
- ✅ DO use `UserDefaults.standard.register(defaults:)` at app launch

### Step 1: Preferences DataStore to UserDefaults

**Kotlin (Preferences DataStore):**
```kotlin
// DataStore definition
val Context.dataStore by preferencesDataStore(name = "settings")

// Keys
object PreferenceKeys {
    val DARK_MODE = booleanPreferencesKey("dark_mode")
    val LANGUAGE = stringPreferencesKey("language")
    val NOTIFICATIONS_ENABLED = booleanPreferencesKey("notifications_enabled")
    val FONT_SIZE = floatPreferencesKey("font_size")
    val ONBOARDING_COMPLETED = booleanPreferencesKey("onboarding_completed")
}

// Reading (reactive)
class SettingsRepository @Inject constructor(
    private val dataStore: DataStore<Preferences>
) {
    val darkMode: Flow<Boolean> = dataStore.data.map { prefs ->
        prefs[PreferenceKeys.DARK_MODE] ?: false
    }

    val language: Flow<String> = dataStore.data.map { prefs ->
        prefs[PreferenceKeys.LANGUAGE] ?: "en"
    }

    // Writing
    suspend fun setDarkMode(enabled: Boolean) {
        dataStore.edit { prefs ->
            prefs[PreferenceKeys.DARK_MODE] = enabled
        }
    }

    suspend fun setLanguage(language: String) {
        dataStore.edit { prefs ->
            prefs[PreferenceKeys.LANGUAGE] = language
        }
    }
}
```

**Swift (UserDefaults with @AppStorage):**
```swift
// SwiftUI reactive access — simplest approach
struct SettingsScreen: View {
    @AppStorage("dark_mode") private var darkMode = false
    @AppStorage("language") private var language = "en"
    @AppStorage("notifications_enabled") private var notificationsEnabled = true
    @AppStorage("font_size") private var fontSize: Double = 16.0
    @AppStorage("onboarding_completed") private var onboardingCompleted = false

    var body: some View {
        Form {
            Toggle("Dark Mode", isOn: $darkMode)
            Picker("Language", selection: $language) {
                Text("English").tag("en")
                Text("Spanish").tag("es")
            }
            Toggle("Notifications", isOn: $notificationsEnabled)
            Slider(value: $fontSize, in: 12...24, step: 1) {
                Text("Font Size: \(Int(fontSize))")
            }
        }
    }
}

// Repository pattern (for non-SwiftUI or shared logic)
@Observable
final class SettingsRepository {
    var darkMode: Bool {
        get { UserDefaults.standard.bool(forKey: "dark_mode") }
        set { UserDefaults.standard.set(newValue, forKey: "dark_mode") }
    }

    var language: String {
        get { UserDefaults.standard.string(forKey: "language") ?? "en" }
        set { UserDefaults.standard.set(newValue, forKey: "language") }
    }

    var notificationsEnabled: Bool {
        get { UserDefaults.standard.bool(forKey: "notifications_enabled") }
        set { UserDefaults.standard.set(newValue, forKey: "notifications_enabled") }
    }

    init() {
        // Register defaults (equivalent to DataStore default values)
        UserDefaults.standard.register(defaults: [
            "dark_mode": false,
            "language": "en",
            "notifications_enabled": true,
            "font_size": 16.0,
            "onboarding_completed": false
        ])
    }
}
```

### Step 2: Proto DataStore to Codable File Storage

**Kotlin (Proto DataStore):**
```kotlin
// Proto definition
// user_preferences.proto
// message UserPreferences {
//   string display_name = 1;
//   Theme theme = 2;
//   repeated string favorite_categories = 3;
// }

val Context.userPrefsStore by dataStore(
    fileName = "user_prefs.pb",
    serializer = UserPreferencesSerializer
)

// Reading
val prefs: Flow<UserPreferences> = userPrefsStore.data

// Writing
suspend fun updateDisplayName(name: String) {
    userPrefsStore.updateData { current ->
        current.toBuilder().setDisplayName(name).build()
    }
}
```

**Swift (Codable struct persisted to file):**
```swift
struct UserPreferences: Codable {
    var displayName: String = ""
    var theme: Theme = .system
    var favoriteCategories: [String] = []

    enum Theme: String, Codable {
        case light, dark, system
    }
}

@Observable
final class UserPreferencesStore {
    private(set) var preferences: UserPreferences

    private let fileURL: URL = {
        FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("user_preferences.json")
    }()

    init() {
        if let data = try? Data(contentsOf: fileURL),
           let prefs = try? JSONDecoder().decode(UserPreferences.self, from: data) {
            self.preferences = prefs
        } else {
            self.preferences = UserPreferences()
        }
    }

    func update(_ transform: (inout UserPreferences) -> Void) {
        transform(&preferences)
        save()
    }

    private func save() {
        guard let data = try? JSONEncoder().encode(preferences) else { return }
        try? data.write(to: fileURL, options: .atomic)
    }
}

// Usage
store.update { prefs in
    prefs.displayName = "Alice"
    prefs.theme = .dark
}
```

### Step 3: Sensitive Data — Keychain

**Kotlin (EncryptedSharedPreferences or DataStore with encryption):**
```kotlin
// Android: Store auth token securely
val encryptedPrefs = EncryptedSharedPreferences.create(
    context, "secure_prefs",
    MasterKey.Builder(context).setKeyScheme(MasterKey.KeyScheme.AES256_GCM).build(),
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)

encryptedPrefs.edit().putString("auth_token", token).apply()
val token = encryptedPrefs.getString("auth_token", null)
```

**Swift (Keychain wrapper):**
```swift
enum KeychainHelper {
    static func save(_ value: String, forKey key: String) throws {
        let data = Data(value.utf8)
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecValueData as String: data,
            kSecAttrAccessible as String: kSecAttrAccessibleAfterFirstUnlock
        ]

        SecItemDelete(query as CFDictionary) // Remove existing
        let status = SecItemAdd(query as CFDictionary, nil)
        guard status == errSecSuccess else {
            throw KeychainError.saveFailed(status)
        }
    }

    static func get(forKey key: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]

        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        guard status == errSecSuccess, let data = result as? Data else {
            return nil
        }
        return String(data: data, encoding: .utf8)
    }

    static func delete(forKey key: String) {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key
        ]
        SecItemDelete(query as CFDictionary)
    }
}

// Usage
try KeychainHelper.save(authToken, forKey: "auth_token")
let token = KeychainHelper.get(forKey: "auth_token")
```

## Expected Output

1. **UserDefaults setup** with registered defaults and property wrappers
2. **Codable file store** for complex preference objects (Proto DataStore equivalent)
3. **Keychain helper** for sensitive data storage
4. **Migration mapping table** showing each DataStore key and its iOS destination

## Example Interaction

**User:** Our Android app stores user settings in Preferences DataStore (8 keys) and an auth token in EncryptedSharedPreferences.

**Assistant:**

| DataStore Key | Type | iOS Storage | iOS API |
|--------------|------|-------------|---------|
| `dark_mode` | Boolean | UserDefaults | `@AppStorage` |
| `language` | String | UserDefaults | `@AppStorage` |
| `font_size` | Float | UserDefaults | `@AppStorage` |
| `notifications_enabled` | Boolean | UserDefaults | `@AppStorage` |
| `onboarding_completed` | Boolean | UserDefaults | `@AppStorage` |
| `last_sync_time` | Long | UserDefaults | `@AppStorage` (as `Double`) |
| `selected_categories` | StringSet | UserDefaults | Codable `[String]` |
| `auth_token` | String (encrypted) | **Keychain** | `KeychainHelper` |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Preferences, proto, and secure storage steps |
| **RT-02: Contextual Reference Integration** | DataStore, UserDefaults, Keychain documentation |
| **DS-02: Output Specification Framework** | Storage mapping, code implementations |

## Related Prompts

- `migration_room_to_core_data.md` — For structured database migration
- `migration_architecture_adaptation.md` — Repository layer consuming preferences
- `migration_platform_feature_mapping.md` — Overall platform API mapping

## Customization Guide

- **App Groups:** If the iOS app has a widget or extension that needs shared preferences, use `UserDefaults(suiteName:)` with an App Group.
- **iCloud Sync:** Use `NSUbiquitousKeyValueStore` to sync preferences across devices (similar to DataStore with cloud backup).
- **Third-Party Keychain:** Libraries like KeychainAccess provide a cleaner API for Keychain operations.
- **SwiftUI Only:** If the app is pure SwiftUI, `@AppStorage` handles most cases without needing a repository wrapper.

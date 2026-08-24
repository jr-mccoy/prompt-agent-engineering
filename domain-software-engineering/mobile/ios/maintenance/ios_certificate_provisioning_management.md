---
title: "iOS Certificate & Provisioning Management"
category: mobile-development
description: "Manage iOS code signing certificates, provisioning profiles, automatic and manual signing, CI/CD signing workflows, and expiration monitoring for reliable app distribution."
techniques:
  - ST-01
  - ST-02
difficulty: intermediate
tags:
  - ios
  - xcode
  - code-signing
  - provisioning
  - certificates
updated: "2026-03-20"
---

# iOS Certificate & Provisioning Management

**Objective:** Manage iOS code signing certificates and provisioning profiles effectively, including understanding certificate types, provisioning profile lifecycle, configuring automatic and manual signing, setting up CI/CD signing, and monitoring expiration dates to prevent distribution failures.

**When to Use:** Use this prompt when setting up a new project for distribution, onboarding new developers, troubleshooting code signing errors, configuring CI/CD pipelines, or when certificates/profiles are approaching expiration. Also essential after Apple Developer Program renewal.

**Prompt Type:** Modular (300+ lines)

---

## Context Gathering

Before managing certificates, gather essential context:

1. **Team Setup:**
   - "What type of Apple Developer account (Individual, Organization, Enterprise)?"
   - "How many developers need signing capabilities?"
   - "Who has Admin/Account Holder access to the Developer Portal?"

2. **Distribution:**
   - "What distribution methods are used (App Store, TestFlight, Ad Hoc, Enterprise)?"
   - "Do you distribute to multiple App IDs or have extensions/widgets?"
   - "Are there any managed distribution services (Firebase App Distribution, Diawi)?"

3. **CI/CD:**
   - "What CI/CD platform is used (Xcode Cloud, GitHub Actions, CircleCI, Bitrise, Jenkins)?"
   - "How are signing credentials currently stored for CI?"
   - "Is Fastlane match or a similar tool in use?"

4. **Current State:**
   - "Are there active code signing errors?"
   - "When do current certificates expire?"
   - "Are there unused or orphaned provisioning profiles?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before making ANY changes to certificates or profiles, you MUST:**

1. **Back up existing certificates** - Export certificates and private keys to a secure location before revoking or regenerating.
2. **Understand the blast radius** - Revoking a distribution certificate invalidates ALL provisioning profiles that use it, affecting the entire team.
3. **Coordinate with the team** - Certificate changes affect every developer. Notify before making changes.
4. **Verify private key availability** - A certificate without its private key is useless. Ensure the private key is in a keychain or securely stored.
5. **Test signing after changes** - Archive and export the app to verify the signing chain is complete.

**Revoking the wrong certificate can break builds for your entire team and CI/CD pipeline. Always verify before revoking.**

### False-Positive Prevention

- ❌ Do NOT revoke certificates without confirming no other team members or CI systems depend on them
- ❌ Do NOT store certificates or private keys in source control (even encrypted, prefer Fastlane match or Xcode Cloud)
- ❌ Do NOT create multiple distribution certificates for the same purpose (causes confusion)
- ❌ Do NOT ignore certificate expiration warnings (builds will fail when they expire)
- ❌ Do NOT mix automatic and manual signing in the same target without understanding the implications
- ✅ DO use automatic signing for development whenever possible
- ✅ DO use a dedicated signing identity for CI/CD separate from developer machines
- ✅ DO maintain a certificate inventory with expiration dates
- ✅ DO set up calendar reminders 30 days before certificate expiration
- ✅ DO use Keychain Access to verify certificate-private key pairing

---

### Phase 1: Certificate Types & Lifecycle

#### 1.1 Certificate Types

| Certificate Type | Purpose | Max Count | Validity | Who Needs It |
|-----------------|---------|-----------|----------|--------------|
| **Apple Development** | Run on device during development | Unlimited (per developer) | 1 year | Every developer |
| **Apple Distribution** | App Store and TestFlight | 3 per account | 1 year | Build machine / CI |
| **Apple Push Notification (APNs)** | Send push notifications | 2 per App ID (dev + prod) | 1 year | Server-side |
| **Apple Distribution (Enterprise)** | In-house distribution | 3 per account | 3 years | Enterprise only |
| **Developer ID Application** | macOS distribution outside App Store | 5 per account | 5 years | macOS apps |

#### 1.2 Certificate Inventory

```markdown
## Certificate Inventory

| Certificate | Type | Serial | Expires | Keychain Location | Used By |
|-------------|------|--------|---------|-------------------|---------|
| [Name] | Apple Distribution | [XXXX] | 2026-08-15 | CI Keychain | CI, Fastlane |
| [Name] | Apple Development | [XXXX] | 2026-11-03 | Dev 1 Keychain | Developer 1 |
| [Name] | Apple Development | [XXXX] | 2026-09-22 | Dev 2 Keychain | Developer 2 |
| [Name] | APNs (Production) | [XXXX] | 2026-07-01 | Server | Push service |

### Expiration Timeline
| Date | Certificate | Action Required |
|------|-------------|----------------|
| 2026-07-01 | APNs Production | Renew, update server config |
| 2026-08-15 | Apple Distribution | Renew, update CI keychain |
| 2026-09-22 | Dev 2 Development | Auto-renew via Xcode |
```

#### 1.3 Certificate Management Commands

```bash
# List certificates in keychain
security find-identity -v -p codesigning

# Check certificate expiration
security find-certificate -c "Apple Distribution" -p | \
    openssl x509 -noout -enddate

# Export certificate and private key (for backup or CI)
security export -k login.keychain -t identities -f pkcs12 \
    -o distribution_cert.p12 -P "password"

# Import certificate on CI machine
security import distribution_cert.p12 -k build.keychain \
    -P "password" -T /usr/bin/codesign -T /usr/bin/security

# Verify a certificate-private key pair
security find-identity -v | grep "Apple Distribution"
```

---

### Phase 2: Provisioning Profile Management

**CHECKPOINT 1:** Confirm certificate inventory is up to date before managing profiles.

```markdown
## Certificate Status

| Type | Count | Nearest Expiry | Status |
|------|-------|----------------|--------|
| Development | [N] | [date] | [OK / Expiring / Expired] |
| Distribution | [N] | [date] | [OK / Expiring / Expired] |
| APNs | [N] | [date] | [OK / Expiring / Expired] |

**Proceed with provisioning profile management?**
```

#### 2.1 Provisioning Profile Types

| Profile Type | Contains | Used For | Distribution Method |
|-------------|----------|----------|---------------------|
| **iOS Development** | Dev certificate + device UDIDs + App ID | Running on test devices | Xcode → Device |
| **Ad Hoc** | Distribution certificate + device UDIDs + App ID | Testing builds on specific devices | IPA → Device |
| **App Store** | Distribution certificate + App ID (no devices) | App Store and TestFlight | App Store Connect |
| **Enterprise (In-House)** | Enterprise certificate + App ID (no devices) | Internal distribution | MDM or direct install |

#### 2.2 Profile Management

```bash
# List installed provisioning profiles
ls ~/Library/MobileDevice/Provisioning\ Profiles/

# Inspect a provisioning profile
security cms -D -i ~/Library/MobileDevice/Provisioning\ Profiles/xxx.mobileprovision

# Find profiles by App ID
for profile in ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision; do
    echo "=== $profile ==="
    security cms -D -i "$profile" 2>/dev/null | grep -A1 "application-identifier"
done

# Delete expired profiles
for profile in ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision; do
    EXPIRY=$(security cms -D -i "$profile" 2>/dev/null | \
        grep -A1 "ExpirationDate" | tail -1 | \
        sed 's/.*<date>\(.*\)<\/date>/\1/')
    if [[ "$EXPIRY" < "$(date -u +%Y-%m-%dT%H:%M:%SZ)" ]]; then
        echo "EXPIRED: $profile ($EXPIRY)"
        # rm "$profile"  # Uncomment to delete
    fi
done
```

#### 2.3 Provisioning Profile Inventory

```markdown
## Provisioning Profile Inventory

| Profile Name | Type | App ID | Certificate | Expires | Devices |
|-------------|------|--------|-------------|---------|---------|
| MyApp Dev | Development | com.company.myapp | Dev Cert 1 | 2026-08-15 | 25 |
| MyApp AdHoc | Ad Hoc | com.company.myapp | Dist Cert | 2026-08-15 | 50 |
| MyApp AppStore | App Store | com.company.myapp | Dist Cert | 2026-08-15 | N/A |
| MyApp Widget Dev | Development | com.company.myapp.widget | Dev Cert 1 | 2026-08-15 | 25 |
| MyApp Widget AppStore | App Store | com.company.myapp.widget | Dist Cert | 2026-08-15 | N/A |
| MyApp Notification | App Store | com.company.myapp.notification | Dist Cert | 2026-08-15 | N/A |

### App IDs and Capabilities
| App ID | Capabilities | Profiles Needed |
|--------|-------------|-----------------|
| com.company.myapp | Push, In-App Purchase, Sign in with Apple, App Groups | Dev, AdHoc, AppStore |
| com.company.myapp.widget | App Groups | Dev, AppStore |
| com.company.myapp.notification | Push, App Groups | Dev, AppStore |
```

---

### Phase 3: Signing Configuration

#### 3.1 Automatic Signing (Recommended for Development)

```markdown
### Xcode Automatic Signing Setup

1. Select target > Signing & Capabilities
2. Check "Automatically manage signing"
3. Select your team
4. Xcode will:
   - Create/update development certificate
   - Create/update provisioning profile
   - Register devices automatically
   - Manage entitlements

### When Automatic Signing Works Best
- Local development builds
- Running on personal test devices
- Small teams (< 10 developers)

### When to Use Manual Signing Instead
- CI/CD pipelines
- Distribution builds (App Store, Ad Hoc)
- Sharing signing credentials across machines
- Enterprise distribution
- Complex multi-target projects with specific profile requirements
```

#### 3.2 Manual Signing Configuration

```markdown
### Xcode Manual Signing Setup

1. Select target > Signing & Capabilities
2. Uncheck "Automatically manage signing"
3. For each configuration (Debug, Release):
   - Select the provisioning profile
   - Verify the certificate is correct

### Build Settings for Manual Signing
```
CODE_SIGN_STYLE = Manual
DEVELOPMENT_TEAM = XXXXXXXXXX
CODE_SIGN_IDENTITY = Apple Distribution
PROVISIONING_PROFILE_SPECIFIER = MyApp AppStore

# Per-configuration:
CODE_SIGN_IDENTITY[config=Debug] = Apple Development
PROVISIONING_PROFILE_SPECIFIER[config=Debug] = MyApp Dev
CODE_SIGN_IDENTITY[config=Release] = Apple Distribution
PROVISIONING_PROFILE_SPECIFIER[config=Release] = MyApp AppStore
```

### For extensions (must match app's team and prefix):
```
# Widget Extension
CODE_SIGN_IDENTITY[config=Release] = Apple Distribution
PROVISIONING_PROFILE_SPECIFIER[config=Release] = MyApp Widget AppStore
```
```

#### 3.3 Troubleshooting Common Signing Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "No signing certificate found" | Certificate not in keychain or expired | Download from Developer Portal or let Xcode manage |
| "Provisioning profile doesn't include signing certificate" | Profile and certificate mismatch | Regenerate profile with correct certificate |
| "A valid provisioning profile for this executable was not found" | Missing or expired profile | Download from Developer Portal or auto-manage |
| "The executable was signed with invalid entitlements" | Entitlements mismatch between app and profile | Verify capabilities in Developer Portal match Xcode |
| "Revoke certificate?" dialog | Xcode wants to create new cert | Only revoke if you know the old cert is unused |
| "No devices registered" (Ad Hoc) | UDID not in profile | Add device in Developer Portal, regenerate profile |

---

### Phase 4: CI/CD Signing

#### 4.1 Fastlane Match (Recommended)

```ruby
# File: Fastfile

lane :certificates do
    match(
        type: "development",
        app_identifier: ["com.company.myapp", "com.company.myapp.widget"],
        readonly: is_ci
    )
    match(
        type: "appstore",
        app_identifier: ["com.company.myapp", "com.company.myapp.widget"],
        readonly: is_ci
    )
end

lane :beta do
    certificates
    build_app(
        scheme: "MyApp",
        export_method: "app-store"
    )
    upload_to_testflight
end
```

```ruby
# File: Matchfile

git_url("https://github.com/company/certificates")
storage_mode("git")  # or "s3", "google_cloud"

type("appstore")
app_identifier(["com.company.myapp", "com.company.myapp.widget"])
team_id("XXXXXXXXXX")
```

#### 4.2 GitHub Actions Signing

```yaml
# File: .github/workflows/build.yml

jobs:
  build:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4

      - name: Install certificates
        env:
          CERTIFICATE_BASE64: ${{ secrets.DISTRIBUTION_CERTIFICATE_BASE64 }}
          CERTIFICATE_PASSWORD: ${{ secrets.CERTIFICATE_PASSWORD }}
          KEYCHAIN_PASSWORD: ${{ secrets.KEYCHAIN_PASSWORD }}
        run: |
          # Create temporary keychain
          security create-keychain -p "$KEYCHAIN_PASSWORD" build.keychain
          security set-keychain-settings -lut 21600 build.keychain
          security unlock-keychain -p "$KEYCHAIN_PASSWORD" build.keychain

          # Import certificate
          echo "$CERTIFICATE_BASE64" | base64 --decode > cert.p12
          security import cert.p12 -k build.keychain \
              -P "$CERTIFICATE_PASSWORD" \
              -T /usr/bin/codesign \
              -T /usr/bin/security
          security set-key-partition-list -S apple-tool:,apple: \
              -s -k "$KEYCHAIN_PASSWORD" build.keychain

          # Set default keychain
          security list-keychains -d user -s build.keychain login.keychain
          security default-keychain -s build.keychain

          # Clean up
          rm cert.p12

      - name: Install provisioning profile
        env:
          PROFILE_BASE64: ${{ secrets.PROVISIONING_PROFILE_BASE64 }}
        run: |
          echo "$PROFILE_BASE64" | base64 --decode > profile.mobileprovision
          mkdir -p ~/Library/MobileDevice/Provisioning\ Profiles
          cp profile.mobileprovision ~/Library/MobileDevice/Provisioning\ Profiles/
          rm profile.mobileprovision

      - name: Build and archive
        run: |
          xcodebuild archive \
              -workspace MyApp.xcworkspace \
              -scheme MyApp \
              -archivePath MyApp.xcarchive \
              -allowProvisioningUpdates \
              CODE_SIGN_STYLE=Manual \
              CODE_SIGN_IDENTITY="Apple Distribution" \
              PROVISIONING_PROFILE_SPECIFIER="MyApp AppStore"

      - name: Cleanup keychain
        if: always()
        run: security delete-keychain build.keychain
```

#### 4.3 Xcode Cloud Signing

```markdown
### Xcode Cloud Automatic Signing

Xcode Cloud manages signing automatically:
1. Connect your Apple Developer account in Xcode Cloud settings
2. Xcode Cloud creates and manages cloud-managed certificates
3. Provisioning profiles are created automatically

### Benefits
- No certificate/profile management needed
- No secrets to store
- Automatic renewal
- Apple-managed keychain

### Limitations
- Only works with Xcode Cloud
- Cannot use custom certificates
- Limited control over profile configuration
```

#### 4.4 Expiration Monitoring

```bash
#!/bin/bash
# File: Scripts/check_signing_expiry.sh

set -euo pipefail

WARN_DAYS=30
TODAY=$(date +%s)

echo "=== Certificate Expiration Check ==="

security find-identity -v -p codesigning | while read -r line; do
    if [[ "$line" =~ \"(.+)\" ]]; then
        CERT_NAME="${BASH_REMATCH[1]}"
        EXPIRY=$(security find-certificate -c "$CERT_NAME" -p 2>/dev/null | \
            openssl x509 -noout -enddate 2>/dev/null | \
            sed 's/notAfter=//')
        if [ -n "$EXPIRY" ]; then
            EXPIRY_TS=$(date -jf "%b %d %H:%M:%S %Y %Z" "$EXPIRY" +%s 2>/dev/null || echo 0)
            DAYS_LEFT=$(( (EXPIRY_TS - TODAY) / 86400 ))
            if [ "$DAYS_LEFT" -lt 0 ]; then
                echo "EXPIRED: $CERT_NAME (expired $EXPIRY)"
            elif [ "$DAYS_LEFT" -lt "$WARN_DAYS" ]; then
                echo "WARNING: $CERT_NAME expires in $DAYS_LEFT days ($EXPIRY)"
            else
                echo "OK: $CERT_NAME expires in $DAYS_LEFT days ($EXPIRY)"
            fi
        fi
    fi
done

echo ""
echo "=== Provisioning Profile Expiration Check ==="

for profile in ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision; do
    NAME=$(security cms -D -i "$profile" 2>/dev/null | grep -A1 "<key>Name</key>" | tail -1 | sed 's/.*<string>\(.*\)<\/string>/\1/')
    EXPIRY=$(security cms -D -i "$profile" 2>/dev/null | grep -A1 "ExpirationDate" | tail -1 | sed 's/.*<date>\(.*\)<\/date>/\1/')
    if [ -n "$EXPIRY" ]; then
        EXPIRY_TS=$(date -jf "%Y-%m-%dT%H:%M:%SZ" "$EXPIRY" +%s 2>/dev/null || echo 0)
        DAYS_LEFT=$(( (EXPIRY_TS - TODAY) / 86400 ))
        if [ "$DAYS_LEFT" -lt 0 ]; then
            echo "EXPIRED: $NAME ($EXPIRY)"
        elif [ "$DAYS_LEFT" -lt "$WARN_DAYS" ]; then
            echo "WARNING: $NAME expires in $DAYS_LEFT days"
        else
            echo "OK: $NAME expires in $DAYS_LEFT days"
        fi
    fi
done
```

---

## Expected Output

### Signing Management Report

```markdown
# Code Signing Report - [Project Name]

## Certificate Status
| Certificate | Type | Expires | Days Left | Status |
|-------------|------|---------|-----------|--------|
| [name] | [type] | [date] | [N] | [OK/Warning/Expired] |

## Provisioning Profile Status
| Profile | Type | App ID | Expires | Status |
|---------|------|--------|---------|--------|
| [name] | [type] | [id] | [date] | [OK/Warning/Expired] |

## CI/CD Signing Configuration
- Method: [Fastlane match / Manual / Xcode Cloud]
- Secrets location: [GitHub Secrets / Vault / etc.]
- Last verified: [date]

## Action Items
- [ ] [Renew certificate X before date Y]
- [ ] [Update CI secrets after renewal]
- [ ] [Add new device UDID to Ad Hoc profile]
```

### Implementation Checklist

- [ ] Certificate inventory documented with expiration dates
- [ ] Provisioning profiles inventoried for all App IDs and extensions
- [ ] Automatic signing configured for development
- [ ] Manual signing configured for distribution builds
- [ ] CI/CD signing workflow established and tested
- [ ] Certificate and private key backed up securely
- [ ] Expiration monitoring script or calendar reminders set up
- [ ] New developer onboarding process documented
- [ ] Signing troubleshooting guide available for the team

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on reliable code signing management
- **ST-02** (Sequential Instructions): Phased approach from certificates to CI/CD to monitoring

---

## Related Prompts

- [ios_dependency_update.md](ios_dependency_update.md) - Dependency updates may require signing changes
- [ios_xcode_build_optimization.md](ios_xcode_build_optimization.md) - Build pipeline includes signing
- [ios_version_upgrade.md](ios_version_upgrade.md) - Version upgrades may require entitlement changes

---
title: "Android Manifest & Permissions Audit"
category: mobile-development
description: "Audits AndroidManifest.xml and the permission model for over-requested or dangerous permissions, unsafe exported components, intent-filter exposure, backup/cleartext flags, and runtime-permission flow correctness."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - android
  - manifest
  - permissions
  - security
  - exported-components
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_privacy_data_flow_audit.md
  - domain-software-engineering/mobile/android/analysis/android_local_data_security_audit.md
  - domain-software-engineering/mobile/android/publishing/android_privacy_compliance.md
---

# Android Manifest & Permissions Audit

**Objective:** Audit `AndroidManifest.xml` (merged across modules and libraries) and the app's permission model to surface over-requested or dangerous permissions, unsafely exported components, over-broad intent filters, risky application flags (`allowBackup`, cleartext traffic), missing `<queries>` declarations, and incorrect runtime-permission flows — reporting each finding with location, risk, and a concrete remediation.

**When to Use:** Use this before a release, during a security review, when preparing a Play Store Data Safety / permissions declaration, after adding an SDK that may inject permissions, or when targeting a new `targetSdkVersion` that changes permission/visibility behavior.

---

## Context Gathering

1. **Build inputs:** "Can you share the app's `AndroidManifest.xml` files (app + library modules) and, ideally, the merged manifest from a build?"
2. **Target SDK:** "What `compileSdk` / `targetSdk` does the app use?"
3. **Feature intent:** "What capabilities does the app legitimately need (camera, location, contacts, background work, deep links)?"
4. **Distribution:** "Google Play, alternative stores, or enterprise/MDM?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Read the merged manifest, not just the app module** — libraries and `manifestPlaceholders` inject permissions and components. Confirm the source of each entry where possible.
2. **Tie every permission to a feature** — a permission is "over-requested" only if no code path uses it. Search call sites before flagging.
3. **Confirm component reachability** — an `exported` component is a risk only if it performs sensitive actions or trusts unvalidated input.
4. **Account for target SDK behavior** — default `exported`, scoped storage, package visibility, and notification/permission prompts vary by API level.

**A lean, correctly-scoped manifest is an acceptable outcome.** Don't invent risk.

### False-Positive Prevention

- ❌ Do NOT flag a permission that has a real, traced call site as "unnecessary."
- ❌ Do NOT flag `exported="true"` on the launcher activity or intentionally public deep-link entry points.
- ❌ Do NOT flag library-injected permissions without noting they're library-sourced and whether they're actually exercised.
- ❌ Do NOT assume `allowBackup="true"` is wrong — flag it only when sensitive data could be exfiltrated via backup.
- ✅ DO flag dangerous/`signature`-level permissions with no code usage.
- ✅ DO flag exported components without permission guards that accept actionable intents.
- ✅ DO flag cleartext traffic enabled for non-localhost endpoints.

---

### Phase 1: Manifest & Permission Inventory

| Item | What to Extract |
|------|-----------------|
| Declared permissions | `<uses-permission>` incl. `maxSdkVersion`, dangerous vs normal vs signature |
| Library-injected permissions | Permissions present only in the merged manifest |
| Feature requirements | `<uses-feature>` and `required` flags (Play filtering) |
| Components | Activities, services, receivers, providers — `exported` value + `permission` guard |
| Intent filters | Actions/categories/data — which components are reachable externally |
| Application flags | `allowBackup`, `fullBackupContent`/`dataExtractionRules`, `usesCleartextTraffic`, `networkSecurityConfig`, `debuggable` |
| Package visibility | `<queries>` vs `QUERY_ALL_PACKAGES` |

---

### Phase 2: Permission Risk Analysis

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Unused dangerous permission | HIGH | Declared `CAMERA`/`LOCATION`/`CONTACTS`/`RECORD_AUDIO` with no traced usage |
| Over-broad location | HIGH | `ACCESS_BACKGROUND_LOCATION` or fine location when coarse/foreground suffices |
| `QUERY_ALL_PACKAGES` | HIGH | Used where targeted `<queries>` would satisfy the need (Play policy risk) |
| Legacy storage | MEDIUM | `WRITE/READ_EXTERNAL_STORAGE` without correct `maxSdkVersion` under scoped storage |
| Signature/system permissions | MEDIUM | Requested without the privilege to be granted |
| Permission–feature mismatch | MEDIUM | Permission with no matching `<uses-feature>` or runtime request |

---

### Phase 3: Component Exposure Analysis

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Unguarded exported component | CRITICAL | `exported="true"` service/receiver/activity doing sensitive work without a `permission` |
| Implicitly exported | HIGH | Component with an intent filter and no explicit `exported` on API 31+ (build error) or legacy implicit export |
| Exported ContentProvider | CRITICAL | Provider exported without `grantUriPermissions` discipline / path permissions |
| Intent redirection | HIGH | Exported component forwarding untrusted intents/extras |
| PendingIntent mutability | HIGH | Mutable `PendingIntent` handed to other apps |
| Deep-link trust | MEDIUM | Exported deep-link activity acting on unvalidated URI params |

---

### Phase 4: Application-Flag & Transport Hardening

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Backup of sensitive data | HIGH | `allowBackup="true"` with credentials/PII and no `dataExtractionRules` exclusions |
| Cleartext traffic | HIGH | `usesCleartextTraffic="true"` or permissive `networkSecurityConfig` for real endpoints |
| Debuggable in release | CRITICAL | `debuggable="true"` reachable in a release variant |
| Missing network config | LOW | No `networkSecurityConfig` where cert pinning/trust anchors would help |

---

## Output Format

```markdown
## Android Manifest & Permissions Audit Report

### Permission Inventory
| Permission | Level | Source (app/library) | Used? (file:line) | Verdict |
|------------|-------|----------------------|-------------------|---------|

### Component Exposure
| Component | Type | exported | Guarded? | Risk |
|-----------|------|----------|----------|------|

### Findings (severity-ordered)
**[SEVERITY] Area: title**
- Location: `AndroidManifest.xml:line` (or merged manifest)
- Risk: concrete attack/abuse or policy consequence
- Fix: exact manifest/code change

### Prioritized Remediation
- P1 / P2 / P3 …

### Play Policy / Data Safety Implications
- (Permissions that require declaration or justification.)
```

---

## Expected Output

1. **Permission inventory** with usage verdicts.
2. **Component-exposure table.**
3. **Severity-rated findings** with locations and fixes.
4. **Play policy implications** for the permission set.

---

## Techniques Used

- **ST-01** (Clear Objective): Manifest/permission scope only.
- **ST-02** (Structured Sequential Instructions): Inventory → permissions → components → flags.
- **RT-02** (Multi-Dimensional Analysis): Security + policy + correctness angles.
- **RT-05** (Evidence-Based Reasoning): Traced usage + locations.
- **DS-06** (Prioritization Guidance): Severity ordering.
- **QA-02** (Edge Case Coverage): Target-SDK behavior changes, library injection.

---

## Related Prompts

- [android_privacy_data_flow_audit.md](android_privacy_data_flow_audit.md) - Where permission-gated data flows next
- [android_local_data_security_audit.md](android_local_data_security_audit.md) - At-rest storage of permission-gated data
- [android_privacy_compliance.md](../publishing/android_privacy_compliance.md) - Translate findings into Play declarations

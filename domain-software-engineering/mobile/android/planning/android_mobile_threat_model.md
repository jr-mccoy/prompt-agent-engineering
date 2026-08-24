---
title: "Android Mobile Threat Model (Planning-Stage)"
category: mobile-development
description: "Produce a planning-stage threat model for an Android app so security is designed in, not audited in later — identifying assets and trust boundaries, enumerating Android-specific attack surface, applying STRIDE with concrete Android examples, deciding secrets/data-at-rest/in-transit/auth strategy, and emitting a prioritized mitigation backlog."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-02
  - AG-12
  - RT-09
difficulty: advanced
tags:
  - android
  - threat-modeling
  - security-by-design
  - stride
  - attack-surface
  - app-security
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - android_architecture_selection.md
  - ../analysis/android_authentication_security_audit.md
  - ../analysis/android_local_data_security_audit.md
  - ../analysis/android_manifest_permissions_audit.md
---

# Android Mobile Threat Model (Planning-Stage)

**Objective:** Produce a structured, planning-stage threat model for an Android application so security is designed into the architecture rather than discovered in a late audit — identifying the assets worth protecting and the trust boundaries around them, enumerating the Android-specific attack surface (exported components, intents, deep/app links, WebView bridges, content providers, broadcast receivers, `PendingIntent` mutability, IPC), applying STRIDE to a mobile client with concrete Android examples, making explicit decisions on secrets handling, data-at-rest, data-in-transit, and auth/session, and emitting a prioritized mitigation backlog cross-referenced to the later security-audit prompts.

**When to Use:** Use this prompt after you have selected an architecture and tech stack but before writing security-sensitive code — anything involving authentication, tokens, local data persistence, payments, deep links, WebViews, or inter-app communication. Also use it when adding a sensitive feature to an existing app (login, in-app purchases, a JS bridge, a new exported component) and you need to reason about what could go wrong before you build it.

**Sequence Map:** Use after `android_architecture_selection.md` and `android_tech_stack_selection.md`; use before security-sensitive implementation and before the audit-stage prompts in `../analysis/`.

**Important context:** A mobile client is fundamentally a hostile-environment program: it runs on devices you do not control, can be rooted, repackaged, decompiled, and run under instrumentation. Treat the APK as fully readable by an adversary — anything shipped inside it (keys, endpoints, logic) is known to the attacker. Android adds a rich, underestimated local attack surface: components are reachable by other apps unless you lock them down, intents and deep links carry attacker-controlled data, WebView JS bridges can become remote-code paths, and `PendingIntent` and IPC mistakes leak capabilities. Threat modeling at planning time is cheap; the same decisions made after launch (a hardcoded key, an exported provider, a mutable `PendingIntent`) become breaking changes, incident reports, and store takedowns. This prompt is a structured-thinking exercise, not a code audit — its output is a set of design decisions and a backlog, which the `../analysis/` prompts later verify against real code.

---

## Context Gathering

1. **App Shape & Stack:**
   - "What does the app do, and what is the architecture (single-module/multi-module, MVVM/MVI, native/Compose, any KMP)?"
   - "Is there a backend? What does the client talk to (your API, third-party APIs, Firebase)?"
   - "Does the app embed a WebView or any JS bridge? Any payments or in-app purchases?"

2. **Assets:**
   - "What user data does the app hold (PII, messages, health, financial, media)?"
   - "What credentials/secrets exist (auth tokens, refresh tokens, API keys, encryption keys)?"
   - "What would an attacker most want — account takeover, data exfiltration, fraud, impersonation?"

3. **Entry Points:**
   - "Which components are or might be exported (activities, services, receivers, providers)?"
   - "Do you handle deep links or App Links? What actions can a link trigger?"
   - "Does any component accept input from other apps or from notifications/`PendingIntent`s?"

4. **Auth & Storage:**
   - "How do users authenticate (password, OAuth, biometric, magic link)?"
   - "Where do tokens live, and how long are sessions valid?"
   - "What is stored locally, and is any of it sensitive?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before declaring the threat model complete, you MUST:**

1. **Treat the APK as readable** — assume the attacker has decompiled the app; no secret in the binary is secret.
2. **Enumerate every entry point** — every exported component, intent filter, deep link, bridge, and IPC channel is attack surface until proven otherwise.
3. **Ground each STRIDE entry in a concrete Android example** — no abstract "tampering risk"; name the component and the attack.
4. **Make explicit, defensible decisions** — for secrets, data-at-rest, data-in-transit, and auth, state the chosen mechanism and the tradeoff.
5. **Prioritize the backlog** — order mitigations by exploitability × impact, and map each to a verification prompt.

**A small, well-justified threat model is better than an exhaustive list of theoretical risks.** Focus on what is reachable and impactful for *this* app.

### False-Positive Prevention

- ❌ Do NOT propose obfuscation or root detection as a substitute for keeping secrets off the device
- ❌ Do NOT mark a component "safe" because it is not *currently* used by other apps — check `exported`
- ❌ Do NOT assume TLS alone defends a high-value flow without considering pinning tradeoffs
- ❌ Do NOT treat certificate pinning as free — account for rotation/bricking risk before mandating it
- ❌ Do NOT list every STRIDE category for every asset — only where a real Android vector exists
- ✅ DO start from assets and trust boundaries, then derive threats from reachable entry points
- ✅ DO name the specific Android mechanism (exported provider, mutable `PendingIntent`, JS bridge) in each threat
- ✅ DO push secrets server-side and use Play Integrity / attestation for client trust
- ✅ DO rank mitigations and tie each to the audit prompt that will later verify it

---

### Phase 1: Assets & Trust Boundaries

Identify what is worth protecting and where control changes hands.

**Asset inventory:**

| Asset | Type | Where It Lives | Impact if Compromised |
|-------|------|----------------|-----------------------|
| Auth/refresh tokens | Credential | On-device storage | Account takeover |
| User PII / content | Data | On-device + backend | Privacy breach, regulatory |
| Encryption keys | Key material | Android Keystore (target) | Decrypts at-rest data |
| Backend API | Service | Remote | Data exfiltration, abuse |
| Payment/entitlement state | Data | Backend (authoritative) | Fraud, unlocked premium |

**Trust boundaries (where data crosses a control change):**

```
[ Other apps on device ] --intent/link/IPC--> [ Your app process ]   <- boundary 1
[ Your app process ]     --local storage-----> [ Device filesystem ] <- boundary 2
[ Your app process ]     --network------------> [ Your backend ]      <- boundary 3
[ Your backend ]         --calls--------------> [ Third-party APIs ]  <- boundary 4
[ WebView content ]      --JS bridge----------> [ Native code ]       <- boundary 5
```

> The most dangerous boundaries are 1 (untrusted apps reach your components) and 5 (web content reaches native capabilities). Mark which boundaries this app actually has.

**CHECKPOINT 1 — Asset/boundary review:** Present the inventory and boundary map. Confirm the high-value assets before enumerating attack surface.

---

### Phase 2: Android Attack-Surface Enumeration

Walk each Android-specific surface and record exposure decisions.

| Surface | Risk | Decision/Hardening |
|---------|------|--------------------|
| **Exported components** | Other apps invoke activities/services/receivers | Default `android:exported="false"`; export only with a signature permission or explicit need |
| **Intents** | Attacker-controlled extras / implicit-intent hijack | Validate all extras; prefer explicit intents; never trust intent data as authenticated |
| **Intent redirection** | App forwards an attacker-supplied intent to a privileged target | Never re-launch a `parcelable`/`extra` intent received from outside without validation |
| **Deep links / App Links** | Link triggers a sensitive action or carries injection | Use verified **App Links** (autoVerify + Digital Asset Links); treat link params as untrusted input |
| **WebView / JS bridges** | `@JavascriptInterface` exposes native methods to web content | Avoid bridges; if required, load only trusted content, disable file access, minimize exposed surface |
| **Content providers** | Exported provider leaks/accepts data; SQL/path injection | Keep providers unexported; parameterize queries; validate URIs/paths |
| **Broadcast receivers** | Spoofed broadcasts trigger actions; eavesdropping | Use `LocalBroadcastManager`/explicit receivers; require permissions on sensitive broadcasts |
| **`PendingIntent` mutability** | Mutable `PendingIntent` lets another app fill in/redirect it | Use `FLAG_IMMUTABLE` by default; set explicit component; share only when necessary |
| **IPC (bound services/AIDL)** | Unprotected interface exposes capabilities | Enforce caller permission/signature checks on every IPC entry |
| **Backup / debuggable** | Cloud/ADB backup leaks data; debug build shipped | Set `allowBackup` deliberately, exclude secrets; never ship `debuggable=true` |
| **Logging** | Tokens/PII written to logcat | No sensitive data in logs; strip in release |

---

### Phase 3: STRIDE Applied to the Android Client

For each STRIDE category, record concrete, reachable Android threats and the planned mitigation.

| STRIDE | Concrete Android Threat (example) | Affected Asset/Boundary | Planned Mitigation |
|--------|-----------------------------------|-------------------------|--------------------|
| **S — Spoofing** | Malicious app sends a forged broadcast/intent the app trusts as the system; phishing app mimics login | Boundary 1; tokens | Verify caller identity; require signature permissions; server-side auth, never trust client identity |
| **T — Tampering** | Attacker repackages APK, hooks methods (Frida), or modifies local DB to unlock premium | Boundary 2; entitlement state | Make backend authoritative for entitlements; Play Integrity attestation; integrity-check critical responses |
| **R — Repudiation** | User/attacker denies an action; no trustworthy audit trail | Backend | Server-side, timestamped, append-only logs of sensitive actions; don't rely on client logs |
| **I — Information disclosure** | Hardcoded API key in APK; tokens in `SharedPreferences` plaintext; PII in logcat; exported provider leak | Boundary 2; secrets, PII | No secrets in APK; encrypt at rest (Keystore-backed); unexport providers; scrub logs |
| **D — Denial of service** | Malformed deep link / intent extra crashes a component; oversized payload | Boundary 1 | Validate/limit all external input; fail closed; don't let one component crash the app |
| **E — Elevation of privilege** | Intent redirection or mutable `PendingIntent` lets a low-privilege app reach a privileged action; JS bridge → native call | Boundaries 1 & 5 | `FLAG_IMMUTABLE`; validate forwarded intents; eliminate/lock down JS bridges; enforce IPC permission checks |

> Populate only the cells that have a real vector for this app. Use **RT-09** reasoning: name the cause (mechanism), the symptom (what the attacker achieves), and the fix (the mitigation).

---

### Phase 4: Secrets Strategy

State the decision explicitly — the governing rule is **no secret survives in the APK**.

| Secret Type | WRONG (do not) | Planned Approach |
|-------------|----------------|------------------|
| Backend API keys | Hardcode in code/`BuildConfig`/`strings.xml`/NDK | Keep server-side; client calls your backend, which holds the key |
| Signing/encryption keys | Bundle in assets | Generate/store in **Android Keystore**; never export key material |
| Third-party secrets (e.g., payment server keys) | Embed in client | Server-side only; client gets short-lived tokens |
| Client-trust proof | "Hidden" key + obfuscation | **Play Integrity API** / app attestation; treat as signal, not a gate |
| Certificate handling | Trust-all / disabled validation | Standard system trust; consider pinning (Phase 6) with rotation plan |

> Obfuscation (R8) and root/tamper detection raise the cost of attack but **never** make a shipped secret safe — design as if the attacker reads everything in the APK.

---

### Phase 5: Data-at-Rest Decisions

| Data Sensitivity | Mechanism | Notes |
|------------------|-----------|-------|
| Non-sensitive prefs | DataStore / `SharedPreferences` | Fine for non-secret config |
| Tokens & small secrets | Keystore-backed encrypted storage | Use a maintained encrypted-preferences approach backed by the Android Keystore |
| Sensitive DB content | **SQLCipher** or field-level encryption with Keystore-held key | Key never leaves Keystore; consider `setUserAuthenticationRequired` for high-value keys |
| Cached files / media | Scoped app-internal storage; encrypt if sensitive | Avoid external/world-readable storage for anything sensitive |
| Backups | Configure `allowBackup`/backup rules | Exclude tokens and secrets from cloud/ADB backup |

---

### Phase 6: Data-in-Transit Decisions

| Concern | Decision | Tradeoff to Record |
|---------|----------|--------------------|
| Transport | TLS for all traffic; cleartext disabled via Network Security Config | Baseline, non-negotiable |
| Certificate pinning | Pin only high-value flows (auth, payments) | Pinning can **brick** the app on cert rotation — require a remote-config kill-switch and overlapping backup pins before mandating |
| Trust configuration | No custom trust-all `TrustManager`; no user-CA trust in release | Prevents trivial MITM via installed proxy certs |
| Sensitive params | Never in URL/query (logged by proxies/servers) | Put in headers/body |

> Document the pinning decision either way — choosing **not** to pin is a valid, recorded decision with its own rationale.

---

### Phase 7: Auth & Session Threats

| Threat | Risk | Mitigation Decision |
|--------|------|---------------------|
| Token theft from device | Account takeover | Store tokens in Keystore-backed storage; short-lived access tokens + rotating refresh tokens |
| Session fixation | Reused session after privilege change | Issue a fresh session/token server-side on login and privilege elevation; invalidate old ones |
| Biometric bypass | Attacker reaches gated feature without auth | Bind biometric to a Keystore key requiring user auth — biometric must unlock crypto, not just toggle a boolean |
| Refresh-token replay | Long-lived access after theft | Server-side refresh-token rotation + revocation; detect reuse |
| Insecure logout | Token usable after logout | Invalidate server-side on logout; clear local token store |

---

### Phase 8: Prioritized Mitigation Backlog

Rank every mitigation and route it to the prompt that will later verify it in code.

| Priority | Mitigation | Exploitability | Impact | Verify With |
|----------|------------|----------------|--------|-------------|
| P0 | Remove all secrets/keys from APK; move to backend | High | Critical | `../analysis/android_local_data_security_audit.md` |
| P0 | Set every component `exported="false"` unless required; protect exported ones | High | High | `../analysis/android_manifest_permissions_audit.md` |
| P0 | All `PendingIntent`s `FLAG_IMMUTABLE` + explicit component | Medium | High | `../analysis/android_manifest_permissions_audit.md` |
| P1 | Keystore-backed token/secret storage; biometric bound to Keystore key | Medium | Critical | `../analysis/android_authentication_security_audit.md` |
| P1 | Validate all deep-link/intent input; verified App Links | High | Medium | `../analysis/android_manifest_permissions_audit.md` |
| P1 | Eliminate/lock down WebView JS bridges; trusted content only | Medium | High | `../analysis/android_local_data_security_audit.md` |
| P2 | Encrypt sensitive DB (SQLCipher/field-level) | Low | High | `../analysis/android_local_data_security_audit.md` |
| P2 | Certificate pinning for auth/payment flows (with rotation plan) | Low | Medium | `../analysis/android_authentication_security_audit.md` |

**CHECKPOINT 2 — Backlog sign-off:** Present the ranked backlog and confirm P0/P1 items are accepted as design constraints before implementation begins.

---

## Expected Output

1. **Asset Inventory & Trust-Boundary Map** — what is protected and where control changes hands
2. **Attack-Surface Table** — every Android entry point with its exposure decision
3. **STRIDE Table** — concrete, reachable Android threats per category with mitigations
4. **Secrets Strategy** — explicit decisions, anchored to "nothing secret in the APK"
5. **Data-at-Rest Decisions** — storage mechanism per sensitivity level
6. **Data-in-Transit Decisions** — TLS, pinning tradeoff, trust config
7. **Auth/Session Threat Decisions** — token storage, rotation, biometric binding, logout
8. **Prioritized Mitigation Backlog** — ranked by exploitability × impact, each mapped to a verification prompt

---

## CRITICAL: Verification Requirements

- [ ] Assets and trust boundaries are identified before threats are derived
- [ ] Every exported/exportable component has an explicit exposure decision
- [ ] Deep links/App Links and all intent input are treated as untrusted and validated
- [ ] WebView JS bridges are eliminated or explicitly locked down to trusted content
- [ ] All `PendingIntent`s default to `FLAG_IMMUTABLE` with an explicit component
- [ ] No secret/key is shipped in the APK; client trust uses Play Integrity / attestation
- [ ] Data-at-rest decision uses Keystore-backed storage (and SQLCipher/field encryption for sensitive DBs)
- [ ] Data-in-transit decision records the certificate-pinning tradeoff and a rotation plan
- [ ] Token storage, refresh rotation, session-fixation, and biometric-binding are addressed
- [ ] Every mitigation is prioritized and mapped to a later security-audit prompt

## False-Positive Prevention

- ❌ Do NOT rely on obfuscation/root detection in place of keeping secrets off the device
- ❌ Do NOT assume a component is safe without checking its `exported` state and intent filters
- ❌ Do NOT mandate certificate pinning without a rotation/kill-switch plan
- ❌ Do NOT enumerate theoretical STRIDE entries with no reachable Android vector
- ❌ Do NOT treat a biometric prompt that flips a boolean as real protection
- ✅ DO derive threats from real, reachable entry points and high-value assets
- ✅ DO make backend authoritative for entitlements, identity, and audit trails
- ✅ DO name the specific Android mechanism behind each threat (cause → impact → fix)
- ✅ DO produce a ranked backlog that the `../analysis/` audits can later verify

## Techniques Used

- **ST-01** (Clear Objective): Focused on a planning-stage threat model that drives design decisions
- **ST-02** (Sequential Instructions): Assets → surface → STRIDE → secrets/storage/transit/auth → backlog
- **RT-02** (Multi-Dimensional Analysis): Each asset examined across the six STRIDE dimensions and multiple boundaries
- **AG-02** (Skeptical Default Stance): Assumes a hostile device and a fully readable APK by default
- **AG-12** (Quantitative Metrics): Backlog ranked by exploitability × impact for objective prioritization
- **RT-09** (Root Cause Explanation): Each threat expressed as mechanism → attacker outcome → mitigation

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) — Choose the architecture this threat model secures
- [../analysis/android_authentication_security_audit.md](../analysis/android_authentication_security_audit.md) — Verify auth/session mitigations against real code
- [../analysis/android_local_data_security_audit.md](../analysis/android_local_data_security_audit.md) — Verify data-at-rest and secrets decisions in the codebase
- [../analysis/android_manifest_permissions_audit.md](../analysis/android_manifest_permissions_audit.md) — Verify exported components, `PendingIntent`, and deep-link hardening

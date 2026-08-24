---
title: "Android-Specific Security and Privacy Audit of a Vibe-Coded App"
category: software-engineering/vibe-coding-rescue/android
description: "Audit a vibe-coded Android app for the security and privacy defects AI generation tends to produce on Android specifically — exported components without explicit flags, intent-filter hijacking, deeplink validation gaps, WebView misconfiguration (JS interface, file access), insecure network (cleartext, missing cert pinning), data-at-rest in plain SharedPreferences, unencrypted Room, permissions overreach, hand-rolled auth, missing input validation, secrets in code or resources, PII in logs, SDK-version-gated security gaps. Produces evidence-cited findings with severity, exploitability under the actual deployment, and remediation pointing to platform primitives. Refuses keyword-match findings."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-01
  - RT-05
  - RT-07
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - vibe-coding
  - android
  - security
  - privacy
  - manifest
  - webview
  - intents
  - deeplinks
  - encryption
  - permissions
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_prioritization.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md
  - domain-software-engineering/mobile/android/analysis/android_authentication_security_audit.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
---

# Android-Specific Security and Privacy Audit of a Vibe-Coded App

**Purpose:** AI-generated Android code has a characteristic security and privacy failure profile: it gets `android:exported` flags wrong (or omits them), opens WebViews with `setJavaScriptEnabled(true)` plus `addJavascriptInterface`, accepts any host on deeplinks, stores auth tokens in plain SharedPreferences, asks for permissions it doesn't need, hand-rolls auth where the AndroidX Security or Credentials APIs exist, logs PII at debug level, and ships secrets in `BuildConfig` or `strings.xml`. This audit targets those Android-specific patterns, traces actual data and intent flows, assigns severity grounded in the app's real deployment posture, and points remediation at platform primitives rather than generic OWASP guidance.

**When to use:**
- The wall-diagnosis prompt flagged A7 (hand-rolled auth/security) or A8 (WebView/Intent abuse).
- The app is going to the Play Store, is in the Play Store, or handles user PII / credentials / payments / location / health data.
- Before handoff to a new engineer or a security reviewer.
- Periodically as part of a maintenance cadence on any AI-generated Android app.

**Don't use when:** The app is a throwaway prototype with no real users and no sensitive data, AND nothing it does crosses a trust boundary. Use the fragility audit (`android_viberescue_codebase_audit.md`) only.

**Audience:** The engineer, a security reviewer, or both. Output is a findings report ready for remediation.

**Agent portability note:** Written for any coding agent (Claude Code, Codex, Cursor). Use whatever file-reading and search tools your agent provides when instructed to "read X" or "search for Y."

---

## Inputs Required

Refuse to audit without 1, 2, 3, 4, and 5.

1. **Project root path** (absolute path to the repo).
2. **Build configuration.** `minSdk`, `targetSdk`, `compileSdk`, AGP version, Kotlin version. (Some platform protections kick in at specific SDK levels — must know.)
3. **Deployment posture.** Play Store / sideloaded / enterprise MDM / internal only / Android Auto / Wear OS / TV. Public release yes/no.
4. **Data sensitivity.** What the app handles: PII (define what kind), credentials, financial, health, location, contacts, photos, voice, biometrics, payment cards, child user data (COPPA), EU user data (GDPR), CA user data (CCPA). Regulatory posture.
5. **Auth model.** What kind of auth: none, OAuth (which provider), Firebase Auth, custom backend with tokens, biometric, SSO. How tokens / sessions are stored.
6. **Threat model in 1–3 sentences.** Who you're defending against: opportunistic attacker, malicious app on the same device, lost / stolen device, network attacker on hostile Wi-Fi, malicious user, supply-chain attacker. Be explicit.
7. **Optional: known concerns.** Files or flows you suspect.

---

## Instructions

### Step 1 — Establish scope and evidence rule

Audit scope:

- Every file in `AndroidManifest.xml` (all modules).
- Every Activity / Service / BroadcastReceiver / ContentProvider in code.
- Every WebView usage.
- Every deeplink intent filter.
- Every PendingIntent construction.
- Every network call (Retrofit / OkHttp / Ktor / HttpURLConnection / WebSocket).
- Every persistence write (SharedPreferences, DataStore, Room, file I/O, `getExternalFiles*`).
- Every permission requested in the manifest and in code.
- Every `BuildConfig` field and every secret-shaped string in resources.
- Every `Log.*` call (especially `Log.d` and `Log.v`).
- Every cryptographic API call.

Every finding MUST cite file + line range. No findings without evidence.

### Step 2 — Run each Android-specific security category

For each, scan and collect findings.

#### 2.1 Manifest and exported components
- Activities, Services, Receivers, Providers without explicit `android:exported`. (Required since `targetSdk` 31 if intent filters present.)
- `android:exported="true"` on components that have no business being external.
- Intent filters with `action` patterns that match unexpectedly broadly.
- `<provider>` with `android:exported="true"` and no `android:permission`.
- `android:grantUriPermissions="true"` without bounded `<grant-uri-permission>` declarations.
- `<intent-filter>` with `<data android:scheme="http">` or other unbounded data patterns.
- Missing `android:permission` on Services / Receivers that should be permission-gated.
- `tools:node="merge"` swallowing security-relevant declarations from libraries.

#### 2.2 Deeplinks and App Links
- Deeplink hosts not validated against an allow-list before use.
- Deeplinks that pass user-supplied parameters into sensitive actions (purchase, account deletion, transfer) without re-authentication.
- App Links (`autoVerify="true"`) without the `assetlinks.json` file deployed and verified.
- Custom scheme deeplinks (`myapp://`) where App Links should be used for verified handling.
- Deeplink targets that open WebView with the deeplinked URL (XSS-equivalent inside the app).

#### 2.3 WebView configuration
- `WebSettings.setJavaScriptEnabled(true)` without justification.
- `addJavascriptInterface(...)` exposing arbitrary objects.
- `setAllowFileAccess(true)`, `setAllowFileAccessFromFileURLs(true)`, `setAllowUniversalAccessFromFileURLs(true)`.
- `setMixedContentMode(MIXED_CONTENT_ALWAYS_ALLOW)`.
- WebView loading user-controlled URLs without allow-list.
- Missing `WebViewClient` (default falls back to system browser for sub-URLs — sometimes wanted, sometimes a leak).
- `onReceivedSslError` overridden to call `proceed()`.
- WebView pre-rendering attacker-controlled content with cookies attached.

#### 2.4 Intents and PendingIntents
- Implicit intents to `ACTION_VIEW` with user-controlled URIs that may resolve to attacker components.
- PendingIntent without `FLAG_IMMUTABLE` (required on API 31+).
- `Intent.setComponent` with class names built from user input.
- `startActivityForResult` callbacks that don't validate the result Uri / data origin.
- Sticky broadcasts (deprecated and insecure).
- Custom permissions defined with `protectionLevel="normal"` where `signature` is needed.

#### 2.5 Network security
- `usesCleartextTraffic="true"` in manifest (or default on `targetSdk` < 28 not overridden).
- Missing `network_security_config.xml` for production apps.
- Certificate pinning absent for sensitive endpoints (banking, auth, payments, health).
- `HostnameVerifier` overridden to return true.
- `X509TrustManager` accepting all certs (`checkServerTrusted` no-op).
- Cleartext URLs (`http://`) anywhere outside test code.
- WebSocket connections over `ws://` for sensitive data.

#### 2.6 Data at rest
- Auth tokens, refresh tokens, or session IDs in plain `SharedPreferences`.
- Tokens or PII in unencrypted Room database.
- Sensitive data written to `getExternalFilesDir()` / external storage where other apps may read.
- Keystore use missing for credential-protecting keys.
- `EncryptedSharedPreferences` / `EncryptedFile` not used where appropriate.
- Backup enabled (`android:allowBackup="true"` — default) without `fullBackupContent` rules excluding sensitive paths.
- `android:debuggable="true"` reachable in release builds.

#### 2.7 Permissions hygiene
- Permissions declared in manifest but never requested or used.
- Dangerous permissions (location, camera, contacts, SMS, call log) requested at app start instead of in-context.
- `READ_EXTERNAL_STORAGE` / `WRITE_EXTERNAL_STORAGE` declared when scoped storage (API 29+) is appropriate.
- `MANAGE_EXTERNAL_STORAGE` requested without Play Store justification.
- `QUERY_ALL_PACKAGES` requested without justification.
- Background location (`ACCESS_BACKGROUND_LOCATION`) requested before foreground location is granted.
- Custom permissions exported without `protectionLevel="signature"`.

#### 2.8 Auth and crypto
- Hand-rolled JWT parsing / signature verification.
- Password hashing with MD5 / SHA-1 / SHA-256 without a key-derivation function.
- Random tokens generated with `Random()` instead of `SecureRandom`.
- Constant-time comparison missing on sensitive equality checks.
- Biometric prompts without `CryptoObject` binding (just yes/no, no key unlock).
- OAuth flows implemented with raw WebView instead of Custom Tabs.
- Refresh tokens stored without device-binding.
- Re-authentication missing on sensitive operations (payment, account change).

#### 2.9 Input validation
- Inputs validated for shape (regex, type) but not for semantic constraints (the user owns that resource, the value is within range).
- Path / filename inputs without traversal protection (`../` allowed).
- Redirects / forwards built from user input without allow-list.
- File-content type trusted from the uploader.
- Push notifications acted on without origin verification.

#### 2.10 Secrets and PII in code / resources / logs
- API keys, secrets, tokens, signing keys in source files, `strings.xml`, `BuildConfig`, or properties files committed to git.
- `Log.d` / `Log.v` / `Log.i` calls including PII, auth tokens, credentials, request bodies, response bodies.
- `Timber` or other logger pipelines that ship logs externally without redaction.
- Crash reporters (Firebase Crashlytics, Sentry, Bugsnag) without PII scrubbing on the wire.
- Analytics events with PII payloads.
- `Toast` / on-screen errors that leak credentials or stack traces.

#### 2.11 SDK-version-gated security gaps
- Code paths that bypass platform protections on older `minSdk` without compensating.
- `minSdk` < 23 still using `MODE_WORLD_READABLE` / `MODE_WORLD_WRITEABLE` (deprecated but possible).
- StrictMode disabled in release builds.
- `BuildConfig.DEBUG` checks gating security-relevant behavior incorrectly (e.g., disabling cert pinning in debug AND reaching prod).
- Apps on `minSdk` < 26 not handling notification trampoline restrictions safely.

### Step 3 — Distinguish AI-specific failure shape

For each finding, note whether the pattern is especially likely to have come from AI generation. Signs are the same as in the general security audit:

- Style mismatch with surrounding code (a hand-rolled crypto block in a Retrofit-heavy file).
- Over-elaborate naming for simple logic.
- Comments that narrate what the code does without why.
- Duplicated logic across files.
- "Nearly-correct" idiom (the right Android API called with subtly wrong arguments).
- Boilerplate that an AndroidX or Jetpack primitive would replace cleanly.

Use this as a confidence raiser, not a blocker.

### Step 4 — Verify each finding before reporting

For each candidate:

- **Trace the flow.** Where does input come from? Where does it reach? Is there validation / sanitization / framework protection anywhere in the chain? Pattern-match without trace = no finding.
- **Check for platform / library protection.** Does AndroidX provide this for free here? Is the protection active under the actual `minSdk` / `targetSdk`?
- **Check deployment posture (input 3).** An internal-only enterprise app has different severity calculus than a Play Store app for kids.
- **Check threat model (input 6).** Findings not relevant to the stated threat model get downgraded with a note.
- **Confidence label.** High / Medium / Low.

### Step 5 — Prioritize

Per finding:

- **Severity:** Critical / High / Medium / Low / Informational.
  - **Critical:** Reachable from an external entry point (exported component, intent filter, deeplink, network) with clear data-exfil, account-takeover, or device-compromise impact.
  - **High:** Reachable from external entry with significant impact under realistic conditions.
  - **Medium:** Requires specific conditions, on-device adversary, or partial compromise.
  - **Low:** Hygiene with no realistic attack path under the stated threat model.
  - **Informational:** Worth noting; not actionable on its own.
- **Exploitability posture:** Realistic attack path under input 3 + input 6.
- **Blast radius:** Per-user / per-device / per-tenant / global.

Sort findings by severity × exploitability × blast radius.

### Step 6 — Emit "AI patterns repeating in this codebase" for the rules file

3–8 patterns recurring. This feeds `android_viberescue_rules_file.md` as hard don'ts. Summarize; don't duplicate per-instance findings.

### Step 7 — Remediation per finding

Specific. Point to a platform primitive when one exists:

- "Replace plain SharedPreferences storage at `AuthRepo.kt:34` with `EncryptedSharedPreferences` (androidx.security:security-crypto) keyed via the Android Keystore."
- "Set `android:exported='false'` on `BillingActivity` in `AndroidManifest.xml:47` — it has no intent filter and is not launched externally."
- "Replace WebView-based OAuth in `LoginFragment.kt:89` with Chrome Custom Tabs (androidx.browser:browser); remove `addJavascriptInterface` call on line 92."

Not "use encryption" — name the API and the file.

### Step 8 — Dual-failure-prevention pass

- **Harmful direction:** Missed Critical finding. Did every exported component, every WebView, every PendingIntent, every network call get walked? If a category was skipped because nothing was found, say so explicitly.
- **Unhelpful direction:** Cap Critical + High at 12 in the main report; appendix the rest. Don't drown the urgent in the merely hygienic.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Every finding cites file + line range.
- Every finding has: category, traced flow, platform-protection check, severity, confidence, AI-pattern tag, remediation pointing to a specific API or file change.
- Severity is grounded in the actual deployment (input 3) and threat model (input 6), not assumed worst-case.
- Critical + High capped at 12 in the main body.
- "AI patterns repeating" section feeds the rules file.
- Scope gaps disclosed when a category couldn't be fully audited.

### Must Not
- Issue a finding on keyword match alone (`setJavaScriptEnabled`, `addJavascriptInterface`) without tracing what the WebView actually loads.
- Flag every `Log.d` call as a finding without checking what's being logged.
- Claim a missing cert-pin is Critical when the threat model excludes network attackers and traffic is internal.
- Issue "you should review this area" — that's a scope gap, not a finding.
- Recommend generic OWASP / SANS advice. Remediations name Android primitives.
- Reference Claude-Code-specific tool names — keep the prompt portable across agents.
- Recommend ProtectionLevel changes to existing custom permissions without checking installed-user impact.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Flag `android:exported="true"` on the LAUNCHER Activity (it must be true).
- Flag every PendingIntent without `FLAG_IMMUTABLE` on `targetSdk` < 31 builds (only required at 31+).
- Flag `allowBackup="true"` without checking whether `fullBackupContent` already excludes sensitive paths.
- Flag SharedPreferences storage of non-sensitive data (UI preferences, feature flags) as if it were credential storage.
- Claim cleartext traffic without checking `network_security_config.xml` overrides.
- Flag WebView JS as Critical when the WebView loads only `file:///android_asset/` content the app ships.
- Report missing cert pinning as Critical when the app's threat model is "trust the network."

DO:
- Trace the actual host loaded into each WebView before flagging.
- Distinguish PII categories (location vs email vs medical) — they have different regulatory weight.
- Check whether AndroidX libraries already wrap a primitive the AI hand-rolled.
- Note when an attack requires on-device malware vs network adversary vs lost-device — exploitability differs.
- Acknowledge unknowns: "potential finding, needs runtime trace" is valid output.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Critical exported component or token-storage issue missed because the auditor focused on showier WebView / crypto findings; user ships with a real hole.

UNHELPFUL failure: 60 Low / Informational findings about `Log.d` calls and `allowBackup` defaults; user can't see the actual Critical.

Quality check: A senior Android security engineer reads each Critical / High finding, can point to the file, agrees with the severity under the stated threat model, and can apply the remediation without further investigation.

---

## Output Format

```markdown
# Android Security & Privacy Audit — [App name]

## Summary
- Deployment posture: [from input 3]
- Threat model: [from input 6]
- Data sensitivity: [from input 4]
- minSdk / targetSdk / compileSdk: [from input 2]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N] | Informational: [N]
- Categories N/A (with reason): [list]

## Findings (sorted by severity × exploitability × blast radius)

### Finding 1: [Short title]
- **File / lines:** path/to/File.kt:42-58
- **Category:** [2.1–2.11 number + name]
- **Evidence:** [Code snippet or paraphrase, ≤5 lines]
- **Traced flow:** [entry point → relevant intermediate steps → sensitive operation]
- **Platform protection check:** [present / absent / partial, brief reasoning]
- **Active SDK gating:** [does this protection apply under app's minSdk/targetSdk?]
- **Severity:** Critical | High | Medium | Low | Informational
- **Exploitability under deployment + threat model:** [realistic attack path or "requires X"]
- **Blast radius:** per-user | per-device | per-tenant | global
- **Confidence:** High | Medium | Low
- **AI-pattern signal:** [yes + which signature(s) / neutral]
- **Remediation:** [Specific file change + Android primitive to use.]

### Finding 2: …

[Continue for Critical + High, up to 12.]

## AI Patterns Repeating in This Codebase
- [Pattern + locations summary] → rules-file hard don't recommendation
- [...]

## Scope Gaps
- [Areas not reached, one-line reason each.]

## Medium / Low / Informational Findings (appendix)
- [Abbreviated list — file:line, category, one-line description.]

## Recommended Next Step
Feed this report + `android_viberescue_codebase_audit.md` output into `android_viberescue_fix_prioritization.md`.
```

---

## Verification

- [ ] Every exported component, every WebView, every PendingIntent, every network call considered.
- [ ] Every finding has file + lines, category, traced flow, platform protection check, severity, exploitability under the actual deployment + threat model, blast radius, confidence, AI-pattern tag, specific remediation.
- [ ] No finding rests on keyword match alone.
- [ ] Severity grounded in input 3 and input 6, not assumed worst-case.
- [ ] Critical + High capped at 12 in main body.
- [ ] N/A categories explicitly noted.
- [ ] AI patterns repeating section present.
- [ ] Scope gaps acknowledged.

---

## Techniques Used

- **ST-01 (Clear Objective):** Findings report with platform-specific remediation, not generic security advice.
- **ST-02 (Structured Sequential Instructions):** Nine steps drive scope → eleven categories → AI signal → verify → prioritize → patterns → remediate → dual-failure → verify.
- **ST-03 (Output Format Specification):** Fixed report schema enables downstream consumption by the prioritization prompt.
- **CM-02 (Constraint Specification):** Must Not block forbids keyword findings, generic remediation, and worst-case severity inflation.
- **DS-01 (Framework Application):** Eleven Android-specific security categories form the framework; tied to platform primitives.
- **RT-05 (Evidence-Based Reasoning):** Every finding traced from entry to sensitive op with platform-protection check.
- **RT-07 (Cascade Effect Analysis):** AI-pattern repeating section traces individual findings to systemic prevention via the rules file.
- **QA-01 (Self-Verification):** Verification checklist + dual-failure prevention block prevents both missed-Critical and finding-flood failures.
- **QA-04 (Confidence Calibration):** Per-finding confidence + exploitability-under-actual-threat-model forces explicit grounding.

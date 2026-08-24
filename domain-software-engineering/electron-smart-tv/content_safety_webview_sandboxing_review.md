---
title: "Content Safety & Webview Sandboxing Review"
category: software-engineering/electron-smart-tv
description: "Verify that a kids entertainment app correctly sandboxes external web content, enforces channel whitelists, prevents navigation to unvetted content, and locks down webview capabilities to protect child users."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - QA-02  # Adversarial Stress-Test
difficulty: advanced
tags:
  - content-safety
  - kids-safety
  - webview-sandbox
  - parental-controls
  - whitelist
  - navigation-control
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/electron_ipc_preload_security_audit.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
---

# Content Safety & Webview Sandboxing Review

**Objective:** Verify that a kids entertainment launcher correctly constrains external web content (YouTube, Disney+) to whitelisted channels and domains, prevents navigation to unvetted pages, sandboxes webview capabilities to prevent content injection, and provides effective parental controls that cannot be bypassed by a curious child.

---

## When to Use

- Use when: An Electron app loads external web content intended for children
- Use when: Adding new content providers (channels, streaming services) to an existing launcher
- Use when: Implementing or reviewing parental controls (PIN, time limits, content restrictions)
- Use when: YouTube integration allows searching or browsing, creating potential for unwanted content
- Don't use when: The app only shows locally-bundled, pre-vetted content with no network access

---

## Inputs / Context

**Required:**
- Main process code handling window creation and navigation events
- Channel/content whitelist configuration (hard-coded or configurable)
- YouTube integration code (search, browse, playlist fetching, player)
- Navigation event handlers (`will-navigate`, `did-navigate`, `new-window`, `setWindowOpenHandler`)

**Optional:**
- Disney+ or other streaming service integration code
- Parental control UI and logic (PIN entry, settings)
- Content filtering or safe-search configuration
- `youtube-preload.js` and `disney-preload.js` for in-page content manipulation

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify that every possible navigation path from the launcher to external content passes through a whitelist check
- Test that YouTube content is restricted to whitelisted channels only — not just at the API level but in the rendered player
- Confirm that webview/BrowserWindow configurations prevent content from opening new windows, executing downloads, or accessing local files
- Evaluate parental controls for bypass resistance appropriate for the target age group

**Must Not:**
- Assume API-level filtering is sufficient — YouTube embedded players can suggest and auto-play unwhitelisted content
- Ignore `target="_blank"` links, `window.open()` calls, or JavaScript-initiated navigation in external content
- Report privacy/tracking concerns (cookies, analytics) as safety issues unless they expose child identity data
- Treat all YouTube content as unsafe — the whitelist exists to curate safe channels

---

## Steps

1. **Map all content entry points**
   - List every way external content reaches the screen: direct URL loading, YouTube API results, embedded players, Disney+ webview, search results
   - For each entry point, trace the content validation chain: is it checked against a whitelist? Where?
   - Identify content that bypasses the whitelist: auto-play suggestions, related videos, end-screen links, ads
   - Check if YouTube's restricted mode (safe search) is enforced at the API level and in embedded players

2. **Audit navigation controls**
   - Check `will-navigate` handlers on every BrowserWindow and webview: do they validate the target URL?
   - Check `setWindowOpenHandler`: does it block or restrict new window creation?
   - Verify `did-navigate` handlers: do they close or redirect windows that reach unwhitelisted URLs?
   - Check if `window.open()`, `<a target="_blank">`, and JavaScript `location.href` changes are all caught
   - Test URL schemes: `javascript:`, `data:`, `blob:`, `file:` — are they blocked?

3. **Evaluate YouTube content isolation**
   - Verify the channel whitelist is enforced at playlist fetch time (API level)
   - Check if the YouTube player (embedded or custom) can navigate to non-whitelisted videos via:
     - Related video suggestions
     - End-screen cards and annotations
     - Auto-play queue
     - Search results (if search is enabled)
     - Comment links (if comments are visible)
   - Verify that the offline search feature only returns results from cached whitelisted content
   - Check if YouTube's own UI elements (logo, channel links) can navigate out of the controlled environment

4. **Verify webview sandbox settings**
   - For each BrowserWindow loading external content, check:
     - `webPreferences.sandbox: true` — renderer process sandboxed
     - `webPreferences.allowRunningInsecureContent: false`
     - No `webPreferences.webviewTag: true` unless necessary (and sub-webviews are also restricted)
     - `webPreferences.enableWebSQL: false` (if available in Electron version)
   - Check Content Security Policy (CSP) headers or meta tags in loaded pages
   - Verify that DevTools are disabled in production builds (`webPreferences.devTools: false`)

5. **Assess parental control bypass resistance**
   - If a PIN/password protects settings, verify:
     - PIN is not stored in renderer-accessible storage (localStorage, sessionStorage)
     - PIN comparison happens in main process, not renderer
     - Failed attempts are rate-limited
     - The settings screen is not accessible via navigation or keyboard shortcuts that bypass the PIN
   - Check if children can access system-level controls (Alt+F4, Ctrl+W, Task Manager) to exit the app
   - Verify kiosk mode settings prevent desktop escape if the app is intended as a full kiosk

6. **Test content injection resistance**
   - Can external content inject script into the parent frame or other windows?
   - Are preload scripts in content windows minimal (not exposing IPC channels that control the launcher)?
   - If content windows use `webContents.executeJavaScript()`, verify the injected code doesn't create new attack surfaces
   - Check if CSS in external content can overlay launcher UI elements (clickjacking-style attacks)

7. **CRITICAL: Verify findings before reporting**
   - Test navigation restrictions by tracing actual event handler code, not just checking if handlers exist
   - Confirm that YouTube content restrictions apply to the actual player implementation, not just API calls
   - Verify that reported bypass paths are accessible to a child user, not just a developer with DevTools
   - Consider the target age group: a 3-year-old's bypass capabilities differ from a 10-year-old's

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag YouTube video playback as a security risk — the risk is unwhitelisted content, not playback itself
- Report cookies set by YouTube/Disney+ as a child safety issue unless they contain PII
- Flag the presence of ads in YouTube content as a safety failure (unless ads lead to inappropriate content)
- Report that YouTube suggestions are "visible" if they are overlaid or hidden by the custom player UI
- Assume all external navigation is malicious — the app intentionally loads YouTube and Disney+

**DO:**
- Verify that every `will-navigate` handler checks the URL against allowed domains AND paths (not just domain)
- Confirm that YouTube's restricted mode parameter is set in API calls AND embedded player URLs
- Check that the YouTube search feature (if enabled) searches within cached whitelisted content, not all of YouTube
- Test what happens when a child clicks a YouTube end-screen link — does it navigate or get blocked?
- Verify that parental control state persists across app restarts and cannot be cleared by the child

---

## Expected Output

### Executive Summary
Assessment of content safety posture for the target age group, with a clear statement of the content boundary (what's allowed, what's blocked).

### Content Entry Point Map
| Entry Point | Whitelist Enforced? | Navigation Controlled? | Content Escape Possible? | Risk |
|------------|--------------------|-----------------------|-------------------------|------|
| YouTube API results | ... | ... | ... | ... |
| YouTube player | ... | ... | ... | ... |
| Disney+ webview | ... | ... | ... | ... |
| Offline search | ... | ... | ... | ... |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Scenario:** [How a child could reach unwhitelisted content]
- **Evidence:** [Code showing the gap in content controls]
- **Impact:** [Child exposed to: unvetted videos / external websites / inappropriate content]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would modify severity]

### Adversarial Scenarios (Child Bypass Testing)
| Scenario | Age Group | Steps | Outcome | Status |
|----------|-----------|-------|---------|--------|
| Child clicks related video in YouTube player | 5-8 | 1. Watch whitelisted video 2. Click end-screen suggestion | ... | ... |
| Child uses keyboard shortcuts to access DevTools | 8-12 | 1. Press F12 or Ctrl+Shift+I | ... | ... |
| Child presses Back repeatedly to escape content area | 3-5 | 1. Press Escape/Back 10 times rapidly | ... | ... |
| Child types URL in any input field | 8-12 | 1. Find any text input 2. Type URL | ... | ... |

### Prioritized Recommendations
| # | Action | Severity | Child Safety Impact |
|---|--------|----------|---------------------|
| 1 | ...    | ...      | ...                 |

---

## Verification

**Quick self-check:**
- [ ] Every content entry point has been mapped with whitelist enforcement status
- [ ] Navigation event handlers verified for all windows loading external content
- [ ] YouTube content isolation tested beyond API level (player UI, suggestions, auto-play)
- [ ] Parental control bypass resistance evaluated for target age group
- [ ] DevTools and system escape routes verified as blocked

**High-stakes option (mandatory for kids apps):**
After completing the analysis:
1. Play adversary: If you were a curious 8-year-old, what three paths would you try to reach content outside the whitelist?
2. What happens if YouTube changes their embed player to add new navigation elements?
3. Are there any time-window gaps during app startup where content restrictions aren't yet active?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focuses on content boundary enforcement for child users
- **ST-02 (Structured Sequential Instructions):** Systematic audit from entry points through bypass testing
- **RT-02 (Multi-Dimensional Analysis):** Content entry, navigation control, sandbox, parental controls, injection
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual event handler code and navigation paths
- **QA-02 (Adversarial Stress-Test):** Explicit adversarial scenarios testing child bypass attempts

---

## Related Prompts

- [Electron IPC & Preload Security Audit](electron_ipc_preload_security_audit.md) - Technical security of IPC channels
- [Security Vulnerability Analysis](../analysis/security/security_vulnerability_analysis.md) - General security review

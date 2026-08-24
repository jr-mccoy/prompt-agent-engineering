---
title: "Electron IPC & Preload Script Security Audit"
category: software-engineering/electron-smart-tv
description: "Audit Electron IPC channels, preload scripts, and contextBridge exposures for privilege escalation, prototype pollution, and unauthorized main-process access."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: advanced
tags:
  - electron
  - ipc-security
  - preload-scripts
  - contextBridge
  - privilege-escalation
  - kids-safety
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/content_safety_webview_sandboxing_review.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
---

# Electron IPC & Preload Script Security Audit

**Objective:** Identify security vulnerabilities in Electron IPC channel definitions, preload script exposures, and contextBridge API surfaces that could allow renderer-side code to escalate privileges, access Node.js APIs, or bypass content isolation in a kids entertainment launcher.

---

## When to Use

- Use when: Adding or modifying IPC handlers in the main process (`ipcMain.handle`, `ipcMain.on`)
- Use when: Creating or changing preload scripts that expose APIs via `contextBridge.exposeInMainWorld`
- Use when: Opening new BrowserWindows or webview tags that load external content (YouTube, Disney+)
- Use when: Reviewing an Electron app that children will use unsupervised
- Don't use when: Reviewing pure renderer-side UI logic with no IPC interaction

---

## Inputs / Context

**Required:**
- Main process file(s) containing IPC handler registrations (e.g., `main.js`)
- All preload scripts (e.g., `launcher-preload.js`, `youtube-preload.js`, `disney-preload.js`)
- `BrowserWindow` creation options (especially `webPreferences`)
- `package.json` for Electron version

**Optional:**
- `.env` or environment configuration files (to check for secrets exposed to renderers)
- Any custom protocol handlers registered via `protocol.registerSchemeAsPrivileged`

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Trace every `contextBridge.exposeInMainWorld` call and catalog the full API surface available to each renderer
- Verify that `nodeIntegration` is `false` and `contextIsolation` is `true` for every BrowserWindow
- Check that no IPC handler passes unsanitized renderer input to Node.js APIs (`fs`, `child_process`, `shell.openExternal`, `require`)
- Assign confidence levels (High/Medium/Low) to each finding with supporting evidence

**Must Not:**
- Flag `contextBridge` usage as inherently insecure — it is the recommended pattern; evaluate what is exposed, not that it exists
- Assume renderer-side code is trusted — treat all renderer inputs as attacker-controlled
- Report findings without tracing the actual code path from renderer to main process
- Invent vulnerabilities not evidenced in the code

---

## Steps

1. **Inventory all BrowserWindow configurations**
   - For each `new BrowserWindow(...)`, extract `webPreferences` settings
   - Confirm `nodeIntegration: false`, `contextIsolation: true`, `sandbox: true` (where applicable)
   - Check if `webSecurity` is disabled anywhere
   - Note which preload script is assigned to each window

2. **Map the IPC attack surface**
   - List every `ipcMain.handle(channel, handler)` and `ipcMain.on(channel, handler)` registration
   - For each handler, trace what the handler does with renderer-provided arguments
   - Identify handlers that perform privileged operations: file system access, shell commands, network requests with API keys, window creation
   - Check if any handler forwards arguments directly to `shell.openExternal`, `require`, `eval`, `Function()`, or template strings used in system calls

3. **Audit preload script exposures**
   - For each preload script, list every function/property exposed via `contextBridge.exposeInMainWorld`
   - For each exposed function, trace the `ipcRenderer.invoke` or `ipcRenderer.send` call it wraps
   - Identify over-permissive exposures: functions that accept arbitrary channel names, functions that pass through raw objects, functions that expose the full `ipcRenderer` API
   - Check for prototype pollution vectors in objects passed across the bridge

4. **Check external content isolation**
   - For windows loading external URLs (Disney+, YouTube), verify they cannot access exposed IPC channels
   - Check for `<webview>` tag usage and verify `nodeIntegration`, `preload`, `partition` settings
   - Verify that navigation is restricted (e.g., `will-navigate` event handlers prevent navigation to unexpected origins)
   - Check `setWindowOpenHandler` to prevent renderer-initiated window creation

5. **Verify environment and secret handling**
   - Confirm API keys (e.g., `YOUTUBE_API_KEY`) are only accessed in the main process
   - Check that no secrets are passed to renderers via IPC, preload, or global variables
   - Verify `.env` values are not bundled into renderer-accessible code

6. **CRITICAL: Verify findings before reporting**
   - For each potential vulnerability, trace the complete code path from renderer input to privileged operation
   - Check if input validation, sanitization, or allow-listing exists along the path
   - Confirm the vulnerability is actually exploitable given the window configuration
   - Assess whether the issue is exploitable by a child accidentally or only by deliberate attack

7. **Prioritize findings** by severity (Critical/High/Medium/Low) weighted toward child safety impact.

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag `contextBridge.exposeInMainWorld` as a vulnerability — it is the correct, recommended pattern for Electron security
- Report `nodeIntegration: false` as "missing nodeIntegration" — false means it's correctly disabled
- Flag IPC channels that only return read-only data with no side effects as "privilege escalation"
- Report preload scripts as insecure simply because they use `ipcRenderer` — that's their purpose
- Flag `shell.openExternal` behind an allow-list as a vulnerability when the allow-list is correctly implemented

**DO:**
- Verify that exposed API functions use specific, named IPC channels (not dynamic channel strings)
- Check that arguments passed from renderer to main are validated before use in privileged operations
- Confirm that IPC handlers receiving URLs validate them against an allow-list before opening
- Trace the full round-trip: renderer → preload → IPC → main handler → side effect
- Check that error responses from IPC handlers don't leak internal paths or stack traces to the renderer

---

## Expected Output

### Executive Summary
1–3 sentences summarizing the overall IPC and preload security posture.

### Window Configuration Audit
| Window | nodeIntegration | contextIsolation | sandbox | webSecurity | Preload | Verdict |
|--------|----------------|------------------|---------|-------------|---------|---------|
| ...    | ...            | ...              | ...     | ...         | ...     | ...     |

### IPC Channel Inventory
| Channel | Direction | Handler Location | Accepts Args | Privileged Operation | Risk |
|---------|-----------|-----------------|--------------|---------------------|------|
| ...     | ...       | ...             | ...          | ...                 | ...  |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Code Path:** renderer → [preload function] → [IPC channel] → [main handler] → [side effect]
- **Evidence:** [Specific code showing the vulnerability]
- **Impact:** [What an attacker/child could do]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would lower/raise severity]

### Prioritized Recommendations
| # | Action | Severity | Effort | Child Safety Impact |
|---|--------|----------|--------|---------------------|
| 1 | ...    | ...      | ...    | ...                 |

---

## Verification

**Quick self-check:**
- [ ] Every BrowserWindow's `webPreferences` have been inspected
- [ ] Every IPC channel has been cataloged with its handler
- [ ] Every preload script exposure has been traced to its IPC call
- [ ] Every finding has file:line citation and code path evidence
- [ ] No findings are based solely on keyword matching without code path tracing

**High-stakes option (recommended for kids apps):**
After completing the audit:
1. What IPC channels could a malicious webpage injected into a webview exploit?
2. If a child accidentally navigates to an untrusted URL, what main-process capabilities are reachable?
3. What assumptions about renderer trust does this audit rely on?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines the specific Electron security aspects to audit
- **ST-02 (Structured Sequential Instructions):** Ordered audit steps from configuration through exploitation verification
- **RT-02 (Multi-Dimensional Analysis):** Each finding analyzed across severity, confidence, code path, impact, and remediation
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual code paths rather than pattern matching
- **DS-06 (Prioritization Guidance):** Findings ranked by severity weighted toward child safety

---

## Related Prompts

- [Content Safety & Webview Sandboxing Review](content_safety_webview_sandboxing_review.md) - Complements this audit with content-level safety checks
- [Security Vulnerability Analysis](../analysis/security/security_vulnerability_analysis.md) - General-purpose security analysis

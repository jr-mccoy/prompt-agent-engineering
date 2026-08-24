---
title: "Electron Packaging & Cross-Platform Distribution Review"
category: software-engineering/electron-smart-tv
description: "Review Electron app packaging configuration for correct bundling, platform-specific issues, production hardening, auto-update readiness, and deployment to TV/kiosk hardware targets."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - electron-packaging
  - cross-platform
  - distribution
  - production-hardening
  - kiosk-mode
  - auto-update
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/electron_app_performance_profiling.md
  - domain-software-engineering/devops/devops_cicd_pipeline_analysis.md
---

# Electron Packaging & Cross-Platform Distribution Review

**Objective:** Review an Electron app's packaging configuration for correct resource bundling, environment variable handling, platform-specific behavior differences, production security hardening, and readiness for deployment to target platforms including kiosk/TV hardware.

---

## When to Use

- Use when: Preparing to package an Electron app for distribution (first release or major update)
- Use when: The app works in development (`npm start`) but fails or behaves differently when packaged
- Use when: Targeting multiple platforms (macOS, Windows, Linux/ARM for TV hardware)
- Use when: Setting up kiosk mode for unattended TV deployment
- Don't use when: Debugging development-mode issues that aren't packaging-related

---

## Inputs / Context

**Required:**
- `package.json` (main entry point, scripts, dependencies vs devDependencies)
- Main process file(s) — especially file path resolution and resource loading
- Packaging configuration (electron-packager, electron-builder, or electron-forge config)
- `.env.example` and environment variable usage throughout the app

**Optional:**
- Build scripts or CI/CD pipeline configuration
- Platform-specific code paths (macOS menu bar, Windows taskbar, Linux tray)
- Auto-update configuration (electron-updater or Squirrel)
- Icon/asset files referenced by the app
- Target hardware specifications for deployment

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify that all referenced files (HTML, preload scripts, assets) are included in the packaged app
- Check that environment variables are handled correctly in production (not just via dotenv + `.env` file)
- Test file path resolution for both development (`npm start`) and packaged (asar archive) modes
- Identify platform-specific code that may break on non-primary development platforms

**Must Not:**
- Assume that `__dirname` resolves the same way in development and in a packaged asar archive
- Ignore the `.env` file handling — dotenv reads from CWD which differs when packaged
- Report cross-platform differences that are handled by Electron's abstraction layer (e.g., `app.getPath()`)
- Suggest packaging approaches that contradict the project's existing tooling choice

---

## Steps

1. **Audit resource bundling**
   - Verify that `package.json` `main` field points to the correct entry file
   - Check all `loadFile()` and `loadURL()` calls — are paths resolved using `__dirname`, `app.getAppPath()`, or hardcoded?
   - Verify preload scripts are referenced with absolute paths that resolve correctly inside an asar archive
   - Check for `fs.readFile` / `require()` calls that load files by relative path (may break when packaged)
   - Identify all asset files (HTML, CSS, JS, images, JSON) and verify they'll be included in the package

2. **Review environment variable handling**
   - Check how `dotenv` is loaded — `require('dotenv').config()` reads from `process.cwd()`, which changes when packaged
   - Verify the app handles missing `.env` gracefully in production (system environment variables should work)
   - Check that `YOUTUBE_API_KEY` validation failure produces a clear error message in production (not a silent crash)
   - Verify cache environment variables (`YT_REFRESH_INTERVAL_MIN`, etc.) have sensible defaults when not set
   - Confirm no secrets are hardcoded as fallbacks in the source code

3. **Check asar archive compatibility**
   - Identify code that won't work inside an asar archive:
     - `fs.existsSync()` on directories inside asar
     - Native module loading (`*.node` files must be unpacked)
     - `child_process.exec/spawn` with paths inside asar
   - Verify the cache file path uses `app.getPath('userData')`, NOT a path relative to the app bundle
   - Check if any dependencies use native modules that require rebuilding per platform

4. **Evaluate platform-specific behavior**
   - **macOS:** App menu, dock behavior, notarization requirements, universal binary (arm64 + x64)
   - **Windows:** Taskbar behavior, installer format (NSIS, MSI, Squirrel), code signing
   - **Linux:** Desktop entry file, tray icon support, permission requirements, Wayland vs X11
   - **ARM Linux (TV hardware):** Electron ARM build availability, GPU acceleration flags, kiosk mode
   - Check `process.platform` conditionals — are all target platforms handled?

5. **Assess production hardening**
   - DevTools: Verify `webPreferences.devTools: false` or that DevTools keyboard shortcuts are disabled
   - Source maps: Check if source maps are included in the package (exposes source code)
   - Debug logging: Verify verbose console output is disabled or redirectable in production
   - Crash reporting: Check if electron's crash reporter or similar is configured
   - Kiosk mode: If deploying to TV, verify `kiosk: true` or `fullscreen: true` with escape prevention
   - Auto-start: Check if instructions/configuration exist for starting the app on boot

6. **Review dependency classification**
   - Check that `devDependencies` are not `require()`'d at runtime (they won't be packaged)
   - Verify `dependencies` doesn't include dev-only packages (bloats package size)
   - Check if `electron` is in `devDependencies` (correct) not `dependencies` (would bundle a second copy)
   - Look for optional dependencies that might be needed on some platforms but not others

7. **CRITICAL: Verify findings before reporting**
   - Test path resolution logic by tracing the actual values of `__dirname`, `app.getAppPath()`, and `process.resourcesPath` in packaged vs development mode
   - Confirm that reported issues are actual packaging problems, not development-mode quirks
   - Verify platform-specific issues against the actual target platforms (don't report Windows issues if only deploying to Linux)
   - Check the packaging tool's documentation for built-in handling of common issues

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag `__dirname` usage as always broken — it works correctly for files at the same level as the main process entry
- Report `dotenv` as incompatible with packaging — it works if the `.env` file is placed alongside the executable
- Flag all `fs` operations as asar-incompatible — Electron patches `fs` to transparently read from asar
- Report missing platform-specific code as a bug when the app only targets one platform
- Flag large `node_modules` as a packaging issue when the packager correctly prunes devDependencies

**DO:**
- Verify that `app.getPath('userData')` is used for writable data (cache, settings), not paths inside the app bundle
- Check that preload script paths use `path.join(__dirname, 'preload.js')` or equivalent, not string concatenation
- Confirm the packager is configured to include all file extensions used by the app (`.html`, `.js`, `.css`, `.json`)
- Test that the `YOUTUBE_API_KEY` validation error message is visible when the app is launched from a terminal/shortcut
- Verify that the cache JSON file persists across app updates (stored in userData, not app directory)

---

## Expected Output

### Executive Summary
Packaging readiness assessment with identified blockers for each target platform.

### Resource Bundling Audit
| Resource | Path Resolution | Asar Compatible? | Included in Package? | Status |
|----------|----------------|-------------------|--------------------|--------|
| launcher.html | ... | ... | ... | ... |
| youtube-preload.js | ... | ... | ... | ... |
| disney-preload.js | ... | ... | ... | ... |
| yt_cache.json | ... | N/A (userData) | N/A | ... |

### Platform Readiness
| Platform | Build Config | Tested? | Known Issues | Deployment Notes |
|----------|-------------|---------|-------------|------------------|
| macOS (x64/arm64) | ... | ... | ... | ... |
| Windows (x64) | ... | ... | ... | ... |
| Linux (x64) | ... | ... | ... | ... |
| Linux (arm64/TV) | ... | ... | ... | ... |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Affects Platform(s):** macOS / Windows / Linux / All
- **Evidence:** [Code showing the packaging issue]
- **Impact:** [App crash, missing resource, broken feature, security exposure]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would modify severity]

### Production Hardening Checklist
| Item | Status | Notes |
|------|--------|-------|
| DevTools disabled | ... | ... |
| Source maps excluded | ... | ... |
| Debug logging controlled | ... | ... |
| Kiosk mode configured | ... | ... |
| Auto-start configured | ... | ... |
| Crash reporting enabled | ... | ... |
| Code signing configured | ... | ... |

### Prioritized Recommendations
| # | Action | Severity | Platform | Effort |
|---|--------|----------|----------|--------|
| 1 | ...    | ...      | ...      | ...    |

---

## Verification

**Quick self-check:**
- [ ] All `loadFile()` / `loadURL()` paths traced for development vs packaged resolution
- [ ] Environment variable handling verified for production deployment
- [ ] Asar compatibility checked for all file system operations
- [ ] Target platform-specific concerns identified
- [ ] Production hardening checklist completed

**High-stakes option (for TV kiosk deployment):**
After completing the review:
1. If the packaged app is placed on a Linux ARM device and launched at boot, will it find all its resources?
2. Can a child exit the app using keyboard shortcuts, Alt+Tab, or other system-level escapes?
3. What happens when the app auto-updates — is the cache preserved or lost?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Targets Electron packaging for multi-platform TV deployment
- **ST-02 (Structured Sequential Instructions):** Systematic review from bundling through production hardening
- **RT-02 (Multi-Dimensional Analysis):** Resources, environment, asar, platforms, hardening, dependencies
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual path resolution behavior
- **DS-06 (Prioritization Guidance):** Ranked by deployment-blocking severity

---

## Related Prompts

- [Electron App Performance Profiling](electron_app_performance_profiling.md) - Performance implications of packaging choices
- [CI/CD Pipeline Analysis](../devops/devops_cicd_pipeline_analysis.md) - Build pipeline for packaging automation

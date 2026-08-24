---
title: "Remote-First Input Handling & Focus Management Review"
category: software-engineering/electron-smart-tv
description: "Review keyboard and remote control event handling across an Electron multi-window app for correct propagation, conflict-free bindings, consistent Back/Home/Enter behavior, and reliable focus restoration during window transitions."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - remote-control
  - keyboard-events
  - focus-management
  - input-handling
  - event-propagation
  - multi-window
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/spatial_navigation_10ft_accessibility_audit.md
  - domain-software-engineering/electron-smart-tv/electron_multi_window_lifecycle_analysis.md
---

# Remote-First Input Handling & Focus Management Review

**Objective:** Review the keyboard and remote control input handling implementation across all windows and contexts in an Electron smart TV launcher to verify that key events propagate correctly, Back/Escape/Home buttons behave consistently, no key binding conflicts exist between the app and spatial navigation polyfill, and focus state is reliably preserved and restored during window transitions.

---

## When to Use

- Use when: The app is designed for hardware remote control operation (Flirc, CEC, Bluetooth remotes)
- Use when: Users report keys not working, wrong behavior on Back/Escape, or focus jumping unexpectedly
- Use when: Adding new windows, overlays, or interactive elements that need key event handling
- Use when: Integrating a spatial navigation polyfill with custom key event listeners
- Don't use when: Reviewing mouse/touch input handling (this prompt is keyboard/remote-specific)

---

## Inputs / Context

**Required:**
- All key event listeners in the application: `keydown`, `keyup`, `keypress` handlers in renderer and preload scripts
- Main process `globalShortcut` registrations (if any)
- Spatial navigation polyfill configuration and its key bindings
- Window management code (how Back/Home triggers window close/show)

**Optional:**
- Flirc or other remote control key mapping configuration
- `BrowserWindow` `webContents` input event interception code
- Accelerator registrations on menus or shortcuts
- Documentation of intended key behavior per screen

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Map every key event listener in every window/preload script and verify there are no conflicts
- Verify Back/Escape behavior follows the expected hierarchy: close overlay → close player → return to launcher
- Confirm that the Home key always returns to the launcher regardless of current context
- Check that key events don't "leak" between windows (main process globalShortcuts affect all windows)

**Must Not:**
- Assume that key events work identically in the main process and renderer process — they have different APIs
- Flag the spatial navigation polyfill's internal key handling as a conflict when it's intentional
- Report that Escape and Back are the same key as a bug (remotes often map Back to Escape)
- Ignore modifier keys — Ctrl+W, Alt+F4, Cmd+Q can break kiosk mode if not handled

---

## Steps

1. **Inventory all key event listeners**
   - For each renderer (launcher, YouTube, Disney+), list every `addEventListener('keydown', ...)` and `addEventListener('keyup', ...)`
   - For each preload script, list any key event interception
   - In the main process, list all `globalShortcut.register()` calls
   - List all Electron `Menu` accelerators that bind keyboard shortcuts
   - Identify the spatial navigation polyfill's key bindings (typically Arrow keys, Enter, Tab)
   - Map which keys have multiple listeners and in which order they fire

2. **Trace Back/Escape behavior chain**
   - Document the expected behavior at each depth level:
     1. In player overlay → close overlay, return to content browser
     2. In YouTube/Disney+ window → close content window, return to launcher
     3. In launcher → do nothing (or show exit confirmation)
   - Trace the actual code path for Escape/Back key:
     - Which listener catches it first?
     - Does `event.stopPropagation()` or `event.preventDefault()` prevent other listeners from firing?
     - Does it trigger an IPC call to the main process to manage windows?
   - Check edge case: What happens if Escape is pressed rapidly multiple times? Does it skip levels?

3. **Trace Home button behavior**
   - Verify Home key always returns to the launcher regardless of context
   - Check if the Home handler:
     - Closes all content windows (or hides them)
     - Shows the launcher window
     - Restores focus to the previously selected launcher tile
   - Test: What happens if Home is pressed during a window transition (creation, loading)?
   - Test: What happens if Home is pressed while a dialog is open?

4. **Check key event propagation and conflicts**
   - Verify that the spatial navigation polyfill and custom key handlers don't conflict:
     - Arrow keys: polyfill handles spatial navigation; does any custom handler also listen?
     - Enter: polyfill may handle activation; does a custom handler also trigger actions?
     - Tab: some polyfills use Tab; does the app have Tab-based navigation too?
   - Check event listener ordering: `addEventListener` in capture phase vs bubble phase
   - Verify that `stopPropagation()` is used correctly (stops the right listeners, not too many)
   - Check if `preventDefault()` is called on events that should still reach the browser (e.g., preventing Space from scrolling, but not preventing Enter from activating)

5. **Audit focus state management**
   - Check if each screen stores the previously focused element when losing focus
   - When a content window opens, is the launcher's focused tile remembered?
   - When returning to the launcher (Back or Home), is focus restored to the correct tile?
   - Check for "focus limbo": states where no element has focus and key events go nowhere
   - Verify that `document.activeElement` is tracked or managed explicitly
   - Test: After a dynamic content update (thumbnails loaded, tiles added), does focus remain stable?

6. **Evaluate system key handling (kiosk safety)**
   - Check if dangerous key combinations are intercepted:
     - Alt+F4 / Cmd+Q (quit app)
     - Ctrl+W / Cmd+W (close window)
     - Alt+Tab / Cmd+Tab (switch app)
     - F11 (toggle fullscreen)
     - F12 / Ctrl+Shift+I (DevTools)
   - Verify that `globalShortcut` registrations correctly prevent these in kiosk mode
   - Check that these blocks are only active in production (development needs these shortcuts)
   - Note: Some system shortcuts (Alt+Tab) cannot be intercepted at the application level on most OS

7. **CRITICAL: Verify findings before reporting**
   - Test key event conflicts by tracing listener registration order, not just checking for multiple handlers on the same key
   - Confirm that reported "dead keys" aren't simply handled by the spatial navigation polyfill transparently
   - Verify that focus restoration issues occur in the actual window transition flow, not in isolated test scenarios
   - Consider Flirc/remote-specific key codes that may differ from standard keyboard codes

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag multiple `keydown` listeners on Arrow keys as a conflict if one is the spatial navigation polyfill (it's expected)
- Report that Escape and Back map to the same keycode as a bug (this is standard for TV remotes)
- Flag `globalShortcut` blocking Alt+Tab as incomplete — this is an OS-level shortcut that Electron cannot block on most platforms
- Report focus moving to `<body>` briefly during window transitions as a bug if it's immediately redirected
- Flag the absence of a visible cursor as a bug in a remote-first interface

**DO:**
- Check that `event.stopPropagation()` in custom handlers doesn't accidentally prevent the spatial navigation polyfill from working
- Verify that Enter key activates the currently focused element AND doesn't trigger a separate hardcoded action simultaneously
- Confirm that rapid key presses (holding Back) don't cause state corruption (multiple windows closing simultaneously)
- Check that media keys (Play, Pause, Stop) are handled if the target remote sends them
- Verify that key repeat rate for held directional keys allows smooth navigation without overshooting

---

## Expected Output

### Executive Summary
Assessment of input handling correctness and remote-first usability.

### Key Event Listener Map
| Key | Launcher Renderer | YouTube Renderer | Disney+ Renderer | Main Process | Spatial Nav Polyfill | Conflicts? |
|-----|-------------------|-----------------|------------------|-------------|---------------------|------------|
| ArrowUp | ... | ... | ... | ... | ✓ | ... |
| ArrowDown | ... | ... | ... | ... | ✓ | ... |
| Enter | ... | ... | ... | ... | ✓ | ... |
| Escape/Back | ... | ... | ... | ... | — | ... |
| Home | ... | ... | ... | ... | — | ... |

### Back/Escape Behavior Chain
| Context | Depth | Expected Behavior | Actual Behavior | Status |
|---------|-------|-------------------|-----------------|--------|
| Player overlay open | 3 | Close overlay | ... | ... |
| YouTube window active | 2 | Close YouTube, show launcher | ... | ... |
| Launcher (nothing open) | 1 | No action or exit prompt | ... | ... |

### Focus Restoration Map
| Transition | Focus Before | Focus After (Expected) | Focus After (Actual) | Status |
|------------|-------------|----------------------|---------------------|--------|
| Launcher → YouTube | Tile [1,1] | YouTube first element | ... | ... |
| YouTube → Launcher (Back) | Video list | Tile [1,1] (restored) | ... | ... |
| YouTube → Launcher (Home) | Any | Last selected tile | ... | ... |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Steps to Reproduce:** [Exact key sequence that triggers the issue]
- **Evidence:** [Code showing the event handler or conflict]
- **Impact:** [Key doesn't work, wrong action, focus lost, navigation broken]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would modify severity]

### Prioritized Recommendations
| # | Action | Severity | Remote Usability Impact |
|---|--------|----------|------------------------|
| 1 | ...    | ...      | ...                    |

---

## Verification

**Quick self-check:**
- [ ] Every key event listener mapped across all windows and the main process
- [ ] Back/Escape chain verified at every navigation depth
- [ ] Home button verified to return to launcher from any context
- [ ] Key binding conflicts between custom handlers and spatial navigation polyfill checked
- [ ] Focus restoration verified for every window transition

**High-stakes option (for remote-only operation):**
After completing the review:
1. Using only 5 buttons (Up, Down, Left, Right, OK) and 2 special buttons (Back, Home), can every feature be accessed?
2. If focus gets lost (no element focused), can the user recover using any key?
3. If a child holds the Back button for 3 seconds, what happens? (Should cleanly return to launcher, not cascade-close everything then quit)

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focuses on remote-first input handling in a multi-window Electron app
- **ST-02 (Structured Sequential Instructions):** Systematic audit from listener inventory through focus restoration
- **RT-02 (Multi-Dimensional Analysis):** Key bindings, propagation, Back/Home chains, focus state, kiosk safety
- **RT-05 (Evidence-Based Reasoning):** Requires tracing event listener registration and propagation order
- **DS-06 (Prioritization Guidance):** Ranked by remote usability impact

---

## Related Prompts

- [10-Foot Spatial Navigation & Accessibility Audit](spatial_navigation_10ft_accessibility_audit.md) - Spatial navigation completeness and focus visibility
- [Multi-Window Lifecycle & Memory Management Analysis](electron_multi_window_lifecycle_analysis.md) - Window transitions that affect focus state

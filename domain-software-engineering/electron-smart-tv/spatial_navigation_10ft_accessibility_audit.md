---
title: "10-Foot Spatial Navigation & Accessibility Audit"
category: software-engineering/electron-smart-tv
description: "Audit a smart TV launcher's spatial navigation, focus management, and 10-foot UI patterns for completeness, reachability of all interactive elements, and accessibility compliance when operated via remote control or D-pad."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - spatial-navigation
  - accessibility
  - remote-control
  - 10-foot-ui
  - focus-management
  - smart-tv
  - d-pad
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/remote_input_handling_focus_management.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# 10-Foot Spatial Navigation & Accessibility Audit

**Objective:** Audit a smart TV launcher's spatial navigation implementation to verify that every interactive element is reachable via directional (D-pad/arrow key) input, focus indicators are clearly visible at 10-foot viewing distance, focus never gets trapped or lost, and the navigation model works correctly across launcher tiles, content views, and overlay dialogs.

---

## When to Use

- Use when: Building a full-screen launcher UI designed for TV or remote control operation
- Use when: Using a spatial navigation polyfill (e.g., `spatial-navigation-polyfill`) in an Electron app
- Use when: Users report that certain elements are unreachable via remote/keyboard navigation
- Use when: Testing focus behavior when transitioning between multiple windows or overlays
- Don't use when: Reviewing a mouse/touch-primary web application

---

## Inputs / Context

**Required:**
- HTML files defining the launcher UI layout (e.g., `launcher.html`)
- CSS files governing focus styles and layout
- JavaScript files managing focus state, navigation handlers, and key event listeners
- Spatial navigation polyfill configuration (if any)

**Optional:**
- Preload scripts that add keyboard event listeners
- Screenshots or screen recordings of the UI at different navigation states
- List of supported remote control buttons and their keyboard mappings

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify every interactive element (buttons, tiles, links, controls) is reachable using only arrow keys and Enter
- Confirm focus indicator is visible with sufficient contrast at 10-foot viewing distance (minimum 3:1 contrast ratio, recommended 4.5:1)
- Test focus behavior across all navigation contexts: launcher grid, content browser, player controls, overlay dialogs, cross-window transitions
- Document the focus order for each screen/context as a navigable map

**Must Not:**
- Assume mouse/pointer navigation testing covers remote control scenarios — spatial navigation resolves focus differently than tab order
- Flag elements as inaccessible without testing directional approach from all four directions
- Report CSS `:focus` styles as sufficient without verifying they are visible on actual TV display resolutions (720p–4K)
- Ignore the distinction between browser focus (`:focus`) and spatial navigation focus (may use custom attributes/classes)

---

## Steps

1. **Map all interactive elements per screen**
   - For each screen/view (launcher, YouTube browser, Disney+ wrapper, settings), list every interactive element
   - Classify each element: tile, button, link, input, custom control, player control
   - Note the visual layout grid (e.g., launcher is a 2×3 grid of tiles)
   - Identify elements that appear conditionally (overlays, popups, loading states)

2. **Audit spatial navigation configuration**
   - Check how the spatial navigation polyfill is loaded and initialized
   - Verify `tabindex` attributes are set on all interactive elements (spatial navigation requires focusable elements)
   - Check for `data-sn-*` or equivalent custom attributes that guide spatial resolution
   - Identify any `focusable: false` or `aria-hidden` elements that should be excluded from navigation
   - Verify that the polyfill handles dynamic content (elements added/removed after initial load)

3. **Test focus reachability (per screen)**
   For each screen, construct a reachability matrix:
   - Starting from each element, verify you can reach every adjacent element using Up/Down/Left/Right
   - Identify dead ends: elements from which a direction leads to no focus change
   - Identify focus traps: regions where arrow keys cycle within a small group with no escape
   - Test edge behavior: What happens when pressing Right on the rightmost tile? Does focus wrap, stay, or jump unexpectedly?
   - Verify initial focus: When a screen opens, which element receives focus first?

4. **Evaluate focus indicators**
   - Check CSS `:focus` and `:focus-visible` styles for all interactive elements
   - Verify focus indicators are not just color changes (use outline, border, scale, glow, or background change)
   - Check visibility at TV resolutions: focus ring should be at least 2px wide, with high contrast
   - Verify focus indicator is visible on all background colors used in the app
   - Check that focus transitions are animated smoothly (not jarring jumps)

5. **Audit cross-context focus transitions**
   - When the YouTube window opens from the launcher, where does focus go? Is it predictable?
   - When pressing Back/Escape to return to the launcher, does focus return to the previously selected tile?
   - When an overlay dialog opens (e.g., parental controls prompt), does focus move into the dialog and trap there correctly?
   - When a dialog closes, does focus return to the element that triggered it?
   - When a player window opens and closes, is focus restored to the content browser?

6. **Check key event handling**
   - Verify Back/Escape behavior: closes innermost overlay first, then returns to parent context
   - Verify Home button: always returns to launcher regardless of depth
   - Verify Enter: activates the focused element (not just clicks it — some custom elements need explicit handling)
   - Check for key event conflicts: if multiple listeners handle the same key, verify correct propagation/stopping
   - Verify long-press behavior (if supported): does holding a direction auto-repeat at a reasonable rate?

7. **CRITICAL: Verify findings before reporting**
   - Test navigation issues in the actual spatial navigation polyfill context, not just by inspecting tab order
   - Confirm that reported focus traps are not intentional (e.g., modal dialogs should trap focus)
   - Verify focus indicator issues on actual target resolution, not just desktop browser
   - Consider that some "unreachable" elements may be intentionally excluded from remote navigation (mouse-only actions)

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag modal dialogs as focus traps — they SHOULD trap focus until dismissed
- Report `tabindex="-1"` elements as broken — they are focusable programmatically but excluded from tab order (may still be reachable via spatial navigation)
- Flag focus wrapping (right from last column jumps to first column of next row) as a bug if it's an intentional design choice
- Report scroll containers as navigation blockers without testing whether the polyfill handles internal scrolling
- Assume desktop keyboard tab order matches TV remote spatial navigation — they work differently

**DO:**
- Test from every edge element in every direction to verify dead-end behavior is intentional
- Verify that initial focus on each screen is on the most logical element (e.g., first content tile, not a hidden control)
- Confirm that focus indicators have sufficient contrast against ALL backgrounds they appear on
- Test navigation after dynamic content loads (e.g., YouTube thumbnails loading after the grid appears)
- Verify that off-screen elements (scrolled out of view) are either excluded from navigation or auto-scroll into view when focused

---

## Expected Output

### Executive Summary
Assessment of spatial navigation completeness, focus visibility, and usability for remote-only operation.

### Navigation Map (per screen)
```
Launcher Screen:
┌─────────┬─────────┬─────────┐
│ YouTube │ Disney+ │ Settings│  Row 1
│  [1,1]  │  [1,2]  │  [1,3]  │
├─────────┼─────────┼─────────┤
│ Channel │ Channel │ Channel │  Row 2
│  [2,1]  │  [2,2]  │  [2,3]  │
└─────────┴─────────┴─────────┘

Initial focus: [1,1]
Edge behavior:
  - Left from [x,1]: No movement (stays)
  - Right from [x,3]: No movement (stays)
  - Up from [1,x]: No movement (stays)
  - Down from [2,x]: No movement (stays)
```

### Reachability Matrix
| Element | Reachable from Up | Reachable from Down | Reachable from Left | Reachable from Right | Status |
|---------|-------------------|--------------------|--------------------|---------------------|--------|
| ...     | ...               | ...                | ...                | ...                 | ...    |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line` and screen/context
- **Evidence:** [Navigation steps that reproduce the issue]
- **Impact:** [Element unreachable, focus lost, navigation confusing for child user]
- **Recommendation:** [Specific fix — tabindex addition, spatial nav hint, CSS change]
- **What would change this assessment:** [Evidence that would modify severity]

### Focus Indicator Review
| Element Type | `:focus` Style | Visible at 10ft? | Contrast Ratio | Verdict |
|-------------|---------------|-------------------|----------------|---------|
| ...         | ...           | ...               | ...            | ...     |

### Prioritized Recommendations
| # | Action | Severity | User Impact |
|---|--------|----------|-------------|
| 1 | ...    | ...      | ...         |

---

## Verification

**Quick self-check:**
- [ ] Every interactive element on every screen has been tested for reachability
- [ ] Focus indicators checked for visibility at target viewing distance
- [ ] Cross-context transitions (launcher ↔ content ↔ player ↔ dialog) all tested
- [ ] Back/Escape/Home key behavior verified at every navigation depth
- [ ] No focus traps exist outside of intentional modal contexts

**High-stakes option (for kids using remotes):**
After completing the audit:
1. Can a 4-year-old with a simple 5-button remote (Up, Down, Left, Right, OK) reach every intended feature?
2. If focus gets "lost" (e.g., after a dynamic content update), is there a recovery path?
3. What happens if the child holds down an arrow key for 5 seconds — does the focus move predictably?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Targets specific spatial navigation completeness
- **ST-02 (Structured Sequential Instructions):** Screen-by-screen audit methodology
- **RT-02 (Multi-Dimensional Analysis):** Reachability, visibility, cross-context, key handling dimensions
- **RT-05 (Evidence-Based Reasoning):** Navigation steps must be reproducible from specific elements
- **DS-06 (Prioritization Guidance):** Ranked by user impact for remote-only child users

---

## Related Prompts

- [Remote-First Input Handling & Focus Management](remote_input_handling_focus_management.md) - Deeper dive into key event handling and hardware remote integration
- [Accessibility WCAG Audit](../../domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md) - Broader web accessibility analysis

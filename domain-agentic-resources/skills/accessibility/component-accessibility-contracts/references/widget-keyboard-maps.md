# Widget Keyboard Maps, Roles and Focus Models

Condensed from the WAI-ARIA Authoring Practices Guide (APG) patterns. Use it to draft
contract clauses quickly, then check the APG page for the pattern before finalising,
because APG guidance is revised over time. Verify against current docs.

Keys listed as "optional" are recommended by APG but not required; decide per component
and write the decision into the contract.

## Contents

1. Button / toggle button
2. Disclosure (show/hide)
3. Accordion
4. Tabs
5. Modal dialog
6. Menu button + menu
7. Combobox with listbox popup
8. Listbox
9. Radio group (custom)
10. Switch
11. Slider
12. Tooltip
13. Status messages and toasts

---

## 1. Button / toggle button

| Item | Requirement |
|---|---|
| Role | `button` (native `<button>` preferred) |
| Name | Visible text, or `aria-label` for icon-only |
| State | Toggle button: `aria-pressed="true|false"`; label must not change when state changes |
| Keys | Enter and Space activate |
| Focus | In Tab sequence |

## 2. Disclosure (show/hide)

| Item | Requirement |
|---|---|
| Role | `button` controlling a region |
| State | `aria-expanded` on the button; optional `aria-controls` pointing at the region |
| Keys | Enter and Space toggle |
| Focus | Stays on the button after toggling |
| Native option | `<details>`/`<summary>` |

## 3. Accordion

| Item | Requirement |
|---|---|
| Structure | Each header is a heading element containing a `button` |
| State | `aria-expanded` on each button; `aria-controls` to its panel |
| Panel | Optional `role="region"` with `aria-labelledby` to its button (avoid when there are many panels, since each becomes a landmark) |
| Keys | Enter/Space toggle; optional Down/Up arrow between headers; optional Home/End |
| Focus | Each header button in Tab sequence |

## 4. Tabs

| Item | Requirement |
|---|---|
| Roles | `tablist` > `tab`; `tabpanel` for each panel |
| Name | `tablist` labelled via `aria-label` or `aria-labelledby`; each panel `aria-labelledby` its tab |
| State | `aria-selected="true"` on exactly one tab; `aria-controls` from tab to panel |
| Keys | Left/Right arrows (Up/Down if vertical, with `aria-orientation="vertical"`); Home/End optional; Enter/Space activate when using manual activation |
| Focus model | Roving tabindex: selected tab `tabindex="0"`, others `-1`. Panel is focusable (`tabindex="0"`) only if it has no focusable content |
| Decide | Automatic activation (arrow selects) vs manual (arrow moves focus, Enter selects). Use manual when showing a panel is slow |

## 5. Modal dialog

| Item | Requirement |
|---|---|
| Role | `dialog` (or `alertdialog` for urgent confirmations) with `aria-modal="true"`; native `<dialog>` + `showModal()` provides modality |
| Name | `aria-labelledby` to the visible title; optional `aria-describedby` |
| Keys | Escape closes; Tab and Shift+Tab cycle within the dialog |
| Focus on open | First focusable element, or the least destructive action for confirmations, or a static element at the top when content is long |
| Focus on close | Returns to the element that opened it, unless the workflow moves on logically |
| Background | Inert: not reachable by Tab or screen-reader virtual cursor (`inert` attribute or `showModal()`) |

## 6. Menu button + menu

Use only for application-style command menus. Site navigation is a list of links.

| Item | Requirement |
|---|---|
| Roles | Trigger `button` with `aria-haspopup="menu"` (or `true`) and `aria-expanded`; popup `menu` > `menuitem` / `menuitemcheckbox` / `menuitemradio` |
| Keys on trigger | Enter, Space, Down arrow open and focus first item; optional Up arrow opens and focuses last item |
| Keys in menu | Up/Down move; Home/End; Escape closes and returns focus to trigger; Enter activates; typing a character moves to the next item starting with it (optional) |
| Focus model | Roving tabindex or `aria-activedescendant`; menu items are not in the page Tab sequence |
| Tab key | Closes the menu and moves focus onward (do not trap) |

## 7. Combobox with listbox popup

| Item | Requirement |
|---|---|
| Roles | Input `role="combobox"`; popup `listbox` > `option` |
| State | `aria-expanded` on the combobox; `aria-controls` to the listbox; `aria-activedescendant` to the highlighted option; `aria-selected` on the highlighted/selected option; `aria-autocomplete="list|both|none"` describing behaviour |
| Keys | Down arrow opens and moves into options; Up/Down move; Enter accepts; Escape closes (second Escape may clear); Alt+Down opens without moving (optional) |
| Focus model | `aria-activedescendant`: DOM focus stays in the input so typing continues |
| Announce | Result count changes via a polite live region ("5 results") if not otherwise announced |

## 8. Listbox

| Item | Requirement |
|---|---|
| Roles | `listbox` > `option`; `aria-multiselectable="true"` for multi-select |
| State | `aria-selected` on options |
| Keys | Up/Down; Home/End; type-ahead (recommended for lists over ~7 items); multi-select: Space toggles, Shift+arrows extend (optional) |
| Focus model | Roving tabindex or `aria-activedescendant` |
| Large lists | `aria-setsize`/`aria-posinset` when virtualised |

## 9. Radio group (custom)

| Item | Requirement |
|---|---|
| Roles | `radiogroup` > `radio`; group labelled |
| State | `aria-checked` on each radio |
| Keys | Arrow keys move and check; Space checks the focused radio if unchecked |
| Focus model | Roving tabindex: checked radio (or first, if none checked) is the single tab stop |
| Native option | `<fieldset>` + `<legend>` + `<input type="radio">` |

## 10. Switch

| Item | Requirement |
|---|---|
| Role | `switch` (can be applied to `<input type="checkbox">` or `<button>`) |
| State | `aria-checked="true|false"` (native checkbox state if using an input) |
| Keys | Space toggles; Enter optional |
| Label | Does not change with state ("Notifications", not "Turn notifications on") |

## 11. Slider

| Item | Requirement |
|---|---|
| Role | `slider` on the thumb |
| State | `aria-valuenow`, `aria-valuemin`, `aria-valuemax`; `aria-valuetext` when the number alone is not meaningful ("3 of 5 stars", "$40") |
| Keys | Right/Up increase; Left/Down decrease; Home/End to min/max; Page Up/Page Down larger steps (optional) |
| Pointer | WCAG 2.2 SC 2.5.7 requires a single-pointer alternative to dragging (for example, clicking on the track or +/- buttons) |
| Native option | `<input type="range">` |

## 12. Tooltip

| Item | Requirement |
|---|---|
| Role | `tooltip` on the popup; trigger has `aria-describedby` pointing at it |
| Behaviour | Appears on focus as well as hover; Escape dismisses without moving focus; hoverable and persistent (WCAG 1.4.13) |
| Content | Plain text only; no interactive content (use a non-modal dialog or disclosure instead) |

## 13. Status messages and toasts

| Item | Requirement |
|---|---|
| Role | `status` (polite) for routine confirmations; `alert` (assertive) only for urgent errors |
| Focus | Do not move focus to a toast; it must not steal focus from the user's task |
| Timing | Messages that disappear need enough time to read, or a way to review them (WCAG 2.2.1) |
| Mounting | The live region must exist in the DOM before its text changes |
| Actions | A toast with an action ("Undo") must make that action reachable by keyboard and must not vanish while focused |

---
name: component-accessibility-contracts
description: Writes a per-component accessibility contract (native-element decision, role, accessible name, states, keyboard map, focus rules, announcements) and turns each clause into an automated component test plus a short manual check. Use when building or reviewing a custom widget or design-system component, or when asked to "make my custom dropdown accessible", "add keyboard support to this component", "what ARIA does this widget need", or "write accessibility acceptance criteria".
metadata:
  tags:
    - a11y
    - accessibility
    - aria
    - components
    - design-system
    - keyboard
    - testing
  updated: "2026-10-04"
---
# Component Accessibility Contracts

Turns "make this component accessible" into a written contract with numbered clauses,
each of which has a test that fails when the clause breaks. The contract lives next to
the component, so the next person to change the component inherits the guarantees
instead of rediscovering them.

## Purpose

Custom widgets are where most keyboard and screen-reader defects come from, and they
regress quietly: a refactor drops `aria-expanded`, a portal breaks focus return, and no
page-level scanner notices. Automated rule engines such as axe check that ARIA is
*valid*; they cannot check that ArrowRight moves to the next tab or that Escape returns
focus to the trigger. A contract plus behaviour tests covers that gap.

## When to Use This Skill

- Building a new interactive component (tabs, dialog, combobox, menu button, listbox,
  disclosure, switch, slider, toast) or adding one to a design system
- Reviewing a pull request that changes an interactive component's markup or event handlers
- Writing accessibility acceptance criteria for a component ticket
- A screen-reader or keyboard bug was fixed and needs a test so it cannot return

## When NOT to Use This Skill

- **Implementation reference code for the common widgets.** The one-off prompt
  `domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md`
  gives full ARIA and JavaScript for dialog, tabs, disclosure, combobox and menu button.
  Use it to write the component; use this skill to specify and test it.
- **Auditing a whole page or site against WCAG.** Use `wcag-audit-patterns`.
- **Automated scanning in CI with a regression baseline.** Use `accessibility-regression-gate`.
- **In-depth screen-reader verification across reader/browser pairs.** Use `screen-reader-testing`.
- **The component is a native element used as intended** (`<button>`, `<a href>`,
  `<select>`, `<input type="checkbox">`). There is nothing to contract beyond a label; check
  the label and stop.

## Prerequisites

- The component source, and any design spec that defines its behaviour
- A DOM test runner. Examples below use Testing Library with `@testing-library/user-event`
  and `@testing-library/jest-dom`; the Playwright equivalents are noted. Verify matcher
  names against the versions installed, because matcher sets change between releases.
- jsdom does not do layout, so focus-visible styling, contrast and reflow need a real
  browser (Playwright, or the manual check in Step 5)

## Workflow

### Step 1: Apply the native-first gate

**Purpose:** Avoid writing ARIA at all where HTML already provides the behaviour.

| Need | Native element | Custom widget justified only if… |
|---|---|---|
| Clickable action | `<button>` | never; style the button instead |
| Navigation | `<a href>` | never |
| Show/hide a section | `<details>`/`<summary>` | animation or styling cannot be achieved |
| Modal dialog | `<dialog>` opened with `showModal()` | target browsers lack support (verify against current docs) |
| Pick one of a few | radio group (`<fieldset>` + `<input type="radio">`) | never for fewer than ~7 options |
| Pick from a list | `<select>` | filtering, rich option content, or multi-select chips are required |
| On/off | `<input type="checkbox">` (optionally `role="switch"`) | — |
| Numeric range | `<input type="range">` | two thumbs or non-linear scale required |

**Output:** either "native element, no contract needed beyond the label" or a named
custom pattern with the reason the native element was rejected. Record the reason in the
contract; it is the first thing a reviewer will ask.

### Step 2: Identify the pattern and focus model

Map the component to its WAI-ARIA Authoring Practices (APG) pattern. The per-widget
keyboard maps, required roles/states and focus models are in
[references/widget-keyboard-maps.md](references/widget-keyboard-maps.md).

Decide the focus model explicitly, because every test depends on it:

- **Roving tabindex:** one item has `tabindex="0"`, the rest `tabindex="-1"`; arrow keys
  move real DOM focus. Used by tabs, radio groups, toolbars, menus.
- **`aria-activedescendant`:** DOM focus stays on the container or input; the active
  option is referenced by id. Used by comboboxes, where focus must stay in the text input.

**Common misclassification:** `role="menu"` is for application-style command menus. Site
navigation is a list of links, optionally behind a disclosure button; giving it menu
semantics changes how screen readers announce and navigate it.

### Step 3: Write the contract

Write numbered clauses. Each clause is a single observable behaviour that a test can
check. Keep the contract in the component's docs or story file.

```markdown
## Accessibility contract: <ComponentName>  (pattern: Tabs, focus model: roving tabindex)

Native element rejected because: <reason>

| ID | Clause | WCAG SC | Test |
|----|--------|---------|------|
| C-ROLE-1 | Container has role=tablist; each tab role=tab; each panel role=tabpanel | 4.1.2 | auto |
| C-NAME-1 | tablist is named via aria-label or aria-labelledby | 4.1.2 | auto |
| C-NAME-2 | each tabpanel is labelled by its tab (aria-labelledby) | 1.3.1 | auto |
| C-STATE-1 | exactly one tab has aria-selected="true" | 4.1.2 | auto |
| C-KEY-1 | ArrowRight/ArrowLeft move focus to next/previous tab, wrapping | 2.1.1 | auto |
| C-KEY-2 | Home/End move focus to first/last tab | 2.1.1 | auto |
| C-FOCUS-1 | only the selected tab is in the Tab sequence | 2.4.3 | auto |
| C-FOCUS-2 | focus indicator visible on every tab, including forced-colors mode | 2.4.7 | manual |
| C-VISUAL-1 | each tab target is at least 24x24 CSS px | 2.5.8 | manual |
| C-ANNOUNCE-1 | screen reader announces "<name>, tab, selected, 2 of 4" or equivalent | 4.1.2 | manual |
```

Rules for clauses:

- One behaviour per clause, with no "and" joining two checkable things.
- State the activation model where the pattern allows a choice (tabs: automatic
  activation on arrow vs manual activation on Enter/Space). Pick one and write it down.
- Mark each clause `auto` or `manual`. Aim for every role, name, state, key and
  focus clause to be `auto`.

### Step 4: Turn each `auto` clause into a test

Query by role and accessible name, never by test id. A test that cannot find the element
by role has already found a defect.

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { Tabs } from './Tabs';

test('C-KEY-1 / C-STATE-1: arrows move focus between tabs and wrap', async () => {
  const user = userEvent.setup();
  render(<Tabs label="Settings" items={['General', 'Privacy', 'Billing']} />);

  const tabs = screen.getAllByRole('tab');
  await user.tab();                                  // C-FOCUS-1: lands on selected tab
  expect(tabs[0]).toHaveFocus();
  expect(tabs[0]).toHaveAttribute('aria-selected', 'true');

  await user.keyboard('{ArrowRight}');
  expect(tabs[1]).toHaveFocus();

  await user.keyboard('{ArrowLeft}{ArrowLeft}');     // wraps to last
  expect(tabs[2]).toHaveFocus();
});

test('C-FOCUS-1: only one tab is in the Tab sequence', () => {
  render(<Tabs label="Settings" items={['General', 'Privacy', 'Billing']} />);
  const inSequence = screen.getAllByRole('tab').filter(t => t.tabIndex === 0);
  expect(inSequence).toHaveLength(1);
});
```

For a modal dialog, the clauses that matter most are focus entry, containment, Escape,
and focus return:

```tsx
test('C-FOCUS dialog: focus enters, Escape closes, focus returns to trigger', async () => {
  const user = userEvent.setup();
  render(<DeleteButtonWithConfirm />);
  const trigger = screen.getByRole('button', { name: 'Delete project' });

  await user.click(trigger);
  const dialog = screen.getByRole('dialog', { name: 'Delete project?' });
  expect(dialog).toContainElement(document.activeElement as HTMLElement);

  await user.keyboard('{Escape}');
  expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
  expect(trigger).toHaveFocus();
});
```

**Playwright equivalent:** `page.getByRole('tab', { name: 'Privacy' })`,
`page.keyboard.press('ArrowRight')`, `await expect(locator).toBeFocused()`,
`await expect(locator).toHaveAttribute('aria-selected', 'true')`. Use Playwright for
clauses that need real layout or real focus behaviour across shadow DOM or iframes.

**Optional:** add a component-level rule scan (for example `jest-axe` or
`@axe-core/playwright` scoped to the component) to catch invalid ARIA. It complements the
behaviour tests and does not replace them.

**Validation checkpoint:**
- [ ] Every `auto` clause ID appears in at least one test name
- [ ] Each test fails when its clause is deliberately broken (remove the attribute or
      the key handler locally and confirm red). A test that stays green when its clause is
      broken is not testing that clause.

### Step 5: Run the manual checks (about five minutes per component)

1. **Keyboard only:** unplug the mouse mentally. Reach, operate and leave the component
   with Tab, Shift+Tab, arrows, Enter, Space and Escape as the contract specifies.
2. **One screen-reader pass:** VoiceOver with Safari, or NVDA with Firefox or Chrome.
   Compare what is announced against the `C-ANNOUNCE` clauses. For reader-specific
   commands see `screen-reader-testing`.
3. **Zoom to 200% and a 320 CSS px wide viewport:** nothing clipped, popups still reachable.
4. **Forced-colors mode** (Windows High Contrast, or emulate `forced-colors: active` in
   browser devtools): focus indicator and selected state still visible, not conveyed only
   by background colour.

Record pass/fail per manual clause in the PR description.

### Step 6: Wire the contract into review

- Link the contract from the component's docs/story.
- Add a PR checklist item for component changes: "Contract clauses still hold; tests
  updated for any behaviour change."
- When a bug is reported against the component, add a clause and a failing test first,
  then fix.

## Verification

The component is done when:

- [ ] Native-first decision recorded with a reason
- [ ] Pattern and focus model named
- [ ] Every role, name, state, keyboard and focus clause is `auto` and has a test that
      was seen failing when the clause was broken
- [ ] Manual clauses checked and recorded in the PR
- [ ] No test locates an interactive element by test id or CSS class

## Common Failure Modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `getByRole('button')` finds nothing | `<div onClick>` without role, or name missing | Use `<button>`; if impossible, add role, `tabindex="0"`, and Enter/Space handlers |
| Two tab stops inside a tablist | Roving tabindex not updated on arrow move | Set the old item to `-1` and the new to `0` in the same handler |
| Focus lost to `<body>` after dialog closes | Trigger unmounted, or focus return not implemented | Store the trigger element on open; restore on close; if it no longer exists, focus a logical fallback |
| Combobox options not announced | `aria-activedescendant` points at an id not in the DOM, or the listbox is rendered in a portal without the id | Ensure the referenced id exists at the moment it is set |
| Live-region message not read | Region inserted into the DOM together with its text | Render the empty live region on mount; change only its text later |
| Screen reader reads hidden content | `aria-hidden="true"` on an ancestor of a focusable element, or visually hidden panel left in the accessibility tree | Use `hidden`/`inert` for inactive panels; never hide focusable content with `aria-hidden` alone |
| Disabled control still activates | `aria-disabled="true"` without blocking the handler | Guard the handler, or use the native `disabled` attribute when removing it from the Tab order is acceptable |

## Edge Cases

- **Shadow DOM:** id references (`aria-labelledby`, `aria-controls`,
  `aria-activedescendant`) do not cross shadow boundaries. Keep referenced ids in the same
  root, or use `aria-label`. Cross-root reference proposals exist; verify browser support
  against current docs before relying on them.
- **Portals:** popups rendered elsewhere in the DOM still need focus return and, for
  menus and listboxes, an `aria-controls` or ownership relationship that resolves.
- **Virtualised lists:** set `aria-setsize` and `aria-posinset` on rendered options so
  position is announced correctly when only a window of items exists.
- **Server-side rendering:** before hydration, buttons rendered by the server do nothing.
  Either render real links/forms that work without script, or disable the control until
  hydrated.
- **Touch and pointer:** the contract still applies to keyboard users on mobile with
  external keyboards; do not drop keyboard clauses for "mobile-only" components.

## Safety & Constraints

**NEVER:**
- Add ARIA roles to native elements that already carry them (`<button role="button">`) or
  override native semantics without a recorded reason
- Mark a clause `manual` only because the test is awkward to write
- Delete a failing contract test to unblock a merge; mark it skipped with a ticket link
  instead, so the gap stays visible

**ALWAYS:**
- Prefer the native element when it meets the requirement
- Keep the contract and the tests in the same change as the behaviour change

## Reference Files

| Resource | Purpose |
|---|---|
| [references/widget-keyboard-maps.md](references/widget-keyboard-maps.md) | Roles, required states, keyboard map and focus model for twelve common widgets |

## Related Skills

- `accessibility-regression-gate`: page-level automated scanning in CI; this skill's
  component tests are the behaviour layer that gate cannot see
- `wcag-audit-patterns`: full WCAG 2.2 audit of a page or flow
- `screen-reader-testing`: reader-specific commands and test scenarios for the
  `C-ANNOUNCE` clauses
- `e2e-testing-patterns` (developer-tools): Playwright and Cypress setup for the
  real-browser checks

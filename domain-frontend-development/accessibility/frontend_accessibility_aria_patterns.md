---
title: "ARIA Implementation Patterns"
category: frontend-development/accessibility
description: "Design and implement accessible ARIA patterns for custom UI components including dialogs, tabs, menus, and interactive widgets"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-01
  - QA-02
difficulty: advanced
tags:
  - accessibility
  - aria
  - wai-aria
  - custom-components
  - semantic-html
  - screen-readers
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-frontend-development/accessibility/frontend_accessibility_screen_reader.md
  - domain-frontend-development/react/frontend_react_component_patterns.md
---

# ARIA Implementation Patterns

**Objective:** Design and implement proper ARIA (Accessible Rich Internet Applications) patterns for custom UI components, ensuring they are fully accessible to assistive technology users.

**When to Use:**
- Use when: Building custom interactive components (dropdowns, modals, tabs)
- Use when: Reviewing existing ARIA implementations for correctness
- Use when: Native HTML elements don't provide needed functionality
- Use when: Debugging screen reader issues with custom components
- Don't use when: Native HTML element would suffice (first rule of ARIA)

## Instructions

1. **Identify Component Type**
   - What interaction pattern does this component follow?
   - Is there a native HTML equivalent?
   - What WAI-ARIA Authoring Practices pattern applies?

2. **Determine Required ARIA**
   - Roles: What role(s) are needed?
   - States: What states change during interaction?
   - Properties: What relationships need to be expressed?

3. **Implement Keyboard Interaction**
   - Map keyboard events to WAI-ARIA patterns
   - Ensure focus management is correct
   - Handle arrow keys, Enter, Space, Escape appropriately

4. **Manage Focus and Announcements**
   - Where should focus go on open/close?
   - What should be announced on state change?
   - Are live regions needed for dynamic content?

5. **CRITICAL: Test with Actual Assistive Technology**
   - Test with at least 2 screen readers
   - Verify announcements match intent
   - Confirm keyboard flow is logical
   - **Confidence level** for implementation:
     - **High Confidence**: Tested with 3+ AT combinations
     - **Medium Confidence**: Tested with 1-2 AT combinations
     - **Low Confidence**: Automated testing only

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Add ARIA to elements that have native semantics (button, input, link)
- Use role="button" on a `<button>` element (redundant)
- Add aria-label when visible text already serves as label
- Use live regions for every dynamic update
- Apply ARIA patterns without keyboard support
- Copy ARIA patterns without understanding them

✅ **DO:**
- Use native HTML first (first rule of ARIA: don't use ARIA if you don't need to)
- Follow WAI-ARIA Authoring Practices exactly
- Test with actual screen readers, not just automated tools
- Ensure state changes are communicated (aria-expanded, aria-selected)
- Keep ARIA simple—complex ARIA is hard to get right
- Update ARIA states in JavaScript when interaction occurs

## Expected Output

ARIA implementation guidance including:
- Correct ARIA pattern for the component
- Complete code example with roles, states, properties
- Keyboard interaction specification
- Testing verification checklist

## Example Output

```markdown
## ARIA Implementation Patterns

### Pattern Selection Guide

| Component | Recommended | Why |
|-----------|-------------|-----|
| Toggle button | Native `<button>` + aria-pressed | Native semantics |
| Dropdown menu | Listbox or menu pattern | Standard interaction |
| Modal dialog | dialog role | Standard pattern |
| Tab interface | tablist/tab/tabpanel | Standard pattern |
| Accordion | Region with button | Simpler than tabs |
| Autocomplete | combobox pattern | Complex but standard |
| Data grid | grid pattern | Complex tabular data |

---

## Pattern 1: Modal Dialog

### Use When
- Blocking content behind it
- User must respond before continuing
- Contains related content or form

### Roles and Properties

```html
<!-- Trigger button -->
<button
  type="button"
  aria-haspopup="dialog"
  aria-expanded="false"
  data-dialog-trigger="signup-modal">
  Open Sign Up Form
</button>

<!-- Modal dialog -->
<div
  id="signup-modal"
  role="dialog"
  aria-modal="true"
  aria-labelledby="signup-title"
  aria-describedby="signup-desc"
  hidden>

  <h2 id="signup-title">Create an Account</h2>
  <p id="signup-desc">Fill in your details to get started.</p>

  <form>
    <label for="email">Email</label>
    <input type="email" id="email" required>

    <label for="password">Password</label>
    <input type="password" id="password" required>

    <button type="submit">Create Account</button>
  </form>

  <button type="button" data-dialog-close aria-label="Close dialog">
    ✕
  </button>
</div>
```

### Keyboard Interaction

| Key | Action |
|-----|--------|
| Tab | Move focus to next focusable element within dialog |
| Shift + Tab | Move focus to previous element within dialog |
| Escape | Close dialog, return focus to trigger |

### Focus Management

```javascript
class ModalDialog {
  constructor(dialogElement) {
    this.dialog = dialogElement;
    this.trigger = document.querySelector(
      `[data-dialog-trigger="${dialogElement.id}"]`
    );
    this.focusableElements = this.getFocusableElements();
    this.firstFocusable = this.focusableElements[0];
    this.lastFocusable = this.focusableElements[this.focusableElements.length - 1];

    this.bindEvents();
  }

  getFocusableElements() {
    return this.dialog.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
  }

  open() {
    this.dialog.hidden = false;
    this.dialog.removeAttribute('hidden');
    this.trigger.setAttribute('aria-expanded', 'true');

    // Store previous focus
    this.previousFocus = document.activeElement;

    // Move focus to dialog
    this.firstFocusable.focus();

    // Trap focus
    document.addEventListener('keydown', this.handleKeydown);

    // Prevent background scroll
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.dialog.hidden = true;
    this.dialog.setAttribute('hidden', '');
    this.trigger.setAttribute('aria-expanded', 'false');

    // Return focus to trigger
    this.previousFocus.focus();

    // Remove event listener
    document.removeEventListener('keydown', this.handleKeydown);

    // Restore scroll
    document.body.style.overflow = '';
  }

  handleKeydown = (event) => {
    if (event.key === 'Escape') {
      this.close();
      return;
    }

    if (event.key === 'Tab') {
      // Focus trap
      if (event.shiftKey) {
        if (document.activeElement === this.firstFocusable) {
          event.preventDefault();
          this.lastFocusable.focus();
        }
      } else {
        if (document.activeElement === this.lastFocusable) {
          event.preventDefault();
          this.firstFocusable.focus();
        }
      }
    }
  };
}
```

### Common Mistakes

❌ **Wrong: No focus trap**
```html
<!-- Focus can escape to background content -->
<div role="dialog">...</div>
```

❌ **Wrong: Focus on dialog container**
```javascript
// Focuses non-interactive element
dialog.focus();
```

✅ **Correct: Focus on first focusable element**
```javascript
// Focuses first interactive element
dialogCloseButton.focus();
```

---

## Pattern 2: Tabs

### Use When
- Switching between related content panels
- Only one panel visible at a time
- Content is in the same context/hierarchy

### Roles and Properties

```html
<div class="tabs-container">
  <!-- Tab list -->
  <div role="tablist" aria-label="Product Information">
    <button
      role="tab"
      id="tab-1"
      aria-selected="true"
      aria-controls="panel-1"
      tabindex="0">
      Description
    </button>
    <button
      role="tab"
      id="tab-2"
      aria-selected="false"
      aria-controls="panel-2"
      tabindex="-1">
      Specifications
    </button>
    <button
      role="tab"
      id="tab-3"
      aria-selected="false"
      aria-controls="panel-3"
      tabindex="-1">
      Reviews
    </button>
  </div>

  <!-- Tab panels -->
  <div
    role="tabpanel"
    id="panel-1"
    aria-labelledby="tab-1"
    tabindex="0">
    <p>Product description content...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-2"
    aria-labelledby="tab-2"
    tabindex="0"
    hidden>
    <p>Product specifications...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-3"
    aria-labelledby="tab-3"
    tabindex="0"
    hidden>
    <p>Customer reviews...</p>
  </div>
</div>
```

### Keyboard Interaction

| Key | Action |
|-----|--------|
| Left Arrow | Move to previous tab (wraps) |
| Right Arrow | Move to next tab (wraps) |
| Home | Move to first tab |
| End | Move to last tab |
| Tab | Move focus into panel |

### JavaScript Implementation

```javascript
class TabList {
  constructor(tablistElement) {
    this.tablist = tablistElement;
    this.tabs = Array.from(this.tablist.querySelectorAll('[role="tab"]'));
    this.panels = this.tabs.map(tab =>
      document.getElementById(tab.getAttribute('aria-controls'))
    );

    this.bindEvents();
  }

  bindEvents() {
    this.tablist.addEventListener('keydown', this.handleKeydown.bind(this));
    this.tabs.forEach(tab => {
      tab.addEventListener('click', () => this.selectTab(tab));
    });
  }

  handleKeydown(event) {
    const currentIndex = this.tabs.indexOf(document.activeElement);

    let newIndex;
    switch (event.key) {
      case 'ArrowLeft':
        newIndex = currentIndex === 0 ? this.tabs.length - 1 : currentIndex - 1;
        break;
      case 'ArrowRight':
        newIndex = currentIndex === this.tabs.length - 1 ? 0 : currentIndex + 1;
        break;
      case 'Home':
        newIndex = 0;
        break;
      case 'End':
        newIndex = this.tabs.length - 1;
        break;
      default:
        return;
    }

    event.preventDefault();
    this.tabs[newIndex].focus();
    this.selectTab(this.tabs[newIndex]);
  }

  selectTab(selectedTab) {
    // Deselect all
    this.tabs.forEach((tab, index) => {
      const selected = tab === selectedTab;
      tab.setAttribute('aria-selected', selected);
      tab.setAttribute('tabindex', selected ? '0' : '-1');
      this.panels[index].hidden = !selected;
    });
  }
}
```

---

## Pattern 3: Disclosure (Accordion)

### Use When
- Showing/hiding content sections
- Content is independent (unlike tabs)
- Can have multiple sections open

### Roles and Properties

```html
<div class="accordion">
  <!-- Accordion item 1 -->
  <h3>
    <button
      type="button"
      aria-expanded="false"
      aria-controls="section-1"
      id="accordion-header-1">
      Shipping Information
      <span aria-hidden="true">▼</span>
    </button>
  </h3>
  <div
    id="section-1"
    role="region"
    aria-labelledby="accordion-header-1"
    hidden>
    <p>We ship to over 100 countries...</p>
  </div>

  <!-- Accordion item 2 -->
  <h3>
    <button
      type="button"
      aria-expanded="false"
      aria-controls="section-2"
      id="accordion-header-2">
      Return Policy
      <span aria-hidden="true">▼</span>
    </button>
  </h3>
  <div
    id="section-2"
    role="region"
    aria-labelledby="accordion-header-2"
    hidden>
    <p>30-day return policy...</p>
  </div>
</div>
```

### JavaScript Implementation

```javascript
class Accordion {
  constructor(containerElement) {
    this.container = containerElement;
    this.buttons = this.container.querySelectorAll('button[aria-expanded]');

    this.bindEvents();
  }

  bindEvents() {
    this.buttons.forEach(button => {
      button.addEventListener('click', () => this.toggle(button));
    });
  }

  toggle(button) {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    const panel = document.getElementById(button.getAttribute('aria-controls'));

    button.setAttribute('aria-expanded', !expanded);
    panel.hidden = expanded;

    // Optional: close others for exclusive accordion
    // this.closeOthers(button);
  }

  closeOthers(exceptButton) {
    this.buttons.forEach(button => {
      if (button !== exceptButton) {
        button.setAttribute('aria-expanded', 'false');
        document.getElementById(button.getAttribute('aria-controls')).hidden = true;
      }
    });
  }
}
```

---

## Pattern 4: Combobox (Autocomplete)

### Use When
- Text input with suggestions
- Search with autocomplete
- Filtering a large list

### Roles and Properties

```html
<div class="combobox-container">
  <label for="city-input" id="city-label">City</label>

  <div class="combobox-wrapper">
    <input
      type="text"
      id="city-input"
      role="combobox"
      aria-autocomplete="list"
      aria-expanded="false"
      aria-controls="city-listbox"
      aria-activedescendant=""
      autocomplete="off">

    <ul
      id="city-listbox"
      role="listbox"
      aria-label="Cities"
      hidden>
      <!-- Options populated dynamically -->
    </ul>
  </div>

  <div
    role="status"
    aria-live="polite"
    aria-atomic="true"
    class="sr-only"
    id="city-status">
    <!-- Status announcements -->
  </div>
</div>
```

### Option HTML

```html
<li
  id="option-1"
  role="option"
  aria-selected="false">
  New York, NY
</li>
```

### Keyboard Interaction

| Key | Action |
|-----|--------|
| Down Arrow | Open list / Move to next option |
| Up Arrow | Move to previous option |
| Enter | Select current option |
| Escape | Close list, clear selection |
| Any character | Filter list |

### JavaScript Implementation

```javascript
class Combobox {
  constructor(inputElement) {
    this.input = inputElement;
    this.listbox = document.getElementById(this.input.getAttribute('aria-controls'));
    this.status = document.getElementById('city-status');
    this.options = [];
    this.activeIndex = -1;

    this.bindEvents();
  }

  bindEvents() {
    this.input.addEventListener('input', this.handleInput.bind(this));
    this.input.addEventListener('keydown', this.handleKeydown.bind(this));
    this.input.addEventListener('blur', this.handleBlur.bind(this));
  }

  async handleInput(event) {
    const query = event.target.value;

    if (query.length < 2) {
      this.close();
      return;
    }

    // Fetch suggestions
    this.options = await this.fetchSuggestions(query);
    this.renderOptions();
    this.open();

    // Announce result count
    this.announce(`${this.options.length} suggestions available`);
  }

  handleKeydown(event) {
    switch (event.key) {
      case 'ArrowDown':
        event.preventDefault();
        this.moveSelection(1);
        break;
      case 'ArrowUp':
        event.preventDefault();
        this.moveSelection(-1);
        break;
      case 'Enter':
        if (this.activeIndex >= 0) {
          event.preventDefault();
          this.selectOption(this.activeIndex);
        }
        break;
      case 'Escape':
        this.close();
        break;
    }
  }

  moveSelection(direction) {
    const maxIndex = this.options.length - 1;
    let newIndex = this.activeIndex + direction;

    if (newIndex < 0) newIndex = maxIndex;
    if (newIndex > maxIndex) newIndex = 0;

    this.setActiveOption(newIndex);
  }

  setActiveOption(index) {
    // Remove previous active
    const prevOption = this.listbox.querySelector('[aria-selected="true"]');
    if (prevOption) prevOption.setAttribute('aria-selected', 'false');

    // Set new active
    const option = this.listbox.children[index];
    option.setAttribute('aria-selected', 'true');
    this.input.setAttribute('aria-activedescendant', option.id);
    this.activeIndex = index;

    // Scroll into view
    option.scrollIntoView({ block: 'nearest' });
  }

  selectOption(index) {
    this.input.value = this.options[index].label;
    this.close();
    this.announce(`${this.options[index].label} selected`);
  }

  open() {
    this.listbox.hidden = false;
    this.input.setAttribute('aria-expanded', 'true');
  }

  close() {
    this.listbox.hidden = true;
    this.input.setAttribute('aria-expanded', 'false');
    this.input.removeAttribute('aria-activedescendant');
    this.activeIndex = -1;
  }

  announce(message) {
    this.status.textContent = message;
  }

  renderOptions() {
    this.listbox.innerHTML = this.options.map((option, index) =>
      `<li id="option-${index}" role="option" aria-selected="false">
        ${option.label}
      </li>`
    ).join('');

    // Add click handlers
    this.listbox.querySelectorAll('[role="option"]').forEach((el, index) => {
      el.addEventListener('click', () => this.selectOption(index));
    });
  }
}
```

---

## Pattern 5: Menu Button

### Use When
- Button that opens a list of actions
- Navigation submenu
- Context menu

```html
<div class="menu-container">
  <button
    type="button"
    aria-haspopup="true"
    aria-expanded="false"
    aria-controls="action-menu"
    id="menu-button">
    Actions
    <span aria-hidden="true">▼</span>
  </button>

  <ul
    id="action-menu"
    role="menu"
    aria-labelledby="menu-button"
    hidden>
    <li role="menuitem" tabindex="-1">Edit</li>
    <li role="menuitem" tabindex="-1">Duplicate</li>
    <li role="separator"></li>
    <li role="menuitem" tabindex="-1">Delete</li>
  </ul>
</div>
```

---

## Live Regions

### When to Use Live Regions

| Scenario | Live Region | Politeness |
|----------|-------------|------------|
| Form error appears | Yes | assertive |
| Search results loaded | Yes | polite |
| Notification toast | Yes | polite or assertive |
| Character count | Maybe | polite |
| Loading spinner | No | - |
| Tab panel content change | No | - |

### Implementation

```html
<!-- Status messages (polite) -->
<div
  role="status"
  aria-live="polite"
  aria-atomic="true">
  3 items added to cart
</div>

<!-- Alert messages (assertive) -->
<div
  role="alert"
  aria-live="assertive"
  aria-atomic="true">
  Error: Please enter a valid email address
</div>
```

---

## Testing Checklist

### For Every Component

- [ ] Keyboard navigation works (Tab, Arrow keys)
- [ ] Focus is visible at all times
- [ ] Focus order is logical
- [ ] Screen reader announces role, name, and state
- [ ] State changes are announced
- [ ] ARIA attributes update correctly

### Screen Reader Testing

| Test With | Platform | Priority |
|-----------|----------|----------|
| NVDA | Windows | High |
| VoiceOver | macOS | High |
| JAWS | Windows | Medium |
| TalkBack | Android | Medium |
| VoiceOver | iOS | Medium |

### Common Issues to Check

- aria-expanded reflects actual state
- aria-selected updates on selection
- aria-activedescendant points to valid ID
- aria-controls/labelledby reference existing elements
- Hidden content has hidden="hidden" or display:none
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on ARIA implementation
- **ST-02 (Structured Sequential Instructions):** Pattern-by-pattern approach
- **RT-02 (Multi-Dimensional Analysis):** Covers multiple component types
- **OC-01 (Output Format Templates):** Complete code examples
- **QA-02 (Adversarial Stress-Test):** Common mistakes highlighted

## Related Prompts

- [frontend_accessibility_wcag_audit.md](frontend_accessibility_wcag_audit.md) - Full WCAG audit
- [frontend_accessibility_screen_reader.md](frontend_accessibility_screen_reader.md) - Testing patterns
- [frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - React component design

## Customization Guide

- **For React**: Use React ARIA or Radix UI primitives
- **For Vue**: Use Vue A11y libraries or Headless UI
- **For Angular**: Use Angular CDK accessibility module
- **For Native Mobile**: Different patterns apply (platform-specific)

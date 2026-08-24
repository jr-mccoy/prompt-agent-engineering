# Screen Reader Testing — JAWS, TalkBack, Test Scenarios, and Debugging

## NVDA Testing Script

```markdown
## NVDA Test Script

### Initial Load
1. Navigate to page
2. Let page finish loading
3. Press Insert + Down to read all
4. Note: Page title, main content identified?

### Landmark Navigation
1. Press D repeatedly
2. Check: All main areas reachable?
3. Check: Landmarks properly labeled?

### Heading Navigation
1. Press Insert + F7 → Headings
2. Check: Logical heading structure?
3. Press H to navigate headings
4. Check: All sections discoverable?

### Form Testing
1. Press F to find first form field
2. Check: Label read?
3. Fill in invalid data
4. Submit form
5. Check: Errors announced?
6. Check: Focus moved to error?

### Interactive Elements
1. Tab through all interactive elements
2. Check: Each announces role and state
3. Activate buttons with Enter/Space
4. Check: Result announced?

### Dynamic Content
1. Trigger content update
2. Check: Change announced?
3. Open modal
4. Check: Focus trapped?
5. Close modal
6. Check: Focus returns?
```

---

## JAWS (Windows)

### Essential Commands

```
Start: Desktop shortcut or Ctrl + Alt + J
Virtual Cursor: Auto-enabled in browsers

Navigation:
Arrow keys         Navigate content
Tab                Next focusable
Insert + Down      Read all
Ctrl               Stop speech

Quick Keys:
H                  Next heading
T                  Next table
F                  Next form field
B                  Next button
G                  Next graphic
L                  Next list
;                  Next landmark

Forms Mode:
Enter              Enter forms mode
Numpad +           Exit forms mode
F5                 List form fields

Lists:
Insert + F7        Link list
Insert + F6        Heading list
Insert + F5        Form field list

Tables:
Ctrl + Alt + Arrows Table navigation
```

---

## TalkBack (Android)

### Setup

```
Enable: Settings → Accessibility → TalkBack
Toggle: Hold both volume buttons 3 seconds
```

### Gestures

```
Explore: Drag finger across screen
Next: Swipe right
Previous: Swipe left
Activate: Double tap
Scroll: Two finger swipe

Reading Controls (swipe up then right):
- Headings
- Links
- Controls
- Characters
- Words
- Lines
- Paragraphs
```

---

## Common Test Scenarios

### 1. Modal Dialog

```html
<!-- Accessible modal structure -->
<div role="dialog"
     aria-modal="true"
     aria-labelledby="dialog-title"
     aria-describedby="dialog-desc">
  <h2 id="dialog-title">Confirm Delete</h2>
  <p id="dialog-desc">This action cannot be undone.</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

```javascript
// Focus management
function openModal(modal) {
  // Store last focused element
  lastFocus = document.activeElement;

  // Move focus to modal
  modal.querySelector('h2').focus();

  // Trap focus
  modal.addEventListener('keydown', trapFocus);
}

function closeModal(modal) {
  // Return focus
  lastFocus.focus();
}

function trapFocus(e) {
  if (e.key === 'Tab') {
    const focusable = modal.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      last.focus();
      e.preventDefault();
    } else if (!e.shiftKey && document.activeElement === last) {
      first.focus();
      e.preventDefault();
    }
  }

  if (e.key === 'Escape') {
    closeModal(modal);
  }
}
```

### 2. Live Regions

```html
<!-- Status messages (polite) -->
<div role="status" aria-live="polite" aria-atomic="true">
  <!-- Content updates will be announced after current speech -->
</div>

<!-- Alerts (assertive) -->
<div role="alert" aria-live="assertive">
  <!-- Content updates interrupt current speech -->
</div>

<!-- Progress updates -->
<div role="progressbar"
     aria-valuenow="75"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-label="Upload progress">
</div>

<!-- Log (additions only) -->
<div role="log" aria-live="polite" aria-relevant="additions">
  <!-- New messages announced, removals not -->
</div>
```

### 3. Tab Interface

```html
<div role="tablist" aria-label="Product information">
  <button role="tab"
          id="tab-1"
          aria-selected="true"
          aria-controls="panel-1">
    Description
  </button>
  <button role="tab"
          id="tab-2"
          aria-selected="false"
          aria-controls="panel-2"
          tabindex="-1">
    Reviews
  </button>
</div>

<div role="tabpanel"
     id="panel-1"
     aria-labelledby="tab-1">
  Product description content...
</div>

<div role="tabpanel"
     id="panel-2"
     aria-labelledby="tab-2"
     hidden>
  Reviews content...
</div>
```

```javascript
// Tab keyboard navigation
tablist.addEventListener('keydown', (e) => {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const index = tabs.indexOf(document.activeElement);

  let newIndex;
  switch (e.key) {
    case 'ArrowRight':
      newIndex = (index + 1) % tabs.length;
      break;
    case 'ArrowLeft':
      newIndex = (index - 1 + tabs.length) % tabs.length;
      break;
    case 'Home':
      newIndex = 0;
      break;
    case 'End':
      newIndex = tabs.length - 1;
      break;
    default:
      return;
  }

  tabs[newIndex].focus();
  activateTab(tabs[newIndex]);
  e.preventDefault();
});
```

---

## Debugging Tips

```javascript
// Log what screen reader sees
function logAccessibleName(element) {
  const computed = window.getComputedStyle(element);
  console.log({
    role: element.getAttribute('role') || element.tagName,
    name: element.getAttribute('aria-label') ||
          element.getAttribute('aria-labelledby') ||
          element.textContent,
    state: {
      expanded: element.getAttribute('aria-expanded'),
      selected: element.getAttribute('aria-selected'),
      checked: element.getAttribute('aria-checked'),
      disabled: element.disabled
    },
    visible: computed.display !== 'none' && computed.visibility !== 'hidden'
  });
}
```

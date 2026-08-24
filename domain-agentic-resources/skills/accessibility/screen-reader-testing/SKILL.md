---
name: screen-reader-testing
description: Test web applications with screen readers including VoiceOver, NVDA, and JAWS. Use when validating screen reader compatibility, debugging accessibility issues, or ensuring assistive technology support.
metadata:
  tags:
    - a11y
    - accessibility
    - debugging
    - reader
    - screen
    - testing
  updated: "2026-04-11"
---
# Screen Reader Testing

Practical guide to testing web applications with screen readers for comprehensive accessibility validation.

## When to Use This Skill

- Validating screen reader compatibility
- Testing ARIA implementations
- Debugging assistive technology issues
- Verifying form accessibility
- Testing dynamic content announcements
- Ensuring navigation accessibility

## Core Concepts

### 1. Major Screen Readers

| Screen Reader | Platform | Browser | Usage |
|---------------|----------|---------|-------|
| **VoiceOver** | macOS/iOS | Safari | ~15% |
| **NVDA** | Windows | Firefox/Chrome | ~31% |
| **JAWS** | Windows | Chrome/IE | ~40% |
| **TalkBack** | Android | Chrome | ~10% |
| **Narrator** | Windows | Edge | ~4% |

### 2. Testing Priority

```
Minimum Coverage:
1. NVDA + Firefox (Windows)
2. VoiceOver + Safari (macOS)
3. VoiceOver + Safari (iOS)

Comprehensive Coverage:
+ JAWS + Chrome (Windows)
+ TalkBack + Chrome (Android)
+ Narrator + Edge (Windows)
```

### 3. Screen Reader Modes

| Mode | Purpose | When Used |
|------|---------|-----------|
| **Browse/Virtual** | Read content | Default reading |
| **Focus/Forms** | Interact with controls | Filling forms |
| **Application** | Custom widgets | ARIA applications |

## VoiceOver (macOS)

### Setup

```
Enable: System Preferences → Accessibility → VoiceOver
Toggle: Cmd + F5
Quick Toggle: Triple-press Touch ID
```

### Essential Commands

```
Navigation:
VO = Ctrl + Option (VoiceOver modifier)

VO + Right Arrow   Next element
VO + Left Arrow    Previous element
VO + Shift + Down  Enter group
VO + Shift + Up    Exit group

Reading:
VO + A             Read all from cursor
Ctrl               Stop speaking
VO + B             Read current paragraph

Interaction:
VO + Space         Activate element
VO + Shift + M     Open menu
Tab                Next focusable element
Shift + Tab        Previous focusable element

Rotor (VO + U):
Navigate by: Headings, Links, Forms, Landmarks
Left/Right Arrow   Change rotor category
Up/Down Arrow      Navigate within category
Enter              Go to item

Web Specific:
VO + Cmd + H       Next heading
VO + Cmd + J       Next form control
VO + Cmd + L       Next link
VO + Cmd + T       Next table
```

### Testing Checklist

```markdown
## VoiceOver Testing Checklist

### Page Load
- [ ] Page title announced
- [ ] Main landmark found
- [ ] Skip link works

### Navigation
- [ ] All headings discoverable via rotor
- [ ] Heading levels logical (H1 → H2 → H3)
- [ ] Landmarks properly labeled
- [ ] Skip links functional

### Links & Buttons
- [ ] Link purpose clear
- [ ] Button actions described
- [ ] New window/tab announced

### Forms
- [ ] All labels read with inputs
- [ ] Required fields announced
- [ ] Error messages read
- [ ] Instructions available
- [ ] Focus moves to errors

### Dynamic Content
- [ ] Alerts announced immediately
- [ ] Loading states communicated
- [ ] Content updates announced
- [ ] Modals trap focus correctly

### Tables
- [ ] Headers associated with cells
- [ ] Table navigation works
- [ ] Complex tables have captions
```

### Common Issues & Fixes

```html
<!-- Issue: Button not announcing purpose -->
<button><svg>...</svg></button>

<!-- Fix -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>

<!-- Issue: Dynamic content not announced -->
<div id="results">New results loaded</div>

<!-- Fix -->
<div id="results" role="status" aria-live="polite">New results loaded</div>

<!-- Issue: Form error not read -->
<input type="email">
<span class="error">Invalid email</span>

<!-- Fix -->
<input type="email" aria-invalid="true" aria-describedby="email-error">
<span id="email-error" role="alert">Invalid email</span>
```

## NVDA (Windows)

### Setup

```
Download: nvaccess.org
Start: Ctrl + Alt + N
Stop: Insert + Q
```

### Essential Commands

```
Navigation:
Insert = NVDA modifier

Down Arrow         Next line
Up Arrow           Previous line
Tab                Next focusable
Shift + Tab        Previous focusable

Reading:
NVDA + Down Arrow  Say all
Ctrl               Stop speech
NVDA + Up Arrow    Current line

Headings:
H                  Next heading
Shift + H          Previous heading
1-6                Heading level 1-6

Forms:
F                  Next form field
B                  Next button
E                  Next edit field
X                  Next checkbox
C                  Next combo box

Links:
K                  Next link
U                  Next unvisited link
V                  Next visited link

Landmarks:
D                  Next landmark
Shift + D          Previous landmark

Tables:
T                  Next table
Ctrl + Alt + Arrows Navigate cells

Elements List (NVDA + F7):
Shows all links, headings, form fields, landmarks
```

### Browse vs Focus Mode

```
NVDA automatically switches modes:
- Browse Mode: Arrow keys navigate content
- Focus Mode: Arrow keys control interactive elements

Manual switch: NVDA + Space

Watch for:
- "Browse mode" announcement when navigating
- "Focus mode" when entering form fields
- Application role forces forms mode
```

The NVDA Testing Script, JAWS Essential Commands, TalkBack setup and gestures, Common Test Scenarios (Modal Dialog, Live Regions, Tab Interface), and Debugging Tips are in the reference file.

See [references/jaws-talkback-test-scenarios.md](references/jaws-talkback-test-scenarios.md)

## Best Practices

### Do's
- **Test with actual screen readers** - Not just simulators
- **Use semantic HTML first** - ARIA is supplemental
- **Test in browse and focus modes** - Different experiences
- **Verify focus management** - Especially for SPAs
- **Test keyboard only first** - Foundation for SR testing

### Don'ts
- **Don't assume one SR is enough** - Test multiple
- **Don't ignore mobile** - Growing user base
- **Don't test only happy path** - Test error states
- **Don't skip dynamic content** - Most common issues
- **Don't rely on visual testing** - Different experience

## Resources

- [VoiceOver User Guide](https://support.apple.com/guide/voiceover/welcome/mac)
- [NVDA User Guide](https://www.nvaccess.org/files/nvda/documentation/userGuide.html)
- [JAWS Documentation](https://support.freedomscientific.com/Products/Blindness/JAWS)
- [WebAIM Screen Reader Survey](https://webaim.org/projects/screenreadersurvey/)

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/jaws-talkback-test-scenarios.md` | NVDA Testing Script, JAWS Essential Commands, TalkBack setup and gestures, Common Test Scenarios (Modal Dialog, Live Regions, Tab Interface), Debugging Tips |

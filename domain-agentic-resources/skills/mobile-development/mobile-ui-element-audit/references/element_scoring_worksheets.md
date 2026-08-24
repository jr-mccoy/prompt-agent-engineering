# Element Scoring Worksheets

Ready-to-use scoring templates for common mobile UI elements. Copy and fill in for each audit.

## Button Audit Worksheet

```
ELEMENT: [Button name/location]
PLATFORM: [iOS / Android / Both]
TYPE: [Primary CTA / Secondary / Tertiary / Icon / FAB]
SCREEN: [Where it appears]
BUSINESS GOAL: [What should tapping this achieve?]

DIMENSION 1: Visual Polish (15%)                          Score: __/10
├─ Background color: [hex] — contrast ratio vs page: [ratio]
├─ Text color: [hex] — contrast ratio vs button bg: [ratio]
├─ Font: [family] [weight] [size] — matches design system? [Y/N]
├─ Corner radius: [dp/pt] — matches other buttons? [Y/N]
├─ Padding: H=[dp/pt] V=[dp/pt] — follows grid? [Y/N]
├─ Shadow/elevation: [values] — appropriate for hierarchy? [Y/N]
├─ Icon (if present): [size] [alignment] [spacing from text]
└─ Dark mode: [appears correct? contrast maintained?]

DIMENSION 2: Interaction Feedback (15%)                    Score: __/10
├─ Press response time: [<100ms / 100-200ms / >200ms]
├─ Press visual: [scale/opacity/color change/ripple] — values: [specifics]
├─ Release animation: [spring/ease/none] — duration: [ms]
├─ Haptic feedback: [none / light / medium / heavy / selection]
├─ Sound feedback: [none / click / custom]
└─ Action confirmation: [how is success communicated?]

DIMENSION 3: State Completeness (12%)                      Score: __/10
├─ Default: [described] ........................... [✓/✗]
├─ Pressed/Active: [described] .................... [✓/✗]
├─ Focused (keyboard/a11y): [described] ........... [✓/✗]
├─ Disabled: [described] .......................... [✓/✗]
├─ Loading: [described] ........................... [✓/✗]
├─ Error: [described] ............................. [✓/✗]
├─ Success: [described] ........................... [✓/✗]
└─ Hover (iPadOS/desktop): [described] ............ [✓/✗]

DIMENSION 4: Animation Quality (10%)                       Score: __/10
├─ Press animation duration: [ms] — appropriate? [Y/N]
├─ Easing curve: [name] — matches intent? [Y/N]
├─ State transition smoothness: [smooth / jerky / none]
├─ 60fps maintained? [Y/N]
└─ Animation serves a purpose? [Y/N — what purpose?]

DIMENSION 5: Accessibility (12%)                           Score: __/10
├─ Touch target: [W]x[H] dp/pt — meets minimum? [≥48dp/44pt]
├─ Text contrast ratio: [ratio] — WCAG AA? [≥4.5:1]
├─ VoiceOver/TalkBack label: [text] — accurate? [Y/N]
├─ Accessibility hint: [text] — helpful? [Y/N]
├─ Dynamic type scaling: [works / breaks / untested]
├─ Color independence: [info conveyed without color? Y/N]
└─ Focus order: [logical position in focus sequence? Y/N]

DIMENSION 6: Engagement Potential (10%)                    Score: __/10
├─ Visual magnetism: [draws eye? Y/N — why?]
├─ Tap satisfaction: [satisfying to press? Y/N]
├─ Reward potential: [does tapping create a reward? what kind?]
├─ Investment creation: [does interaction create user investment?]
└─ Variable element: [does anything change between interactions?]

DIMENSION 7: Consistency (8%)                              Score: __/10
├─ Design system compliance: [matches tokens? Y/N]
├─ Other buttons consistent: [same style as similar buttons? Y/N]
├─ Platform convention: [follows Material/HIG? Y/N]
└─ Animation consistency: [same timing/easing as other elements? Y/N]

DIMENSION 8: Performance (6%)                              Score: __/10
├─ Render delay: [none / noticeable / significant]
├─ Animation framerate: [60fps / drops / untested]
└─ Resource usage: [efficient / wasteful]

DIMENSION 9: Platform Fit (6%)                             Score: __/10
├─ Feels native: [Y/N — why not?]
├─ System settings respected: [dark mode / dynamic type / reduce motion]
└─ Platform gesture compatibility: [no conflicts with system gestures?]

DIMENSION 10: Emotional Impact (6%)                        Score: __/10
├─ Evokes intended emotion: [Y/N — what emotion?]
├─ Brand contribution: [reinforces brand? Y/N]
└─ Delight factor: [creates any delight? Y/N — how?]

OVERALL SCORE: __(weighted calculation)__/100
RATING: [Exceptional/Excellent/Good/Adequate/Needs Work/Major Redesign]

TOP 3 IMPROVEMENTS:
1. [Improvement] — impact: [score gain] — effort: [1-5]
2. [Improvement] — impact: [score gain] — effort: [1-5]
3. [Improvement] — impact: [score gain] — effort: [1-5]
```

---

## Card Component Audit Worksheet

```
ELEMENT: [Card name/location]
PLATFORM: [iOS / Android / Both]
TYPE: [Content card / Action card / Navigation card / Info card]
SCREEN: [Where it appears — list / grid / standalone]
BUSINESS GOAL: [What should the card communicate/achieve?]

DIMENSION 1: Visual Polish (15%)                          Score: __/10
├─ Background: [color/hex] — contrast vs page: [ratio]
├─ Border: [none / solid / subtle] — color: [hex] width: [dp/pt]
├─ Corner radius: [dp/pt] — consistent with app? [Y/N]
├─ Shadow/elevation: [values] — hierarchy appropriate? [Y/N]
├─ Internal padding: [all sides dp/pt] — follows grid? [Y/N]
├─ Title typography: [family] [weight] [size] [color]
├─ Body typography: [family] [weight] [size] [color]
├─ Image (if present): [aspect ratio] [corner treatment] [loading state]
├─ Spacing between elements: [dp/pt] — consistent? [Y/N]
├─ Dark mode: [correct colors? contrast maintained?]
└─ Card-to-card spacing (in list): [dp/pt]

DIMENSION 2: Interaction Feedback (15%)                    Score: __/10
├─ Tappable? [Y/N] — affordance clear? [Y/N]
├─ Press state: [scale/elevation/color change] — values: [specifics]
├─ Release animation: [spring/ease/none] — duration: [ms]
├─ Swipe actions: [none / left / right / both] — what actions?
├─ Long-press: [none / context menu / drag]
├─ Haptic on press: [none / light / selection]
└─ Expansion animation: [if expandable — duration: [ms] easing: [curve]]

DIMENSION 3: State Completeness (12%)                      Score: __/10
├─ Default: [described] ........................... [✓/✗]
├─ Pressed: [described] ........................... [✓/✗]
├─ Loading/skeleton: [described] .................. [✓/✗]
├─ Error content: [described] ..................... [✓/✗]
├─ Empty content: [described] ..................... [✓/✗]
├─ Selected/highlighted: [described] .............. [✓/✗]
├─ Expanded (if applicable): [described] .......... [✓/✗]
└─ Partially loaded (image loading): [described] .. [✓/✗]

DIMENSION 4: Animation Quality (10%)                       Score: __/10
├─ List entry animation: [fade/slide/scale] duration: [ms]
├─ Content loading: [shimmer/skeleton/fade] — quality: [rating]
├─ Expand/collapse: duration: [ms] easing: [curve]
├─ Image load transition: [fade/blur-to-sharp/none]
├─ Swipe action reveal: [smooth spring / linear / none]
└─ Reorder animation: [smooth / jumpy / none]

DIMENSION 5: Accessibility (12%)                           Score: __/10
├─ Card as accessible element: [grouped / individual elements]
├─ VoiceOver/TalkBack announcement: [full text read?]
├─ Action label: ["Double tap to open [destination]"]
├─ Custom actions: [swipe actions accessible? Y/N]
├─ Text contrast (all text): [ratios — all ≥ 4.5:1?]
├─ Dynamic type: [text scales? layout adapts? truncation handled?]
└─ Touch target (if tappable): [full card / specific areas only]

DIMENSION 6: Engagement Potential (10%)                    Score: __/10
├─ Content variety: [same every time / personalized / variable]
├─ Visual interest: [draws eye? Y/N]
├─ Action motivation: [desire to tap? what drives it?]
├─ Social proof: [likes / views / indicators present?]
├─ Freshness indicator: ["New" badge / time stamp / changed indicator]
└─ Preview quality: [enough info to decide whether to tap?]

DIMENSIONS 7-10: [Same structure as Button worksheet]

OVERALL SCORE: __/100
```

---

## Navigation Bar Audit Worksheet

```
ELEMENT: Bottom Navigation / Tab Bar
PLATFORM: [iOS / Android / Both]
TAB COUNT: [3 / 4 / 5]
TABS: [Tab1] [Tab2] [Tab3] [Tab4] [Tab5]

DIMENSION 1: Visual Polish (15%)                          Score: __/10
├─ Bar height: [dp/pt] — matches platform standard? [Y/N]
├─ Background: [solid / translucent / blur] — color: [hex]
├─ Active tab icon: [filled / color change / indicator] — color: [hex]
├─ Inactive tab icon: [outlined / dimmed] — color: [hex] opacity: [%]
├─ Active tab label: [font] [weight] [size] [color]
├─ Inactive tab label: [font] [weight] [size] [color]
├─ Icon size: [dp/pt] — consistent? [Y/N]
├─ Indicator style: [pill / underline / dot / none]
├─ Badge (if present): [size] [color] [position] [max count display]
├─ Safe area: [respects home indicator / nav bar?]
├─ Divider/shadow: [top border / shadow / none]
└─ Dark mode: [colors appropriate? contrast maintained?]

DIMENSION 2: Interaction Feedback (15%)                    Score: __/10
├─ Tab tap response: [<100ms / 100-200ms / >200ms]
├─ Tab switch animation: [crossfade / slide / instant]
├─ Active indicator animation: [slide / snap / morph] duration: [ms]
├─ Haptic on tab switch: [none / selection / light impact]
├─ Badge count animation: [scale bounce / fade / none]
├─ Long press behavior: [none / preview / shortcut menu]
└─ Double tap on active tab: [scroll to top / refresh / none]

DIMENSION 3: State Completeness (12%)                      Score: __/10
├─ Default (no selection): [N/A — always has selection]
├─ Active tab: [described] ........................ [✓/✗]
├─ Inactive tabs: [described] ..................... [✓/✗]
├─ Badge present: [described] ..................... [✓/✗]
├─ Badge cleared: [animation?] .................... [✓/✗]
├─ Hidden during scroll: [Y/N] — animation? .......[described]
├─ Landscape orientation: [adapts?] ............... [✓/✗]
└─ Keyboard visible: [hidden / visible / adapts?] . [✓/✗]

DIMENSIONS 4-10: [Same structure as Button worksheet]

OVERALL SCORE: __/100
```

---

## Text Input Audit Worksheet

```
ELEMENT: [Input field name/location]
PLATFORM: [iOS / Android / Both]
TYPE: [Single line / Multi-line / Password / Search / Number / Email / Phone]
SCREEN: [Where it appears]

DIMENSION 1: Visual Polish (15%)                          Score: __/10
├─ Border style: [outlined / underline / filled]
├─ Default border color: [hex] — subtle but visible? [Y/N]
├─ Focus border color: [hex] — prominent? [Y/N]
├─ Error border color: [hex] — clearly red/error? [Y/N]
├─ Background: [hex/transparent] — dark mode? [hex]
├─ Label: [floating / inline / above] — animation: [Y/N]
├─ Placeholder text: [color hex] — legible but subtle? [Y/N]
├─ Input text: [font] [weight] [size] [color]
├─ Corner radius: [dp/pt] — matches design system? [Y/N]
├─ Height: [dp/pt] — touch-friendly? [≥ 48dp]
├─ Helper text: [present? position? color?]
└─ Character count (if applicable): [position? color?]

DIMENSION 2: Interaction Feedback (15%)                    Score: __/10
├─ Focus animation: [border color change / label float / glow]
├─ Focus animation duration: [ms] — smooth? [Y/N]
├─ Typing feedback: [cursor visible? auto-scroll? haptic on keyboard?]
├─ Clear button: [appears when text entered? X icon? tap area?]
├─ Password toggle: [eye icon? position? tap area?]
├─ Error appearance: [shake / red border / error text] — timing: [ms]
├─ Submit/done on keyboard: [action? dismiss keyboard?]
└─ Auto-focus behavior: [correct field focused on screen enter?]

DIMENSION 3: State Completeness (12%)                      Score: __/10
├─ Empty/unfocused: [described] ................... [✓/✗]
├─ Focused/empty: [described] ..................... [✓/✗]
├─ Focused/with text: [described] ................. [✓/✗]
├─ Unfocused/with text: [described] ............... [✓/✗]
├─ Error: [described] ............................. [✓/✗]
├─ Disabled: [described] .......................... [✓/✗]
├─ Read-only: [described] ......................... [✓/✗]
├─ Character limit reached: [described] ........... [✓/✗]
└─ Loading/validating: [described] ................ [✓/✗]

DIMENSIONS 4-10: [Same structure as Button worksheet]

KEYBOARD CONFIGURATION:
├─ Keyboard type: [default/email/number/phone/URL]
├─ Autocapitalize: [none/words/sentences/all]
├─ Autocorrect: [on/off]
├─ Return key label: [done/next/search/go/send]
├─ Secure text entry: [Y/N]
└─ Content type (autofill): [username/password/email/address/etc.]

OVERALL SCORE: __/100
```

---

## Scoring Calculator

```
Overall Score =
  (Dim1 × 0.15) + (Dim2 × 0.15) + (Dim3 × 0.12) + (Dim4 × 0.10) +
  (Dim5 × 0.12) + (Dim6 × 0.10) + (Dim7 × 0.08) + (Dim8 × 0.06) +
  (Dim9 × 0.06) + (Dim10 × 0.06)

Maximum possible: 10.0 (multiply by 10 for 100-point scale)

Rating Scale:
  90-100: Exceptional — Industry-leading element
  80-89:  Excellent — Minor polish opportunities only
  70-79:  Good — Several meaningful improvements available
  60-69:  Adequate — Functional but lacking polish
  50-59:  Needs Work — Multiple significant gaps
  Below 50: Major Redesign — Fundamental issues present

Improvement Priority Score:
  (Score_Gain × Dimension_Weight) / Effort_Level

  Higher priority score = implement first
```

# Animation Timing Reference

Comprehensive timing, easing, and physics parameter reference for mobile UI micro-interactions.

## Easing Curves

### Standard Curves

| Curve Name | CSS Equivalent | Compose | SwiftUI | Use Case |
|-----------|---------------|---------|---------|----------|
| ease-in | cubic-bezier(0.42, 0, 1, 1) | FastOutLinearInEasing | .easeIn | Elements leaving the screen |
| ease-out | cubic-bezier(0, 0, 0.58, 1) | LinearOutSlowInEasing | .easeOut | Elements entering the screen |
| ease-in-out | cubic-bezier(0.42, 0, 0.58, 1) | FastOutSlowInEasing | .easeInOut | State changes, position moves |
| linear | cubic-bezier(0, 0, 1, 1) | LinearEasing | .linear | Progress bars, loading indicators |

### Spring Physics Parameters

| Feel | Compose Parameters | SwiftUI Parameters | Use Case |
|------|-------------------|-------------------|----------|
| Snappy | dampingRatio=0.7, stiffness=800 | response=0.2, dampingFraction=0.7 | Button press, toggle |
| Bouncy | dampingRatio=0.5, stiffness=300 | response=0.3, dampingFraction=0.5 | Card bounce, pull release |
| Gentle | dampingRatio=0.8, stiffness=200 | response=0.4, dampingFraction=0.8 | Page transitions, expand |
| Critical | dampingRatio=1.0, stiffness=500 | response=0.25, dampingFraction=1.0 | No overshoot, precise |

## Complete Timing Table

### Touch & Interaction Feedback

| Interaction | Duration | Easing | Properties | Haptic |
|------------|----------|--------|-----------|--------|
| Button press down | 80-100ms | ease-out | scale: 0.95, opacity: 0.9 | light impact |
| Button press release | 150-200ms | spring (snappy) | scale: 1.0, opacity: 1.0 | — |
| Card press down | 100ms | ease-out | scale: 0.98, elevation: -2dp | — |
| Card press release | 200ms | spring (bouncy) | scale: 1.0, elevation: restore | — |
| Toggle switch | 200ms | spring (snappy) | position, color | light impact |
| Checkbox check | 150ms | ease-out | scale: 0→1, opacity: 0→1 | selection |
| Radio button select | 120ms | ease-out | scale: 0→1, opacity: 0→1 | selection |
| Slider thumb drag | immediate | — | position follows finger | selection on tick marks |
| Long press activation | 500ms hold | — | scale: 0.95, haptic at trigger | medium impact |
| Swipe action reveal | spring | spring (snappy) | translate-x, background color | — |
| Pull-to-refresh pull | spring | under-damped spring | translate-y, rotation | — |
| Pull-to-refresh trigger | — | — | — | medium impact |
| Pull-to-refresh complete | 300ms | spring (gentle) | translate-y: 0 | success notification |

### State Transitions

| Transition | Duration | Easing | Properties |
|-----------|----------|--------|-----------|
| Content fade in | 200-300ms | ease-out | opacity: 0→1 |
| Content fade out | 150-200ms | ease-in | opacity: 1→0 |
| Expand/reveal | 250-350ms | ease-in-out | height, opacity |
| Collapse/hide | 200-250ms | ease-in | height, opacity |
| Slide in from right | 300ms | ease-out | translate-x: 100%→0 |
| Slide out to right | 250ms | ease-in | translate-x: 0→100% |
| Slide in from bottom | 300ms | ease-out | translate-y: 100%→0 |
| Slide out to bottom | 250ms | ease-in | translate-y: 0→100% |
| Scale in (appear) | 200ms | spring (bouncy) | scale: 0.8→1, opacity: 0→1 |
| Scale out (disappear) | 150ms | ease-in | scale: 1→0.8, opacity: 1→0 |
| Color change | 200ms | ease-in-out | color, backgroundColor |
| Size change | 300ms | spring (gentle) | width, height |

### Navigation Transitions

| Transition | Duration | Easing | Properties |
|-----------|----------|--------|-----------|
| Push (forward) | 350ms | ease-in-out | translate-x, shadow |
| Pop (back) | 300ms | ease-in-out | translate-x, shadow |
| Modal present | 350ms | spring (gentle) | translate-y, scrim opacity |
| Modal dismiss | 300ms | ease-in | translate-y, scrim opacity |
| Bottom sheet present | 300ms | spring (gentle) | translate-y |
| Bottom sheet dismiss | 250ms | ease-in | translate-y |
| Tab switch | 200ms | ease-in-out | opacity (crossfade) |
| Shared element | 350-400ms | spring (gentle) | bounds, corner radius |

### Loading & Progress

| Animation | Duration | Easing | Properties |
|-----------|----------|--------|-----------|
| Shimmer sweep | 1500ms | linear | gradient translate-x (loop) |
| Spinner rotation | 1200ms | linear | rotation (loop) |
| Progress bar fill | 300ms | ease-out | width (per increment) |
| Skeleton pulse | 1500ms | ease-in-out | opacity: 0.3↔0.7 (loop) |
| Content placeholder → content | 200ms | ease-out | opacity crossfade |

### Celebration & Feedback

| Animation | Duration | Easing | Properties |
|-----------|----------|--------|-----------|
| Checkmark draw | 400ms | ease-out | path stroke (circle + check) |
| Confetti burst | 2000ms | gravity physics | position, rotation, opacity |
| Number counter | 800ms | ease-out | numeric interpolation |
| Badge unlock | 600ms | spring (bouncy) | scale: 0→1.1→1, opacity |
| Star rating fill | 150ms each | ease-out | scale: 0→1.2→1, color |
| Error shake | 400ms | ease-in-out | translate-x: 0→6→-6→4→-4→0 |
| Success pulse | 300ms | ease-out | scale: 1→1.05→1, green glow |

## Platform-Specific Notes

### Android Compose
- Use `graphicsLayer` for transform animations (GPU-accelerated)
- Use `animateFloatAsState` for single-value animations
- Use `updateTransition` for multi-value coordinated animations
- Use `AnimatedVisibility` for enter/exit animations
- Always provide a `label` parameter for animation debugging

### iOS SwiftUI
- Use `withAnimation(.spring(...))` for spring animations
- Use `.animation(.easeInOut, value: state)` for implicit animations
- Use `matchedGeometryEffect` for shared element transitions
- Check `UIAccessibility.isReduceMotionEnabled` and provide alternatives
- Use `PhaseAnimator` for multi-step sequential animations (iOS 17+)

### Cross-Platform (React Native)
- Use `Animated.spring()` with `useNativeDriver: true` for performance
- Use `react-native-reanimated` for complex gesture-linked animations
- Lottie for complex illustration animations (LottieView)

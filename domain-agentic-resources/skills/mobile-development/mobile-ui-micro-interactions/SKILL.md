---
name: mobile-ui-micro-interactions
description: "Design and implement delightful micro-interactions for mobile apps including touch feedback, transitions, loading states, celebration animations, haptic patterns, and state change animations. Covers both iOS (SwiftUI/UIKit) and Android (Compose/View) with production-ready code. Use this skill when designing animations, adding touch feedback, creating loading states, implementing pull-to-refresh, building celebration effects, or when a developer mentions 'micro-interaction', 'animation', 'haptic feedback', 'transition', 'pull-to-refresh', 'skeleton loading', or 'delight'."
metadata:
  tags:
    - mobile
    - ui
    - ux
    - animation
    - micro-interaction
    - haptic
    - transition
    - ios
    - android
    - compose
    - swiftui
  updated: "2026-02-27"
---

# Mobile UI Micro-Interactions

Design and implement micro-interactions that make mobile apps feel alive, responsive, and delightful. Covers the complete spectrum from basic touch feedback to complex celebration animations, with production-ready code for both iOS and Android.

## Purpose

Micro-interactions are the difference between an app that feels functional and one that feels magical. This skill provides a comprehensive catalog of micro-interaction patterns with exact timing, easing, and implementation details so developers can add polish and delight to every touchpoint in their app.

## When to Use This Skill

Use this skill when you need to:
- Design touch/tap feedback for buttons, cards, or interactive elements
- Create smooth transitions between screens or states
- Implement loading states (skeleton, shimmer, progressive)
- Add haptic feedback patterns for iOS and Android
- Build celebration/success animations (confetti, checkmarks, level-ups)
- Design pull-to-refresh, swipe-to-dismiss, or drag interactions
- Animate state changes (expand/collapse, show/hide, toggle)
- Add scroll-linked animations or parallax effects
- Create onboarding animations or feature tutorials

## When NOT to Use This Skill

Do NOT use this skill when:
- Working on backend or data layer code with no UI component
- Building CI/CD or deployment pipelines
- Working on accessibility-only improvements without animation (use accessibility skills)

## Core Micro-Interaction Patterns

### 1. Touch Feedback

Every tappable element needs immediate, satisfying feedback. Users should feel their touch was registered within 50ms.

#### Button Press Effect

**Timing:** Scale down on press (100ms ease-out), scale up on release (200ms spring)

```kotlin
// Android Compose — Bouncy Button
@Composable
fun BouncyButton(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()

    val scale by animateFloatAsState(
        targetValue = if (isPressed) 0.95f else 1f,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessLow
        ),
        label = "buttonScale"
    )

    Surface(
        onClick = onClick,
        modifier = modifier.graphicsLayer {
            scaleX = scale
            scaleY = scale
        },
        interactionSource = interactionSource,
        content = content
    )
}
```

```swift
// iOS SwiftUI — Bouncy Button
struct BouncyButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
            .animation(.spring(response: 0.2, dampingFraction: 0.6), value: configuration.isPressed)
    }
}

// Usage
Button("Tap Me") { /* action */ }
    .buttonStyle(BouncyButtonStyle())
```

#### Card Press Effect

**Timing:** Slight elevation reduction + scale on press, spring back on release

```kotlin
// Android Compose — Pressable Card
@Composable
fun PressableCard(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()

    val elevation by animateDpAsState(
        targetValue = if (isPressed) 1.dp else 4.dp,
        animationSpec = tween(100),
        label = "cardElevation"
    )

    val scale by animateFloatAsState(
        targetValue = if (isPressed) 0.98f else 1f,
        animationSpec = spring(dampingRatio = 0.7f, stiffness = 800f),
        label = "cardScale"
    )

    Card(
        onClick = onClick,
        modifier = modifier.graphicsLayer {
            scaleX = scale
            scaleY = scale
        },
        elevation = CardDefaults.cardElevation(defaultElevation = elevation),
        interactionSource = interactionSource,
    ) {
        content()
    }
}
```

### 2. State Transition Animations

#### Expand/Collapse

**Timing:** 300ms ease-in-out for expand, 250ms ease-in for collapse (collapse feels faster)

```kotlin
// Android Compose — Animated Expand/Collapse
@Composable
fun ExpandableSection(
    title: String,
    content: @Composable () -> Unit
) {
    var expanded by remember { mutableStateOf(false) }

    Column {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .clickable { expanded = !expanded }
                .padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(title, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.weight(1f))
            Icon(
                Icons.Default.ExpandMore,
                contentDescription = if (expanded) "Collapse" else "Expand",
                modifier = Modifier.rotate(
                    animateFloatAsState(
                        targetValue = if (expanded) 180f else 0f,
                        animationSpec = tween(300, easing = FastOutSlowInEasing),
                        label = "chevronRotation"
                    ).value
                )
            )
        }

        AnimatedVisibility(
            visible = expanded,
            enter = expandVertically(
                animationSpec = tween(300, easing = FastOutSlowInEasing)
            ) + fadeIn(animationSpec = tween(300)),
            exit = shrinkVertically(
                animationSpec = tween(250, easing = FastOutLinearInEasing)
            ) + fadeOut(animationSpec = tween(200))
        ) {
            content()
        }
    }
}
```

#### Toggle/Switch

**Timing:** 200ms spring animation with slight overshoot

```swift
// iOS SwiftUI — Satisfying Custom Toggle
struct SatisfyingToggle: View {
    @Binding var isOn: Bool

    var body: some View {
        Capsule()
            .fill(isOn ? Color.green : Color.gray.opacity(0.3))
            .frame(width: 51, height: 31)
            .overlay(
                Circle()
                    .fill(.white)
                    .shadow(radius: 1, y: 1)
                    .padding(2)
                    .offset(x: isOn ? 10 : -10),
                alignment: .center
            )
            .animation(.spring(response: 0.2, dampingFraction: 0.7), value: isOn)
            .onTapGesture {
                let impactFeedback = UIImpactFeedbackGenerator(style: .light)
                impactFeedback.impactOccurred()
                isOn.toggle()
            }
    }
}
```

## Advanced Patterns and Timing

Patterns 3–7 (Loading States/Shimmer, Celebration/Checkmark, Haptics iOS+Android, Pull-to-Refresh, Scroll-Linked/Collapsing Header), the Timing Reference Guide table, Best Practices, and Related Skills are in the reference file.

See [references/advanced-patterns-and-timing.md](references/advanced-patterns-and-timing.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-patterns-and-timing.md` | Patterns 3–7 (Shimmer, Checkmark, Haptics, Pull-to-Refresh, Collapsing Header), Timing Reference Guide table, Best Practices (10 items), Related Skills |

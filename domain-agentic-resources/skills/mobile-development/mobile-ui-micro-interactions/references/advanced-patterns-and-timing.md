# Mobile UI Micro-Interactions — Advanced Patterns and Timing

## Pattern 3: Loading States

#### Skeleton Loading (Shimmer)

**Timing:** 1.5s linear infinite loop, left-to-right gradient sweep

```kotlin
// Android Compose — Shimmer Skeleton
@Composable
fun ShimmerEffect(
    modifier: Modifier = Modifier
) {
    val shimmerColors = listOf(
        Color.LightGray.copy(alpha = 0.6f),
        Color.LightGray.copy(alpha = 0.2f),
        Color.LightGray.copy(alpha = 0.6f)
    )

    val transition = rememberInfiniteTransition(label = "shimmer")
    val translateAnim by transition.animateFloat(
        initialValue = 0f,
        targetValue = 1000f,
        animationSpec = infiniteRepeatable(
            animation = tween(1500, easing = LinearEasing),
            repeatMode = RepeatMode.Restart
        ),
        label = "shimmerTranslate"
    )

    val brush = Brush.linearGradient(
        colors = shimmerColors,
        start = Offset(translateAnim - 500f, 0f),
        end = Offset(translateAnim, 0f)
    )

    Box(
        modifier = modifier
            .clip(RoundedCornerShape(8.dp))
            .background(brush)
    )
}

// Usage — Skeleton Card
@Composable
fun SkeletonCard() {
    Card(modifier = Modifier.fillMaxWidth().padding(16.dp)) {
        Column(modifier = Modifier.padding(16.dp)) {
            ShimmerEffect(Modifier.fillMaxWidth(0.7f).height(20.dp))
            Spacer(Modifier.height(12.dp))
            ShimmerEffect(Modifier.fillMaxWidth().height(14.dp))
            Spacer(Modifier.height(8.dp))
            ShimmerEffect(Modifier.fillMaxWidth(0.9f).height(14.dp))
        }
    }
}
```

## Pattern 4: Celebration & Success Animations

#### Checkmark Success

**Timing:** 400ms total — circle draws (200ms), then checkmark draws (200ms), then subtle scale bounce

```kotlin
// Android Compose — Animated Checkmark
@Composable
fun AnimatedCheckmark(
    visible: Boolean,
    modifier: Modifier = Modifier
) {
    val progress by animateFloatAsState(
        targetValue = if (visible) 1f else 0f,
        animationSpec = tween(400, easing = FastOutSlowInEasing),
        label = "checkProgress"
    )

    val scale by animateFloatAsState(
        targetValue = if (visible) 1f else 0f,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessMediumLow
        ),
        label = "checkScale"
    )

    Canvas(
        modifier = modifier
            .size(64.dp)
            .graphicsLayer { scaleX = scale; scaleY = scale }
    ) {
        val strokeWidth = 4.dp.toPx()
        val center = Offset(size.width / 2, size.height / 2)
        val radius = size.minDimension / 2 - strokeWidth

        // Circle
        drawArc(
            color = Color(0xFF4CAF50),
            startAngle = -90f,
            sweepAngle = 360f * minOf(progress * 2, 1f),
            useCenter = false,
            style = Stroke(strokeWidth, cap = StrokeCap.Round)
        )

        // Checkmark (draws after circle completes)
        if (progress > 0.5f) {
            val checkProgress = (progress - 0.5f) * 2
            val path = Path().apply {
                moveTo(size.width * 0.28f, size.height * 0.52f)
                val midX = size.width * 0.45f
                val midY = size.height * 0.65f
                lineTo(
                    lerp(size.width * 0.28f, midX, minOf(checkProgress * 2, 1f)),
                    lerp(size.height * 0.52f, midY, minOf(checkProgress * 2, 1f))
                )
                if (checkProgress > 0.5f) {
                    val endProgress = (checkProgress - 0.5f) * 2
                    lineTo(
                        lerp(midX, size.width * 0.72f, endProgress),
                        lerp(midY, size.height * 0.38f, endProgress)
                    )
                }
            }
            drawPath(path, Color(0xFF4CAF50), style = Stroke(strokeWidth, cap = StrokeCap.Round))
        }
    }
}
```

## Pattern 5: Haptic Feedback Patterns

#### iOS Haptic Catalog

```swift
// iOS — Haptic Feedback Patterns
struct HapticManager {
    // Button tap — light impact
    static func buttonTap() {
        UIImpactFeedbackGenerator(style: .light).impactOccurred()
    }

    // Toggle switch — medium impact
    static func toggle() {
        UIImpactFeedbackGenerator(style: .medium).impactOccurred()
    }

    // Delete/destructive action — heavy impact
    static func destructive() {
        UIImpactFeedbackGenerator(style: .heavy).impactOccurred()
    }

    // Success completion — success notification
    static func success() {
        UINotificationFeedbackGenerator().notificationOccurred(.success)
    }

    // Error/failure — error notification
    static func error() {
        UINotificationFeedbackGenerator().notificationOccurred(.error)
    }

    // Picker/scroll selection — selection changed
    static func selection() {
        UISelectionFeedbackGenerator().selectionChanged()
    }

    // Long press activation — rigid impact
    static func longPress() {
        UIImpactFeedbackGenerator(style: .rigid).impactOccurred()
    }
}
```

#### Android Haptic Catalog

```kotlin
// Android — Haptic Feedback via View or Compose
// Compose modifier approach
fun Modifier.hapticFeedback(
    feedbackType: HapticFeedbackType = HapticFeedbackType.LongPress
): Modifier = composed {
    val haptic = LocalHapticFeedback.current
    this.then(
        Modifier.pointerInput(Unit) {
            detectTapGestures(
                onPress = { haptic.performHapticFeedback(feedbackType) }
            )
        }
    )
}

// Common haptic patterns in Compose
@Composable
fun HapticButton(onClick: () -> Unit, content: @Composable () -> Unit) {
    val haptic = LocalHapticFeedback.current
    Button(onClick = {
        haptic.performHapticFeedback(HapticFeedbackType.LongPress)
        onClick()
    }) { content() }
}
```

## Pattern 6: Pull-to-Refresh

**Timing:** Elastic overscroll (spring physics), indicator appears at 64dp pull, triggers at 128dp

```kotlin
// Android Compose — Material 3 Pull to Refresh
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PullToRefreshList(
    items: List<String>,
    isRefreshing: Boolean,
    onRefresh: () -> Unit
) {
    val pullToRefreshState = rememberPullToRefreshState()

    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        state = pullToRefreshState
    ) {
        LazyColumn(Modifier.fillMaxSize()) {
            items(items, key = { it }) { item ->
                ListItem(headlineContent = { Text(item) })
            }
        }
    }
}
```

## Pattern 7: Scroll-Linked Animations

#### Collapsing Header

**Timing:** Direct scroll mapping (no animation delay), parallax at 0.5x scroll speed

```kotlin
// Android Compose — Collapsing Header with Parallax
@Composable
fun CollapsibleHeader(
    title: String,
    imageUrl: String,
    content: @Composable () -> Unit
) {
    val scrollState = rememberScrollState()
    val headerHeight = 250.dp
    val minHeaderHeight = 64.dp

    val headerProgress = remember {
        derivedStateOf {
            val maxScroll = with(LocalDensity.current) { (headerHeight - minHeaderHeight).toPx() }
            (scrollState.value / maxScroll).coerceIn(0f, 1f)
        }
    }

    Box {
        // Parallax image
        AsyncImage(
            model = imageUrl,
            contentDescription = null,
            modifier = Modifier
                .fillMaxWidth()
                .height(headerHeight)
                .graphicsLayer {
                    translationY = scrollState.value * 0.5f  // Parallax
                    alpha = 1f - headerProgress.value
                },
            contentScale = ContentScale.Crop
        )

        // Scrollable content
        Column(
            modifier = Modifier
                .verticalScroll(scrollState)
                .padding(top = headerHeight)
        ) {
            content()
        }

        // Collapsed title bar
        TopAppBar(
            title = {
                Text(
                    title,
                    modifier = Modifier.graphicsLayer {
                        alpha = headerProgress.value
                    }
                )
            },
            colors = TopAppBarDefaults.topAppBarColors(
                containerColor = MaterialTheme.colorScheme.surface.copy(
                    alpha = headerProgress.value
                )
            )
        )
    }
}
```

---

## Timing Reference Guide

| Interaction Type | Duration | Easing | Notes |
|-----------------|----------|--------|-------|
| Touch feedback | 80-120ms | ease-out | Must feel instant |
| Button press | 100ms down, 200ms up | spring (0.6 damping) | Slight overshoot on release |
| Toggle switch | 200ms | spring (0.7 damping) | Paired with haptic |
| Expand/collapse | 250-350ms | ease-in-out | Collapse slightly faster |
| Screen transition | 300-400ms | ease-in-out | Shared elements follow spring |
| Fade in | 200-300ms | ease-out | Content appears |
| Fade out | 150-200ms | ease-in | Content disappears (faster) |
| Skeleton shimmer | 1500ms | linear | Infinite loop |
| Success animation | 400-600ms | spring | Celebration should feel earned |
| Error shake | 400ms (3 oscillations) | ease-in-out | 6px amplitude |
| Pull-to-refresh | spring physics | under-damped spring | Elastic feel |
| Scroll parallax | Immediate | linear | 0.3-0.5x scroll speed |

---

## Best Practices Summary

1. **Touch feedback must be instant** — under 100ms response or users feel disconnected
2. **Exits are faster than entrances** — collapse/fade-out should be 20-30% shorter than expand/fade-in
3. **Use spring physics for organic feel** — linear animations feel robotic, springs feel natural
4. **Haptics amplify visual feedback** — pair animations with appropriate haptic patterns
5. **Don't animate everything** — reserve animation for meaningful state changes and user actions
6. **Respect reduced motion** — check `UIAccessibility.isReduceMotionEnabled` (iOS) or `Settings.Global.ANIMATOR_DURATION_SCALE` (Android)
7. **Performance first** — use `graphicsLayer` (Compose) or `CALayer` animations (iOS) to stay on the GPU
8. **Consistent timing** — use the same easing curves throughout your app for a cohesive feel
9. **One animation at a time** — avoid competing animations that create visual noise
10. **Test on real devices** — animations that look smooth in emulators may stutter on lower-end devices

---

## Related Skills

- `jetpack-compose-patterns` - Compose UI fundamentals
- `mobile-ui-habit-loop-design` - Engagement mechanics that use micro-interactions
- `mobile-ui-element-audit` - Comprehensive element-level analysis including animation quality

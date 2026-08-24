# Jetpack Compose Patterns — Material 3 Theming and Common Issues

## Material 3 Theming

### Dynamic Color Theme

```kotlin
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context)
            else dynamicLightColorScheme(context)
        }
        darkTheme -> darkColorScheme()
        else -> lightColorScheme()
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        content = content
    )
}
```

### Custom Color Scheme

```kotlin
private val LightColorScheme = lightColorScheme(
    primary = Color(0xFF6200EE),
    onPrimary = Color.White,
    primaryContainer = Color(0xFFBB86FC),
    onPrimaryContainer = Color(0xFF21005D),
    secondary = Color(0xFF03DAC6),
    onSecondary = Color.Black,
    // ... other colors
)

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFFBB86FC),
    onPrimary = Color.Black,
    primaryContainer = Color(0xFF6200EE),
    onPrimaryContainer = Color.White,
    // ... other colors
)
```

### Typography

```kotlin
val AppTypography = Typography(
    displayLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    headlineMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 28.sp,
        lineHeight = 36.sp,
        letterSpacing = 0.sp
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    )
)
```

---

## Common Issues

### Issue: Unnecessary Recompositions

**Quick Diagnosis:**
- Enable Compose compiler reports in build.gradle
- Use Layout Inspector to track recompositions

**Resolution:**
```kotlin
// Bad: Lambda recreated on every recomposition
Button(onClick = { viewModel.doSomething() }) { ... }

// Good: Stable lambda reference
Button(onClick = viewModel::doSomething) { ... }

// Or use remember for complex lambdas
val onClick = remember { { viewModel.doSomething() } }
```

### Issue: State Lost on Configuration Change

**Resolution:**
```kotlin
// Use rememberSaveable instead of remember
var text by rememberSaveable { mutableStateOf("") }

// Or use ViewModel for complex state
val viewModel: MyViewModel = hiltViewModel()
```

### Issue: Infinite Recomposition Loop

**Resolution:**
```kotlin
// Bad: State change triggers recomposition that changes state
@Composable
fun BadExample() {
    var count by remember { mutableStateOf(0) }
    count++ // DON'T DO THIS
}

// Good: Change state only in response to events
@Composable
fun GoodExample() {
    var count by remember { mutableStateOf(0) }
    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}
```

### Issue: Navigation Memory Leak

**Resolution:**
```kotlin
// Always use currentBackStackEntryAsState for navigation state
val navBackStackEntry by navController.currentBackStackEntryAsState()
val currentRoute = navBackStackEntry?.destination?.route
```

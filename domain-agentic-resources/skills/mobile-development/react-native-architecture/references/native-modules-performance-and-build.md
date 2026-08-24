# React Native Architecture — Native Modules, Performance & Build

## Pattern 4: Native Module Integration

```typescript
// services/haptics.ts
import * as Haptics from 'expo-haptics'
import { Platform } from 'react-native'

export const haptics = {
  light: () => {
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)
    }
  },
  medium: () => {
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)
    }
  },
  heavy: () => {
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy)
    }
  },
  success: () => {
    if (Platform.OS !== 'web') {
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success)
    }
  },
  error: () => {
    if (Platform.OS !== 'web') {
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error)
    }
  },
}

// services/biometrics.ts
import * as LocalAuthentication from 'expo-local-authentication'

export async function authenticateWithBiometrics(): Promise<boolean> {
  const hasHardware = await LocalAuthentication.hasHardwareAsync()
  if (!hasHardware) return false

  const isEnrolled = await LocalAuthentication.isEnrolledAsync()
  if (!isEnrolled) return false

  const result = await LocalAuthentication.authenticateAsync({
    promptMessage: 'Authenticate to continue',
    fallbackLabel: 'Use passcode',
    disableDeviceFallback: false,
  })

  return result.success
}

// services/notifications.ts
import * as Notifications from 'expo-notifications'
import { Platform } from 'react-native'
import Constants from 'expo-constants'

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
  }),
})

export async function registerForPushNotifications() {
  let token: string | undefined

  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('default', {
      name: 'default',
      importance: Notifications.AndroidImportance.MAX,
      vibrationPattern: [0, 250, 250, 250],
    })
  }

  const { status: existingStatus } = await Notifications.getPermissionsAsync()
  let finalStatus = existingStatus

  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync()
    finalStatus = status
  }

  if (finalStatus !== 'granted') {
    return null
  }

  const projectId = Constants.expoConfig?.extra?.eas?.projectId
  token = (await Notifications.getExpoPushTokenAsync({ projectId })).data

  return token
}
```

---

## Pattern 5: Platform-Specific Code

```typescript
// components/ui/Button.tsx
import { Platform, Pressable, StyleSheet, Text, ViewStyle } from 'react-native'
import * as Haptics from 'expo-haptics'
import Animated, {
  useAnimatedStyle,
  useSharedValue,
  withSpring,
} from 'react-native-reanimated'

const AnimatedPressable = Animated.createAnimatedComponent(Pressable)

interface ButtonProps {
  title: string
  onPress: () => void
  variant?: 'primary' | 'secondary' | 'outline'
  disabled?: boolean
}

export function Button({
  title,
  onPress,
  variant = 'primary',
  disabled = false,
}: ButtonProps) {
  const scale = useSharedValue(1)

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }))

  const handlePressIn = () => {
    scale.value = withSpring(0.95)
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)
    }
  }

  const handlePressOut = () => {
    scale.value = withSpring(1)
  }

  return (
    <AnimatedPressable
      onPress={onPress}
      onPressIn={handlePressIn}
      onPressOut={handlePressOut}
      disabled={disabled}
      style={[
        styles.button,
        styles[variant],
        disabled && styles.disabled,
        animatedStyle,
      ]}
    >
      <Text style={[styles.text, styles[`${variant}Text`]]}>{title}</Text>
    </AnimatedPressable>
  )
}

// Platform-specific files
// Button.ios.tsx - iOS-specific implementation
// Button.android.tsx - Android-specific implementation
// Button.web.tsx - Web-specific implementation

// Or use Platform.select
const styles = StyleSheet.create({
  button: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 4,
      },
      android: {
        elevation: 4,
      },
    }),
  },
  primary: {
    backgroundColor: '#007AFF',
  },
  secondary: {
    backgroundColor: '#5856D6',
  },
  outline: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: '#007AFF',
  },
  disabled: {
    opacity: 0.5,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
  primaryText: {
    color: '#FFFFFF',
  },
  secondaryText: {
    color: '#FFFFFF',
  },
  outlineText: {
    color: '#007AFF',
  },
})
```

---

## Pattern 6: Performance Optimization

```typescript
// components/ProductList.tsx
import { FlashList } from '@shopify/flash-list'
import { memo, useCallback } from 'react'

interface ProductListProps {
  products: Product[]
  onProductPress: (id: string) => void
}

// Memoize list item
const ProductItem = memo(function ProductItem({
  item,
  onPress,
}: {
  item: Product
  onPress: (id: string) => void
}) {
  const handlePress = useCallback(() => onPress(item.id), [item.id, onPress])

  return (
    <Pressable onPress={handlePress} style={styles.item}>
      <FastImage
        source={{ uri: item.image }}
        style={styles.image}
        resizeMode="cover"
      />
      <Text style={styles.title}>{item.name}</Text>
      <Text style={styles.price}>${item.price}</Text>
    </Pressable>
  )
})

export function ProductList({ products, onProductPress }: ProductListProps) {
  const renderItem = useCallback(
    ({ item }: { item: Product }) => (
      <ProductItem item={item} onPress={onProductPress} />
    ),
    [onProductPress]
  )

  const keyExtractor = useCallback((item: Product) => item.id, [])

  return (
    <FlashList
      data={products}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      estimatedItemSize={100}
      // Performance optimizations
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      windowSize={5}
      // Pull to refresh
      onRefresh={onRefresh}
      refreshing={isRefreshing}
    />
  )
}
```

---

## EAS Build & Submit

```json
// eas.json
{
  "cli": { "version": ">= 5.0.0" },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "ios": { "simulator": true }
    },
    "preview": {
      "distribution": "internal",
      "android": { "buildType": "apk" }
    },
    "production": {
      "autoIncrement": true
    }
  },
  "submit": {
    "production": {
      "ios": { "appleId": "your@email.com", "ascAppId": "123456789" },
      "android": { "serviceAccountKeyPath": "./google-services.json" }
    }
  }
}
```

```bash
# Build commands
eas build --platform ios --profile development
eas build --platform android --profile preview
eas build --platform all --profile production

# Submit to stores
eas submit --platform ios
eas submit --platform android

# OTA updates
eas update --branch production --message "Bug fixes"
```

---

## Best Practices

### Do's
- **Use Expo** - Faster development, OTA updates, managed native code
- **FlashList over FlatList** - Better performance for long lists
- **Memoize components** - Prevent unnecessary re-renders
- **Use Reanimated** - 60fps animations on native thread
- **Test on real devices** - Simulators miss real-world issues

### Don'ts
- **Don't inline styles** - Use StyleSheet.create for performance
- **Don't fetch in render** - Use useEffect or React Query
- **Don't ignore platform differences** - Test on both iOS and Android
- **Don't store secrets in code** - Use environment variables
- **Don't skip error boundaries** - Mobile crashes are unforgiving

## Resources

- [Expo Documentation](https://docs.expo.dev/)
- [Expo Router](https://docs.expo.dev/router/introduction/)
- [React Native Performance](https://reactnative.dev/docs/performance)
- [FlashList](https://shopify.github.io/flash-list/)

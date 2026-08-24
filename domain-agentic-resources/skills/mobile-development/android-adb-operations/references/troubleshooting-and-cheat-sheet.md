# Android ADB Operations — Troubleshooting and Cheat Sheet

## Troubleshooting Common Issues

### "device not found"
1. Check USB cable (use a data cable, not charge-only)
2. Verify USB debugging is enabled on device
3. Try `adb kill-server && adb start-server`
4. On Linux, check udev rules for your device vendor

### "device unauthorized"
1. Check device screen for USB debugging authorization prompt
2. Tap "Always allow from this computer" and confirm
3. If no prompt appears: revoke USB debugging authorizations in Developer Options, then reconnect

### "device offline"
1. Unplug and re-plug USB cable
2. Try a different USB port
3. Run `adb kill-server && adb start-server`
4. Restart the device

### "INSTALL_FAILED_UPDATE_INCOMPATIBLE"
```bash
# Signing key changed — uninstall first
adb uninstall com.example.myapp
adb install app-debug.apk
```

### "INSTALL_FAILED_INSUFFICIENT_STORAGE"
```bash
# Check device storage
adb shell df -h /data

# Clear unused app data
adb shell pm clear com.example.unused_app
```

### Slow ADB over Wi-Fi
- Ensure both device and computer are on 5GHz Wi-Fi (not 2.4GHz)
- Reduce distance to router
- For large file transfers, temporarily switch to USB

---

## ADB Cheat Sheet

| Task | Command |
|------|---------|
| List devices | `adb devices` |
| Install APK | `adb install -r app.apk` |
| Uninstall | `adb uninstall com.example.app` |
| Start activity | `adb shell am start -n com.example.app/.MainActivity` |
| Force stop | `adb shell am force-stop com.example.app` |
| Clear data | `adb shell pm clear com.example.app` |
| Logcat (errors) | `adb logcat *:E` |
| Logcat (app only) | `adb logcat --pid=$(adb shell pidof -s com.example.app)` |
| Screenshot | `adb exec-out screencap -p > screen.png` |
| Screen record | `adb shell screenrecord /sdcard/rec.mp4` |
| Open deep link | `adb shell am start -a android.intent.action.VIEW -d "URL"` |
| Push file | `adb push local /sdcard/Download/` |
| Pull file | `adb pull /sdcard/file ./` |
| Device info | `adb shell getprop ro.build.version.release` |
| Grant permission | `adb shell pm grant com.example.app android.permission.CAMERA` |
| Revoke permission | `adb shell pm revoke com.example.app android.permission.CAMERA` |
| Wireless pair | `adb pair IP:PAIRING_PORT` |
| Wireless connect | `adb connect IP:PORT` |
| Bug report | `adb bugreport ./bugreport.zip` |
| Dump package info | `adb shell dumpsys package com.example.app` |
| Disable animations | `adb shell settings put global window_animation_scale 0` |

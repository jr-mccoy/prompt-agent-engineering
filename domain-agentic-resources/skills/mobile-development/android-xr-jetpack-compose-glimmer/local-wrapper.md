## Offline reference mirrors

This skill's body links to several developer.android.com pages over HTTPS. Local
mirrors of four of them are bundled here, so the workflow still works without network
access:

| Linked page | Local mirror |
|---|---|
| Build your first activity for intelligent eyewear | `references/android/develop/xr/jetpack-xr-sdk/ai-glasses/first-activity.md` |
| Check device capabilities at runtime | `references/android/develop/xr/jetpack-xr-sdk/ai-glasses/check-capabilities.md` |
| Understand notification behavior | `references/android/develop/xr/jetpack-xr-sdk/ai-glasses/notifications/behavior.md` |
| Start a glasses activity from a notification | `references/android/develop/xr/jetpack-xr-sdk/ai-glasses/notifications/start-activity.md` |

Prefer the live page when you have network access — these mirrors are snapshots and
carry no freshness guarantee.

## Verification

After implementing, confirm:

**Builds and runs**

- [ ] Project builds and IDE sync succeeds
- [ ] The Glasses Activity launches **on the projected device**, not on the phone
- [ ] `android:requiredDisplayCategory="xr_projected"` is set on the Glasses Activity
- [ ] Launch entry point is disabled when glasses are not connected
- [ ] Hardware permissions are requested through the projected-context flow

**Respects the platform constraints in Limitations**

- [ ] No Material 3 shadow or elevation modifiers — `ShadowScope` / `Depth` tokens only
- [ ] No text below 18sp anywhere, including labels and captions
- [ ] No Thin or Hairline font weights
- [ ] Glimmer components used rather than phone Material equivalents
- [ ] Focus handling is explicit; every interactive element is reachable by the mapped
      input controls

**Behaves on device**

- [ ] Legible against a bright real-world background, not just the emulator
- [ ] Degrades sensibly if the glasses disconnect mid-session
- [ ] Notification-launched activities land in the right place

Emulator-only validation is not sufficient — legibility, depth, and input mapping are
the failure modes, and all three need real hardware.

## Related Skills

- [`android-edge-to-edge`](../android-edge-to-edge/) — **do not apply phone
  edge-to-edge patterns here.** XR uses a different safe-area model; that skill is
  for handset Compose only.
- [`jetpack-compose-patterns`](../jetpack-compose-patterns/) — general Compose state
  and composition work, subject to the Glimmer constraints above.
- [`android-rich-notification-system`](../android-rich-notification-system/) —
  phone-side notification design that the glasses experience projects from.
- [`android-accessibility-testing`](../android-accessibility-testing/) — the 18sp
  floor and focus requirements are accessibility constraints first.

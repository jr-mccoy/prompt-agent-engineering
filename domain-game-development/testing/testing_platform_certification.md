---
title: "Platform Certification Checklist"
category: game-development/testing
description: "Generate platform-specific certification checklists for Sony TRC, Microsoft XR, Nintendo Lotcheck, Steam, and App Store submissions"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DS-01
  - QA-02
difficulty: intermediate
tags:
  - testing
  - certification
  - console
  - submission
  - trc
  - lotcheck
  - compliance
updated: "2026-03-19"
related_prompts:
  - domain-game-development/testing/testing_gameplay_test_plan.md
  - domain-game-development/testing/testing_automated_game_testing.md
  - domain-game-development/performance/performance_frame_budget_analysis.md
---

# Platform Certification Checklist

**Objective:** Generate comprehensive, platform-specific certification checklists covering technical requirements, content policies, and submission workflows for console (Sony, Microsoft, Nintendo), PC (Steam, Epic), and mobile (App Store, Google Play) game releases.

## When to Use

- Use when preparing a game for platform submission (first submission or update)
- Use when planning which platforms to target and understanding their requirements early
- Use when a submission has been rejected and you need to identify remaining compliance gaps
- Don't use for general game QA — use `testing_gameplay_test_plan.md` for functional testing

## Instructions

1. **Identify Target Platforms and Requirements**
   - List all target platforms and their certification programs:
     - Sony PlayStation: Technical Requirements Checklist (TRC)
     - Microsoft Xbox: Xbox Requirements (XR)
     - Nintendo Switch: Lotcheck Guidelines
     - Steam: Steamworks Review + Steam Deck Verified
     - Epic Games Store: Epic Review
     - Apple App Store: App Review Guidelines
     - Google Play: Play Console Policies
   - Note platform-specific development kits and SDK versions required
   - Identify region-specific requirements (CERO, PEGI, ESRB ratings)

2. **Generate Technical Compliance Checklist**
   - For each platform, cover:
     - **Boot and initialization:** startup time limits, splash screen requirements, first-party logos
     - **Save data:** platform storage API usage, save size limits, corruption handling
     - **User accounts:** platform account integration, sign-in/sign-out handling, guest mode
     - **Suspend/resume:** proper background behavior, quick resume support (Xbox)
     - **Controller:** button prompts match platform conventions, no hardcoded buttons, accessibility
     - **Network:** online requirements disclosure, offline mode behavior, network error handling
     - **Achievements/trophies:** platform achievement API integration, naming conventions
     - **DLC/IAP:** store integration, entitlement checks, restore purchases
     - **Performance:** framerate requirements, resolution requirements, loading times

3. **Generate Content Policy Checklist**
   - Age rating requirements (IARC, ESRB, PEGI, CERO) and content descriptors
   - User-generated content moderation requirements
   - Loot box/gacha disclosure requirements by region
   - Accessibility requirements (CVAA for US, EAA for EU)
   - Privacy policy and data collection disclosure (COPPA, GDPR)
   - Platform-specific content restrictions (e.g., Nintendo family-friendly expectations)

4. **Generate Submission Workflow**
   - Build and packaging requirements (signing, encryption, manifest files)
   - Metadata preparation (descriptions, screenshots, trailers, store art dimensions)
   - Pre-submission self-test checklist
   - Submission portal steps and expected review timeline
   - Post-submission: handling feedback, resubmission process, expedited review options

5. **Create Platform-Specific Test Cases**
   - For each technical requirement, write a concrete test case:
     - Test ID, description, steps, expected result, pass/fail criteria
   - Group test cases by category (boot, save, network, controller, performance)
   - Flag tests that commonly cause rejection (based on platform feedback patterns)

6. **CRITICAL: Verify Checklist Completeness**
   - Cross-reference against the latest platform documentation (SDKs update requirements)
   - Verify region-specific requirements for each target market
   - Confirm all first-party API integrations are listed (achievements, friends, voice chat)
   - Check that accessibility requirements match current regulations
   - Verify store asset dimensions and format requirements are current

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't assume all platforms have identical requirements — each has unique rules
- Don't skip "obvious" requirements (splash screens, button prompts) — these cause the most rejections
- Don't provide outdated SDK version requirements — always note "verify against current docs"
- Don't assume F2P and premium have the same requirements — IAP adds compliance layers

✅ **DO:**
- Note which requirements are hard fails vs warnings vs recommendations
- Highlight the top 5 most common rejection reasons per platform
- Include timeline estimates for review cycles (first submission vs updates)
- Specify exact asset dimensions (screenshots, icons, banners) per platform
- Call out requirements that differ between regions (Japan vs US vs EU)

## Expected Output

A platform certification compliance document including:

- Per-platform technical requirement checklists with pass/fail criteria
- Content policy compliance matrix
- Submission workflow with timeline estimates
- Test case catalog grouped by requirement category
- Common rejection reasons with prevention strategies
- Store asset specification table

## Example Output

```markdown
## Platform Certification Checklist — "Neon Drift" (Racing Game)

### Target Platforms
- PlayStation 5 (Sony TRC)
- Xbox Series X|S (Microsoft XR)
- Nintendo Switch (Lotcheck)
- Steam (Steamworks + Deck Verified)
- **Rating:** ESRB E10+, PEGI 7, CERO A

---

### PlayStation 5 — Technical Requirements (TRC)

#### Boot & Initialization

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-001 | Display SIE logo on startup | SIE logo shown for minimum 2 seconds, unmodified | ⚠️ Yes |
| TRC-002 | Boot to interactive within 30s | Player can interact within 30s of launch | |
| TRC-003 | Language follows system settings | Game defaults to PS5 system language if supported | ⚠️ Yes |
| TRC-004 | HDCP handling | Game does not break when HDCP is enabled/disabled | |

#### Save Data

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-010 | Use PS5 save data API | All saves use `SceSaveData` API, not raw file I/O | ⚠️ Yes |
| TRC-011 | Save data size declaration | Save size declared in param.json matches actual usage | |
| TRC-012 | Corrupted save handling | Game detects corruption and offers recovery, no crash | ⚠️ Yes |
| TRC-013 | Save icon and description | Each save shows icon and description in system storage | |

#### User Accounts & Network

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-020 | Support multiple PSN accounts | Switching users loads correct profile/saves | |
| TRC-021 | PS Plus requirement disclosure | Online features clearly state PS Plus requirement | ⚠️ Yes |
| TRC-022 | Network error handling | All network errors show user-friendly message, no hang | ⚠️ Yes |
| TRC-023 | Offline mode | Single-player fully functional without internet | |

#### Controller & Input

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-030 | DualSense button prompts | All prompts use PS button names/icons (Cross, Circle) | ⚠️ Yes |
| TRC-031 | Controller disconnect handling | Game pauses, shows reconnect prompt | |
| TRC-032 | DualSense haptics | Adaptive triggers and haptic feedback where appropriate | |
| TRC-033 | PS button behavior | PS button opens system menu at any time | |

#### Trophies

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-040 | Trophy set registered | All trophies registered via PlayStation Partners | |
| TRC-041 | Platinum trophy included | Games with 1+ Gold must include Platinum | |
| TRC-042 | Trophy names/descriptions | No spoilers in trophy descriptions visible before unlock | |

#### Performance

| ID | Requirement | Pass Criteria | Common Fail? |
|----|------------|---------------|--------------|
| TRC-050 | No crashes or hangs | Zero crashes in 20+ hours of testing | ⚠️ Yes |
| TRC-051 | Frame rate stability | No drops below 20 FPS; target mode (30/60) stated | |
| TRC-052 | Loading time limits | No single load screen exceeds 30 seconds | |
| TRC-053 | Resolution modes | Declare performance (60fps) and quality (4K) modes | |

---

### Xbox Series X|S — Xbox Requirements (XR)

#### Top 5 Rejection Reasons (Xbox)
1. **XR-015:** Game doesn't handle Quick Resume correctly (saves/restores state)
2. **XR-022:** Button prompts show PlayStation icons instead of Xbox
3. **XR-045:** Game crashes when user signs out during gameplay
4. **XR-067:** Smart Delivery not configured (Series X|S vs One builds)
5. **XR-078:** Achievement descriptions exceed character limits

#### Key Xbox-Specific Requirements

| ID | Requirement | Notes |
|----|------------|-------|
| XR-010 | Quick Resume support | Game must save/restore state seamlessly on suspend |
| XR-011 | Smart Delivery | Single purchase, optimized build per console generation |
| XR-015 | Xbox button guide | Xbox button opens guide overlay at all times |
| XR-020 | Xbox Live integration | Gamertag display, presence strings, rich presence |
| XR-030 | Accessibility | Xbox Accessibility Guidelines (XAG) compliance recommended |
| XR-040 | Game Pass compatibility | If on Game Pass: handle entitlement loss gracefully |

---

### Nintendo Switch — Lotcheck

#### Key Lotcheck Requirements

| ID | Requirement | Notes |
|----|------------|-------|
| NL-001 | Nintendo logo display | Display correctly per guidelines (not SIE or Xbox) |
| NL-010 | Handheld mode support | Touchscreen support optional, button controls required |
| NL-011 | Docked/handheld transition | Seamless transition, no crash, adjust resolution |
| NL-020 | Joy-Con support | Support detached, attached, and Pro Controller |
| NL-021 | HD Rumble | Implement where appropriate |
| NL-030 | Sleep mode handling | Save state on sleep, restore on wake |
| NL-040 | Performance | Minimum 720p handheld, 1080p docked, stable framerate |
| NL-050 | File size | Base game on cartridge, updates via eShop |
| NL-060 | Local multiplayer | If supported: handle Joy-Con sharing correctly |

---

### Steam — Steamworks Requirements

| Category | Requirement | Notes |
|----------|------------|-------|
| Store page | Minimum 5 screenshots (1920×1080), description, system requirements | |
| Controller | Full controller support for "Full Controller Support" tag | |
| Cloud saves | Steam Cloud integration recommended (not required) | |
| Achievements | Optional but strongly recommended (impact visibility) | |
| Steam Deck | Test and submit for Deck Verified status | Key differentiator |
| Review build | Submit 2 weeks before target release for Steamworks review | |
| DRM | Steamworks DRM optional, no third-party DRM required | |
| Overlay | Steam Overlay must function (F12 screenshots, chat) | |

#### Steam Deck Verified Checklist

| Requirement | Criteria |
|------------|---------|
| Input | Default controller config works, no keyboard required |
| Display | Correct at 1280×800, text readable at 7" |
| Seamlessness | No launcher windows, no first-party login required |
| System support | Runs on SteamOS 3.0 (Proton compatible if Windows) |

---

### Store Asset Specifications

| Platform | Icon | Screenshot | Banner/Hero | Video |
|----------|------|-----------|-------------|-------|
| PS5 | 512×512 PNG | 1920×1080 or 3840×2160 | 1920×1080 | MP4, ≤100MB |
| Xbox | 300×300 PNG | 1920×1080 | 1920×1080 (Hero), 584×800 (Poster) | MP4, ≤100MB |
| Switch | 256×256 PNG | 1280×720 | 1920×1080 | MP4 |
| Steam | Multiple sizes | 1920×1080 min (5+ required) | Header: 460×215, Capsule: 231×87 | MP4/WebM |
| App Store | 1024×1024 PNG | Device-specific (6.7", 6.1", etc.) | — | 30s preview |
| Google Play | 512×512 PNG | Min 320px, 16:9 recommended | Feature: 1024×500 | YouTube link |

---

### Submission Timeline

| Platform | Initial Review | Update Review | Expedited? |
|----------|---------------|--------------|------------|
| PlayStation | 5-10 business days | 3-5 days | Yes (at cost) |
| Xbox | 5-10 business days | 3-5 days | Yes (partner program) |
| Nintendo | 10-15 business days | 5-10 days | Limited |
| Steam | 2-5 business days | 1-2 days | No |
| App Store | 1-3 business days | 1-2 days | Yes (limited) |
| Google Play | Hours to 3 days | Hours to 1 day | No |

### Common Cross-Platform Rejection Prevention

1. **Test controller prompts per platform** — #1 rejection cause across all consoles
2. **Handle network disconnection gracefully everywhere** — show message, don't crash
3. **Implement proper suspend/resume** — test by pulling power/closing lid
4. **Include all required first-party logos** — in correct order, correct duration
5. **Test save corruption recovery** — corrupt a save file, verify graceful handling
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Scopes certification across specific platforms
- **ST-02 (Structured Sequential Instructions):** Platform-by-platform systematic checklist process
- **ST-03 (Explicit Output Specification):** Defines exact table format for requirements
- **DS-01 (Domain Terminology):** Uses platform-specific terms (TRC, XR, Lotcheck)
- **QA-02 (Validation and Verification):** CRITICAL step cross-references latest platform documentation

## Related Prompts

- [Gameplay Test Plan](testing_gameplay_test_plan.md) — Functional testing beyond platform requirements
- [Automated Game Testing](testing_automated_game_testing.md) — Automate certification regression tests
- [Frame Budget Analysis](../performance/performance_frame_budget_analysis.md) — Meet platform performance requirements

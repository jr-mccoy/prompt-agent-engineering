# Apple App Store Readiness Checklist

Checks to work through in Phase 3. Each is a **question about this app**, not a
statement of policy. Read the actual requirement from the App Review Guidelines via
[`policy_source_registry.md`](policy_source_registry.md) before grading.

> Apple renumbers guideline sections between revisions. **Never cite a section number
> from memory.** Open the guidelines, find the section, cite what you read.

---

## A. App Privacy labels (highest-yield section)

- [ ] For each data type observed in Phase 1, is it reflected in the App Privacy
      labels?
- [ ] Is each correctly categorized — *Used to Track You*, *Linked to You*, *Not
      Linked to You*?
- [ ] Are third-party SDK collections included? (The developer is responsible for
      SDK behavior, not just first-party code.)
- [ ] Are labels stale relative to SDKs added or removed this cycle?
- [ ] Do purpose strings in `Info.plist` match the declared purposes?

**Cannot be read from source.** Ask, or record as *Not Checked*.

## B. Tracking and ATT

- [ ] Does the app access IDFA, or combine signals to track across apps/websites
      owned by other companies?
- [ ] If so, is `AppTrackingTransparency` authorization requested **before** tracking?
- [ ] Is `NSUserTrackingUsageDescription` present and specific?
- [ ] Does the app degrade gracefully when authorization is denied?
- [ ] Is there any fingerprinting fallback when ATT is denied? (Treat this as a
      `BLOCKER` candidate if found — verify against the guidelines first.)
- [ ] Do App Privacy labels declare tracking consistently with ATT usage?

## C. Purpose strings and capabilities

For each `NS*UsageDescription` in `Info.plist`:

- [ ] Is there an actual call site using that capability?
- [ ] Does the string explain the *specific* user benefit, not a generic sentence?
- [ ] Are there capabilities used without a purpose string? (Runtime crash + rejection)
- [ ] Are there purpose strings for capabilities no longer used? (Reviewer questions)
- [ ] Do entitlements match declared functionality?

## D. Account and identity

- [ ] Does the app support account creation?
- [ ] If so, is there an **in-app** account-deletion path (not merely a support email)?
- [ ] If third-party sign-in is offered, are the equivalent-privacy sign-in
      requirements met? Read the current rule — this one has changed repeatedly.
- [ ] Is sign-in required only where genuinely necessary for functionality?
- [ ] Are working demo credentials supplied in App Review notes where sign-in gates
      functionality?

## E. Payments

- [ ] Are digital goods and services sold through In-App Purchase where required?
- [ ] Any external purchase links or steering, and if so does the app qualify under a
      current exception or entitlement? **Verify the current rule** — this area
      changes frequently and by jurisdiction.
- [ ] Subscription terms disclosed before purchase: price, period, renewal, how to
      cancel
- [ ] Restore-purchases path present
- [ ] Physical goods/services correctly *not* using IAP

## F. Content, functionality, completeness

- [ ] No placeholder content, lorem ipsum, or non-functional buttons
- [ ] Not a repackaged website with no native value
- [ ] No mention of other mobile platforms in copy or screenshots
- [ ] No beta/trial/demo framing in a public submission
- [ ] Age rating answers match actual content
- [ ] User-generated content, if present, has a reporting mechanism, blocking, and a
      moderation commitment

## G. Technical

- [ ] Builds against a current-enough SDK for submission
- [ ] No private API use
- [ ] No code downloaded and executed at runtime beyond what is permitted
- [ ] Export compliance answered correctly for the encryption actually used
- [ ] Handles permission denial and offline state without crashing
- [ ] Supports current required device sizes and orientations

## H. App Review notes (frequently the difference between pass and fail)

- [ ] Demo account credentials, valid and tested
- [ ] Instructions to reach features behind non-obvious flows
- [ ] Explanation for any capability whose purpose is not self-evident
- [ ] Hardware requirements noted where the reviewer cannot reproduce them
- [ ] Contact for reviewer questions

An otherwise-compliant app is routinely rejected because a reviewer could not reach
the functionality. Treat missing review notes as `IMPORTANT`, not cosmetic.

## I. Kids Category (only if applicable)

- [ ] Kids Category declaration accurate
- [ ] No third-party analytics or advertising beyond what is permitted
- [ ] No external links, purchases, or third-party content outside a parental gate
- [ ] Privacy policy addresses children's data

As with Play families, this materially changes the risk profile — flag it in the
header.

---

## Recording results

Every unchecked box becomes either a graded finding (with evidence + verified
requirement) or a *Not Checked* entry with a question.

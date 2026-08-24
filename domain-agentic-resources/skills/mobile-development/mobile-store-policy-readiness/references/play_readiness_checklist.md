# Google Play Readiness Checklist

Checks to work through in Phase 3. Each is phrased as a **question about this app**,
not as a statement of policy — read the requirement itself from
[`policy_source_registry.md`](policy_source_registry.md) before grading anything.

> Run [`android-play-policy-insights`](../../android-play-policy-insights/) first if
> the app is Android and you can. It performs the deep code-side pass with a scripted
> scanner. Use this checklist for the surfaces it does not cover, and to reconcile.

---

## A. Declaration reconciliation (highest-yield section)

For every data type the app touches, the Data Safety form must match observed
behavior. Mismatches are the most common avoidable rejection.

- [ ] For each data type observed in Phase 1, is it declared as **collected**?
- [ ] For each type transmitted to a third party (analytics, ads, crash, attribution),
      is it declared as **shared**?
- [ ] Are data types the app *no longer* touches still declared? (stale over-declaration)
- [ ] Does declared encryption-in-transit match observed network config?
- [ ] Does the declared data-deletion pathway exist in reality?
- [ ] Are SDK-collected types declared, even where first-party code never reads them?

**Cannot be read from source.** Ask the user for the current form, or record each as
*Not Checked* with the question.

## B. Permissions and restricted APIs

For each of the following present in the manifest, is there a first-party call site,
and is it justified by **core** functionality (not ads, analytics, or convenience)?

- [ ] Background location
- [ ] `MANAGE_EXTERNAL_STORAGE` (All Files Access) — could the Storage Access
      Framework or scoped storage serve instead?
- [ ] Broad media permissions — could the Photo Picker serve instead?
- [ ] `QUERY_ALL_PACKAGES` — could a targeted `<queries>` element serve instead?
- [ ] SMS / Call Log
- [ ] Contacts
- [ ] Microphone / audio recording
- [ ] Accessibility APIs — is the use an accessibility use?
- [ ] Exact alarms — is the use case one the policy permits?
- [ ] Foreground service types — declared, and matching actual use?

For each: is the permission first-party or merged in from a library? A merged-in
permission with no call site is `ADVISORY`, not a violation.

## C. Prominent disclosure and consent

- [ ] Where sensitive data is collected outside an obvious user-initiated action, is
      there an in-app disclosure **before** collection?
- [ ] Is the disclosure distinct from the privacy policy and from a generic OS
      permission prompt?
- [ ] Is consent affirmative rather than implied by continued use?
- [ ] Is data collection stopped if consent is declined?

## D. Account and identity

- [ ] Does the app support account creation?
- [ ] If so, is there an **in-app** account-deletion path?
- [ ] Is there a **web-reachable** deletion path that does not require the app?
- [ ] Does deletion cover associated data, not just the login record?
- [ ] Are working review credentials supplied where sign-in gates functionality?

## E. Monetization

- [ ] Are digital goods sold through Play Billing where required?
- [ ] Are subscription terms — price, period, renewal, cancellation — disclosed
      before purchase?
- [ ] Does the listing description match what is actually sold?
- [ ] Are free-trial terms disclosed?

See [`android-play-billing-upgrade`](../../android-play-billing-upgrade/) for the
library-side work.

## F. Ads

- [ ] Is the ads presence declaration accurate?
- [ ] Any full-screen or interstitial ads in positions policies restrict (app launch,
      unexpected interruption, unskippable beyond permitted duration)?
- [ ] Ads visually distinguishable from app UI?
- [ ] Ad content appropriate to the declared content rating?
- [ ] If the app targets children, are ad SDKs and ad content compliant with the
      families requirements?

## G. Technical requirements

- [ ] Target API level meets the current requirement for new submissions and updates
- [ ] App bundle (not APK) where required
- [ ] 64-bit support
- [ ] No debug builds, test endpoints, or hardcoded credentials shipping
- [ ] Deep links resolve; no broken or hijackable intent filters (see
      upstream `security/android-intent-security`)

## H. Store listing

- [ ] Description matches actual functionality; no unimplemented features claimed
- [ ] Screenshots from the current build, no fabricated UI
- [ ] No claims of affiliation the app does not have
- [ ] Content rating questionnaire answers match actual content
- [ ] Privacy policy URL resolves and is a privacy policy
- [ ] No policy-restricted keyword stuffing in title or short description

## I. Families / children (only if targeting under 13, or mixed audience)

- [ ] Target-audience declaration accurate
- [ ] Ad SDKs on the approved list for families
- [ ] No collection of personal data from children beyond what is permitted
- [ ] Neutral age screen where required

If this section applies, the audit's risk profile changes substantially — say so
explicitly in the report header.

---

## Recording results

Every unchecked box becomes either a graded finding (with evidence + verified
requirement) or a *Not Checked* entry with a question. Nothing silently disappears.

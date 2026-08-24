# Policy Source Registry

Canonical URLs to read policy requirements from. **This file deliberately contains no
policy text** — only pointers. Policy wording, section numbers, thresholds, and
deadlines change; a copied excerpt goes stale silently and becomes the exact
fabrication hazard this skill exists to prevent.

## How to use this file

1. Find the row matching the behavior you observed in the app.
2. **Open the URL and read the current requirement.**
3. Quote the requirement in your finding, with the URL and the date you read it.
4. If the page will not load or has moved, mark the finding `[UNVERIFIED]` and cap
   its severity at `IMPORTANT`. Do not substitute a remembered requirement, a
   third-party blog summary, or an LLM-generated paraphrase.

**Never invent a URL.** If a topic has no row here, navigate from the store's policy
index (first row of each table) rather than guessing a deep link.

---

## Google Play

Provenance: extracted from `policies.json` in Google's own
[`android-play-policy-insights`](../../android-play-policy-insights/) skill, upstream
commit `23d9eae` (skill `last-updated: 2026-07-13`). Authoritative at extraction
time; still requires reading at run time.

| Topic | Source |
|---|---|
| Policy Center (index — navigate from here if a link below is dead) | https://support.google.com/googleplay/android-developer |
| Data safety section | https://support.google.com/googleplay/android-developer/answer/10787469 |
| Data safety — declaring data use | https://developer.android.com/privacy-and-security/declare-data-use |
| User Data policy (incl. prominent disclosure) | https://support.google.com/googleplay/android-developer/answer/10144311 |
| Prominent disclosure & consent | https://support.google.com/googleplay/android-developer/answer/10144311 |
| Account deletion requirement | https://support.google.com/googleplay/android-developer/answer/13327111 |
| Login credentials / demo accounts for review | https://support.google.com/googleplay/android-developer/answer/15748846 |
| Restricted permissions (index) | https://support.google.com/googleplay/android-developer/answer/16558241 |
| SMS & Call Log permissions | https://support.google.com/googleplay/android-developer/answer/10208820 |
| Package (app) visibility — `QUERY_ALL_PACKAGES` | https://support.google.com/googleplay/android-developer/answer/10158779 |
| All Files Access (`MANAGE_EXTERNAL_STORAGE`) | https://support.google.com/googleplay/android-developer/answer/10467955 |
| All Files Access — implementation guidance | https://developer.android.com/training/data-storage/manage-all-files |
| Photo & video permissions | https://support.google.com/googleplay/android-developer/answer/16935362 |
| Photo picker — implementation guidance | https://developer.android.com/training/data-storage/shared/media |
| Location permissions (incl. background) | https://support.google.com/googleplay/android-developer/answer/9799150 |
| Contacts permissions | https://support.google.com/googleplay/android-developer/answer/16909972#contacts-permissions |
| Audio recording | https://support.google.com/googleplay/android-developer/answer/10144311 |
| Files & docs access | https://support.google.com/googleplay/android-developer/answer/10467955 |
| Accessibility API use | https://support.google.com/googleplay/android-developer/answer/16558241#accessibility |
| Exact alarms | https://support.google.com/googleplay/android-developer/answer/16558241#exact_alarm |
| Foreground services | https://support.google.com/googleplay/android-developer/answer/13392821 |
| Target API level requirements | https://support.google.com/googleplay/android-developer/answer/11926878 |

---

## Apple App Store

Provenance: long-stable Apple entry points. **Treat these as navigation roots, not
deep links.** Apple restructures guideline numbering between revisions — always read
the current section from the guidelines page rather than citing a number from memory.

| Topic | Source |
|---|---|
| App Review Guidelines (index — the authoritative document) | https://developer.apple.com/app-store/review/guidelines/ |
| App Privacy details ("nutrition labels") | https://developer.apple.com/app-store/app-privacy-details/ |
| App Tracking Transparency | https://developer.apple.com/documentation/apptrackingtransparency |
| Developer program agreements & policy index | https://developer.apple.com/support/terms/ |

For any Apple topic not listed — account deletion, IAP and external purchase rules,
age rating, sign-in requirements, export compliance — **navigate from the App Review
Guidelines index** and cite the section you actually read. Do not assume a section
number.

---

## Cross-platform

| Topic | Where to look |
|---|---|
| Privacy policy URL reachability | Fetch the URL the listing declares; confirm HTTP 200 and that it is a privacy policy |
| Third-party SDK data behavior | The SDK vendor's own privacy/data-use documentation. If undocumented → `ADVISORY` + a question for the vendor |
| Regional requirements (GDPR, CCPA, DMA, KOSA, etc.) | Out of scope for this skill. Route to `domain-legal/`. Do not opine. |

---

## Maintaining this file

Re-check quarterly alongside the vendored-skill re-sync
(see `../../ANDROID_SKILLS_UPSTREAM.md`):

- [ ] Every URL still resolves
- [ ] Play rows still match `policies.json` in the current upstream `android-play-policy-insights`
- [ ] New restricted permissions or declaration requirements have rows
- [ ] Still no policy text copied into this file

Record dead links as findings against this registry, not as `[UNVERIFIED]` app findings.

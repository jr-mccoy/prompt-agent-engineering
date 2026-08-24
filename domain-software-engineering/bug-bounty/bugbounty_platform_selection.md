---
title: "Bug Bounty Platform Selection & Track Choice"
category: bug-bounty/strategy
description: "Choose which crowdsourced-security platform(s) to join and whether to pursue the open-bounty track or the vetted pay-for-effort (PTaaS/contractor) track, based on eligibility, payment model, geography/KYC, and fit"
techniques:
  - ST-01
  - RT-02
  - DS-06
  - ED-01
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - strategy
  - platform-selection
  - ptaas
  - career
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_program_selection_roi.md
  - domain-software-engineering/bug-bounty/bugbounty_getting_started_orientation.md
  - domain-software-engineering/bug-bounty/bugbounty_payment_kyc_operations.md
---

# Bug Bounty Platform Selection & Track Choice

**Objective:** Decide which platform(s) to commit to and which earning track to pursue — open
bounty (pay-for-finding) vs. vetted PTaaS/contractor work (pay-for-effort) — by matching each
platform's eligibility, payment model, and access path to the user's real constraints and goals.

> **Distinction from `bugbounty_program_selection_roi.md`:** that prompt ranks *programs within a
> platform you are already on*. This prompt operates one level up — choosing the *platform(s)* and
> *track* themselves (e.g., HackerOne vs. Bugcrowd vs. Intigriti vs. YesWeHack vs. Synack; open
> bounty vs. PTaaS). Run this first, then `program_selection_roi` once you are on a platform.

## When to Use
- You are deciding where to invest your reputation-building time and don't want to spread thin.
- You want to know whether you qualify for, or should aim toward, contractor-style (PTaaS) work.
- Your geography, payout method, or business structure may constrain which platforms can actually pay you.

## Inputs / Context
Provide what you can (the prompt should ask for anything missing — never invent it):
- **Location & payout constraints:** country of residence, preferred payout method, whether sanctions/
  blacklisted-country rules or banking limits might block withdrawals.
- **Legal structure:** participating as an individual or through a company/entity (LLC, sole trader, etc.).
- **Vetting tolerance:** willingness to complete ID/background checks, technical assessments, interviews.
- **Goal & income need:** learning vs. supplemental income vs. moving toward contract/consulting income; how soon you need cash.
- **Skill profile:** strongest vuln classes and asset types (web, API, mobile, cloud).
- **Current access:** any invites, existing accounts, or reputation you already hold.
- **Live platform data you can see** (optional): current payout models, fees, KYC requirements — supply
  these from the platforms' own current pages; do not rely on the model's memory for figures.

## Instructions

1. **Authorization framing.** This prompt is about *where to work legitimately*, not about circumventing
   access. Only recommend platforms/tracks the user can lawfully join, and flag any that their geography,
   sanctions status, or employment NDA would exclude.

2. **Separate the two tracks explicitly** and explain the fork in the user's terms:
   - **Open-bounty track (pay-for-finding):** you are paid for valid, first-to-report findings. Lowest-
     friction entry, highest competition, lumpy income. Classic crowdsourced platforms.
   - **Vetted / PTaaS / contractor track (pay-for-effort):** selective communities and scoped engagements
     that may pay hourly mission time, retest/patch-verification, or fixed-scope testing in addition to (or
     instead of) per-finding bounties. More predictable, more like contracting, but gated by vetting
     (resume, technical assessment, ID/background checks, interview).
   - Make clear that most platforms support *both*, and that the realistic path is usually open-bounty
     first → reputation → invites/PTaaS.

3. **Score each candidate platform/track on the decision axes** (default; let the user reweight):
   - **Eligibility & access path** — open signup vs. invite/application/assessment; can the user actually get in now or only later?
   - **Geography & payout viability** — can the user be *paid* from their country with their method? (Treat this as a hard gate, not a soft factor — a platform that can't pay you scores zero regardless of payouts.)
   - **KYC / compliance burden** — ID verification, tax forms, background checks; weigh against the user's tolerance.
   - **Payment model fit** — pure bounty vs. bonuses vs. pay-for-effort/hourly vs. invoice/self-billing; match to the user's income-stability need.
   - **Entity support** — does the platform let the user bill as a company if that's their structure?
   - **Skill & asset fit** — does the platform's program mix match the user's strong classes?
   - **Reputation/liquidity** — breadth of active programs and opportunity flow (use only data the user supplies; don't quote stale stats).

4. **Apply the hard gates before ranking.** If geography/payout or eligibility fully blocks a platform,
   mark it **EXCLUDED** with the reason and remove it from the ranked recommendation rather than scoring it low.

5. **Recommend a concrete starting posture**, not a vague list:
   - One **primary platform** to build reputation on (best access + fit + payout viability).
   - Optionally one **secondary** to diversify program flow.
   - A **track recommendation** (stay bounty-first, or actively work toward a named PTaaS/vetted track) tied to the user's goal and vetting tolerance.
   - If contractor-style income is the real goal, note that bounty reputation is the *on-ramp* to PTaaS, and name the qualifying steps.

6. **CRITICAL — verify the recommendation is grounded and current:**
   - Confirm every platform-specific claim (payout model, fees, KYC, eligibility) is either supplied by the
     user or labeled **"VERIFY ON PLATFORM"** — do not assert figures or policies from memory.
   - Confirm geography/payout viability was treated as a hard gate, and that no EXCLUDED platform leaked into the ranked picks.
   - Confirm the track recommendation matches the user's stated income need and vetting tolerance.
   - Confirm you did not promise specific earnings.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT quote specific payout ranges, fees, founding dates, or researcher-count stats from memory — they go stale and vary; require the user to supply or verify current figures.
- ❌ Do NOT recommend a platform the user cannot be *paid* from (sanctions/blacklisted-country/banking blocks) just because its payouts look attractive.
- ❌ Do NOT treat the vetted/PTaaS track as something a beginner can skip into; it is gated by assessment and reputation.
- ❌ Do NOT advise gaming invite-only access or misrepresenting identity/geography to pass KYC.
- ❌ Do NOT imply any platform is reliable income.
- ✅ DO treat geography + payout viability as a hard gate that can exclude a platform outright.
- ✅ DO label any platform policy/figure not supplied by the user as VERIFY ON PLATFORM.
- ✅ DO tie the track choice (bounty vs. PTaaS) to the user's income-stability need and vetting tolerance.
- ✅ DO frame open-bounty reputation as the normal on-ramp to contractor-style work.

## Output Format
```
## Track Fork (read first)
- Open bounty (pay-for-finding): [1-2 lines, fit for this user]
- Vetted / PTaaS (pay-for-effort): [1-2 lines, fit for this user]
Recommended track: [bounty-first | work toward PTaaS] — why

## Hard Gates Applied
- [Platform]: EXCLUDED — [geography/payout/eligibility reason]   (if any)

## Platform Scorecard (candidates that pass the gates)
| Platform | Access path | Payout viability | KYC burden | Payment-model fit | Entity support | Skill fit | Notes |
(label anything not user-supplied as VERIFY ON PLATFORM)

## Recommended Starting Posture
- Primary platform: [name] — why
- Secondary (optional): [name] — why
- Track: [bounty-first | toward PTaaS] — and, if PTaaS is the goal, the qualifying steps

## What to verify before committing
- [Per-platform: the current policies/figures the user must confirm on the platform's own pages]
```

## Example Output
```
## Track Fork (read first)
- Open bounty (pay-for-finding): lowest-friction entry for your 6 hrs/week and web/API strengths;
  income will be lumpy.
- Vetted / PTaaS (pay-for-effort): better income stability and closer to the contracting you ultimately
  want, but gated by assessment + ID/background checks; not an immediate option.
Recommended track: bounty-first now, with PTaaS as a 6–12 month target once you have a track record.

## Hard Gates Applied
- [None excluded — confirm payout viability for your country on each platform's payout page before relying on this.]

## Platform Scorecard (candidates that pass the gates)
| Platform   | Access path        | Payout viability      | KYC burden | Payment-model fit        | Entity support | Skill fit | Notes |
|------------|--------------------|-----------------------|------------|--------------------------|----------------|-----------|-------|
| Platform A | Open signup        | VERIFY ON PLATFORM    | ID + tax form | Bounty + some pay-for-effort | VERIFY     | Strong (web/API) | Broad program flow |
| Platform B | Open signup        | VERIFY ON PLATFORM    | ID + tax form | Bounty + invoice/self-bill   | Yes (company) | Strong   | Clear entity/invoicing path |
| Platform C | Application/assess  | VERIFY ON PLATFORM    | Heavy (interview, background) | Hourly + bounty | VERIFY | Strong | PTaaS-style; target later |

## Recommended Starting Posture
- Primary platform: Platform B — open access, strong web/API fit, and a clean invoicing path that matches
  your plan to bill through your sole-trader entity later.
- Secondary (optional): Platform A — adds program flow once your primary feels low-yield.
- Track: bounty-first. Revisit Platform C's vetted track after ~2 quarters of valid reports; its qualifying
  steps are a technical assessment and an ID/background check.

## What to verify before committing
- Confirm on each platform's own payout page that your country + payout method are supported.
- Confirm current KYC, tax-form, and (for Platform B) company-billing requirements before signup.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — frames the task as a gated platform+track choice under real constraints.
- **RT-02 (Multi-Dimensional Analysis)** — scores platforms across eligibility, payout viability, KYC, model fit, entity support, and skill fit.
- **DS-06 (Prioritization Guidance)** — outputs a ranked starting posture with primary/secondary and a track call.
- **ED-01 (Iterative Scaffolding)** — teaches the bounty-vs-PTaaS fork before asking the user to choose.
- **DD-07 (Self-Audit Table)** — verification enforces hard gates, VERIFY-ON-PLATFORM labeling, and no earnings promises.

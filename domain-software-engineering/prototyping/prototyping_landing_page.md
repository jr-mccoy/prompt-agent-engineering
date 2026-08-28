---
title: "Landing Page with Email Capture — Six-Section Marketing Page MVP"
category: software-engineering/prototyping
description: "Spec a single-page marketing site: hero, problem, solution, optional social proof, CTA with local email capture, and footer — with design specs, explicit exclusions, and content-gap handling."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - landing-page
  - marketing
  - email-capture
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/prototyping/prototyping_event_registration.md
  - domain-software-engineering/prototyping/prototyping_personal_crm.md
  - domain-software-engineering/prototyping/prototyping_habit_tracker.md
---

# Landing Page with Email Capture

**Objective:** Produce a build-ready spec for a single, shareable marketing page — hero, problem, solution, optional social proof, a CTA with local email capture, and a footer — with concrete design specs, explicit exclusions, and a plan for sections where the user hasn't supplied content.

**When to use:**
- Launching a product, side project, or idea and needing a page today.
- Building a waitlist or validating interest before building the real thing.
- A clean, dependency-light page you can host or share immediately.

**When NOT to use:**
- A full multi-page site or app — this is one page.
- Pages requiring a real email backend / CRM integration at MVP (capture is local for the demo).
- Heavily interactive product demos — out of scope.

**Audience:** Individuals generating pages with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following (sections you skip are handled explicitly):

1. **Product/project name** and one-line value.
2. **Headline + subheadline + primary CTA text.**
3. **Problem statements** — 3–4 pain bullets.
4. **Three features** — title + 1–2 sentence description each.
5. **Social proof (optional)** — testimonials, logos, or a metric (or "skip").
6. **Design** — color palette (or "suggest"), and any brand notes.
7. **Email-capture scope** — confirm local-storage/console for MVP (no real backend).

---

## Constraints

### Must
- Build all six sections in order: Hero, Problem, Solution, Social Proof (optional), CTA, Footer.
- Use only content the user supplies; for skipped optional sections, omit them cleanly (don't fabricate testimonials/metrics).
- Make the email-capture form validate format, store locally (or log), and show a success message.
- Be mobile-responsive with subtle scroll-in animation; use no stock photos (generate simple graphics/icons).
- Stay dependency-light (single file or component; standard CDN only).

### Must Not
- Invent testimonials, customer logos, fake metrics, or claims the user didn't provide.
- Add the excluded elements: chat widgets, popups, video backgrounds, autoplaying anything.
- Imply a real backend/email service when capture is local for the MVP.
- Over-scope into multiple pages or a full app.

---

## Instructions

1. **Confirm scope.** Restate it as a one-page MVP with local email capture (flag if a real backend is needed).
2. **Specify the hero.** Headline + subheadline + prominent CTA; optional simple generated graphic.
3. **Specify the problem section.** Heading + the user's 3–4 pain bullets.
4. **Specify the solution section.** Heading + three feature blocks (icon, title, description) from the user's features.
5. **Specify social proof.** Only if content is provided; otherwise omit the section entirely (state this).
6. **Specify the CTA section.** Repeat CTA + email input with format validation; success message; local storage / console for MVP.
7. **Specify footer + design + technical + exclusions.** Copyright + placeholder links; color palette; clean modern style; mobile-responsive; scroll animations; single file/component; standard CDN only; the four explicit exclusions.
8. **Self-check before output.** Confirm: all required sections present and in order; no fabricated social proof; email form validates + stores locally + confirms; exclusions honored; mobile-responsive; no real-backend implication. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate testimonials, logos, or "Join 10,000+ users" metrics the user didn't give.
- Add chat widgets, popups, video backgrounds, or autoplay.
- Pretend local email capture is a real signup backend.
- Use stock photos or heavy graphics that slow the page.
- Expand into a multi-page site or app.

✅ **DO:**
- Use only supplied content; omit optional sections that lack content and say so.
- Validate the email format, store locally/log, and confirm to the user.
- Generate simple icons/abstract graphics instead of stock imagery.
- Keep it one mobile-responsive, dependency-light page.
- Flag clearly that real email capture needs a backend/integration later.

---

## Output Format

```
APP: Landing Page — [PRODUCT/PROJECT NAME]
SCOPE: [one-page MVP, local email capture / flag if backend needed]

1. HERO
- Headline / Subheadline / Primary CTA; optional generated graphic (no stock photos)

2. PROBLEM
- Heading; 3–4 pain bullets [user content]

3. SOLUTION
- Heading; 3 feature blocks (icon, title, 1–2 sentence description) [user content]

4. SOCIAL PROOF (optional)
- [testimonials/logos/metric IF PROVIDED, else: section omitted]

5. CTA
- Repeat CTA; email input (format-validated); success message; store local / console (MVP)

6. FOOTER
- Copyright; placeholder Privacy/Terms; [optional social links]

DESIGN / TECHNICAL
- Palette [...]; clean modern, whitespace; sans-serif; mobile-responsive; subtle scroll-in
- Single file/component; standard CDN only

EXCLUDE
- No chat widgets / popups / video backgrounds / autoplay

VERIFICATION NOTES
- [assumptions / omitted sections flagged]
```

---

## Example Output

```
APP: Landing Page — "FocusLane" (deep-work timer)
SCOPE: One-page MVP, email capture stored in local storage. NOTE: real waitlist needs a backend later.

1. HERO
- Headline: "Protect your deep work."
- Subheadline: "FocusLane blocks distractions and times your focus sprints so you finish what matters."
- CTA: "Join the Waitlist"
- Generated abstract graphic (calm gradient shape) — no stock photos

2. PROBLEM
- Heading: "The Problem"
- Bullets: "Your day gets eaten by pings." / "Context-switching kills momentum." / "Generic timers ignore how focus actually works." / "You end the day busy but not done."

3. SOLUTION
- Heading: "How FocusLane Helps"
- Block 1 — (Shield icon) "Distraction Blocking": Mutes notifications during a sprint.
- Block 2 — (Timer icon) "Adaptive Sprints": Suggests sprint lengths from your history.
- Block 3 — (BarChart icon) "Focus Insights": Shows when you actually do your best work.

4. SOCIAL PROOF
- Section omitted (no testimonials/metrics provided).

5. CTA
- Repeat "Join the Waitlist"
- Email input with format validation
- On submit: store email in local storage; show "Thanks! We'll be in touch."

6. FOOTER
- "© 2026 FocusLane"
- Placeholder links: Privacy · Terms
- (No social links provided → omit)

DESIGN / TECHNICAL
- Palette: deep indigo + warm off-white + one teal accent
- Clean, lots of whitespace; Inter font; mobile-responsive; fade-in on scroll
- Single HTML file with embedded CSS/JS; standard CDN only

EXCLUDE
- No chat widget, no popup, no video background, no autoplay

VERIFICATION NOTES
- Social-proof section omitted by design (no content). Add later when testimonials exist.
- Email capture is local for the demo; wire to a real list/backend before launch.
```

---

## Verification

- [ ] All required sections present and in order (Hero → Footer).
- [ ] Optional social-proof section included only if content was provided; otherwise omitted explicitly.
- [ ] Email form validates format, stores locally/logs, and shows a success message.
- [ ] No fabricated testimonials, logos, or metrics.
- [ ] The four exclusions (chat/popup/video bg/autoplay) are honored.
- [ ] Mobile-responsive, dependency-light, no stock photos.
- [ ] Local-capture-vs-real-backend distinction is flagged.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the deliverable to a single shareable page with email capture so scope stays one page.
- **ST-03 (Output Format Specification):** Locks the six-section + design + exclusions structure into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (no fabricated proof, honored exclusions, local-capture honesty) as explicit constraints.
- **DS-06 (Prioritization and Severity Guidance):** Orders sections by persuasion flow and treats social proof as conditional so the page leads with what matters.
- **QA-01 (Self-Verification):** A pre-output check confirms section order, no fabricated content, email-form behavior, and exclusions before emitting.

---

## Related Prompts

- `domain-software-engineering/prototyping/prototyping_event_registration.md` — Pair the page with a real signup flow.
- `domain-software-engineering/prototyping/prototyping_personal_crm.md` — Where captured leads/contacts could later live.
- `domain-software-engineering/prototyping/prototyping_habit_tracker.md` — Build the product the page promotes.

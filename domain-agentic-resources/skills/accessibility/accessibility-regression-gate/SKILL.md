---
name: accessibility-regression-gate
description: Sets up an accessibility regression gate in CI using an inventory of pages and UI states, axe scans run through the existing browser test runner, a committed baseline so the build fails only on new violations, a ratchet that shrinks the baseline, and a timed screen-reader smoke script per release. Use when asked to "add accessibility tests to CI", "stop accessibility regressions", "fail the build on a11y violations", or "run axe in Playwright".
metadata:
  tags:
    - a11y
    - accessibility
    - axe
    - ci
    - playwright
    - regression-testing
  updated: "2026-10-04"
---
# Accessibility Regression Gate

Adds a CI check that stops accessibility from getting worse, on a codebase that is not yet
clean. The gate fails on *new* detectable violations, tolerates a committed baseline of
known ones, and makes that baseline shrink over time. A short manual screen-reader script
covers what automation cannot see.

## Purpose

Two things usually go wrong when teams add axe to CI. Either the existing violations turn
the build red on day one, so the check is disabled within a week. Or the check scans only
the initial page load, so the modal, the error state and the open menu are never tested.
This skill handles both: baseline-and-ratchet for the first problem, a state inventory for
the second.

## When to Use This Skill

- Adding automated accessibility checks to a pull-request pipeline
- An existing axe check is flaky, ignored, or disabled because of pre-existing violations
- Accessibility regressions keep reappearing after an audit was remediated
- Defining the per-release manual accessibility check

## When NOT to Use This Skill

- **A conformance audit or VPAT/ACR evidence.** Automated rules detect only a subset of
  WCAG failures. Use `wcag-audit-patterns`; this gate makes no conformance claim.
- **A one-off audit and report of the current state.** The `/accessibility_audit` command
  (`domain-agentic-resources/commands/accessibility/accessibility_audit.md`) covers that.
- **Designing an overall accessibility test strategy.** The prompt
  `domain-software-engineering/testing/testing_accessibility_wcag.md` designs the strategy;
  this skill implements its CI-gate component.
- **Keyboard and focus behaviour of individual widgets.** Rule engines cannot check that
  arrows move focus. Use `component-accessibility-contracts`.
- **No browser test runner exists yet.** Set one up first with `e2e-testing-patterns`.

## Prerequisites

- A browser test runner already running in CI. Examples use Playwright Test with
  `@axe-core/playwright`. For Cypress, `cypress-axe` provides `cy.injectAxe()` and
  `cy.checkA11y()`, and the baseline logic below carries over. Verify package APIs
  against current docs before copying.
- A way to start the app (or a preview deployment) in CI with deterministic test data
- An owner for the baseline file (a CODEOWNERS entry or equivalent review rule)

## Workflow

### Step 1: Write down what the gate claims

Put this sentence in the test file header and the CI job description, so nobody reads a
green build as "accessible":

> This gate fails when a change introduces an automatically detectable accessibility
> violation in the listed pages and states. It does not establish WCAG conformance.

### Step 2: Build the state inventory

List page × state combinations, not just URLs. Prioritise the journeys users cannot
avoid: sign-in, primary task, checkout or submit, account settings.

| State key | URL | Setup to reach the state | Why it matters |
|---|---|---|---|
| `home.default` | `/` | none | entry point |
| `nav.menu-open` | `/` | open main menu | popups are often unlabelled |
| `signup.errors` | `/signup` | submit empty form | error messages and `aria-invalid` |
| `checkout.dialog` | `/cart` | open "remove item" dialog | modal naming and focus |
| `search.empty` | `/search?q=zzzz` | none | empty-state messaging |
| `home.mobile` | `/` | 375 px viewport | reflow, hidden-but-focusable items |
| `home.dark` | `/` | dark colour scheme | contrast regressions in themes |

Start with 10–20 states; scans take seconds each. Add a state when a bug is found in a
state not yet covered.

### Step 3: Choose the ruleset

- Gate on WCAG A and AA tags: `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, plus `wcag22aa`
  where the installed axe-core version supports it (verify against current docs).
- Run `best-practice` rules as report-only at first; promote individual rules to the gate
  once their baseline is empty.
- Treat `results.incomplete` ("needs review", for example contrast over images or
  gradients) as a manual-review list, never as a failure.
- Exclude a third-party region only with a ticket link and an expiry date in a comment.

### Step 4: Add the scan helper with a baseline

A violation is fingerprinted as `ruleId::target-selector`, keyed by state. The baseline is
a committed JSON file mapping state keys to known fingerprints.

```ts
// tests/a11y/gate.ts
import { expect, type Page } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs';
import path from 'node:path';

const TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const BASELINE_PATH = path.join(__dirname, 'a11y-baseline.json');
const RESULTS_DIR = path.join(__dirname, '..', '..', 'a11y-results');

const baseline: Record<string, string[]> = fs.existsSync(BASELINE_PATH)
  ? JSON.parse(fs.readFileSync(BASELINE_PATH, 'utf8'))
  : {};

export async function expectNoNewViolations(page: Page, stateKey: string) {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();

  const current = results.violations.flatMap(v =>
    v.nodes.map(n => `${v.id}::${n.target.flat().join(' >> ')}`)
  ).sort();

  fs.mkdirSync(RESULTS_DIR, { recursive: true });
  fs.writeFileSync(path.join(RESULTS_DIR, `${stateKey}.json`),
    JSON.stringify({ violations: current, incomplete: results.incomplete.map(i => i.id) }, null, 2));

  const known = new Set(baseline[stateKey] ?? []);
  const added = current.filter(f => !known.has(f));
  const fixed = [...known].filter(f => !current.includes(f));
  if (fixed.length) {
    console.log(`[a11y] ${stateKey}: ${fixed.length} baseline entries now pass; remove them:\n  ${fixed.join('\n  ')}`);
  }
  expect(added, `New accessibility violations in ${stateKey}`).toEqual([]);
}
```

```ts
// tests/a11y/states.spec.ts
import { test } from '@playwright/test';
import { expectNoNewViolations } from './gate';

test.describe('@a11y', () => {
  test('signup.errors', async ({ page }) => {
    await page.goto('/signup');
    await page.getByRole('button', { name: 'Create account' }).click();
    await page.getByRole('alert').first().waitFor();   // wait for the state, not for time
    await expectNoNewViolations(page, 'signup.errors');
  });
});
```

**Seeding the baseline:** run the suite once on the main branch, then build
`a11y-baseline.json` from the `a11y-results/*.json` files (state key → `violations`
array). Commit it in its own pull request, reviewed by the baseline owner, with a link to
the remediation backlog.

**If fingerprints churn between runs:** the target selectors contain generated ids or
`nth-child` indexes. Add stable `id`s or test attributes to the offending elements, or
normalise the selector in the helper (for example, strip a known generated-id pattern).
Do not loosen the fingerprint to rule id alone; that hides new instances of a known rule.

### Step 5: Wire it into CI

- Run as a separately named job (for example `accessibility-gate`) so a failure is
  identifiable at a glance, filtering with `npx playwright test --grep @a11y`.
- Upload `a11y-results/` as a build artifact on every run, including passing runs, so
  "fixed" entries are visible.
- Require the job on pull requests to the main branch once it has been stable for a week.

### Step 6: Enforce the ratchet

The baseline may only shrink without special approval:

1. Protect `a11y-baseline.json` with a CODEOWNERS (or equivalent) entry for the
   accessibility owner.
2. Pull requests that only *remove* baseline entries are approved routinely.
3. Pull requests that *add* entries need the owner's approval and a ticket link in the
   description.
4. Review the baseline monthly; report the count per state as a trend.

### Step 7: Add the manual screen-reader smoke script

Automation cannot judge whether announcements make sense. Before each release, run a
fixed, time-boxed script (15 minutes) with one reader/browser pair, rotating pairs
between releases (NVDA with Firefox or Chrome, VoiceOver with Safari, TalkBack with Chrome).

```markdown
## Release a11y smoke (reader: ____ / browser: ____ / build: ____)
| # | Journey step | Expected announcement or behaviour | Pass/Fail | Note |
|---|---|---|---|---|
| 1 | Load home; list headings | One h1; headings describe sections | | |
| 2 | Open main menu with keyboard | "Menu, expanded" (or equivalent); items reachable | | |
| 3 | Submit empty sign-up form | Errors announced; focus moves to first error or summary | | |
| 4 | Open and dismiss remove-item dialog | Dialog name read on open; focus returns on close | | |
| 5 | Complete primary task | Success message announced without moving focus away | | |
```

A failure is logged as a defect and, if it is automatable, a new state or contract test.
For reader-specific commands see `screen-reader-testing`.

## Verification

Prove the gate works before relying on it:

- [ ] On a throwaway branch, remove an `alt` attribute or a form label in a scanned state;
      the gate turns red and names the rule and selector
- [ ] A pull request that only fixes a baseline entry passes and prints it under "now pass"
- [ ] Two consecutive runs on an unchanged commit produce identical fingerprints
- [ ] The CI job's description states the "does not establish conformance" sentence
- [ ] The release checklist links the smoke script

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Gate fails intermittently on the same commit | Scan runs before the state settles (animations, lazy content) | Wait for a specific element or role; emulate reduced motion; never use fixed sleeps |
| Fingerprints differ every run | Generated ids or positional selectors | Stabilise ids, or normalise selectors in the helper |
| Baseline grows every sprint | Entries added without review | Enforce Step 6; report baseline size in sprint review |
| Gate is green but users report problems | Only initial page loads scanned, or the problem is behavioural | Add the missing state; add a component contract test for behaviour |
| Contrast failures flip-flop | Text over images or gradients reported inconsistently | These belong in `incomplete`; review manually |
| Content inside a cross-origin iframe is never checked | The scanner cannot reach cross-origin frames | Scan the embedded app in its own suite, or list it for manual review |

## Safety & Constraints

**NEVER:**
- Disable the gate to merge a red build; add a baseline entry through the owner instead,
  so the debt stays recorded
- Present a passing gate as WCAG conformance in contracts, procurement answers or ACRs
- Commit a baseline regenerated wholesale on a feature branch; regenerate only on main,
  in a dedicated reviewed change

**ALWAYS:**
- Keep exclusions explicit, ticketed and dated
- Keep the manual smoke script in the release checklist even when automation is green

## Related Skills

- `component-accessibility-contracts`: behaviour tests for keyboard, focus and state that
  rule engines cannot check
- `wcag-audit-patterns`: full WCAG 2.2 audit; use its findings to seed the state inventory
- `screen-reader-testing`: reader commands and deeper scenarios behind the smoke script
- `e2e-testing-patterns` (developer-tools): Playwright and Cypress setup this gate runs on
- `github-actions-templates` / `gitlab-ci-patterns` (cicd-automation): pipeline wiring

# Finding Grading Rubric

Every finding is graded on two independent axes. Grade them separately — conflating
"this is serious" with "I am sure about this" is what produces confident wrong output.

## Axis 1 — Severity

| Grade | Definition | Test |
|---|---|---|
| `BLOCKER` | Would plausibly cause rejection or removal if submitted as-is | Can you name the specific requirement it violates, from a page you read? |
| `IMPORTANT` | Real policy risk; likely to draw reviewer questions or a declaration mismatch | Would a reviewer reasonably ask about this? |
| `ADVISORY` | Hygiene, future-proofing, or a question to resolve | Nothing breaks today |

## Axis 2 — Confidence

| Grade | Definition | Requires |
|---|---|---|
| `CONFIRMED` | Both legs present | Cited `file:line` or named store surface **AND** policy requirement read from an official URL this session |
| `PROBABLE` | One leg missing | Usually: strong code evidence, but the store-side declaration is unknown |
| `UNVERIFIED` | Could not check | Does **not** belong in Findings — move to *Not Checked* |

## The hard gate

```
BLOCKER  requires  CONFIRMED.
```

If either leg is missing, the finding is **at most** `IMPORTANT`. This is absolute.

| Evidence | Policy verified | Max severity |
|---|---|---|
| `file:line` cited | Yes, URL read | `BLOCKER` |
| `file:line` cited | No / `[UNVERIFIED]` | `IMPORTANT` |
| Behavior inferred, no location | Yes, URL read | `IMPORTANT` |
| Behavior inferred, no location | No | `ADVISORY` or *Not Checked* |
| Absence of something unobservable | — | *Not Checked* (never a finding) |

## Downgrade triggers

Apply mechanically. Each drops severity one level:

- Logic sits behind an interface, repository, or DI boundary
- Evidence is from a build variant or flavor that may not ship
- Behavior comes from a third-party SDK whose data use is undocumented
- The permission appears only in a merged manifest, with no first-party call site
- An innocent explanation exists that you could not exclude

Downgrades stack. Two triggers on a `BLOCKER` make it `ADVISORY`.

**Nothing upgrades severity.** There is no "this looks really bad" escalation.

## Finding format

```markdown
### [BLOCKER · CONFIRMED] Background location accessed without a declared foreground use

**Observed:** `app/src/main/java/com/example/LocationSync.kt:88` requests
`ACCESS_BACKGROUND_LOCATION` and starts a periodic worker.

**Requirement:** "<quoted text from the policy page>"
Source: https://support.google.com/googleplay/android-developer/answer/9799150
(read 2026-08-02)

**Why this is graded CONFIRMED:** call site cited; requirement read this session.

**Alternative explanations considered:** Checked whether the worker is gated to a
user-enabled feature — `LocationSync.kt:71` starts it unconditionally in
`onCreate`, so no.

**Remediation:** Either gate behind an explicit opt-in with prominent disclosure,
or move to foreground-only location.
```

Mandatory fields: **Observed** (with location), **Requirement** (with URL + read
date), **Alternative explanations considered**, **Remediation**.

If you cannot fill *Alternative explanations considered* with something real, you
have not done Phase 4 — go back.

## Not Checked entries

```markdown
- **Data Safety declaration for `PRECISE_LOCATION`** — cannot read Play Console.
  *Question:* Does the current Data Safety form declare precise location as
  collected and shared? If not, this becomes a BLOCKER.
```

Every entry names the question that would resolve it. *Not Checked* being empty is
almost always a mistake — you cannot read either store's console.

## Calibration

For a typical mid-size app in decent shape, expect roughly:

- `BLOCKER`: 0–2
- `IMPORTANT`: 2–6
- `ADVISORY`: 3–10
- *Not Checked*: 5–15

A run producing ten `BLOCKER`s means the gate was not applied. Re-run Phase 4 before
reporting. Conversely, zero findings with an empty *Not Checked* means the audit did
not actually run — you cannot verify console state from source.

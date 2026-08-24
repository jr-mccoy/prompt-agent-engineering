# Report Template

Emit exactly this structure. Omit no section — an empty section is reported as empty,
never padded and never silently dropped.

---

```markdown
# Store Policy Readiness Report — {{app_name}}

**Stores audited:** {{Google Play | Apple App Store | both}}
**Mode:** {{VERIFIED | DEGRADED}}   **Date:** {{YYYY-MM-DD}}
**Source scope:** {{what was read; note any missing platform or submodule}}
**Special profile:** {{Families/Kids Category if applicable, else "standard"}}

## Summary

| Severity | Confirmed | Probable | Total |
|---|---|---|---|
| BLOCKER | {{n}} | — | {{n}} |
| IMPORTANT | {{n}} | {{n}} | {{n}} |
| ADVISORY | {{n}} | {{n}} | {{n}} |

**Not Checked:** {{n}} items requiring information unavailable from source.

{{One-paragraph plain assessment. If there are no blockers, say so directly.
Do not manufacture concern.}}

---

## Findings

{{Ordered BLOCKER → IMPORTANT → ADVISORY. Each in the format from
finding_grading_rubric.md, with Observed / Requirement (+ URL and read date) /
Alternative explanations considered / Remediation.}}

{{If none: "No findings met the evidentiary bar for reporting." Then say what was
checked, so the reader can distinguish a clean audit from a shallow one.}}

---

## Not Checked

Items that could not be verified from the source tree. Each names the question that
would resolve it.

{{- **<item>** — <why unavailable>. *Question:* <question>. <consequence if
adverse>}}

{{This section is essentially never legitimately empty: neither store's console is
readable from source.}}

---

## Remediation Checklist

Ordered by severity, then by effort within a severity band.

- [ ] {{action}} — {{finding ref}}
- [ ] {{action}} — {{finding ref}}

---

## Sources Consulted

| Requirement area | URL | Read |
|---|---|---|
| {{area}} | {{url}} | {{date}} |

{{In DEGRADED mode, state instead: "No policy sources were verified. All
requirements in this report are marked [UNVERIFIED] and must be confirmed against
official sources before action."}}

---

> **Disclaimer.** This is an automated engineering readiness assessment for
> informational purposes only. It is **not legal advice**, **not a guarantee of store
> approval**, and **not a complete compliance check**. Google Play and Apple App
> Review have final authority, and undiscovered issues may remain. Verify every
> requirement against the official policy source before acting. The developer retains
> sole responsibility for the app's compliance and submission.
```

---

## Rules for filling this in

1. **Never pad.** Empty arrays and empty sections are reported as empty. No `N/A`
   rows, no placeholder findings, no "no issues found, but consider…" filler.
2. **Counts must match.** The summary table is derived from the findings list.
3. **Every BLOCKER appears in Sources Consulted.** If a requirement is not in that
   table, no finding citing it can be `CONFIRMED` — which means it cannot be a
   `BLOCKER`.
4. **State the mode in the header.** A `DEGRADED` report that reads like a `VERIFIED`
   one is the most dangerous output this skill can produce.
5. **Plain assessment, honestly calibrated.** If the app looks ready, say it looks
   ready. Manufacturing concern to justify the audit is the failure mode that makes
   these tools ignored.

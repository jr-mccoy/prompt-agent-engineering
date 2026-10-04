---
name: changelog_reconcile
description: Pre-tag check that a changelog section (for example `[Unreleased]` or a version heading) matches the commits actually in the release range. Lists user-visible commits with no entry (MISSING), entries with no matching commit in the range (PHANTOM), entries filed under the wrong Keep a Changelog heading (MISCLASSIFIED), breaking changes not called out (BREAKING-UNFLAGGED), and duplicates — then drafts entries for the gaps, marked as drafts. Read-only; never edits the changelog or tags unless explicitly asked. Distinct from the changelog-automation skill (sets up generation tooling and commit conventions) and the release-notes writer prompt (writes user-facing and internal notes).
version: "1.0.0"
category: documentation
tags: [documentation, changelog, release, git, conventional-commits, keep-a-changelog, verification]
agents_used: []
---

# Changelog Reconcile

Check a hand-written or generated changelog section against the real commit
range before you tag a release. You reconcile in both directions — commits
without entries and entries without commits — and you show the evidence for
every mismatch.

[Extended thinking: Changelogs fail quietly. A fix lands without an entry, an
entry describes a change that was reverted or never merged, a removal is filed
under "Changed" with no warning, or a breaking change hides in a commit footer.
Generating a changelog from scratch is a solved tooling problem; checking the
one you are about to publish against what actually shipped is the step teams
skip. This command does that check and drafts only what is missing.]

## Requirements
$ARGUMENTS

Expected: the changelog file (default `CHANGELOG.md`), the section to check
(default `[Unreleased]`), and the commit range (for example
`v1.4.0..HEAD`, or previous tag to release branch). If the range is not given,
propose `<latest tag>..HEAD` from `git describe --tags --abbrev=0` and ask the
user to confirm before continuing.

## When NOT to use

- Setting up automated changelog generation, commit conventions, or release
  tooling → `skills/developer-tools/changelog-automation/`
- Writing user-facing release notes and internal enablement notes →
  `domain-product-management/prompts/product_release_notes_writer.md`
- Deciding whether the release is ready to ship → `release-readiness-gatekeeper`
  (`agents/deployment/release_readiness_gatekeeper.md`)
- Checking prose docs against code → `/docs_drift_check`
  (`commands/documentation/docs_drift_check.md`)

## Configuration

- `--include-internal`: treat refactor/test/ci/chore commits as changelog-worthy
  (default: excluded, but listed in an appendix)
- `--no-drafts`: report mismatches only; skip drafting entries

## Instructions

### Phase 1 — Collect the range
```bash
git log --no-merges --format='%h%x09%s' <range>
git log --merges --format='%h%x09%s' <range>      # PR numbers on merge-commit workflows
git log --no-merges --format='%h%n%B%n--END--' <range>   # bodies, for BREAKING CHANGE footers
```
Note whether the project squash-merges (PR numbers in subjects) or uses merge
commits, and whether it follows Conventional Commits. Do not assume either.

### Phase 2 — Classify commits
For each commit: user-visible or internal; proposed heading (Added, Changed,
Deprecated, Removed, Fixed, Security); breaking or not. With Conventional
Commits, a `!` after the type/scope or a `BREAKING CHANGE:` footer marks a
breaking change; without them, look for removed public symbols, flags, routes,
or config keys in the diff (`git show --stat <sha>`). Reverted pairs within the
range cancel out — list them, do not expect an entry.

### Phase 3 — Parse the changelog section
Extract each entry with its heading and any PR/issue references.

### Phase 4 — Match and classify mismatches
Match entries to commits by PR/issue number first, then by subject keywords.
Mark low-confidence matches as `[uncertain]` rather than forcing them.

| Status | Meaning |
|--------|---------|
| MATCHED | Entry and commit(s) agree |
| MISSING | User-visible commit, no entry |
| PHANTOM | Entry with no commit in range (wrong range, unmerged, or from a prior release) |
| MISCLASSIFIED | Entry under the wrong heading (e.g., a removal under Changed) |
| BREAKING-UNFLAGGED | Breaking change not marked as such in the entry |
| DUPLICATE | Same change listed twice |

### Phase 5 — Draft (unless `--no-drafts`)
For MISSING and BREAKING-UNFLAGGED items, draft entries written as user impact
("You can now…", "`--foo` was removed; use `--bar`"), not as commit subjects.
Prefix each with `DRAFT:` and cite the commit. Never fold drafts into the file
without explicit approval.

## Output

```markdown
# Changelog Reconcile: <section> vs <range>
Commits in range: <n> (user-visible <n>, internal <n>, reverted pairs <n>)
Entries in section: <n>

## Verdict: CONSISTENT | GAPS FOUND
MATCHED <n> · MISSING <n> · PHANTOM <n> · MISCLASSIFIED <n> · BREAKING-UNFLAGGED <n> · DUPLICATE <n>

## Mismatches
| Status | Entry / commit | Evidence | Fix |
|--------|----------------|----------|-----|

## Draft entries
### Fixed
- DRAFT: <user-facing sentence> (<sha>, #<PR>)

## Appendix: internal commits excluded
- <sha> <subject>
```

## Success Criteria

- Reconciliation closes: every user-visible commit is MATCHED or MISSING; every entry is MATCHED, PHANTOM, or DUPLICATE
- Every breaking-change signal in the range is accounted for
- Drafts are labelled and cite their commits
- No files changed and no tags created

## Constraints

- NEVER edit the changelog, create tags, or push in this command unless the user explicitly asks after seeing the report
- NEVER invent PR numbers, issue links, or version numbers
- NEVER treat commit subjects as finished changelog prose

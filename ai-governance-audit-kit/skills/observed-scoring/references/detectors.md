# Detectors: what is observable, and what is not

Every detector below is pure regex or a filesystem fact. The column that
matters is the last one: what the detector deliberately does **not** claim.

## Category 1 — Metadata (11 observable of 20)

| Check | Points | Detects | Does not claim |
|---|---|---|---|
| `name_length` | 1 | 1–64 characters | that the name is meaningful |
| `name_lowercase` | 1 | no uppercase | — |
| `name_charset` | 1 | alphanumeric and single hyphens | — |
| `name_no_edge_hyphens` | 1 | no leading, trailing or doubled hyphen | — |
| `name_matches_directory` | 1 | equals the bundle directory | — |
| `description_length_band` | 2 | 50–500 characters | that the description is good |
| `description_third_person` | 2 | no first- or second-person pronoun | correct voice throughout |
| `description_states_trigger` | 2 | a trigger phrase is present | that the trigger is the right one |

The rubric's "describes WHAT" and "describes WHEN" are judgements. The length
band and the trigger phrase are **proxies** for them, worth 4 of the rubric's
6 points for those two criteria, and they are reported as what they are.

## Category 2 — Structure (14 observable of 20)

| Check | Points | Detects |
|---|---|---|
| `under_500_lines` | 2 | SKILL.md line count |
| `long_content_pushed_to_references` | 2 | under 300 lines, or a populated `references/` |
| `explicit_bundled_references` | 2 | at least one backticked path to a bundled file |
| `when_to_use_section` | 1 | a "When to Use" heading |
| `when_not_to_use_section` | 1 | a "When NOT to Use" heading |
| `related_section` | 2 | a "Related" heading |
| `skill_md_at_root` | 2 | SKILL.md at the bundle root |
| `no_nested_skill` | 1 | no second SKILL.md below it |
| `resource_dirs_named_conventionally` | 1 | every subdirectory is a known component dir |

"Logical section ordering", worth 2 rubric points, is not detected. Section
order carries meaning a regex cannot read.

## Category 3 — Content (7 observable of 25)

| Check | Points | Detects |
|---|---|---|
| `numbered_instruction_steps` | 3 | three or more numbered steps |
| `verification_section` | 2 | a Verification or Validation heading |
| `worked_example_present` | 2 | a fenced or indented example |

This is the category where the honest denominator matters most. Actionability,
completeness and accuracy are 25 rubric points and 7 observable ones. **A low
`cat3_content` score is not evidence that the content is bad.** It is evidence
that the three observable structures are missing.

## Category 4 — Resources (9 observable of 15)

| Check | Points | Detects |
|---|---|---|
| `referenced_files_resolve` | 3 | every backticked component path exists |
| `scripts_have_docstrings` | 2 | each `.py` opens with a module docstring |
| `scripts_validate_input` | 1 | each `.py` uses `argparse` or reads `sys.argv` |
| `references_are_markdown` | 1 | nothing non-markdown under `references/` |
| `no_oversized_bundled_file` | 2 | no bundled file over 1 MiB |

## Category 5 — Safety (13 observable of 20)

| Check | Points | Blocking | Detects |
|---|---|---|---|
| `no_hardcoded_secret` | 3 | yes | a credential-shaped assignment, an AWS key ID, a PEM private-key header |
| `no_absolute_user_path` | 2 | yes | `/Users/x/`, `/home/x/`, `C:\Users\x\` |
| `no_personal_contact` | 2 | yes | an email address, or a phone number in dialable shape |
| `env_vars_for_sensitive_values` | 3 | no | a credential-shaped name read from the environment |
| `safety_section` | 2 | no | a Safety, Warnings or Cautions heading |
| `failure_handling_section` | 1 | no | Troubleshooting, Failure, Recovery or Errors |

### The three blocking checks cap the verdict

They are the rubric's own "Must Pass (Blocking)" security items. A failure caps
the verdict at `blocked` regardless of the total, exactly as
`agentic-system-factory/scripts/score_rubric.py` caps a tier regardless of the
total when `cat3_security` falls below its load-bearing minimum.

### Security detectors run on the whole bundle, unstripped

A credential inside a code fence is still a credential in the file, and a
bundled script is the likelier place for one than the prose. Prose detectors
are the opposite: they run with fences and inline code removed, so a documented
example never scores as the real thing.

### The narrow phone pattern, and the false positive it prevents

An earlier draft matched `\+?\d[\d ()-]{8,}\d`, which reported
`updated: "2026-06-18"` as leaked contact detail — an ISO date is ten
characters of digits and hyphens. A detector that flags every `updated:` line
trains its reader to ignore the category, which is worse than not running. The
shipped pattern requires a dialable shape and rejects an ISO date outright, and
`test_an_iso_date_is_not_reported_as_a_contact_detail` pins it.

## The self-reported block

If the artifact carries a `<!-- RUBRIC -->` block, it is parsed and reported
under `self_reported`, **beside** the observed scores and never merged into
them. The gap between the two is one of the more useful findings an audit
produces, and merging would destroy it.

## Why no tier

Only 54 of 100 points are mechanically observable. A tier derived from the
observable subset would be a rubric score that nobody computed, which is what
`pae_registry/governance.py` refuses when it declines to infer one from
document structure. `tier` is `null`, `tier_basis` says why, and Gate A rejects
any score record that fills it in.

Note also `meta/adr/0041-author-reviewer-separation.md`: author is not
reviewer. That applies directly to who adjudicates these findings on a client's
corpus, and the engagement should say so out loud.

# Third-Party Notices

This repository contains original work by the repository owner **plus** third-party
material that is vendored, adapted, or derived from other projects. Those components
retain their own licenses. The root [`LICENSE`](LICENSE) governs the repository's
original content only; it does not relicense anything listed below.

This file records what was verified at the time of the public release. Where a claim
could not be verified, it says so explicitly rather than asserting a license.

---

## 1. Google — `android/skills`

| | |
|---|---|
| **Component** | Eight Android skills under `domain-agentic-resources/skills/mobile-development/` |
| **Upstream** | [github.com/android/skills](https://github.com/android/skills) |
| **License** | Apache License 2.0 |
| **License text** | [`domain-agentic-resources/skills/mobile-development/ANDROID_SKILLS_LICENSE.txt`](domain-agentic-resources/skills/mobile-development/ANDROID_SKILLS_LICENSE.txt) |
| **Relationship** | **Vendored verbatim**, with two documented local modifications |
| **Provenance detail** | [`domain-agentic-resources/skills/mobile-development/ANDROID_SKILLS_UPSTREAM.md`](domain-agentic-resources/skills/mobile-development/ANDROID_SKILLS_UPSTREAM.md) |
| **Pinned commit** | `23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4` (2026-07-29) |

Vendored skills: `android-agp-9-upgrade`, `android-edge-to-edge`,
`android-migrate-xml-to-compose`, `android-navigation-3`,
`android-play-billing-upgrade`, `android-play-policy-insights`, `android-r8-analyzer`,
`android-xr-jetpack-compose-glimmer`.

Each skill body and its `references/` tree are byte-identical to upstream. The only
local changes are (1) a `name:` prefix matching the local directory name, (2)
provenance keys injected under `metadata:` (`author: Google LLC`, `upstream`,
`upstream-path`, `upstream-commit`, `upstream-synced`), and (3) an appended
`local-wrapper.md` block below a marker, kept outside the upstream body. The
upstream `metadata.author` and `last-updated` fields are preserved.

> **Note on the license pointer.** These eight `SKILL.md` files carry
> `license: Complete terms in LICENSE.txt` in their frontmatter, inherited verbatim
> from upstream. The Apache-2.0 text for them is shipped once, one directory up, at
> `ANDROID_SKILLS_LICENSE.txt`, and is mapped to each skill by
> `ANDROID_SKILLS_UPSTREAM.md`. The files are not hand-edited to repoint that line,
> because their bodies are kept byte-identical to upstream by the re-sync procedure.

## 2. Anthropic — `anthropics/skills` (skill-creator)

| | |
|---|---|
| **Component** | `domain-agentic-resources/skills/developer-tools/skill-creator/` |
| **Upstream** | [github.com/anthropics/skills](https://github.com/anthropics/skills) (`skills/skill-creator`) |
| **License** | Apache License 2.0 |
| **License text** | [`domain-agentic-resources/skills/developer-tools/skill-creator/LICENSE.txt`](domain-agentic-resources/skills/developer-tools/skill-creator/LICENSE.txt) |
| **Relationship** | **Vendored**, with local `metadata:` additions |

The bundled `LICENSE.txt` is the Apache-2.0 text as published upstream, including its
unfilled `Copyright [yyyy] [name of copyright owner]` appendix line. Upstream ships the
same unfilled template; it has not been altered here. Copyright in this component is
held by Anthropic, not by this repository's owner.

## 3. `wshobson/agents`

| | |
|---|---|
| **Component** | A substantial portion of `domain-agentic-resources/agents/`, `skills/`, and `commands/` |
| **Upstream** | [github.com/wshobson/agents](https://github.com/wshobson/agents) |
| **License** | MIT (verified against the upstream repository) |
| **Relationship** | **Adapted** — imported, reorganized into this repository's category layout, renamed to its naming conventions, and in many cases restructured or extended |

The original import comprised 158 agents, 107 skills, and 71 commands. Those resources
have since been renamed, recategorized, merged, extended, and in part replaced, so the
present tree is not a verbatim copy and no per-file provenance map is maintained.

## 4. `daymade/claude-code-skills`

| | |
|---|---|
| **Component** | Approximately 25 skills under `domain-agentic-resources/skills/` |
| **Upstream** | [github.com/daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) |
| **License** | MIT (verified against the upstream repository) |
| **Relationship** | **Adapted** — imported and reorganized as above |

Skills whose names still match upstream include: `cli-demo-generator`,
`cloudflare-troubleshooting`, `github-ops`, `llm-icon-finder`, `promptfoo-evaluation`,
`prompt-optimizer`, `qa-expert`, `repomix-safe-mixer`, `repomix-unmixer`,
`teams-channel-post-writer`, `transcript-fixer`, `ui-designer`, `video-comparer`,
`youtube-downloader`. Some carry upstream-authored `references/` and `scripts/`.

## 5. Repository-owned components with their own LICENSE file

| Component | License | Note |
|---|---|---|
| [`continuity-kit/`](continuity-kit/) | MIT ([`continuity-kit/LICENSE`](continuity-kit/LICENSE)) | Original work of this repository's owner; carries its own license file because it is designed to be extracted as a standalone package. |

## 6. Reference material quoted from vendor documentation

Several skills bundle offline mirrors of vendor documentation so they work without
network access — most substantially the `references/android/…` trees inside the
vendored Google skills, which mirror pages from `developer.android.com`. That material
is covered by section 1 above. Other skills quote or summarize vendor documentation
(Google Play, Apple App Store, Stripe, Firebase, Kubernetes, and similar) inline;
those quotations are attributed in place and remain the property of their respective
owners.

---

## Scope and limitations of this notice

- Licenses in sections 1–4 were verified against the upstream repositories at the time
  of the public release. Upstream licenses can change; this file is a point-in-time record.
- Sections 3 and 4 describe **adapted** material. Because the imported resources were
  reorganized and edited over time, this repository does not maintain a file-by-file
  attribution map back to those upstreams. Both upstreams are MIT-licensed, which
  permits this use provided the copyright and permission notice is preserved — which is
  the purpose of this file.
- If you are the author of material you believe is used here without correct
  attribution or licensing, please open an issue or use the private reporting route in
  [`SECURITY.md`](SECURITY.md), and it will be corrected.

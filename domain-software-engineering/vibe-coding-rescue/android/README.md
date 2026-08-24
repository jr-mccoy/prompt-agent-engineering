# Android Vibe-Coding Rescue

A six-prompt workflow for rescuing AI-generated ("vibe-coded") Android apps. Fuses the general vibe-coding rescue methodology (see `../`) with Android-specific failure modes (manifest drift, lifecycle scope leaks, Compose state sprawl, Hilt scope confusion, WebView misconfiguration, hand-rolled auth, `exported` flag gaps, deeplink validation, Gradle / version-catalog hygiene, deprecated-API patchwork).

These prompts are written to be **portable across coding agents** — Claude Code, Codex, Cursor, Windsurf — and to chain: the output of one is the input of the next.

## When to Use This Cluster

- An Android app built largely with AI assistance has reached a "works but fragile / sprawling" state.
- Security or privacy concerns you can't yet articulate (exported components, deeplinks, WebView, token storage, permissions).
- Builds intermittently break across AGP / Gradle / Compose Compiler / Hilt upgrades.
- The AI keeps adding overlapping ViewModels, repositories, Hilt modules, or screens.
- Lifecycle bugs (rotation loses state, process death surprises) are landing repeatedly.
- The app is going to the Play Store, is in the Play Store, or is being handed to a new engineer.

## Prompts (in workflow order)

| # | Prompt | Purpose |
|---|--------|---------|
| 1 | [`android_viberescue_wall_diagnosis.md`](android_viberescue_wall_diagnosis.md) | Classify the app's failure mode into a 12-mode Android-specific taxonomy (A1–A12). Output a single primary mode + cascade check + one rescue action + next prompt. |
| 2 | [`android_viberescue_codebase_audit.md`](android_viberescue_codebase_audit.md) | Systematic audit across 10 fragility categories (duplication, deprecated APIs, lifecycle, coroutine scope, Compose, null safety, Hilt, Gradle, error handling, tests). Severity-tiered findings with file:line evidence. |
| 3 | [`android_viberescue_security_privacy_audit.md`](android_viberescue_security_privacy_audit.md) | Android-specific security/privacy audit across 11 categories (manifest, deeplinks, WebView, intents, network, data-at-rest, permissions, auth, validation, secrets/PII, SDK-gated gaps). Severity grounded in the app's actual deployment + threat model. |
| 4 | [`android_viberescue_fix_prioritization.md`](android_viberescue_fix_prioritization.md) | Merge both audits' findings into a four-tier fix queue (Tier 0 security-critical → Tier 3 cleanup). Per-fix impact × effort × reversibility × blast-radius score, batch/isolate recommendation, dependency graph, test gap. |
| 5 | [`android_viberescue_fix_executor.md`](android_viberescue_fix_executor.md) | Execute one fix from the queue safely: precondition checks → failing test first → smallest change → full pipeline → cascade check → single commit → rollback path → queue update. Run in a loop. |
| 6 | [`android_viberescue_rules_file.md`](android_viberescue_rules_file.md) | Generate a project `CLAUDE.md` / `.cursorrules` / `AGENTS.md` sourced entirely to audit evidence and exemplar files. ≤400 lines. Hard don'ts, required patterns, lifecycle rules, security gates, vocabulary, escalation protocol. |

## Recommended Sequence (first run on an app)

```
1.  android_viberescue_wall_diagnosis.md
        └─→ primary mode + cascade check + next prompt pointer
                │
                ├─ if A7 / A8 (security/WebView): → 3 → 4 → 5 (loop) → 6
                └─ otherwise: → 2 → 3 → 4 → 5 (loop) → 6
```

After the first pass:
- **Quarterly maintenance:** re-run #2 + #3, prepend new findings to the queue (#4), execute the new top items (#5), refresh the rules file (#6).
- **Pre-release:** re-run #3, address every Tier 0.
- **Onboarding a new engineer or AI tool:** share the current rules file (#6) and the latest queue (#4).

## How Outputs Chain

| Prompt | Consumes | Produces |
|--------|----------|----------|
| 1 Wall diagnosis | App description, recent sessions, mental model | Primary mode + rescue + next-prompt pointer |
| 2 Codebase audit | Project path, build config, (optional) wall diagnosis | Findings report (sortable, evidence-cited) |
| 3 Security audit | Project path, deployment, threat model | Findings report (severity grounded in deployment) |
| 4 Prioritization | Both audit reports + stakes/capacity | Tiered fix queue with dependency graph |
| 5 Fix executor | One queue item + build/test commands | Commit + rollback + queue update |
| 6 Rules file | Both audits + exemplar files + vocabulary | `CLAUDE.md` / `.cursorrules` ready to commit |

## Reuse Notes (Existing Prompts in the Repo)

These Android-specific prompts **extend, not replace**, the general vibe-rescue and Android-analysis prompts. Reach for the originals when you need:

- **General (non-Android) vibe-rescue:** `../viberescue_wall_diagnosis.md`, `../viberescue_security_audit.md`, `../viberescue_rules_file_design.md`, `../viberescue_decompose_stuck_task.md`, `../viberescue_engineer_handoff_briefing.md`.
- **Android non-rescue analysis** (well-built apps needing review): `../../mobile/android/analysis/android_codebase_health_assessment.md`, `../../mobile/android/analysis/android_authentication_security_audit.md`, `../../mobile/android/analysis/ai_code_review_android.md`.
- **Task too big for the executor (#5)?** Decompose with `../viberescue_decompose_stuck_task.md` first, then run subtasks through the executor.
- **Engineer handoff after fixes:** `../viberescue_engineer_handoff_briefing.md`.

## Agent Compatibility

All six prompts are written without Claude-Code-specific tool names. They use generic verbs: "read the file at X", "search the codebase for Y", "run `./gradlew assembleDebug`". Tested against:

- Claude Code (CLI and web)
- Codex / OpenAI agents
- Cursor
- Windsurf

If your agent has specialized tools (e.g., a manifest validator, a Compose lint), feel free to substitute — the prompt's structure is the contract, not the verb choice.

## Design Principles

- **Evidence over intuition.** Every finding cites file + line. Every rule traces to evidence in this codebase.
- **One fix per commit.** The executor refuses to batch unrelated work, "while-you're-here" cleanups, or scope creep.
- **Severity grounded in deployment + threat model.** A missing cert pin in an internal-only enterprise app is not Critical. The audits ask for the deployment posture and adjust accordingly.
- **Refusal of generic advice.** "Add tests," "refactor," "follow Android guidelines" are explicitly forbidden. Every output names a file, an API, a primitive.
- **Abort > half-fix.** The executor aborts loudly when preconditions fail, when tests don't fail-first, when the diff cascades. Half-applied fixes are worse than the original problem.
- **Rules files are evidence-sourced.** Generic Android style guides don't reduce vibe-coding regression. Rules grounded in this codebase's actual recurring mistakes do.

## Quick Start for a New User

If you've never run this on an app before:

1. `cd` into the Android project root.
2. Open Claude Code / Codex / your agent in that directory.
3. Paste `android_viberescue_wall_diagnosis.md` as the opening message. Answer its input questions.
4. Follow the "next prompt" pointer in the diagnosis output.
5. By the time you reach `android_viberescue_fix_executor.md`, you'll have a ranked queue. Loop the executor over the top items.
6. End the first session with `android_viberescue_rules_file.md` so future sessions stop repeating the same mistakes.

A reasonable first session is **4–8 hours**: diagnosis + both audits + prioritization + a few Tier 0 fixes + rules file. Subsequent sessions execute against the queue.

## Cross-References

- General vibe-coding rescue cluster: [`../`](..)
- Mobile / Android prompts (analysis & implementation): [`../../mobile/android/`](../../mobile/android/)
- AI patterns and footgun detection: [`../../../domain-engineering-workflows/ai-patterns/`](../../../domain-engineering-workflows/ai-patterns/)
- Long-running project memory: [`../../../domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md`](../../../domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md)
- General security analysis (cross-language): [`../../analysis/security/`](../../analysis/security/)

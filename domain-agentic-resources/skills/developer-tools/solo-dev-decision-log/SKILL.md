---
name: solo-dev-decision-log
description: "Lightweight Architecture Decision Record (ADR) system for solo developers. Generates and maintains numbered markdown decision records in a decisions/ directory. Emphasizes speed (under 5 minutes per decision) and communication with your future self. Use this skill when making technology choices, architecture trade-offs, or any 'why did I do it this way?' decisions, or when a developer mentions 'ADR', 'decision log', 'why did I choose', 'document decision', or 'architecture decision'."
metadata:
  tags:
    - architecture
    - documentation
    - solo-developer
    - adr
    - decision-making
  updated: "2026-03-06"
---

# Solo Dev Decision Log

Lightweight Architecture Decision Record (ADR) system designed for solo developers. Creates and maintains a `decisions/` directory with numbered markdown records that communicate with your future self about non-obvious choices.

## Purpose

Solo developers make every architectural and technology decision alone. Three months later, they forget why they chose Room over Realm, Hilt over Koin, or a single-module structure over multi-module. Without a team to ask, they either re-research the decision or blindly change it — both waste time. This skill provides a 5-minute decision record format that captures the "why" and prevents re-debating settled questions. It is explicitly designed for speed — if writing a decision record takes longer than the decision itself, something is wrong.

## When to Use This Skill

Use this skill when you need to:
- Document a technology or library choice (database, DI, networking, image loading)
- Record an architecture decision (single vs multi-module, MVVM vs MVI, navigation approach)
- Capture a trade-off you made (performance vs readability, speed vs correctness)
- Explain a non-obvious implementation choice to your future self
- Document decisions made during vibe coding sessions
- Record why you rejected an alternative that seems obvious

## When NOT to Use This Skill

Do NOT use this skill when:
- The decision is obvious (using Kotlin for an Android app)
- The decision is trivially reversible in under 5 minutes (variable naming, file organization)
- You are using a standard library in a standard way (no decision to record)
- The decision has already been recorded (update the existing record instead)

## Prerequisites

- A `decisions/` directory in your project root (will be created on first use)
- Basic markdown editing capability

## Step 1: Decide Whether to Record

Use this 30-second filter:

```
Will I (or someone else) wonder "why?" about this in 3 months?
├── YES → Write a decision record (go to Step 2)
├── MAYBE → Write a quick-format record (go to Step 2, use Quick Format)
└── NO → Don't write anything
```

**Examples that warrant a record:**
- "Why Room instead of SQLite directly?" → YES
- "Why Hilt instead of Koin?" → YES
- "Why single Activity architecture?" → YES
- "Why did I hardcode this timeout at 30 seconds?" → MAYBE
- "Why did I name this variable `items`?" → NO

## Step 2: Write the Record

### 2.1 Standard Format (3-5 minutes)

Create a new file: `decisions/NNNN-short-title.md`

```markdown
# NNNN. Short Decision Title

**Date:** YYYY-MM-DD
**Status:** accepted

## Context

What is the situation that requires a decision? What problem are you solving?
Keep this to 2-3 sentences.

## Options Considered

### Option A: [Name]
- **Pros:** [1-2 bullet points]
- **Cons:** [1-2 bullet points]

### Option B: [Name]
- **Pros:** [1-2 bullet points]
- **Cons:** [1-2 bullet points]

## Decision

We chose **Option [X]** because [one sentence explaining why].

## Consequences

- [What becomes easier as a result of this decision]
- [What becomes harder as a result of this decision]
- [What we give up]
```

### 2.2 Quick Format (1-2 minutes)

For smaller decisions, use this compressed format:

```markdown
# NNNN. Short Title

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** [One sentence]
**Decision:** [One sentence]
**Because:** [One sentence]
**Trade-off:** [What we gave up]
```

### 2.3 Numbering

Sequential four-digit numbers: `0001`, `0002`, `0003`, ...

```bash
# Find the next number
ls decisions/ | tail -1
# If last file is 0007-..., next is 0008
```

## Step 3: Status Lifecycle

| Status | Meaning | When to Use |
|--------|---------|-------------|
| **proposed** | Under consideration | Before you commit to the decision |
| **accepted** | Decision made and active | Default for new decisions |
| **deprecated** | No longer relevant | Technology removed or approach abandoned |
| **superseded by NNNN** | Replaced by newer decision | When you change your mind with new evidence |

## Templates for Common Decisions

### Database Choice
```markdown
# 000N. Use [Room/Realm/SQLDelight] for Local Storage

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** App needs local persistence for [what data].
**Decision:** Use [choice] for local storage.
**Because:** [reason — e.g., "Room has first-party Compose Flow support and Google maintains it"]
**Trade-off:** [e.g., "Room requires more boilerplate than Realm but has better long-term support"]
```

### DI Framework Choice
```markdown
# 000N. Use [Hilt/Koin/Manual] for Dependency Injection

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** App needs dependency injection for [testability/modularity/etc].
**Decision:** Use [choice].
**Because:** [reason]
**Trade-off:** [e.g., "Hilt adds compile-time overhead but catches DI errors at compile time vs Koin's runtime errors"]
```

### Architecture Pattern
```markdown
# 000N. Use [MVVM/MVI/MVP] Architecture Pattern

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** Establishing the UI architecture pattern for the app.
**Decision:** Use [pattern] with [specific variant — e.g., "MVVM with StateFlow and Compose"].
**Because:** [reason]
**Trade-off:** [e.g., "More boilerplate per screen but predictable state management"]
```

### Navigation Approach
```markdown
# 000N. Use [Navigation Compose/Fragment Navigation/Custom] for Navigation

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** App has [N] screens with [describe flow complexity].
**Decision:** Use [choice].
**Because:** [reason]
**Trade-off:** [what's harder]
```

### Module Structure
```markdown
# 000N. Use [Single Module/Multi-Module] Project Structure

**Date:** YYYY-MM-DD | **Status:** accepted

**Context:** Project is currently [size] with [N] features.
**Decision:** Use [single module/multi-module] structure.
**Because:** [reason — e.g., "single module until app exceeds 50k LOC to keep build times fast"]
**Revisit when:** [trigger — e.g., "build time exceeds 60 seconds or team grows beyond 1"]
```

## Step 4: Link Decisions to Code

Reference ADR numbers in code where the decision is implemented:

```kotlin
// ADR-0003: Using Room over Realm for local storage
@Database(entities = [ItemEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
```

```kotlin
// ADR-0007: Single Activity architecture — all navigation via NavHost
class MainActivity : ComponentActivity() {
```

This creates a two-way link: code explains "how", ADR explains "why".

## Step 5: Periodic Review

Every quarter (or every 10 decisions), scan your decisions:

```bash
# List all decisions
ls decisions/

# Find accepted decisions older than 6 months
find decisions/ -name "*.md" -mtime +180
```

For each old decision:
- Is it still relevant? → Keep as `accepted`
- Has the technology been removed? → Update to `deprecated`
- Have you changed your approach? → Create a new decision that `supersedes` this one

## Example Decision Log

```
decisions/
├── 0001-use-room-for-local-storage.md
├── 0002-use-hilt-for-dependency-injection.md
├── 0003-mvvm-with-stateflow-and-compose.md
├── 0004-single-module-until-50k-loc.md
├── 0005-navigation-compose-for-navigation.md
├── 0006-coil-for-image-loading.md
├── 0007-retrofit-with-kotlinx-serialization.md
├── 0008-single-activity-architecture.md
└── 0009-github-actions-for-ci.md
```

## Anti-Patterns

### "Documenting Everything"
If you have 50 decision records for a 10k LOC project, you are over-documenting. Most projects need 10-20 significant decisions.

### "Writing a Novel"
If a decision record takes more than 5 minutes to write, you are including too much detail. Keep it to the format above.

### "Never Revisiting"
Decision records are not permanent laws. Technology changes, requirements evolve, and your understanding deepens. Review and update regularly.

### "Skipping the 'Because'"
"We use Room" is not a decision record. "We use Room because it has first-party Compose integration and Google maintains it" is a decision record. The "because" is the entire point.

## Related Skills

- `vibe-coding-workflow` — Document decisions made during vibe sessions
- `solo-dev-self-review` — Review discovers decisions that should be documented
- `android-quarterly-maintenance` — Quarterly review of past decisions

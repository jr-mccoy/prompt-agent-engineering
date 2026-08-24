# Technique Promotion Criteria

Decision rules for "should this pattern become a new technique ID in `MASTER_TECHNIQUE_INDEX.md`?"

## Default: Match an Existing Technique

The master index has 258+ techniques. Most patterns in incoming kits map to existing IDs. Before proposing a new technique, search the index for:

- The pattern's behavioral verb (gate, enumerate, classify, audit, score)
- The pattern's structural shape (multi-phase, conditional output, adversarial pass)
- The pattern's domain (agent, metric, trace, observability, oversight)

If you can find a 70%+ match, **use the existing ID**.

## Promote to a New ID Only If All Five Apply

1. **Genuinely novel mechanism.** The pattern does something no existing technique does. "Adversarial pass" exists; "adversarial pass scoped to inflate-without-deliver scenarios specifically" probably doesn't merit a new ID — that's a use-case variant.

2. **Reusable across domains.** The pattern would be useful in at least three unrelated domains (e.g., agent loops + healthcare metrics + business KPIs). Single-domain patterns belong as prompt-level tags, not techniques.

3. **Articulable as a standalone instruction.** You can describe the technique in 1–2 sentences without referencing the source kit. If the description requires the kit's context, it's not a technique — it's a prompt.

4. **Has an obvious "different from" pair.** You can name the existing technique it most resembles and articulate what makes the new one distinct in one sentence (the master index uses this `**Different from X:**` pattern throughout).

5. **Not just a composition.** "Use ST-01 then run QA-08" is a workflow, not a technique. Workflows belong in `domain-engineering-workflows/`, not the technique index.

## ID Assignment

If the criteria pass, assign the next sequential ID in the most appropriate category:

| Category Prefix | Domain |
|---|---|
| `ST` | Structural |
| `RT` | Reasoning |
| `CM` | Constraint Management |
| `DS` | Data Specification |
| `OC` | Output Control |
| `QA` | Quality Assurance |
| `RT` | Red Teaming |
| `AG` | Agentic |
| `NE` | Negotiation / Phasing |
| `DT` | Decision Trees |
| `DP` | Default Policy |

Check the highest existing ID in the category (e.g., `grep "^### AG-" MASTER_TECHNIQUE_INDEX.md | tail -1`) and increment.

## New Entry Skeleton

When adding to `MASTER_TECHNIQUE_INDEX.md`, use:

```markdown
### XX-NN: Technique Name

**What it does:** One-sentence behavioral description.

**When to use:** Triggers / scenarios.

**Pattern:**
```
{instruction template the user would actually paste}
```

**Example:** Concrete short example showing input → expected behavior.

**Different from XX-MM:** One sentence distinguishing it from the closest existing technique.

**See Also:** XX-AA, XX-BB
```

Update the table of contents at the top of `MASTER_TECHNIQUE_INDEX.md` and any `USE_CASE_LOOKUP.md` entries the new technique enables.

## Bias Toward Restraint

Adding a technique ID is permanent — it gets referenced in frontmatter across the repo and becomes a load-bearing part of the catalog. Removing one later requires updating every prompt that cites it. When in doubt, **don't promote.** Tag the prompt with the closest existing IDs and add a `tags:` keyword for the novel angle.

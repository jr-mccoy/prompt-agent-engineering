# Ingestion Checklist

Run this against every extracted prompt file before declaring the ingestion complete. Any unchecked item blocks delivery.

## Per-File Checks

- [ ] Filename follows `{category}_{specific_function}.md` (or `workflow_agent_{topic}.md` for ai-patterns)
- [ ] Lives in a directory consistent with root `CLAUDE.md` Category Mapping
- [ ] YAML frontmatter parses (no missing colons, balanced quotes)
- [ ] `title` is in title case
- [ ] `category` matches the directory
- [ ] `description` is one sentence ending in a period
- [ ] `techniques` lists 3+ IDs and every ID exists in `MASTER_TECHNIQUE_INDEX.md`
- [ ] `tags` lists 3–6 lowercase keywords
- [ ] `difficulty` is one of: beginner | intermediate | advanced
- [ ] `updated` is today's date in `YYYY-MM-DD`
- [ ] `related_prompts` lists at least one valid path
- [ ] Body opens with `# {Title}` matching the frontmatter title
- [ ] Body has `Purpose`, `When to use`, `What you'll get`, `Source` lines in order
- [ ] `Source:` line names the original kit file
- [ ] Verbatim prompt is inside a fenced ```markdown block
- [ ] Prompt content is not paraphrased — matches the source author's wording exactly

## Repo-Level Checks

- [ ] Every new file appears in `PROMPT_INDEX.json` with all required fields
- [ ] Every new file appears in `PROMPT_INDEX.md` in the appropriate domain section
- [ ] If new technique IDs were added, they have full definitions (not just IDs) in `MASTER_TECHNIQUE_INDEX.md`
- [ ] If a new subdirectory was created, root `CLAUDE.md` Category Mapping is updated to include it
- [ ] Source kit file has a `> **Repository note:**` block at the top listing the new structured files
- [ ] Source kit file has no other modifications

## Pre-Delivery Checks

- [ ] `git status` shows only the expected new and modified files
- [ ] No accidental edits to unrelated prompts
- [ ] Implications memo drafted (covers pattern family, cross-references, technique impact, gaps, follow-ups)
- [ ] Memo is 200–400 words, direct prose

## Anti-Checklist (things that mean you went off-script)

- [ ] Did NOT re-read the source file after Phase 1
- [ ] Did NOT re-verify the master technique index after Phase 3
- [ ] Did NOT modify any prompts unrelated to this kit
- [ ] Did NOT commit unless the user asked
- [ ] Did NOT build the follow-up resources suggested in the memo unless requested

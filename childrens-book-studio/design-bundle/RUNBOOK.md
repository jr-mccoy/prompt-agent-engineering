# Runbook — Children's Book Studio (design bundle)

How to run the system, what can go wrong, and how to recover.

## Deployment / rollout

There is nothing to deploy — the system is a set of markdown prompts. "Rollout" means: an author (or a coding agent) loads `childrens-book-studio/orchestrator_childrens_book.md` and follows it. For a careful first run, do a **shadow run** on a throwaway idea to see each gate fire (see `../DRY_RUN.md`).

## Standard run

1. Load the orchestrator (or `/write-childrens-book`).
2. Answer the five intake questions.
3. Follow the recommended stage prompts in order; paste each output back for critique.
4. Clear each gate before advancing.
5. Collect the deliverable bundle at Stage 6.

## Rollback

<!-- ROLLBACK: present -->

Every state-modifying action is a **versioned manuscript write** (`manuscript-v[N].md`); the prior version is never overwritten. To roll back: discard the latest version and resume from any earlier one. The author owns all files and can revert at any gate. No external state is mutated, so there is nothing else to undo.

## Failure-mode catalog

| Failure | Symptom | Recovery |
|---------|---------|----------|
| **Form mismatch** | idea won't fit the chosen form's word band | re-run Stage 0; resize idea or re-pick form |
| **Passive protagonist** | Gate A fails on agency | return to Stage 4; re-anchor the climax to the child's action |
| **Preachy theme** | Gate A fails on no-moral | return to Stage 4; cut stated morals; let events prove the theme |
| **Reading level off band** | Gate A fails on level | run `/calibrate-reading-level`; adjust vocab/syntax, keep voice |
| **Unsourced NF fact** | open `VERIFY` at Gate B | return to Stage 5; source it or cut it — never guess |
| **Audit reads as approval** | certification language at Gate B | return to Stage 5; rewrite audit as flags/questions |
| **Mature content leak** | Gate B fails on age-appropriateness | return to Stage 5 (or Stage 0 if the project is really mature-YA → redirect out) |
| **Fabricated comp/agent** | un-bracketed market fact at Gate C | return to Stage 6; bracket `[AUTHOR TO VERIFY]` |
| **Revision loop won't converge** | Stage 4 keeps surfacing issues | stop after a pass yields no new high-impact issue and Gate A passes; if structural, return to Stage 2 |

## Escalations (out of the system)

- Cultural authenticity questions the audit raises → a paid sensitivity reader / own-voices author.
- Real comps, agent lists, submission rules → the author's market research (e.g., agent databases, recent catalogs).
- Final illustration → a hired illustrator or the publisher's art department.
- Mature-YA content → `domain-creative-writing/`.

# Referenced Prompts (vendored)

*Not legal, tax, or accounting advice.*

**Pinned copies** of the 39 prompts this toolkit's stages orchestrate, vendored so
`client-services-studio/` can be unpacked on its own and run without the rest of the
parent repository.

These are copies. The maintained originals live at the paths mirrored here;
`meta/VENDORED.tsv` in the parent repository records each canonical → copy pair, and
`scripts/check_vendored_copies.py` enforces in CI that they do not drift.

**Do not edit anything in this directory.** Edit the canonical and run
`python3 scripts/check_vendored_copies.py --fix` from the repository root.

## What is here

| Directory | Count | Used by |
|---|---|---|
| `domain-business-strategy/client-services/` | 8 | Stages 0, 1, 4 — offer, ICP, pricing model, value, retainer, capacity, productization, concentration |
| `domain-business-strategy/go-to-market/` | 1 | Stage 1 — background research |
| `domain-sales-customer/sales/` | 1 | Stage 2 — discovery-call preparation (moved from `go-to-market/` in coverage Wave 2) |
| `domain-finance/corporate-finance-fpa/` | 3 | Stages 0, 4, 9 — rate floor, subcontractor margin, engagement profitability |
| `domain-finance/accounting-controllership/` | 3 | Stage 8 — invoice schedule, AR aging, collections ladder |
| `domain-legal/contracts-transactional/` | 6 | Stages 5, 6 — SOW, clause redlines, risk heatmap, payment terms, termination economics, flow-down |
| `domain-legal/client-intake-communications/` | 1 | Stage 8 — demand letter, the ladder's final rung |
| `domain-professional-writing/business-writing/` | 4 | Stages 5, 7, 9 — proposal, status report, case study, testimonial and referral |
| `domain-professional-writing/content-quality/` | 2 | Stages 5, 9 — client-deliverable and case-study quality gates |
| `domain-engineering-workflows/workflows/` | 1 | Stage 3 — definition-of-done builder, for testable acceptance criteria |
| `domain-negotiation/` | 7 | Stages 2, 4, 7 — information plan, interest mapping, opening offer, rate conversation, implementation and drift, bad news, saying no |
| `domain-risk/` | 2 | Stages 3, 9 — engagement risk register, after-action review |

## Why these and not others

The toolkit orchestrates rather than duplicates. Each prompt here is one a stage
actually invokes. Cross-references *inside* these copies that point at prompts not
vendored here resolve back to the parent repository's canonicals — that is what
`check_vendored_copies.py --fix` maintains. Unpacked standalone, those particular
links will not resolve; every prompt the pipeline itself needs is present.

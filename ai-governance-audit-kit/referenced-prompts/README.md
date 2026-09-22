# Referenced prompts — vendored copies

Thirty-one prompts the engagement runs against, copied here so the kit unpacks
and runs with nothing else from the parent repository.

**These are copies, not canonicals.** Every pair is registered in
`meta/VENDORED.tsv` and checked by `scripts/check_vendored_copies.py`, which
fails CI if a copy drifts from its canonical. Edit the canonical; never edit a
file under this directory.

This tree sits in `NON_RESOURCE_PREFIXES`, so nothing here is counted twice in
the registry.

## What is here, and why the engagement needs it

| Source | Count | Where it is used |
|---|---|---|
| `domain-AI-ML/responsible-ai-governance/` | 12 | the governance instruments a client's programme is assessed against — NIST AI RMF, the EU AI Act, model risk, documentation freshness, red teaming, privacy, ethics review |
| `domain-AI-ML/agentic-ai-systems/` | 3 | zero-trust maturity, the supply-chain AIBOM (which *is* the inventory artifact a client's security function will ask for), and the complexity-ladder gate that asks whether an agent was needed at all |
| `domain-prompt-engineering/evaluation/` | 4 | the per-artifact audit unit (`correctness_prompt_specification_audit`), the org-level maturity instrument (`prompt_lifecycle_assessment`), eval design, and repository-level reflection |
| `domain-prompt-engineering/prompt-improvement/` | 12 | remediation: this is what Stage 7 hands the client's team to execute, rather than a list of complaints |

## The division of labour

The scripts in `skills/` observe **structure** — what is present, what is
duplicated, what is exposed. They deliberately cannot judge content.

These prompts are where the judgement happens, and it happens with a human in
the loop. The audit locates; the prompts remediate. Keeping the two separate is
what lets the machine half refuse to assert a tier while the engagement still
produces an opinion — a clearly attributed one.

## Orchestrated, not rebuilt

The kit adds no governance prompt of its own. Everything in this directory
already existed; what did not exist was a pipeline that sequences them against
a real corpus with gates that fail closed. That sequencing is the kit.

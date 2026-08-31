# Security & Privacy Policy

This is primarily a documentation and prompt repository — it ships markdown, not a deployed service. Even so, a few security and privacy concerns matter here, and we take them seriously.

## Reporting a concern

If you find any of the following, please report it **privately** rather than opening a public issue:

- Secrets, credentials, API keys, or tokens accidentally committed anywhere in the repo
- Personal or sensitive data (PII) committed to the repository
- A prompt that could materially mislead in a high-stakes domain (e.g. clinical, legal, financial) in a way that looks like a genuine safety problem
- Any vulnerability in the helper scripts under `scripts/` or the toolkits

**Contact:** Report privately via GitHub's [Security Advisories](https://github.com/jr-mccoy/prompt-agent-engineering/security/advisories/new) (Security → Report a vulnerability).

Please include the file path(s), a short description, and (if relevant) how to reproduce. We aim to acknowledge reports within a few days. Public disclosure of an accidentally committed secret should be avoided until it has been rotated and purged.

## What we ask of contributors

- **Never commit secrets.** No API keys, passwords, tokens, or `.env` files. The root [`.gitignore`](.gitignore) provides a safety net (`.env*`, `*.local.yaml`, `secrets.yaml`), but the first line of defense is you.
- **Never commit real personal data.** Prompts should use synthetic or clearly fictional examples. Do not paste real patient records, client files, financial statements, or anyone's private information into a prompt or example.
- **Keep working data out of git.** The self-contained toolkits handle sensitive working data locally and ship their own nested `.gitignore` files — do not remove or weaken them:
  - [`financial-records-toolkit/`](financial-records-toolkit/) and [`domain-agentic-resources/skills/financial-records/`](domain-agentic-resources/skills/financial-records/) process bank/credit-card statements; their convention is that **PII stays local and out of version control**.
  - [`ai-investment-research-toolkit/`](ai-investment-research-toolkit/) keeps market data, snapshots, and secrets out of git and is paper-only by design.

## Domain-specific threat models

Some toolkits document their own detailed threat models (prompt injection, untrusted content, data governance). These are the authoritative references for those areas:

- [`ai-investment-research-toolkit/SECURITY.md`](ai-investment-research-toolkit/SECURITY.md) — prompt-injection & untrusted-content threat model, gate architecture, kill switch
- [`domain-AI-ML/agentic-ai-systems/`](domain-AI-ML/agentic-ai-systems/) — design prompts for agent safety, sandboxing, runtime guardrails, prompt-injection defense, and privacy/data governance

## Scope

This policy covers the repository contents and its helper scripts. It does **not** cover third-party AI models or platforms (ChatGPT, Claude, Cursor, etc.) that you use these prompts with — report issues with those to their respective vendors.

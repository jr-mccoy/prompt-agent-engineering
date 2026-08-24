# Privacy & Data Handling

You are processing highly sensitive personal financial data (account numbers,
balances, spending patterns). Handle it accordingly.

## Process locally; minimize exposure

- This entire pipeline runs **locally** with deterministic Python scripts. The
  only step that touches the network is *optional* merchant research, which
  searches a **merchant descriptor string** — never your account number, name,
  or other PII.
- Do not paste raw statements or full transaction exports into web chat tools.
  Work from the local files.

## If you use a private GitHub repo to drive the agents

A private repo is a reasonable way to let Claude Code / Codex process the files,
but treat it as temporary and contained:

- Make the repo **private**. Confirm it is private before pushing anything.
- Use the included `.gitignore` so raw PDFs and outputs are **never committed**.
  Keep statements in `data/input_pdfs/` and results in `data/output/` (both ignored).
- Commit only the **tooling** (skills, scripts, config), not your data.
- When finished: download the outputs you need, then **delete the repo** (and any
  forks/clones) to reduce the window of exposure.
- Rotate any credential that ever sat in the repo.

## Secure deletion when done

- Remove local working copies of raw statements and intermediate CSVs you no
  longer need.
- Empty trash / recycle bin; on SSDs, secure-erase tools have limited effect, so
  prefer full-disk encryption from the start.
- Keep only the final deliverables your attorney asked for, stored where your
  attorney directs.

## Sharing with your attorney

- Send files through the channel your attorney specifies (secure portal,
  encrypted email). Avoid unencrypted email for full exports.
- The review queue and workbook are designed to be attorney-facing; they contain
  facts, not conclusions.

## What the tools will not do

- They will not transmit your data anywhere on their own.
- They will not fabricate transactions, merchants, or categories.
- They will not characterize the other party or assert wrongdoing.

If any step would require sending your financial data to an external service,
stop and confirm that is what you intend.

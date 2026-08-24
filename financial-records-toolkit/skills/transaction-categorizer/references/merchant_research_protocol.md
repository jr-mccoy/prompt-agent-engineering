# Merchant Research Protocol

When the categorizer cannot identify a merchant, it queues the descriptor instead
of guessing. This protocol explains how to identify it accurately and record the
result so the system learns. The `transaction-research-agent` automates it.

## The one rule: never fabricate

If you cannot determine what a merchant is, leave it `UNKNOWN` and
`needs_review = TRUE`. A wrong category is worse than an honest unknown,
especially when the data may be reviewed by an attorney.

## How to identify a descriptor

Bank descriptors are noisy (prefixes like `SQ *`, `TST*`, `PP*`, `ACH DEBIT`,
trailing store/reference numbers). To identify one:

1. **Strip the noise.** Remove processor prefixes (`SQ *`, `TST*`, `PP*`,
   `PAYPAL *`, `CKE*`), trailing digits, city/state, and store numbers to find
   the core name.
2. **Web search the core name** (and, if present, the city/state). Confirm what
   the business is and its primary category.
3. **Use MCC if available.** If the descriptor includes an MCC, the open
   `greggles/mcc-codes` table maps it to a category — often decisive.
4. **Recognize payment platforms.** `VENMO`, `ZELLE`, `PAYPAL`, `CASH APP`,
   `WISE` are *transfers*, not spending categories — categorize as
   `TRANSFER_IN`/`TRANSFER_OUT` and note the counterparty if known.
5. **Recognize financial movements.** Brokerages, robo-advisors, crypto
   exchanges, and bank transfers are `TRANSFER_OUT`/`TRANSFER_IN`, not purchases.

## Recording findings

Write a YAML list and merge it with `--merge`. The `match` is matched as a
substring against the uppercased description, so use a stable core token:

```yaml
- match: "SQ *BLUE BOTTLE"
  category: FOOD_AND_DRINK
  subcategory: COFFEE
  note: "researched 2026-06-09: Blue Bottle Coffee, Square seller; confirmed via web search"
- match: "WEALTHFRONT"
  category: TRANSFER_OUT
  subcategory: INVESTMENT
  note: "researched: Wealthfront automated investing transfer"
```

Always fill `note` with the basis for the decision and (optionally) the date —
it is your audit trail if a category is ever questioned.

## Ambiguous cases

- **Generic descriptors** (`ACH DEBIT 8829`, `POS PURCHASE`): if the
  counterparty can't be determined, leave UNKNOWN and note "uninterpretable
  descriptor — needs bank detail or memory."
- **Could be personal or business:** record both possibilities in `note` and let
  the human decide; do not silently pick one.
- **Same name, different businesses:** use city/state from the descriptor to
  disambiguate; if you can't, leave UNKNOWN.

## Privacy

Search only the merchant descriptor text — never the account number, your name,
or other PII. You are identifying a business, not exposing your records.

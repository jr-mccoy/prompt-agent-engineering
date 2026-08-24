# Category Taxonomy & Matching Layers

## Plaid personal-finance taxonomy (the standard)

Use these 16 primary categories verbatim as the `category` value. Each has
detailed subcategories (104 total). The full, free taxonomy CSV:
https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv

| Category | Typical contents |
|----------|------------------|
| `INCOME` | Wages, dividends, interest, bonuses |
| `TRANSFER_IN` | Deposits, inter-account transfers in, loans received |
| `TRANSFER_OUT` | Withdrawals, inter-account transfers out, cash |
| `LOAN_PAYMENTS` | Credit-card, mortgage, auto, student-loan payments |
| `BANK_FEES` | ATM fees, overdraft, NSF, service charges |
| `ENTERTAINMENT` | Streaming, games, movies, events, gambling |
| `FOOD_AND_DRINK` | Groceries, restaurants, coffee, bars |
| `GENERAL_MERCHANDISE` | Amazon, superstores, clothing, electronics |
| `HOME_IMPROVEMENT` | Furniture, hardware, repair, contractors |
| `MEDICAL` | Doctors, dentists, pharmacy, vet |
| `PERSONAL_CARE` | Gyms, salons, laundry |
| `GENERAL_SERVICES` | Childcare, tuition, insurance, legal, accounting |
| `GOVERNMENT_AND_NON_PROFIT` | Taxes, government agencies, donations |
| `TRANSPORTATION` | Gas, parking, transit, rideshare |
| `TRAVEL` | Flights, hotels, rental cars |
| `RENT_AND_UTILITIES` | Rent, electricity, gas, water, phone, internet |

## Matching layers (first hit wins)

1. **MCC code** — if the descriptor contains `MCC:1234`, look it up in
   `mcc_mappings`. Open MCC table: https://github.com/greggles/mcc-codes
   (confidence 0.97).
2. **Merchant whitelist** — exact match (confidence 1.0), then substring
   (0.95). Most reliable; prefer adding whitelist entries for recurring payees.
3. **Regex patterns** — broad descriptor families like `CHEVRON|SHELL|EXXON`
   (confidence 0.93). Good for chains.
4. **Fuzzy** — closest known merchant name above `--threshold` (confidence
   scales with similarity). A safety net, not a primary method.

Anything unmatched → `category = UNKNOWN`, `needs_review = TRUE`, queued for research.

## Confidence and review

The CSV's `confidence` is the minimum of the extraction confidence and the
categorization confidence. Rows below 0.75 are marked `needs_review = TRUE` so a
human verifies them. Unknowns are 0.0 until researched.

## Subcategories

Subcategories are free-form here (e.g. `GROCERIES`, `COFFEE`, `RENT`). For strict
Plaid alignment, use the detailed labels from the taxonomy CSV. Consistency
matters more than exactness — pick a convention and keep it in the rules file.

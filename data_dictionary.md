# Data Dictionary - Mutual Fund Analytics DB

## Table: dim_fund
| Column Name | Data Type | Business Definition | Source |
| :--- | :--- | :--- | :--- |
| amfi_code | INTEGER (PK) | Unique AMFI structural identifier for schemes | Scheme Master |
| fund_name | TEXT | Fully qualified name of mutual fund scheme | Scheme Master |
| category | TEXT | Fund class asset allocation group (Equity, Debt) | Scheme Master |
| isin | TEXT | International Securities Identification Number | Scheme Master |

## Table: fact_transactions
| Column Name | Data Type | Business Definition | Source |
| :--- | :--- | :--- | :--- |
| transaction_id | TEXT (PK) | Unique operational key per ledger entry | Transaction Log |
| amfi_code | INTEGER (FK) | Links transaction transaction map to schema master | Transaction Log |
| amount | REAL | Monetary volume footprint of action item | Transaction Log |
| transaction_type| TEXT | Strategy flag applied: SIP, Lumpsum, Redemption | Transaction Log |
| kyc_status | TEXT | Investor operational identity validation state | CRM Export |
| state | TEXT | Geographic footprint region state identifier | CRM Export |
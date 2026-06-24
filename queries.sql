-- 1. Top 5 funds by AUM
SELECT amfi_code, total_aum
FROM fact_aum
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT amfi_code, STRFTIME('%Y-%m', date_id) as month, AVG(nav) as avg_nav
FROM fact_nav
GROUP BY amfi_code, month;

-- 3. SIP Year-over-Year (YoY) growth
SELECT STRFTIME('%Y', transaction_date) as year, SUM(amount) as total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year;

-- 4. Transactions volume/amount distributed by state
SELECT state, COUNT(*) as transaction_count, SUM(amount) as total_invested
FROM fact_transactions
GROUP BY state
ORDER BY total_invested DESC;

-- 5. Funds with expense_ratio < 1%
SELECT amfi_code, expense_ratio
FROM fact_performance
WHERE expense_ratio < 0.01;

-- 6. Total Redemption amount per fund
SELECT amfi_code, SUM(amount) as total_redeemed
FROM fact_transactions
WHERE transaction_type = 'Redemption'
GROUP BY amfi_code;

-- 7. Funds with high performance (>12% return over 3y) but low expense ratio (<1.5%)
SELECT amfi_code, return_3y, expense_ratio
FROM fact_performance
WHERE return_3y > 0.12 AND expense_ratio < 0.015;

-- 8. Count of non-compliant (Pending/Failed) KYC transactions
SELECT kyc_status, COUNT(*) as txn_count
FROM fact_transactions
WHERE kyc_status != 'VERIFIED'
GROUP BY kyc_status;

-- 9. Latest recorded NAV for each fund scheme
SELECT amfi_code, MAX(date_id) as latest_date, nav
FROM fact_nav
GROUP BY amfi_code;

-- 10. Top 3 states with highest active SIP setups
SELECT state, COUNT(*) as sip_count
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY state
ORDER BY sip_count DESC
LIMIT 3;
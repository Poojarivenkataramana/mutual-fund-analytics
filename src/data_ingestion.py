import pandas as pd
import os

# Path to your raw data folder
raw_data_path = "data/raw/"

# The exact 10 filenames you just moved
csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("--- STARTING DATA INGESTION QUALITY CHECK ---")

for file in csv_files:
    file_path = os.path.join(raw_data_path, file)

    if os.path.exists(file_path):
        print(f"\n==========================================")
        print(f"Checking File: {file}")
        print(f"==========================================")

        # Load the dataset
        df = pd.read_csv(file_path)

        # Print shape, dtypes, and head
        print(f"🔹 Rows & Columns (Shape): {df.shape}")
        print("\n🔹 Column Data Types:")
        print(df.dtypes)
        print("\n🔹 First 3 Rows:")
        print(df.head(3))

    else:
        print(f"❌ File missing: {file}. Please check your mymfproject/data/raw/ folder.")

print("\n--- INGESTION CHECK COMPLETE ---")

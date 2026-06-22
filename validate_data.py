import pandas as pd

# Load the master file and history file
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("--- TASK 6: EXPLORING FUND MASTER ---")
print("\n🔹 Unique Fund Houses:")
print(fund_master['fund_house'].unique())

print("\n🔹 Unique Categories:")
print(fund_master['category'].unique())

print("\n🔹 Unique Sub-Categories:")
print(fund_master['sub_category'].unique())

print("\n🔹 Unique Risk Categories:")
print(fund_master['risk_category'].unique())

print("\n==========================================")
print("--- TASK 7: VALIDATING AMFI SCHEME CODES ---")
print("==========================================")

# Let's inspect the column names of nav_history to find the correct code column
print("📋 Columns available in 02_nav_history.csv are:")
print(list(nav_history.columns))
print("-" * 40)

# We will look for a column that has 'code' or 'amfi' in its name dynamically
history_code_col = [col for col in nav_history.columns if 'code' in col.lower() or 'amfi' in col.lower()]

if history_code_col:
    target_col = history_code_col[0]
    print(f"Using '{target_col}' as the code column for nav_history.\n")

    master_codes = set(fund_master['amfi_code'].unique())
    history_codes = set(nav_history[target_col].unique())

    # Check if all master codes are in the history file
    missing_in_history = master_codes - history_codes

    print(f"Total unique schemes in Master (amfi_code): {len(master_codes)}")
    print(f"Total unique schemes in History ({target_col}): {len(history_codes)}")

    if len(missing_in_history) == 0:
        print("\n✅ DATA QUALITY SUMMARY: Validation Passed! Every AMFI code in fund_master exists in nav_history.")
    else:
        print(
            f"\n⚠️ DATA QUALITY SUMMARY: Found {len(missing_in_history)} codes in fund_master that are missing from nav_history!")
        print(f"Missing codes sample: {list(missing_in_history)[:5]}")
else:
    print("❌ Could not automatically find a code column in nav_history. Please check your column names printout.")
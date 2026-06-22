import requests
import pandas as pd
import os
import time

# 1. Setup the correct folder path
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

# 2. Dictionary of the 5 key schemes with their AMFI codes
schemes = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

print("--- STARTING MULTI-SCHEME LIVE NAV FETCH ---")

# Loop through each scheme and download its data
for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"\nFetching live data for {name.upper()} (Code: {code})...")

    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        nav_history = json_data['data']

        # Convert to DataFrame
        df_scheme = pd.DataFrame(nav_history)

        # Save as a unique CSV file
        output_path = os.path.join(output_dir, f"{name}_raw.csv")
        df_scheme.to_csv(output_path, index=False)

        print(f"✅ Success! Saved {df_scheme.shape[0]} rows to {output_path}")

        # Short pause to be polite to the public API server
        time.sleep(1)
    else:
        print(f"❌ Failed to fetch data for {name}. Status code: {response.status_code}")

print("\n--- ALL LIVE FETCHES COMPLETE ---")
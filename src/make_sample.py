import pandas as pd
import os

# Paths to raw dataset and sample CSV
RAW_FILE = os.path.join("..", "data", "raw", "default_of_credit_card_clients.xls")
SAMPLE_FILE = os.path.join("..", "data", "samples", "default_sample.csv")

# Load the full dataset
df = pd.read_excel(RAW_FILE)

# Keep the first 2 rows separately (column names + descriptions)
header_rows = df.iloc[:2]

# Randomly select 498 rows from the remaining dataset
sample_rows = df.iloc[2:].sample(498, random_state=42)

# Combine the first 2 rows with the random sample
sample_df = pd.concat([header_rows, sample_rows])

# Create the folder if it doesn't exist
os.makedirs(os.path.dirname(SAMPLE_FILE), exist_ok=True)

# Save the sample CSV
sample_df.to_csv(SAMPLE_FILE, index=False)

print(f"Sample created: {SAMPLE_FILE}")
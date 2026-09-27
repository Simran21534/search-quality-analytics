import pandas as pd
from pathlib import Path

input_path = Path("data/raw/search_interactions.csv")
df = pd.read_csv(input_path)

print("Original shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

df["result_position"] = pd.to_numeric(
    df["result_position"], errors="coerce"
)

df["clicked"] = pd.to_numeric(
    df["clicked"], errors="coerce"
)

df["dwell_time_seconds"] = pd.to_numeric(
    df["dwell_time_seconds"], errors="coerce"
)

df["num_results_viewed"] = pd.to_numeric(
    df["num_results_viewed"], errors="coerce"
)

df["session_duration"] = pd.to_numeric(
    df["session_duration"], errors="coerce"
)

df = df.dropna(
    subset=[
        "event_id",
        "user_id",
        "session_id",
        "timestamp",
        "result_position",
        "clicked"
    ]
)

df = df[
    (df["result_position"] >= 1) &
    (df["result_position"] <= 10) &
    (df["clicked"].isin([0, 1])) &
    (df["dwell_time_seconds"] >= 0) &
    (df["num_results_viewed"] >= 1) &
    (df["session_duration"] > 0)
]

output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)

output_file = output_path / "search_interactions_clean.csv"
df.to_csv(output_file, index=False)

print("\nCleaning completed successfully!")
print("Cleaned shape:", df.shape)
print("Saved to:", output_file)
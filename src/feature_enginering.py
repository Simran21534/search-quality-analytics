import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/search_interactions_clean.csv")

# 1. Short dwell-time signal
df["short_dwell_flag"] = (
    df["dwell_time_seconds"] < 15
).astype(int)

# 2. High query-reformulation signal
df["high_reformulation_flag"] = (
    df["query_reformulated"] == 1
).astype(int)

# 3. Low results-viewed signal
df["low_results_viewed_flag"] = (
    df["num_results_viewed"] <= 2
).astype(int)

# 4. Rapid interaction signal
df["rapid_interaction_flag"] = (
    df["session_duration"] < 30
).astype(int)

# 5. Behavioral risk score
df["behavior_risk_score"] = (
    df["short_dwell_flag"]
    + df["high_reformulation_flag"]
    + df["low_results_viewed_flag"]
    + df["rapid_interaction_flag"]
)
# Save feature-engineered dataset
output_path = "data/processed/search_interactions_features.csv"

df.to_csv(output_path, index=False)

print("Feature engineering completed successfully!")
print("Rows:", len(df))
print("New columns:")
print([
    "short_dwell_flag",
    "high_reformulation_flag",
    "low_results_viewed_flag",
    "rapid_interaction_flag",
    "behavior_risk_score"
])

print("\nRisk score distribution:")
print(df["behavior_risk_score"].value_counts().sort_index())
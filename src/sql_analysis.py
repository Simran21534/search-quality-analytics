import pandas as pd
import sqlite3

df = pd.read_csv("data/processed/search_interactions_clean.csv")

conn = sqlite3.connect("data/processed/search_quality.db")

df.to_sql(
    "search_interactions",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Rows:", len(df))

conn.close()

 # Run SQL Query 1
query = """
SELECT
    is_suspicious,
    COUNT(*) AS total_events
FROM search_interactions
GROUP BY is_suspicious;
"""

conn = sqlite3.connect("data/processed/search_quality.db")

result = pd.read_sql_query(query, conn)

print(result)

conn.close()

# Query 2: Click rate by behavior type

query = """
SELECT
    is_suspicious,
    ROUND(AVG(clicked), 3) AS click_rate
FROM search_interactions
GROUP BY is_suspicious;
"""

conn = sqlite3.connect("data/processed/search_quality.db")

result = pd.read_sql_query(query, conn)

print("\nClick Rate:")
print(result)

conn.close()
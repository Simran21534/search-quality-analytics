import pandas as pd
import numpy as np
import pathlib as path

np.random.seed(42)

n_events=50000
n_users=5000
n_sessions=15000

event_ids=[f"E{i:06d}" for i in range(1,n_events+1)]
user_ids=np.random.choice([f"U{i:05d}"for i in range(1,n_users+1)],n_events)
session_ids=np.random.choice([f"S{i:05d}"for i in range(1,n_sessions+1)],n_events)

queries=["weather today","python tutorial","data analytics","machine learning","sql tutorial","mathematics","excel formulas","data visualization","python pandas","google careers","data engineering","statistics tutorial","cloud computing","tableau tutorial"]
queries_text=np.random.choice(queries,n_events)

device_type=np.random.choice(["india","UK","USA","canada","australia"],n_events,p=[0.55,0.20,0.10,0.08,0.07])

result_position=np.random.randint(1,11,n_events)
clicked=np.random.binomial(1,0.55,n_events)
dwell_time=np.random.gamma(shape=2,scale=30,size=n_events).round(2)
num_results_viewed=np.random.randint(1,11,n_events)
query_reformulated=np.random.binomial(1,0.18,n_events)
session_duration=np.random.randint(20,900,n_events)

risk_score=np.random.random(n_events)
is_suspicious=(risk_score<0.08).astype(int)
suspicious_mask=is_suspicious==1
dwell_time[suspicious_mask]=np.random.uniform(1,15,suspicious_mask.sum()).round(2)
num_results_viewed[suspicious_mask]=np.random.randint(1,3,suspicious_mask.sum())
query_reformulated[suspicious_mask]=np.random.binomial(1,0.65,suspicious_mask.sum())
session_duration[suspicious_mask]=np.random.randint(10,120,suspicious_mask.sum())

timestamp=pd.date_range(start="2026-01-01",periods=n_events,freq="10min")

df= pd.DataFrame({"event_id":event_ids,"user_id":user_ids,"session_id":session_ids,"query_text":queries_text,"timestamp":timestamp,"result_position":result_position,"clicked":clicked,"dwell_time_seconds":dwell_time,"num_results_viewed":num_results_viewed,"query_reformulated":query_reformulated,"session_duration":session_duration,"country":device_type,"device_type":device_type,"is_suspicious":is_suspicious})

output_path=path.Path("data/raw")
output_path.mkdir(parents=True,exist_ok=True)

file_path=output_path/"search_interactions.csv" 
df.to_csv(file_path,index=False)

print("dataset created successfully")
print(f"Rows:{len(df)}")
print(f"Columns:{len(df.columns)}")
print(f"Saved to:{file_path}")
print("\nSuspicious vs Normal:")
print(df["is_suspicious"].value_counts())
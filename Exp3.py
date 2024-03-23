import pandas as pd
data = [
    {"JOB_ID": "AD_PRES", "JOB_TITLE": "President", "MIN_SALARY": 20080, "MAX_SALARY": 40000},
    {"JOB_ID": "AD_VP", "JOB_TITLE": "Administration Vice President", "MIN_SALARY": 15000, "MAX_SALARY": 30000}
]
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='JOB_TITLE', ascending=False)
print(sorted_df.to_string())

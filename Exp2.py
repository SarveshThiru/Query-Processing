import pandas as pd

data = [
    {"EMPLOYEE_ID": 102, "START_DATE": "2001-01-13", "END_DATE": "2006-07-24", "JOB_ID": "IT_PROG", "DEPARTMENT_ID": 60},
    {"EMPLOYEE_ID": 101, "START_DATE": "1997-09-21", "END_DATE": "2001-10-27", "JOB_ID": "AC_ACCOUNT", "DEPARTMENT_ID": 110},
    {"EMPLOYEE_ID": 101, "START_DATE": "2001-10-28", "END_DATE": "2005-03-15", "JOB_ID": "AC_MGR", "DEPARTMENT_ID": 110}
]
df = pd.DataFrame(data)
job_counts = df.groupby('EMPLOYEE_ID')['JOB_ID'].count()


multiple_jobs = job_counts[job_counts >= 2]

employee_ids = multiple_jobs.index.tolist()

print("Employee IDs with two or more jobs:")
print(employee_ids)

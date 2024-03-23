import pandas as pd

# Sample data as a list of dictionaries
data = [
    {"DEPARTMENT_ID": 10, "DEPARTMENT_NAME": "Administration", "MANAGER_ID": 200, "LOCATION_ID": 1700},
    {"DEPARTMENT_ID": 20, "DEPARTMENT_NAME": "Marketing", "MANAGER_ID": 201, "LOCATION_ID": 1800},
    {"DEPARTMENT_ID": 30, "DEPARTMENT_NAME": "Purchasing", "MANAGER_ID": 114, "LOCATION_ID": 1700},
    {"DEPARTMENT_ID": 40, "DEPARTMENT_NAME": "Human Resources", "MANAGER_ID": 203, "LOCATION_ID": 2400},
    {"DEPARTMENT_ID": 50, "DEPARTMENT_NAME": "Shipping", "MANAGER_ID": 121, "LOCATION_ID": 1500},
    {"DEPARTMENT_ID": 60, "DEPARTMENT_NAME": "IT", "MANAGER_ID": 103, "LOCATION_ID": 1400},
    {"DEPARTMENT_ID": 70, "DEPARTMENT_NAME": "Public Relations", "MANAGER_ID": 204, "LOCATION_ID": 2700}
]

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Option 1: Print all data
print("All data:")
print(df.to_string())  # Print the entire DataFrame

# Option 2: Get distinct department IDs and print corresponding data
print("\nData for departments with distinct IDs:")
distinct_departments = df['DEPARTMENT_ID'].unique()
print(df[df['DEPARTMENT_ID'].isin(distinct_departments)])

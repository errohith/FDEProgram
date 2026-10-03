employees = [
    [101, "Rohith", 300000],
    [102, "Arun", 200000],
    [103, "Karthikeyan", 220000],
    [104, "Suresh", 180000],
    [105, "Praveen", 240000]
]

for employee in employees:
    emp_id, name, salary = employee

    if len(name) > 6 and salary < 250000:
        print(name)


employees = [
    {"Employee ID": 101, "Name": "Rohith", "Salary": 200000},
    {"Employee ID": 102, "Name": "Prakash", "Salary": 240000},
    {"Employee ID": 103, "Name": "Sureshkumar", "Salary": 220000},
    {"Employee ID": 104, "Name": "Karthik", "Salary": 300000},
    {"Employee ID": 105, "Name": "Arunesh", "Salary": 180000},
    {"Employee ID": 106, "Name": "Vignesh", "Salary": 250000}
]

for employee in employees:
    if len(employee["Name"]) > 6 and employee["Salary"] < 250000:
        print(employee["Name"])
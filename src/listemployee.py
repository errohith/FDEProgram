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
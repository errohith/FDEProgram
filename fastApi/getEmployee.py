from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "John Doe", "position": "Software Engineer"},
    {"id": 2, "name": "Jane Smith", "position": "Data Scientist"},
    {"id": 3, "name": "Bob Johnson", "position": "Product Manager"},
    {"id": 4, "name": "Alice Brown", "position": "UX Designer"},
    {"id": 5, "name": "Charlie Davis", "position": "DevOps Engineer"},
    {"id": 6, "name": "Eve Wilson", "position": "QA Engineer"}
]

@app.get("/employees")
def get_employees():
    return employees    

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}
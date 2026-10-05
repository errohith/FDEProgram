
from fastapi import APIRouter
from dataStore import Employee as employees


app = APIRouter()


@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}
from fastapi import APIRouter
from dataStore import Employee as employees
from model import Employee

app = APIRouter()

@app.post("/employees")
def create_employee(employee: Employee):
    new_employee = employee.model_dump()
    employees.append(new_employee)
    return {"message": "Employee created successfully", "employee": new_employee}

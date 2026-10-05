import importlib
from fastapi import FastAPI


create_employee = importlib.import_module("01_create_Employee")
get_employee = importlib.import_module("02_get_Employee")

app = FastAPI()
app.include_router(create_employee.app)
app.include_router(get_employee.app)

from fastapi import APIRouter
from models.employee import Employee
from services.employee_service import create_employee, get_employees
from models.employee import Employee, SalaryUpdate
from services.employee_service import (
    create_employee,
    get_employees,
    get_employee_by_id,
    update_employee_salary
)
router = APIRouter()

@router.post("/employees")
def add_employee(emp: Employee):
    return create_employee(emp)
@router.get("/employees")
def list_employees():
    return get_employees()
@router.get("/employees/{emp_id}")
def search_employee(emp_id: int):
    return get_employee_by_id(emp_id)
@router.put("/employees/{emp_id}")
def update_salary(emp_id: int, data: SalaryUpdate):
    return update_employee_salary(emp_id, data.salary)
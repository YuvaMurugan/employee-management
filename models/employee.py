from pydantic import BaseModel, Field
from datetime import date


class Employee(BaseModel):
    emp_id: int
    emp_name: str
    department: str
    salary: float
    hire_date: date





class SalaryUpdate(BaseModel):
    salary: float = Field(..., gt=0)
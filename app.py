"""
Employee Management API application.
"""

from fastapi import FastAPI
from db.connection import check_connection
from routes.employee_routes import router

app = FastAPI()


@app.on_event("startup")
def startup():
    """Check database connection when application starts."""
    check_connection()


app.include_router(router)


@app.get("/")
def home():
    """Home endpoint."""
    return {
        "message": "Employee API Running"
    }
    
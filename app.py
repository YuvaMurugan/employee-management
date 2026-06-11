from fastapi import FastAPI
from db.connection import check_connection
from routes.employee_routes import router

app = FastAPI()


@app.on_event("startup")
def startup():
    check_connection()


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Employee API Running"
    }
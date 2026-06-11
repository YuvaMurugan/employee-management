from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee API Running"
    }


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200


def test_employee_not_found():
    response = client.get("/employees/99999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Employee not found"
    }
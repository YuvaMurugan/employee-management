from db.connection import get_connection
from fastapi import HTTPException

def create_employee(emp):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO EMPLOYEES
    (EMP_ID, EMP_NAME, DEPARTMENT, SALARY, HIRE_DATE)
    VALUES (:1, :2, :3, :4, :5)
    """

    cursor.execute(
        query,
        (
            emp.emp_id,
            emp.emp_name,
            emp.department,
            emp.salary,
            emp.hire_date
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Employee created successfully"
    }
def get_employees():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT EMP_ID, EMP_NAME, DEPARTMENT, SALARY, HIRE_DATE
    FROM EMPLOYEES
    ORDER BY EMP_ID
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "emp_id": row[0],
            "emp_name": row[1],
            "department": row[2],
            "salary": row[3],
            "hire_date": row[4]
        })

    cursor.close()
    conn.close()

    return employees
def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT EMP_ID, EMP_NAME, DEPARTMENT, SALARY, HIRE_DATE
    FROM EMPLOYEES
    WHERE EMP_ID = :1
    """

    cursor.execute(query, (emp_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return {
            "emp_id": row[0],
            "emp_name": row[1],
            "department": row[2],
            "salary": row[3],
            "hire_date": row[4]
        }

    raise HTTPException(
    status_code=404,
    detail="Employee not found"
)
def update_employee_salary(emp_id, salary):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE EMPLOYEES
    SET SALARY = :1
    WHERE EMP_ID = :2
    """

    cursor.execute(query, (salary, emp_id))

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
       

    conn.commit()

    cursor.execute("""
        SELECT EMP_ID, EMP_NAME, DEPARTMENT, SALARY, HIRE_DATE
        FROM EMPLOYEES
        WHERE EMP_ID = :1
    """, (emp_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "emp_id": row[0],
        "emp_name": row[1],
        "department": row[2],
        "salary": row[3],
        "hire_date": row[4]
    }
    raise HTTPException(
    status_code=404,
    detail="Employee not found"
)
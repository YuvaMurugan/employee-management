import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

# Enable Oracle Thick Mode
oracledb.init_oracle_client(
    lib_dir=r"C:\instantclient_23_0"
)


def get_connection():
    connection = oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        service_name=os.getenv("DB_SERVICE")
    )
    return connection


def check_connection():
    try:
        conn = get_connection()
        print("Oracle Database Connected Successfully")
        conn.close()

    except Exception as e:
        print("Database Connection Failed")
        print(e)
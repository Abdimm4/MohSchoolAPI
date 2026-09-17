import os
import mysql.connector


def get_connection():
    print("DEBUG MYSQLHOST:", repr(os.getenv("MYSQLHOST")))
    print("DEBUG MYSQLPORT:", repr(os.getenv("MYSQLPORT")))
    print("DEBUG MYSQLUSER:", repr(os.getenv("MYSQLUSER")))
    print("DEBUG MYSQLDATABASE:", repr(os.getenv("MYSQLDATABASE")))
    print("DEBUG ALL ENV KEYS:", [k for k in os.environ if "MYSQL" in k.upper()])

    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT", 3306)),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
    )
import os
import mysql.connector
from urllib.parse import urlparse


def get_connection():
    url = os.getenv("MYSQL_URL")

    parsed = urlparse(url)

    return mysql.connector.connect(
        host=parsed.hostname,
        port=parsed.port,
        user=parsed.username,
        password=parsed.password,
        database=parsed.path.lstrip("/")
    )
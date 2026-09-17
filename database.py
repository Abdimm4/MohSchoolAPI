def get_connection():
    url = os.getenv("MYSQL_URL")
    if url is None:
        raise RuntimeError("MYSQL_URL is not set")
    if isinstance(url, bytes):
        url = url.decode("utf-8")

    parsed = urlparse(url)

    return mysql.connector.connect(
        host=parsed.hostname,
        port=parsed.port,
        user=parsed.username,
        password=parsed.password,
        database=(parsed.path or "").lstrip("/"),
    )
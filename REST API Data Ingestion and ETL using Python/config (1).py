from sqlalchemy import create_engine
from urllib.parse import quote_plus

USERNAME = "system"
PASSWORD = quote_plus("system")
HOST = "localhost"
PORT = 1521
SERVICE_NAME = "orcl"

ENGINE = create_engine(
    f"oracle+oracledb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/?service_name={SERVICE_NAME}"
)

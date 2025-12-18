from sqlalchemy import create_engine
from urllib.parse import quote_plus

USERNAME = "SYSTEM"
PASSWORD = quote_plus("system")
HOST = "localhost"
PORT = 1521
SID = "orcle"

ENGINE = create_engine(
    f"oracle+oracledb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{SID}"
)

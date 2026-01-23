import os
from dotenv import load_dotenv
from config.schemas.database_url import ConnectionData
from config.manager import *

load_dotenv()

##client-server
CONNECTION_DATA = ConnectionData(
    USER=os.getenv("USER"),
    PASSWORD=os.getenv("PASSWORD"),
    HOST=os.getenv("HOST"),
    PORT=os.getenv("PORT"),
    DATABASE=os.getenv("DATABASE"),
    DIALECT=os.getenv("DIALECT"),
    DRIVER=os.getenv("DRIVER")
)

## embedded
# CONNECTION_DATA = ConnectionData(
#     DATABASE=os.getenv("DATABASE"),
#     DIALECT=os.getenv("DIALECT"),
# )

DATABASE_URL = CONNECTION_DATA.url_server #url_embedded

engine = init_database(
    DATABASE_URL,
    echo = False)

SessionLocal = init_session(engine, autocommit = False, autoflush = False)
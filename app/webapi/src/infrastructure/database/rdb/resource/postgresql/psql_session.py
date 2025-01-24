import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv()

PSQL_USER: str = os.environ.get("RDB_USER", 'postgres')
PSQL_PASSWORD: str = os.environ.get("RDB_PASSWORD", 'postgres')
PSQL_HOST: str = os.environ.get("RDB_HOST", 'postgres')
PSQL_PORT: str = os.environ.get("RDB_PORT", '5432')
PSQL_HOST: str = os.environ.get("RDB_HOST", 'postgres')


RDB_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(PSQL_USER, PSQL_PASSWORD, PSQL_HOST, PSQL_PORT, PSQL_HOST)
ENGINE = create_engine(RDB_URL, echo = False)

session_local = scoped_session(
    sessionmaker(
        autocommit = False,
        expire_on_commit = False,
        autoflush = True,
        bind = ENGINE
        )
    )

def get_psql_session():
    try:
        session = session_local()
        yield session

    finally:
        session.close()
    


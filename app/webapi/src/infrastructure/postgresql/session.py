import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv()

PSQL_USER: str = os.environ.get("POSTGRES_USER", 'postgres')
PSQL_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", 'postgres')
PSQL_HOST: str = os.environ.get("POSTGRES_HOST", 'postgres')
PSQL_PORT: str = os.environ.get("POSTGRES_PORT", '5432')
PSQL_DB: str = os.environ.get("POSTGRES_DB", 'postgres')


PSQL_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(PSQL_USER, PSQL_PASSWORD, PSQL_HOST, PSQL_PORT, PSQL_DB)
ENGINE = create_engine(PSQL_URL, echo = False)

session_local = scoped_session(
    sessionmaker(
        autocommit = False,
        expire_on_commit = False,
        autoflush = True,
        bind = ENGINE
        )
    )

def get_rdb_session():
    try:
        session = session_local()
        yield session

    finally:
        session.close()
    


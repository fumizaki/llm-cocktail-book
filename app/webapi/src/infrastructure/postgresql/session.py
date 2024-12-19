import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv()

RDB_USER: str = os.environ.get("RDB_USER", 'postgres')
RDB_PASSWORD: str = os.environ.get("RDB_PASSWORD", 'postgres')
RDB_HOST: str = os.environ.get("RDB_HOST", 'postgres')
RDB_PORT: str = os.environ.get("RDB_PORT", '5432')
RDB_DB: str = os.environ.get("RDB_DB", 'postgres')


RDB_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(RDB_USER, RDB_PASSWORD, RDB_HOST, RDB_PORT, RDB_DB)
ENGINE = create_engine(RDB_URL, echo = False)

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
    


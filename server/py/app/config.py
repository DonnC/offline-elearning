import os

from sqlmodel import  SQLModel
from sqlmodel import create_engine

ROOT_DIR = "database"
SQLITE_DB_NAME = "hero_test.db"

DB_FILE_PATH = os.path.join(ROOT_DIR, SQLITE_DB_NAME)

DB_URL = f"sqlite:///{SQLITE_DB_NAME}"

def get_engine():
    connect_args = {"check_same_thread": False}
    
    engine = create_engine(DB_URL, echo=True, connect_args=connect_args)

    return engine

def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())


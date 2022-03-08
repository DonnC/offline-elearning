from fastapi import Header, HTTPException
from sqlmodel import  Session

from app.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    
    try:
        yield db

    finally:
        db.close()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    if token != "donnc":
        raise HTTPException(status_code=400, detail="No DonnC token provided")

def hash_password(password: str):
    '''
        TODO use proper password hashing
        hash user password
    '''
    return password + "notreallyhashed"
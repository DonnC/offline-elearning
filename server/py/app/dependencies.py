from fastapi import Header, HTTPException
from sqlmodel import  Session

from app.config import get_engine

engine = get_engine()

def get_session():
    with Session(engine) as session:
        yield session

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    if token != "donnc":
        raise HTTPException(status_code=400, detail="No DonnC token provided")

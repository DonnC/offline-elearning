from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_session
from app.models.models import *

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/teams",
    tags=["teams"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=TeamRead)
async def create_team(*, session: Session = Depends(get_session), team: TeamCreate):
    db_team = Team.from_orm(team)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    
    return db_team

@router.get("/", response_model=List[TeamRead])
async def read_teams(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    teams = session.exec(select(Team).offset(offset).limit(limit)).all()

    return teams


@router.get("/{team_id}", response_model=TeamReadWithHeroes)
async def read_team(*, session: Session = Depends(get_session), team_id: int):
    team = session.get(Team, team_id)
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    return team


@router.patch("/{team_id}", response_model=TeamRead)
async def update_team(
    *, session: Session = Depends(get_session), team_id: int, team: TeamUpdate
):
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    team_data = team.dict(exclude_unset=True)
    
    for key, value in team_data.items():
        setattr(db_team, key, value)
    
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    
    return db_team


@router.delete("/{team_id}")
async def delete_team(*, session: Session = Depends(get_session), team_id: int):
    team = session.get(Team, team_id)

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    session.delete(team)
    session.commit()
    
    return {
        "ok": True
    }



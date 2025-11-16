from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.player import Player
from src.shemas.player import PlayerCreate, PlayerFromDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PlayerFromDB:
    query = select(Player).where(Player.uid == uid)
    query_Player = await db_session.execute(query)
    player = query_Player.scalar()
    return player

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[PlayerFromDB]:
    query = select(Player)
    result = await db_session.execute(query)
    player = result.scalars().all()
    return [player for player in player]

@router.put('/')
async def update(body: PlayerFromDB, db_session: AsyncSession = Depends(get_session)) ->PlayerFromDB:
    query = await db_session.execute(select(Player).where(Player.uid == body.uid))
    player_obj = query.scalar()
    if player_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(player_obj, key, value)
        await db_session.commit()
        await db_session.refresh(player_obj)
    return player_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PlayerFromDB:
    query = select(Player).where(Player.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: PlayerCreate, db_session: AsyncSession = Depends(get_session)) -> PlayerFromDB:
    item_obj = Player(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
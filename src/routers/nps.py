from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.nps import Nps
from src.shemas.nps import NPSCreate, NPSFromDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> NPSFromDB:
    query = select(Nps).where(Nps.uid == uid)
    query_nps = await db_session.execute(query)
    nps = query_nps.scalar()
    return nps

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[NPSFromDB]:
    query = select(Nps)
    result = await db_session.execute(query)
    nps_ = result.scalars().all()
    return [nps_ for nps_ in nps_]

@router.put('/')
async def update(body: NPSFromDB, db_session: AsyncSession = Depends(get_session)) ->NPSFromDB:
    query = await db_session.execute(select(Nps).where(Nps.uid == body.uid))
    Nps_obj = query.scalar()
    if Nps_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(Nps_obj, key, value)
        await db_session.commit()
        await db_session.refresh(Nps_obj)
    return Nps_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> NPSFromDB:
    query = select(Nps).where(Nps.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: NPSCreate, db_session: AsyncSession = Depends(get_session)) -> NPSFromDB:
    item_obj = Nps(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
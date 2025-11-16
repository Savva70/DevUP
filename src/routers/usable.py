from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models.usable import Usable
from src.shemas.usable import UsableFromBD, UsableCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> UsableFromBD:
    query = select(Usable).where(Usable.uid == uid)
    query_Usable = await db_session.execute(query)
    usable = query_Usable.scalar()
    return usable

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[UsableFromBD]:
    query = select(Usable)
    result = await db_session.execute(query)
    usable_ = result.scalars().all()
    return [usable_ for usable_ in usable_]

@router.put('/')
async def update(body: UsableFromBD, db_session: AsyncSession = Depends(get_session)) ->UsableFromBD:
    query = await db_session.execute(select(Usable).where(Usable.uid == body.uid))
    Usable_obj = query.scalar()
    if Usable_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(Usable_obj, key, value)
        await db_session.commit()
        await db_session.refresh(Usable_obj)
    return Usable_obj

@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Usable).where(Usable.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: UsableCreate, db_session: AsyncSession = Depends(get_session)) -> UsableFromBD:
    item_obj = Usable(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models.enchatmens import Enchantmens
from src.shemas.enchatmens import EnchatmentsFromDB,EnchatmentsCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> EnchatmentsFromDB:
    query = select(Enchantmens).where(Enchantmens.uid == uid)
    query_Enchatments = await db_session.execute(query)
    Armor = query_Enchatments.scalar()
    return Armor

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[EnchatmentsFromDB]:
    query = select(Enchantmens)
    result = await db_session.execute(query)
    enchatments = result.scalars().all()
    return [enchatments for enchatments in enchatments]

@router.put('/')
async def update(body: EnchatmentsFromDB, db_session: AsyncSession = Depends(get_session)) ->EnchatmentsFromDB:
    query = await db_session.execute(select(Enchantmens).where(Enchantmens.uid == body.uid))
    enchatments_obj = query.scalar()
    if enchatments_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(enchatments_obj, key, value)
        await db_session.commit()
        await db_session.refresh(enchatments_obj)
    return enchatments_obj
@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Enchantmens).where(Enchantmens.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: EnchatmentsCreate, db_session: AsyncSession = Depends(get_session)) -> EnchatmentsFromDB:
    item_obj = Enchantmens(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj


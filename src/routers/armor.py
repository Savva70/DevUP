from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.armor import Armor
from src.shemas.armor import ArmorCreate, ArmorFromDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ArmorFromDB:
    query = select(Armor).where(Armor.uid == uid)
    query_armor = await db_session.execute(query)
    Armor = query_armor.scalar()
    return Armor

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ArmorFromDB]:
    query = select(Armor)
    result = await db_session.execute(query)
    armors = result.scalars().all()
    return [armors for armors in armors]

@router.put('/')
async def update(body: ArmorFromDB, db_session: AsyncSession = Depends(get_session)) -> ArmorFromDB:
    query = await db_session.execute(select(Armor).where(Armor.uid == body.uid))
    armor_obj = query.scalar()
    if armor_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(armor_obj, key, value)
        await db_session.commit()
        await db_session.refresh(armor_obj)
    return armor_obj

@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Armor).where(Armor.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: ArmorCreate, db_session: AsyncSession = Depends(get_session)) -> ArmorFromDB:
    item_obj = Armor(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
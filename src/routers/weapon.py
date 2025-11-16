from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models.weapon import Weapon
from src.shemas.weapon import WeaponFromDB, WeaponCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> WeaponFromDB:
    query = select(Weapon).where(Weapon.uid == uid)
    query_Weapon = await db_session.execute(query)
    weapon = query_Weapon.scalar()
    return weapon

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WeaponFromDB]:
    query = select(Weapon)
    result = await db_session.execute(query)
    weapon_ = result.scalars().all()
    return [weapon_ for weapon_ in weapon_]

@router.put('/')
async def update(body: WeaponFromDB, db_session: AsyncSession = Depends(get_session)) ->WeaponFromDB:
    query = await db_session.execute(select(Weapon).where(Weapon.uid == body.uid))
    Weapon_obj = query.scalar()
    if Weapon_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(Weapon_obj, key, value)
        await db_session.commit()
        await db_session.refresh(Weapon_obj)
    return Weapon_obj

@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Weapon).where(Weapon.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: WeaponCreate, db_session: AsyncSession = Depends(get_session)) -> WeaponFromDB:
    item_obj = Weapon(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
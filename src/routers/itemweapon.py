from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.itemweapon import ItemWeapon
from src.shemas.itemweapon import ItemWeaponCreate, ItemWeaponDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemWeaponDB:
    query = select(ItemWeapon).where(ItemWeapon.uid == uid)
    query_ItemWeapon = await db_session.execute(query)
    Armor = query_ItemWeapon.scalar()
    return Armor

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ItemWeaponDB]:
    query = select(ItemWeapon)
    result = await db_session.execute(query)
    itemWeapon = result.scalars().all()
    return [itemWeapon for itemWeapon in itemWeapon]

@router.put('/')
async def update(body: ItemWeaponDB, db_session: AsyncSession = Depends(get_session)) ->ItemWeaponDB:
    query = await db_session.execute(select(ItemWeapon).where(ItemWeapon.uid == body.uid))
    ItemWeapon_obj = query.scalar()
    if ItemWeapon_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(ItemWeapon_obj, key, value)
        await db_session.commit()
        await db_session.refresh(ItemWeapon_obj)
    return ItemWeapon_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemWeaponDB:
    query = select(ItemWeapon).where(ItemWeapon.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: ItemWeaponCreate, db_session: AsyncSession = Depends(get_session)) -> ItemWeaponDB:
    item_obj = ItemWeapon(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj

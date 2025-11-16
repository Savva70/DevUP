from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.itemarmor import ItemArmor
from src.shemas.itemarmor import ItemArmorCreate, ItemArmorDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemArmorDB:
    query = select(ItemArmor).where(ItemArmor.uid == uid)
    query_ItemArmor = await db_session.execute(query)
    ItemArmor = query_ItemArmor.scalar()
    return ItemArmor

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ItemArmorDB]:
    query = select(ItemArmor)
    result = await db_session.execute(query)
    itemArmor = result.scalars().all()
    return [itemArmor for itemArmor in itemArmor]

@router.put('/')
async def update(body: ItemArmorDB, db_session: AsyncSession = Depends(get_session)) ->ItemArmorDB:
    query = await db_session.execute(select(ItemArmor).where(ItemArmor.uid == body.uid))
    ItemArmor_obj = query.scalar()
    if ItemArmor_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(ItemArmor_obj, key, value)
        await db_session.commit()
        await db_session.refresh(ItemArmor_obj)
    return ItemArmor_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemArmorDB:
    query = select(ItemArmor).where(ItemArmor.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: ItemArmorCreate, db_session: AsyncSession = Depends(get_session)) -> ItemArmorDB:
    item_obj = ItemArmor(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj

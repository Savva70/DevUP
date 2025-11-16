from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.item import Item
from src.shemas.item import ItemCreate, ItemFromDB

router = APIRouter()



@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemFromDB:
    query = select(Item).where(Item.uid == uid)
    query_item = await db_session.execute(query)
    item = query_item.scalar()
    return item


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ItemFromDB]:
    query = select(Item)
    result = await db_session.execute(query)
    clients = result.scalars().all()
    return [client for client in clients]


@router.post('/')
async def create(body: ItemCreate, db_session: AsyncSession = Depends(get_session)) -> ItemFromDB:
    item_obj = Item(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj


@router.put('/')
async def update(body: ItemFromDB, db_session: AsyncSession = Depends(get_session)) -> ItemFromDB:
    query = await db_session.execute(select(Item).where(Item.uid == body.uid))
    item_obj = query.scalar()
    if item_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(item_obj, key, value)
        await db_session.commit()
        await db_session.refresh(item_obj)
    return item_obj


# Заменить на put запрос archivate
@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Item).where(Item.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l


# Расставить такие блоки там где нужно
@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ItemFromDB:
    query = select(Item).where(Item.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj




   
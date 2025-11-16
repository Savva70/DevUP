from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models.usableitem import UsableItem
from src.shemas.usableitem import UsableItemFromDB, UsableItemCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> UsableItemFromDB:
    query = select(UsableItem).where(UsableItem.uid == uid)
    query_UsableItem = await db_session.execute(query)
    usableItem = query_UsableItem.scalar()
    return usableItem

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[UsableItemFromDB]:
    query = select(UsableItem)
    result = await db_session.execute(query)
    UsableItems = result.scalars().all()
    return [UsableItems for UsableItems in UsableItems]

@router.put('/')
async def update(body: UsableItemFromDB, db_session: AsyncSession = Depends(get_session)) ->UsableItemFromDB:
    query = await db_session.execute(select(UsableItem).where(UsableItem.uid == body.uid))
    UsableItem_obj = query.scalar()
    if UsableItem_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(UsableItem_obj, key, value)
        await db_session.commit()
        await db_session.refresh(UsableItem_obj)
    return UsableItem_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> UsableItemFromDB:
    query = select(UsableItem).where(UsableItem.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: UsableItemCreate, db_session: AsyncSession = Depends(get_session)) -> UsableItemFromDB:
    item_obj = UsableItem(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
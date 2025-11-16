from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models.property import Property
from src.shemas.property import PropertyDB, PropertyCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PropertyDB:
    query = select(Property).where(Property.uid == uid)
    query_item = await db_session.execute(query)
    property_ = query_item.scalar()
    return property_

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[PropertyDB]:
    query = select(Property)
    result = await db_session.execute(query)
    _property = result.scalars().all()
    return [_property for _property in _property]

@router.put('/')
async def update(body: PropertyDB, db_session: AsyncSession = Depends(get_session)) ->PropertyDB:
    query = await db_session.execute(select(Property).where(Property.uid == body.uid))
    Property_obj = query.scalar()
    if Property_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(Property_obj, key, value)
        await db_session.commit()
        await db_session.refresh(Property_obj)
    return Property_obj

@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Property).where(Property.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: PropertyCreate, db_session: AsyncSession = Depends(get_session)) -> PropertyDB:
    item_obj = Property(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
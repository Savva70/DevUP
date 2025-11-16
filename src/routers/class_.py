from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.db.session import get_session
from src.models._class import Class
from src.shemas.__class import ClassFromDB, ClassCreate

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClassFromDB:
    query = select(Class).where(Class.uid == uid)
    query_class = await db_session.execute(query)
    Class = query_class.scalar()
    return Class

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ClassFromDB]:
    query = select(Class)
    result = await db_session.execute(query)
    class_ = result.scalars().all()
    return [class_ for class_ in class_]

@router.put('/')
async def update(body: ClassFromDB, db_session: AsyncSession = Depends(get_session)) ->ClassFromDB:
    query = await db_session.execute(select(Class).where(Class.uid == body.uid))
    class_obj = query.scalar()
    if class_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(class_obj, key, value)
        await db_session.commit()
        await db_session.refresh(class_obj)
    return class_obj

@router.delete('/')
async def _delete(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    query = delete(Class).where(Class.uid == uid)
    l = await db_session.execute(query)
    await db_session.commit()
    return l

@router.post('/')
async def create(body: ClassCreate, db_session: AsyncSession = Depends(get_session)) -> ClassFromDB:
    item_obj = Class(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj

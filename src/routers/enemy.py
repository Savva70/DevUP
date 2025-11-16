from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.models.enemy import Enemy
from src.shemas.enemy import EnemyCreate, EnemyFromDB

router = APIRouter()

@router.get('/')
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> EnemyFromDB:
    query = select(Enemy).where(Enemy.uid == uid)
    query_enemy = await db_session.execute(query)
    enemy = query_enemy.scalar()
    return enemy

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[EnemyFromDB]:
    query = select(Enemy)
    result = await db_session.execute(query)
    enemys = result.scalars().all()
    return [enemys for enemys in enemys]

@router.put('/')
async def update(body: EnemyFromDB, db_session: AsyncSession = Depends(get_session)) ->EnemyFromDB:
    query = await db_session.execute(select(Enemy).where(Enemy.uid == body.uid))
    enemy_obj = query.scalar()
    if enemy_obj:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(enemy_obj, key, value)
        await db_session.commit()
        await db_session.refresh(enemy_obj)
    return enemy_obj

@router.put('/archivate')
async def archivate(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> EnemyFromDB:
    query = select(Enemy).where(Enemy.uid == uid)
    query_obj = (await db_session.execute(query)).scalar()
    if query_obj:
        setattr(query_obj, 'archivate', not query_obj.archivate)
        await db_session.commit()
        await db_session.refresh(query_obj)
    return query_obj

@router.post('/')
async def create(body: EnemyCreate, db_session: AsyncSession = Depends(get_session)) -> EnemyFromDB:
    item_obj = Enemy(**body.model_dump(exclude_unset=True))
    db_session.add(item_obj)
    await db_session.commit()
    return item_obj
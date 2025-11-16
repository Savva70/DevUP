from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

engine = create_async_engine(url=settings.DB.SQLALCHEMY_DATABASE_URI, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
Base = declarative_base()

async def get_session() -> AsyncSession: # type: ignore
    async with async_session() as session:
        yield session

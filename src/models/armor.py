import uuid

from sqlalchemy import UUID, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Armor(Base):
    __tablename__ = 'armor'
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type:Mapped[str] =  mapped_column(String(255), nullable=False)
    rare:Mapped[str] =  mapped_column(String(255), nullable=False)
    defense:Mapped[int] =  mapped_column(Integer, nullable=False)
    price:Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(255),nullable=False)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)

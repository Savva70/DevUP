import uuid

from sqlalchemy import UUID, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Weapon(Base):
    __tablename__ = 'weapon'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type:Mapped[str] =  mapped_column(String(255), nullable=False)
    rare:Mapped[str] =  mapped_column(String(255), nullable=False)
    defense:Mapped[int] =  mapped_column(Integer, default=0)
    price:Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[str] = mapped_column(String(255),nullable=True)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
    
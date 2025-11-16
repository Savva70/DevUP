import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Property(Base):
    __tablename__ = 'property'
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    hp: Mapped[int] = mapped_column(Integer,default=100)
    defence: Mapped[int] = mapped_column(Integer,default=0)
    ManaPull: Mapped[int] = mapped_column(Integer,default=100)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
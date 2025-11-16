import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Usable(Base):
    __tablename__ = 'usable'
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    type:Mapped[str] =  mapped_column(String(255), nullable=False)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
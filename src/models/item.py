import uuid

from sqlalchemy import UUID, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Item(Base):
    __tablename__ = 'items'
    
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    archivate: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

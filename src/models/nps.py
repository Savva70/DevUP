import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class Nps(Base):
    
    __tablename__ = 'nps'
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    item_uid:Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("items.uid"), default=None)
    class_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("class.uid"), default=None)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
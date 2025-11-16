import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class UsableItem(Base):
    __tablename__ = 'usable_item'
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    weapon_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("usable.uid"), default=None)
    item_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("items.uid"), default=None)
    count:Mapped[int] = mapped_column(Integer, default=1)
    rare: Mapped[str] = mapped_column(String, default=None, nullable=True)
    usable_locate:Mapped[str] = mapped_column(String, default=None, nullable=True)
    eatable:Mapped[str] = mapped_column(String, default=None, nullable=True)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)

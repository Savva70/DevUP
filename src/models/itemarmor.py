import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class ItemArmor(Base):
    __tablename__ = 'items_armor'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    armor_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("armor.uid"), default=None)
    item_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("items.uid"), default=None)
    enchatmens_uid:Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("enchantmens.uid"), default=None)
    count:Mapped[int] = mapped_column(Integer, nullable=False)
    strength:Mapped[int] = mapped_column(Integer, nullable=True)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
    
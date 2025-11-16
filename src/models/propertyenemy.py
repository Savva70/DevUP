import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class PropertyEnemy(Base):
    __tablename__ = 'property_enemy'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    property_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("property.uid"), default=None)
    enemy_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("enemy.uid"), default=None)
    count:Mapped[int] = mapped_column(Integer, nullable=False)
    strength:Mapped[int] = mapped_column(Integer, nullable=True)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
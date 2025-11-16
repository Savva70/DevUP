import uuid

from sqlalchemy import UUID, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.session import Base


class PropertyNps(Base):
    __tablename__ = 'property_nps'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    property_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("property.uid"), default=None)
    nps_uid_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("nps.uid"), default=None)
    count:Mapped[int] = mapped_column(Integer, nullable=False)
    strength:Mapped[int] = mapped_column(Integer, nullable=True)
    archivate:Mapped[bool] = mapped_column(Boolean, nullable=False)
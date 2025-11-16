from pydantic import UUID4, BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(
        description="Название инвентаря",
    )
    archivate: bool = False


class ItemFromDB(BaseModel):
    uid: UUID4 = Field(
        description="UID инвентаря",
        default=None     
    )
    name: str = Field(
        description="Название инвентаря"
    )
    archivate: bool = False

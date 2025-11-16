from pydantic import UUID4, BaseModel, Field


class NPSCreate(BaseModel):
    name: str = Field(
         description='Имя NPS',
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у NPS',
        default=None
    )


class NPSFromDB(BaseModel):
    uid: UUID4 = Field(
        description='UID NPS',
        default=None
    )
    name: str = Field(
        description='Имя NPS',
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у NPS',
        default=None
    )
    class_uid: UUID4 | None = Field(
        description='Класс у Nps',
        default=None
    )

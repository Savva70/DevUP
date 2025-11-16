from pydantic import UUID4, BaseModel, Field


class PlayerFromDB(BaseModel):
    uid: UUID4 = Field(
        description= 'UID игрока',
        default=None
    )
    name: str = Field(
        description='Имя игрока'
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у игрока',
        default=None
    )


class PlayerCreate(BaseModel):
    name: str = Field(
        description='Имя игрока',
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у игрока',
        default=None
    )
    class_uid:  UUID4 | None = Field(
        description='Класс у игрока',
        default=None
    )

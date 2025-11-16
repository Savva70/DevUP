from pydantic import UUID4, BaseModel, Field


class EnemyCreate(BaseModel):
    name:str = Field(
        description='Имя врага',
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у зачарования',
        default=None
    )

class EnemyFromDB(BaseModel):
    uid: UUID4 = Field(
        description= 'UID врага',
        default=None
    )
    name:str = Field(
        description='Имя врага',
    )
    item_uid: UUID4 | None = Field(
        description='Название предмета у зачарования',
        default=None
    )
    class_uid:  UUID4 | None = Field(
        description='Класс у врага',
        default=None
    )


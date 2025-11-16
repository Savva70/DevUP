from pydantic import UUID4, BaseModel, Field


class ArmorFromDB(BaseModel):
    uid: UUID4 = Field(
            description='UID брони',
            default=None
        )
    name:str = Field(
        description='Название брони',
    )
    type: str | None= Field(
        description='Тип брони',
    )
    rare: str = Field(
        description='Редкость брони',
    )
    defense: int = Field(
        description='Значение брони',
    )
    price: int = Field(
        description='Цена брони',
    )
    dicscription: str = Field(
        description='Описание брони'
    )
class ArmorCreate(BaseModel):
    name:str = Field(
        description='Название брони',
    )
    type: str | None= Field(
        description='Тип брони',
    )
    rare: str = Field(
        description='Редкость брони',
    )
    defense: int = Field(
        description='Значение брони',
    )
    price: int = Field(
        description='Цена брони',
    )
    dicscription: str = Field(
        description='Описание брони'
    )
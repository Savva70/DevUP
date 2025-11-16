from pydantic import UUID4, BaseModel, Field


class WeaponFromDB(BaseModel):
    uid: UUID4 = Field(
        description='UID брони',
        default=None
    )
    name: str = Field(
        description='Название оружия'
    )
    type: str = Field(
        description='Тип оружия'
    )
    rare: str = Field(
        description='Редкость оружия'
    )
    defense: int = Field(
        description='Значение оружия'
    )
    price: int = Field(
        description='Цена оружия'
    )
    description: str = Field(
        description='Описание оружия'
    )


class WeaponCreate(BaseModel):
    name: str = Field(
        description='Название оружия'
    )
    description: str = Field(
        description='Описание оружия'
    )
    type: str = Field(
        description='Тип оружия'
    )
    rare: str = Field(
        description='Редкость оружия'
    )
    defense: int = Field(
        description='Значение оружия'
    )
    price: int = Field(
        description='Цена оружия'
    )

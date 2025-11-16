from pydantic import UUID4, BaseModel, Field


class PropertyDB(BaseModel):
    uid: UUID4 = Field(
        description= 'UID Характеристики'
    )
    hp: int = Field(
        description='Здоровье'
    )
    defence: int = Field(
        description='Защита'
    )
    ManaPull: int = Field(
        description= 'Обьём манны'
    )


class PropertyCreate(BaseModel):
    hp: int = Field(
        description='Здоровье',
        default=100
    )
    defence: int = Field(
        description='Защита',
        default=0
    )
    ManaPull: int = Field(
        description= 'Обьём манны',
        default=0
    )

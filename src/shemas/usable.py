from pydantic import UUID4, BaseModel, Field


class UsableFromBD(BaseModel):
    uid: UUID4 = Field(
        description='UID Используемые',
        default=None
    )
    name: str = Field(
        description='Название используемого предмета',
    )
    type: str = Field(
        description='Тип использунемого предмета'
    )


class UsableCreate(BaseModel):
    name: str = Field(
        description='Название используемого предмета',
    )
    type: str | None= Field(
        description='Тип использунемого предмета'
    )


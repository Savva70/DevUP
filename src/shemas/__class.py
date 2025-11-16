from pydantic import UUID4, BaseModel, Field


class ClassFromDB(BaseModel):
    uid: UUID4 = Field(
        description= 'UID класса',
        default=None
    )
    name:str = Field(
        description='Имя класса',
    )

class ClassCreate(BaseModel):
    name:str = Field(
        description='Имя класса',
    )

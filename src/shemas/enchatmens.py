from pydantic import UUID4, BaseModel, Field


class EnchatmentsFromDB(BaseModel):
    uid: UUID4 = Field(
        description='UID зачарования',
        default=None
    )
    name:str = Field(description='Название зачарования')
    type: str | None = Field(
        description='Тип зачарования',
        default=None
    )
class EnchatmentsCreate(BaseModel):
    name:str = Field(
        description='Название зачарования'
    )

from pydantic import UUID4, BaseModel, Field


class UsableItemFromDB(BaseModel):
    uid: UUID4 = Field(
        description='UID UsableItem',
        default=None
    )
    weapon_id:UUID4 = Field(
        description='UID weapon',
        default=None
    )
    item_uid:UUID4 = Field(
        description='UID item',
        default=None
    )
    count:int= Field(
        description='Количество',
        default=None
    )
    rare:str = None
    usable_locate:str = Field(
        default=None
    )
    eatable:str=Field(
        description= 'Еда',
        default=None
    )
    
class UsableItemCreate(BaseModel):
    weapon_id:UUID4 = Field(
        description='UID weapon',
        default=None
    )
    item_uid:UUID4 = Field(
        description='UID item',
        default=None
    )
    count:int= Field(
        description='Количество',
        default=None
    )
    rare:str = None
    usable_locate:str = Field(
        default=None
    )
    eatable:str=Field(
        description= 'Еда',
        default=None
    )
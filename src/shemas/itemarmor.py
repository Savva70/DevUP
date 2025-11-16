from pydantic import UUID4, BaseModel, Field

class ItemArmorDB(BaseModel):
    uid: UUID4 = Field(
        description='UID ItemArmor',
        default=None
    )
    armor_id:UUID4 = Field(
        description='UID armor',
        default=None
    )
    item_uid:UUID4 = Field(
        description='UID item',
        default=None
    )
    enchatmens_uid:UUID4 = Field(
        description='UID enchatmens',
        default=None
    )
    count:int= Field(
        description='Количество',
        default=None
    )
    strength:int=Field(
        description='Качество',
        default=None
    )
 

class ItemArmorCreate(BaseModel):
    armor_id:UUID4 = Field(
        description='UID armor',
        default=None
    )
    item_uid:UUID4 = Field(
        description='UID item',
        default=None
    )
    enchatmens_uid:UUID4 = Field(
        description='UID enchatmens',
        default=None
    )
    count:int= Field(
        description='Количество',
        default=None
    )
    strength:int=Field(
        description='Качество',
        default=None
    )
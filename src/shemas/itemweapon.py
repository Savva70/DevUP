from pydantic import UUID4, BaseModel, Field

class ItemWeaponDB(BaseModel):
    uid: UUID4 = Field(
        description='UID ItemWeapon',
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
class ItemWeaponCreate(BaseModel):
    weapon_id:UUID4 = Field(
        description='UID weapon',
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
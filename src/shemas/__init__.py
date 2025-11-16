from datetime import date

from pydantic import UUID4, BaseModel, Field, computed_field


class StaffCreate(BaseModel):
    # Строковые значения
    full_name: str = Field(
        description="ФИО"
    )
    gmail: str = Field(
        description="Адрес электронной почты"
    )
    phone_number: str = Field(
        description="Номер телефона"
    )
    description: str | None = Field(
        description="Описание",
        default=None
    )
    github: str | None = Field(
        description="Ссылка на GitHub",
        default=None
    )
    gitlab: str | None = Field(
        description="Ссылка на GitLab",
        default=None
    )
    telegram: str | None = Field(
        description="Телеграм ссылка",
        default=None
    )
    where_did_come: str | None = Field(
        description="Откуда пришёл сотрудник",
        default=None
    )
    # Значения - даты
    first_appearance: date | None = Field(
        description="Первое появление",
        default=None
    )
    birthdate: date | None = Field(
        description="Дата рождения",
        default=None
    )
    # Булевое значение
    is_archive: bool = Field(
        description="Архивный",
        default=False
    )


class FilterStaff(BaseModel):
    limit: int = Field(
        description="Лимит вывода записей",
        default=-1,
        ge=-1
    )
    offset: int = Field(
        description="Смещение вывода записей",
        default=0,
        ge=0
    )
    # Проверка входимости подстроки во все строковые значения
    search_query: str | None = Field(
        description="Подстрока имеется в строковых значениях",
        default=None
    )
    # Фильтрация дат первого появления (От - До)
    appearence_from: date | None = Field(
        description="Дата появления от",
        default=None
    )
    appearence_to: date | None = Field(
        description="Дата появления до",
        default=None
    )
    # Фильтрация дат рождения (От - До)
    birthdate_from: date | None = Field(
        description="Дата рождения от",
        default=None
    )
    birthdate_to: date | None = Field(
        description="Дата рождения до",
        default=None
    )
    # Булевые значения
    is_archive: bool | None = Field(
        description="Имеется в архиве",
        default=None
    )
    


class DBStaff(BaseModel):
    # UID значения
    uid: UUID4 = Field(
        description="UID сотрудника",
        default=None
    )
    # Строковые значения
    full_name: str = Field(
        description="ФИО"
    )
    gmail: str = Field(
        description="Адрес электронной почты"
    )
    phone_number: str = Field(
        description="Номер телефона"
    )
    description: str | None = Field(
        description="Описание",
        default=None
    )
    github: str | None = Field(
        description="Ссылка на GitHub",
        default=None
    )
    gitlab: str | None = Field(
        description="Ссылка на GitLab",
        default=None
    )
    telegram: str | None = Field(
        description="Телеграм ссылка",
        default=None
    )
    where_did_come: str | None = Field(
        description="Откуда пришёл сотрудник",
        default=None
    )
    # Значения - даты
    first_appearance: date | None = Field(
        description="Первое появление",
        default=None
    )
    birthdate: date | None = Field(
        description="Дата рождения",
        default=None
    )
    # Булевые значения
    is_archive: bool = Field(
        description="Архивный",
        default=False
    )

    # Вычисляемые поля
    @computed_field
    def age(self) -> int | None:
        if self.birthdate is None:
            return None

        today = date.today()
        years_diff = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            years_diff -= 1
        return years_diff

    class Config:
        from_attributes = True

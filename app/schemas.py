# #schemas.py

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class TaskShiftBase(BaseModel):
    status: bool = Field(alias="СтатусЗакрытия")
    task_description: str = Field(alias="ПредставлениеЗаданияНаСмену")
    work_center: str = Field(alias="РабочийЦентр")
    shift: str = Field(alias="Смена")
    brigade: str = Field(alias="Бригада")
    batch_number: int = Field(alias="НомерПартии")
    batch_date: date = Field(alias="ДатаПартии")
    product_name: str = Field(alias="Номенклатура")
    ecn_code: str = Field(alias="КодЕКН")
    rc_identifier: str = Field(alias="ИдентификаторРЦ")
    start_time: datetime = Field(alias="ДатаВремяНачалаСмены")
    end_time: datetime = Field(alias="ДатаВремяОкончанияСмены")
    closed_at: Optional[datetime] = None

    class Config:
        fields = {
            "СтатусЗакрытия": "status",
            "ПредставлениеЗаданияНаСмену": "task_description",
            "РабочийЦентр": "work_center",
            "Смена": "shift",
            "Бригада": "brigade",
            "НомерПартии": "batch_number",
            "ДатаПартии": "batch_date",
            "Номенклатура": "product_name",
            "КодЕКН": "ecn_code",
            "ИдентификаторРЦ": "rc_identifier",
            "ДатаВремяНачалаСмены": "start_time",
            "ДатаВремяОкончанияСмены": "end_time"
        }

    @classmethod
    def from_orm(cls, obj):
        return cls(**obj.__dict__)


class TaskShiftCreate(TaskShiftBase):
    СтатусЗакрытия: bool
    ПредставлениеЗаданияНаСмену: str
    РабочийЦентр: str
    Смена: str
    Бригада: str
    НомерПартии: int
    ДатаПартии: date
    Номенклатура: str
    КодЕКН: str
    ИдентификаторРЦ: str
    ДатаВремяНачалаСмены: datetime
    ДатаВремяОкончанияСмены: datetime

    class Config:
        fields = {
            "СтатусЗакрытия": "status",
            "ПредставлениеЗаданияНаСмену": "task_description",
            "РабочийЦентр": "work_center",
            "Смена": "shift",
            "Бригада": "brigade",
            "НомерПартии": "batch_number",
            "ДатаПартии": "batch_date",
            "Номенклатура": "product_name",
            "КодЕКН": "ecn_code",
            "ИдентификаторРЦ": "rc_identifier",
            "ДатаВремяНачалаСмены": "start_time",
            "ДатаВремяОкончанияСмены": "end_time"
        }


class TaskShiftUpdate(BaseModel):
    status: Optional[bool]
    task_description: Optional[str]
    work_center: Optional[str]
    shift: Optional[str]
    brigade: Optional[str]
    batch_number: Optional[int]
    batch_date: Optional[date]
    product_name: Optional[str]
    ecn_code: Optional[str]
    rc_identifier: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    closed_at: Optional[datetime]

    class Config:
        fields = {
            "СтатусЗакрытия": "status",
            "ПредставлениеЗаданияНаСмену": "task_description",
            "РабочийЦентр": "work_center",
            "Смена": "shift",
            "Бригада": "brigade",
            "НомерПартии": "batch_number",
            "ДатаПартии": "batch_date",
            "Номенклатура": "product_name",
            "КодЕКН": "ecn_code",
            "ИдентификаторРЦ": "rc_identifier",
            "ДатаВремяНачалаСмены": "start_time",
            "ДатаВремяОкончанияСмены": "end_time"
        }


class TaskShiftInDBBase(TaskShiftBase):
    id: int
    closed_at: Optional[datetime]

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        return cls(**obj.__dict__)


class TaskShiftInDB(TaskShiftInDBBase):
    pass


class TaskShift(TaskShiftInDBBase):
    @classmethod
    def from_orm(cls, obj):
        return cls(**obj.__dict__)


class UniqueProductCode(BaseModel):
    unique_code: str = Field(alias="УникальныйКодПродукта")
    batch_number: int = Field(alias="НомерПартии")
    batch_date: date = Field(alias="ДатаПартии")


class AggregatedProduct(BaseModel):
    unique_code: str = Field(alias="УникальныйКодПродукта")
    is_aggregated: bool
    aggregated_at: Optional[datetime]
    batch_number: int = Field(alias="НомерПартии")
    batch_date: date = Field(alias="ДатаПартии")


class AggregatedProductResult(BaseModel):
    unique_code: str = Field(alias="УникальныйКодПродукта")


class Product(BaseModel):
    unique_code: str
    batch_number: int
    batch_date: date
    is_aggregated: bool = False
    aggregated_at: datetime


class ProductCreate(BaseModel):
    pass


class TaskShiftDB(BaseModel):
    id: int
    status: bool
    task_description: str
    work_center: str
    shift: str
    brigade: str
    batch_number: int
    batch_date: date
    product_name: str
    ecn_code: str
    rc_identifier: str
    start_time: datetime
    end_time: datetime
    closed_at: Optional[datetime]

    class Config:
        orm_mode = True

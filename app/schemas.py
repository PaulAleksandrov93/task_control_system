# from pydantic import BaseModel, Field
# from datetime import datetime, date
# from typing import List, Optional


# class TaskBase(BaseModel):
#     status: Optional[bool]
#     task_description: str
#     work_center: str
#     shift: str
#     brigade: str
#     batch_number: int
#     batch_date: date
#     product_name: str
#     ecn_code: str
#     rc_identifier: str
#     start_time: datetime
#     end_time: datetime
#     priority: Optional[int]


# class Product(ProductBase):
#     id: int
#     is_aggregated: Optional[bool]
#     aggregated_at: Optional[datetime]
#     task_id: int

#     class Config:
#         orm_mode = True


# class TaskCreate(TaskBase):
#     pass  # Оставляем без изменений для использования всех атрибутов в TaskBase


# class Task(TaskBase):
#     id: int
#     closed_at: Optional[datetime]
#     products: List[Product] = []

#     class Config:
#         orm_mode = True


# class ProductCreate(ProductBase):
#     is_aggregated: Optional[bool]


# class TaskUpdate(BaseModel):
#     task_description: Optional[str] = None
#     work_center: Optional[str] = None
#     shift: Optional[str] = None
#     brigade: Optional[str] = None
#     batch_number: Optional[int] = None
#     batch_date: Optional[datetime] = None
#     product_name: Optional[str] = None
#     ecn_code: Optional[str] = None
#     rc_identifier: Optional[str] = None
#     start_time: Optional[datetime] = None
#     end_time: Optional[datetime] = None
#     priority: Optional[int] = None  # Добавлен атрибут приоритета

#     class Config:
#         orm_mode = True


# class TaskShiftCreate(BaseModel):
#     СтатусЗакрытия: bool
#     ПредставлениеЗаданияНаСмену: str
#     РабочийЦентр: str
#     Смена: str
#     Бригада: str
#     НомерПартии: int
#     ДатаПартии: date
#     Номенклатура: str
#     КодЕКН: str
#     ИдентификаторРЦ: str
#     ДатаВремяНачалаСмены: datetime
#     ДатаВремяОкончанияСмены: datetime

#     class Config:
#         validation_alias = True

#schemas.py
from datetime import date, datetime
from typing import List, Optional
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
    # status: Optional[bool] = Field(alias="СтатусЗакрытия")
    # task_description: Optional[str] = Field(alias="ПредставлениеЗаданияНаСмену")
    # work_center: Optional[str] = Field(alias="РабочийЦентр")
    # shift: Optional[str] = Field(alias="Смена")
    # brigade: Optional[str] = Field(alias="Бригада")
    # batch_number: Optional[int] = Field(alias="НомерПартии")
    # batch_date: Optional[date] = Field(alias="ДатаПартии")
    # product_name: Optional[str] = Field(alias="Номенклатура")
    # ecn_code: Optional[str] = Field(alias="КодЕКН")
    # rc_identifier: Optional[str] = Field(alias="ИдентификаторРЦ")
    # start_time: Optional[datetime] = Field(alias="ДатаВремяНачалаСмены")
    # end_time: Optional[datetime] = Field(alias="ДатаВремяОкончанияСмены")
    
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
        

class TaskShift(TaskShiftInDBBase):
    pass

class TaskShiftInDB(TaskShiftInDBBase):
    pass

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
    aggregated_at: datetime = None
    
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


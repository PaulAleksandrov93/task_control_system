#schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ProductBase(BaseModel):
    unique_code: str
    
class TaskBase(BaseModel):
    status: Optional[bool]
    task_description: str
    work_center: str
    shift: str
    brigade: str
    batch_number: int
    batch_date: datetime
    product_name: str
    ecn_code: str
    rc_identifier: str
    start_time: datetime
    end_time: datetime

class Product(ProductBase):
    id: int
    is_aggregated: Optional[bool]
    aggregated_at: Optional[datetime]
    task_id: int

    class Config:
        orm_mode = True
        
class TaskCreate(TaskBase):
    priority: int


class Task(TaskBase):
    id: int
    closed_at: Optional[datetime]
    products: List[Product] = []

    class Config:
        orm_mode = True

class ProductCreate(ProductBase):
    is_aggregated: Optional[bool]
    

class TaskUpdate(BaseModel):
    task_description: Optional[str] = None
    work_center: Optional[str] = None
    shift: Optional[str] = None
    brigade: Optional[str] = None
    batch_number: Optional[int] = None
    batch_date: Optional[datetime] = None
    product_name: Optional[str] = None
    ecn_code: Optional[str] = None
    rc_identifier: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    class Config:
        orm_mode = True
#models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Date,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

Base: Any = declarative_base()


class TaskShift(Base):
    __tablename__ = "task_shifts"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=False)
    task_description = Column(String, nullable=False)
    work_center = Column(String, nullable=False)
    shift = Column(String, nullable=False)
    brigade = Column(String, nullable=False)
    batch_number = Column(Integer, nullable=False, unique=True)
    batch_date = Column(Date, nullable=False)
    product_name = Column(String, nullable=False)
    ecn_code = Column(String, nullable=False)
    rc_identifier = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    closed_at = Column(DateTime, nullable=True)

    products = relationship("Product", back_populates="task_shift")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    unique_code = Column(String, unique=True, nullable=False)
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(DateTime)
    task_shift_id = Column(Integer, ForeignKey("task_shifts.id"))

    task_shift = relationship("TaskShift", back_populates="products")



from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=False)
    task_description = Column(String, index=True)
    work_center = Column(String)
    shift = Column(String)
    brigade = Column(String)
    batch_number = Column(Integer, index=True, unique=True)
    batch_date = Column(DateTime)
    product_name = Column(String)
    ecn_code = Column(String)
    rc_identifier = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    closed_at = Column(DateTime)
    priority = Column(Integer, index=True)  

    products = relationship("Product", back_populates="task")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    unique_code = Column(String, index=True, unique=True)
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(DateTime)
    task_id = Column(Integer, ForeignKey("tasks.id"))

    task = relationship("Task", back_populates="products")
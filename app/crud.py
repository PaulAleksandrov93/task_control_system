# crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from datetime import datetime
from typing import List, Dict, Any

from app.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_shift_tasks(db: Session, shift_tasks_data: List[Dict[str, Any]]):
    created_task_shifts = []
    for task_shift_data in shift_tasks_data:
        task_shift = schemas.TaskShiftCreate(**task_shift_data)
        created_task_shift = create_task_shift(db, task_shift)
        created_task_shifts.append(created_task_shift)
    return created_task_shifts


def create_task_shift(db: Session, task_shift: schemas.TaskShiftCreate):
    # Проверяем наличие записи с такой же комбинацией номера партии и даты партии
    existing_task_shift = (
        db.query(models.TaskShift)
        .filter_by(
            batch_number=task_shift.batch_number,
            batch_date=task_shift.batch_date,
        )
        .first()
    )

    if existing_task_shift:
        for field, value in task_shift.dict().items():
            setattr(existing_task_shift, field, value)

        if existing_task_shift.status:
            existing_task_shift.closed_at = datetime.now()  # type: ignore

        db.add(existing_task_shift)
        db_task_shift = existing_task_shift
    else:
        db_task_shift = models.TaskShift(**task_shift.dict())

        if db_task_shift.status:
            db_task_shift.closed_at = datetime.now()  # type: ignore
        db.add(db_task_shift)
        db.commit()
        db.refresh(db_task_shift)

    return db_task_shift


def get_task_shift(db: Session, task_shift_id: int):
    task_shift = (
        db.query(models.TaskShift)
        .filter(models.TaskShift.id == task_shift_id)
        .first()
    )
    if task_shift is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task shift not found",
        )
    print("Data from database:", task_shift.__dict__)
    return task_shift


def update_task_shift(
    db: Session, task_shift_id: int, task_shift: schemas.TaskShiftUpdate
):
    db_task_shift = (
        db.query(models.TaskShift)
        .filter(models.TaskShift.id == task_shift_id)
        .first()
    )
    if db_task_shift is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task shift not found",
        )

    for field, value in task_shift.dict().items():
        if value is not None:
            setattr(db_task_shift, field, value)

    if db_task_shift.status:
        db_task_shift.closed_at = datetime.now()  # type: ignore
    else:
        db_task_shift.closed_at = None  # type: ignore

    db.commit()
    db.refresh(db_task_shift)
    return db_task_shift


def get_task_shifts(db: Session, skip: int = 0, limit: int = 10):
    task_shifts = db.query(models.TaskShift).offset(skip).limit(limit).all()
    print(
        "Fetched task shifts from database:", task_shifts
    )
    return [
        schemas.TaskShift.from_orm(task_shift) for task_shift in task_shifts
    ]


def get_task_shift_by_filters(
    db: Session, filters: dict, skip: int = 0, limit: int = 10
):
    query = db.query(models.TaskShift)
    for key, value in filters.items():
        query = query.filter_by(**{key: value})
    return query.offset(skip).limit(limit).all()


def add_product_to_task_shift(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def aggregate_product(db: Session, task_shift_id: int, unique_code: str):
    db_product = (
        db.query(models.Product)
        .filter(models.Product.unique_code == unique_code)
        .first()
    )
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    if db_product.task_shift_id != task_shift_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unique code is attached to another batch",
        )

    if db_product.is_aggregated:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unique code already used at {db_product.aggregated_at}",
        )

    db_product.is_aggregated = True  # type: ignore
    db_product.aggregated_at = datetime.now()  # type: ignore
    db.commit()
    return {"unique_code": db_product.unique_code}

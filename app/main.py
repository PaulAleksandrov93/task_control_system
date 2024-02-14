# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import get_db, engine
from typing import Dict, Any

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post(
    "/task-shifts/",
    response_model=schemas.TaskShift,
    status_code=status.HTTP_201_CREATED,
)
def create_task_shift(
    task_shift: schemas.TaskShiftCreate, db: Session = Depends(get_db)
):
    created_task_shift = crud.create_task_shift(db=db, task_shift=task_shift)
    return created_task_shift


@app.post(
    "/shift-tasks/",
    response_model=List[schemas.TaskShift],
    status_code=status.HTTP_201_CREATED,
)
def create_shift_tasks_endpoint(
    shift_tasks_data: List[Dict[str, Any]], db: Session = Depends(get_db)
):
    created_shift_tasks = crud.create_shift_tasks(
        db=db, shift_tasks_data=shift_tasks_data
    )
    return created_shift_tasks


@app.get("/task-shifts/", response_model=List[schemas.TaskShift])
def read_task_shifts(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    task_shifts = crud.get_task_shifts(db=db, skip=skip, limit=limit)
    return [
        schemas.TaskShift.from_orm(task_shift) for task_shift in task_shifts
    ]


@app.get("/task-shifts/{task_shift_id}", response_model=schemas.TaskShiftDB)
def read_task_shift(task_shift_id: int, db: Session = Depends(get_db)):
    db_task_shift = crud.get_task_shift(db=db, task_shift_id=task_shift_id)
    if db_task_shift is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task shift not found",
        )

    # Сериализуем дату в строку
    db_task_shift.batch_date = db_task_shift.batch_date.isoformat()

    return db_task_shift


@app.put(
    "/task-shifts/{task_shift_id}", response_model=schemas.TaskShiftUpdate
)
def update_task_shift(
    task_shift_id: int,
    task_shift: schemas.TaskShiftUpdate,
    db: Session = Depends(get_db),
):
    updated_task_shift = crud.update_task_shift(
        db=db, task_shift_id=task_shift_id, task_shift=task_shift
    )
    return updated_task_shift


@app.get("/task-shifts/filters", response_model=List[schemas.TaskShift])
def read_task_shifts_by_filters(
    filters: dict = {},
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    task_shifts = crud.get_task_shift_by_filters(db=db, filters=filters)
    return task_shifts


@app.post(
    "/task-shifts/{task_shift_id}/products/", response_model=schemas.Product
)
def add_product_to_task_shift(
    task_shift_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    product.task_shift_id = task_shift_id
    added_product = crud.add_product_to_task_shift(db=db, product=product)
    return added_product


@app.put(
    "/task-shifts/{task_shift_id}/aggregate/",
    response_model=schemas.AggregatedProduct,
)
def aggregate_product(
    task_shift_id: int, unique_code: str, db: Session = Depends(get_db)
):
    aggregated_product = crud.aggregate_product(
        db=db, task_shift_id=task_shift_id, unique_code=unique_code
    )
    return aggregated_product

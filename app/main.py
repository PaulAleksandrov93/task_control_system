# from fastapi import FastAPI, HTTPException, Depends, status
# from sqlalchemy.orm import Session
# from typing import List
# from app import crud, models, schemas
# from app.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
# def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     created_task = crud.create_task(db=db, task=task)
#     return created_task

# @app.post("/shift-tasks/", response_model=List[schemas.Task])
# def create_shift_tasks(shift_tasks: List[schemas.TaskShiftCreate], db: Session = Depends(get_db)):
#     created_shift_tasks = []
#     for shift_task in shift_tasks:
#         created_shift_task = crud.create_shift_task(db=db, task=shift_task)
#         created_shift_tasks.append(created_shift_task)
#     return created_shift_tasks

# @app.get("/tasks/", response_model=list[schemas.Task])
# def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
#     return tasks

# @app.get("/tasks/{task_id}", response_model=schemas.Task)
# def read_task(task_id: int, db: Session = Depends(get_db)):
#     db_task = crud.get_task(db=db, task_id=task_id)
#     if db_task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return db_task

# @app.put("/tasks/{task_id}", response_model=schemas.Task)
# def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
#     db_task = crud.get_task(db=db, task_id=task_id)
#     if db_task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return crud.update_task(db=db, task_id=task_id, task=task)

# @app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     deleted_task = crud.delete_task(db=db, task_id=task_id)
#     return None

#main.py
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import get_db, engine
from app.schemas import TaskShift

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/task-shifts/", response_model=schemas.TaskShift, status_code=status.HTTP_201_CREATED)
def create_task_shift(task_shift: schemas.TaskShiftCreate, db: Session = Depends(get_db)):
    created_task_shift = crud.create_task_shift(db=db, task_shift=task_shift)
    return created_task_shift

@app.get("/task-shifts/", response_model=List[schemas.TaskShift])
def read_task_shifts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    task_shifts = crud.get_task_shifts(db=db, skip=skip, limit=limit)
    return task_shifts

@app.get("/task-shifts/{task_shift_id}", response_model=TaskShift)
def read_task_shift(task_shift_id: int, db: Session = Depends(get_db)):
    db_task_shift = crud.get_task_shift(db=db, task_shift_id=task_shift_id)
    if db_task_shift is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task shift not found")
    
    
    return TaskShift(**db_task_shift.__dict__)

@app.put("/task-shifts/{task_shift_id}", response_model=schemas.TaskShift)
def update_task_shift(task_shift_id: int, task_shift: schemas.TaskShiftUpdate, db: Session = Depends(get_db)):
    updated_task_shift = crud.update_task_shift(db=db, task_shift_id=task_shift_id, task_shift=task_shift)
    return updated_task_shift

@app.get("/task-shifts/filters", response_model=List[schemas.TaskShift])
def read_task_shifts_by_filters(filters: dict = {}, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    task_shifts = crud.get_task_shift_by_filters(db=db, filters=filters)
    return task_shifts

@app.post("/task-shifts/{task_shift_id}/products/", response_model=schemas.Product)
def add_product_to_task_shift(task_shift_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product.task_shift_id = task_shift_id
    added_product = crud.add_product_to_task_shift(db=db, product=product)
    return added_product

@app.put("/task-shifts/{task_shift_id}/aggregate/", response_model=schemas.AggregatedProduct)
def aggregate_product(task_shift_id: int, unique_code: str, db: Session = Depends(get_db)):
    aggregated_product = crud.aggregate_product(db=db, task_shift_id=task_shift_id, unique_code=unique_code)
    return aggregated_product
# test_crud.py

import pytest
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from app.models import TaskShift
from datetime import date, datetime


@pytest.fixture
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_create_task_shift(db: Session):
    task_shift_data = {
        "СтатусЗакрытия": False,
        "ПредставлениеЗаданияНаСмену": "Тестовое задание",
        "РабочийЦентр": "Центр",
        "Смена": "Первая",
        "Бригада": "Бригада №1",
        "НомерПартии": 1,
        "ДатаПартии": date(2024, 1, 1),
        "Номенклатура": "Продукт",
        "КодЕКН": "123",
        "ИдентификаторРЦ": "ID",
        "ДатаВремяНачалаСмены": datetime(2024, 1, 1, 0, 0, 0),
        "ДатаВремяОкончанияСмены": datetime(2024, 1, 1, 8, 0, 0)
    }
    task_shift_create = schemas.TaskShiftCreate(
        **task_shift_data)  # type: ignore

    try:
        task_shift = crud.create_task_shift(db, task_shift_create)
        assert isinstance(task_shift, TaskShift)
        assert task_shift.task_description == "Тестовое задание"
        assert task_shift.closed_at is None
    except Exception as e:
        raise e

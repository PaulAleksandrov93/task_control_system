#test_crud.py
import pytest
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from app.models import TaskShift

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
        "ДатаПартии": "2024-01-01",
        "Номенклатура": "Продукт",
        "КодЕКН": "123",
        "ИдентификаторРЦ": "ID",
        "ДатаВремяНачалаСмены": "2024-01-01T00:00:00",
        "ДатаВремяОкончанияСмены": "2024-01-01T08:00:00"
    }
    task_shift_create = schemas.TaskShiftCreate(**task_shift_data)
    
    # Используем контекстный менеджер try-except для перехвата и вывода ошибок валидации
    try:
        task_shift = crud.create_task_shift(db, task_shift_create)
        # Проверяем, что создан объект TaskShift
        assert isinstance(task_shift, TaskShift)
        # Проверяем соответствие представления задания
        assert task_shift.task_description == "Тестовое задание"
        # Проверяем, что closed_at не установлено, если статус задания False
        assert task_shift.closed_at is None
    except Exception as e:
        # Повторно поднимаем исключение для передачи его тестовому фреймворку
        raise e
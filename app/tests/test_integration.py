# test_integration.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app import crud
import json


@pytest.fixture(scope="module")
def test_db():
    yield SessionLocal()


@pytest.fixture
def client(test_db):
    def override_get_db():
        yield test_db
    app.dependency_overrides[crud.get_db] = override_get_db
    yield TestClient(app)


def test_create_shift_tasks(client):
    shift_tasks_data = [
        {
            "СтатусЗакрытия": False,
            "ПредставлениеЗаданияНаСмену": "Сменное задание 1",
            "РабочийЦентр": "Рабочий центр 1",
            "Смена": "Смена 1",
            "Бригада": "Бригада №1",
            "НомерПартии": 12345,
            "ДатаПартии": "2024-02-11",
            "Номенклатура": "Номенклатура 1",
            "КодЕКН": "456678",
            "ИдентификаторРЦ": "A",
            "ДатаВремяНачалаСмены": "2024-02-11T20:00:00+05:00",
            "ДатаВремяОкончанияСмены": "2024-02-12T08:00:00+05:00"
        },
        {
            "СтатусЗакрытия": True,
            "ПредставлениеЗаданияНаСмену": "Сменное задание 2",
            "РабочийЦентр": "Рабочий центр 2",
            "Смена": "Смена 2",
            "Бригада": "Бригада №2",
            "НомерПартии": 12346,
            "ДатаПартии": "2024-02-12",
            "Номенклатура": "Номенклатура 2",
            "КодЕКН": "456679",
            "ИдентификаторРЦ": "B",
            "ДатаВремяНачалаСмены": "2024-02-12T20:00:00+05:00",
            "ДатаВремяОкончанияСмены": "2024-02-13T08:00:00+05:00"
        }
    ]

    # Преобразование даты в строки
    for task in shift_tasks_data:
        task["ДатаПартии"] = str(task["ДатаПартии"])

    # Отправка POST запроса для создания сменных задач
    response = client.post("/shift-tasks/", json=shift_tasks_data)

    # Проверка статус кода ответа
    assert response.status_code == 201


def test_create_task_shift(client):
    task_shift_data = {
        "СтатусЗакрытия": False,
        "ПредставлениеЗаданияНаСмену": "Test task",
        "РабочийЦентр": "Center",
        "Смена": "Shift",
        "Бригада": "Brigade",
        "НомерПартии": 1,
        "ДатаПартии": "2024-01-01",
        "Номенклатура": "Product",
        "КодЕКН": "123",
        "ИдентификаторРЦ": "ID",
        "ДатаВремяНачалаСмены": "2024-01-01T00:00:00",
        "ДатаВремяОкончанияСмены": "2024-01-01T08:00:00"
    }

    response = client.post("/task-shifts/", data=json.dumps(task_shift_data))
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_task_shift_by_id(client):
    task_shift_id = 1
    response = client.get(f"/task-shifts/{task_shift_id}")
    assert response.status_code == 200
    data = response.json()
    print("Data from response:", data)
    assert data["id"] == task_shift_id

#test_integration.py
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
    assert "СтатусЗакрытия" in data  
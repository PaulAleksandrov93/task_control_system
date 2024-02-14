# test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_task_shift_endpoint(client):
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
        "ДатаВремяОкончанияСмены": "2024-01-01T08:00:00",
    }
    response = client.post("/task-shifts/", json=task_shift_data)
    assert response.status_code == 201


def test_get_task_shift_by_id_endpoint(client):
    task_shift_id = 1
    response = client.get(f"/task-shifts/{task_shift_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_shift_id


# def test_update_task_shift_endpoint(client):
#     task_shift_id = 1
#     updated_task_shift_data = {
#         "СтатусЗакрытия": True,
#         "ПредставлениеЗаданияНаСмену": "Updated task",
#         "РабочийЦентр": "Updated Center",
#         "Смена": "Updated Shift",
#         "Бригада": "Updated Brigade",
#         "НомерПартии": 2,
#         "ДатаПартии": "2024-01-02",
#         "Номенклатура": "Updated Product",
#         "КодЕКН": "456",
#         "ИдентификаторРЦ": "Updated ID",
#         "ДатаВремяНачалаСмены": "2024-01-02T00:00:00",
#         "ДатаВремяОкончанияСмены": "2024-01-02T08:00:00"
#     }
#     response = client.put(f"/task-shifts/{task_shift_id}", json=updated_task_shift_data)
#     assert response.status_code == 200
#     assert response.json()["id"] == task_shift_id
#     assert response.json()["СтатусЗакрытия"] == True
#     assert response.json()["ПредставлениеЗаданияНаСмену"] == "Updated task"

# def test_get_task_shifts_by_filters_endpoint(client):
#     filters = {"РабочийЦентр": "Center", "Смена": "Shift"}
#     response = client.get("/task-shifts/filters", params=filters)
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_add_product_to_task_shift_endpoint(client):
#     task_shift_id = 1
#     product_data = {
#         "task_shift_id": 1,
#         "Название": "Product",
#         "Количество": 10
#     }
#     response = client.post(f"/task-shifts/{task_shift_id}/products/", json=product_data)
#     assert response.status_code == 200
#     assert "id" in response.json()

# def test_aggregate_product_endpoint(client):
#     task_shift_id = 1
#     unique_code = "1234567890"
#     response = client.put(f"/task-shifts/{task_shift_id}/aggregate/?unique_code={unique_code}")
#     assert response.status_code == 200
#     assert response.json()["unique_code"] == unique_code

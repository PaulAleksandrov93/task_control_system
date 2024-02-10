from fastapi.testclient import TestClient
from ..main import app
from .. import crud, models, schemas
from ..database import SessionLocal
import json

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[crud.get_db] = override_get_db

client = TestClient(app)



def test_create_task():
    task_data = {
        "task_description": "Test task",
        "work_center": "WC1",
        "shift": "Morning",
        "brigade": "Brigade1",
        "batch_number": 12345,
        "batch_date": "2024-01-30T00:00:00",
        "product_name": "Test Product",
        "ecn_code": "ECN123",
        "rc_identifier": "RC001",
        "start_time": "2024-01-30T08:00:00",
        "end_time": "2024-01-30T16:00:00",
        "priority": 1,
        "status": True  
    }
    response = client.post("/tasks/", json=task_data)
    if response.status_code != 201:
        print("Error creating task:")
        print(json.dumps(response.json(), indent=4))

    assert response.status_code == 201

def test_read_task():
    task_data = {
        "task_description": "Test task",
        "work_center": "WC1",
        "shift": "Morning",
        "brigade": "Brigade1",
        "batch_number": 12345,
        "batch_date": "2024-01-30T00:00:00",
        "product_name": "Test Product",
        "ecn_code": "ECN123",
        "rc_identifier": "RC001",
        "start_time": "2024-01-30T08:00:00",
        "end_time": "2024-01-30T16:00:00",
        "priority": 1,
        "status": True
    }
    client.post("/tasks/", json=task_data)

    response = client.get("/tasks/1")
    if response.status_code != 200:
        print("Error reading task:")
        print(json.dumps(response.json(), indent=4))

    assert response.status_code == 200

def test_update_task():
    task_data = {
        "task_description": "Test task",
        "work_center": "WC1",
        "shift": "Morning",
        "brigade": "Brigade1",
        "batch_number": 12345,
        "batch_date": "2024-01-30T00:00:00",
        "product_name": "Test Product",
        "ecn_code": "ECN123",
        "rc_identifier": "RC001",
        "start_time": "2024-01-30T08:00:00",
        "end_time": "2024-01-30T16:00:00",
        "priority": 1,
        "status": True
    }
    client.post("/tasks/", json=task_data)

    updated_task_data = {
        "task_description": "Updated task description",
        "work_center": "WC2",
        "shift": "Afternoon",
        "brigade": "Brigade2",
        "batch_number": 54321,
        "batch_date": "2024-02-01T00:00:00",
        "product_name": "Updated Product",
        "ecn_code": "ECN456",
        "rc_identifier": "RC002",
        "start_time": "2024-02-01T08:00:00",
        "end_time": "2024-02-01T16:00:00",
        "priority": 2,
        "status": False
    }
    response = client.put("/tasks/1", json=updated_task_data)
    if response.status_code != 200:
        print("Error updating task:")
        print(json.dumps(response.json(), indent=4))

    assert response.status_code == 200
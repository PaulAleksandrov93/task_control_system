# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy.orm import Session
# from app import crud, models, schemas
# from ..database import engine, TestingSessionLocal


# # Fixture для создания тестовой базы данных
# @pytest.fixture(scope="module")
# def db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # # Fixture для очистки тестовой базы данных перед каждым тестом
# @pytest.fixture(autouse=True)
# def clean_test_db(db: Session):
#     try:
#         yield
#     finally:
#         print("Cleaning test database")
#         models.Base.metadata.drop_all(bind=engine)
#         models.Base.metadata.create_all(bind=engine)

# # Fixture для создания клиента тестирования
# @pytest.fixture(scope="module")
# def client():
#     from app.main import app
#     return TestClient(app)

# def test_create_task(client: TestClient, db: Session):
#     # Данные для создания задачи
#     task_data = {
#         "task_description": "Test Task",
#         "work_center": "Test Work Center",
#         "shift": "Test Shift",
#         "brigade": "Test Brigade",
#         "batch_number": 12345,
#         "batch_date": "2024-02-11T12:00:00",
#         "product_name": "Test Product",
#         "ecn_code": "Test ECN",
#         "rc_identifier": "Test RC",
#         "start_time": "2024-02-11T08:00:00",
#         "end_time": "2024-02-11T16:00:00",
#         "priority": 1,
#         "status": True
#     }
#     # Отправка POST запроса для создания задачи
#     response = client.post("/tasks/", json=task_data)
#     # Проверка статус кода ответа
#     assert response.status_code == 201

# def test_get_task_by_id(client: TestClient, db: Session):
#     # Создаем задачу
#     task_data = {
#         "task_description": "Test Task",
#         "work_center": "Test Work Center",
#         "shift": "Test Shift",
#         "brigade": "Test Brigade",
#         "batch_number": 12345,
#         "batch_date": "2024-02-11T12:00:00",
#         "product_name": "Test Product",
#         "ecn_code": "Test ECN",
#         "rc_identifier": "Test RC",
#         "start_time": "2024-02-11T08:00:00",
#         "end_time": "2024-02-11T16:00:00",
#         "priority": 1,
#         "status": True
#     }
#     response = client.post("/tasks/", json=task_data)
#     created_task = response.json()

#     # Получаем задачу по ID
#     response = client.get(f"/tasks/{created_task['id']}")
#     assert response.status_code == 200
#     retrieved_task = response.json()
#     assert retrieved_task == created_task

# # Тест для получения списка всех задач
# def test_get_all_tasks(client: TestClient, db: Session):
#     # Создаем несколько задач
#     task_data_1 = {
#         "task_description": "Test Task 1",
#         "work_center": "Test Work Center 1",
#         "shift": "Test Shift 1",
#         "brigade": "Test Brigade 1",
#         "batch_number": 12345,
#         "batch_date": "2024-02-11T12:00:00",
#         "product_name": "Test Product 1",
#         "ecn_code": "Test ECN 1",
#         "rc_identifier": "Test RC 1",
#         "start_time": "2024-02-11T08:00:00",
#         "end_time": "2024-02-11T16:00:00",
#         "priority": 1,
#         "status": True
#     }
#     task_data_2 = {
#         "task_description": "Test Task 2",
#         "work_center": "Test Work Center 2",
#         "shift": "Test Shift 2",
#         "brigade": "Test Brigade 2",
#         "batch_number": 12346,
#         "batch_date": "2024-02-12T12:00:00",
#         "product_name": "Test Product 2",
#         "ecn_code": "Test ECN 2",
#         "rc_identifier": "Test RC 2",
#         "start_time": "2024-02-12T08:00:00",
#         "end_time": "2024-02-12T16:00:00",
#         "priority": 2,
#         "status": True
#     }
#     # Создаем задачи
#     client.post("/tasks/", json=task_data_1)
#     client.post("/tasks/", json=task_data_2)

#     # Получаем список всех задач
#     response = client.get("/tasks/")
#     assert response.status_code == 200
#     tasks = response.json()
#     assert len(tasks) == 2  # Проверяем, что получено две задачи


# def test_update_task(client: TestClient, db: Session):
#     # Создаем задачу для обновления
#     task_data = {
#         "task_description": "Test Task",
#         "work_center": "Test Work Center",
#         "shift": "Test Shift",
#         "brigade": "Test Brigade",
#         "batch_number": 12345,
#         "batch_date": "2024-02-11T12:00:00",
#         "product_name": "Test Product",
#         "ecn_code": "Test ECN",
#         "rc_identifier": "Test RC",
#         "start_time": "2024-02-11T08:00:00",
#         "end_time": "2024-02-11T16:00:00",
#         "priority": 1,
#         "status": True
#     }
#     response = client.post("/tasks/", json=task_data)
#     created_task = response.json()
    
#     # Обновляем задачу
#     update_data = {"task_description": "Updated Task"}
#     response = client.put(f"/tasks/{created_task['id']}", json=update_data)
    
#     # Проверяем статус кода и обновленные данные
#     assert response.status_code == 200  # Изменено на 200, если требуется вернуть обновленные данные, иначе можно использовать 204
#     updated_task = response.json()
#     assert updated_task["task_description"] == "Updated Task"


# def test_delete_task(client: TestClient, db: Session):
#     # Создаем задачу для удаления
#     task_data = {
#         "task_description": "Test Task",
#         "work_center": "Test Work Center",
#         "shift": "Test Shift",
#         "brigade": "Test Brigade",
#         "batch_number": 12345,
#         "batch_date": "2024-02-11T12:00:00",
#         "product_name": "Test Product",
#         "ecn_code": "Test ECN",
#         "rc_identifier": "Test RC",
#         "start_time": "2024-02-11T08:00:00",
#         "end_time": "2024-02-11T16:00:00",
#         "priority": 1,
#         "status": True
#     }
#     response = client.post("/tasks/", json=task_data)
#     created_task = response.json()
    
#     # Удаляем задачу
#     response = client.delete(f"/tasks/{created_task['id']}")
    
#     # Проверяем статус кода и сообщение об успешном удалении
#     assert response.status_code == 204  # Изменено на 204, так как по стандарту удаление ресурса должно возвращать 204 No Content

# def test_create_shift_task(client: TestClient, db: Session):
#     # Данные для создания сменных задач
#     shift_tasks_data = [
#         {
#             "СтатусЗакрытия": False,
#             "ПредставлениеЗаданияНаСмену": "Сменное задание 1",
#             "РабочийЦентр": "Рабочий центр 1",
#             "Смена": "Смена 1",
#             "Бригада": "Бригада №1",
#             "НомерПартии": 12345,
#             "ДатаПартии": "2024-02-11",
#             "Номенклатура": "Номенклатура 1",
#             "КодЕКН": "456678",
#             "ИдентификаторРЦ": "A",
#             "ДатаВремяНачалаСмены": "2024-02-11T20:00:00+05:00",
#             "ДатаВремяОкончанияСмены": "2024-02-12T08:00:00+05:00"
#         },
#         {
#             "СтатусЗакрытия": True,
#             "ПредставлениеЗаданияНаСмену": "Сменное задание 2",
#             "РабочийЦентр": "Рабочий центр 2",
#             "Смена": "Смена 2",
#             "Бригада": "Бригада №2",
#             "НомерПартии": 12346,
#             "ДатаПартии": "2024-02-12",
#             "Номенклатура": "Номенклатура 2",
#             "КодЕКН": "456679",
#             "ИдентификаторРЦ": "B",
#             "ДатаВремяНачалаСмены": "2024-02-12T20:00:00+05:00",
#             "ДатаВремяОкончанияСмены": "2024-02-13T08:00:00+05:00"
#         }
#     ]
    
#     # Отправка POST запроса для создания сменных задач
#     response = client.post("/shift-tasks/", json=shift_tasks_data)
    
#     # Проверка статус кода ответа
#     assert response.status_code == 201







# #test_main.py
# import pytest
# from fastapi.testclient import TestClient
# from app.main import app

# @pytest.fixture
# def client():
#     return TestClient(app)

# def test_create_task_shift_endpoint(client):
#     task_shift_data = {
#         "СтатусЗакрытия": False,
#         "ПредставлениеЗаданияНаСмену": "Test task",
#         "РабочийЦентр": "Center",
#         "Смена": "Shift",
#         "Бригада": "Brigade",
#         "НомерПартии": 1,
#         "ДатаПартии": "2024-01-01",
#         "Номенклатура": "Product",
#         "КодЕКН": "123",
#         "ИдентификаторРЦ": "ID",
#         "ДатаВремяНачалаСмены": "2024-01-01T00:00:00",
#         "ДатаВремяОкончанияСмены": "2024-01-01T08:00:00"
#     }
#     response = client.post("/task-shifts/", json=task_shift_data)
#     assert response.status_code == 201

# def test_get_task_shift_by_id_endpoint(client):
#     task_shift_id = 1
#     response = client.get(f"/task-shifts/{task_shift_id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == task_shift_id
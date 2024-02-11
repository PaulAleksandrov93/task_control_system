from sqlalchemy import inspect, create_engine
from sqlalchemy.ext.automap import automap_base

# Создаем строку подключения к базе данных
DATABASE_URL = "postgresql://control_task_user:control_task_password@localhost:5432/control_task_database"

# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL)

# Создаем отображение таблиц из базы данных
Base = automap_base()
Base.prepare(engine, reflect=True)

# Получаем объект-инспектор для таблицы "tasks"
inspector = inspect(engine)
columns = inspector.get_columns("tasks")

# Проверяем, есть ли столбец "priority" в таблице "tasks"
if any(column["name"] == "priority" for column in columns):
    print("Столбец 'priority' успешно добавлен в таблицу 'tasks'")
else:
    print("Столбец 'priority' не найден в таблице 'tasks'")
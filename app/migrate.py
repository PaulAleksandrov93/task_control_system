import logging
import sys

from migrate.versioning import api
from migrate.exceptions import DatabaseAlreadyControlledError
from migrate.exceptions import DatabaseNotControlledError

from sqlalchemy import create_engine

# Конфигурация подключения к базе данных
DB_USERNAME = 'control_task_user'
DB_PASSWORD = 'control_task_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'control_task_database'

# Создаем строку подключения к базе данных
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Инициализация логирования
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Подключаемся к базе данных
engine = create_engine(DATABASE_URL)

# Инициализируем миграции
try:
    api.version_control(engine, 'migrations')
    print('Migration repository created')
except DatabaseAlreadyControlledError:
    print('Migration repository already exists')
except Exception as e:
    print('An error occurred during migration repository creation:', e)

# Создаем файл миграции
try:
    api.create_script('',
                      'migrations',
                      'Add_priority_to_task',
                      'sqlalchemy')
    print('Migration script created')
except Exception as e:
    print('An error occurred during migration script creation:', e)
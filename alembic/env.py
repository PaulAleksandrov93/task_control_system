import logging
import logging.config
import sys
import os

# Определение стандартной конфигурации логирования
default_logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'myapp.log',
            'maxBytes': 10485760,
            'backupCount': 5,
            'encoding': 'utf8'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

# Применение стандартной конфигурации логирования
logging.config.dictConfig(default_logging_config)

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Импорт моделей SQLAlchemy 
# Учитывая, что путь к вашему модулю Base указан как 'app.models'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base

# Загрузка конфигурации логирования
config = context.config
if config.config_file_name:
    logging.config.dictConfig(default_logging_config)  # Используем стандартную конфигурацию логирования

# Использование моделей SQLAlchemy в миграциях
target_metadata = Base.metadata

# Получение URL-адреса базы данных из конфигурации SQLAlchemy
url = config.get_main_option("sqlalchemy.url")

# Конфигурация миграций
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_online()
else:
    run_migrations_online()
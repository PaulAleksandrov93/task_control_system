import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.database import Base, engine


@pytest.fixture(scope="session", autouse=True)
def clear_test_db():
    # Создаем соединение с тестовой базой данных
    connection = engine.connect()
    # Начинаем транзакцию
    trans = connection.begin()
    try:
        # Очищаем все таблицы в тестовой базе данных
        for table in reversed(Base.metadata.sorted_tables):
            connection.execute(table.delete())
        # Коммитим изменения
        trans.commit()
    except:
        # Если произошла ошибка, откатываем изменения
        trans.rollback()
        raise
    finally:
        # Закрываем соединение
        connection.close()
# Установка базового образа Python
FROM python:3.9

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование зависимостей проекта в контейнер
COPY requirements.txt .

# Установка зависимостей проекта
RUN pip install --no-cache-dir -r requirements.txt

# Установка PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Копирование остальных файлов проекта в контейнер
COPY . .

# Команда для запуска приложения внутри контейнера
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
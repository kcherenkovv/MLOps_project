# Базовый образ с Python
FROM python:3.9-slim

# Копирование файлов приложения
COPY scripts/image_processing.py /app/image_processing.py
COPY scripts/main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Рабочая директория
WORKDIR /app

# Установка зависимостей
RUN pip install -r requirements.txt

# Команда для запуска Streamlit
CMD ["streamlit", "run", "main.py"]
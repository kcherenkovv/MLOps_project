# Базовый образ с Python
FROM python:3.9-slim

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование файлов приложения
COPY image_processing.py /app/image_processing.py
COPY main.py /app/main.py

# Рабочая директория
WORKDIR /app

# Команда для запуска Streamlit
CMD ["streamlit", "run", "main.py"]
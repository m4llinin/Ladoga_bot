# Используем базовый образ Python
FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование исходного кода
COPY . /app

# Запуск бота
CMD ["python", "main.py"]
FROM python:3.11

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade fastapi-prometheus-exporter

# Перенос проекта в образ
COPY ./app /code/app

# Копирование файлов alembic
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations
COPY ./main.py /code/

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port ${PORT}"]

#alembic init migrations && alembic revision --autogenerate -m add_db_task &&
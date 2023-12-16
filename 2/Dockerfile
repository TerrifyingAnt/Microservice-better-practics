FROM python:3.11

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /code/
COPY ./main.py /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Перенос проекта в образ
COPY ./app /code/app


CMD ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 80"]
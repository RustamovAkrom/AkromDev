FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN pip install flower

RUN apt update && at upgrade -y && apt install git -y

WORKDIR /app
COPY . /app

RUN --mount-type=cache,id=custum-pip,target=/root/.cache/pip \ 
    pip install --upgrade pip && \ 
    pip install -r /app/requirements.txt && \ 
    pip install gunicorn

COPY ./compose/django/entrypoint /entrypoint

RUN sed -i 's/\r$//g' /entrypoint \ 
    chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i 's/\r$//g' /start \ 
    chmod +x /start


ENTRYPOINT [ "/entrypoint" ]
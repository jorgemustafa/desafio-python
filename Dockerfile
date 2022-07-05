FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ../../Desktop/test_python/desafio-python/requirements.txt /code/
RUN pip install -r requirements.txt
COPY core /code/
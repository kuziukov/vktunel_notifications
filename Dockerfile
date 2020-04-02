FROM python:3

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

WORKDIR /code/

COPY ./src/ /code/

FROM python:3.7

WORKDIR /code

COPY requirements.txt .

RUN CMD flask db upgrade && python seed.py && pip install --no-cache-dir -r requirements.txt

# RUN flask run
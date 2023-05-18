FROM python:3.10

WORKDIR /usr/src/backend

COPY ./requirements.txt /usr/src/backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/backend/requirements.txt

COPY . /usr/src/backend/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
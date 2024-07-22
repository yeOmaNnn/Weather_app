FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
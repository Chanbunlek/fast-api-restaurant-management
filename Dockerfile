FROM python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-root --no-dev

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

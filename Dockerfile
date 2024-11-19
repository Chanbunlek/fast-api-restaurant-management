FROM python:3.11

WORKDIR /app

COPY . /app/

RUN pip install poetry && poetry install --no-root --no-dev

EXPOSE 8000

WORKDIR /app/app

CMD ["poetry", "run", "fastapi", "run", "main.py", "--port", "8000"]

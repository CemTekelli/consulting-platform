FROM python:3.12-slim

WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --only main   # <-- on ignore le package local

COPY . /code                              

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

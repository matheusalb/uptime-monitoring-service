FROM python:3.12

# Set the working directory
WORKDIR /src

# Copy the requirements file into the container
COPY pyproject.toml ./

RUN apt update && \
    apt install -y pipx && \
    pipx ensurepath

ENV PATH="/root/.local/bin:$PATH"

RUN PIPX_DEFAULT_PYTHON=/usr/local/bin/python3.12 pipx install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

ENV PYTHONPATH="/src/src:${PYTHONPATH}"

EXPOSE 8000

COPY ./src ./src

CMD ["uvicorn", "src.mysqldb.main:app", "--host", "0.0.0.0", "--port", "8000"]

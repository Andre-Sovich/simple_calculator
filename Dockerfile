FROM python:3.12-alpine3.19

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.2 python3 -
# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set work directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Install the project
RUN poetry install

# Run pytest
RUN poetry run pytest

# Command to run your application (replace with your actual command)
CMD python calculator.py
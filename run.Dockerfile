FROM python:3.10
ENV POETRY_VERSION=1.3.1 POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN mkdir sigaebot
COPY . sigaebot
WORKDIR sigaebot
RUN poetry install --no-root --only main
CMD poetry run python main.py
FROM python:3.11-bookworm

ENV POETRY_VERSION="1.8.3" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTIONS=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends rsync git python3.11-venv

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN python3 -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION \
    && $POETRY_HOME/bin/poetry --version
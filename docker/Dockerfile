FROM debian

ENV POETRY_VERSION="1.8.3" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTIONS=1

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends rsync pipx git
RUN pipx ensurepath
RUN pipx install poetry==$POETRY_VERSION


ENV PATH="$POETRY_HOME/bin:$PATH"
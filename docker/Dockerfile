FROM python:3.11-bookworm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install rsync git pipx -y
RUN pipx ensurepath
RUN pipx install poetry

ENTRYPOINT [ "poetry" ]
CMD ["-V"]
#RUN poetry version

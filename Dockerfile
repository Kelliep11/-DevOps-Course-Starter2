FROM python:3.8 as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY todo_app /app/todo_app/


FROM base as production
ENTRYPOINT [ "poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]
EXPOSE 5000

FROM base as development
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host", "0.0.0.0"]
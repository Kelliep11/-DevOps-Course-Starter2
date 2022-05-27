FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY todo_app /app/todo_app/
ENTRYPOINT [ "poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]
EXPOSE 5000
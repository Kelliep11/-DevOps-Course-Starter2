FROM python:3.8 as base

RUN curl -sSL https://install.python-poetry.org/ | python -
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN  poetry config virtualenvs.create false --local && poetry install
COPY todo_app /app/todo_app/


FROM base as production
ENV PORT=5000
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:$PORT
EXPOSE 5000

FROM base as development
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]
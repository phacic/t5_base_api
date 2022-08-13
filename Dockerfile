FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

ARG ENV=dev

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
#    bash -c "if [ $ENV == 'dev' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY . /app/
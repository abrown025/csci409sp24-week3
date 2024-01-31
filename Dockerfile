FROM python:3.12-apline3.19
LABEL maintainer="Adam Brown"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./api /api
WORKDIR /api
EXPOSE 8000

RUN python -m venv312 /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \ 
        --no-create-home \ 
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
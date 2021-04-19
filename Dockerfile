FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /backend
COPY ./backend /backend
WORKDIR /backend/backend

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app
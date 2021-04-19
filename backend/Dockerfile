FROM python:3.8.5-alpine

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./backend /backend

WORKDIR /backend

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app
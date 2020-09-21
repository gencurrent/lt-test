FROM python:3.8-alpine

RUN apk add ca-certificates gcc postgresql-dev linux-headers musl-dev zlib-dev libffi-dev jpeg-dev

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ./conditional_start.sh
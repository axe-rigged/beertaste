FROM python:latest

WORKDIR /usr/src/app

COPY required.txt ./

RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip libmariadb-dev build-essential python-dev gcc -y

RUN pip install -r required.txt

COPY . .

FROM debian:bullseye-20220328-slim
MAINTAINER BoRu Su <kilfu0701@gmail.com>

RUN apt-get update -y && apt-get -yq install python3 python3-pip python3-dev build-essential libxslt1-dev libxml2 vim

RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv

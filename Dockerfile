FROM debian:bullseye-20220328-slim
MAINTAINER BoRu Su <kilfu0701@gmail.com>

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libsqlite3-dev \
        libreadline-dev \
        libffi-dev \
        curl \
        libbz2-dev \
        libxslt1-dev \
        libxml2 \
        vim \
        wget

ENV PYTHON_VERSION 3.8.13

RUN set -eux && \
    wget -O Python-$PYTHON_VERSION.tar.xz https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz && \
    tar -xf Python-$PYTHON_VERSION.tar.xz && \
    mv Python-$PYTHON_VERSION /opt/Python-$PYTHON_VERSION && \
    cd /opt/Python-$PYTHON_VERSION && \
    ./configure --enable-optimizations --enable-shared && \
    make -j 6 && \
    make altinstall && \
    ldconfig /opt/Python-$PYTHON_VERSION

RUN ln -s /usr/local/bin/python3.8 /usr/local/bin/python3
RUN ln -s /usr/local/bin/pip3.8 /usr/local/bin/pip3

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade virtualenv

RUN apt-get install -y locales-all

EXPOSE 8000

FROM python:3.5

MAINTAINER Stephan Meijer "me@stephanmeijer.com"

RUN apt-get update

RUN apt-get --yes install build-essential

COPY . /tmp/

RUN cd /tmp && make install-requirements
FROM python:3.6-slim

RUN ln -fs /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt && rm -fr /tmp/*

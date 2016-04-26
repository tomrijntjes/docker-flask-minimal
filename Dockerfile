FROM python:2.7
ADD . /swain
WORKDIR /swain
RUN pip install -r requirements.txt

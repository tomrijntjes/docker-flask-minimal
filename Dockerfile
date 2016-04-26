FROM python:2.7
ADD . /minimal
WORKDIR /minimal
RUN pip install -r requirements.txt

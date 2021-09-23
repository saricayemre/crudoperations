FROM python:3.9.7
ADD . /run
WORKDIR /run
RUN pip install -r requirements.txt
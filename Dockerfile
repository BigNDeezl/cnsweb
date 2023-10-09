FROM python:3

WORKDIR /code
COPY . /code
RUN apt-get -y update &&\
    apt-get -y install git &&\
    pip install -r requirements.txt
CMD [ "python", "./index.py", "--reload" ]
EXPOSE 3000
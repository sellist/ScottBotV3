FROM balenalib/raspberry-pi-debian:latest

ADD . /app
RUN cd /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc
RUN apt-get install python3-pip

RUN cd /app
WORKDIR /app

RUN pip3 install discord.py
RUN pip3 install psycopg2
RUN pip3 install pip install python-dotenv

CMD [ "python3", "./main.py"]
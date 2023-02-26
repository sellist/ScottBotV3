FROM python:3.11-slim

ADD main.py .

RUN apt-get update && \
    apt-get install -y libpq-dev gcc


RUN pip install discord.py
RUN pip install psycopg2
RUN pip install pip install python-dotenv

CMD [ "python", "./main.py"]
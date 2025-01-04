FROM python:3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/


RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN python3 manage.py migrate

EXPOSE 8002

CMD [ "python3", "-m", "gunicorn", "pocket_sense.wsgi", "-w", "4", "--bind", "0.0.0.0:8000" ]
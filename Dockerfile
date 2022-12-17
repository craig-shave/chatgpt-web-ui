FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3 django pip3 -y
RUN pip3 install django
RUN pip3 install openai
RUN pip3 install waitress
COPY .ask/ /code/ask
ENTRYPOINT ["python3 /code/ask/manage.py runserver"]

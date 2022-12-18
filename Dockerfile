FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install django
RUN pip3 install openai
RUN pip3 install waitress
ENV PYTHONUNBUFFERED 1
RUN apt-get autoremove --purge -y
RUN mkdir -p /code/ask
COPY ask/ /code/ask
EXPOSE 8222
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

FROM ubuntu:latest
MAINTAINER omkar yadav <omkarsyadav26@gmail.com>
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY /app /app
WORKDIR /app
#EXPOSE 5000
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]

FROM ubuntu:latest
MAINTAINER HELAL ALI Misu "helal.michou.works@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","launch.py"]

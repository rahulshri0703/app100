FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN apt update -y
RUN apt install python3-pip -y
RUN pip install -r requirements.txt

CMD ["bash","run.sh"]
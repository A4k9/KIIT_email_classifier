FROM ubuntu:latest
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/


RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y \
    python3.8 \
    python3-pip


RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0" ]
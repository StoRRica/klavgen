FROM python:3.10.13
LABEL Maintainer="StoRRica"

WORKDIR /usr/app/src

COPY . ./
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get update && apt-get install libgl1
RUN pip install -r requirements.txt
CMD [ "echo", "1"]

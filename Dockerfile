# build image in context folder first
FROM klavgen-context 
LABEL Maintainer="StoRRica"

WORKDIR /usr/app/src

COPY . ./
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get update && apt-get install libgl1
# RUN pip install -r requirements.txt
# RUN mkdir result
# RUN python ./example_2__single_key_save.py
# RUN mv *.stl result
# CMD [ "tail", "-f", "/dev/null"]
CMD [ "python", "./example_2__single_key_save.py", "||", "mv", "*.stl", "result" ]
# try to run script and copy data back
#  docker run --rm -v ./test:/usr/app/src/result klavgen-test 
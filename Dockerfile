# build image in context folder first
FROM klavgen-context 
LABEL Maintainer="StoRRica"

WORKDIR /usr/app/src

COPY . ./
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get update && apt-get install libgl1
# RUN pip install -r requirements.txt
RUN mkdir result
RUN python ./example_2__single_key_save.py
RUN mv *.stl result
# CMD [ "tail", "-f", "/dev/null"]
# CMD [ "python", "./example_2__single_key_save.py", "||", "mv", "*.stl", "result" ]
CMD ["echo", "1"] 

# build context image, buils testing image, crete container, extract result
# to extract all builds run:

# docker create --name dummy klavgen-test
# docker cp dummy:/usr/app/src/result ./test
# docker rm -f dummy
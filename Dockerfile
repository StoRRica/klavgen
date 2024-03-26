# build image in context folder first
FROM klavgen-context 
LABEL Maintainer="StoRRica"

WORKDIR /usr/app/src

COPY . ./
RUN mkdir result
RUN python ./generate_oppodox.py
RUN mv *.stl result
CMD ["echo", "1"] 

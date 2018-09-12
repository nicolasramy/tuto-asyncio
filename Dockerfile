FROM python:3-alpine


RUN apk update \
    && apk upgrade

RUN apk add -f build-base python3-dev


RUN mkdir /app
WORKDIR /app
VOLUME /app
ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt


CMD ["sh"]

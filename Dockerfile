FROM python:3.9

RUN mkdir -p /user/src/app
WORKDIR /user/src/app

COPY . /user/src/app

CMD ["python" , "app.py"]

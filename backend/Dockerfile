FROM python:3.8-buster

RUN apt-get update &&\
    apt-get install -y postgresql-client &&\
    rm -rf /var/lib/apt/lists/
RUN pip install gunicorn 
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
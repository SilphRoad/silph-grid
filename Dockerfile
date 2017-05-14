FROM python:3.5

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["python", "app.py"]

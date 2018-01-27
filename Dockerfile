FROM python:3.6

WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8081

CMD ["python", "app.py"]

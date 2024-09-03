FROM python:3.12-slim

ENV PYTHONBUFFERED=1

WORKDIR /CODE

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python","manage.py","runserver" ]
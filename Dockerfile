FROM python:3.10.6-buster

WORKDIR /prod

COPY vegatation vegatation
COPY setup.py setup.py
COPY requirements_prod.txt requirements.txt
COPY models models

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uvicorn

CMD uvicorn vegatation.api.fast:app --host 0.0.0.0 --port $PORT

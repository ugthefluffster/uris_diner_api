FROM python:3.11.3-slim

WORKDIR /uris_diner__api_root

COPY . .

RUN pip install -r requirements.txt

CMD python server.py
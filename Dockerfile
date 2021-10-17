FROM python:3.9-slim

COPY requirements.txt .
COPY ./ ./

WORKDIR /etl_challenge

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./main.py", "--host=0.0.0.0", "--reload"]
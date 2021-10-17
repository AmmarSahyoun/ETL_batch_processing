FROM python:3.9

WORKDIR /etl_challenge

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "./main.py"]
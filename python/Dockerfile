FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY appMarketing.xlsx appMarketing.xlsx 
COPY main.py main.py

CMD ["python", "main.py"]

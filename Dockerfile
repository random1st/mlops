FROM python:3.11

WORKDIR /app

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]

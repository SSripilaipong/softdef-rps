FROM python:slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5002
CMD ["python", "main.py"]

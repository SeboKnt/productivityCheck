FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env .
COPY *.py .
CMD ["python", "main.py"]


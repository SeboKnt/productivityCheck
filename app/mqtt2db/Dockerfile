FROM python:3.9
LABEL org.opencontainers.image.source https://github.com/seboknt/productivityCheck
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env .
COPY *.py .
CMD ["python", "main.py"]


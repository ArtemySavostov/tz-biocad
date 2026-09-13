FROM python:3.12-slim

WORKDIR /app
COPY app.py ./app.py

EXPOSE 32777

CMD ["python", "-u", "app.py"]

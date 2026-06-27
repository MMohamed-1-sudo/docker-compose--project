FROM python:3.12-slim

WORKDIR /app

COPY ..
RUN pip install flask redis
EXPOSE 5002
CMD ["python", "app.py"]
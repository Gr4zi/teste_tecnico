FROM python:3.9-slim
WORKDIR /app
COPY app.py /app/app.py
RUN pip install --no-cache-dir logging
CMD ["python", "app.py"]
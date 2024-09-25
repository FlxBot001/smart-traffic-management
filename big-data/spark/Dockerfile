FROM python 3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cachee-dir-r requirements.txt

CMD ["python", "traffic_pipeline.py"]

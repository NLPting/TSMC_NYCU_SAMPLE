FROM python:3.6.15-slim
COPY . /sample_crawler
WORKDIR /sample_crawler
RUN pip install -r ./requirements.txt
CMD ["python","crawler_sample.py"]
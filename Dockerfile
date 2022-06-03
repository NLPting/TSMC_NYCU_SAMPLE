FROM alpine:3.16
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-wheel \
    py3-pandas \
    py3-requests \
    py3-beautifulsoup4 \
    py3-openpyxl

RUN pip install \
    requests-html \
    nltk

RUN python3 -m nltk.downloader -d /usr/share/nltk_data -q all

COPY . /sample_crawler
WORKDIR /sample_crawler

CMD ["python3", "crawler_sample.py"]

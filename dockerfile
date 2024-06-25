FROM python:3.10-buster

# RUN apt-get update && apt-get install -y bash

WORKDIR /GA4

# RUN python -m venv venv

# # 啟用虛擬環境
# SHELL ["bash", "-c"]
# RUN source venv/bin/activate

RUN pip install google-analytics-data

ENV GOOGLE_APPLICATION_CREDENTIALS=/GA4/GA4/credentials.json
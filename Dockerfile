FROM python:3.7-slim-stretch
MAINTAINER Mohsin Mohammed "mohsinmohammed2019@outlook.com"
RUN mkdir /app && chmod 755 /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["snapCode.py"]
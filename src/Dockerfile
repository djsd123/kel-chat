FROM --platform=linux/amd64 python:3.11.2-slim
MAINTAINER Mikael Allison <mikellallison@hotmail.com>
WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

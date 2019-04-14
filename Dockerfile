FROM tensorflow/tensorflow:latest-py3
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./backend/index.py

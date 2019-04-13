FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk add --update git
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./backend/index.py

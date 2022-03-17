FROM python:3.7
LABEL maintainer="oo.vivian@hotmail.com"


WORKDIR /Project_hot_news_api
COPY . /Project_hot_news_api/

RUN pip install -r requirements.txt

WORKDIR /Project_hot_news_api/hot_news_project

VOLUME /Project_hot_news_api
EXPOSE 8000 

#ENTRYPOINT [ "sh", "docker-entrypoint.sh" ]

CMD python manage.py runserver 0.0.0.0:8000

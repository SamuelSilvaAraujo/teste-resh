FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt start_server.sh /
RUN pip install -r /requirements.txt

ENV APP_HOME=/var/www
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN chown -R www-data:www-data ${APP_HOME}

CMD ["/start_server.sh"]

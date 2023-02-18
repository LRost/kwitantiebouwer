FROM python:3.10

RUN set -ex
RUN apt update
RUN apt install -y build-essential
RUN python -m venv /env
RUN /env/bin/pip install --upgrade pip
RUN /env/bin/pip install -r /app/requirements.txt
RUN python manage.py migrate

ADD . /app
WORKDIR /app
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH


EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "--timeout",  "60000", "--preload", "kwitantiebouwer.wsgi", "--access-logfile", "-"]

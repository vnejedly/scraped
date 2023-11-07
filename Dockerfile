FROM python

COPY scraped /app/scraped
COPY requirements.txt /app/requirements.txt

COPY .env /app/.env

RUN pip install -r /app/requirements.txt
RUN pip install gunicorn

WORKDIR /app/scraped

CMD python manage.py api_load_real_estates && gunicorn --bind 0.0.0.0:8080 scraped.wsgi

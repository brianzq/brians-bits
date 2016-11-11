FROM brian/python:latest

RUN apt-get update -y && apt-get install -y nginx
# python packages
RUN pip install django
RUN pip install uwsgi
RUN pip install supervisor
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8
# pull package
RUN pip install git+https://github.com/brianzq/mysite#egg=mysite-0.1
RUN mkdir -p /data/scripts/ /data/static
COPY ./scripts/nginx/site.conf /etc/nginx/sites-enabled/
COPY ./scripts/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./scripts/supervisor/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf
COPY ./scripts/supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
RUN sed -i -e 's@#NAME#@my-site@' /etc/supervisor/conf.d/uwsgi.conf
COPY ./scripts/uwsgi/uwsgi.ini /data/scripts/uwsgi.ini
COPY ./scripts/uwsgi/uwsgi_params /data/scripts/uwsgi_params
RUN sed -i -e 's@#WSGI#@mysite.wsgi:application@' /data/scripts/uwsgi.ini
#RUN /usr/bin/mysiteadmin migrate
#RUN /usr/bin/mysiteadmin collectstatic --noinput

CMD ['/usr/bin/supervisord']

EXPOSE 80

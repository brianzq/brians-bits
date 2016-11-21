FROM ubuntu:latest

# system packages
RUN apt-get update -y && apt-get install -y \
    nginx \
    git \
    python-dev \
    python-pip \
    python3 \
    vim

# python packages
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN pip install django
RUN pip install uwsgi
RUN pip install supervisor
RUN pip install supervisor_checks
RUN pip install supervisor-stdout
RUN pip install setuptools_git
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

# pull mysite package
RUN pip install git+https://github.com/brianzq/mysite#egg=mysite-0.1

# configuration
RUN mkdir -p /data/scripts/ /data/static
RUN mkdir -p /etc/supervisor/conf.d/
RUN rm /etc/nginx/sites-enabled/default
COPY ./scripts/nginx/site.conf /etc/nginx/sites-enabled/
COPY ./scripts/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY ./scripts/supervisor/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf
COPY ./scripts/supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
RUN sed -i -e 's@#NAME#@my-site@' /etc/supervisor/conf.d/uwsgi.conf
COPY ./scripts/uwsgi/uwsgi.ini /data/scripts/uwsgi.ini
COPY ./scripts/uwsgi/uwsgi_params /data/scripts/uwsgi_params
RUN sed -i -e 's@#WSGI#@mysite.wsgi:application@' /data/scripts/uwsgi.ini

# django setup
RUN /usr/local/bin/mysiteadmin migrate
RUN /usr/local/bin/mysiteadmin collectstatic --noinput

# run supervisor
CMD /usr/local/bin/supervisord

EXPOSE 80

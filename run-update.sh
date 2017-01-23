#!/usr/bin/env bash

# build new docker image
docker build -t brianzq/mysite https://github.com/brianzq/mysite.git
# remove previous containers
docker rm -f $(docker ps -a -q)
# run new docker image
docker run -d -p 80:80 brianzq/mysite

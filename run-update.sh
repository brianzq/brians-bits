#!/usr/bin/env bash

# build new docker image
docker build -t brianzq/brians-bits https://github.com/brianzq/brians-bits.git
# remove previous containers
docker rm -f $(docker ps -a -q)
# run new docker image
docker run -d -p 80:80 brianzq/brians-bits

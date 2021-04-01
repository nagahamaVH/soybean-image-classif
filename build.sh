#!/bin/bash

export CURRENT_UID=$(id -u):$(id -g)

COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build --progress plain

if [ ! -d runtime ]; then
    mkdir runtime
fi

if [ ! -d app ]; then
    mkdir app
fi

if [ ! -d app/src ]; then
    mkdir app/src
fi

if [ ! -d app/src ]; then
    mkdir app/data
fi

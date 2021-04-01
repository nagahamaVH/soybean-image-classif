#!/bin/bash

export CURRENT_UID=$(id -u):$(id -g)
echo "UID $CURRENT_UID"
docker-compose up

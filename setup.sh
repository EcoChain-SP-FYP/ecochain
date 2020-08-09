#!/bin/sh

sudo apt update && sudo apt install docker.io docker-compose -y
echo "Now run 'docker-compose up -d' to launch both EcoChain as well as it's dashboard"

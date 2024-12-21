#!/bin/bash

ssh-keygen -t rsa -b 4096 -C "$1"
eval $(ssh-agent -s) >> /dev/null 2>&1
cat ~/.ssh/id_rsa.pub

#!/bin/bash

filename=`date +'%y-%m-%d-%H-%M-%S'`
echo "Hi this is a record" > "/var/log/history/${filename}"
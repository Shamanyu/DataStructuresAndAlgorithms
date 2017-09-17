#!/bin/bash

while true
do 
    eject 
    sleep $(($RANDOM % 240))
    eject -t
    sleep $(($RANDOM % 20))
done

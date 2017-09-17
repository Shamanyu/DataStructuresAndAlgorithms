#!/bin/bash

influx -database  'GreyOrange' -format 'csv' -execute='Select * from flow_events' > /home/gor/flow_events.txt

scp -r /home/gor/flow_events.txt gor@172.21.161.158:~ || echo "apj0702"

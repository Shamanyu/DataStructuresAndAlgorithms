#!/bin/bash

influx -database  'GreyOrange' -format 'csv' -execute='Select * from flow_events' > flow_events.txt

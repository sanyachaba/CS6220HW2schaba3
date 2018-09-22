#!/usr/bin/env bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.12.0.jar \
 -file /home/cloudera/BDS/mapper-part3.py \
 -mapper /home/cloudera/BDS/mapper-part3.py \
 -file /home/cloudera/BDS/reducer-1.py \
 -reducer /home/cloudera/BDS/reducer-1.py \
 -input /user/cs6220/obama-visitor-logs/* \
 -output /user/cs6220/BDS-part1-temp1

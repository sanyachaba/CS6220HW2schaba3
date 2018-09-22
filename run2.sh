#!/usr/bin/env bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.12.0.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D stream.map.output.field.separator='\t' \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.map.output.key.field.separator='\t' \
    -D mapreduce.partition.keycomparator.options='-k1,1nr' \
    -D mapreduce.job.reduces=12 \
 -file /home/cloudera/BDS/mapper-2.py \
 -mapper /home/cloudera/BDS/mapper-2.py \
 -file /home/cloudera/BDS/reducer-2.py \
 -reducer /home/cloudera/BDS/reducer-2.py \
 -input /user/cs6220/BDS-part1-temp1/part-00000 \
 -output /user/cs6220/BDS-part1-temp2

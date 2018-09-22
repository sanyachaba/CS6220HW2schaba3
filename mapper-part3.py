#!/usr/bin/env python

import sys

i = 1
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    if i != 1:
        last_name = words[0]
        first_name = words[1]
        name_mid = words[2]
        visitee_last_name = words[19]
        visitee_first_name = words[20]
        if ((visitee_last_name != '' or visitee_first_name != '') and (last_name != '' or first_name != '')):
            name_string = "Visitor " + last_name + ',' + first_name + ',' + name_mid + " Visitee " + visitee_last_name + ',' + visitee_first_name 

            print '%s\t%s' % (name_string, 1)

    i += 1

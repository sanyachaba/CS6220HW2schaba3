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
        first_name = words[1]
        if (first_name != ''):
            name_string = first_name
            print '%s\t%s' % (name_string, 1)

    i += 1

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

        name_string = last_name + ',' + first_name + ',' + name_mid

        print '%s\t%s' % (name_string, 1)

    i += 1

    #     # write the results to STDOUT (standard output);
    #     # what we output here will be the input for the
    #     # Reduce step, i.e. the input for reducer.py
    #     #
    #     # tab-delimited; the trivial word count is 1
    #     print '%s\t%s' % (word, 1)

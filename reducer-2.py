#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('\t')
    # increase counters
    word_0 = str(words[0])
    word_1 = str(words[1])

    print '%s\t%s' % (word_0, word_1)

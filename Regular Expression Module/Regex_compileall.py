#!usr/bin/python

import re

text = 'ababbbbabbbabbabbabbbb'

for match in re.findall('ab',text):
    print("Found '%s'" % match)
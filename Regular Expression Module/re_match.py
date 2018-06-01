#!/usr/bin/python

import re

line = "python and perl are languages those are easy"
#(.) means any character in the string,(.*) everything in the line
matchObj = re.match(r'(.*) are(.*)', line , re.M | re.I)

if matchObj:
    print("matchObj.group() :", matchObj.group())
    print("matchObj.groups():", matchObj.groups())

else:
    print("No match found!")
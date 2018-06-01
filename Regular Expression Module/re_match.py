#!/usr/bin/python

import re

line = "python and perl are languages"

matchObj = (r'(.*) and', line , re.M | re.I)

if matchObj:
    print("matchObj.group() :", matchObj.group())
    print("matchObj.groups():", matchObj.groups())

else:
    print("No match found!")
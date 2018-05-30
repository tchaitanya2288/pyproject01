#!/usr/bin/python

import re

a = "ABCDEFabcdef123450"

b = "*&%@#!}{"

matchObj = re.match(r'(.*)@',b,re.M)

if matchObj:
    print('matchObj.group()',matchObj.group())

else:
    print("No matchObj found")


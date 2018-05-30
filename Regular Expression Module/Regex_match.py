#!usr\bin\python
import re

line = "Python and perl are programming languahes"

matchObj = re.match(r'(.*) and',line,re.M|re.I)

if matchObj:
    print("matchObj.group(): ",matchObj.group)
    print("matchObj.groups() ",matchObj.groups)

else:
    print("match not found")



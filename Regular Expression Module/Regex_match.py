#!usr\bin\python
import re

str ='python and perl are programming languahes'

matchobj = re.match(r'(.*) are',str,re.M|re.I)

if matchobj:
    print('matchobj.group():',matchobj.group)
    print('matchobj.groups()',matchobj.groups)

else:
    print("match not found")



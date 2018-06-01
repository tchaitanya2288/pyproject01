#!usr/bin/python

import re

str = "python is easy language,but it need's some easy practice"

matchsearch = re.search(r'(.*)easy(.*)',str,re.M | re.I)

if matchsearch:
    print("matchsearch.group() :", matchsearch.group())
    print("matchsearch.group(1) :", matchsearch.group(1))
    print("matchsearch.group(2) :", matchsearch.group(2))
    print("matchsearch.groups() :", matchsearch.groups())
#print("matchsearch.group(3) :", matchsearch.group(3)) ,it will through exception no such group

else:
    print("No search found")




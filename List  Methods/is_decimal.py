#!/usr/bin/python
str1 = "44"
print (str1.isdecimal())
str2 = u"695979"
print (str2.isdecimal())

#c = "\u0123456789" # decimal-radix numbers
#c = '\u2155'
#c = '\u214675'
#c = r'\u2155'
#c = u"77"
#c = "77"

c = u'77'  # 0-9
#print(c)
#print(c.isdecimal())

print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())

print(c.isdecimal(), c.isdigit(), c.isnumeric())
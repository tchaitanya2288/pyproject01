#!/usr/bin/python3
a = 20
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", id(a),id(b),id(c),type(c),c)

print('Value of c = a+b is',c)
c += a
print ("Line 2 - Value of c is ", id(a),id(b),id(c),type(c),"c + a", c , sep=':')

print('Value of c += a is',c)

c *= a
print ("Line 3 - Value of c is ", id(a),id(b),id(c),type(c),c )

print('Value of c *= a is',c)

c /= a 
print ("Line 4 - Value of c is ", id(a),id(b),id(c),type(c),c )
print('Value of c /= a is',c)

c %= a
print ("Line 5 - Value of c is ", id(a),id(b),id(c),type(c),c)

print('Value of c %= a is',c)

c **= a
print ("Line 6 - Value of c is ", id(a),id(b),id(c),type(c),c)

print('Value of c **= a is',c)

c //= a
print ("Line 7 - Value of c is ", id(a),id(b),id(c),type(c),c)
print('Value of c //= a is',c)
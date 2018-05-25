#!/usr/bin/python

A = []

for i in range(1000,2500):
    if (i%7==0)and(i%5!=0):
        A.append(str(i))

print(','.join(A))

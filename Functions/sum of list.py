#!/user/bin/python

def sumlist(numlist):
    sum=0
    for i in numlist:
        sum = sum+i
    return sum

print(sumlist([8,2,3,7,0]))
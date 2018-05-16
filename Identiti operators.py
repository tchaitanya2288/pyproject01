# Example : Identity operators in Python

x1 = 8
y1 = 8

x2 = "Praveen"
y2 = 'Praveen'

x3 = [22,33,44]
y3 = [22,33,44]

# Output: False
print(id(x1),id(y1),x1 is not y1)

# Output: True
print(id(x2),id(y2),x2 is y2)

# Output: False
print(id(x3),id(y3),x3 is y3)

print(id(x3),id(y3),x3 is not y3)

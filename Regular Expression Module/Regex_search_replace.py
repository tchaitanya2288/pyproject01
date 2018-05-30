#!/usr/bin/python3

import re

phone_number = "9902030405 # This is phone number"

print(phone_number)
#Delete Python-style comments
num = re.sub(r'#.*', "",phone_number)
print("phone number : ",num)
#Delete Python-style comments
num =re.sub(r'This',"",phone_number)
print("phone number : ",num)

#Remove anything other than digits
num = re.sub(r'\D',"",phone_number)
print("phone number : ",num)



#!/usr/bin/python3

str1 = "ABC123 ABC123 ABC123 ABC123 ABC123 ABC123"

print (str1.split())

print (str1.split('A'))
print (str1.split('123'))
print (str1 .split('ABC'))


"""
split(str="", num=string.count(str))
	Splits string according to delimiter str (space if not provided)
	and returns list of substrings; split into at most num substrings if given.
strLower = "this@is@a@lower@case@string"
splitString = strLower.split('@')
for i in splitString:
    print (i)
print("="*30)
"""


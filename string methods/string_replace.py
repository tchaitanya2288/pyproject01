#!/usr/bin/python

str = "python is scripting is and is programming is language"
print(str.replace("is", "was"))
str1 = "python is scripting is and is programming is language"
print(str1.replace("is", "was",3))


"""
26	replace(old, new [, max])
	Replaces all occurrences of old in string with new or at
	most max occurrences if max given.
"""
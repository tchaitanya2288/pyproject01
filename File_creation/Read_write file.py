#!/usr/bin/python

fileobject = open("C:\\Users\\wi10\\pyproject01.sample.txt","wb+")

fileobject.write("This is testing project")
print(fileobject)
fileobject("This is written by chaithanya")
print(fileobject)

fileobject = open("sample.txt")
filetext = fileobject.read()
print(filetext)
fileobject.close()

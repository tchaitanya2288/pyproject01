#!/usr/bin/python

with open("C:\\Users\\wi10\\pyproject01//File_creation//test_file.txt") as file:
    print(file.read())
    print(file.readlines())
    file.close()

with open("sample.txt",'w',encoding = 'utf-8') as f:
    f.write("This is my sample file\n")
    f.write("This file is written by chaithanya\n\n")
    f.write("This file contains no data\n")
    f.close()

with open("C:\\Users\\wi10\\pyproject01//File_creation//sample.txt") as f:
    print(f.read())

with open("C:\\Users\\wi10\\pyproject01//File_creation//test_file.txt") as f:
    print(f.read())










# !/usr/bin/python3
from tkinter import *

import tkinter

top = Tk()
top.geometry("500x500")

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.insert(7, "AWS")
Lb1.insert(8, "Dotnet")
Lb1.insert(9, "Java")
Lb1.insert(10, "SAP")

Lb1.pack()
top.mainloop()
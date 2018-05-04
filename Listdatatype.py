#Declaring list data types

#List is a mutable data type

#List can accepts any values Like strings,nums,special characters

#list start with zero called empty list

list1  = [23,13.45,67,89,12999]
list2  = ['sathvika',2012,'vikram',2014,'Born@India']
list3  = [3.6,"python",'start_date_23-april',14000]
list4  = ["praveen",1983,"dec_10",'ielts']

print(list1,type(list1),id(list1),len(list1))
print(list2,type(list2),id(list2),len(list2))
print(list3,type(list3),id(list3),len(list3))
print(list4,type(list4),id(list4),len(list4))

print(" ")
print(list2,len(list2))
print(' ')
list2[4] = 'Born@India'

del list3[2]
print(" ")
print(list3)

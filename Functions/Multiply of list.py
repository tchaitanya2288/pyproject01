#!/user/bin/python

def multipylist(list):
    multiple=1
    for i in list:
        multiple=multiple*i
    return multiple

print(multipylist([5, 2, 3, 5, 5]))
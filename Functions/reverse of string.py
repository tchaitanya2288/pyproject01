def rev_str(a_str):
    new_str = ''
    index   = len(a_str)
    while index:
        index -= 1                    # index = index - 1
        new_str += a_str[index] # new_string = new_string + character
    return new_str
print(rev_str('abcd1234'))
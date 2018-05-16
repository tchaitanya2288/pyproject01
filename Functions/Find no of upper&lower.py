def up_low(string):
  upper = 0
  lower = 0
  for char in string:
    if char.islower():
      lower += 1
    elif char.isupper():
      upper +=1
    else:
      pass
  return(upper, lower)

print(up_low('Python World And AWS Cloud'))


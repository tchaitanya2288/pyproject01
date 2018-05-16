def unique_list(list):
  a = []
  for x in list:
    if x not in a:
      a.append(x)
  return a

print(unique_list([1,2,3,3,3,3,4,5])) 
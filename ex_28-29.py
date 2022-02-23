# ex_28
str = input()

for i in range(len(str)-1):
  print(str[i]+str[i+1])

# ex_29
str2 = input()

for i in range(len(str2)):
  if str2[i].isupper():
    print('Yes')
  else:
    print('No')

data = input()
ans =[]

for i in data:
    if i.isupper():
        ans.append(i.lower())
    else:
        ans.append(i.upper())

for i in ans:
    print(i, end='')
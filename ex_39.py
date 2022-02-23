""""
data = list(input().split())

for i in range(len(data)):
  data[i] = data[i].replace('b', 'n')
  data[i] = data[i].replace('q', 'e')

for i in range(len(data)):
  print(data[i], end = ' ')
"""

data = input()

print(data.replace('q','e').replace('b','n'))
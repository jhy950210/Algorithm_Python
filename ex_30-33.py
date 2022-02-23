# ex_30
str = input()
find_str = input()

print(str.find(find_str))

# ex_33
reverse = list(map(int,input().split()))

for i in range(len(reverse)-1, -1, -1):
  print(reverse[i], end = ' ')
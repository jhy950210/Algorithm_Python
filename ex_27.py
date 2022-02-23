names = list(input().split())
scores = list(map(int, input().split()))

s = dict()

for i in range(len(names)):
  s[names[i]] = scores[i]


keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))

print(s)
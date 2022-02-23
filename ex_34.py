data = list(map(int, input().split()))

if data != sorted(data):
  print('No')
else:
  print('Yes')
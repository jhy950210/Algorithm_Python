max_weight = int(input('제한 몸무게 : '))
friend = int(input('친구들 수 : '))
count = 0
weight = 0;

for i in range(friend):
  weight += int(input('친구 몸무게 : '))

  if weight > max_weight:
    break

  count += 1

print(count)
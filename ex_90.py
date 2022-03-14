import random as r
from itertools import permutations

l = [chr(i) for i in range(65, 91)]

total_medicine = []
medicine = []

#이해를 돕기 위한 예제
for i in range(100):
    total_medicine.append(r.sample(l, 8))

data = input()

find_string = []

per = [i for i in permutations(data,4)]

for i in per:
    i = ''.join(i)
    find_string.append(i)

answer = []

for i in total_medicine:
    i = ''.join(i)

    for j in find_string:
        if i.find(j) != -1:
            answer.append(i)
            break

print(answer)
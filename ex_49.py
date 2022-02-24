data = list(map(int, input().split()))
max = data[0]

for i in range(1, len(data)):
    if data[i] > max:
        max = data[i]

print(max)
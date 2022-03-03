data = input()

start = data[0]
count = 1
result = ''

for i in range(1, len(data)):

    if data[i] == start:
        count += 1

        if i == len(data)-1:
            result += start + str(count)
    else:
        result += start + str(count)
        start = data[i]
        count = 1

print(result)
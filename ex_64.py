n = int(input())
count = 0

while n > 0:
    if n - 7 >= 0:
        n -= 7
        count += 1
    elif n - 3 >= 0:
        n -= 3
        count += 1
    else:
        count = -1
        break

print(count)
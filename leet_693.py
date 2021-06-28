n=5

b = format(n, 'b')
bOne = list(map(int,b))
result = True

for i in range(len(bOne)-1):
    if bOne[i] == bOne[i+1]:
        result = False

print(result)
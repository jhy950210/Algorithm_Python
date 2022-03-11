import itertools

data = input().split(',')
len = int(input())

print(list(map(''.join, itertools.combinations(data,len))))
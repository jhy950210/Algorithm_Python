name = list(input().split())
dish = list(map(int,(input().split())))

rank = {}
tmp_rank =[]

for i, j in zip(name,dish):
    tmp_rank.append([i,j])

tmp_rank = sorted(tmp_rank, key=lambda x:x[1], reverse=True)
count = 0

for i in range(len(tmp_rank)):
    rank[tmp_rank[i][0]] = i+1

print(rank)
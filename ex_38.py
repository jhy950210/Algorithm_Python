data = list(map(int,input().split()))

data.sort(reverse=True)

count = 1
rank = 1


for i in range(1,len(data)):
  if data[i] != data[i-1]:
    rank += 1

  if rank == 4:
    break

  count += 1
  
    
print(count)
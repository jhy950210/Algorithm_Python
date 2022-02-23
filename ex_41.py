data = int(input())
val = True

for i in range(2, data):
  if( data % i == 0):
    val = False
    break
  
if val == True:
  print('YES')
else:
  print('NO')
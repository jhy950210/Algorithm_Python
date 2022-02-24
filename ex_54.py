def isSequence(e):
    e.sort()

    for i in range(len(e)-1):
        if e[i+1] - e[i] > 1:
            return False

    return True

data = list(map(int,input().split()))

if isSequence(data) == True:
    print('Yes')
else:
    print('NO')   
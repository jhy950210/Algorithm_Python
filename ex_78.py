data = input().split()

n = data[0]
k = data[1]


def sol(n, k):
    idx = 0

    list = [i for i in range(1,n+1)]

    while len(list) > 2:
        if idx > len(list) - 1:
           idx -= len(list)

        list.pop(idx) 
        idx += k
        idx -= 1
    
    print(list)

sol(int(n), int(k))

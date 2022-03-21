data = [[0 for i in range(4)] for j in range(5)]

print(data)


def sol(l, d):
    
    result = [0]
    point = 0

    while d:
        now = d.pop(0) - 1

        for i in range(len(l)):
            if l[i][now] != 0:
                if result[len(result)-1] == l[i][now]:
                    point += l[i][now]*2
                    result.pop()
                    
                else:
                    result.append(l[i][now])
                    
                l[i][now] = 0
                break
            else:
                if i == len(l)-1:
                    point -= 1

    return point

퍼즐판 = [[0, 0, 0, 0], [0, 1, 0, 3], [2, 5, 0, 1], [2, 4, 4, 1], [5, 1, 1, 1]]
조작 = [1, 1, 1, 1, 3, 3, 3] 
print(sol(퍼즐판,조작))
def solution(stamp, k):
    result = [[0 for i in range(len(stamp))] for j in range(len(stamp))]

    # 1
    # (0,0) -> (0,3) / (0,1) -> (1,3) / (0,2) -> (2,3) / (0,3) -> (3,3)
    # (1,0) -> (0,2) / (1,1) -> (1,2) / (1,2) -> (2,2) / (1,3) -> (3,2)
    # (2,0) -> (0,1) / (2,1) -> (1,1) / (2,2) -> (2,1) / (2,3) -> (3,1)
    # [i][j] -> [j][len-1-i] : 90도

    # 2
    # (0,0) -> (3,3) / (0,1) -> (3,2) / (0,2) -> (3,1) / (0,3) -> (3,0)
    # (1,0) -> (2,3) / (1,1) -> (2,2) / (1,2) -> (2,1) / (1,3) -> (2,0)
    # [i][j] -> [len-1-i][len-1-j]
 

    if k % 4 == 1:
        for i in range(len(stamp)):
            for j in range(len(stamp)):
                result[j][len(stamp)-1-i] = stamp[i][j]
        
        result = [[c+d for c,d in zip(a,b)] for a,b in zip(result, stamp)]
    
    elif k % 4 == 2:
        for i in range(len(stamp)):
            for j in range(len(stamp)):
                result[len(stamp)-1-i][len(stamp)-j-1] = stamp[i][j]

        result = [[c+d for c,d in zip(a,b)] for a,b in zip(result, stamp)]
    
    return result

도장 = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]

회전 = 2
print(solution(도장,회전))
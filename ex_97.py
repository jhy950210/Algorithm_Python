from numpy import empty


배달원 = 3
배달시간 = [1,2,1,3,3,3]

def solution(n,l):
    time = 0
    deliver = []

    for _ in range(n):
        now = l.pop(0)
        deliver.append(now)

    while True:
        time += 1
        length_deliver = len(deliver)

        for i in range(length_deliver):
            
            deliver[i] -= 1

            if deliver[i] == 0 and l:
                deliver[i] = l.pop(0)
                
                
        if not l:
            break
    
    time += max(deliver)

    return time


print(solution(배달원,배달시간))
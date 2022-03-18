def solution(dense, power):
    answer = []

    for i in power:
        before_len = len(answer)

        for j in range(i-1, len(dense), i):
            if dense[j] == 0:
                answer.append('fail')
                break
            else:
                dense[j] -= 1
        
        if before_len == len(answer):
            answer.append('pass')
    
    return answer

돌의내구도 = [1, 2, 1, 4, 5, 2]
토끼의점프력 = [2, 1, 3, 1]

print(solution(돌의내구도, 토끼의점프력))
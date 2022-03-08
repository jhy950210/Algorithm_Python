def sol(n):
    """
    3의 개수 == 숫자의 길이
    """
    answer = 0

    for i in range(1,n+1):
        count = str(i).count('3') + str(i).count('6') + str(i).count('9')
        length = len(str(i))

        if count == length:
            answer += 1
    
    return answer

print(sol(93))
    
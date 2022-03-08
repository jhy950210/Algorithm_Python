a = input()
b = input()

def sol(string):
    result = []

    for i in range(1, len(string)+1):
        for j in range(i):
            result.append(string[j : j + len(string) - i + 1])

    return result

list1 = set(sol(a))
list2 = set(sol(b))

answers = list1.intersection(list2)

answer = max(answers,key=len)

print(answer, len(answer))

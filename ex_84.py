from audioop import reverse


data = int(input())

def find_max_num(num,k):
    num_split = []

    while num > 0:
        num_split.append(num%10)
        num //= 10

    num_split.sort(reverse=True)

    num_split = list(map(str,num_split[:k]))

    return ''.join(num_split)

print(find_max_num(data,2))
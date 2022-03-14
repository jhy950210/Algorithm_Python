point = [5,2,3,1,2,5]
dish = 1

def sol(rank, target_idx):
    count = -1
    target_rank = point[target_idx-1]

    while True:
        count += 1

        now = rank.pop(0)
        min_value = min(i for i in rank)

        if now > min_value:
            rank.append(int(now))

        elif now == target_rank:
            return count

print(sol(point,dish))

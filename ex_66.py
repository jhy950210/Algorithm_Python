탑 = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
규칙 = "ABD"
answer = []

for data in 탑:
    res = []

    for i in 규칙:
        if data.find(i) != -1:
            res.append(data.find(i))
        
    sorted_res = sorted(res)

    if res == sorted_res:
        answer.append("가능")
    else:
        answer.append("불가능")

print(answer)
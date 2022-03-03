def cal(a, b):
    result =[]

    if len(a[0]) == len(b):
        for i in range(len(b)):
            result.append([0]*len(a[0]))
            
    for i in len(a):
        for j in len(b):
            #c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
            #c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]

            #c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]

            result[i][j] += a[i][k] * b[k][j]
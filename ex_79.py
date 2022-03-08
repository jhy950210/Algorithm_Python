from multiprocessing.sharedctypes import Value


l = [10, 20, 25, 27, 34, 35, 39] #기존 입력 값
n = int(input('순회 횟수는 :'))

def rotate(inL, inN):
    orginalList = inL.copy()
    res = []

    for _ in range(inN):
        a = inL.pop()
        inL.insert(0,a)

    
    for i,j in zip(orginalList, inL):
        res.append(abs(i-j))
    
    idx = res.index(min(res))
    print('index :', idx)
    print('value :', orginalList[idx], inL[idx])

rotate(l, n)
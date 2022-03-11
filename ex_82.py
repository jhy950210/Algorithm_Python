def math(e):
    count = 0
    if e.count('(') != e.count(')'):
        print('Not Equal')
        return False

    for i in e:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        
        if count < 0:
            print('Non Mathmatic')
            return False
    
    return True

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break
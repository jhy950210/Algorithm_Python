student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']

student.sort()

for number,name in enumerate(student):
    print('번호: {}, 이름: {}'.format(number+1, name))
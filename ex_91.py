import random  as r

student_score = []
class_score = []
total_score = []

for j in range(7):
    class_score = []
    for k in range(30):
        student_score = []
        for i in range(5):
            student_score.append(r.randint(1, 100))
        
        class_score.append(student_score) 
    total_score.append(class_score)

class_average = 0
first_in_class = 0
total_average = 0

#print(student_score, len(student_score))  
#print(class_score, len(class_score))  
#print(total_score, len(total_score))  
count = 0

for i in total_score:
    count += 1
    class_average = 0

    for j in i:
        student_average = sum(j) // 5

        first_in_class = max(first_in_class, student_average)

        class_average += student_average
    
    class_average //= 30
    total_average += class_average

    print(count,'반 평균 :', class_average, ',', count, '반 1등 점수 :', first_in_class)

print('전체 평균 :', total_average // 7)
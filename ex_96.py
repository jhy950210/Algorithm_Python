orignal_land = [] #입력받은 텃밭 리스트
after_land = [] #텃밭을 가꾼 후 저장된 리스트

for i in range(5):
    orignal_land.append(input('텃밭을 입력하세요 :').split(' '))


for i in range(5):
    for j in range(5):
        if orignal_land[i][j] == 1:
            n = j # 바위 전까지의 가로 길이
            
print(after_land)
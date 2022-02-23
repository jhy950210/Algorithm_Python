# ex_02
l = [200, 100, 300]

l.insert(2,10000)
print(l)

# ex_03, ex_04
l = [100, 200, 300]
a = 'p'
print(type(a))

# ex_05
a = 10
b = 2

for i in range(1, 5, 2):
  a += i

print(a+b)

# ex_06
print(bool(1))

# ex_08
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight'])

# ex_09
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')
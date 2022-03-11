value ='''0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0'''

print(value.split('\n'))
sp = value.split('\n')
count = 0

for i in sp:
    sp[count] = i.replace('1', 'f').split(' ')
    count += 1

count = 0
print(sp)

for s in sp:
    for i in s:
        if i =='f':
            search = s.index(i)
            if search > 0:
                s[search-1] = '*'
            if search < 4:
                s[search+1] = '*'
            if count > 0:
                sp[count-1][search] = '*'
            if count < 4:
                sp[count+1][search] = '*'
    
    count += 1

for i in sp:
    print(i)
nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900
    }

korea = nationWidth['korea']
nationWidth.pop('korea')

gap = max(nationWidth.values())
l = list(nationWidth.items())
item = 0

for i in l:
    if gap > abs(i[1] - korea):
        gap = abs(i[1] - korea)
        item = i
        
print(item[0], item[1] - korea)
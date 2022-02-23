data = input().split()

data_set = set(data)
data_dict = {}

for key in data_set:
  data_dict[key] = data.count(key)

max_key = max(data_dict, key=data_dict.get)
max_value = str(max(data_dict.values()))

print(max_key + '(이)가 총 ' + max_value + '표로 반장이 되었습니다.')
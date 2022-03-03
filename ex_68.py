def bus_time_check(bus_time_table, current_time):
    split_current_time = list(map(int,current_time.split(':')))
    answer = []

    for data in bus_time_table:
        split_bus_time_table = list(map(int,data.split(':')))

        if split_bus_time_table[0] < split_current_time[0]:
            answer.append('지나갔습니다.')
        elif split_bus_time_table[0] == split_current_time[0] & split_bus_time_table[1] < split_current_time[1]:
            answer.append('지나갔습니다.')
        else:
            minutes = (split_bus_time_table[0] * 60 + split_bus_time_table[1]) - (split_current_time[0] * 60 + split_current_time[1])
            hour = minutes // 60
            minute = minutes - hour * 60
            answer.append('{}시간 {}분'.format(hour, minute))
    return answer

print(bus_time_check(["12:30", "13:20", "14:13"], "12:40"))


from datetime import datetime
count_error = 0
count_info = 0
count_warning = 0
dates = []
with open('../log.txt', 'r', encoding='utf-8') as file:
    for i in file:
        parts = i.split()
        print(parts)

        date_str = parts[0]
        log_type = parts[1]

        dates.append(datetime.strptime(date_str,'%Y-%m-%d'))


        if log_type == 'ERROR':
            count_error += 1
        elif log_type == 'INFO':
            count_info += 1
        elif log_type == 'WARNING':
            count_warning +=1

print(f'Кол-во ERROR - {count_error}\nКол-во INFO - {count_info}\nКол-во WARNING - {count_warning}')

# print(dates)

print(f'Самая раняя дата {min(dates).date()}')
print(f'Самая поздняя дата {max(dates).date()}')

    # s = file.readlines()
    # print(s).split


# dates = [datetime.strptime(line.strip(), '%Y.%m.%d') for line in s]
#
# print(min(dates).strftime('%Y.%m.%d'))


#     s = file.read().title()
#     ls = s.split()
#
# print(ls)
# ls.sort()


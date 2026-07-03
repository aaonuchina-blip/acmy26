from datetime import datetime, date, timedelta, time, UTC

# t = time(12)
# print(t)
# t = time(12, 30)
# print(t)
# t = time(12, 30, 15)
# print(t)
# d = date(2020,12,31)
# print(d)
# dd = date.today()
# print(dd)
# # dt = dd + time нельзя делать так, т.к. разные форматы данных
# dt = datetime.combine(dd, t)
# print(dt)
#
# print(dd - d)
# current_date = datetime.now
# print(current_date)
# # inp_date = input('Введите дату(дд.мм.гггг)')
# # dt = datetime.strpftime(inp_date,'%d.%m.%Y')
# print(dt)
# # print(inp_date)
# # print(current_date - dt)
# # print((current_date - dt).days)
# # print(type((current_date - dt).days))
# # current_date_str = datetime.strftime('%d.%m.%Y')
# # print(current_date_str)
# # print(datetime.strptime('12/03/1987 16:44', '%d.%m.%Y'))
# # print(datetime.strptime('12/03/1987 16:44', '%d.%m.%Y'))
# # print(current_date.strftime('%A %d %B %Y %I:%M %p '))
# print(current_date.replace(year=2033, microsend=0))

from datetime import datetime, date, timedelta, time
#
# t = time(12)
# # t = time(25)  # будет ошибка нельзя вводить время вне диапазона
# print(t)
# t = time(12, 30)
# print(t)
# t = time(12, 30,15)
# print(t)
# d = date(2020, 12, 31)  # соблюдаем порядок год, месяц, день
# print(d)
# # dd = date(2026, 3, 23)
# dd = date.today()
# print(dd)
# dt = dd + time  - нельзя разные типы данных
# dt = datetime.combine(dd, t)
# print(dt)
# print(dd - d)
# current_date = datetime.now()
# print(current_date)
# # inp_date = input('Введите дату (дд.мм.гггг): ')
# # print(inp_date)
# # dt = datetime.strptime(inp_date, '%d.%m.%Y')
# print(dt)
# print((current_date - dt))
# print((current_date - dt).days)
# curr_date_str = current_date.strftime('%d.%m.%Y')
# print(current_date.strftime('%A %d %B %Y %I:%M %p '))
# print(current_date.replace(year=2033, microsecond=0))
# print(datetime.today())
# print(datetime.now(UTC))
# tt = curr_date
#
# print(current_date.weekday())
# print(current_date.isoweekday()) # номер дня недели начиная c 1 (понедельник)
# print(current_date.isocalendar())

# days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб','Вс']
# print(days_of_week[current_date.weekday()])

# monthRu = ['', 'Янв', 'Фев', 'Март', 'Апрель', 'Май', 'Июнь','Июль''Авг']
# print(monthRu[current_date.month])
birthdate = input('Введите дату рождения в формате (дд.мм.гггг): ')
birthdate = datetime.strptime(birthdate, '%d.5m.%Y')
birthdate = birthdate.date()
current_date = date.today()
yyear = current_date.year
birthday = birthdate.replace(year=yyear)
if current_date > birthday:
    birthday = birthdate.replace(year= yyear + 1)
elif current_date == birthday:
    print(f' С др!')
    exit(0)
amount_days = (birthdate - current_date)
print(f' До дня рождения осталось {amount_days.days} дней/дня')
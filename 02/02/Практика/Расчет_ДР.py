from datetime import datetime, date, timedelta, time, UTC
try:
    birth_date = input('Введите дату вашего рождения в формате DD.MM.YYYY.: ')

    birth_date = datetime.strptime(birth_date,'%d.%m.%Y')
    current_date = datetime(2026,6,19)
    age = current_date.year - birth_date.year


    print(f'Вам {age} лет')

except Exception as e:
    print('Error', e)

# user_birthday = input('Введите дату вашего рождения в формате DD.MM.YYYY.: ')
# duser_birthday = datetime.strpftime(inp_date,'%d.%m.%Y')
# current_date = datetime.now
# y = current_date - user_birthday
# print(y)
s = ' ЗдравстВуйте, гоСти! '
s1 = '12345'


# print(s.islower()) #проверяет, состоят ли все буквенные символы строки из строчных букв (нижнего регистра)

# print(s.isupper())
# print(s.isalpha()) #проверка состоит ли строка исключительно из буквенных символов.
# print(s.isdigit())
# print(s.isnumeric() #проверяет, состоит ли строка исключительно из числовых символов
# print(s.isalnum()) #Возвращает True, если все символы в строке — это буквы или цифры, и строка состоит как минимум из одного символа
# print(s.startswith('Зд')) #проверяет, начинается ли строка с указанной подстроки
# print(s.endswith('Зд'))

# print(s.lower())
# print(s.upper())
# # s = s.upper()
# print(s.capitalize())
# print(s.title())
# print(s.rjust(50))
# print(s.rjust(50,'l'))

# print(s.ljust(40))
# print(s.center(40))

# items = [("Яблоки", 50), ("Бананы", 150), ("Молоко", 85)]
#
# for name, price in items:
#     # Имя выравниваем по левому краю, а цену по правому
#     print(name.ljust(10) + str(price).rjust(5))

# print(s.strip()) # удаляет все пробельные символы (пробелы, табуляцию, переводы строк) с обоих концов строки.
# s1 = "   Привет, мир!   "
# print(s1.strip())
# print(s.lstrip())
# print(s.rstrip())
#
# name = input("Введите имя: ").strip()
# print(f"Привет, {name}!")

# print(s)
# print(s.strip('! З и с т С о'))

# print(s.index('т', 12, 19))
# print(s.find('т', 12, 18))

# name = 'Andrey'
# symbol = input('Введите символ: ')
# ind = name.find(symbol)
# if ind != -1:
#     print(f'есть буква {symbol} в этом слове! index {ind}')
# else:
#     print(None)

# print(s.replace('т', 'Т'))  # O(n) - линейная
# print(s.replace(',', ''))
# print(s.replace('т', 'Т').replace('-', ''))
# res = s.replace(',', '')
# print(res) # в Python используется для вывода содержимого переменной res (result — результат) на экран
# print(type(res))
# ls = s.split(' ') # используется для разбиения строки s на список подстрок ls, используя пробел ' ' в качестве разделителя
# print(ls)
# print(' '.join(ls)) #бъединяет элементы списка строк ls в одну строку через пробел и выводит её на экран
#
# print(ls[1].split()) #берет элемент под индексом 1 из списка ls (который должен быть строкой) и разбивает его на список подстрок. По умолчанию разделителем выступает пробел.
#
# sl =[ls[0]] + ls[1].split()
# print(sl)
# print(', '.join(sl))

#Работа со срезами
# s = 'ЗдравстВуйте, гоСти! '
# res = s[11]
# res = s[1:12]
# res = s[::-1] #Start:stop:step
# print(res)
 #Задача на проверку слова полиндрома
# s1 = input('Введите слово: ')
#
# if s1 == s1[::-1]:
#     print('Это полиндром')
# else:
#     print('Это не полиндром')

# print(len(s))
# print(s.count('т'))

# s1 = "aaa bbb ccc ddd "
# s2 = '111 222 333 444 '
# res = ''
# for i in range(0, len(s1), 4):
#     res += s1[i:i+4] + s2[i:i+4]
# print(res)
# print(ord('F')) #показывает каккой код в юникоде у символа
# print(chr(71)) #из юникода преобразовать в символ
#
# s1 = input('Введите слово: ').strip()
# res = 'полиндром' if s1.lower() == s1[::-1].lower() else ' это не полиндром'  #тернарное выражение
# print(res)
# print(s1)

# s='-125x^2+158x-258=0'
# # d=b^2-4ac
# ind=s.find('x^2')
# if s[0]=='x':
#     a=1
# elif s[0]=='-' and s[1]=='x':
#     a=-1
# else:
#     a=int(s[:ind])
# print(a)
#
# s=s[ind+3:]
# ind=s.find('x')
# if s[0]=='+' and s[1]=='x':
#     b=1
# elif s[0]=='-' and s[1]=='x':
#     b=-1
# else:
#     b=int(s[:ind])
# print(b)
#
# s=s[ind+1:]
# ind=s.find('=')
# if s[0]=="=":
#     c=0
# else:
#     c=int(s[:ind])
# print(c)


# s = "-13x^2+2x-3=0"
#
# # d = b^2 - 4ac
#
# ind = s.find('x^2')
# if ind == 0  and s[0] != '-':
#     a = 1
#
# elif s[0] == '-' and s[1] == 'x':
#     a = -1
# else:
#    a = int(s[:ind])
# print(a)
#
# # ind1 = s.find('x',ind +1)
# s = s[ind+3:]
#
# ind = s.find('x^2')
# if is[0] != '-' or ind == 1 and s == '+':
#     b = 1
#
# elif s[0] == '-' and s[1] == 'x':
#     b = -1
# else
#    b = int(s[:ind])
# print(b)
# Код от преподавателя
# s = '-14x^2+x-3=0'
# # d = b^2 - 4ac
# ind = s.find('x')
# if ind == 0 and s[0] != '-':
#     a = 1
# elif s[0] == '-' and s[1] == 'x':
#     a = -1
# else:
#     a = int(s[:ind])
# print(a)
# # ind1 = s.find('x', ind + 1)
# s = s[ind+3:]
# ind = s.find('x')
# if ind == 0 and s[0] != '-' or ind == 1 and s[0] == '+':
#     b = 1
# elif s[0] == '-' and s[1] == 'x':
#     b = -1
# else:
#     b = int(s[:ind])
# print(b)

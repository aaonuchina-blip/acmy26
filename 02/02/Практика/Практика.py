# Задание 1
# n = 'Pyton - современный язык программирования! Многие начинают изучать Pyton! Мы уже пишем код на Pyton!'
#
# print(n.replace('Pyton', 'Java'))
# print(n.replace('!', ''))
# print(n.upper())
import random
from itertools import count

# t = input('Введите пароль,  не менее 8 символов, используйте хотябы одну заглавную букву и одну цифру: ')
# Задание 2

# while True:
#     passw = input('Введите пароль, используйте не менее 8 символов, используйте хотябы одну заглавную букву и одну цифру: ')
#     has_upper = False
#     has_digit = False
#
#     for i in passw:
#         if i.isupper():
#             has_upper = True
#         if i.isdigit():
#             has_digit = True
#
#     if len(passw) >= 8 and has_upper and has_digit:
#         print("Пароль принят")
#         break
#     else:
#         print("Пароль не соответствует требованиям")



numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]

# print(numbers[1::2])
# print(numbers[::-1])
# print(numbers)

# for id in numbers:
#     if id % 3 == 0:
#         numbers.remove(id)
# print(numbers)

# Задание 4
# fruits = ('яблоко', 'банан','груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# print(fruits.index('банан'))
# print(fruits.count("банан"))
#
#
# fruits2 = fruits * 2
# fr = fruits[:]
# fr3 = fruits + fr
# print(fr)
# print(fr3)
#
#
# fr4 = ()
# for i in fruits:
#     fr4 +=(i,i)
# print(fr4)

# Задание 5
# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
#
# res1 = set1.intersection(set2)
# res3 = set1.union(set2)
# res = set1.difference(set2)
# print(res1)
# print(res3)
# print(res)
# print(set1.issuperset(set2))

# d = {'Иван':[5, 4, 5],
#      'Петр':[3, 4, 4],
#      'Мария':[5, 5, 4],
#      'Ольга':[4, 5, 5]}
#
# d.setdefault('Анна',[5, 5, 5])
# d.pop('Петр')
#
# print(d)
#
#
# # print(list(d))
# # print(d.values())
#
# for k,v in d.items():
#     average = round(sum(v)/len(v),2)
#     print(k, average)
#
# # for d[keyword]:
# #     value = sum(value)/len(value)
# #     print(d)
#
# d2 = {'Елена':[5,4,5],'Дмитрий':[4,3,5],'Сергей': [5, 5, 5] }
#
# d3 = d | d2
# print(d3)

# Задание 7

# N1 = random.randint(1,100)
# print(N1)
# proba = 0
#
# while True:
#     n = int(input('Угадайте число от 1 до 100. Введите его: '))
#     proba += 1
#
#     if n < N1:
#         print('Больше')
#     elif n < N1:
#         print("Больше!")
#     else:
#         print(f'Угадала. Угадала с {proba} попытки.')
#         break

st = input('Введите символы: ')
abs1  = ( 'а, е, ё, о, и, э, я, у, ю, ы')
abs2 =  ('ц, к, н, г, ш, щ, з, х, ф, в, п, р, л, д, ж, ч, с, м, т, б')

abs1 = [i.strip() for i in abs1.split(',')]
print(abs1)

count_abs1 = 0
count_con = 0
count_digit = 0

for i in st:
    if i in abs1:
        count_abs1 +=1

    elif i.isalpha():
        count_con += 1
    elif i.isdigit:
        count_digit += 1
max_count = 0
max_ch = ' '
count = 0

for i in st:
    if i != ' ':
        count = st.count(i)
    if count > max_count:
        max_count = count
        max_ch = i

print(f'Количество гласных {count_abs1}\nкол-во согласных {count_con}\nкол-во цифр: {count_digit} \nсамый встречаемый символ "{max_ch}" встречается {max_count} раза')









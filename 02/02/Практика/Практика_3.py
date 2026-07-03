# def process_list(lst):
#     if not isinstance(lst, list):
#         print('Неверный тип данных')
#         return
#     new_list = []
#
#     for i in lst:
#         if i % 2 == 0:
#             new_list.append(i**2)
#         else:
#             new_list.append(i**3)
#     # if not isinstance(lst, list)
#     #     print('Неверный тип данных')
#     return new_list
#
# def pr_list(lst):
#     # if not isinstance(lst, list):
#     #     print('Неверный тип данных')
#     # return
#     new_list = []
#     new_list = [i**2  if i  % 2 == 0 else i**3 for i in lst]
#     return new_list
#
#
#     new_list = list(map(lambda i: i**2 if i % 2 == 0 else i**3, lst))
#     return new_list
#
#
# # new_list = []
# print(process_list([1, 3, 4, 5, 6]))
# print(pr_list([1, 3, 4, 5, 6]))
import random
from operator import truediv

# n = input('Введите "камень, ножницы, бумага", для того чтобы выйти напишите "Выход": ')
a = ['камень', 'ножницы', 'бумага']
n2 = random.choice(a)
print(n2)
while True:
    n = input('Введите "камень, ножницы, бумага", для того чтобы выйти напишите "Выход": ')
    a = ['камень', 'ножницы', 'бумага']

    if n == 'выход':
        print('Конец игры')
        break

    if n not in a:
        print('Выберите из списка')
        continue

    if n == n2:
        print('Ничья')
    elif ((n == 'ножницы' and n2 == 'бумага')
        or (n == 'бумага' and n2 == 'камень')
        or (n == 'камень' and n2 == 'ножницы')):
        print('Вы выиграли')
    else:
        print('Вы проиграли')




# if choice
# print()


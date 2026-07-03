import random
import time
from curses import wrapper


# def summator(x, y):
# def summator(z, y):
#     global x #можем менять переменную
#     # x = 30
#     x += 10
#     print('x - function - ', x)
#
# x = 1000
# summator(10, 20)
# print('modul x -', x)

def is_even(n: int) -> bool:
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    # return n % 2 == 0
    return not n % 2

def choice_even(x, y):
    for i in range(x,y + 1):
        if is_even(i):
            print(i, end = ' ')

# choice_even(100, 140)
# print(is_even(9))

# Рекурсия - функиця внутри себя вызывает себя. Мартрешка. В памчти две функции, которые работают по разым адресам
# Стек - последний зашел, а первым вышел.
# def nums2(n):
#     if n > 1:
#         nums(n - 1)
#     print(n)
#
# def nums2(n):
#     if n > 1:
#         nums2(n - 1)
#     print(n)

def nums(n):
    if n > 1:
        nums(n - 1)
    print(n)

# nums(7)
""""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1
n! = n * (n-1)!
"""

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(9))

# """0 1 1 2 3 5 8 13 21 34 55  Ряд Фибанче"""
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# # print(fib(10))
#
# def name(nm):
#     cnt = 0
#     def surname(snm):
#         nonlocal cnt
#         cnt +=1
#         print(cnt, nm, snm)
#     return surname
#
# zam = name('Mary') #замыкание
# zam('Ivanova') #замыкание
# zam('Romanova') #замыкание
# zam('Andreeva') #замыкание

# Декоратор
def in_out(func):
    def wrapper(*args, **kwargs):

# import time
# def time_run(func):
#     def wrap(*args, **kwargs):
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = round(end - start, 2)
#         print(f'Время выполнения {func.__name__} - {duration} сек.')
#     return wrap()
#
# def etalon(n):
#     print('START')
#     time.sleep(n)
#
# def decor(func):
#     def wrapper():
#         print('Before')
#         func()
#         print('After')
#     return wrapper()
# @decor
# def proba():
#     print("PROBA")

def sumr(x, y):
    return x + y

# decor(proba)()
# proba()
# etalon(3)

# n, *c, z, d = 1, 2, 3, 4 ,5, 6, 7
# print(t, c, 7)
result = sumr(random.randint(10, 10000)), random.randint(10, 10000)) / 0.35 * 0.56
print(result)
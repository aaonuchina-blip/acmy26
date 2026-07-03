# """Это подпрограмма которая ждет вызова для работы """
#
#
# def proba(): # Это процедура
#     print('Ura-ura')
#
#
# def summotor(x, y):  # параметры функции x, y
#     """Описание фунции, инструкция как пользоваться функцией"""
#     z = x + y   # тело функции
#     return z #возврат результата
#
#
# summotor('20', '15') #передача аргументов
#
# n = summotor(20,15)
# print(n)
# print(summotor('20', '15'))
# print(summotor.__doc__)

# def adding(x, y = 15):
#     return x + y
# def adding(*args, **kwargs): #разное количество позиционных и ключевых аргументов
#     print(args)
#     print(kwargs, list(kwargs.values()))
#     sumkw = sum(list(kwargs.values()))
#     return sum(list(args) + list(kwargs.values()))
#
# print (adding(2, 15, 33, x=12, y=33, z=18))
# print (adding())
# # print (adding(y = 30))


# n, m, *z = 5, 7, 44, 88, 99
# print(n, type(n), m)
# print(z, type(z))
# print(*z) # превращает список в переменную
d = {}
n = 3
for _ in range(n):
    name, *marks = input().split()
    marks = [int(m) for m in marks]
    d[name] = round(sum(marks) / len(marks), 2)
print(d)

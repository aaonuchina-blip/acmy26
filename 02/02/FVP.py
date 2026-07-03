""""Функции высшего порядка"""
from functools import reduce



def power(n):
    return n ** 2


lst = [1, 11, 11, 22, 55]
lss = [2, 3, 4, 5]
# #res = list(map(str, lst))
# res = list(map(power, lst)) # применяет функцию power ко всем элементам списка
# res1 = [power(i) for i in lst] #занимает 4 ячейки помяти
# res = list(map(lambda n: n ** 2, lst))
# # лямбда функция (унарная функция) возникает,
# # отрабатывает и изчезает после выполнения, позволяет экономить память
# res = list(map(lambda n, m: n - m, lst, lss))
# res = list(map(lambda n, m: n > m, lst, lss))
# #print(next(res))
# print(res)
# # print(res1)

# res = list(filter(lambda n: n % 2 == 0, lst))
# print(res)
def conc(x, y):
    print('X', x)
    print('Y', y)
    print('X+Y', str(x)+str(y))
    return str(x)+str(y)


city = ['Y', 'f', 'a', '-', 4, 5]
# print(' '.join(city))  нельзя так как присутствуют нестроковые обьекты
# res = reduce(lambda x, y: str(x) + str(y), city)
res = reduce(conc, city) #переключательб выбирает параметры из одной коллекции и обьединяет
print(res)



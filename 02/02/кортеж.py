"""Кортеж - tuple""" # упорядоченный набор неизменяемых объектов

tp = (33, 'Vasya', True, [1, 2])
tp1 = tp[:3]
print(tp1)
print(type(tp1)) # копия кортеж набор из трех значений
tp[-1][0] = 10 # если элемент ссылочный изменяемый объект можем изменить
print(tp, tp1, end='/n')
for i in tp:
    print(i)

PI = 3.1415926, # константу задаём как кортеж с единственным элементом
print(PI)
print(PI[0]) # значение константы вытаскивается только по индексу 0

tp = ('login', 'password')
print(id(tp))
buf = list(tp) # преобразовали в список, изменили
buf[-1] = 'new_password' ## и обратно в кортеж преобразовываем
tp = tuple(buf) # новый другой объект, tuple пересоздаётся
print(id(tp))
print(tp)

tp_sort = sorted(tp, reverse=True) # при сортировке кортежа возвращается список
print(id(tp_sort))
print(tp_sort)
print(type(tp_sort))
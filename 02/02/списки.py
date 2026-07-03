"""list  -упорядоченный набор объектов """
import copy

""""   0   1    2  3   4   """
# ls = [22, 33, 44, 55, 99]
"""   -5   -4   -3  -2  -1  """
# print(ls[4])
# print(ls[-1])
# print(id(ls))
# l1  = ls[:] #срез формирует отдельный
# l1 = ls.copy()
# print(id(l1))
# ls[1] = 333
# print(ls)
# print(l1)
# l = [2, '3', [22, 33]]
# # l1 = l #создается ссылка на тот же объект
# # l1 = l.copy() #поверхностное копирование
# l1 = copy.deepcopy(l) #копирует и вложения в списке с изменяем типом
# l[0] = 200
# l[-1][0] = 5520
# print(l)
# print(l1)
#
#
# print(ls[:3])
# ls[1] = 33
# print(ls[1:])
#
# ls = [22, 33, 44, 55, 99]
# print(ls[2::])
# print(ls[2::-1])
# print(ls[::-1])
# ls[1:3] = 220, 300 #можно добавить другой тип?
# print(ls)
#
# ls.append(100) #добавить значение в конец списка 0(1)
# print(ls)
# ls.insert(3, 200) #добавить по индексу 0(n)
#
# ls.extend([1,2]) #добавляет элементы в существующий список
# ls.extend([1,2]) #добавляет элементы в существующий список
#
# print(ls)
# n = ls.pop(3) #удалет объект по индексу
# print(n)
#
#
# l2 = [22, 33, 44, 55, 99, 'cat']
# print(l2)
# l2.('cat') #удаляем конктретный объектremove
# print(l2)
# ######################
# """list - упорядоченный набор объектов"""
# import copy
#
# """    0   1   2   3   4    """
# ls = [22, 33, 44, 55, 99]
# """   -5  -4  -3  -2  -1  """
#
# print(ls[4])
# print(ls[-1])
# print(id(ls))
# # l1 = ls[:]
# l1 = ls.copy()
# print(id(l1))
# ls[1] = 333
# print(ls)
# print(l1)
# # l = [2, '3', [22, 23]]
# # # l1 = l.copy()
# # l1 = copy.deepcopy(l)
# # l[0] = 200
# # l[-1][0] = 220
# # print(l)
# # print(l1)
# print(ls[:3])
# ls[1] = 33
# print(ls[1:])
# ls = [22, 33, 44, 55, 99]
# print(ls[2:])
# print(ls[2::-1])
# new = ls[::-1]
# print(new)
# ls[1:3] = 200, 300
# print(ls)

# ls.append(100)  # добавить в конец списка O(1)
# print(ls)
# ls.insert(3, 200)  # вставить по индексу O(n)
# print(ls)
# print(id(ls))
# ls.extend([100, 2])
# # ls += [1, 2]
# # ls = ls + [1, 2]
# print(id(ls))
#
# print(ls)
# n = ls.pop()
# nn = ls.pop(3)
# print(n, nn)
# while 100 in ls:
#     ls.remove(100)
# print(ls)

ls1 = [22, 33, 1, 44, 55, 99]
print(ls1)
ls1.append(100)
print(ls1.index(33))
ls1.reverse()
print(ls1)
ls1.sort()
print(ls1)


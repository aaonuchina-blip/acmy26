""" DICT - НЕУПОРЯДОЧЕННЫЙ НАБОР пар ключ:значений, в котором ключи уникальны"""

d = {}
d = {
    'Pb': 'Свинец',
    'Au': 'Золото'
    }
print(d)
print(d['Au'])
print(d['Pb'])
print(len(d))
print(d.get('Pb1')) #если нет ключа значения в  d получаем None
print(d.get('Pb1', 'my value'))

d['Pb'] = 'Свинец' #изменил значение в словаре
d[10] = 100 #добавили новый ключ со значением, так как ключ отсутсвует
print(d)

d.setdefault(10, 200) #добавляет пару только в случае отсутсвия ключа 10 в словаре d

value = d.setdefault(10, 200) #value получает значение по ключу 10:(100)
print(value)
d.setdefault(20, 200)
value = d.setdefault(20, 200) #добавляет пару только в случае отсутвия ключа
print(value)

# d.update({3:300, 10:10}) #создался новый ключ, а в уже существуюшем ключе обновили значение
# dd = d | {3:300, 10:10} #объединение словарей, в существующих ключах выбирает значение, которое указано вторым
print(d)
# print(dd)

n = d.pop(20) #убрали по ключу 20 значение. удаляется вся пара
print(n) #выводит значение удаленного ключа
print(d)
i = d.popitem() #удаляет последнюю добавленную или последнюю существующую пару
print(n, i)

ls = [22, 33, 44]
dd = dict.fromkeys(ls, 10000) #элеементы списка становятся ключами
dd = {i: i ** 2 for i in range(10,20)} #диткомпрехеншн
people = (('Mary', 22), ('Cherry', 26), ('Berry', 30))
dd = dict(people)
# print(dd)
#
# people = {
#     12030291929: {'name': 'Irina',
#                   'age': 24
#     },
#     123456678: {'name': 'Dasha',
#                   'age': 25
#     },
# }
#
# print(dd.keys())
#
# lst = [
#     {'name': 'Irina', 'inn': 12345,'age': 24},
#     {'name': 'Marina', 'inn': 123465, 'age': 25}
#
# ]

# print(dd.keys())
# print(list(dd)) #по умолчанию получаем ключи из словаря dd
# print(list(dd.values())) #по умолчанию получаем значения из словаря dd
# print(list(dd.items())) #по умолчанию получаем все из словаря dd в формате кортежа
#
# for i in dd: #получем только ключи
#     print(i, end='...')
# print()
#
# for i in dd.values(): #получем только значение
#     print(i, end='...')
# print()
#
# for i in dd.items(): #получем все из словаря
#     print(i, end='...')
# print()

s = 'aaaaaabaaaaaafaaaaaaaaaaaaaaaaacaaaaaaaaa'
symbols = {}
for i in s:
    # if i not in symbols:
    #     symbols[i] = 1
    # else:
    #     symbols[i] += 1
    symbols[i] = symbols.get(i, 0) +1
print(symbols

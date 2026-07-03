""" set - неупорядоченный нобор уникальных объектов"""

# st = {22, 33, 44, 44, 444}
# print(st)
# st.clear()
# print(st)
# st = set() #создание пустого множества
# ls = [22, 33, 44, 44]
# st = set(ls)
# print(st)
# st.add(1000)
# st.add((1000,))
# print(st)
# st.update([1, 2])
# print(st)
# n = st.pop()
# nn = st.pop()
# print(st, n, nn)
# st.remove(2)
# print(st)
# st.discard(22)
# print(st)
# st1 = {1, 2, 33}
# st2 = {1, 2, 44}
# res = st1.union(st2)
# res= st1 | st2
# print(res)
#
# res = st1.intersection(st2)
# print(res)
# res = st1 & st2
# print(res)
#
# res = st1.difference(st2)
# print(res)
# res = st2 - st1
# print(res)
#
# res = st1.symmetric_difference(st2)
# print(res)
#
# res = st1 ^ st2
# print(res)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
st3 = {1, 2}
# print(st1.issuperset(st3))
# print(st3.issubset(st2))
res = st1.difference(st2)
# print(res) #создается новый объект
# print(st1)
# print(st2)

# st1.difference_update(st2)
# print(st1)

# ice_cream = ['клубника', 'малина', 'банан', 'клубника']
# result = []
# for n in ice_cream:
#     if n not in result:
#         result.append(n)
# print(result)
# stt = set(ice_cream #чтобы сохранился обьект
# result = [n for n in set(ice_cream)]
# print(result)

a = 'I like pyton, it is very useful for data analysis'
b = 'pyton is the best tool for dealing with big data'
a = a.replace(',', '')
sta = set(a.split())
stb = set(b.split())
print(' '.join(list(stb - sta)))

la = a.split()
lb = b.split()
res1 = [w for w in lb if w not in sta ] #работает намного быстрее
print(res1)
res = []
for w in lb:
    if w not in la:
        res.append(w)
print(' '.join(res))
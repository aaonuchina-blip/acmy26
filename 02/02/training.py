# n1, n2 = input('>').split()
# n1, n2 = int(n1), int(n2)
# print(n1+n2)
#
# print(n := 345, n // 10, n % 10)

# print(next(n := map(int, input('>').split())) + next(n)) # присваиваем значение внутри функции, а потом им пользуемся. Моржевой оператор
# next  - генераторное значение
n = map(int, in3put('>').split())
print(next(n) + next(n))


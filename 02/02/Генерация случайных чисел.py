import random

import random
#
# nums = [22, 33, 44, 55, 66, 77, 88, 99]
# names = ['Dasha', 'Saahs', 'Glasha', 'Vera', 'Igor']
# print('Random - ', random.random())
# print('Uniform - ', random.uniform(0, 1)) # Вещественные числа
# print('Uniform - ', random.uniform(-10,-1))
#
# print('Randint - ', random.randint(9, 10))    #целое число включая 10
# print('Randrange - ', random.randrange(2, 100, 2)) # степ 2 - четное будет, а если 1 не четное
#
# print('Choice - ', random.choice(nums)) #
# print('Choice - ', random.choice(range(1, 11, 2))) #
# print('Choice - ', random.choice(names)) #
#
# print('Choices - ', random.choices(nums, k=20))
# print('Sample - ', random.sample(nums, 3))

# salary = [[60, 80, 70], [99, 102, 122],]
workers = 5
months = 3
salary = [random.choices(range(60, 151,5), k=months) for _ in range(workers)]
# for w in range(workers):
#     salary.append(random.choices(range(50, 150, 5), k=months))
# #     for m in range(months):
# #         salary[w].append(random.randint(50, 150))
# print(salary)
print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'* 22} {chr(2930)} {'-'*7} {chr(2930)}')
print(f'{chr(2930)} Работники {chr(2930)} ', end='')
for i in range(months):
    print(f'{i +1} Мес.', end=chr(2930) +  ' ')
print(f'Итого {chr(2930)} ')

itog = [0]* months
for k, i in enumerate(salary):
    print(f'{chr(2930)}  {k + 1} сотр.', end=chr(2930) + ' ')
    for n, j in enumerate(i):
        itog[n] +=1


        print(f'{j:4}', end=chr(2930) + ' ')
    print(f'{sum(i):6} {chr(2930)}')

# for i in range(2120, 2220):
#     print(f'{chr(i)} - {i}')



# list comprehention
# l = [22, 22, 44, 55, 77, 88]
# res = []
# for i in l:
#     if i % 2 == 0:
#         res.append(i ** 2)
#     print(res)
#
# res = [i ** 2 for i in l if i % 2 == 0]
# print(res)


# l = [22, 22, 44, 55, 77, 88, 200, 150]
# res = []
# for i in l:
#     if i % 2 == 0:
#         if i>= 55:
#             res.append(100)
#     else:
#         res.append(i ** 2)
#     print(res)
#
# res = [i ** 2 if i<55 else 100 for i in l if i % 2 == 0]
# print(res)
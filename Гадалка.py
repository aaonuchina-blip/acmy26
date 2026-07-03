# print('Привет, моя дорогая.')
# print('Меня зовут гадалка Марго.')
#
# n = input('Напиши как тебя зовут: ')
#
# print(f'Здравствуй, {n}.')
#
# n1 = int(input("Сколько тебе ле? Напиши: "))
# n1 = int
# print(f'Через год тебе будет {n1+1} ')

# name = input("Write your name: ")
# age = input('How old are you? Write:')
# print(f'Hello {name}! Your are {age} old.')

# fio = input("Введите ФИО: ")
#
# print(fio.replace(" ","\

# fio = input("Введите ФИО: ")
# f, i, o = fio.split()
# print(f"Фамилия: {f}")
# print(f"Имя: {i}")
# print(f"Отчество: {o}")

# fio = input("Введите ФИО: ")
# f, i, o = fio.split()
# s = f"| {f} | {i} | {o} |"
# print("-" * len(s))
# print(s)
# print("-" * len(s))

from tkinter import * # подключение модуля tkinter
root = Tk() # создание главного окна
btn = Button(root, text = ’Кнопочка’, width = 10, height=  2,
    bg=’white’, fg=’black’, font = ’Liberation␣14’) # создание кнопки
lab = Label(root, text=’Ваша фамилия:’,
    font=’Arial␣14’) # создание надписи
Edit = Entry (root, width=20) # создание поля ввода
btn.pack() # размещение кнопки на форме
lab.pack() # размещение надписи на форме
Edit.pack() # размещение поля ввода на форме
root.mainloop() # отображение главного окна
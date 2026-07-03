# from tkinter import *
# from tkinter import messagebox as mb
#
# okno = Tk()
# okno.title("Моя первая программа")
# m = Label(text = 'Моя первая программа',fg = 'DarkBlue', bg = 'LightBlue', height=3, width=20)
# m.pack()
# okno.geometry('500x250')
#
# okno.mainloop()

# import tkinter as tk
# from tkinter import *



#
# num1 = 0
# def add():
#     global num1
#     num1 = num1 + 1
#     l.config(text = f' {num1} ')
#
# def minus():
#     global num1
#     num1 = num1 - 1
#     l.config(text = f' {num1} ')
#
# def savebtn():
#     a = e.get()
#     e.delete(0, 'end')
#     l1.config(text=a)
#
# win = Tk()
# win.geometry("500x400")
# win.title('Моя первая программа')
#
# center = tk.Frame(win)
# center.pack()
#
# fr1 = Frame(center)
# fr1.pack(side=LEFT)
#
# fr2 = Frame(center)
# fr2.pack(side=RIGHT)
#
# l = tk.Label(fr1, text = f'{num1}', fg = 'DarkBlue', bg = 'LightBlue', height=3, width=40)
# l.pack(pady = 5)
#
# btn1 = tk.Button(fr2, text = '+1',width= 5, command=add)
# btn1.pack()
#
# btn2 = tk.Button(fr2, text = '-1',width=5, command=minus)
# btn2.pack()
#
# e = Entry(fr2, width= 10)
#
# e.pack()
#
# btn3 = tk.Button(fr2, text = 'Текст в Label', command=savebtn)
# btn3.pack()
#
# l1 =tk.Label(fr1, text = 'Моя вторая метка', fg = 'DarkBlue', bg = 'LightBlue', height=3, width=40)
# l1.pack(pady = 5)
# l2 =tk.Label(fr1, text = 'Моя третья метка', fg = 'Red', bg = 'Pink', height=3, width=40)
# l2.pack(pady = 5)
# win.mainloop()

# win = Tk()
# win.geometry("500x400")
# win.title('Анкета')
#
# def show():
#     name = e.get()
#     age = int(e1.get())
#
#     if age % 10 == 1 and age != 11:
#         word = 'год'
#     elif (age % 10 == 2 and age != 12) or (age % 10 == 3 and age != 13) or (age % 10 == 4 and age != 14):
#         word = 'года'
#     else:
#         word = 'лет'
#     l3.config(text=f'Привет, {name}!\n Ну где ты был, ну обними меня скорей!\n Тебе {age} {word}.')
#
#
# center = tk.Frame()
# center.pack()
#
# l1 = tk.Label(center,text="Имя:")
# l1.pack()
#
# e = tk.Entry(center, width=30)
# e.pack()
#
# l2 = tk.Label(center, text="Возраст:")
# l2.pack()
#
# l3 = tk.Label()
# l3.pack()
#
# e1 = tk.Entry(center, width=30)
# e1.pack()
#
# btn = tk.Button(center, text="Показать", command=show)
# btn.config(pady = 5)
# btn.pack(pady= 10)
# win.mainloop()
#
# import tkinter as tk
# from tkinter import *
# win = Tk()
# win.geometry("500x400")
#
# def clean():
#     # e.delete(1.0, tk.END)
#     print(e.get(1.0, 1.5) # срез текста с первой строки с нулевого ао 5й символ
# def add_text():
#     # n = "Hello World "
#     # e.insert(1.0, n)
#     e.insert(tk.END, "Hellow World!")
#
# e = tk.Text(win, width=40, height=5)
# e.pack()
#
# btn=tk.Button(text='Очистить', command=clean)
# btn.pack()
#
# btn2=tk.Button(text='Вставляет текст', command=add_text)
# btn2.pack()
#
# win.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

win = Tk()
win.geometry("500x400")
win.title('Приветствие')

def show():
    name = e.get()
    if not name.lstrip('-'):
        mb.showerror("Ошибка", "Введите имя")
        return
    l.config(text=f'Привет, {name}!')

center = tk.Frame()
center.pack()

l = tk.Label(center,text="")
l.pack()

e = tk.Entry(center, width=30)
e.pack()

btn = tk.Button(center, text="Приветствие", command=show)
btn.config(pady = 5)
btn.pack(pady= 10)
win.mainloop()
